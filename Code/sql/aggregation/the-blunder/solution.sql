-- The Blunder  (Easy · Aggregation)  https://www.hackerrank.com/challenges/the-blunder/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql  (differs: CEIL(x) → integer part + 1 if there are decimals)

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS EMPLOYEES;
CREATE TABLE EMPLOYEES (ID INTEGER, Name TEXT, Salary INTEGER);
INSERT INTO EMPLOYEES VALUES (1, 'Kristeen', 1420), (2, 'Ashley', 2006), (3, 'Julia', 2210), (4, 'Maria', 3000);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): 2061
-- ---------------------------------------------------------------------------
-- Samantha's salaries = the real salaries with every 0 removed: REPLACE(Salary, '0', '') (1420 → 142).
-- Error = real average − miscalculated average, then round up with CEIL.
-- Local SQLite: no CEIL, so it adds 1 when there is a decimal part.
SELECT CAST(err AS INTEGER) + (err > CAST(err AS INTEGER))   -- round UP (CEIL)
FROM (
    SELECT AVG(Salary)
         - AVG(CAST(REPLACE(CAST(Salary AS TEXT), '0', '') AS INTEGER)) AS err
    FROM EMPLOYEES
) t;
