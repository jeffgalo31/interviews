-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Weather Observation Station 19 (Medium · Aggregation). Explained version: solution.sql
SELECT ROUND(SQRT(POWER(MAX(LAT_N) - MIN(LAT_N), 2) + POWER(MAX(LONG_W) - MIN(LONG_W), 2)), 4)
FROM STATION;
