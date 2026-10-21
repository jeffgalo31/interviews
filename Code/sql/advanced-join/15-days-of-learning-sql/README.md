# 15 Days of Learning SQL

**Difficulty:** Hard · **Section:** Advanced Join · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem)

---

Julia conducted a $15$ days of learning SQL contest. The start date of the contest was _March 01, 2016_ and the end date was _March 15, 2016_. 

Write a query to print total number of unique hackers who made at least $1$ submission each day (starting on the first day of the contest), and find the _hacker\_id_ and _name_ of the hacker who made maximum number of submissions each day. If more than one such hacker has a maximum number of submissions, print the lowest *hacker\_id*. The query should print this information for each day of the contest, sorted by the date.

----

**Input Format**

The following tables hold contest data:

- _Hackers:_ The _hacker\_id_ is the id of the hacker, and _name_ is the name of the hacker.<img src="https://s3.amazonaws.com/hr-challenge-images/19597/1458511164-12adec3b8b-ScreenShot2016-03-21at3.26.47AM.png"/>

- _Submissions:_ The _submission\_date_ is the date of the submission, _submission\_id_ is the id of the submission, _hacker\_id_ is the id of the hacker who made the submission, and _score_ is the score of the submission. <img src="https://s3.amazonaws.com/hr-challenge-images/19597/1458511251-0b534030b9-ScreenShot2016-03-21at3.26.56AM.png"/>

**Sample Input**

For the following sample input, assume that the end date of the contest was March 06, 2016.
 
Hackers Table: ![](https://s3.amazonaws.com/hr-challenge-images/19597/1458511957-814a2c7bf2-ScreenShot2016-03-21at3.27.06AM.png) Submissions Table: ![](https://s3.amazonaws.com/hr-challenge-images/19597/1458512015-ff6a708164-ScreenShot2016-03-21at3.27.21AM.png)

**Sample Output**

```
2016-03-01 4 20703 Angela
2016-03-02 2 79722 Michael
2016-03-03 2 20703 Angela
2016-03-04 2 20703 Angela
2016-03-05 1 36396 Frank
2016-03-06 1 20703 Angela
```

**Explanation**

> The explanation on HackerRank uses formulas that don't copy as text; see the [problem page](https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem). The Solution section below walks through it.

## Solution

```sql
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
```

- One output row per contest day (`SELECT DISTINCT submission_date`).
- **Streak count:** a hacker is still in on day N if they submitted on all N−1 earlier days, i.e. their number of distinct earlier submission dates equals the days since March 1.
- **Top hacker:** group that day's submissions by hacker, most submissions first, lowest id on ties, `LIMIT 1`; the same subquery is reused to look up the name.
- Days since start: `DATEDIFF(date, '2016-03-01')` in MySQL, `julianday` difference in SQLite.

**Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `DATEDIFF(a, b)` → `CAST(julianday(a) - julianday(b) AS INTEGER)`.

**Sample data in solution.sql:** rebuilt to reproduce HackerRank's Sample Output (the sample tables are images on HackerRank).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
