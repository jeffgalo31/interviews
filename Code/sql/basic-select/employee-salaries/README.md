# Employee Salaries

**Difficulty:** Easy · **Section:** Basic Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/salary-of-employees/problem)

---

Write a query that prints a list of employee names (i.e.: the *name* attribute) for employees in **Employee** having a salary greater than $\$2000$ per month who have been employees for less than $10$ months. Sort your result by ascending _employee\_id_.

**Input Format**

The **Employee** table containing employee data for a company is described as follows: 

<img src="https://s3.amazonaws.com/hr-challenge-images/19629/1458557872-4396838885-ScreenShot2016-03-21at4.27.13PM.png"/>

where _employee\_id_ is an employee's ID number, _name_ is their name, _months_ is the total number of months they've been working for the company, and _salary_ is the their monthly salary.

**Sample Input**

![](https://s3.amazonaws.com/hr-challenge-images/19630/1458558612-af3da3ceb7-ScreenShot2016-03-21at4.32.59PM.png)

**Sample Output**

```
Angela
Michael
Todd
Joe
```

**Explanation**

> The explanation on HackerRank uses formulas that don't copy as text; see the [problem page](https://www.hackerrank.com/challenges/salary-of-employees/problem). The Solution section below walks through it.

## Solution

```sql
SELECT name
FROM Employee
WHERE salary > 2000
  AND months < 10
ORDER BY employee_id;
```

- Both conditions with `AND`.
- Output is sorted by `employee_id`, even though only `name` is printed.

**Sample data in solution.sql:** the official HackerRank sample, so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
