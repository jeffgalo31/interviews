<!-- study-layout -->
# Weather Observation Station 20

🟡 **Medium** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/weather-observation-station-20/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

A *[median](https://en.wikipedia.org/wiki/Median)* is defined as a number separating the higher half of a data set from the lower half. Query the *median* of the *Northern Latitudes* (*LAT\_N*) from **STATION** and round your answer to $4$ decimal places.

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
> **Key idea:** The median is the value with as many values below it as above it.

### ✍️ The query

```sql
SELECT ROUND(s.LAT_N, 4)
FROM STATION s
WHERE (SELECT COUNT(*) FROM STATION WHERE LAT_N < s.LAT_N)
    = (SELECT COUNT(*) FROM STATION WHERE LAT_N > s.LAT_N);
```

### 🔍 How it works

- For each row, count the smaller and the larger LAT_N values; keep the row where both counts are equal.
- Works when the row count is odd (HackerRank's STATION has 499 rows).

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Weather Observation Station 19](../weather-observation-station-19/README.md) · [🗄️ All SQL exercises](../../README.md) · [Population Census ](../../basic-join/population-census/README.md) ➡️
