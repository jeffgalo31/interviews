# HackerRank: Interviews

**Type:** HackerRank SQL challenge
**Source:** [Interviews](https://www.hackerrank.com/challenges/interviews/problem)
**Focus:** multi-table joins, aggregation, avoiding duplicate counts, null handling

## Exercise

For each contest, follow the relationships `Contests -> Colleges -> Challenges` and total its challenge statistics. Return exactly one row per contest with these columns, in order: `contest_id`, `hacker_id`, `name`, total submissions, total accepted submissions, total views, and total unique views. Order rows by `contest_id`. Exclude a contest only when all four totals are zero.

The stats tables can contain multiple rows for one challenge. Here is a small illustrative dataset (not the HackerRank sample input):

**Contests**

| contest_id | hacker_id | name |
|---:|---:|---|
| 100 | 7 | DataSprint |

**Colleges**

| college_id | contest_id |
|---:|---:|
| 10 | 100 |

**Challenges**

| challenge_id | college_id |
|---:|---:|
| 501 | 10 |

**Submission_Stats**

| challenge_id | total_submissions | total_accepted_submissions |
|---:|---:|---:|
| 501 | 10 | 4 |
| 501 | 5 | 2 |

**View_Stats**

| challenge_id | total_views | total_unique_views |
|---:|---:|---:|
| 501 | 20 | 12 |
| 501 | 8 | 5 |

Expected output:

```text
100 7 DataSprint 15 6 28 17
```

If raw submission and view rows are joined first, the two rows from each table create four joined rows. Aggregating each stats table by `challenge_id` first avoids that fan-out and gives the totals above.

## Solution

Aggregate each stats table to one row per challenge before joining. This prevents submissions from multiplying against multiple view rows (or vice versa).

```sql
WITH submission_totals AS (
    SELECT challenge_id,
           SUM(total_submissions) AS total_submissions,
           SUM(total_accepted_submissions) AS total_accepted_submissions
    FROM Submission_Stats
    GROUP BY challenge_id
),
view_totals AS (
    SELECT challenge_id,
           SUM(total_views) AS total_views,
           SUM(total_unique_views) AS total_unique_views
    FROM View_Stats
    GROUP BY challenge_id
)
SELECT contest.contest_id,
       contest.hacker_id,
       contest.name,
       SUM(COALESCE(submission_totals.total_submissions, 0)) AS total_submissions,
       SUM(COALESCE(submission_totals.total_accepted_submissions, 0)) AS total_accepted_submissions,
       SUM(COALESCE(view_totals.total_views, 0)) AS total_views,
       SUM(COALESCE(view_totals.total_unique_views, 0)) AS total_unique_views
FROM Contests AS contest
JOIN Colleges AS college
  ON college.contest_id = contest.contest_id
JOIN Challenges AS challenge
  ON challenge.college_id = college.college_id
LEFT JOIN submission_totals
  ON submission_totals.challenge_id = challenge.challenge_id
LEFT JOIN view_totals
  ON view_totals.challenge_id = challenge.challenge_id
GROUP BY contest.contest_id, contest.hacker_id, contest.name
HAVING SUM(COALESCE(submission_totals.total_submissions, 0))
     + SUM(COALESCE(submission_totals.total_accepted_submissions, 0))
     + SUM(COALESCE(view_totals.total_views, 0))
     + SUM(COALESCE(view_totals.total_unique_views, 0)) > 0
ORDER BY contest.contest_id;
```

**Key check:** Aggregate `Submission_Stats` and `View_Stats` independently before joining. Joining raw stats can create a many-to-many product and overcount totals.
