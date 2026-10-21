-- Challenges  (Medium · Basic Join)  https://www.hackerrank.com/challenges/challenges/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Hackers;
DROP TABLE IF EXISTS Challenges;
-- Sample Input 0 (Sample Input 1 is loaded further down)
CREATE TABLE Hackers (hacker_id INTEGER, name TEXT);
INSERT INTO Hackers VALUES
    (5077, 'Rose'),
    (21283, 'Angela'),
    (62743, 'Frank'),
    (88255, 'Patrick'),
    (96196, 'Lisa');

CREATE TABLE Challenges (challenge_id INTEGER, hacker_id INTEGER);
INSERT INTO Challenges VALUES
    (61654, 5077),
    (58302, 21283),
    (40587, 88255),
    (29477, 5077),
    (1220, 21283),
    (69514, 21283),
    (46561, 62743),
    (58077, 62743),
    (18483, 88255),
    (76766, 21283),
    (52382, 5077),
    (74467, 21283),
    (33625, 96196),
    (26053, 88255),
    (42665, 62743),
    (12859, 62743),
    (70094, 21283),
    (34599, 88255),
    (54680, 88255),
    (61881, 5077);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): 21283 Angela 6 / 88255 Patrick 5 / 96196 Lisa 1 / 12299 Rose 6 / 34856 Angela 6 / 79345 Frank 4 / 80491 Patrick 3 / 81041 Lisa 1
-- ---------------------------------------------------------------------------
-- Count challenges per hacker.
-- Keep a hacker if their count is the maximum (ties allowed), or if no other hacker has the same count.
-- (SELECT COUNT(*) ... GROUP BY hacker_id) is the list of all counts; grouping that list by count and HAVING COUNT(*) = 1 gives counts used by exactly one hacker.
SELECT h.hacker_id, h.name, COUNT(c.challenge_id) AS total
FROM Hackers h
JOIN Challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total = (SELECT MAX(cnt)
                FROM (SELECT COUNT(*) AS cnt FROM Challenges GROUP BY hacker_id) m)
    OR total IN (SELECT cnt
                 FROM (SELECT COUNT(*) AS cnt FROM Challenges GROUP BY hacker_id) u
                 GROUP BY cnt
                 HAVING COUNT(*) = 1)
ORDER BY total DESC, h.hacker_id;

-- ---------------------------------------------------------------------------
-- SAMPLE INPUT 1: replace the data and run the same query again
-- ---------------------------------------------------------------------------
DELETE FROM Hackers;
DELETE FROM Challenges;
INSERT INTO Hackers VALUES
    (12299, 'Rose'),
    (34856, 'Angela'),
    (79345, 'Frank'),
    (80491, 'Patrick'),
    (81041, 'Lisa');
INSERT INTO Challenges VALUES
    (63963, 81041),
    (63117, 79345),
    (28225, 34856),
    (21989, 12299),
    (4653, 12299),
    (70070, 79345),
    (36905, 34856),
    (61136, 80491),
    (17234, 12299),
    (80308, 79345),
    (40510, 34856),
    (79820, 80491),
    (22720, 12299),
    (21394, 12299),
    (36261, 34856),
    (15334, 12299),
    (71435, 79345),
    (23157, 34856),
    (54102, 34856),
    (69065, 80491);

SELECT h.hacker_id, h.name, COUNT(c.challenge_id) AS total
FROM Hackers h
JOIN Challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total = (SELECT MAX(cnt)
                FROM (SELECT COUNT(*) AS cnt FROM Challenges GROUP BY hacker_id) m)
    OR total IN (SELECT cnt
                 FROM (SELECT COUNT(*) AS cnt FROM Challenges GROUP BY hacker_id) u
                 GROUP BY cnt
                 HAVING COUNT(*) = 1)
ORDER BY total DESC, h.hacker_id;
