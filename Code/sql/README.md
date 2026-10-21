# 🗄️ SQL Coding Practice

All **58** challenges from the [HackerRank SQL track](https://www.hackerrank.com/domains/sql), grouped by HackerRank section, with the same names and difficulty. Every problem is fully in text (tables instead of images), solved, explained and runnable.

| | Section | Challenges | 🟢 Easy | 🟡 Medium | 🔴 Hard |
|---|---|---|---|---|---|
| 1️⃣ | [Basic Select](#1-basic-select-20) | 20 | 20 | 0 | 0 |
| 2️⃣ | [Advanced Select](#2-advanced-select-5) | 5 | 1 | 4 | 0 |
| 3️⃣ | [Aggregation](#3-aggregation-17) | 17 | 14 | 3 | 0 |
| 4️⃣ | [Basic Join](#4-basic-join-8) | 8 | 3 | 5 | 0 |
| 5️⃣ | [Advanced Join](#5-advanced-join-5) | 5 | 0 | 3 | 2 |
| 6️⃣ | [Alternative Queries](#6-alternative-queries-3) | 3 | 2 | 1 | 0 |
| | **Total** | **58** | **40** | **16** | **2** |

## 📖 How to study one exercise

1. Read the problem in the exercise's `README.md` and try writing the query yourself.
2. Check the **🧪 Example** section: that's the data the query must handle.
3. Read **💡 Solution**: the key idea first, then the query and how it works.
4. Run `solution.sql` to see it on real data (it builds the sample tables first).
5. Submit `solution_hackerrank.sql` on HackerRank (choose **MySQL**) and mark it ✅ below.

## ▶️ Running

Open the `interviews` folder (or this `sql` folder) in VS Code, open a `solution.sql`, then **Terminal → Run Task → Run SQL file (SQLite)**. It runs on a fresh in-memory database every time.

From a terminal in this folder: `sqlite3 -header -column :memory: < basic-select/select-all/solution.sql`

## 🔀 SQLite vs MySQL

HackerRank uses MySQL; the local files use SQLite (built into macOS, nothing to install). Most SQL is identical; where it isn't, the exercise says so:

| MySQL (HackerRank) | SQLite (local) | Meaning |
|---|---|---|
| `CONCAT(a, b, c)` | `a \|\| b \|\| c` | join strings |
| `LEFT(s, 1)` | `SUBSTR(s, 1, 1)` | first character |
| `FLOOR(x)` / `CEIL(x)` | `CAST(x AS INTEGER)` (+1 if decimals for CEIL) | round down / up |
| `TRUNCATE(x, 4)` | `CAST(x * 10000 AS INTEGER) / 10000.0` | cut to 4 decimals |
| `DATEDIFF(a, b)` | `julianday(a) - julianday(b)` | days between dates |
| `REPEAT(s, n)` | `REPLACE(HEX(ZEROBLOB(n)), '00', s)` | repeat a string |

## 1️⃣ Basic Select (20)

| # | Challenge | Level | Runnable | HackerRank | Done |
|---|---|---|---|---|---|
| 1 | [Revising the Select Query I](basic-select/revising-the-select-query-i/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/revising-the-select-query-i/solution.sql) | [📋 copy](basic-select/revising-the-select-query-i/solution_hackerrank.sql) | ⬜ |
| 2 | [Revising the Select Query II](basic-select/revising-the-select-query-ii/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/revising-the-select-query-ii/solution.sql) | [📋 copy](basic-select/revising-the-select-query-ii/solution_hackerrank.sql) | ⬜ |
| 3 | [Select All](basic-select/select-all/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/select-all/solution.sql) | [📋 copy](basic-select/select-all/solution_hackerrank.sql) | ⬜ |
| 4 | [Select By ID](basic-select/select-by-id/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/select-by-id/solution.sql) | [📋 copy](basic-select/select-by-id/solution_hackerrank.sql) | ⬜ |
| 5 | [Japanese Cities' Attributes](basic-select/japanese-cities-attributes/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/japanese-cities-attributes/solution.sql) | [📋 copy](basic-select/japanese-cities-attributes/solution_hackerrank.sql) | ⬜ |
| 6 | [Japanese Cities' Names](basic-select/japanese-cities-names/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/japanese-cities-names/solution.sql) | [📋 copy](basic-select/japanese-cities-names/solution_hackerrank.sql) | ⬜ |
| 7 | [Weather Observation Station 1](basic-select/weather-observation-station-1/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-1/solution.sql) | [📋 copy](basic-select/weather-observation-station-1/solution_hackerrank.sql) | ⬜ |
| 8 | [Weather Observation Station 3](basic-select/weather-observation-station-3/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-3/solution.sql) | [📋 copy](basic-select/weather-observation-station-3/solution_hackerrank.sql) | ⬜ |
| 9 | [Weather Observation Station 4](basic-select/weather-observation-station-4/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-4/solution.sql) | [📋 copy](basic-select/weather-observation-station-4/solution_hackerrank.sql) | ⬜ |
| 10 | [Weather Observation Station 5](basic-select/weather-observation-station-5/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-5/solution.sql) | [📋 copy](basic-select/weather-observation-station-5/solution_hackerrank.sql) | ⬜ |
| 11 | [Weather Observation Station 6](basic-select/weather-observation-station-6/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-6/solution.sql) | [📋 copy](basic-select/weather-observation-station-6/solution_hackerrank.sql) | ⬜ |
| 12 | [Weather Observation Station 7](basic-select/weather-observation-station-7/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-7/solution.sql) | [📋 copy](basic-select/weather-observation-station-7/solution_hackerrank.sql) | ⬜ |
| 13 | [Weather Observation Station 8](basic-select/weather-observation-station-8/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-8/solution.sql) | [📋 copy](basic-select/weather-observation-station-8/solution_hackerrank.sql) | ⬜ |
| 14 | [Weather Observation Station 9](basic-select/weather-observation-station-9/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-9/solution.sql) | [📋 copy](basic-select/weather-observation-station-9/solution_hackerrank.sql) | ⬜ |
| 15 | [Weather Observation Station 10](basic-select/weather-observation-station-10/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-10/solution.sql) | [📋 copy](basic-select/weather-observation-station-10/solution_hackerrank.sql) | ⬜ |
| 16 | [Weather Observation Station 11](basic-select/weather-observation-station-11/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-11/solution.sql) | [📋 copy](basic-select/weather-observation-station-11/solution_hackerrank.sql) | ⬜ |
| 17 | [Weather Observation Station 12](basic-select/weather-observation-station-12/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/weather-observation-station-12/solution.sql) | [📋 copy](basic-select/weather-observation-station-12/solution_hackerrank.sql) | ⬜ |
| 18 | [Higher Than 75 Marks](basic-select/higher-than-75-marks/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/higher-than-75-marks/solution.sql) | [📋 copy](basic-select/higher-than-75-marks/solution_hackerrank.sql) | ⬜ |
| 19 | [Employee Names](basic-select/employee-names/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/employee-names/solution.sql) | [📋 copy](basic-select/employee-names/solution_hackerrank.sql) | ⬜ |
| 20 | [Employee Salaries](basic-select/employee-salaries/README.md) | 🟢 Easy | [▶️ solution.sql](basic-select/employee-salaries/solution.sql) | [📋 copy](basic-select/employee-salaries/solution_hackerrank.sql) | ⬜ |

## 2️⃣ Advanced Select (5)

| # | Challenge | Level | Runnable | HackerRank | Done |
|---|---|---|---|---|---|
| 1 | [Type of Triangle](advanced-select/type-of-triangle/README.md) | 🟢 Easy | [▶️ solution.sql](advanced-select/type-of-triangle/solution.sql) | [📋 copy](advanced-select/type-of-triangle/solution_hackerrank.sql) | ⬜ |
| 2 | [The PADS](advanced-select/the-pads/README.md) | 🟡 Medium | [▶️ solution.sql](advanced-select/the-pads/solution.sql) | [📋 copy](advanced-select/the-pads/solution_hackerrank.sql) | ⬜ |
| 3 | [Occupations](advanced-select/occupations/README.md) | 🟡 Medium | [▶️ solution.sql](advanced-select/occupations/solution.sql) | [📋 copy](advanced-select/occupations/solution_hackerrank.sql) | ⬜ |
| 4 | [Binary Tree Nodes](advanced-select/binary-tree-nodes/README.md) | 🟡 Medium | [▶️ solution.sql](advanced-select/binary-tree-nodes/solution.sql) | [📋 copy](advanced-select/binary-tree-nodes/solution_hackerrank.sql) | ⬜ |
| 5 | [New Companies](advanced-select/new-companies/README.md) | 🟡 Medium | [▶️ solution.sql](advanced-select/new-companies/solution.sql) | [📋 copy](advanced-select/new-companies/solution_hackerrank.sql) | ⬜ |

## 3️⃣ Aggregation (17)

| # | Challenge | Level | Runnable | HackerRank | Done |
|---|---|---|---|---|---|
| 1 | [Revising Aggregations - The Count Function](aggregation/revising-aggregations-the-count-function/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/revising-aggregations-the-count-function/solution.sql) | [📋 copy](aggregation/revising-aggregations-the-count-function/solution_hackerrank.sql) | ⬜ |
| 2 | [Revising Aggregations - The Sum Function](aggregation/revising-aggregations-the-sum-function/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/revising-aggregations-the-sum-function/solution.sql) | [📋 copy](aggregation/revising-aggregations-the-sum-function/solution_hackerrank.sql) | ⬜ |
| 3 | [Revising Aggregations - Averages](aggregation/revising-aggregations-averages/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/revising-aggregations-averages/solution.sql) | [📋 copy](aggregation/revising-aggregations-averages/solution_hackerrank.sql) | ⬜ |
| 4 | [Average Population](aggregation/average-population/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/average-population/solution.sql) | [📋 copy](aggregation/average-population/solution_hackerrank.sql) | ⬜ |
| 5 | [Japan Population](aggregation/japan-population/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/japan-population/solution.sql) | [📋 copy](aggregation/japan-population/solution_hackerrank.sql) | ⬜ |
| 6 | [Population Density Difference](aggregation/population-density-difference/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/population-density-difference/solution.sql) | [📋 copy](aggregation/population-density-difference/solution_hackerrank.sql) | ⬜ |
| 7 | [The Blunder](aggregation/the-blunder/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/the-blunder/solution.sql) | [📋 copy](aggregation/the-blunder/solution_hackerrank.sql) | ⬜ |
| 8 | [Top Earners](aggregation/top-earners/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/top-earners/solution.sql) | [📋 copy](aggregation/top-earners/solution_hackerrank.sql) | ⬜ |
| 9 | [Weather Observation Station 2](aggregation/weather-observation-station-2/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/weather-observation-station-2/solution.sql) | [📋 copy](aggregation/weather-observation-station-2/solution_hackerrank.sql) | ⬜ |
| 10 | [Weather Observation Station 13](aggregation/weather-observation-station-13/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/weather-observation-station-13/solution.sql) | [📋 copy](aggregation/weather-observation-station-13/solution_hackerrank.sql) | ⬜ |
| 11 | [Weather Observation Station 14](aggregation/weather-observation-station-14/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/weather-observation-station-14/solution.sql) | [📋 copy](aggregation/weather-observation-station-14/solution_hackerrank.sql) | ⬜ |
| 12 | [Weather Observation Station 15](aggregation/weather-observation-station-15/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/weather-observation-station-15/solution.sql) | [📋 copy](aggregation/weather-observation-station-15/solution_hackerrank.sql) | ⬜ |
| 13 | [Weather Observation Station 16](aggregation/weather-observation-station-16/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/weather-observation-station-16/solution.sql) | [📋 copy](aggregation/weather-observation-station-16/solution_hackerrank.sql) | ⬜ |
| 14 | [Weather Observation Station 17](aggregation/weather-observation-station-17/README.md) | 🟢 Easy | [▶️ solution.sql](aggregation/weather-observation-station-17/solution.sql) | [📋 copy](aggregation/weather-observation-station-17/solution_hackerrank.sql) | ⬜ |
| 15 | [Weather Observation Station 18](aggregation/weather-observation-station-18/README.md) | 🟡 Medium | [▶️ solution.sql](aggregation/weather-observation-station-18/solution.sql) | [📋 copy](aggregation/weather-observation-station-18/solution_hackerrank.sql) | ⬜ |
| 16 | [Weather Observation Station 19](aggregation/weather-observation-station-19/README.md) | 🟡 Medium | [▶️ solution.sql](aggregation/weather-observation-station-19/solution.sql) | [📋 copy](aggregation/weather-observation-station-19/solution_hackerrank.sql) | ⬜ |
| 17 | [Weather Observation Station 20](aggregation/weather-observation-station-20/README.md) | 🟡 Medium | [▶️ solution.sql](aggregation/weather-observation-station-20/solution.sql) | [📋 copy](aggregation/weather-observation-station-20/solution_hackerrank.sql) | ⬜ |

## 4️⃣ Basic Join (8)

| # | Challenge | Level | Runnable | HackerRank | Done |
|---|---|---|---|---|---|
| 1 | [Population Census ](basic-join/population-census/README.md) | 🟢 Easy | [▶️ solution.sql](basic-join/population-census/solution.sql) | [📋 copy](basic-join/population-census/solution_hackerrank.sql) | ⬜ |
| 2 | [African Cities](basic-join/african-cities/README.md) | 🟢 Easy | [▶️ solution.sql](basic-join/african-cities/solution.sql) | [📋 copy](basic-join/african-cities/solution_hackerrank.sql) | ⬜ |
| 3 | [Average Population of Each Continent](basic-join/average-population-of-each-continent/README.md) | 🟢 Easy | [▶️ solution.sql](basic-join/average-population-of-each-continent/solution.sql) | [📋 copy](basic-join/average-population-of-each-continent/solution_hackerrank.sql) | ⬜ |
| 4 | [The Report](basic-join/the-report/README.md) | 🟡 Medium | [▶️ solution.sql](basic-join/the-report/solution.sql) | [📋 copy](basic-join/the-report/solution_hackerrank.sql) | ⬜ |
| 5 | [Top Competitors](basic-join/top-competitors/README.md) | 🟡 Medium | [▶️ solution.sql](basic-join/top-competitors/solution.sql) | [📋 copy](basic-join/top-competitors/solution_hackerrank.sql) | ⬜ |
| 6 | [Ollivander's Inventory](basic-join/ollivanders-inventory/README.md) | 🟡 Medium | [▶️ solution.sql](basic-join/ollivanders-inventory/solution.sql) | [📋 copy](basic-join/ollivanders-inventory/solution_hackerrank.sql) | ⬜ |
| 7 | [Challenges](basic-join/challenges/README.md) | 🟡 Medium | [▶️ solution.sql](basic-join/challenges/solution.sql) | [📋 copy](basic-join/challenges/solution_hackerrank.sql) | ⬜ |
| 8 | [Contest Leaderboard](basic-join/contest-leaderboard/README.md) | 🟡 Medium | [▶️ solution.sql](basic-join/contest-leaderboard/solution.sql) | [📋 copy](basic-join/contest-leaderboard/solution_hackerrank.sql) | ⬜ |

## 5️⃣ Advanced Join (5)

| # | Challenge | Level | Runnable | HackerRank | Done |
|---|---|---|---|---|---|
| 1 | [SQL Project Planning](advanced-join/sql-project-planning/README.md) | 🟡 Medium | [▶️ solution.sql](advanced-join/sql-project-planning/solution.sql) | [📋 copy](advanced-join/sql-project-planning/solution_hackerrank.sql) | ⬜ |
| 2 | [Placements](advanced-join/placements/README.md) | 🟡 Medium | [▶️ solution.sql](advanced-join/placements/solution.sql) | [📋 copy](advanced-join/placements/solution_hackerrank.sql) | ⬜ |
| 3 | [Symmetric Pairs](advanced-join/symmetric-pairs/README.md) | 🟡 Medium | [▶️ solution.sql](advanced-join/symmetric-pairs/solution.sql) | [📋 copy](advanced-join/symmetric-pairs/solution_hackerrank.sql) | ⬜ |
| 4 | [Interviews](advanced-join/interviews/README.md) | 🔴 Hard | [▶️ solution.sql](advanced-join/interviews/solution.sql) | [📋 copy](advanced-join/interviews/solution_hackerrank.sql) | ⬜ |
| 5 | [15 Days of Learning SQL](advanced-join/15-days-of-learning-sql/README.md) | 🔴 Hard | [▶️ solution.sql](advanced-join/15-days-of-learning-sql/solution.sql) | [📋 copy](advanced-join/15-days-of-learning-sql/solution_hackerrank.sql) | ⬜ |

## 6️⃣ Alternative Queries (3)

| # | Challenge | Level | Runnable | HackerRank | Done |
|---|---|---|---|---|---|
| 1 | [Draw The Triangle 1](alternative-queries/draw-the-triangle-1/README.md) | 🟢 Easy | [▶️ solution.sql](alternative-queries/draw-the-triangle-1/solution.sql) | [📋 copy](alternative-queries/draw-the-triangle-1/solution_hackerrank.sql) | ⬜ |
| 2 | [Draw The Triangle 2](alternative-queries/draw-the-triangle-2/README.md) | 🟢 Easy | [▶️ solution.sql](alternative-queries/draw-the-triangle-2/solution.sql) | [📋 copy](alternative-queries/draw-the-triangle-2/solution_hackerrank.sql) | ⬜ |
| 3 | [Print Prime Numbers](alternative-queries/print-prime-numbers/README.md) | 🟡 Medium | [▶️ solution.sql](alternative-queries/print-prime-numbers/solution.sql) | [📋 copy](alternative-queries/print-prime-numbers/solution_hackerrank.sql) | ⬜ |

> [!TIP]
> Change ⬜ to ✅ in the **Done** column as you finish each challenge.

---

🛠️ How this was built (and how to do the same for another tech): [HACKERRANK-IMPORT.md](../HACKERRANK-IMPORT.md) · generator: [_tools/gen.py](_tools/gen.py)

**Back to:** [All Topics](../../Overview/All-Topics.md) · [Practices](../../Overview/Practices.md) · [☕ Java exercises](../java/README.md)
