-- Print Prime Numbers  (Medium · Alternative Queries)  https://www.hackerrank.com/challenges/print-prime-numbers/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql  (differs: GROUP_CONCAT(n ORDER BY n SEPARATOR '&') → GROUP_CONCAT(n, '&'))

-- ---------------------------------------------------------------------------
-- SETUP: sample data (made up: HackerRank shows no sample for this one)
-- ---------------------------------------------------------------------------
-- No table needed.

-- ---------------------------------------------------------------------------
-- QUERY
-- ---------------------------------------------------------------------------
-- A recursive CTE generates the numbers 2..1000.
-- NOT EXISTS: keep n if no number d with d² ≤ n divides it evenly (% = remainder).
-- GROUP_CONCAT(... SEPARATOR '&') joins them on one line (SQLite: GROUP_CONCAT(n, '&')).
-- WITH RECURSIVE needs MySQL 8 (HackerRank's MySQL).
WITH RECURSIVE nums AS (
    SELECT 2 AS n
    UNION ALL
    SELECT n + 1 FROM nums WHERE n < 1000
)
SELECT GROUP_CONCAT(n, '&')
FROM nums
WHERE NOT EXISTS (
    SELECT 1
    FROM nums d
    WHERE d.n * d.n <= nums.n      -- only divisors up to the square root
      AND nums.n % d.n = 0         -- d divides n -> not prime
);
