-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- African Cities (Easy · Basic Join). Explained version: solution.sql
SELECT CITY.NAME
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Africa';
