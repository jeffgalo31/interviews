-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Weather Observation Station 3 (Easy · Basic Select). Explained version: solution.sql
SELECT DISTINCT CITY
FROM STATION
WHERE ID % 2 = 0;
