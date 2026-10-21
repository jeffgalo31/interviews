<!-- study-layout -->
# Occupations

🟡 **Medium** · 📁 **Advanced Select** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/occupations/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

[Pivot](https://en.wikipedia.org/wiki/Pivot_table) the *Occupation* column in **OCCUPATIONS** so that each *Name* is sorted alphabetically and displayed underneath its corresponding *Occupation*. The output should consist of four columns (*Doctor*, *Professor*, *Singer*, and *Actor*) in that specific order, with their respective names listed alphabetically under each column.

**Note:** Print **NULL** when there are no more names corresponding to an occupation.

## 📥 Input & output

### Input format

The **OCCUPATIONS** table is described as follows:

| Column | Type |
|---|---|
| Name | String |
| Occupation | String |

*Occupation* will only contain one of the following values: **Doctor**, **Professor**, **Singer** or **Actor**.

## 🧪 Example

**Input**

| Name | Occupation |
|---|---|
| Samantha | Doctor |
| Julia | Actor |
| Maria | Actor |
| Meera | Singer |
| Ashely | Professor |
| Ketty | Professor |
| Christeen | Professor |
| Jane | Actor |
| Jenny | Doctor |
| Priya | Singer |

**Output**

```
Jenny    Ashley     Meera  Jane
Samantha Christeen  Priya  Julia
NULL     Ketty      NULL   Maria
```

**Why**

The first column is an alphabetically ordered list of Doctor names.
 The second column is an alphabetically ordered list of Professor names.
 The third column is an alphabetically ordered list of Singer names.
 The fourth column is an alphabetically ordered list of Actor names.
 The empty cell data for columns with less than the maximum number of names per occupation (in this case, the Professor and Actor columns) are filled with **NULL**  values.

## 💡 Solution

> [!TIP]
> **Key idea:** `ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name)` numbers the names 1, 2, 3... inside each occupation, alphabetically.

### ✍️ The query

```sql
SELECT MAX(CASE WHEN Occupation = 'Doctor'    THEN Name END) AS Doctor,
       MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS Professor,
       MAX(CASE WHEN Occupation = 'Singer'    THEN Name END) AS Singer,
       MAX(CASE WHEN Occupation = 'Actor'     THEN Name END) AS Actor
FROM (
    SELECT Name, Occupation,
           ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS rn
    FROM OCCUPATIONS
) ranked
GROUP BY rn
ORDER BY rn;
```

### 🔍 How it works

- `GROUP BY rn` makes one output row per position: row 1 holds the 1st doctor, 1st professor, ...
- `MAX(CASE WHEN ... THEN Name END)` picks the one name for that column; when an occupation has no name at that position it is NULL.
- Window functions need MySQL 8 (HackerRank's MySQL) / SQLite 3.25+.
- HackerRank's sample table spells the name **Ashely** while its Sample Output says **Ashley** (a typo on HackerRank); the local run prints Ashely.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [The PADS](../the-pads/README.md) · [🗄️ All SQL exercises](../../README.md) · [Binary Tree Nodes](../binary-tree-nodes/README.md) ➡️
