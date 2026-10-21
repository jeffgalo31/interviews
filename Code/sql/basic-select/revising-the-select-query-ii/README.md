# Revising the Select Query II

**Difficulty:** Easy · **Section:** Basic Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/revising-the-select-query-2/problem)

---

Query the **NAME** field for all American cities in the **CITY** table with populations larger than `120000`. The *CountryCode* for America is `USA`. 

The **CITY** table is described as follows:  
![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Solution

```sql
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'USA'
  AND POPULATION > 120000;
```

- Same filter idea as part I, but only the `NAME` column is selected.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
