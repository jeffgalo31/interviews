# Employee Names

**Difficulty:** Easy · **Section:** Basic Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/name-of-employees/problem)

---

Write a query that prints a list of employee names (i.e.: the _name_ attribute) from the **Employee** table in alphabetical order.

**Input Format**

The **Employee** table containing employee data for a company is described as follows: 

<img src="https://s3.amazonaws.com/hr-challenge-images/19629/1458557872-4396838885-ScreenShot2016-03-21at4.27.13PM.png"/>

where _employee\_id_ is an employee's ID number, _name_ is their name, _months_ is the total number of months they've been working for the company, and _salary_ is their monthly salary.

**Sample Input**

![](https://s3.amazonaws.com/hr-challenge-images/19629/1458558202-9a8721e44b-ScreenShot2016-03-21at4.32.59PM.png)

**Sample Output**

```
Angela
Bonnie
Frank
Joe
Kimberly
Lisa
Michael
Patrick
Rose
Todd
```

## Solution

```sql
SELECT name
FROM Employee
ORDER BY name;
```

- `ORDER BY name` sorts alphabetically (ascending is the default).

**Sample data in solution.sql:** the official HackerRank sample, so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
