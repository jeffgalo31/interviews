-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Placements (Medium · Advanced Join). Explained version: solution.sql
SELECT s.Name
FROM Students s
JOIN Friends  f  ON s.ID = f.ID
JOIN Packages me ON s.ID = me.ID
JOIN Packages fr ON f.Friend_ID = fr.ID
WHERE fr.Salary > me.Salary
ORDER BY fr.Salary;
