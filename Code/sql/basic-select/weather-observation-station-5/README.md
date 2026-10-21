# Weather Observation Station 5

**Difficulty:** Easy · **Section:** Basic Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/weather-observation-station-5/problem)

---

Query the two cities in **STATION** with the shortest and longest *CITY* names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.  
The **STATION** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg" title="Station.jpg" />

where **LAT\_N** is the northern latitude and **LONG\_W** is the western longitude.

**Sample Input**

For example, **CITY**  has four entries: **DEF, ABC, PQRS**  and **WXY** .

**Sample Output**

```
ABC 3
PQRS 4
```

**Explanation**

> The explanation on HackerRank uses formulas that don't copy as text; see the [problem page](https://www.hackerrank.com/challenges/weather-observation-station-5/problem). The Solution section below walks through it.

**Note**  
 You can write two separate queries to get the desired output. It need not be a single query.

## Solution

```sql
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY), CITY
LIMIT 1;

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY
LIMIT 1;
```

- Two separate queries (allowed by the note).
- Shortest: sort by length ascending, ties alphabetically, keep the first row (`LIMIT 1`).
- Longest: sort by length **descending**, ties still alphabetically, keep the first row.

**Sample data in solution.sql:** the official HackerRank sample, so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
