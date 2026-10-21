<!-- study-layout -->
# Weather Observation Station 13

🟢 **Easy** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/weather-observation-station-13/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query the sum of *Northern Latitudes* (*LAT\_N*) from **STATION** having values greater than $38.7880$ and less than $137.2345$. Truncate your answer to $4$ decimal places.

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
> **Key idea:** **Truncate** (cut off) to 4 decimals, not round: `TRUNCATE(x, 4)` in MySQL.

### ✍️ The query

```sql
SELECT TRUNCATE(SUM(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7880
  AND LAT_N < 137.2345;
```

### 🔍 How it works

- Local SQLite: multiply by 10000, drop the decimals, divide back.

> [!NOTE]
> **Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `TRUNCATE(x, 4)` → `CAST(x * 10000 AS INTEGER) / 10000.0`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Weather Observation Station 2](../weather-observation-station-2/README.md) · [🗄️ All SQL exercises](../../README.md) · [Weather Observation Station 14](../weather-observation-station-14/README.md) ➡️
