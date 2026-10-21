# Weather Observation Station 10

**Difficulty:** Easy · **Section:** Basic Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-10/problem)

---

Query the list of *CITY* names from **STATION** that *do not end* with vowels. Your result cannot contain duplicates.

**Input Format**

The **STATION** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" title="Station.jpg" />

where *LAT\_N* is the northern latitude and *LONG\_W* is the western longitude.

## Solution

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTR(CITY, -1, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
```

- `SUBSTR(CITY, 1, 1)` is the first character, `SUBSTR(CITY, -1, 1)` the last (negative = count from the end).
- `LOWER(...)` so `A` and `a` both match the vowel list.
- `DISTINCT` because the result cannot contain duplicates.
- `NOT IN`: last letter is **not** a vowel.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
