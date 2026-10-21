# Symmetric Pairs

**Difficulty:** Medium · **Section:** Advanced Join · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/symmetric-pairs/problem)

---

You are given a table, <em>Functions</em>, containing two columns: <em>X&nbsp;</em>and <em>Y</em>.

<img src="https://s3.amazonaws.com/hr-challenge-images/12892/1443818798-51909e977d-1.png" />

Two pairs <em>(X<sub>1</sub>, Y<sub>1</sub>)</em> and <em>(X<sub>2</sub>, Y<sub>2</sub>)</em> are said to be <em>symmetric</em> <em>pairs</em> if&nbsp;<em>X<sub>1</sub> = Y<sub>2</sub></em> and <em>X<sub>2</sub> = Y<sub>1</sub></em>.

Write a query to output all such <em>symmetric</em> <em>pairs</em> in ascending order by the value of <em>X</em>.  List the rows such that <em>X<sub>1</sub> &le; Y<sub>1</sub></em>.  

__Sample Input__

<img src="https://s3.amazonaws.com/hr-challenge-images/12892/1443818693-b384c24e35-2.png" />

__Sample Output__

    20 20
    20 21
    22 23

## Solution

```sql
SELECT f1.X, f1.Y
FROM Functions f1
JOIN Functions f2 ON f1.X = f2.Y AND f1.Y = f2.X
GROUP BY f1.X, f1.Y
HAVING f1.X < f1.Y OR COUNT(*) > 1
ORDER BY f1.X;
```

- Self-join: find a row whose (X, Y) is this row flipped.
- `X < Y` keeps one of each pair (20 21, not 21 20).
- When X = Y a row matches **itself**, so it only counts if that pair appears at least twice: `COUNT(*) > 1`.

**Sample data in solution.sql:** the official HackerRank sample, so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
