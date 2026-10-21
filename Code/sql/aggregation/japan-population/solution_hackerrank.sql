-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Japan Population (Easy · Aggregation). Explained version: solution.sql
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN';
