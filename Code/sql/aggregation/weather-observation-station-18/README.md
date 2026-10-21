<!-- study-layout -->
# Weather Observation Station 18

🟡 **Medium** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/weather-observation-station-18/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Consider $P_1(a, b)$ and $P_2(c, d)$ to be two points on a *2D* plane.

- $a$ happens to equal the minimum value in *Northern Latitude* (*LAT\_N* in **STATION**).
- $b$ happens to equal the minimum value in *Western Longitude* (*LONG\_W* in **STATION**).
- $c$ happens to equal the maximum value in *Northern Latitude* (*LAT\_N* in **STATION**).
- $d$ happens to equal the maximum value in *Western Longitude* (*LONG\_W* in **STATION**).

Query the [Manhattan Distance](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html)  between points $P_1$ and $P_2$ and round it to a scale of $4$ decimal places.

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
> **Key idea:** Manhattan distance = |a − c| + |b − d|.

### ✍️ The query

```sql
SELECT ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)), 4)
FROM STATION;
```

### 🔍 How it works

- a, c are MIN/MAX of LAT_N; b, d are MIN/MAX of LONG_W.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Weather Observation Station 17](../weather-observation-station-17/README.md) · [🗄️ All SQL exercises](../../README.md) · [Weather Observation Station 19](../weather-observation-station-19/README.md) ➡️
