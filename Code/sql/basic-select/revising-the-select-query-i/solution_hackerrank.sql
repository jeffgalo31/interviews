-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Revising the Select Query I (Easy · Basic Select). Explained version: solution.sql
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'USA'
  AND POPULATION > 100000;
