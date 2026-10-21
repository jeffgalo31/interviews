<!-- study-layout -->
# Revising Aggregations - The Count Function

🟢 **Easy** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query a *count* of the number of cities in **CITY** having a *Population* larger than $100,000$.

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
> **Key idea:** `COUNT(*)` counts the rows that pass the `WHERE` filter.

### ✍️ The query

```sql
SELECT COUNT(*)
FROM CITY
WHERE POPULATION > 100000;
```

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [New Companies](../../advanced-select/new-companies/README.md) · [🗄️ All SQL exercises](../../README.md) · [Revising Aggregations - The Sum Function](../revising-aggregations-the-sum-function/README.md) ➡️
