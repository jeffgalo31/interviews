-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Population Census  (Easy · Basic Join). Explained version: solution.sql
SELECT SUM(CITY.POPULATION)
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Asia';
