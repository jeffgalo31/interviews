<!-- study-layout -->
# Select By ID

🟢 **Easy** · 📁 **Basic Select** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/select-by-id/problem)

**On this page:** [📝 Problem](#-problem) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query all columns for a city in **CITY** with the *ID* `1661`.

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
> **Key idea:** Filter on the primary key: returns one row.

### ✍️ The query

```sql
SELECT *
FROM CITY
WHERE ID = 1661;
```

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Select All](../select-all/README.md) · [🗄️ All SQL exercises](../../README.md) · [Japanese Cities' Attributes](../japanese-cities-attributes/README.md) ➡️
