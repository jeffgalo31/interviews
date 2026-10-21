-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Weather Observation Station 15 (Easy · Aggregation). Explained version: solution.sql
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC
LIMIT 1;
