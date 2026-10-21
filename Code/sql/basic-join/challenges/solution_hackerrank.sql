-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Challenges (Medium · Basic Join). Explained version: solution.sql
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
