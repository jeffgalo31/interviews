-- Weather Observation Station 5  (Easy · Basic Select)  https://www.hackerrank.com/challenges/weather-observation-station-5/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION (ID INTEGER, CITY TEXT, STATE TEXT, LAT_N REAL, LONG_W REAL);
INSERT INTO STATION (ID, CITY) VALUES (1, 'DEF'), (2, 'ABC'), (3, 'PQRS'), (4, 'WXY');

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): ABC 3 / PQRS 4
-- ---------------------------------------------------------------------------
-- Two separate queries (allowed by the note).
-- Shortest: sort by length ascending, ties alphabetically, keep the first row (LIMIT 1).
-- Longest: sort by length descending, ties still alphabetically, keep the first row.
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY), CITY
LIMIT 1;

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY
LIMIT 1;
