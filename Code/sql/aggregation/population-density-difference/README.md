# Population Density Difference

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/population-density-difference/problem)

---

Query the difference between the maximum and minimum populations in **CITY**.

**Input Format**

The **CITY** table is described as follows:
<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" title="CITY.jpg" />

## Solution

```sql
SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY;
```

- Two aggregates in one expression: largest minus smallest.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
