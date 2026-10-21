-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).
-- Top Competitors (Medium · Basic Join). Explained version: solution.sql
SELECT h.hacker_id, h.name
FROM Submissions s
JOIN Challenges c ON s.challenge_id = c.challenge_id
JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
JOIN Hackers h    ON s.hacker_id = h.hacker_id
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(DISTINCT s.challenge_id) > 1
ORDER BY COUNT(DISTINCT s.challenge_id) DESC, h.hacker_id;
