-- Interviews  (Hard · Advanced Join)  https://www.hackerrank.com/challenges/interviews/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (rebuilt from HackerRank's sample output)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Contests;
DROP TABLE IF EXISTS Colleges;
DROP TABLE IF EXISTS Challenges;
DROP TABLE IF EXISTS View_Stats;
DROP TABLE IF EXISTS Submission_Stats;
CREATE TABLE Contests (contest_id INTEGER, hacker_id INTEGER, name TEXT);
INSERT INTO Contests VALUES (66406, 17973, 'Rose'), (66556, 79153, 'Angela'), (94828, 80275, 'Frank'), (70000, 12345, 'Lisa');

CREATE TABLE Colleges (college_id INTEGER, contest_id INTEGER);
INSERT INTO Colleges VALUES (11219, 66406), (11220, 66406), (32473, 66556), (56685, 94828), (60000, 70000);

CREATE TABLE Challenges (challenge_id INTEGER, college_id INTEGER);
INSERT INTO Challenges VALUES (18765, 11219), (47127, 11219), (90000, 11220), (60292, 32473), (72974, 56685), (80000, 60000);

CREATE TABLE View_Stats (challenge_id INTEGER, total_views INTEGER, total_unique_views INTEGER);
INSERT INTO View_Stats VALUES (47127, 26, 19), (47127, 15, 14), (18765, 43, 10), (18765, 72, 13), (60292, 11, 10), (72974, 41, 15);

CREATE TABLE Submission_Stats (challenge_id INTEGER, total_submissions INTEGER, total_accepted_submissions INTEGER);
INSERT INTO Submission_Stats VALUES (47127, 27, 10), (47127, 56, 18), (18765, 28, 11), (90000, 0, 0), (72974, 150, 38);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): 66406 17973 Rose 111 39 156 56 / 66556 79153 Angela 0 0 11 10 / 94828 80275 Frank 150 38 41 15
-- ---------------------------------------------------------------------------
-- Path: contest → colleges → challenges → stats.
-- Aggregate each stats table per challenge first (the subqueries). Joining both raw stats tables directly would multiply rows and inflate the sums.
-- LEFT JOIN + COALESCE(..., 0): challenges without stats count as 0 instead of disappearing.
-- HAVING ... > 0 drops contests where all four sums are 0.
SELECT c.contest_id, c.hacker_id, c.name,
       SUM(COALESCE(s.ts, 0))  AS total_submissions,
       SUM(COALESCE(s.tas, 0)) AS total_accepted_submissions,
       SUM(COALESCE(v.tv, 0))  AS total_views,
       SUM(COALESCE(v.tuv, 0)) AS total_unique_views
FROM Contests c
JOIN Colleges   col ON c.contest_id = col.contest_id
JOIN Challenges ch  ON col.college_id = ch.college_id
LEFT JOIN (SELECT challenge_id, SUM(total_views) AS tv, SUM(total_unique_views) AS tuv
           FROM View_Stats GROUP BY challenge_id) v ON ch.challenge_id = v.challenge_id
LEFT JOIN (SELECT challenge_id, SUM(total_submissions) AS ts, SUM(total_accepted_submissions) AS tas
           FROM Submission_Stats GROUP BY challenge_id) s ON ch.challenge_id = s.challenge_id
GROUP BY c.contest_id, c.hacker_id, c.name
HAVING SUM(COALESCE(s.ts, 0)) + SUM(COALESCE(s.tas, 0)) + SUM(COALESCE(v.tv, 0)) + SUM(COALESCE(v.tuv, 0)) > 0
ORDER BY c.contest_id;
