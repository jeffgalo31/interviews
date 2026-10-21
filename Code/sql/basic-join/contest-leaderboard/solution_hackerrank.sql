-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Contest Leaderboard (Medium · Basic Join). Explained version: solution.sql
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
