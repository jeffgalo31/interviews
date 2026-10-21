<!-- study-layout -->
# Weather Observation Station 5

🟢 **Easy** · 📁 **Basic Select** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/weather-observation-station-5/problem)

**On this page:** [📝 Problem](#-problem) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Query the two cities in **STATION** with the shortest and longest *CITY* names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
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

## 🧪 Example

**Input**

For example, **CITY**  has four entries: **DEF, ABC, PQRS**  and **WXY** .

**Output**

```
ABC 3
PQRS 4
```

**Why**

When ordered alphabetically, the **CITY** names are listed as **ABC, DEF, PQRS,** and **WXY**, with lengths 3, 3, 4, and 3. The longest name is **PQRS**, but there are 3 options for shortest named city. Choose **ABC**, because it comes first alphabetically.

### Note

You can write two separate queries to get the desired output. It need not be a single query.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** Two separate queries (allowed by the note).

### ✍️ The query

```sql
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY), CITY
LIMIT 1;

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY
LIMIT 1;
```

### 🔍 How it works

- Shortest: sort by length ascending, ties alphabetically, keep the first row (`LIMIT 1`).
- Longest: sort by length **descending**, ties still alphabetically, keep the first row.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [Weather Observation Station 4](../weather-observation-station-4/README.md) · [🗄️ All SQL exercises](../../README.md) · [Weather Observation Station 6](../weather-observation-station-6/README.md) ➡️
