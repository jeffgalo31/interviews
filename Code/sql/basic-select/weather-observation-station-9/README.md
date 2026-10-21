<!-- study-layout -->
# Weather Observation Station 9

🟢 **Easy** · 📁 **Basic Select** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/weather-observation-station-9/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query the list of *CITY* names from **STATION** that *do not start* with vowels. Your result cannot contain duplicates.

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
> **Key idea:** `SUBSTR(CITY, 1, 1)` is the first character, `SUBSTR(CITY, -1, 1)` the last (negative = count from the end).

### ✍️ The query

```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTR(CITY, 1, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');
```

### 🔍 How it works

- `LOWER(...)` so `A` and `a` both match the vowel list.
- `DISTINCT` because the result cannot contain duplicates.
- `NOT IN` flips the test: first letter is **not** a vowel.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Weather Observation Station 8](../weather-observation-station-8/README.md) · [🗄️ All SQL exercises](../../README.md) · [Weather Observation Station 10](../weather-observation-station-10/README.md) ➡️
