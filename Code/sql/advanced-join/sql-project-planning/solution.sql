-- SQL Project Planning  (Medium · Advanced Join)  https://www.hackerrank.com/challenges/sql-projects/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql  (differs: DATEDIFF(a, b) → julianday(a) - julianday(b))

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Projects;
CREATE TABLE Projects (Task_ID INTEGER, Start_Date TEXT, End_Date TEXT);
INSERT INTO Projects VALUES
    (1, '2015-10-01', '2015-10-02'), (2, '2015-10-02', '2015-10-03'), (3, '2015-10-03', '2015-10-04'),
    (4, '2015-10-13', '2015-10-14'), (5, '2015-10-14', '2015-10-15'), (6, '2015-10-28', '2015-10-29'),
    (7, '2015-10-30', '2015-10-31');

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): 2015-10-28 2015-10-29 / 2015-10-30 2015-10-31 / 2015-10-13 2015-10-15 / 2015-10-01 2015-10-04
-- ---------------------------------------------------------------------------
-- A project starts on a Start_Date that is nobody's End_Date (no task right before it).
-- A project ends on an End_Date that is nobody's Start_Date (no task right after it).
-- Pair each start with the first end after it (MIN).
-- Sort by length in days (DATEDIFF in MySQL, julianday difference in SQLite), then by start date.
SELECT s.Start_Date, MIN(e.End_Date) AS End_Date
FROM (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) s,
     (SELECT End_Date   FROM Projects WHERE End_Date   NOT IN (SELECT Start_Date FROM Projects)) e
WHERE s.Start_Date < e.End_Date
GROUP BY s.Start_Date
ORDER BY julianday(MIN(e.End_Date)) - julianday(s.Start_Date), s.Start_Date;
