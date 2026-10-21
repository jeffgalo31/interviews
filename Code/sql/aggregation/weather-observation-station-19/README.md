# Weather Observation Station 19

**Difficulty:** Medium · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-19/problem)

---

Consider $P_1(a, c)$ and $P_2(b, d)$ to be two points on a 2D plane where $(a, b)$ are the respective minimum and maximum values of *Northern Latitude* (*LAT\_N*) and $(c, d)$ are the respective minimum and maximum values of *Western Longitude* (*LONG\_W*) in **STATION**.

Query the [Euclidean Distance](https://en.wikipedia.org/wiki/Euclidean_distance) between points $P_1$ and $P_2$ and *format your answer* to display $4$ decimal digits.

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
SELECT ROUND(SQRT(POWER(MAX(LAT_N) - MIN(LAT_N), 2) + POWER(MAX(LONG_W) - MIN(LONG_W), 2)), 4)
FROM STATION;
```

- Euclidean distance = √((b − a)² + (d − c)²) with a, b = min/max LAT_N and c, d = min/max LONG_W.
- Local SQLite needs `SQRT` (built in on most current builds); if yours says "no such function", the HackerRank version still works.

**Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `POWER(x, 2)` → `x * x`.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
