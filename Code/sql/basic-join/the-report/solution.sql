-- The Report  (Medium · Basic Join)  https://www.hackerrank.com/challenges/the-report/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Grades;
CREATE TABLE Students (ID INTEGER, Name TEXT, Marks INTEGER);
INSERT INTO Students VALUES (1, 'Julia', 88), (2, 'Samantha', 68), (3, 'Maria', 99), (4, 'Scarlet', 78), (5, 'Ashley', 63), (6, 'Jane', 81);

CREATE TABLE Grades (Grade INTEGER, Min_Mark INTEGER, Max_Mark INTEGER);
INSERT INTO Grades VALUES (1, 0, 9), (2, 10, 19), (3, 20, 29), (4, 30, 39), (5, 40, 49),
                          (6, 50, 59), (7, 60, 69), (8, 70, 79), (9, 80, 89), (10, 90, 100);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): Maria 10 99 / Jane 9 81 / Julia 9 88 / Scarlet 8 78 / NULL 7 63 / NULL 7 68
-- ---------------------------------------------------------------------------
-- The join is a range: each mark matches the grade row whose Min_Mark..Max_Mark contains it.
-- CASE hides names below grade 8 (prints NULL).
-- Sort: grade high → low; then name (only for grades 8-10, NULL for the rest); then marks ascending, which orders the NULL rows.
SELECT CASE WHEN g.Grade >= 8 THEN s.Name ELSE NULL END AS Name,
       g.Grade,
       s.Marks
FROM Students s
JOIN Grades g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY g.Grade DESC,
         CASE WHEN g.Grade >= 8 THEN s.Name END,
         s.Marks;
