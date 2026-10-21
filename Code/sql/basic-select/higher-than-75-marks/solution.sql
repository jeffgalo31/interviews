-- Higher Than 75 Marks  (Easy · Basic Select)  https://www.hackerrank.com/challenges/more-than-75-marks/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS STUDENTS;
CREATE TABLE STUDENTS (ID INTEGER, NAME TEXT, MARKS INTEGER);
INSERT INTO STUDENTS VALUES (1, 'Ashley', 81), (2, 'Samantha', 75), (4, 'Julia', 76), (3, 'Belvet', 84);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): Ashley / Julia / Belvet
-- ---------------------------------------------------------------------------
-- SUBSTR(NAME, -3) = last three characters (RIGHT(NAME, 3) is the same in MySQL).
-- Second sort key ID breaks ties when two names end the same way.
-- > 75 excludes Samantha's exact 75.
SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
ORDER BY SUBSTR(NAME, -3), ID;
