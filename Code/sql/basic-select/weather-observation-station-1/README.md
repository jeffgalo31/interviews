<!-- study-layout -->
# Weather Observation Station 1

🟢 **Easy** · 📁 **Basic Select** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/weather-observation-station-1/problem)

**On this page:** [📝 Problem](#-problem) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query a list of **CITY** and **STATE** from the **STATION** table.
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
> **Key idea:** List the two columns, separated by a comma.

### ✍️ The query

```sql
SELECT CITY, STATE
FROM STATION;
```

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Japanese Cities' Names](../japanese-cities-names/README.md) · [🗄️ All SQL exercises](../../README.md) · [Weather Observation Station 3](../weather-observation-station-3/README.md) ➡️
