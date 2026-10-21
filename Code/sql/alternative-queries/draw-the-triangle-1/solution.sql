-- Draw The Triangle 1  (Easy · Alternative Queries)  https://www.hackerrank.com/challenges/draw-the-triangle-1/problem
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
-- MySQL: a user variable @n starts at 21 and goes down by 1 on every row; REPEAT('* ', n) draws the row.
-- information_schema.tables is just any table with at least 20 rows to loop over; LIMIT 20 stops at 20 rows.
-- SQLite has no REPEAT: a recursive CTE counts 20 → 1 and HEX(ZEROBLOB(n)) makes n copies of 00, replaced by * .
WITH RECURSIVE rows_(n) AS (
    SELECT 20
    UNION ALL
    SELECT n - 1 FROM rows_ WHERE n > 1
)
SELECT TRIM(REPLACE(HEX(ZEROBLOB(n)), '00', '* '))
FROM rows_;
