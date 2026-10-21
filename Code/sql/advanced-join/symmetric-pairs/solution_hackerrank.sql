-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Symmetric Pairs (Medium · Advanced Join). Explained version: solution.sql
SELECT f1.X, f1.Y
FROM Functions f1
JOIN Functions f2 ON f1.X = f2.Y AND f1.Y = f2.X
GROUP BY f1.X, f1.Y
HAVING f1.X < f1.Y OR COUNT(*) > 1
ORDER BY f1.X;
