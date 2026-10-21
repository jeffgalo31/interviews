<!-- study-layout -->
# Average Population

🟢 **Easy** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/average-population/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query the average population for all cities in **CITY**, rounded *down* to the nearest integer.

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
> **Key idea:** Rounded **down**: `FLOOR(AVG(...))` in MySQL.

### ✍️ The query

```sql
SELECT FLOOR(AVG(POPULATION))
FROM CITY;
```

### 🔍 How it works

- Local SQLite has no `FLOOR` by default; `CAST(... AS INTEGER)` cuts off the decimals, which is the same for positive numbers.

> [!NOTE]
> **Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `FLOOR(x)` → `CAST(x AS INTEGER)`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Revising Aggregations - Averages](../revising-aggregations-averages/README.md) · [🗄️ All SQL exercises](../../README.md) · [Japan Population](../japan-population/README.md) ➡️
