-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Population Density Difference (Easy · Aggregation). Explained version: solution.sql
SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY;
