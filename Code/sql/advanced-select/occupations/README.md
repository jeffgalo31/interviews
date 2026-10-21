# Occupations

**Difficulty:** Medium · **Section:** Advanced Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/occupations/problem)

---

[Pivot](https://en.wikipedia.org/wiki/Pivot_table) the *Occupation* column in **OCCUPATIONS** so that each *Name* is sorted alphabetically and displayed underneath its corresponding *Occupation*. The output should consist of four columns (*Doctor*, *Professor*, *Singer*, and *Actor*) in that specific order, with their respective names listed alphabetically under each column.

**Note:** Print **NULL** when there are no more names corresponding to an occupation.

**Input Format**

The **OCCUPATIONS** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/12889/1443816414-2a465532e7-1.png" />

*Occupation* will only contain one of the following values: **Doctor**, **Professor**, **Singer** or **Actor**.

**Sample Input**

![](https://s3.amazonaws.com/hr-challenge-images/12890/1443817648-1b2b8add45-2.png)

**Sample Output**

```
Jenny    Ashley     Meera  Jane
Samantha Christeen  Priya  Julia
NULL     Ketty      NULL   Maria
```

**Explanation**

The first column is an alphabetically ordered list of Doctor names. 
 The second column is an alphabetically ordered list of Professor names. 
 The third column is an alphabetically ordered list of Singer names. 
 The fourth column is an alphabetically ordered list of Actor names. 
 The empty cell data for columns with less than the maximum number of names per occupation (in this case, the Professor and Actor columns) are filled with **NULL**  values.

## Solution

```sql
SELECT MAX(CASE WHEN Occupation = 'Doctor'    THEN Name END) AS Doctor,
       MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS Professor,
       MAX(CASE WHEN Occupation = 'Singer'    THEN Name END) AS Singer,
       MAX(CASE WHEN Occupation = 'Actor'     THEN Name END) AS Actor
FROM (
    SELECT Name, Occupation,
           ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS rn
    FROM OCCUPATIONS
) ranked
GROUP BY rn
ORDER BY rn;
```

- `ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name)` numbers the names 1, 2, 3... inside each occupation, alphabetically.
- `GROUP BY rn` makes one output row per position: row 1 holds the 1st doctor, 1st professor, ...
- `MAX(CASE WHEN ... THEN Name END)` picks the one name for that column; when an occupation has no name at that position it is NULL.
- Window functions need MySQL 8 (HackerRank's MySQL) / SQLite 3.25+.

**Sample data in solution.sql:** the official HackerRank sample, so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
