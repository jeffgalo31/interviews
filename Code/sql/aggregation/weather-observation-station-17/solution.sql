-- Weather Observation Station 17  (Easy · Aggregation)  https://www.hackerrank.com/challenges/weather-observation-station-17/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (made up: HackerRank shows no sample for this one)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS STATION;
CREATE TABLE STATION (ID INTEGER, CITY TEXT, STATE TEXT, LAT_N REAL, LONG_W REAL);
INSERT INTO STATION VALUES
    (1, 'Acme',         'LA',  36.7,   41.2),
    (2, 'Ozark',        'AL',  50.9,   86.6),
    (3, 'Upton',        'WY', 103.2,  122.1),
    (4, 'Amo',          'IN',  75.5,   57.9),
    (5, 'Kissee Mills', 'MO', 139.65,  73.42),
    (6, 'Ozark',        'AL',  62.3,   45.9),
    (7, 'Loma Mar',     'CA',  48.69, 130.33),
    (8, 'Eros',         'LA', 137.2,   69.1),
    (9, 'Gustine',      'CA',  38.9,  140.5);

-- ---------------------------------------------------------------------------
-- QUERY
-- ---------------------------------------------------------------------------
-- Value from the row with the smallest LAT_N above the limit: sort ascending, keep 1 row.
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N
LIMIT 1;
