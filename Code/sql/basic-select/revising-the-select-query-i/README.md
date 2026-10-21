# Revising the Select Query I

**Difficulty:** Easy · **Section:** Basic Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/revising-the-select-query/problem)

---

Query all columns for all American cities in the **CITY** table with populations larger than `100000`. The **CountryCode** for America is `USA`. 

The **CITY** table is described as follows:  

![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Solution

```sql
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'USA'
  AND POPULATION > 100000;
```

- `SELECT *` returns every column.
- `WHERE` keeps only rows where **both** conditions are true (`AND`).

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
