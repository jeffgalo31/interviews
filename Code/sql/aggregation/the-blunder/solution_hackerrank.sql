-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- The Blunder (Easy · Aggregation). Explained version: solution.sql
SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', '')))
FROM EMPLOYEES;
