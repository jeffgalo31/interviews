#!/usr/bin/env python3
"""Generate the HackerRank Java track exercises and test them against the official samples.

usage: jgen.py <challenges.json> <out_dir>      (out_dir gets src/<section>/<exercise>/... and README.md)
"""
import json, os, re, shutil, subprocess, sys, tempfile, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import samples as sample_parser
from solutions import S, YC, END
from jtext import IMG, EXPLAIN, FIX

SRC, OUT = sys.argv[1], sys.argv[2]
CH = json.load(open(SRC))
EXISTING = {"java-regex": "strings/java_regex", "java-dequeue": "data_structures/java_dequeue"}

def under(name):
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", name.lower())).strip("_")

def section_dir(sub):
    return under(sub)

# ------------------------------------------------------------------------------------------- statement
IMG_RE = re.compile(r'!\[[^\]]*\]\((https://s3\.amazonaws\.com/([^)\s]+))\)|<img[^>]*src="(https://s3\.amazonaws\.com/([^"]+))"[^>]*/?>')
EXPL_RE = re.compile(r"\n\s*(?:\*\*|__)Explanation\s*\d*\s*(?:\*\*|__)\s*(?:\n|$)")
NEXT_RE = re.compile(r"\n\s*(?:\*\*|__)Sample (?:Input|Output)")

def statement(slug, s):
    s = s.replace("\r", "")
    for old, new in FIX.get(slug, []):
        assert old in s, (slug, old[:60])
        s = s.replace(old, new, 1)
    if slug in EXPLAIN:
        m = EXPL_RE.search(s)
        assert m, slug
        nxt = NEXT_RE.search(s, m.end())
        rest = s[nxt.start():] if nxt else ""
        s = s[:m.start()] + "\n\n**Explanation**\n\n" + EXPLAIN[slug] + "\n\n> Numbers that appear as formulas on HackerRank are filled in here.\n" + rest
    def repl(m):
        key = m.group(2) or m.group(4)
        if key not in IMG:
            raise KeyError("no transcription for image " + key)
        return "\n\n" + IMG[key] + "\n\n"
    s = IMG_RE.sub(repl, s)
    s = re.sub(r"[ \t]+\n", "\n", s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()

# ------------------------------------------------------------------------------------------- java source helpers
def top_level_items(src):
    """Split Java source into top-level items: ('stmt', text) for package/import, ('type', text), ('trail', text)."""
    items, buf, depth, i, n = [], [], 0, 0, len(src)
    while i < n:
        c = src[i]
        two = src[i:i + 2]
        if two == "//":
            j = src.find("\n", i); j = n if j < 0 else j
            buf.append(src[i:j]); i = j; continue
        if two == "/*":
            j = src.find("*/", i + 2); j = n if j < 0 else j + 2
            buf.append(src[i:j]); i = j; continue
        if src.startswith('"""', i):
            j = src.find('"""', i + 3) + 3
            buf.append(src[i:j]); i = j; continue
        if c in "\"'":
            j = i + 1
            while j < n and src[j] != c:
                j += 2 if src[j] == "\\" else 1
            buf.append(src[i:j + 1]); i = j + 1; continue
        buf.append(c)
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                items.append(["type", "".join(buf)]); buf = []
        elif c == ";" and depth == 0:
            items.append(["stmt", "".join(buf)]); buf = []
        i += 1
    if "".join(buf).strip():
        items.append(["trail", "".join(buf)])
    return items

DECL_RE = re.compile(r"\b(public\s+)?((?:abstract\s+|final\s+|static\s+)*)(class|interface|enum|@interface)\s+(\w+)")

def decl(text):
    body_start = text.find("{")
    # skip annotations/comments: search for the declaration before the first brace
    m = None
    for m2 in DECL_RE.finditer(text[:body_start]):
        m = m2
    return m

def java_string(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'

def strip_markers_at_depth0(text):
    return re.sub(r"(?m)^[ \t]*// ---- (your code|end of your code) ----[ \t]*\n", "", text)

def make_local(e, pkg, header, sample_input):
    src = e["hr"]
    for old, new in e["local"]:
        assert old in src, (pkg, old)
        src = src.replace(old, new)
    if e["extra"]:
        src = src.rstrip("\n") + "\n" + e["extra"]
    src = src.replace('new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));',
                      "new BufferedWriter(new OutputStreamWriter(System.out));   // HackerRank writes to a file (OUTPUT_PATH)")
    src = re.sub(r"(?m)^(\s*)((?:Do_Not_Terminate|DoNotTerminate)\.forbidExit\(\);)",
                 r"\1// \2   // HackerRank-only guard (uses SecurityManager, disabled in newer Java)", src)

    items = top_level_items(src)
    types = [it for it in items if it[0] == "type"]
    mains = [it for it in types if "static void main(" in it[1]]
    assert len(mains) == 1, (pkg, len(mains))
    main = mains[0]
    reordered = types[0] is not main
    stmts = [it for it in items if it[0] == "stmt"]
    rest = [it for it in types if it is not main]
    trail = [it for it in items if it[0] == "trail"]

    # only Solution may stay public (file name); main class first so `java Solution.java` runs it
    for it in types:
        m = decl(it[1])
        if m and m.group(1) and m.group(4) != "Solution":
            it[1] = it[1][:m.start(1)] + it[1][m.end(1):]
    main_name = decl(main[1]).group(4)

    if sample_input is not None:
        inject = ("\n    // ---- local only: with no piped input, use HackerRank's sample input ----\n"
                  f"    private static final String SAMPLE_INPUT = {java_string(sample_input.rstrip(chr(10)) + chr(10))};\n"
                  "    static {\n"
                  "        try {\n"
                  "            if (System.in.available() == 0) {\n"
                  "                System.setIn(new java.io.ByteArrayInputStream(SAMPLE_INPUT.getBytes()));\n"
                  "            }\n"
                  "        } catch (java.io.IOException e) {\n"
                  "            // keep reading the real input\n"
                  "        }\n"
                  "    }\n")
        b = main[1].find("{")
        main[1] = main[1][:b + 1] + inject + main[1][b + 1:]

    parts = [it[1] for it in stmts]
    body_types = [main] + rest if reordered else types
    type_text = "".join(it[1] for it in body_types) + "".join(it[1] for it in trail)
    if reordered:
        type_text = strip_markers_at_depth0(type_text)
    out = header + f"package {pkg};\n" + "".join(parts).rstrip("\n").lstrip("\n").join(["\n", "\n"]) + type_text.lstrip("\n")
    return out, main_name, reordered

def your_code(hr):
    blocks = re.findall(r"// ---- your code ----[^\n]*\n(.*?)\n[ \t]*// ---- end of your code ----", hr, re.S)
    if not blocks:
        return hr.strip()
    return "\n    // ...\n".join(textwrap.dedent(b).rstrip() for b in blocks)

def md_to_comment(t):
    return re.sub(r"\*\*|`", "", t)

# ------------------------------------------------------------------------------------------- generate
os.makedirs(OUT, exist_ok=True)
built = []
for c in CH:
    slug = c["slug"]
    sec = section_dir(c["subdomain"])
    if slug in EXISTING:
        built.append(dict(c=c, rel=EXISTING[slug], existing=True))
        continue
    e = S[slug]
    pkg_last = under(c["name"])
    rel = f"{sec}/{pkg_last}"
    pkg = f"{sec}.{pkg_last}"
    d = os.path.join(OUT, "src", sec, pkg_last)
    os.makedirs(d, exist_ok=True)

    stmt = statement(slug, c["statement"])
    pairs = e["samples"] or [(a, b) for a, b in sample_parser.parse(stmt) if b is not None]
    sample_input = next((a for a, b in pairs if a), None)

    run_hint = f"java src/{rel}/Solution.java"
    lines = [f"// {c['name']}  ({c['difficulty']} · {c['subdomain']})  {c['url']}",
             "// Description and explanation: README.md (same folder).",
             "//",
             "// RUNNABLE LOCAL VERSION: click Run above main() in VS Code, or from the java folder run",
             f"//   {run_hint}"]
    if sample_input is not None:
        lines += ["// With no input piped in it uses HackerRank's sample input (SAMPLE_INPUT below).",
                  f"// Your own input:  printf '...' | {run_hint}"]
    lines += ["// HackerRank copy: Solution_hackerrank.java (HackerRank's exact code, no package line;",
              "//   the part you write is between the \"your code\" markers)."]
    header = "\n".join(lines) + "\n//\n// How it works:\n" + "\n".join("// - " + md_to_comment(n) for n in e["notes"]) + "\n"
    local, main_name, reordered = make_local(e, pkg, header, sample_input)
    if reordered:
        local = local.replace("// How it works:", "// Locally the class with main() comes first (so this single file can run);\n"
                              "// HackerRank's order and the exact part you write are in Solution_hackerrank.java.\n//\n// How it works:", 1)
    open(os.path.join(d, "Solution.java"), "w").write(local)

    hr_header = (f"// HackerRank submission copy: {c['name']} ({c['difficulty']} · {c['subdomain']}).\n"
                 "// Paste the whole file; if HackerRank shows part of the code as locked, paste only the\n"
                 "// lines between \"// ---- your code ----\" and \"// ---- end of your code ----\".\n"
                 "// Explained, runnable version: Solution.java\n")
    open(os.path.join(d, "Solution_hackerrank.java"), "w").write(hr_header + e["hr"])

    readme = [f"# {c['name']}", "",
              f"**Difficulty:** {c['difficulty']} · **Section:** {c['subdomain']} · **Track:** HackerRank Java · [Open on HackerRank]({c['url']})", "",
              "---", "", stmt, "", "## Solution", "", "The part you write:", "", "```java", your_code(e["hr"]), "```", ""]
    readme += [f"- {n}" for n in e["notes"]]
    readme += ["", "**Files**", "",
               f"- [Solution.java](Solution.java): runnable and commented. In VS Code click **Run** above `main`, or `{run_hint}` from the `java` folder"
               + (" (with no input it uses the sample input)." if sample_input is not None else "."),
               "- [Solution_hackerrank.java](Solution_hackerrank.java): HackerRank's exact program with the solution filled in. "
               "If HackerRank shows part of the code as locked, paste only the lines between the `// ---- your code ----` markers.", ""]
    open(os.path.join(d, "README.md"), "w").write("\n".join(readme))
    built.append(dict(c=c, rel=rel, pkg=pkg, main=main_name, pairs=pairs, e=e, dir=d, sample_input=sample_input))

# ------------------------------------------------------------------------------------------- test
def norm(t, pkg=None):
    if pkg:
        t = t.replace(pkg + ".", "")
    lines = [l.rstrip() for l in t.replace("\r", "").split("\n")]
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)

def run(cmd, inp, cwd=None):
    env = {k: v for k, v in os.environ.items() if k != "JAVA_TOOL_OPTIONS"}
    p = subprocess.run(cmd, input=inp, capture_output=True, text=True, timeout=60, cwd=cwd, env=env)
    return p.returncode, p.stdout, p.stderr

work = tempfile.mkdtemp()
classes = os.path.join(work, "classes"); os.makedirs(classes)
results = []
for b in built:
    if b.get("existing"):
        continue
    slug = b["c"]["slug"]
    rc, _, err = run(["javac", "-nowarn", "-Xlint:none", "-d", classes, os.path.join(b["dir"], "Solution.java")], "")
    if rc:
        results.append((slug, "COMPILE-ERROR", err.strip().splitlines()[:3])); continue
    status, detail = "PASS", ""
    for k, (inp, exp) in enumerate(b["pairs"]):
        rc, out, err = run(["java", "-cp", classes, b["pkg"] + "." + b["main"]], inp + "\n" if inp else "")
        got, want = norm(out, b["pkg"] if b["e"]["strip_pkg"] else None), norm(exp or "")
        if b["e"]["compare"] == "currency":
            status, detail = "CHECK", "currency symbols depend on the Java version: " + got.replace("\n", " | ")
            continue
        if got != want:
            status, detail = "FAIL", f"sample {k}: got {got[:200]!r} want {want[:200]!r} {err.strip()[:200]}"
            break
    if status == "PASS" and b["sample_input"] is not None:                 # fallback with no piped input
        rc, out, err = run(["java", "-cp", classes, b["pkg"] + "." + b["main"]], "")
        first_exp = next(exp for inp, exp in b["pairs"] if inp)
        if norm(out, b["pkg"] if b["e"]["strip_pkg"] else None) != norm(first_exp):
            status, detail = "FAIL", f"no-input fallback: got {out[:120]!r} {err[:200]}"
    # single-file launch (what the VS Code task / `java Solution.java` does)
    if status == "PASS":
        rc, out, err = run(["java", os.path.join(b["dir"], "Solution.java")], b["pairs"][0][0] + "\n" if b["pairs"] and b["pairs"][0][0] else "")
        if norm(out, b["pkg"] if b["e"]["strip_pkg"] else None) != norm(b["pairs"][0][1] or ""):
            status, detail = "FAIL", f"single-file launch: {out[:120]!r} {err[:300]}"
    # HackerRank copy compiles?
    hr = open(os.path.join(b["dir"], "Solution_hackerrank.java")).read()
    if slug == "java-reflection-attributes":
        hr += S["java-reflection-attributes"]["extra"]
    pub = re.search(r"\bpublic\s+(?:abstract\s+|final\s+)*class\s+(\w+)", hr)
    hd = tempfile.mkdtemp(dir=work)
    fn = os.path.join(hd, (pub.group(1) if pub else "Solution") + ".java")
    open(fn, "w").write(hr)
    rc, _, err = run(["javac", "-nowarn", "-Xlint:none", "-d", hd, fn], "")
    hr_ok = "hr-compiles" if rc == 0 else "hr-COMPILE-ERROR: " + " ".join(err.strip().splitlines()[:2])[:160]
    results.append((slug, status, detail, hr_ok))

for r in results:
    print(*r)
print("PASS:", sum(r[1] == "PASS" for r in results), "/", len(results),
      "| hr copies compiling:", sum(len(r) > 3 and r[3] == "hr-compiles" for r in results))
json.dump([{k: v for k, v in b.items() if k in ("rel",)} | {"slug": b["c"]["slug"], "name": b["c"]["name"],
            "difficulty": b["c"]["difficulty"], "subdomain": b["c"]["subdomain"]} for b in built],
          open(os.path.join(OUT, "_index.json"), "w"), indent=1)
shutil.rmtree(work, ignore_errors=True)
