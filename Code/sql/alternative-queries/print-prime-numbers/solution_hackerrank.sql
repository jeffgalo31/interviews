-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Print Prime Numbers (Medium · Alternative Queries). Explained version: solution.sql
WITH RECURSIVE nums AS (
    SELECT 2 AS n
    UNION ALL
    SELECT n + 1 FROM nums WHERE n < 1000
)
SELECT GROUP_CONCAT(n ORDER BY n SEPARATOR '&')
FROM nums
WHERE NOT EXISTS (
    SELECT 1
    FROM nums d
    WHERE d.n * d.n <= nums.n      -- only divisors up to the square root
      AND nums.n % d.n = 0         -- d divides n -> not prime
);
