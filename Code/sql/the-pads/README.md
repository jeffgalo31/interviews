# The PADS

*HackerRank · SQL · Advanced Select*

Generate the following two result sets:

1. Query an alphabetically ordered list of all names in **OCCUPATIONS**, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: `AnActorName(A)`, `ADoctorName(D)`, `AProfessorName(P)`, and `ASingerName(S)`.
2. Query the number of ocurrences of each occupation in **OCCUPATIONS**. Sort the occurrences in ascending order, and output them in the following format:

   ```
   There are a total of [occupation_count] [occupation]s.
   ```

   where `[occupation_count]` is the number of occurrences of an occupation in **OCCUPATIONS** and `[occupation]` is the lowercase occupation name. If more than one Occupation has the same `[occupation_count]`, they should be ordered alphabetically.

**Note:** There will be at least two entries in the table for each type of occupation.

## Input Format

The **OCCUPATIONS** table is described as follows:

| Column | Type |
|---|---|
| Name | String |
| Occupation | String |

Occupation will only contain one of the following values: **Doctor**, **Professor**, **Singer** or **Actor**.

## Sample Input

An **OCCUPATIONS** table that contains the following records:

| Name | Occupation |
|---|---|
| Samantha | Doctor |
| Julia | Actor |
| Maria | Actor |
| Meera | Singer |
| Ashely | Professor |
| Ketty | Professor |
| Christeen | Professor |
| Jane | Actor |
| Jenny | Doctor |
| Priya | Singer |

## Sample Output

```
Ashely(P)
Christeen(P)
Jane(A)
Jenny(D)
Julia(A)
Ketty(P)
Maria(A)
Meera(S)
Priya(S)
Samantha(D)
There are a total of 2 doctors.
There are a total of 2 singers.
There are a total of 3 actors.
There are a total of 3 professors.
```

## Explanation

The results of the first query are formatted to the problem description's specifications.

The results of the second query are ascendingly ordered first by number of names corresponding to each profession (2 ≤ 2 ≤ 3 ≤ 3), and then alphabetically by profession (doctor ≤ singer, and actor ≤ professor).

## Solution

Two separate queries, run one after the other: HackerRank prints both result sets together.

**Query 1: name + first letter of the occupation**

```sql
SELECT CONCAT(Name, '(', LEFT(Occupation, 1), ')')
FROM OCCUPATIONS
ORDER BY Name;
```

- `LEFT(Occupation, 1)` takes the first letter: `Professor` → `P`.
- `CONCAT(...)` glues the pieces together: `Ashely` + `(` + `P` + `)` → `Ashely(P)`.
- `ORDER BY Name` sorts alphabetically.

**Query 2: count per occupation as a sentence**

```sql
SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(*), Occupation;
```

- `GROUP BY Occupation` makes one group per occupation (Actor, Doctor, Professor, Singer).
- `COUNT(*)` counts the rows in each group: Actor 3, Doctor 2, Professor 3, Singer 2.
- `LOWER(Occupation)` → `actor`, then `'s.'` makes it plural: `actors.`
- `ORDER BY COUNT(*), Occupation` sorts by the count first (2, 2, 3, 3); when counts tie,
  by occupation name (Doctor before Singer, Actor before Professor).

| Occupation | COUNT(*) | Output line |
|---|---|---|
| Doctor | 2 | There are a total of 2 doctors. |
| Singer | 2 | There are a total of 2 singers. |
| Actor | 3 | There are a total of 3 actors. |
| Professor | 3 | There are a total of 3 professors. |

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank, MySQL)
