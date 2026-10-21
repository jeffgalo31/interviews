-- Draw The Triangle 2  (Easy · Alternative Queries)  https://www.hackerrank.com/challenges/draw-the-triangle-2/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql  (differs: REPEAT('* ', n) + variables → recursive CTE + REPLACE(HEX(ZEROBLOB(n)), '00', '* '))

-- ---------------------------------------------------------------------------
-- SETUP: sample data (made up: HackerRank shows no sample for this one)
-- ---------------------------------------------------------------------------
-- No table needed.

-- ---------------------------------------------------------------------------
-- QUERY
-- ---------------------------------------------------------------------------
-- Same as Draw The Triangle 1, counting up from 1 to 20 instead of down.
WITH RECURSIVE rows_(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM rows_ WHERE n < 20
)
SELECT TRIM(REPLACE(HEX(ZEROBLOB(n)), '00', '* '))
FROM rows_;
