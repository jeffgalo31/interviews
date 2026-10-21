# Weather Observation Station 2

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-2/problem)

---

Query the following two values from the **STATION** table:

1. The sum of all values in *LAT\_N* rounded to a scale of $2$ decimal places.
2. The sum of all values in *LONG\_W* rounded to a scale of $2$ decimal places.

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

**Output Format**

Your results must be in the form:

	lat lon

where $lat$ is the sum of all values in *LAT\_N* and $lon$ is the sum of all values in *LONG\_W*. Both results must be rounded to a scale of $2$ decimal places.

## Solution

```sql
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2)
FROM STATION;
```

- `ROUND(x, 2)` keeps 2 decimal places.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
