# Interviews

**Difficulty:** Hard · **Section:** Advanced Join · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/interviews/problem)

---

Samantha interviews many candidates from different colleges using coding challenges and contests. Write a query to print the _contest\_id_, _hacker\_id_, _name_, and the sums of _total\_submissions_, _total\_accepted\_submissions_, _total\_views_, and _total\_unique\_views_ for each contest sorted by _contest\_id_. Exclude the contest from the result if all four sums are $0$.

**Note:** A specific contest can be used to screen candidates at more than one college, but each college only holds $1$ screening contest.

----

**Input Format**

The following tables hold interview data:

- _Contests:_ The _contest\_id_ is the id of the contest, _hacker\_id_ is the id of the hacker who created the contest, and _name_ is the name of the hacker.

| Column | Type |
|---|---|
| contest_id | Integer |
| hacker_id | Integer |
| name | String |

- _Colleges:_ The _college\_id_ is the id of the college, and _contest\_id_ is the id of the contest that Samantha used to screen the candidates.

| Column | Type |
|---|---|
| college_id | Integer |
| contest_id | Integer |

- _Challenges:_ The _challenge\_id_ is the id of the challenge that belongs to one of the contests whose contest_id Samantha forgot, and _college\_id_ is the id of the college where the challenge was given to candidates.

| Column | Type |
|---|---|
| challenge_id | Integer |
| college_id | Integer |

- _View\_Stats:_ The _challenge\_id_ is the id of the challenge, _total\_views_ is the number of times the challenge was viewed by candidates, and _total\_unique\_views_ is the number of times the challenge was viewed by unique candidates.

| Column | Type |
|---|---|
| challenge_id | Integer |
| total_views | Integer |
| total_unique_views | Integer |

- _Submission\_Stats:_ The _challenge\_id_ is the id of the challenge, _total\_submissions_ is the number of submissions for the challenge, and _total\_accepted\_submission_ is the number of submissions that achieved full scores.

| Column | Type |
|---|---|
| challenge_id | Integer |
| total_submissions | Integer |
| total_accepted_submissions | Integer |

----

**Sample Input**

Contests Table:

| contest_id | hacker_id | name |
|---|---|---|
| 66406 | 17973 | Rose |
| 66556 | 79153 | Angela |
| 94828 | 80275 | Frank |

 Colleges Table:

| college_id | contest_id |
|---|---|
| 11219 | 66406 |
| 32473 | 66556 |
| 56685 | 94828 |

 Challenges Table:

| challenge_id | college_id |
|---|---|
| 18765 | 11219 |
| 47127 | 11219 |
| 60292 | 32473 |
| 72974 | 56685 |

 View_Stats Table:

| challenge_id | total_views | total_unique_views |
|---|---|---|
| 47127 | 26 | 19 |
| 47127 | 15 | 14 |
| 18765 | 43 | 10 |
| 18765 | 72 | 13 |
| 75516 | 35 | 17 |
| 60292 | 11 | 10 |
| 72974 | 41 | 15 |
| 75516 | 75 | 11 |

 Submission_Stats Table:

| challenge_id | total_submissions | total_accepted_submissions |
|---|---|---|
| 75516 | 34 | 12 |
| 47127 | 27 | 10 |
| 47127 | 56 | 18 |
| 75516 | 74 | 12 |
| 75516 | 83 | 8 |
| 72974 | 68 | 24 |
| 72974 | 82 | 14 |
| 47127 | 28 | 11 |

**Sample Output**

```
66406 17973 Rose 111 39 156 56
66556 79153 Angela 0 0 11 10
94828 80275 Frank 150 38 41 15
```

**Explanation**

The contest 66406 is used in the college 11219. In this college 11219, challenges 18765 and 47127 are asked, so from the view and submission stats:

- Sum of total submissions = 27 + 56 + 28 = 111
- Sum of total accepted submissions = 10 + 18 + 11 = 39
- Sum of total views = 43 + 72 + 26 + 15 = 156
- Sum of total unique views = 10 + 13 + 19 + 14 = 56

Similarly, we can find the sums for contests 66556 and 94828.

> Numbers that appear as formulas on HackerRank are filled in here.

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

**Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
