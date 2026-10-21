-- Top Competitors  (Medium · Basic Join)  https://www.hackerrank.com/challenges/full-score/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Hackers;
DROP TABLE IF EXISTS Difficulty;
DROP TABLE IF EXISTS Challenges;
DROP TABLE IF EXISTS Submissions;
CREATE TABLE Hackers (hacker_id INTEGER, name TEXT);
INSERT INTO Hackers VALUES (5580, 'Rose'), (8439, 'Angela'), (27205, 'Frank'), (52243, 'Patrick'), (52348, 'Lisa'),
                           (57645, 'Kimberly'), (77726, 'Bonnie'), (83082, 'Michael'), (86870, 'Todd'), (90411, 'Joe');

CREATE TABLE Difficulty (difficulty_level INTEGER, score INTEGER);
INSERT INTO Difficulty VALUES (1, 20), (2, 30), (3, 40), (4, 60), (5, 80), (6, 100), (7, 120);

CREATE TABLE Challenges (challenge_id INTEGER, hacker_id INTEGER, difficulty_level INTEGER);
INSERT INTO Challenges VALUES (4810, 77726, 4), (21089, 27205, 1), (36566, 5580, 7), (66730, 52243, 6), (71055, 52243, 2);

CREATE TABLE Submissions (submission_id INTEGER, hacker_id INTEGER, challenge_id INTEGER, score INTEGER);
INSERT INTO Submissions VALUES
    (68628, 77726, 36566, 30), (65300, 77726, 21089, 10), (40326, 52243, 36566, 77), (8941, 27205, 4810, 4),
    (83554, 77726, 66730, 30), (43353, 52243, 66730, 0),  (55385, 52348, 71055, 20), (39784, 27205, 71055, 23),
    (94613, 86870, 71055, 30), (45788, 52348, 36566, 0),  (93058, 86870, 36566, 30), (7344, 8439, 66730, 92),
    (2721, 8439, 4810, 36),    (523, 5580, 71055, 4),     (49105, 52348, 66730, 0),  (55877, 57645, 66730, 80),
    (38355, 27205, 66730, 35), (3924, 8439, 36566, 80),   (97397, 90411, 66730, 100), (84162, 83082, 4810, 40),
    (97431, 90411, 71055, 30);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): 90411 Joe
-- ---------------------------------------------------------------------------
-- Chain the joins: submission → its challenge → that challenge's difficulty (max score) → the hacker.
-- WHERE s.score = d.score keeps only full-score submissions.
-- HAVING filters groups (after counting): more than one full-score challenge.
SELECT h.hacker_id, h.name
FROM Submissions s
JOIN Challenges c ON s.challenge_id = c.challenge_id
JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
JOIN Hackers h    ON s.hacker_id = h.hacker_id
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(DISTINCT s.challenge_id) > 1
ORDER BY COUNT(DISTINCT s.challenge_id) DESC, h.hacker_id;
