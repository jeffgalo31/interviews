#!/usr/bin/env python3
"""Give every exercise README (Code/sql, Code/java) the same study-friendly layout and rebuild the two indexes.

usage (from the interviews folder):  python3 Code/_tools/study_layout.py
Safe to run again: READMEs already in the new layout are left as they are, indexes are rebuilt.
"""
import os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MARK = "<!-- study-layout -->"
DIFF = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
NUM = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
TRACK = {"sql": ("🗄️", "SQL"), "java": ("☕", "Java")}

META_RE = re.compile(r"^\*\*Difficulty:\*\* (\w+) · \*\*Section:\*\* (.+?) · \*\*Track:\*\* HackerRank (\w+) · \[Open on HackerRank\]\((\S+)\)", re.M)
H_BOLD = re.compile(r"^\s*(?:\*\*|__)\s*([A-Za-z][A-Za-z0-9 \-/]*?)\s*:?\s*(?:\*\*|__)\s*:?\s*(?:<br\s*/?>)?\s*$")
H_MD = re.compile(r"^#{2,3}\s+(.+?)\s*$")

def slug(heading):
    t = re.sub(r"[^\w\- ]", "", heading.lower(), flags=re.U)
    t = re.sub(r"_", "", t)
    return "#" + t.replace(" ", "-")

def classify(name):
    clean = re.sub(r"\*\([^)]*\)\*", "", name).strip().strip(":").strip()
    low = re.sub(r"\s+", " ", clean.lower())
    m = re.match(r"(sample input|sample output|explanation)\s*(\d*)$", low)
    if m:
        return {"sample input": "in", "sample output": "out", "explanation": "expl"}[m.group(1)], m.group(2) or "0", clean
    if low in ("input format", "constraints", "output format"):
        return "io", low, clean
    return "generic", None, clean

def split_statement(lines):
    """-> intro lines, list of sections (kind, key, title, lines)."""
    intro, sections, cur, fence = [], [], None, False
    for l in lines:
        if l.strip().startswith("```"):
            fence = not fence
        m = None if fence else (H_BOLD.match(l) or H_MD.match(l))
        if m:
            kind, key, title = classify(m.group(1))
            cur = [kind, key, title, []]
            sections.append(cur)
            continue
        (cur[3] if cur else intro).append(l)
    return intro, sections

def tidy(lines):
    text = "\n".join(lines).strip("\n")
    return re.sub(r"\n{3,}", "\n\n", text)

def render_statement(lines):
    intro, sections = split_statement(lines)
    first_ex = next((i for i, s in enumerate(sections) if s[0] in ("in", "out", "expl")), len(sections))
    problem = [tidy(intro)] if tidy(intro) else []
    io, after = [], []
    examples = {}
    order = []
    for i, (kind, key, title, body) in enumerate(sections):
        body_t = tidy(body)
        if kind == "io":
            io.append(f"### {title[0].upper() + title[1:].lower()}\n\n{body_t}")
        elif kind in ("in", "out", "expl"):
            if key not in examples:
                examples[key] = {}
                order.append(key)
            examples[key][kind] = body_t
        elif i < first_ex:
            problem.append(f"### {title}\n\n{body_t}" if body_t else f"### {title}")
        else:
            after.append(f"### {title}\n\n{body_t}" if body_t else f"### {title}")
    out = {"problem": "\n\n".join(p for p in problem if p).strip(), "io": "\n\n".join(io)}
    ex_parts = []
    for n, key in enumerate(order, 1):
        e = examples[key]
        part = [f"### Example {n}"] if len(order) > 1 else []
        if e.get("in"):
            part.append("**Input**\n\n" + e["in"])
        if e.get("out") is not None:
            part.append("**Output**\n\n" + (e["out"] or "*(nothing is printed)*"))
        if e.get("expl"):
            part.append("**Why**\n\n" + e["expl"])
        ex_parts.append("\n\n".join(part))
    out["examples"] = "\n\n".join(ex_parts + after)
    out["n_examples"] = len(order)
    return out

def parse_solution(lines):
    """Generated solutions: code block + bullets + notes. Hand-written ones: keep as they are."""
    text = "\n".join(lines)
    text = re.sub(r"(?m)^Files: .*$", "", text)
    text = re.sub(r"(?s)\n\*\*Files\*\*\n.*$", "", text)
    sample = re.search(r"(?m)^\*\*Sample data in solution\.sql:\*\* (.*)$", text)
    text = re.sub(r"(?m)^\*\*Sample data in solution\.sql:\*\* .*$", "", text)
    local = re.search(r"(?m)^\*\*Local SQLite version\*\* (.*)$", text)
    text = re.sub(r"(?m)^\*\*Local SQLite version\*\* .*$", "", text)
    text = re.sub(r"(?m)^The part you write:\s*$", "", text)
    stripped = text.strip()
    generated = bool(re.fullmatch(r"```\w*\n.*?\n```\s*(\n- .*)*", stripped, re.S))
    return dict(text=stripped, generated=generated, sample=sample.group(1) if sample else None,
                local=local.group(1) if local else None)

def render_solution(sol, lang):
    if not sol["generated"]:
        return sol["text"]
    m = re.match(r"(```\w*\n.*?\n```)", sol["text"], re.S)
    code = m.group(1)
    bullets = re.findall(r"(?m)^- (.*)$", sol["text"][m.end():])
    parts = []
    if bullets:
        parts.append("> [!TIP]\n> **Key idea:** " + bullets[0])
    parts.append(("### ✍️ The query\n\n" if lang == "SQL" else "### ✍️ The code you write\n\n") + code)
    if len(bullets) > 1:
        parts.append("### 🔍 How it works\n\n" + "\n".join("- " + b for b in bullets[1:]))
    if sol["local"]:
        parts.append("> [!NOTE]\n> **Local SQLite version** " + sol["local"])
    return "\n\n".join(parts)

def files_table(lang, readme_path, sample_note):
    if lang == "SQL":
        rows = ["| | File | What it's for |", "|---|---|---|",
                "| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |",
                "| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |"]
        if sample_note:
            rows += ["", f"🧪 **Sample data in solution.sql:** {sample_note.replace('the Sample Output above', 'the Example above')}"]
    else:
        rel = os.path.relpath(os.path.dirname(readme_path), os.path.join(ROOT, "java")).replace(os.sep, "/")
        rows = ["| | File | What it's for |", "|---|---|---|",
                f"| ▶️ | [Solution.java](Solution.java) | Runnable, commented version. In VS Code click **Run** above `main`; terminal (in `java`): `java {rel}/Solution.java` |",
                "| 📋 | [Solution_hackerrank.java](Solution_hackerrank.java) | HackerRank's exact program: paste it whole, or only the `// ---- your code ----` part if the rest is locked |"]
    return "\n".join(rows)

def restyle(path, nav):
    src = open(path, encoding="utf-8").read()
    if src.startswith(MARK):
        return False
    lines = src.split("\n")
    title = lines[0][2:].strip()
    mi = next(i for i, l in enumerate(lines) if META_RE.match(l))
    diff, section, lang, url = META_RE.match(lines[mi]).groups()
    si = next(i for i, l in enumerate(lines) if l.startswith("## Solution"))
    sol_title = lines[si][len("## Solution"):].strip()
    stmt_lines = [l for l in lines[mi + 1:si]]
    while stmt_lines and stmt_lines[0].strip() in ("", "---"):
        stmt_lines.pop(0)
    st = render_statement(stmt_lines)
    sol = parse_solution(lines[si + 1:])

    icon, _ = TRACK[lang.lower()]
    heads = [("📝 Problem", st["problem"]), ("📥 Input & output", st["io"]),
             ("🧪 Examples" if st["n_examples"] > 1 else "🧪 Example", st["examples"]),
             ("💡 Solution" + (sol_title if sol_title else ""), render_solution(sol, lang)),
             ("📂 Files", files_table(lang, path, sol["sample"]))]
    heads = [(h, b) for h, b in heads if b]
    on_page = " · ".join(f"[{h}]({slug(h)})" for h, _ in heads)
    out = [MARK, f"# {title}", "",
           f"{DIFF.get(diff, '')} **{diff}** · 📁 **{section}** · {icon} HackerRank {lang} · [Open on HackerRank ↗]({url})", "",
           f"**On this page:** {on_page}", "", "---", ""]
    for h, b in heads:
        out += [f"## {h}", "", b, ""]
    out += ["---", "", nav, ""]
    open(path, "w", encoding="utf-8").write("\n".join(out))
    return True

# ------------------------------------------------------------------------------------------------ indexes
def exercises(track):
    """Ordered exercises of a track, read from each README (works before and after restyling)."""
    base = os.path.join(ROOT, track)
    idx = open(os.path.join(base, "README.md"), encoding="utf-8").read()
    rows = []
    for name, link in re.findall(r"^\| [^|]* \| \[([^\]]+)\]\(([^)#][^)]*?)/?(?:README\.md)?\) \|", idx, re.M):
        d = os.path.normpath(os.path.join(base, link))
        text = open(os.path.join(d, "README.md"), encoding="utf-8").read()
        m = META_RE.search(text) or re.search(r"^(?:🟢|🟡|🔴) \*\*(\w+)\*\* · 📁 \*\*(.+?)\*\*", text, re.M)
        rows.append(dict(name=name, dir=d, diff=m.group(1), section=m.group(2)))
    return rows

def nav_line(rows, i, track):
    here = rows[i]["dir"]
    rel = lambda d: os.path.relpath(os.path.join(d, "README.md"), here).replace(os.sep, "/")
    idx = os.path.relpath(os.path.join(ROOT, track, "README.md"), here).replace(os.sep, "/")
    icon, lang = TRACK[track]
    parts = []
    if i > 0:
        parts.append(f"⬅️ [{rows[i - 1]['name']}]({rel(rows[i - 1]['dir'])})")
    parts.append(f"[{icon} All {lang} exercises]({idx})")
    if i + 1 < len(rows):
        parts.append(f"[{rows[i + 1]['name']}]({rel(rows[i + 1]['dir'])}) ➡️")
    return " · ".join(parts)

def build_index(track, rows, intro, how, running, extra, footer):
    icon, lang = TRACK[track]
    base = os.path.join(ROOT, track)
    sections = list(dict.fromkeys(r["section"] for r in rows))
    count = lambda sec, d=None: sum(1 for r in rows if r["section"] == sec and (d is None or r["diff"] == d))
    L = [f"# {icon} {lang} Coding Practice", "", intro, "",
         "| | Section | Challenges | 🟢 Easy | 🟡 Medium | 🔴 Hard |", "|---|---|---|---|---|---|"]
    for n, sec in enumerate(sections):
        L.append(f"| {NUM[n]} | [{sec}]({slug(NUM[n] + ' ' + sec + ' (' + str(count(sec)) + ')')}) | {count(sec)} | "
                 f"{count(sec, 'Easy')} | {count(sec, 'Medium')} | {count(sec, 'Hard')} |")
    tot = lambda d=None: sum(1 for r in rows if d is None or r["diff"] == d)
    L += [f"| | **Total** | **{tot()}** | **{tot('Easy')}** | **{tot('Medium')}** | **{tot('Hard')}** |", "",
          "## 📖 How to study one exercise", "", how, "", "## ▶️ Running", "", running, ""]
    if extra:
        L += [extra, ""]
    for n, sec in enumerate(sections):
        L += [f"## {NUM[n]} {sec} ({count(sec)})", "", "| # | Challenge | Level | Runnable | HackerRank | Done |", "|---|---|---|---|---|---|"]
        for i, r in enumerate([r for r in rows if r["section"] == sec], 1):
            d = os.path.relpath(r["dir"], base).replace(os.sep, "/")
            run_f, hr_f = ("solution.sql", "solution_hackerrank.sql") if track == "sql" else ("Solution.java", "Solution_hackerrank.java")
            L.append(f"| {i} | [{r['name']}]({d}/README.md) | {DIFF[r['diff']]} {r['diff']} | [▶️ {run_f}]({d}/{run_f}) | [📋 copy]({d}/{hr_f}) | ⬜ |")
        L.append("")
    L += ["> [!TIP]", "> Change ⬜ to ✅ in the **Done** column as you finish each challenge.", "", "---", "", footer, ""]
    open(os.path.join(base, "README.md"), "w", encoding="utf-8").write("\n".join(L))

SQL_TEXT = dict(
    intro="All **58** challenges from the [HackerRank SQL track](https://www.hackerrank.com/domains/sql), grouped by HackerRank section, "
          "with the same names and difficulty. Every problem is fully in text (tables instead of images), solved, explained and runnable.",
    how="1. Read the problem in the exercise's `README.md` and try writing the query yourself.\n"
        "2. Check the **🧪 Example** section: that's the data the query must handle.\n"
        "3. Read **💡 Solution**: the key idea first, then the query and how it works.\n"
        "4. Run `solution.sql` to see it on real data (it builds the sample tables first).\n"
        "5. Submit `solution_hackerrank.sql` on HackerRank (choose **MySQL**) and mark it ✅ below.",
    running="Open the `interviews` folder (or this `sql` folder) in VS Code, open a `solution.sql`, then "
            "**Terminal → Run Task → Run SQL file (SQLite)**. It runs on a fresh in-memory database every time.\n\n"
            "From a terminal in this folder: `sqlite3 -header -column :memory: < basic-select/select-all/solution.sql`",
    extra="## 🔀 SQLite vs MySQL\n\nHackerRank uses MySQL; the local files use SQLite (built into macOS, nothing to install). "
          "Most SQL is identical; where it isn't, the exercise says so:\n\n"
          "| MySQL (HackerRank) | SQLite (local) | Meaning |\n|---|---|---|\n"
          "| `CONCAT(a, b, c)` | `a \\|\\| b \\|\\| c` | join strings |\n"
          "| `LEFT(s, 1)` | `SUBSTR(s, 1, 1)` | first character |\n"
          "| `FLOOR(x)` / `CEIL(x)` | `CAST(x AS INTEGER)` (+1 if decimals for CEIL) | round down / up |\n"
          "| `TRUNCATE(x, 4)` | `CAST(x * 10000 AS INTEGER) / 10000.0` | cut to 4 decimals |\n"
          "| `DATEDIFF(a, b)` | `julianday(a) - julianday(b)` | days between dates |\n"
          "| `REPEAT(s, n)` | `REPLACE(HEX(ZEROBLOB(n)), '00', s)` | repeat a string |",
    footer="🛠️ How this was built (and how to do the same for another tech): [HACKERRANK-IMPORT.md](../HACKERRANK-IMPORT.md) · generator: [_tools/gen.py](_tools/gen.py)\n\n"
           "**Back to:** [All Topics](../../Overview/All-Topics.md) · [Practices](../../Overview/Practices.md) · [☕ Java exercises](../java/README.md)")

JAVA_TEXT = dict(
    intro="All **64** challenges from the [HackerRank Java track](https://www.hackerrank.com/domains/java), grouped by HackerRank section, "
          "with the same names and difficulty. Every problem is fully in text, solved, explained and runnable.",
    how="1. Read the problem in the exercise's `README.md` and try solving it yourself.\n"
        "2. Check the **🧪 Example** section: the exact input your program gets and the output it must print.\n"
        "3. Read **💡 Solution**: the key idea first, then the code you write and how it works.\n"
        "4. Run `Solution.java` (it uses the sample input when you don't type any).\n"
        "5. Submit `Solution_hackerrank.java` on HackerRank and mark it ✅ below.",
    running="Open the `interviews` folder (or this `java` folder) in VS Code with the Extension Pack for Java, open a "
            "`Solution.java` and click **Run** above `main`. From a terminal in this folder:\n\n"
            "```\njava src/introduction/java_if_else/Solution.java                 # uses the sample input\n"
            "printf '24\\n' | java src/introduction/java_if_else/Solution.java  # your own input\n```\n\n"
            "> [!NOTE]\n> VS Code may list errors for the `Solution_hackerrank.java` files: they have no `package` line on purpose "
            "(that's how HackerRank needs them). They don't stop the `Solution.java` files from running.",
    extra="## 📄 What's in each exercise\n\n| | File | What it's for |\n|---|---|---|\n"
          "| 📝 | `README.md` | The problem, examples, and the explained solution |\n"
          "| ▶️ | `Solution.java` | Runnable and commented; falls back to HackerRank's sample input |\n"
          "| 📋 | `Solution_hackerrank.java` | HackerRank's exact program; your part is between `// ---- your code ----` markers |",
    footer="🛠️ How this was built (and how to do the same for another tech): [HACKERRANK-IMPORT.md](../HACKERRANK-IMPORT.md) · generator: [_tools/](_tools/)\n\n"
           "**Back to:** [All Topics](../../Overview/All-Topics.md) · [Practices](../../Overview/Practices.md) · [🗄️ SQL exercises](../sql/README.md)")

if __name__ == "__main__":
    changed = 0
    for track, text in (("sql", SQL_TEXT), ("java", JAVA_TEXT)):
        rows = exercises(track)
        for i, r in enumerate(rows):
            changed += restyle(os.path.join(r["dir"], "README.md"), nav_line(rows, i, track))
        build_index(track, rows, **text)
        print(f"{track}: {len(rows)} exercises")
    print("restyled:", changed)
