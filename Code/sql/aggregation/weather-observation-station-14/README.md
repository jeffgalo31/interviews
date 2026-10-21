# Weather Observation Station 14

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-14/problem)

---

Query the greatest value of the *Northern Latitudes* (*LAT\_N*) from **STATION** that is less than $137.2345$. Truncate your answer to $4$ decimal places.

**Input Format**

The **STATION** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" title="Station.jpg" />

where *LAT\_N* is the northern latitude and *LONG\_W* is the western longitude.

## Solution

```sql
SELECT TRUNCATE(MAX(LAT_N), 4)
FROM STATION
WHERE LAT_N < 137.2345;
```

- Largest value **below** the limit: filter first, then `MAX`.
- Truncate to 4 decimals (`TRUNCATE` in MySQL).

**Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `TRUNCATE(x, 4)` → `CAST(x * 10000 AS INTEGER) / 10000.0`.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
