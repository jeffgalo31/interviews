-- Symmetric Pairs  (Medium · Advanced Join)  https://www.hackerrank.com/challenges/symmetric-pairs/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Functions;
CREATE TABLE Functions (X INTEGER, Y INTEGER);
INSERT INTO Functions VALUES (20, 20), (20, 20), (20, 21), (23, 22), (22, 23), (21, 20);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): 20 20 / 20 21 / 22 23
-- ---------------------------------------------------------------------------
-- Self-join: find a row whose (X, Y) is this row flipped.
-- X < Y keeps one of each pair (20 21, not 21 20).
-- When X = Y a row matches itself, so it only counts if that pair appears at least twice: COUNT(*) > 1.
SELECT f1.X, f1.Y
FROM Functions f1
JOIN Functions f2 ON f1.X = f2.Y AND f1.Y = f2.X
GROUP BY f1.X, f1.Y
HAVING f1.X < f1.Y OR COUNT(*) > 1
ORDER BY f1.X;
