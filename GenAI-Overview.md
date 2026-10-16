# Gen AI & Agentic Patterns Interview Cheat Sheet

*LLMs · Prompt Engineering · RAG · Agents · Tool Use · MCP · Evaluation · Guardrails*

**Jump to:** [All Topics](All-Topics-Overview.md) · [AWS](AWS-Overview.md) · [Data](Data-Overview.md) · [Spring Boot](Frameworks-Overview.md) · [DevOps](DevOps-Overview.md) · [Practices](Practices-Overview.md) · **Gen AI**

> [!TIP]
> Click any question to expand the answer. Try answering out loud first.

<details>
<summary><b>📑 Table of contents</b></summary>

1. [🧭 Quick Overview](#-quick-overview)
2. [🧠 1. LLM Fundamentals](#-1-llm-fundamentals)
3. [✍ 2. Prompt Engineering](#-2-prompt-engineering)
4. [📚 3. RAG (Retrieval-Augmented Generation)](#-3-rag-retrieval-augmented-generation)
5. [🤖 4. Agents & Agentic Patterns](#-4-agents--agentic-patterns)
6. [📊 5. Evaluation, Guardrails & Production](#-5-evaluation-guardrails--production)
7. [🧩 Cross-Topic / Scenario Questions](#-cross-topic--scenario-questions)
8. [🎯 Core Concepts to Know Cold](#-core-concepts-to-know-cold)

</details>

---

## 🧭 Quick Overview

| Topic | What it is | Use it for |
|---|---|---|
| **LLM** | Transformer model that predicts the next token | Text generation, reasoning, code, summarization |
| **Prompt engineering** | Crafting instructions, context, and examples | Steering model output without training |
| **Embeddings + Vector DB** | Numeric vectors capturing meaning; similarity search | Semantic search, RAG retrieval |
| **RAG** | Retrieve relevant docs, add to prompt, then generate | Grounded answers on private/fresh data |
| **Fine-tuning** | Further training on domain data | Style, format, specialized behavior |
| **Tool / function calling** | Model emits structured calls to external functions | Actions, APIs, DB queries |
| **Agent** | LLM in a loop that plans, calls tools, observes, repeats | Multi-step, open-ended tasks |
| **MCP** | Open protocol for connecting models to tools/data | Standard tool/context integration |
| **Guardrails & evals** | Safety checks and quality measurement | Reliable, safe production systems |

**Typical architecture:** User → app/API → orchestrator (prompt + context) → LLM ⇄ tools / retrieval (vector DB, APIs) → guardrails/validation → response; with logging, evals, and cost tracking around it.

---

## 🧠 1. LLM Fundamentals

#### 📌 Key points
- Based on the **Transformer** (self-attention); trained to predict the next **token**.
- Lifecycle: pre-training → instruction tuning / fine-tuning → alignment (RLHF and similar).
- **Context window:** max tokens (input + output) the model can attend to.
- Key parameters: **temperature** (randomness), **top-p**, **max tokens**, stop sequences.
- Limitations: **hallucination**, knowledge cutoff, non-determinism, context limits, prompt injection risk.
- Cost and latency scale with tokens; streaming improves perceived latency.

#### ❓ Questions
<details>
<summary><b>1. How do LLMs work at a high level?</b></summary>

Text → tokens → embeddings → transformer layers with attention → probability distribution over the next token, sampled repeatedly.

</details>

<details>
<summary><b>2. What are tokens and why do they matter?</b></summary>

Sub-word units; they determine cost, latency, and context limits.

</details>

<details>
<summary><b>3. What does temperature do?</b></summary>

Low = focused/deterministic; high = diverse/creative. Use low for extraction and code.

</details>

<details>
<summary><b>4. What is hallucination and how do you reduce it?</b></summary>

Confident but false output. Reduce with RAG/grounding, citations, lower temperature, constraints, verification, and "say you don't know" instructions.

</details>

<details>
<summary><b>5. What is the context window? What if the data exceeds it?</b></summary>

Chunk, summarize, retrieve (RAG), or use long-context models.

</details>

<details>
<summary><b>6. Base vs instruction-tuned models?</b></summary>

Base completes text; instruction-tuned follows directions and chats.

</details>

<details>
<summary><b>7. Prompt caching and why use it?</b></summary>

Reuse the processed prefix (system prompt, docs) to cut cost and latency.

</details>

<details>
<summary><b>8. How do you choose a model?</b></summary>

Quality, latency, cost, context size, modality, data privacy, tool-use ability; use smaller models for simple tasks, larger for reasoning.

</details>

<details>
<summary><b>9. Why is output non-deterministic?</b></summary>

Sampling; even at temperature 0, minor variation can occur, so design tests accordingly.

</details>

---

## ✍ 2. Prompt Engineering

#### 📌 Key points
- Structure: **role/system prompt, task, context, constraints, examples, output format**.
- Techniques: zero-shot, few-shot, **chain-of-thought / step-by-step reasoning**, role prompting, delimiters (XML/JSON tags), prompt chaining, self-consistency.
- Structured output: JSON schema / tool use / constrained decoding, then validate.
- Treat prompts as code: version them, test them, review them.

#### ❓ Questions
<details>
<summary><b>1. Zero-shot vs few-shot?</b></summary>

Zero-shot: instructions only. Few-shot: include examples to show format and behavior.

</details>

<details>
<summary><b>2. What is chain-of-thought?</b></summary>

Having the model reason step by step before answering to improve complex reasoning.

</details>

<details>
<summary><b>3. How do you get reliable structured output?</b></summary>

Provide a schema, use structured outputs/tool calling, validate and retry on parse failure.

</details>

<details>
<summary><b>4. System vs user prompt?</b></summary>

System sets persistent role, rules, and constraints; user carries the task and input.

</details>

<details>
<summary><b>5. How do you make a prompt robust?</b></summary>

Be specific, give examples, define edge cases and format, separate instructions from data, iterate against a test set.

</details>

<details>
<summary><b>6. What is prompt injection?</b></summary>

Untrusted input that overrides instructions (direct or hidden in retrieved docs). Mitigate with input isolation, least-privilege tools, output validation, and human approval for risky actions.

</details>

<details>
<summary><b>7. How do you handle long prompts?</b></summary>

Put key instructions clearly, structure with tags, retrieve only relevant context, use caching.

</details>

<details>
<summary><b>8. How do you evaluate prompt changes?</b></summary>

Run a fixed eval set before and after, compare metrics, avoid judging on a few examples.

</details>

---

## 📚 3. RAG (Retrieval-Augmented Generation)

#### 📌 Key points
- Pipeline: **ingest → chunk → embed → store in vector DB → retrieve (top-k) → augment prompt → generate (with citations)**.
- **Embeddings:** vectors where semantically similar text is close (cosine similarity).
- Vector stores: pgvector, OpenSearch, Pinecone, Weaviate, Chroma, Bedrock Knowledge Bases.
- Improvements: **hybrid search** (BM25 + vector), **reranking**, metadata filters, query rewriting, parent-child chunking.
- RAG vs fine-tuning: RAG for fresh/private knowledge; fine-tuning for style/behavior.

#### ❓ Questions
<details>
<summary><b>1. What is RAG and why use it?</b></summary>

Retrieve relevant documents at query time and pass them to the LLM, giving grounded, up-to-date answers with source attribution and no retraining.

</details>

<details>
<summary><b>2. RAG vs fine-tuning?</b></summary>

RAG: dynamic knowledge, cheaper to update, traceable. Fine-tuning: teaches behavior/format/style, not reliable for facts.

</details>

<details>
<summary><b>3. How do you chunk documents?</b></summary>

By semantic or structural boundaries with overlap; sized to balance context and precision (e.g., 200-800 tokens). Bad chunking is a top failure cause.

</details>

<details>
<summary><b>4. How do you improve retrieval quality?</b></summary>

Hybrid search, reranker, metadata filters, query expansion, better embeddings, tuned top-k.

</details>

<details>
<summary><b>5. How do you evaluate RAG?</b></summary>

Retrieval metrics (recall@k, precision, MRR) and generation metrics (faithfulness, answer relevance, groundedness), e.g., RAGAS.

</details>

<details>
<summary><b>6. What if retrieval returns nothing relevant?</b></summary>

Detect low similarity, respond "I don't know" or fall back; don't force an answer.

</details>

<details>
<summary><b>7. How do you handle access control in RAG?</b></summary>

Filter by user permissions at retrieval time using metadata; never expose documents the user can't see.

</details>

<details>
<summary><b>8. How do you keep the index fresh?</b></summary>

Incremental ingestion pipelines, CDC/events, re-embedding on updates, deleting stale chunks.

</details>

<details>
<summary><b>9. What's a vector DB and how does search work?</b></summary>

Stores embeddings; uses approximate nearest neighbor indexes (HNSW, IVF) for fast similarity search.

</details>

<details>
<summary><b>10. Common failure modes?</b></summary>

Poor chunking, irrelevant retrieval, context stuffing, stale data, missing citations, prompt injection from documents.

</details>

---

## 🤖 4. Agents & Agentic Patterns

#### 📌 Key points
- **Agent** = LLM + tools + memory + loop (reason → act → observe) that works toward a goal.
- **Workflow vs agent:** workflows follow predefined code paths; agents decide their own steps dynamically. Prefer the simplest approach that works.
- **Common patterns:**
  - **Prompt chaining:** sequential LLM steps with checks.
  - **Routing:** classify input and send it to a specialized path.
  - **Parallelization:** run subtasks or multiple votes concurrently.
  - **Orchestrator-workers:** a lead agent delegates to sub-agents.
  - **Evaluator-optimizer:** generate, critique, refine loop.
  - **ReAct:** interleave reasoning with tool actions.
  - **Plan-and-execute:** plan first, then execute steps.
  - **Reflection:** the model reviews and improves its own output.
- **Multi-agent systems:** specialized agents (researcher, coder, reviewer) coordinating; adds complexity and cost.
- **Memory:** short-term (context), long-term (vector/DB), working scratchpad; summarize to manage context.
- **Human-in-the-loop** for high-risk actions.

#### ❓ Questions
<details>
<summary><b>1. What is an agent vs a simple LLM call?</b></summary>

An LLM call is one-shot. An agent loops: decides actions, calls tools, observes results, and continues until done.

</details>

<details>
<summary><b>2. Workflow vs agent: when to use which?</b></summary>

Workflows for predictable, well-defined tasks (cheaper, reliable). Agents for open-ended tasks where steps can't be predetermined.

</details>

<details>
<summary><b>3. Explain ReAct.</b></summary>

The model alternates thought → action (tool call) → observation until it can answer.

</details>

<details>
<summary><b>4. How does tool/function calling work?</b></summary>

You describe tools with JSON schemas; the model returns a structured call; your code executes it and returns the result for the next turn.

</details>

<details>
<summary><b>5. What is MCP (Model Context Protocol)?</b></summary>

An open standard for exposing tools, resources, and prompts to AI apps through a client-server protocol, so integrations are reusable across models and apps.

</details>

<details>
<summary><b>6. How do you design good tools?</b></summary>

Clear names/descriptions, narrow single-purpose functions, typed inputs, helpful error messages, idempotency, least privilege.

</details>

<details>
<summary><b>7. How do you stop an agent from looping or running away?</b></summary>

Max iterations/steps, token and time budgets, termination criteria, loop detection, human approval gates.

</details>

<details>
<summary><b>8. How do you manage agent memory?</b></summary>

Context trimming and summarization, retrieval from a vector store for long-term memory, structured state outside the prompt.

</details>

<details>
<summary><b>9. Single agent vs multi-agent?</b></summary>

Start single. Use multi-agent when tasks are parallelizable or need distinct roles/context isolation, accepting more cost, latency, and coordination complexity.

</details>

<details>
<summary><b>10. How do you handle tool failures?</b></summary>

Return clear errors to the model, retry with backoff, fall back, or escalate to a human.

</details>

<details>
<summary><b>11. How do you keep agents safe?</b></summary>

Least-privilege credentials, sandboxed execution, allowlisted tools, confirmation for destructive actions, audit logs, prompt injection defenses.

</details>

<details>
<summary><b>12. How do you debug an agent?</b></summary>

Trace every step (prompts, tool calls, outputs) with observability tools (LangSmith, OpenTelemetry), replay failures, add them to evals.

</details>

<details>
<summary><b>13. Frameworks?</b></summary>

LangChain/LangGraph, LlamaIndex, Claude Agent SDK, AutoGen, CrewAI, AWS Bedrock Agents/Strands; or plain SDK calls for simple cases.

</details>

---

## 📊 5. Evaluation, Guardrails & Production

#### 📌 Key points
- **Evals:** golden datasets, automated metrics, **LLM-as-judge**, human review, regression suites in CI.
- **Guardrails:** input/output filters, PII redaction, content moderation, schema validation, topic restrictions, grounding checks.
- **Observability:** logging prompts/responses, latency, token usage, cost, error rates, user feedback.
- **Cost/latency levers:** smaller models, caching, batching, streaming, shorter prompts, routing by difficulty.
- **Governance:** data privacy, no training on sensitive data, auditability, bias and fairness, compliance.

#### ❓ Questions
<details>
<summary><b>1. How do you evaluate an LLM application?</b></summary>

Build a representative test set, define metrics (accuracy, faithfulness, format validity, safety), run automated and LLM-judge scoring plus human spot checks, and track regressions.

</details>

<details>
<summary><b>2. What is LLM-as-judge and its pitfalls?</b></summary>

Using a model to grade outputs. Pitfalls: bias toward verbose or its own style, inconsistency; calibrate against human labels.

</details>

<details>
<summary><b>3. What guardrails would you add?</b></summary>

Input validation, PII redaction, moderation, output schema validation, groundedness checks, rate limits, human review for sensitive actions.

</details>

<details>
<summary><b>4. How do you reduce cost and latency?</b></summary>

Right-size models, prompt caching, shorter context via retrieval, batching, streaming, model routing, caching frequent answers.

</details>

<details>
<summary><b>5. How do you handle sensitive data?</b></summary>

Redact or mask PII, use private endpoints/VPC, enterprise data-retention terms, access controls, encryption, audit logging.

</details>

<details>
<summary><b>6. How do you monitor in production?</b></summary>

Trace requests, track quality via feedback and sampled evals, alert on error/latency/cost spikes, watch for drift.

</details>

<details>
<summary><b>7. Reliability issues to plan for?</b></summary>

Rate limits, timeouts, malformed output, model/version changes; use retries, fallbacks, validation, and pinned model versions.

</details>

<details>
<summary><b>8. Responsible AI concerns?</b></summary>

Bias, misinformation, privacy, transparency, misuse; address with testing, guardrails, disclosure, and human oversight.

</details>

---

## 🧩 Cross-Topic / Scenario Questions

<details>
<summary><b>1. Build a chatbot over company documents.</b></summary>

Ingest and chunk docs → embeddings in a vector DB with access metadata → hybrid retrieval + rerank → prompt with citations → guardrails → evals and feedback loop.

</details>

<details>
<summary><b>2. Design a customer-support agent.</b></summary>

Tools: order lookup, refund (with approval), KB search; routing for intent; escalation to human; audit logs; evals on real transcripts.

</details>

<details>
<summary><b>3. How would you add Gen AI to an existing Spring Boot / AWS app?</b></summary>

Wrap the model API (e.g., Bedrock or Anthropic API) in a service behind existing auth; RAG using pgvector/OpenSearch; stream responses; secrets in Secrets Manager; monitor tokens and cost.

</details>

<details>
<summary><b>4. Agent gives wrong answers sometimes. What do you do?</b></summary>

Trace failures, categorize errors, improve prompts/tools/retrieval, add validation and evals, then constrain the workflow if needed.

</details>

<details>
<summary><b>5. When should you NOT use an LLM?</b></summary>

Deterministic logic, strict correctness, simple rules, low-latency/low-cost needs, or where errors are unacceptable without verification.

</details>

<details>
<summary><b>6. How do you apply TDD and CI/CD to Gen AI?</b></summary>

Eval suites as tests, prompts under version control, regression gates in CI, canary rollouts for prompt/model changes.

</details>

<details>
<summary><b>7. How do you prevent data leakage / prompt injection in an agent?</b></summary>

Least privilege, isolate untrusted content, validate tool arguments, confirm risky actions, restrict egress.

</details>

---

## 🎯 Core Concepts to Know Cold

- **Tokens, context window, temperature, hallucination.**
- **Prompting:** few-shot, chain-of-thought, structured output, prompt injection.
- **RAG pipeline** (chunk, embed, retrieve, rerank, generate) and RAG vs fine-tuning.
- **Agent loop,** tool calling, ReAct, workflow vs agent, orchestrator-workers, MCP.
- **Evals and guardrails** as the core of production readiness.
- **Safety:** least privilege, human-in-the-loop, sandboxing, auditing.
- **Tradeoffs:** quality vs latency vs cost; simplest solution that works.

---

**Jump to:** [All Topics](All-Topics-Overview.md) · [AWS](AWS-Overview.md) · [Data](Data-Overview.md) · [Spring Boot](Frameworks-Overview.md) · [DevOps](DevOps-Overview.md) · [Practices](Practices-Overview.md) · **Gen AI**
