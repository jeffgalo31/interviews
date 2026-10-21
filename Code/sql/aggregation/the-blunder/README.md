# The Blunder

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/the-blunder/problem)

---

Samantha was tasked with calculating the average monthly salaries for all employees in the **EMPLOYEES** table, but did not realize her keyboard's $0$ key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: $actual - miscalculated$ average monthly salaries), and round it up to the next integer.

**Input Format**

The **EMPLOYEES** table is described as follows:

| Column | Type |
|---|---|
| ID | Integer |
| Name | String |
| Salary | Integer |

**Note:**  *Salary* is per month.

**Constraints**

$1000 \lt \text{Salary} \lt 10^5$.

**Sample Input**

| ID | Name | Salary |
|---|---|---|
| 1 | Kristeen | 1420 |
| 2 | Ashley | 2006 |
| 3 | Julia | 2210 |
| 4 | Maria | 3000 |

**Sample Output**

```
2061
```

**Explanation**

The table below shows the salaries without zeros as they were entered by Samantha:

| ID | Name | Salary |
|---|---|---|
| 1 | Kristeen | 142 |
| 2 | Ashley | 26 |
| 3 | Julia | 221 |
| 4 | Maria | 3 |

Samantha computes an average salary of 98.00. The actual average salary is 2159.00.

The resulting error between the two calculations is 2159.00 − 98.00 = 2061.00. Since it is equal to the integer 2061, it does not get rounded up.

> Numbers that appear as formulas on HackerRank are filled in here.

## Solution

```sql
SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', '')))
FROM EMPLOYEES;
```

- Samantha's salaries = the real salaries with every `0` removed: `REPLACE(Salary, '0', '')` (1420 → 142).
- Error = real average − miscalculated average, then round **up** with `CEIL`.
- Local SQLite: no `CEIL`, so it adds 1 when there is a decimal part.

**Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `CEIL(x)` → integer part + 1 if there are decimals.

**Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
