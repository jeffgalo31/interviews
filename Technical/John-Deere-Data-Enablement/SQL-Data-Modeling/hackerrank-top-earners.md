# HackerRank: Top Earners

**Type:** HackerRank SQL challenge
**Source:** [Top Earners](https://www.hackerrank.com/challenges/earnings-of-employees/problem)
**Focus:** derived measures, aggregation, maxima, ties

## Exercise

Employee earnings equal months worked multiplied by monthly salary. Return the maximum earnings and the number of employees who have that amount.

Example `Employee` rows:

| employee_id | name | months | salary |
|---:|---|---:|---:|
| 1 | Ada | 6 | 10 |
| 2 | Ben | 3 | 20 |
| 3 | Chen | 2 | 15 |

Earnings are `60`, `60`, and `30`. The expected output is the maximum and the number of employees tied at that maximum:

```text
60 2
```

## Solution

```sql
WITH employee_earnings AS (
    SELECT months * salary AS total_earnings
    FROM Employee
),
maximum_earnings AS (
    SELECT MAX(total_earnings) AS total_earnings
    FROM employee_earnings
)
SELECT maximum_earnings.total_earnings,
       COUNT(*) AS employee_count
FROM employee_earnings
JOIN maximum_earnings
  ON maximum_earnings.total_earnings = employee_earnings.total_earnings
GROUP BY maximum_earnings.total_earnings;
```

The equality join retains every employee tied for the maximum, so the count is correct without a dialect-specific `LIMIT` clause.
