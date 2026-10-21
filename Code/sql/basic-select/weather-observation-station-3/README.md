<!-- study-layout -->
# Weather Observation Station 3

🟢 **Easy** · 📁 **Basic Select** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/weather-observation-station-3/problem)

**On this page:** [📝 Problem](#-problem) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query a list of **CITY** names from **STATION** for cities that have an even **ID** number. Print the results in any order, but exclude duplicates from the answer.
The **STATION** table is described as follows:

*STATION*

| Field | Type |
|---|---|
| ID | NUMBER |
| CITY | VARCHAR2(21) |
| STATE | VARCHAR2(2) |
| LAT_N | NUMBER |
| LONG_W | NUMBER |

where **LAT\_N** is the northern latitude and **LONG\_W** is the western longitude.

## 💡 Solution

> [!TIP]
> **Key idea:** `ID % 2 = 0`: the remainder of dividing by 2 is 0, so the ID is even (`MOD(ID, 2) = 0` also works in MySQL).

### ✍️ The query

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE ID % 2 = 0;
```

### 🔍 How it works

- `DISTINCT` removes duplicate city names.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Weather Observation Station 1](../weather-observation-station-1/README.md) · [🗄️ All SQL exercises](../../README.md) · [Weather Observation Station 4](../weather-observation-station-4/README.md) ➡️
