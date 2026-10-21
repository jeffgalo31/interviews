<!-- study-layout -->
# Print Prime Numbers

🟡 **Medium** · 📁 **Alternative Queries** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/print-prime-numbers/problem)

**On this page:** [📝 Problem](#-problem) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Write a query to print all *prime numbers* less than or equal to $1000$. Print your result on a single line, and use the ampersand ($\&$) character as your separator (instead of a space).

For example, the output for all prime numbers $\leq 10$ would be:

	2&3&5&7

## 💡 Solution

> [!TIP]
> **Key idea:** A recursive CTE generates the numbers 2..1000.

### ✍️ The query

```sql
WITH RECURSIVE nums AS (
    SELECT 2 AS n
    UNION ALL
    SELECT n + 1 FROM nums WHERE n < 1000
)
SELECT GROUP_CONCAT(n ORDER BY n SEPARATOR '&')
FROM nums
WHERE NOT EXISTS (
    SELECT 1
    FROM nums d
    WHERE d.n * d.n <= nums.n      -- only divisors up to the square root
      AND nums.n % d.n = 0         -- d divides n -> not prime
);
```

### 🔍 How it works

- `NOT EXISTS`: keep n if no number d with d² ≤ n divides it evenly (`%` = remainder).
- `GROUP_CONCAT(... SEPARATOR '&')` joins them on one line (SQLite: `GROUP_CONCAT(n, '&')`).
- `WITH RECURSIVE` needs MySQL 8 (HackerRank's MySQL).

> [!NOTE]
> **Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `GROUP_CONCAT(n ORDER BY n SEPARATOR '&')` → `GROUP_CONCAT(n, '&')`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Draw The Triangle 2](../draw-the-triangle-2/README.md) · [🗄️ All SQL exercises](../../README.md)
