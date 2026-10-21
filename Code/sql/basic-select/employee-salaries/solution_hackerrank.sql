-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Employee Salaries (Easy · Basic Select). Explained version: solution.sql
SELECT name
FROM Employee
WHERE salary > 2000
  AND months < 10
ORDER BY employee_id;
