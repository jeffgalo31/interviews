# Top Earners

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/earnings-of-employees/problem)

---

We define an employee's *total earnings* to be their monthly $salary \times  months$ worked, and the *maximum total earnings* to be the maximum total earnings for any employee in the **Employee** table. Write a query to find the _maximum total earnings_ for all employees as well as the total number of employees who have maximum total earnings. Then print these values as $2$ space-separated integers.

**Input Format**

The **Employee** table containing employee data for a company is described as follows: 

<img src="https://s3.amazonaws.com/hr-challenge-images/19629/1458557872-4396838885-ScreenShot2016-03-21at4.27.13PM.png"/>

where _employee\_id_ is an employee's ID number, _name_ is their name, _months_ is the total number of months they've been working for the company, and _salary_ is the their monthly salary.

**Sample Input**

![](https://s3.amazonaws.com/hr-challenge-images/19631/1458559098-23bf583125-ScreenShot2016-03-21at4.32.59PM.png)

**Sample Output**

```
69952 1
```

**Explanation**

> The explanation on HackerRank uses formulas that don't copy as text; see the [problem page](https://www.hackerrank.com/challenges/earnings-of-employees/problem). The Solution section below walks through it.

## Solution

```sql
SELECT salary * months AS earnings, COUNT(*)
FROM Employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;
```

- Group employees by their total earnings and count each group.
- Highest earnings first, keep only that row: the max and how many employees have it.

**Sample data in solution.sql:** the official HackerRank sample, so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
