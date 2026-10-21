# Weather Observation Station 4

**Difficulty:** Easy · **Section:** Basic Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-4/problem)

---

Find the difference between the total number of **CITY** entries in the table and the number of distinct **CITY** entries in the table.  
The **STATION** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" title="Station.jpg" />

where **LAT\_N** is the northern latitude and **LONG\_W** is the western longitude.

For example, if there are three records in the table with **CITY** values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 'New York' and 'Bengalaru'.  The query returns $1$, because $\text{total number of records} - \text{number of unique city names} = 3 - 2 = 1$.

## Solution

```sql
SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION;
```

- `COUNT(CITY)` counts all rows, `COUNT(DISTINCT CITY)` counts unique names; the difference is the number of repeats.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
