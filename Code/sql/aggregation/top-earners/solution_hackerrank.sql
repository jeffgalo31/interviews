-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Top Earners (Easy · Aggregation). Explained version: solution.sql
SELECT salary * months AS earnings, COUNT(*)
FROM Employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;
