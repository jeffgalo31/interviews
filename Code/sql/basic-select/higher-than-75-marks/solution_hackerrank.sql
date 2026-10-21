-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Higher Than 75 Marks (Easy · Basic Select). Explained version: solution.sql
SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
ORDER BY SUBSTR(NAME, -3), ID;
