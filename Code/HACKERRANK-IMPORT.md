# Importing a HackerRank track into `Code/`

How the whole [SQL track](sql/README.md) was imported, written so the same work can be repeated for another
tech (Java, Python, ...). Follow the steps in order; each one says what "done" looks like.

**Goal for every challenge:** HackerRank's exact name, difficulty and section; the full problem as **text**
(no images, no missing formulas); a runnable, commented solution that uses the **official sample data**; and a
plain copy to paste into HackerRank.

---

## 1. Get the challenge list (name, difficulty, section)

HackerRank blocks direct downloads from scripts and servers, so everything goes through **Chrome**, on a
`https://www.hackerrank.com/...` page, using its own API (`fetch` in the page's console / JavaScript tool):

```js
// <track> = sql, java, python, ... (the part after /domains/ in https://www.hackerrank.com/domains/<track>)
const page = (o) => fetch(`/rest/contests/master/tracks/<track>/challenges?offset=${o}&limit=50&track_login=true`).then(r => r.json());
// the API returns at most 50 per call: keep calling with offset 0, 50, 100, ... until you have `total` items
// each model has: slug, name, difficulty_name (Easy/Medium/Hard), track.name (the section, e.g. "Basic Select")
```

## 2. Get every problem statement

```js
const c = await fetch(`/rest/contests/master/challenges/${slug}`).then(r => r.json());
// c.model.problem_statement  markdown, math as $...$        (main text)
// c.model.input_format       markdown                        (input format; for SQL, also the table schemas)
// c.model.constraints, c.model.output_format                 (often empty)
// c.model.body_html          the rendered page: the ONLY place with Sample Input / Sample Output / Explanation
//                            when they are not in the markdown fields; its math is SVG (numbers are lost)
// c.model.<lang>_template    starter code for that language (e.g. java8_template) - useful for Java/Python
```

- Build each statement as: `problem_statement` + `input_format` (+ constraints/output_format), then append the
  **Sample Input / Sample Output / Explanation** part from `body_html` if the markdown fields don't have it.
- **Check for missing math:** count `span.MathJax_SVG` in `body_html` vs `$...$` in the markdown. Where
  `body_html` has more, its explanation lost numbers: fill them in by hand (see step 4).

**Saving the data:** the browser can't write into your folders, so put a button on the page whose click
downloads one JSON file (a real click is required), then move it to `Documents/hackerrank/<tech>/`.
Chrome blocks a second automatic download from the same site: allow it once via the icon at the right of the
address bar ("Always allow www.hackerrank.com to download multiple files"). SQL's file:
`Documents/hackerrank/sql/hackerrank-sql-challenges.json` (58 challenges).

## 3. Turn every image into text

Statements reference images on `https://s3.amazonaws.com/hr-challenge-images/...` (schemas, sample tables,
diagrams). Scripts can't download them (blocked), so:

1. List every image URL used by the statements.
2. Open each one in a Chrome tab and take a screenshot. Tall images get cut off: shrink them first with
   `document.querySelector('img').style.height = '700px'`. Batch several navigate + screenshot steps per call.
3. Write each one as a Markdown table (or a code block for diagrams/trees) in `sql/_tools/images.py`
   (`IMG = { "<path after hr-challenge-images/>": "<markdown>" }`).
4. The generator replaces every image with its transcription and **fails if any image has none**.

Watch for HackerRank typos (SQL: the Occupations sample table says "Ashely", its expected output "Ashley"):
keep HackerRank's data and note the typo in the README.

## 4. Fill in explanations that lost their numbers

Where an Explanation used formulas, rewrite it in HackerRank's own wording with the numbers filled in,
computed from the official sample data (`EXPLAIN` in `images.py`). Mark it with
"> Numbers that appear as formulas on HackerRank are filled in here."

## 5. Write the solutions

For each challenge: the solution, 2-4 short explanation bullets, and the sample data as code.

- **Use the official sample** whenever HackerRank shows one (transcribed in step 3), with the official expected
  output so the run can be checked automatically.
- No sample on HackerRank: make up small data and say so in the file.
- Keep the runnable version and the HackerRank copy identical where possible; where the local runtime lacks a
  feature, say exactly what differs (SQL: MySQL `FLOOR`/`TRUNCATE`/`DATEDIFF`/`REPEAT` vs SQLite).

SQL does this with one script, [`sql/_tools/gen.py`](sql/_tools/gen.py): an `ex(...)` entry per challenge
(setup, local query, HackerRank query, notes, expected output). Copy it as the starting point for a new tech.

## 6. Folder layout and files

```
Code/<tech>/README.md                         index: every challenge by section, name, difficulty, links
Code/<tech>/<section>/<challenge>/README.md   name, difficulty, section, link, full problem, solution + notes
                                 /<runnable>   commented, runs locally with the sample input built in
                                 /<hackerrank> plain copy to paste into HackerRank
```

- **SQL:** `solution.sql` (SQLite: creates the sample tables, runs the query) + `solution_hackerrank.sql` (MySQL).
- **Java** (done: [`java/`](java/README.md), generator in [`java/_tools/`](java/_tools/)): `src/<section>/<challenge>/`
  with `package <section>.<challenge>;` (letters/underscores only), `Solution.java` (runnable, falls back to
  `SAMPLE_INPUT`), `Solution_hackerrank.java` (HackerRank's exact program, no package line) and `README.md`.
- **Other languages:** same idea: a runnable file that falls back to the sample input, plus the paste copy.

Folder names: the challenge name in lowercase with dashes (`Ollivander's Inventory` -> `ollivanders-inventory`).
Sections: HackerRank's `track.name` (`Basic Select` -> `basic-select`).

## 7. Verify before committing

- Every runnable file runs without errors.
- Every challenge with an official sample prints exactly HackerRank's Sample Output.
- No `amazonaws` link is left anywhere (`grep -rl amazonaws Code/<tech>`).
- Every link in the index exists.
- Copies that use features the local runtime lacks can't be tested locally: say which ones in the summary.

## 8. Commit and push

- Author **Jeffrey Galo**, committer **Claude** (`GIT_COMMITTER_NAME=Claude GIT_COMMITTER_EMAIL=noreply@anthropic.com`),
  message ending with the Co-Authored-By / Claude-Session lines.
- Git on the Mac needs delete permission in `Documents` (it removes its own lock files).
- Claude can't push to GitHub yet: push with **Sync Changes** in VS Code's Source Control.
- Link the new tech from `Overview/Practices.md` and `Overview/All-Topics.md` ("Coding practice" line).

## Lessons from the Java track

- **Code templates:** `java8_template_head` / `java8_template` / `java8_template_tail` (or `java_template*`) are
  HackerRank's starter code. Write the full program (head + your code + tail) and wrap your part in
  `// ---- your code ----` / `// ---- end of your code ----`, so it's clear what to paste if HackerRank locks the rest.
  `solutions.py` holds one entry per challenge; a check confirms every template line is still in the program.
- **Runnable version** (made automatically from the HackerRank program): add the `package` line; put the class
  with `main` first (single-file `java Solution.java` runs the first class); only `Solution` may stay `public`;
  inject a `static { ... }` block that swaps in `SAMPLE_INPUT` when nothing is piped in (it must be the first member
  so it runs before `static Scanner` fields); write to `System.out` instead of HackerRank's `OUTPUT_PATH` file;
  comment out HackerRank's `DoNotTerminate.forbidExit()` (SecurityManager is disabled in newer Java).
- **Samples:** parse `Sample Input N` / `Sample Output N` (code fences or indented blocks). A statement can *mention*
  "sample output" without having one: check for the heading, and take missing samples from `body_html`.
- **Images:** besides `hr-challenge-images`, statements use `s3.amazonaws.com/hr-assets/...` images too.
- **Tests:** compile each runnable file, run every official sample (piped and with no input), run the single-file
  launch, and compile every HackerRank copy. Strip the package prefix when the expected output prints class names.
- **Known HackerRank quirks:** Currency Formatter's symbols depend on the Java version (Java 8: `Rs.`, `￥`);
  Prime Checker's locked code says `misc.Prime`; Covariant Return Types' diagram says Lotus but the code uses Lily;
  Java Factory's text says "ordered Fast Food" but the code prints "ordered a Fast Food".

