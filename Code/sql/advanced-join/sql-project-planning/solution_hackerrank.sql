-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- SQL Project Planning (Medium · Advanced Join). Explained version: solution.sql
SELECT s.Start_Date, MIN(e.End_Date)
FROM (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) s,
     (SELECT End_Date   FROM Projects WHERE End_Date   NOT IN (SELECT Start_Date FROM Projects)) e
WHERE s.Start_Date < e.End_Date
GROUP BY s.Start_Date
ORDER BY DATEDIFF(MIN(e.End_Date), s.Start_Date), s.Start_Date;
