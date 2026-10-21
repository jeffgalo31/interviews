-- Contest Leaderboard  (Medium · Basic Join)  https://www.hackerrank.com/challenges/contest-leaderboard/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Hackers;
DROP TABLE IF EXISTS Submissions;
CREATE TABLE Hackers (hacker_id INTEGER, name TEXT);
INSERT INTO Hackers VALUES
    (4071, 'Rose'),
    (4806, 'Angela'),
    (26071, 'Frank'),
    (49438, 'Patrick'),
    (74842, 'Lisa'),
    (80305, 'Kimberly'),
    (84072, 'Bonnie'),
    (87868, 'Michael'),
    (92118, 'Todd'),
    (95895, 'Joe');

CREATE TABLE Submissions (submission_id INTEGER, hacker_id INTEGER, challenge_id INTEGER, score INTEGER);
INSERT INTO Submissions VALUES
    (67194, 74842, 63132, 76),
    (64479, 74842, 19797, 98),
    (40742, 26071, 49593, 20),
    (17513, 4806, 49593, 32),
    (69846, 80305, 19797, 19),
    (41002, 26071, 89343, 36),
    (52826, 49438, 49593, 9),
    (31093, 26071, 19797, 2),
    (81614, 84072, 49593, 100),
    (44829, 26071, 89343, 17),
    (75147, 80305, 49593, 48),
    (14115, 4806, 49593, 76),
    (6943, 4071, 19797, 95),
    (12855, 4806, 25917, 13),
    (73343, 80305, 49593, 42),
    (84264, 84072, 63132, 0),
    (9951, 4071, 49593, 43),
    (45104, 49438, 25917, 34),
    (53795, 74842, 19797, 5),
    (26363, 26071, 19797, 29),
    (10063, 4071, 49593, 96);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): 4071 Rose 191 / 74842 Lisa 174 / 84072 Bonnie 100 / 4806 Angela 89 / 26071 Frank 85 / 80305 Kimberly 67 / 49438 Patrick 43
-- ---------------------------------------------------------------------------
-- Step 1 (subquery): best score per hacker per challenge, so retries don't count twice.
-- Step 2: sum those best scores per hacker.
-- HAVING total_score > 0 removes hackers whose total is 0.
SELECT h.hacker_id, h.name, SUM(m.max_score) AS total_score
FROM Hackers h
JOIN (
    SELECT hacker_id, challenge_id, MAX(score) AS max_score
    FROM Submissions
    GROUP BY hacker_id, challenge_id
) m ON h.hacker_id = m.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total_score > 0
ORDER BY total_score DESC, h.hacker_id;
