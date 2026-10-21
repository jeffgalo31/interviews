# SQL Coding Practice

HackerRank-style SQL exercises. Each exercise has its own folder.

| Exercise | Topic | Files |
|---|---|---|
| [The PADS](the-pads/) | Advanced Select: CONCAT, GROUP BY, ORDER BY | [README](the-pads/README.md) · [solution.sql](the-pads/solution.sql) · [HackerRank copy](the-pads/solution_hackerrank.sql) |
| [New Companies](new-companies/) | Advanced Select: COUNT(DISTINCT), correlated subqueries | [README](new-companies/README.md) · [solution.sql](new-companies/solution.sql) · [HackerRank copy](new-companies/solution_hackerrank.sql) |

## Files in each exercise

- `README.md`: the problem description and how the solution works.
- `solution.sql`: the runnable version, with comments. It creates the sample table first, then runs the queries.
  Written for **SQLite** (built into macOS), so there's nothing to install.
- `solution_hackerrank.sql`: the plain copy to paste into HackerRank (**MySQL**, no table setup:
  HackerRank already has the table).

## Running

Open this `sql` folder in VS Code, open a `solution.sql`, then **Terminal → Run Task → Run SQL file (SQLite)**
(or ⇧⌘B). It runs on a fresh in-memory database every time, so there's nothing to clean up.

From the terminal: `sqlite3 -header -column :memory: < the-pads/solution.sql`

## SQLite vs MySQL

HackerRank uses MySQL; the local files use SQLite. Most SQL is the same, but a few functions differ:

| MySQL (HackerRank) | SQLite (local) | Meaning |
|---|---|---|
| `CONCAT(a, b, c)` | `a \|\| b \|\| c` | join strings |
| `LEFT(s, 1)` | `SUBSTR(s, 1, 1)` | first character |

---

**Back to:** [All Topics](../../Overview/All-Topics.md) · [Java exercises](../java/)
