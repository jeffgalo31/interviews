-- Ollivander's Inventory  (Medium · Basic Join)  https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (rebuilt from HackerRank's sample output)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Wands_Property;
DROP TABLE IF EXISTS Wands;
CREATE TABLE Wands_Property (code INTEGER, age INTEGER, is_evil INTEGER);
INSERT INTO Wands_Property VALUES (1, 45, 0), (2, 40, 0), (3, 4, 1), (4, 20, 0), (5, 17, 0);

CREATE TABLE Wands (id INTEGER, code INTEGER, coins_needed INTEGER, power INTEGER);
INSERT INTO Wands VALUES
    (1, 4, 3688, 8),  (2, 1, 8000, 10), (3, 3, 1000, 8), (4, 2, 7000, 7),  (5, 1, 6020, 2),
    (6, 4, 8000, 6),  (7, 5, 10000, 10), (8, 2, 3500, 3), (9, 1, 1647, 10), (10, 4, 504, 5),
    (11, 2, 7587, 5), (12, 5, 9897, 10), (13, 4, 700, 5), (14, 2, 5408, 1), (15, 2, 6018, 7),
    (16, 1, 6100, 2), (17, 3, 100, 1),   (18, 2, 3312, 3), (19, 4, 7651, 6), (20, 5, 5689, 3);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): 9 45 1647 10 / 12 17 9897 10 / 1 20 3688 8 / 15 40 6018 7 / 19 20 7651 6 / 11 40 7587 5 / 10 20 504 5 / 18 40 3312 3 / 20 17 5689 3 / 5 45 6020 2 / 14 40 5408 1
-- ---------------------------------------------------------------------------
-- Join each wand to its property row to get age and is_evil.
-- For every (age, power) combination keep only the cheapest wand: the subquery finds that minimum for the current row's age and power.
-- Exclude evil wands; sort by power, then age, both descending.
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
