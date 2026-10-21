# Revising Aggregations - The Count Function

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem)

---

Query a *count* of the number of cities in **CITY** having a *Population* larger than $100,000$.

**Input Format**

The **CITY** table is described as follows:
<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" title="CITY.jpg" />

## Solution

```sql
SELECT COUNT(*)
FROM CITY
WHERE POPULATION > 100000;
```

- `COUNT(*)` counts the rows that pass the `WHERE` filter.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
