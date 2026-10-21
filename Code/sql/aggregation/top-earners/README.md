# Top Earners

**Difficulty:** Easy · **Section:** Aggregation · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/earnings-of-employees/problem)

---

We define an employee's *total earnings* to be their monthly $salary \times  months$ worked, and the *maximum total earnings* to be the maximum total earnings for any employee in the **Employee** table. Write a query to find the _maximum total earnings_ for all employees as well as the total number of employees who have maximum total earnings. Then print these values as $2$ space-separated integers.

**Input Format**

The **Employee** table containing employee data for a company is described as follows:

| Column | Type |
|---|---|
| employee_id | Integer |
| name | String |
| months | Integer |
| salary | Integer |

where _employee\_id_ is an employee's ID number, _name_ is their name, _months_ is the total number of months they've been working for the company, and _salary_ is the their monthly salary.

**Sample Input**

| employee_id | name | months | salary |
|---|---|---|---|
| 12228 | Rose | 15 | 1968 |
| 33645 | Angela | 1 | 3443 |
| 45692 | Frank | 17 | 1608 |
| 56118 | Patrick | 7 | 1345 |
| 59725 | Lisa | 11 | 2330 |
| 74197 | Kimberly | 16 | 4372 |
| 78454 | Bonnie | 8 | 1771 |
| 83565 | Michael | 6 | 2017 |
| 98607 | Todd | 5 | 3396 |
| 99989 | Joe | 9 | 3573 |

**Sample Output**

```
69952 1
```

**Explanation**

The table and earnings data is depicted in the following diagram:

| employee_id | name | months | salary | earnings |
|---|---|---|---|---|
| 12228 | Rose | 15 | 1968 | 29520 |
| 33645 | Angela | 1 | 3443 | 3443 |
| 45692 | Frank | 17 | 1608 | 27336 |
| 56118 | Patrick | 7 | 1345 | 9415 |
| 59725 | Lisa | 11 | 2330 | 25630 |
| 74197 | Kimberly | 16 | 4372 | 69952 |
| 78454 | Bonnie | 8 | 1771 | 14168 |
| 83565 | Michael | 6 | 2017 | 12102 |
| 98607 | Todd | 5 | 3396 | 16980 |
| 99989 | Joe | 9 | 3573 | 32157 |

The maximum earnings value is 69952. The only employee with earnings = 69952 is Kimberly, so we print the maximum earnings value (69952) and a count of the number of employees who have earned $69952 (which is 1) as two space-separated values.

> Numbers that appear as formulas on HackerRank are filled in here.

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

**Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
