<!-- study-layout -->
# Type of Triangle

🟢 **Easy** · 📁 **Advanced Select** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/what-type-of-triangle/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Write a query identifying the *type* of each record in the **TRIANGLES** table using its three side lengths. Output one of the following statements for each record in the table:

- **Equilateral**: It's a triangle with $3$ sides of equal length.
- **Isosceles**: It's a triangle with $2$ sides of equal length.
- **Scalene**: It's a triangle with $3$ sides of differing lengths.
- **Not A Triangle**: The given values of *A*, *B*, and *C* don't form a triangle.

## 📥 Input & output

### Input format

The **TRIANGLES** table is described as follows:

| Column | Type |
|---|---|
| A | Integer |
| B | Integer |
| C | Integer |

Each row in the table denotes the lengths of each of a triangle's three sides.

## 🧪 Example

**Input**

| A | B | C |
|---|---|---|
| 20 | 20 | 23 |
| 20 | 20 | 20 |
| 20 | 21 | 22 |
| 13 | 14 | 30 |

**Output**

```
Isosceles
Equilateral
Scalene
Not A Triangle
```

**Why**

Values in the tuple (20, 20, 23) form an Isosceles triangle, because A ≡ B.

Values in the tuple (20, 20, 20) form an Equilateral triangle, because A ≡ B ≡ C.

Values in the tuple (20, 21, 22) form a Scalene triangle, because A ≠ B ≠ C.

Values in the tuple (13, 14, 30) cannot form a triangle because the combined value of sides A and B is not larger than that of side C.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** Check **Not A Triangle first**: `CASE` stops at the first true `WHEN`, and (13, 13, 30) would otherwise be labeled Isosceles.

### ✍️ The query

```sql
SELECT CASE
           WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
           WHEN A = B AND B = C                       THEN 'Equilateral'
           WHEN A = B OR B = C OR A = C               THEN 'Isosceles'
           ELSE 'Scalene'
       END
FROM TRIANGLES;
```

### 🔍 How it works

- A triangle needs every pair of sides to add up to more than the third side.
- Then all three equal, then any two equal, otherwise all different.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [Employee Salaries](../../basic-select/employee-salaries/README.md) · [🗄️ All SQL exercises](../../README.md) · [The PADS](../the-pads/README.md) ➡️
