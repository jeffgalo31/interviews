<!-- study-layout -->
# Weather Observation Station 2

🟢 **Easy** · 📁 **Aggregation** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/weather-observation-station-2/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query the following two values from the **STATION** table:

1. The sum of all values in *LAT\_N* rounded to a scale of $2$ decimal places.
2. The sum of all values in *LONG\_W* rounded to a scale of $2$ decimal places.

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

### Output format

Your results must be in the form:

	lat lon

where $lat$ is the sum of all values in *LAT\_N* and $lon$ is the sum of all values in *LONG\_W*. Both results must be rounded to a scale of $2$ decimal places.

## 💡 Solution

> [!TIP]
> **Key idea:** `ROUND(x, 2)` keeps 2 decimal places.

### ✍️ The query

```sql
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2)
FROM STATION;
```

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Top Earners](../top-earners/README.md) · [🗄️ All SQL exercises](../../README.md) · [Weather Observation Station 13](../weather-observation-station-13/README.md) ➡️
