-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Weather Observation Station 8 (Easy · Basic Select). Explained version: solution.sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTR(CITY, 1, 1)) IN ('a', 'e', 'i', 'o', 'u')
  AND LOWER(SUBSTR(CITY, -1, 1)) IN ('a', 'e', 'i', 'o', 'u');
