-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Weather Observation Station 20 (Medium · Aggregation). Explained version: solution.sql
SELECT ROUND(s.LAT_N, 4)
FROM STATION s
WHERE (SELECT COUNT(*) FROM STATION WHERE LAT_N < s.LAT_N)
    = (SELECT COUNT(*) FROM STATION WHERE LAT_N > s.LAT_N);
