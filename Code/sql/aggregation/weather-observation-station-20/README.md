# Weather Observation Station 20

**Difficulty:** Medium · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-20/problem)

---

A *[median](https://en.wikipedia.org/wiki/Median)* is defined as a number separating the higher half of a data set from the lower half. Query the *median* of the *Northern Latitudes* (*LAT\_N*) from **STATION** and round your answer to $4$ decimal places.

**Input Format**

The **STATION** table is described as follows:

*STATION*

| Field | Type |
|---|---|
| ID | NUMBER |
| CITY | VARCHAR2(21) |
| STATE | VARCHAR2(2) |
| LAT_N | NUMBER |
| LONG_W | NUMBER |

where *LAT\_N* is the northern latitude and *LONG\_W* is the western longitude.

## Solution

```sql
SELECT ROUND(s.LAT_N, 4)
FROM STATION s
WHERE (SELECT COUNT(*) FROM STATION WHERE LAT_N < s.LAT_N)
    = (SELECT COUNT(*) FROM STATION WHERE LAT_N > s.LAT_N);
```

- The median is the value with as many values below it as above it.
- For each row, count the smaller and the larger LAT_N values; keep the row where both counts are equal.
- Works when the row count is odd (HackerRank's STATION has 499 rows).

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
