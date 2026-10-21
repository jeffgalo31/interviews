# Revising Aggregations - Averages

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem)

---

Query the average population of all cities in **CITY** where *District* is **California**.

**Input Format**

The **CITY** table is described as follows:
<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" title="CITY.jpg" />

## Solution

```sql
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';
```

- `AVG` = sum / number of rows, over the filtered rows.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
