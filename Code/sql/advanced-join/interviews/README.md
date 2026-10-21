# Interviews

**Difficulty:** Hard · **Section:** Advanced Join · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/interviews/problem)

---

Samantha interviews many candidates from different colleges using coding challenges and contests. Write a query to print the _contest\_id_, _hacker\_id_, _name_, and the sums of _total\_submissions_, _total\_accepted\_submissions_, _total\_views_, and _total\_unique\_views_ for each contest sorted by _contest\_id_. Exclude the contest from the result if all four sums are $0$.

**Note:** A specific contest can be used to screen candidates at more than one college, but each college only holds $1$ screening contest.

----

**Input Format**

The following tables hold interview data:

- _Contests:_ The _contest\_id_ is the id of the contest, _hacker\_id_ is the id of the hacker who created the contest, and _name_ is the name of the hacker. <img src="https://s3.amazonaws.com/hr-challenge-images/19596/1458517426-e017c3460e-ScreenShot2016-03-21at4.57.47AM.png"/>

- _Colleges:_ The _college\_id_ is the id of the college, and _contest\_id_ is the id of the contest that Samantha used to screen the candidates. <img src="https://s3.amazonaws.com/hr-challenge-images/19596/1458517503-fd4aa63111-ScreenShot2016-03-21at4.57.56AM.png"/>

- _Challenges:_ The _challenge\_id_ is the id of the challenge that belongs to one of the contests whose contest_id Samantha forgot, and _college\_id_ is the id of the college where the challenge was given to candidates. <img src="https://s3.amazonaws.com/hr-challenge-images/19596/1458517661-a642f750ce-ScreenShot2016-03-21at4.58.04AM.png"/>

- _View\_Stats:_ The _challenge\_id_ is the id of the challenge, _total\_views_ is the number of times the challenge was viewed by candidates, and _total\_unique\_views_ is the number of times the challenge was viewed by unique candidates. <img src="https://s3.amazonaws.com/hr-challenge-images/19596/1458517983-b4302286a8-ScreenShot2016-03-21at4.58.15AM.png"/>

- _Submission\_Stats:_ The _challenge\_id_ is the id of the challenge, _total\_submissions_ is the number of submissions for the challenge, and _total\_accepted\_submission_ is the number of submissions that achieved full scores. <img src="https://s3.amazonaws.com/hr-challenge-images/19596/1458518090-80983c916a-ScreenShot2016-03-21at4.58.27AM.png"/>

----

**Sample Input**

Contests Table: ![](https://s3.amazonaws.com/hr-challenge-images/19596/1458519044-d788f8a6ee-ScreenShot2016-03-21at4.58.39AM.png) Colleges Table: ![](https://s3.amazonaws.com/hr-challenge-images/19596/1458519098-912836d6ac-ScreenShot2016-03-21at4.59.22AM.png) Challenges Table: ![](https://s3.amazonaws.com/hr-challenge-images/19596/1458519120-c531743caf-ScreenShot2016-03-21at4.59.32AM.png) View_Stats Table: ![](https://s3.amazonaws.com/hr-challenge-images/19596/1458519152-107a67866b-ScreenShot2016-03-21at4.59.43AM.png) Submission_Stats Table: ![](https://s3.amazonaws.com/hr-challenge-images/19596/1458519173-091aba871a-ScreenShot2016-03-21at4.59.55AM.png)

**Sample Output**

```
66406 17973 Rose 111 39 156 56
66556 79153 Angela 0 0 11 10
94828 80275 Frank 150 38 41 15
```

**Explanation**

> The explanation on HackerRank uses formulas that don't copy as text; see the [problem page](https://www.hackerrank.com/challenges/interviews/problem). The Solution section below walks through it.

## Solution

```sql
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
```

- Path: contest → colleges → challenges → stats.
- **Aggregate each stats table per challenge first** (the subqueries). Joining both raw stats tables directly would multiply rows and inflate the sums.
- `LEFT JOIN` + `COALESCE(..., 0)`: challenges without stats count as 0 instead of disappearing.
- `HAVING ... > 0` drops contests where all four sums are 0.

**Sample data in solution.sql:** rebuilt to reproduce HackerRank's Sample Output (the sample tables are images on HackerRank).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
