-- Contest Leaderboard  (Medium · Basic Join)  https://www.hackerrank.com/challenges/contest-leaderboard/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (rebuilt from HackerRank's sample output)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Hackers;
DROP TABLE IF EXISTS Submissions;
CREATE TABLE Hackers (hacker_id INTEGER, name TEXT);
INSERT INTO Hackers VALUES (4071, 'Rose'), (4806, 'Angela'), (26071, 'Frank'), (49438, 'Patrick'), (74842, 'Lisa'),
                           (80305, 'Kimberly'), (84072, 'Bonnie'), (87868, 'Michael'), (92118, 'Todd'), (95895, 'Joe');

CREATE TABLE Submissions (submission_id INTEGER, hacker_id INTEGER, challenge_id INTEGER, score INTEGER);
INSERT INTO Submissions VALUES
    (1, 4071, 19797, 95),  (2, 4071, 19797, 43),  (3, 4071, 49593, 96),
    (4, 74842, 19797, 98), (5, 74842, 19797, 5),  (6, 74842, 63132, 76),
    (7, 84072, 49593, 100), (8, 84072, 63132, 0),
    (9, 4806, 49593, 89),  (10, 4806, 49593, 30),
    (11, 26071, 19797, 85),
    (12, 80305, 19797, 67), (13, 80305, 19797, 0),
    (14, 49438, 49593, 43),
    (15, 87868, 63132, 0);

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
