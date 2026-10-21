# Average Population

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/average-population/problem)

---

Query the average population for all cities in **CITY**, rounded *down* to the nearest integer.

**Input Format**

The **CITY** table is described as follows:
<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" title="CITY.jpg" />

## Solution

```sql
SELECT FLOOR(AVG(POPULATION))
FROM CITY;
```

- Rounded **down**: `FLOOR(AVG(...))` in MySQL.
- Local SQLite has no `FLOOR` by default; `CAST(... AS INTEGER)` cuts off the decimals, which is the same for positive numbers.

**Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `FLOOR(x)` → `CAST(x AS INTEGER)`.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
