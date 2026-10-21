# Population Census 

**Difficulty:** Easy · **Section:** Basic Join · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/asian-population/problem)

---

Given the **CITY** and **COUNTRY** tables, query the sum of the populations of all cities where the *CONTINENT* is *'Asia'*.
    
**Note:** *CITY.CountryCode* and *COUNTRY.Code* are matching key columns.

**Input Format**

The **CITY** and **COUNTRY** tables are described as follows:
<img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg" title="CITY.jpg" />

<img src="https://s3.amazonaws.com/hr-challenge-images/8342/1449769013-e54ce90480-Country.jpg" title="Country.jpg" />

## Solution

```sql
SELECT SUM(CITY.POPULATION)
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Asia';
```

- `JOIN ... ON` attaches each city's country row, so we can filter on CONTINENT.
- Then `SUM` the city populations.

**Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
