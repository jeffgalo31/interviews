-- Placements  (Medium · Advanced Join)  https://www.hackerrank.com/challenges/placements/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Friends;
DROP TABLE IF EXISTS Packages;
CREATE TABLE Students (ID INTEGER, Name TEXT);
INSERT INTO Students VALUES (1, 'Ashley'), (2, 'Samantha'), (3, 'Julia'), (4, 'Scarlet');

CREATE TABLE Friends (ID INTEGER, Friend_ID INTEGER);
INSERT INTO Friends VALUES (1, 2), (2, 3), (3, 4), (4, 1);

CREATE TABLE Packages (ID INTEGER, Salary REAL);
INSERT INTO Packages VALUES (1, 15.20), (2, 10.06), (3, 11.55), (4, 12.12);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): Samantha / Julia / Scarlet
-- ---------------------------------------------------------------------------
-- Join Packages twice with different aliases: me = the student's salary, fr = the best friend's salary.
-- Keep students whose friend earns more; sort by the friend's salary.
SELECT s.Name
FROM Students s
JOIN Friends  f  ON s.ID = f.ID
JOIN Packages me ON s.ID = me.ID
JOIN Packages fr ON f.Friend_ID = fr.ID
WHERE fr.Salary > me.Salary
ORDER BY fr.Salary;
