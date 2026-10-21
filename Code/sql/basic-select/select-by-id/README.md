# Select By ID

**Difficulty:** Easy · **Section:** Basic Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/select-by-id/problem)

---

Query all columns for a city in **CITY** with the *ID* `1661`.

The **CITY** table is described as follows:  
<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" title="CITY.jpg" />

## Solution

```sql
SELECT *
FROM CITY
WHERE ID = 1661;
```

- Filter on the primary key: returns one row.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
