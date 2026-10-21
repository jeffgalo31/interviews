<!-- study-layout -->
# The Blunder

🟢 **Easy** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/the-blunder/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Samantha was tasked with calculating the average monthly salaries for all employees in the **EMPLOYEES** table, but did not realize her keyboard's $0$ key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: $actual - miscalculated$ average monthly salaries), and round it up to the next integer.

## 📥 Input & output

### Input format

The **EMPLOYEES** table is described as follows:

| Column | Type |
|---|---|
| ID | Integer |
| Name | String |
| Salary | Integer |

**Note:**  *Salary* is per month.

### Constraints

$1000 \lt \text{Salary} \lt 10^5$.

## 🧪 Example

**Input**

| ID | Name | Salary |
|---|---|---|
| 1 | Kristeen | 1420 |
| 2 | Ashley | 2006 |
| 3 | Julia | 2210 |
| 4 | Maria | 3000 |

**Output**

```
2061
```

**Why**

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

## 💡 Solution

> [!TIP]
> **Key idea:** Samantha's salaries = the real salaries with every `0` removed: `REPLACE(Salary, '0', '')` (1420 → 142).

### ✍️ The query

```sql
SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', '')))
FROM EMPLOYEES;
```

### 🔍 How it works

- Error = real average − miscalculated average, then round **up** with `CEIL`.
- Local SQLite: no `CEIL`, so it adds 1 when there is a decimal part.

> [!NOTE]
> **Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `CEIL(x)` → integer part + 1 if there are decimals.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [Population Density Difference](../population-density-difference/README.md) · [🗄️ All SQL exercises](../../README.md) · [Top Earners](../top-earners/README.md) ➡️
