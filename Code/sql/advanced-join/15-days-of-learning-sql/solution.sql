-- 15 Days of Learning SQL  (Hard · Advanced Join)  https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql  (differs: DATEDIFF(a, b) → CAST(julianday(a) - julianday(b) AS INTEGER))

-- ---------------------------------------------------------------------------
-- SETUP: sample data (official HackerRank sample)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Hackers;
DROP TABLE IF EXISTS Submissions;
-- The sample assumes the contest ended on March 06, 2016.
CREATE TABLE Hackers (hacker_id INTEGER, name TEXT);
INSERT INTO Hackers VALUES
    (15758, 'Rose'),
    (20703, 'Angela'),
    (36396, 'Frank'),
    (38289, 'Patrick'),
    (44065, 'Lisa'),
    (53473, 'Kimberly'),
    (62529, 'Bonnie'),
    (79722, 'Michael');

CREATE TABLE Submissions (submission_date TEXT, submission_id INTEGER, hacker_id INTEGER, score INTEGER);
INSERT INTO Submissions VALUES
    ('2016-03-01', 8494, 20703, 0),
    ('2016-03-01', 22403, 53473, 15),
    ('2016-03-01', 23965, 79722, 60),
    ('2016-03-01', 30173, 36396, 70),
    ('2016-03-02', 34928, 20703, 0),
    ('2016-03-02', 38740, 15758, 60),
    ('2016-03-02', 42769, 79722, 25),
    ('2016-03-02', 44364, 79722, 60),
    ('2016-03-03', 45440, 20703, 0),
    ('2016-03-03', 49050, 36396, 70),
    ('2016-03-03', 50273, 79722, 5),
    ('2016-03-04', 50344, 20703, 0),
    ('2016-03-04', 51360, 44065, 90),
    ('2016-03-04', 54404, 53473, 65),
    ('2016-03-04', 61533, 79722, 45),
    ('2016-03-05', 72852, 20703, 0),
    ('2016-03-05', 74546, 38289, 0),
    ('2016-03-05', 76487, 62529, 0),
    ('2016-03-05', 82439, 36396, 10),
    ('2016-03-05', 90006, 36396, 40),
    ('2016-03-06', 90404, 20703, 0);

-- ---------------------------------------------------------------------------
-- QUERY
-- Expected (HackerRank sample): 2016-03-01 4 20703 Angela / 2016-03-02 2 79722 Michael / 2016-03-03 2 20703 Angela / 2016-03-04 2 20703 Angela / 2016-03-05 1 36396 Frank / 2016-03-06 1 20703 Angela
-- ---------------------------------------------------------------------------
-- One output row per contest day (SELECT DISTINCT submission_date).
-- Streak count: a hacker is still in on day N if they submitted on all N−1 earlier days, i.e. their number of distinct earlier submission dates equals the days since March 1.
-- Top hacker: group that day's submissions by hacker, most submissions first, lowest id on ties, LIMIT 1; the same subquery is reused to look up the name.
-- Days since start: DATEDIFF(date, '2016-03-01') in MySQL, julianday difference in SQLite.
SELECT d.submission_date,
       -- hackers who submitted every single day from 03-01 up to this date
       (SELECT COUNT(DISTINCT s2.hacker_id)
          FROM Submissions s2
         WHERE s2.submission_date = d.submission_date
           AND (SELECT COUNT(DISTINCT s3.submission_date)
                  FROM Submissions s3
                 WHERE s3.hacker_id = s2.hacker_id
                   AND s3.submission_date < d.submission_date) = CAST(julianday(d.submission_date) - julianday('2016-03-01') AS INTEGER)) AS streak_hackers,
       -- hacker with the most submissions that day (lowest id on ties)
       (SELECT s4.hacker_id
          FROM Submissions s4
         WHERE s4.submission_date = d.submission_date
         GROUP BY s4.hacker_id
         ORDER BY COUNT(*) DESC, s4.hacker_id
         LIMIT 1) AS top_hacker_id,
       (SELECT h.name
          FROM Hackers h
         WHERE h.hacker_id = (SELECT s5.hacker_id
                                FROM Submissions s5
                               WHERE s5.submission_date = d.submission_date
                               GROUP BY s5.hacker_id
                               ORDER BY COUNT(*) DESC, s5.hacker_id
                               LIMIT 1)) AS top_hacker_name
FROM (SELECT DISTINCT submission_date FROM Submissions) d
ORDER BY d.submission_date;
