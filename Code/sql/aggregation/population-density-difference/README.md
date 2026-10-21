<!-- study-layout -->
# Population Density Difference

🟢 **Easy** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/population-density-difference/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query the difference between the maximum and minimum populations in **CITY**.

## 📥 Input & output

### Input format

The **CITY** table is described as follows:

*CITY*

| Field | Type |
|---|---|
| ID | NUMBER |
| NAME | VARCHAR2(17) |
| COUNTRYCODE | VARCHAR2(3) |
| DISTRICT | VARCHAR2(20) |
| POPULATION | NUMBER |

## 💡 Solution

> [!TIP]
> **Key idea:** Two aggregates in one expression: largest minus smallest.

### ✍️ The query

```sql
SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY;
```

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Japan Population](../japan-population/README.md) · [🗄️ All SQL exercises](../../README.md) · [The Blunder](../the-blunder/README.md) ➡️
