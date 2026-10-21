# Weather Observation Station 13

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-13/problem)

---

Query the sum of *Northern Latitudes* (*LAT\_N*) from **STATION** having values greater than $38.7880$ and less than $137.2345$. Truncate your answer to $4$ decimal places.

**Input Format**

The **STATION** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" title="Station.jpg" />

where *LAT\_N* is the northern latitude and *LONG\_W* is the western longitude.

## Solution

```sql
SELECT TRUNCATE(SUM(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7880
  AND LAT_N < 137.2345;
```

- **Truncate** (cut off) to 4 decimals, not round: `TRUNCATE(x, 4)` in MySQL.
- Local SQLite: multiply by 10000, drop the decimals, divide back.

**Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `TRUNCATE(x, 4)` → `CAST(x * 10000 AS INTEGER) / 10000.0`.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
