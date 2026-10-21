"""Extract official sample input/output pairs from HackerRank statements."""
import re

HEAD = re.compile(r"^\s*(?:\*\*|__)?\s*Sample\s+(Input|Output)\s*(\d*)\s*:?\s*(?:\*\*|__)?\s*:?\s*$", re.I)

def _block(lines, i):
    """Return the text block starting at/after line i (code fence or indented/tab block)."""
    n = len(lines)
    while i < n and not lines[i].strip():
        i += 1
    if i < n and lines[i].strip().startswith("```"):
        j = i + 1
        out = []
        while j < n and not lines[j].strip().startswith("```"):
            out.append(lines[j]); j += 1
        return "\n".join(out)
    out = []
    while i < n:
        l = lines[i]
        if HEAD.match(l) or re.match(r"^\s*(\*\*|__)", l) or (l and not l[0] in " \t" and l.strip()):
            break
        out.append(l)
        i += 1
    while out and not out[-1].strip():
        out.pop()
    # strip one level of indentation (tab or 4 spaces) per line
    return "\n".join(re.sub(r"^(\t| {4}| {2}\t|\t)", "", l) for l in out)

def parse(statement):
    lines = statement.replace("\r", "").split("\n")
    ins, outs = {}, {}
    for i, l in enumerate(lines):
        m = HEAD.match(l)
        if m:
            kind, idx = m.group(1).lower(), m.group(2) or "0"
            (ins if kind == "input" else outs)[idx] = _block(lines, i + 1)
    pairs = []
    for k in sorted(set(ins) | set(outs)):
        pairs.append((ins.get(k), outs.get(k)))
    return pairs
