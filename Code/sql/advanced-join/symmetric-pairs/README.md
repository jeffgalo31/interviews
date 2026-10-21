<!-- study-layout -->
# Symmetric Pairs

🟡 **Medium** · 📁 **Advanced Join** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/symmetric-pairs/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You are given a table, <em>Functions</em>, containing two columns: <em>X&nbsp;</em>and <em>Y</em>.

| Column | Type |
|---|---|
| X | Integer |
| Y | Integer |

Two pairs <em>(X<sub>1</sub>, Y<sub>1</sub>)</em> and <em>(X<sub>2</sub>, Y<sub>2</sub>)</em> are said to be <em>symmetric</em> <em>pairs</em> if&nbsp;<em>X<sub>1</sub> = Y<sub>2</sub></em> and <em>X<sub>2</sub> = Y<sub>1</sub></em>.

Write a query to output all such <em>symmetric</em> <em>pairs</em> in ascending order by the value of <em>X</em>.  List the rows such that <em>X<sub>1</sub> &le; Y<sub>1</sub></em>.

## 🧪 Example

**Input**

| X | Y |
|---|---|
| 20 | 20 |
| 20 | 20 |
| 20 | 21 |
| 23 | 22 |
| 22 | 23 |
| 21 | 20 |

**Output**

    20 20
    20 21
    22 23

## 💡 Solution

> [!TIP]
> **Key idea:** Self-join: find a row whose (X, Y) is this row flipped.

### ✍️ The query

```sql
SELECT f1.X, f1.Y
FROM Functions f1
JOIN Functions f2 ON f1.X = f2.Y AND f1.Y = f2.X
GROUP BY f1.X, f1.Y
HAVING f1.X < f1.Y OR COUNT(*) > 1
ORDER BY f1.X;
```

### 🔍 How it works

- `X < Y` keeps one of each pair (20 21, not 21 20).
- When X = Y a row matches **itself**, so it only counts if that pair appears at least twice: `COUNT(*) > 1`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [Placements](../placements/README.md) · [🗄️ All SQL exercises](../../README.md) · [Interviews](../interviews/README.md) ➡️
