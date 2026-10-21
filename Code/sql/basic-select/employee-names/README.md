<!-- study-layout -->
# Employee Names

🟢 **Easy** · 📁 **Basic Select** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/name-of-employees/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Write a query that prints a list of employee names (i.e.: the _name_ attribute) from the **Employee** table in alphabetical order.

## 📥 Input & output

### Input format

The **Employee** table containing employee data for a company is described as follows:

| Column | Type |
|---|---|
| employee_id | Integer |
| name | String |
| months | Integer |
| salary | Integer |

where _employee\_id_ is an employee's ID number, _name_ is their name, _months_ is the total number of months they've been working for the company, and _salary_ is their monthly salary.

## 🧪 Example

**Input**

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

**Output**

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

## 💡 Solution

> [!TIP]
> **Key idea:** `ORDER BY name` sorts alphabetically (ascending is the default).

### ✍️ The query

```sql
SELECT name
FROM Employee
ORDER BY name;
```

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [Higher Than 75 Marks](../higher-than-75-marks/README.md) · [🗄️ All SQL exercises](../../README.md) · [Employee Salaries](../employee-salaries/README.md) ➡️
