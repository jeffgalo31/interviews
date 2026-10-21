<!-- study-layout -->
# Population Census

🟢 **Easy** · 📁 **Basic Join** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/asian-population/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Given the **CITY** and **COUNTRY** tables, query the sum of the populations of all cities where the *CONTINENT* is *'Asia'*.

**Note:** *CITY.CountryCode* and *COUNTRY.Code* are matching key columns.

## 📥 Input & output

### Input format

The **CITY** and **COUNTRY** tables are described as follows:

*CITY*

| Field | Type |
|---|---|
| ID | NUMBER |
| NAME | VARCHAR2(17) |
| COUNTRYCODE | VARCHAR2(3) |
| DISTRICT | VARCHAR2(20) |
| POPULATION | NUMBER |

*COUNTRY*

| Field | Type |
|---|---|
| CODE | VARCHAR2(3) |
| NAME | VARCHAR2(44) |
| CONTINENT | VARCHAR2(13) |
| REGION | VARCHAR2(25) |
| SURFACEAREA | NUMBER |
| INDEPYEAR | VARCHAR2(5) |
| POPULATION | NUMBER |
| LIFEEXPECTANCY | VARCHAR2(4) |
| GNP | NUMBER |
| GNPOLD | VARCHAR2(9) |
| LOCALNAME | VARCHAR2(44) |
| GOVERNMENTFORM | VARCHAR2(44) |
| HEADOFSTATE | VARCHAR2(32) |
| CAPITAL | VARCHAR2(4) |
| CODE2 | VARCHAR2(2) |

## 💡 Solution

> [!TIP]
> **Key idea:** `JOIN ... ON` attaches each city's country row, so we can filter on CONTINENT.

### ✍️ The query

```sql
SELECT SUM(CITY.POPULATION)
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Asia';
```

### 🔍 How it works

- Then `SUM` the city populations.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).

---

⬅️ [Weather Observation Station 20](../../aggregation/weather-observation-station-20/README.md) · [🗄️ All SQL exercises](../../README.md) · [African Cities](../african-cities/README.md) ➡️
