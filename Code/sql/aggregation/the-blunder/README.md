# The Blunder

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/the-blunder/problem)

---

Samantha was tasked with calculating the average monthly salaries for all employees in the **EMPLOYEES** table, but did not realize her keyboard's $0$ key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: $actual - miscalculated$ average monthly salaries), and round it up to the next integer.

**Input Format**

The **EMPLOYEES** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/12893/1443817108-adc2235c81-1.png" />

**Note:**  *Salary* is per month.

**Constraints**

$1000 \lt \text{Salary} \lt 10^5$.

**Sample Input**

![](https://s3.amazonaws.com/hr-challenge-images/12893/1443817161-299cc6eb7f-2.png)

**Sample Output**

```
2061
```

**Explanation**

> The explanation on HackerRank uses formulas that don't copy as text; see the [problem page](https://www.hackerrank.com/challenges/the-blunder/problem). The Solution section below walks through it.

## Solution

```sql
SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', '')))
FROM EMPLOYEES;
```

- Samantha's salaries = the real salaries with every `0` removed: `REPLACE(Salary, '0', '')` (1420 → 142).
- Error = real average − miscalculated average, then round **up** with `CEIL`.
- Local SQLite: no `CEIL`, so it adds 1 when there is a decimal part.

**Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `CEIL(x)` → integer part + 1 if there are decimals.

**Sample data in solution.sql:** the official HackerRank sample, so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
