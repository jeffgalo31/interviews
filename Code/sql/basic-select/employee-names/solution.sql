-- Employee Names  (Easy · Basic Select)  https://www.hackerrank.com/challenges/name-of-employees/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee (employee_id INTEGER, name TEXT, months INTEGER, salary INTEGER);
INSERT INTO Employee VALUES
    (12228, 'Rose',     15, 1968),
    (33645, 'Angela',    1, 3443),
    (45692, 'Frank',    17, 1608),
    (56118, 'Patrick',   7, 1345),
    (59725, 'Lisa',     11, 2330),
    (74197, 'Kimberly', 16, 4372),
    (78454, 'Bonnie',    8, 1771),
    (83565, 'Michael',   6, 2017),
    (98607, 'Todd',      5, 3396),
    (99989, 'Joe',       9, 3573);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): Angela / Bonnie / Frank / Joe / Kimberly / Lisa / Michael / Patrick / Rose / Todd
-- ---------------------------------------------------------------------------
-- ORDER BY name sorts alphabetically (ascending is the default).
SELECT name
FROM Employee
ORDER BY name;
