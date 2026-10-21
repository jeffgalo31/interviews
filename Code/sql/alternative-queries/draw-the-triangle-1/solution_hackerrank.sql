-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Draw The Triangle 1 (Easy · Alternative Queries). Explained version: solution.sql
SET @n := 21;
SELECT REPEAT('* ', @n := @n - 1)
FROM information_schema.tables
LIMIT 20;
