# Type of Triangle

**Difficulty:** Easy · **Section:** Advanced Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/what-type-of-triangle/problem)

---

Write a query identifying the *type* of each record in the **TRIANGLES** table using its three side lengths. Output one of the following statements for each record in the table:

- **Equilateral**: It's a triangle with $3$ sides of equal length.
- **Isosceles**: It's a triangle with $2$ sides of equal length.
- **Scalene**: It's a triangle with $3$ sides of differing lengths.
- **Not A Triangle**: The given values of *A*, *B*, and *C* don't form a triangle.

**Input Format**

The **TRIANGLES** table is described as follows:

<img src="https://s3.amazonaws.com/hr-challenge-images/12887/1443815629-ac2a843fb7-1.png" />

Each row in the table denotes the lengths of each of a triangle's three sides.

**Sample Input**

![](https://s3.amazonaws.com/hr-challenge-images/12887/1443815827-cbfc1ca12b-2.png)

**Sample Output**

```
Isosceles
Equilateral
Scalene
Not A Triangle
```

**Explanation**

> The explanation on HackerRank uses formulas that don't copy as text; see the [problem page](https://www.hackerrank.com/challenges/what-type-of-triangle/problem). The Solution section below walks through it.

## Solution

```sql
SELECT CASE
           WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
           WHEN A = B AND B = C                       THEN 'Equilateral'
           WHEN A = B OR B = C OR A = C               THEN 'Isosceles'
           ELSE 'Scalene'
       END
FROM TRIANGLES;
```

- Check **Not A Triangle first**: `CASE` stops at the first true `WHEN`, and (13, 13, 30) would otherwise be labeled Isosceles.
- A triangle needs every pair of sides to add up to more than the third side.
- Then all three equal, then any two equal, otherwise all different.

**Sample data in solution.sql:** the official HackerRank sample, so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
