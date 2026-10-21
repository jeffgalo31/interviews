<!-- study-layout -->
# Revising Aggregations - The Sum Function

🟢 **Easy** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/revising-aggregations-sum/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query the total population of all cities in **CITY** where *District* is **California**.

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
> **Key idea:** `SUM` adds the column over the filtered rows.

### ✍️ The query

```sql
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';
```

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Revising Aggregations - The Count Function](../revising-aggregations-the-count-function/README.md) · [🗄️ All SQL exercises](../../README.md) · [Revising Aggregations - Averages](../revising-aggregations-averages/README.md) ➡️
