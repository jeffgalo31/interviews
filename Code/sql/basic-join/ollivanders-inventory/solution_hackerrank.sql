-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Ollivander's Inventory (Medium · Basic Join). Explained version: solution.sql
SELECT w.id, p.age, w.coins_needed, w.power
FROM Wands w
JOIN Wands_Property p ON w.code = p.code
WHERE p.is_evil = 0
  AND w.coins_needed = (
        SELECT MIN(w2.coins_needed)
        FROM Wands w2
        JOIN Wands_Property p2 ON w2.code = p2.code
        WHERE p2.age = p.age
          AND w2.power = w.power
      )
ORDER BY w.power DESC, p.age DESC;
