# Draw The Triangle 1

**Difficulty:** Easy · **Section:** Alternative Queries · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/draw-the-triangle-1/problem)

---

_P(R)_ represents a pattern drawn by Julia in _R_ rows. The following pattern represents _P(5)_:

    * * * * * 
    * * * * 
    * * * 
    * * 
    *

Write a query to print the pattern _P(20)_.

## Solution

```sql
SET @n := 21;
SELECT REPEAT('* ', @n := @n - 1)
FROM information_schema.tables
LIMIT 20;
```

- MySQL: a user variable `@n` starts at 21 and goes down by 1 on every row; `REPEAT('* ', n)` draws the row.
- `information_schema.tables` is just any table with at least 20 rows to loop over; `LIMIT 20` stops at 20 rows.
- SQLite has no `REPEAT`: a recursive CTE counts 20 → 1 and `HEX(ZEROBLOB(n))` makes n copies of `00`, replaced by `* `.

**Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `REPEAT('* ', n)` + variables → recursive CTE + `REPLACE(HEX(ZEROBLOB(n)), '00', '* ')`.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
