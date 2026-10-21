-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- The Report (Medium · Basic Join). Explained version: solution.sql
SELECT CASE WHEN g.Grade >= 8 THEN s.Name ELSE NULL END AS Name,
       g.Grade,
       s.Marks
FROM Students s
JOIN Grades g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY g.Grade DESC,
         CASE WHEN g.Grade >= 8 THEN s.Name END,
         s.Marks;
