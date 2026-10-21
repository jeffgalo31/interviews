<!-- study-layout -->
# Draw The Triangle 2

🟢 **Easy** · 📁 **Alternative Queries** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/draw-the-triangle-2/problem)

**On this page:** [📝 Problem](#-problem) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

_P(R)_ represents a pattern drawn by Julia in _R_ rows. The following pattern represents _P(5)_:

    *
    * *
    * * *
    * * * *
    * * * * *

Write a query to print the pattern _P(20)_.

## 💡 Solution

> [!TIP]
> **Key idea:** Same as Draw The Triangle 1, counting **up** from 1 to 20 instead of down.

### ✍️ The query

```sql
SET @n := 0;
SELECT REPEAT('* ', @n := @n + 1)
FROM information_schema.tables
LIMIT 20;
```

> [!NOTE]
> **Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `REPEAT('* ', n)` + variables → recursive CTE + `REPLACE(HEX(ZEROBLOB(n)), '00', '* ')`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Draw The Triangle 1](../draw-the-triangle-1/README.md) · [🗄️ All SQL exercises](../../README.md) · [Print Prime Numbers](../print-prime-numbers/README.md) ➡️
