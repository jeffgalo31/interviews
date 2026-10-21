<!-- study-layout -->
# Revising the Select Query II

🟢 **Easy** · 📁 **Basic Select** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/revising-the-select-query-2/problem)

**On this page:** [📝 Problem](#-problem) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query the **NAME** field for all American cities in the **CITY** table with populations larger than `120000`. The *CountryCode* for America is `USA`.

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
> **Key idea:** Same filter idea as part I, but only the `NAME` column is selected.

### ✍️ The query

```sql
SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'USA'
  AND POPULATION > 120000;
```

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Revising the Select Query I](../revising-the-select-query-i/README.md) · [🗄️ All SQL exercises](../../README.md) · [Select All](../select-all/README.md) ➡️
