# Weather Observation Station 15

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-15/problem)

---

Query the *Western Longitude* (*LONG\_W*) for the largest *Northern Latitude* (*LAT\_N*) in **STATION** that is less than $137.2345$. Round your answer to $4$ decimal places.

**Input Format**

The **STATION** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" title="Station.jpg" />

where *LAT\_N* is the northern latitude and *LONG\_W* is the western longitude.

## Solution

```sql
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC
LIMIT 1;
```

- We need a value from the **row** with the largest LAT_N, so sort instead of using `MAX`: largest LAT_N first, keep 1 row.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
