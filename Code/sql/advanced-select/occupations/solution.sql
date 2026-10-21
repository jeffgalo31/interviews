-- Occupations  (Medium · Advanced Select)  https://www.hackerrank.com/challenges/occupations/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS OCCUPATIONS;
CREATE TABLE OCCUPATIONS (Name TEXT, Occupation TEXT);
INSERT INTO OCCUPATIONS VALUES
    ('Samantha', 'Doctor'),
    ('Julia', 'Actor'),
    ('Maria', 'Actor'),
    ('Meera', 'Singer'),
    ('Ashely', 'Professor'),
    ('Ketty', 'Professor'),
    ('Christeen', 'Professor'),
    ('Jane', 'Actor'),
    ('Jenny', 'Doctor'),
    ('Priya', 'Singer');

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): Jenny Ashely Meera Jane / Samantha Christeen Priya Julia / NULL Ketty NULL Maria
-- ---------------------------------------------------------------------------
-- ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) numbers the names 1, 2, 3... inside each occupation, alphabetically.
-- GROUP BY rn makes one output row per position: row 1 holds the 1st doctor, 1st professor, ...
-- MAX(CASE WHEN ... THEN Name END) picks the one name for that column; when an occupation has no name at that position it is NULL.
-- Window functions need MySQL 8 (HackerRank's MySQL) / SQLite 3.25+.
-- HackerRank's sample table spells the name Ashely while its Sample Output says Ashley (a typo on HackerRank); the local run prints Ashely.
SELECT MAX(CASE WHEN Occupation = 'Doctor'    THEN Name END) AS Doctor,
       MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS Professor,
       MAX(CASE WHEN Occupation = 'Singer'    THEN Name END) AS Singer,
       MAX(CASE WHEN Occupation = 'Actor'     THEN Name END) AS Actor
FROM (
    SELECT Name, Occupation,
           ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS rn
    FROM OCCUPATIONS
) ranked
GROUP BY rn
ORDER BY rn;
