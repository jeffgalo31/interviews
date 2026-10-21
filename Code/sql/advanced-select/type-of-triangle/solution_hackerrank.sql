-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Type of Triangle (Easy · Advanced Select). Explained version: solution.sql
SELECT CASE
           WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
           WHEN A = B AND B = C                       THEN 'Equilateral'
           WHEN A = B OR B = C OR A = C               THEN 'Isosceles'
           ELSE 'Scalene'
       END
FROM TRIANGLES;
