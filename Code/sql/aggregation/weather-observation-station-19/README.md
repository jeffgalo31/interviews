<!-- study-layout -->
# Weather Observation Station 19

🟡 **Medium** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/weather-observation-station-19/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Consider $P_1(a, c)$ and $P_2(b, d)$ to be two points on a 2D plane where $(a, b)$ are the respective minimum and maximum values of *Northern Latitude* (*LAT\_N*) and $(c, d)$ are the respective minimum and maximum values of *Western Longitude* (*LONG\_W*) in **STATION**.

Query the [Euclidean Distance](https://en.wikipedia.org/wiki/Euclidean_distance) between points $P_1$ and $P_2$ and *format your answer* to display $4$ decimal digits.

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
> **Key idea:** Euclidean distance = √((b − a)² + (d − c)²) with a, b = min/max LAT_N and c, d = min/max LONG_W.

### ✍️ The query

```sql
SELECT ROUND(SQRT(POWER(MAX(LAT_N) - MIN(LAT_N), 2) + POWER(MAX(LONG_W) - MIN(LONG_W), 2)), 4)
FROM STATION;
```

### 🔍 How it works

- Local SQLite needs `SQRT` (built in on most current builds); if yours says "no such function", the HackerRank version still works.

> [!NOTE]
> **Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: `POWER(x, 2)` → `x * x`.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Weather Observation Station 18](../weather-observation-station-18/README.md) · [🗄️ All SQL exercises](../../README.md) · [Weather Observation Station 20](../weather-observation-station-20/README.md) ➡️
