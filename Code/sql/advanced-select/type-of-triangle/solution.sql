-- Type of Triangle  (Easy · Advanced Select)  https://www.hackerrank.com/challenges/what-type-of-triangle/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS TRIANGLES;
CREATE TABLE TRIANGLES (A INTEGER, B INTEGER, C INTEGER);
INSERT INTO TRIANGLES VALUES (20, 20, 23), (20, 20, 20), (20, 21, 22), (13, 14, 30);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): Isosceles / Equilateral / Scalene / Not A Triangle
-- ---------------------------------------------------------------------------
-- Check Not A Triangle first: CASE stops at the first true WHEN, and (13, 13, 30) would otherwise be labeled Isosceles.
-- A triangle needs every pair of sides to add up to more than the third side.
-- Then all three equal, then any two equal, otherwise all different.
SELECT CASE
           WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
           WHEN A = B AND B = C                       THEN 'Equilateral'
           WHEN A = B OR B = C OR A = C               THEN 'Isosceles'
           ELSE 'Scalene'
       END
FROM TRIANGLES;
