<!-- study-layout -->
# Higher Than 75 Marks

🟢 **Easy** · 📁 **Basic Select** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/more-than-75-marks/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query the *Name* of any student in **STUDENTS** who scored higher than $75$ *Marks*. Order your output by the *last three characters* of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending *ID*.

## 📥 Input & output

### Input format

The **STUDENTS** table is described as follows:

| Column | Type |
|---|---|
| ID | Integer |
| Name | String |
| Marks | Integer |

The *Name* column only contains uppercase (`A`-`Z`) and lowercase (`a`-`z`) letters.

## 🧪 Example

**Input**

| ID | Name | Marks |
|---|---|---|
| 1 | Ashley | 81 |
| 2 | Samantha | 75 |
| 4 | Julia | 76 |
| 3 | Belvet | 84 |

**Output**

```
Ashley
Julia
Belvet
```

**Why**

Only Ashley, Julia, and Belvet have Marks > 75. If you look at the last three characters of each of their names, there are no duplicates and 'ley' < 'lia' < 'vet'.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** `SUBSTR(NAME, -3)` = last three characters (`RIGHT(NAME, 3)` is the same in MySQL).

### ✍️ The query

```sql
SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
ORDER BY SUBSTR(NAME, -3), ID;
```

### 🔍 How it works

- Second sort key `ID` breaks ties when two names end the same way.
- `> 75` excludes Samantha's exact 75.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [Weather Observation Station 12](../weather-observation-station-12/README.md) · [🗄️ All SQL exercises](../../README.md) · [Employee Names](../employee-names/README.md) ➡️
