-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Weather Observation Station 18 (Medium · Aggregation). Explained version: solution.sql
SELECT ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)), 4)
FROM STATION;
