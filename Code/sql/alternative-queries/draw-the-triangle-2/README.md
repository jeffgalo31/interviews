# Draw The Triangle 2

**Difficulty:** Easy · **Section:** Alternative Queries · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/draw-the-triangle-2/problem)

---

_P(R)_ represents a pattern drawn by Julia in _R_ rows. The following pattern represents _P(5)_:

    *
    * *
    * * *
    * * * *
    * * * * *

Write a query to print the pattern _P(20)_.

## Solution

```sql
SET @n := 0;
SELECT REPEAT('* ', @n := @n + 1)
FROM information_schema.tables
LIMIT 20;
```

- Same as Draw The Triangle 1, counting **up** from 1 to 20 instead of down.

**Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `REPEAT('* ', n)` + variables → recursive CTE + `REPLACE(HEX(ZEROBLOB(n)), '00', '* ')`.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
