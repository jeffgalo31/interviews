# Top Competitors

**Difficulty:** Medium · **Section:** Basic Join · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/full-score/problem)

---

Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective _hacker\_id_ and _name_ of hackers who achieved full scores for *more than one* challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending _hacker\_id_.

----

**Input Format**

The following tables contain contest data:

- _Hackers:_ The _hacker\_id_ is the id of the hacker, and _name_ is the name of the hacker. <img src="https://s3.amazonaws.com/hr-challenge-images/19504/1458526776-67667350b4-ScreenShot2016-03-21at7.45.59AM.png"/>

- _Difficulty:_ The _difficult\_level_ is the level of difficulty of the challenge,  and _score_ is the maximum score that can be achieved for a challenge at that difficulty level. <img src="https://s3.amazonaws.com/hr-challenge-images/19504/1458526915-57eb75d9a2-ScreenShot2016-03-21at7.46.09AM.png"/>

- _Challenges:_ The _challenge\_id_ is the id of the challenge, the _hacker\_id_ is the id of the hacker who created the challenge, and _difficulty\_level_ is the level of difficulty of the challenge. <img src="https://s3.amazonaws.com/hr-challenge-images/19504/1458527032-f9ca650442-ScreenShot2016-03-21at7.46.17AM.png"/>

- _Submissions:_ The _submission\_id_ is the id of the submission, _hacker\_id_ is the id of the hacker who made the submission, _challenge\_id_ is the id of the challenge that the submission belongs to, and _score_ is the score of the submission. <img src="https://s3.amazonaws.com/hr-challenge-images/19504/1458527077-298f8e922a-ScreenShot2016-03-21at7.46.29AM.png"/>

----

**Sample Input**

Hackers Table: ![](https://s3.amazonaws.com/hr-challenge-images/19504/1458527241-6922b4ad87-ScreenShot2016-03-21at7.47.02AM.png) Difficulty Table: ![](https://s3.amazonaws.com/hr-challenge-images/19504/1458527265-7ad6852a13-ScreenShot2016-03-21at7.46.50AM.png) Challenges Table: ![](https://s3.amazonaws.com/hr-challenge-images/19504/1458527285-01e95eb6ec-ScreenShot2016-03-21at7.46.40AM.png) Submissions Table: ![](https://s3.amazonaws.com/hr-challenge-images/19504/1458527812-479a74b99f-ScreenShot2016-03-21at8.06.05AM.png)

**Sample Output**

```
90411 Joe
```

**Explanation**

> The explanation on HackerRank uses formulas that don't copy as text; see the [problem page](https://www.hackerrank.com/challenges/full-score/problem). The Solution section below walks through it.

## Solution

```sql
SELECT h.hacker_id, h.name
FROM Submissions s
JOIN Challenges c ON s.challenge_id = c.challenge_id
JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
JOIN Hackers h    ON s.hacker_id = h.hacker_id
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(DISTINCT s.challenge_id) > 1
ORDER BY COUNT(DISTINCT s.challenge_id) DESC, h.hacker_id;
```

- Chain the joins: submission → its challenge → that challenge's difficulty (max score) → the hacker.
- `WHERE s.score = d.score` keeps only full-score submissions.
- `HAVING` filters groups (after counting): more than one full-score challenge.

**Sample data in solution.sql:** rebuilt to reproduce HackerRank's Sample Output (the sample tables are images on HackerRank).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
