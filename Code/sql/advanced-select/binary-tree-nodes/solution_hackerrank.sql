-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Binary Tree Nodes (Medium · Advanced Select). Explained version: solution.sql
SELECT N,
       CASE
           WHEN P IS NULL THEN 'Root'
           WHEN N IN (SELECT P FROM BST) THEN 'Inner'
           ELSE 'Leaf'
       END
FROM BST
ORDER BY N;
