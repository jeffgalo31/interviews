-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Interviews (Hard · Advanced Join). Explained version: solution.sql
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
