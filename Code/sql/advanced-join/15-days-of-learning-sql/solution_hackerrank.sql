-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- 15 Days of Learning SQL (Hard · Advanced Join). Explained version: solution.sql
SELECT d.submission_date,
       -- hackers who submitted every single day from 03-01 up to this date
       (SELECT COUNT(DISTINCT s2.hacker_id)
          FROM Submissions s2
         WHERE s2.submission_date = d.submission_date
           AND (SELECT COUNT(DISTINCT s3.submission_date)
                  FROM Submissions s3
                 WHERE s3.hacker_id = s2.hacker_id
                   AND s3.submission_date < d.submission_date) = DATEDIFF(d.submission_date, '2016-03-01')) AS streak_hackers,
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
