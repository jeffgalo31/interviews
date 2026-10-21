<!-- study-layout -->
# Weather Observation Station 17

🟢 **Easy** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/weather-observation-station-17/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query the *Western Longitude* (*LONG\_W*)where the smallest *Northern Latitude* (*LAT\_N*) in **STATION** is greater than $38.7780$. Round your answer to $4$ decimal places.

## 📥 Input & output

### Input format

The **STATION** table is described as follows:

*STATION*

| Field | Type |
|---|---|
| ID | NUMBER |
| CITY | VARCHAR2(21) |
| STATE | VARCHAR2(2) |
| LAT_N | NUMBER |
| LONG_W | NUMBER |

where *LAT\_N* is the northern latitude and *LONG\_W* is the western longitude.

## 💡 Solution

> [!TIP]
> **Key idea:** Value from the row with the smallest LAT_N above the limit: sort ascending, keep 1 row.

### ✍️ The query

```sql
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N
LIMIT 1;
```

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Weather Observation Station 16](../weather-observation-station-16/README.md) · [🗄️ All SQL exercises](../../README.md) · [Weather Observation Station 18](../weather-observation-station-18/README.md) ➡️
