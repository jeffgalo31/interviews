# Agentic AI: Guarded Data Assistant

**Type:** Supplemental original exercise
**Source:** [OpenAI function calling guide](https://developers.openai.com/api/docs/guides/function-calling)
**Focus:** tool use, bounded agent loops, authorization, validation, human approval, auditability

## Exercise

A GenAI assistant may answer questions about data-ingestion jobs. It can read a job status and request a retry. Design the tool boundary so the model cannot run arbitrary SQL, choose arbitrary functions, access another user's jobs, or perform a retry without authorization and approval.

Example requests and expected outcomes:

| Actor/request | Expected result |
|---|---|
| Authorized user asks `get_job_status` for `job-42` | Return only that user's permitted status fields. |
| Model requests `retry_job` for `job-42` without user confirmation | Return `approval_required`; do not call the retry handler. |
| User approves retry through the application UI | Server verifies the approval and authorization, then invokes the retry handler once. |
| Model requests an undeclared `run_sql` tool | Reject the tool name; execute nothing. |
| User requests another tenant's job | The handler denies access, even if the model supplies a valid job ID. |

## Solution

Keep policy enforcement in application code, not in the prompt. Treat model-generated tool calls as untrusted input. This dispatcher illustrates an allowlist and an explicit approval gate; the callback implementations must enforce tenant-level authorization in the service layer as well. Set `server_verified_approval` only from an authenticated approval record, never from model-generated arguments.

```python
from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class Tool:
    handler: Callable[..., Any]
    required_arguments: frozenset[str]
    read_only: bool


class ToolError(ValueError):
    pass


def build_tools(get_job_status, retry_job):
    return {
        "get_job_status": Tool(
            handler=get_job_status,
            required_arguments=frozenset({"job_id"}),
            read_only=True,
        ),
        "retry_job": Tool(
            handler=retry_job,
            required_arguments=frozenset({"job_id"}),
            read_only=False,
        ),
    }


def execute_tool_call(name, arguments, tools, actor, server_verified_approval=False):
    tool = tools.get(name)
    if tool is None:
        raise ToolError("Tool is not available")

    if not isinstance(arguments, dict) or set(arguments) != tool.required_arguments:
        raise ToolError("Invalid tool arguments")

    job_id = arguments["job_id"]
    if not isinstance(job_id, str) or not job_id.strip():
        raise ToolError("job_id must be a non-empty string")

    if not tool.read_only and not server_verified_approval:
        return {"status": "approval_required", "action": name}

    result = tool.handler(actor=actor, job_id=job_id)
    return {"status": "ok", "data": result}
```

The model receives only the two declared tool schemas. The application should also:

- Enforce user authorization inside each handler and return only fields the user may see.
- Require explicit user confirmation for retries; model confidence is not approval.
- Bound tool-call count and execution time, validate output size, and treat tool results as untrusted data.
- Log actor, tool name, decision, and correlation ID without logging secrets or unnecessary sensitive data.
- Return a safe fallback when the model, tool, or downstream service fails; never expose stack traces or raw prompts to clients.

**Architecture point:** The LLM proposes a tool call; deterministic application code validates, authorizes, executes, and records it. The model is not the security boundary.
