-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Weather Observation Station 4 (Easy · Basic Select). Explained version: solution.sql
SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION;
