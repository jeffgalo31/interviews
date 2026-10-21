-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Average Population of Each Continent (Easy · Basic Join). Explained version: solution.sql
SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;
