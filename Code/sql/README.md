# SQL Coding Practice

All 58 challenges of the [HackerRank SQL track](https://www.hackerrank.com/domains/sql), grouped by HackerRank section,
with the same name and difficulty as on HackerRank.

Each exercise folder has:

- `README.md`: the problem (from HackerRank) and how the solution works.
- `solution.sql`: the runnable, commented version. It creates sample tables first, then runs the query.
  Written for **SQLite** (built into macOS), so there's nothing to install.
- `solution_hackerrank.sql`: the copy to paste into HackerRank (**MySQL**; pick MySQL in the language menu, it opens on DB2).

## Running

Open the `interviews` folder (or this `sql` folder) in VS Code, open a `solution.sql`, then
**Terminal → Run Task → Run SQL file (SQLite)**. It runs on a fresh in-memory database every time.

From the terminal: `sqlite3 -header -column :memory: < basic-select/select-all/solution.sql`

## SQLite vs MySQL

HackerRank uses MySQL; the local files use SQLite. Most SQL is identical. Where it isn't, the README of that exercise says so:

| MySQL (HackerRank) | SQLite (local) | Meaning |
|---|---|---|
| `CONCAT(a, b, c)` | `a \|\| b \|\| c` | join strings |
| `LEFT(s, 1)` | `SUBSTR(s, 1, 1)` | first character |
| `FLOOR(x)` / `CEIL(x)` | `CAST(x AS INTEGER)` (+1 if decimals for CEIL) | round down / up |
| `TRUNCATE(x, 4)` | `CAST(x * 10000 AS INTEGER) / 10000.0` | cut to 4 decimals |
| `DATEDIFF(a, b)` | `julianday(a) - julianday(b)` | days between dates |
| `REPEAT(s, n)` | `REPLACE(HEX(ZEROBLOB(n)), '00', s)` | repeat a string |

## Basic Select (20)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Revising the Select Query I](basic-select/revising-the-select-query-i/) | Easy | [README](basic-select/revising-the-select-query-i/README.md) · [solution.sql](basic-select/revising-the-select-query-i/solution.sql) · [HackerRank copy](basic-select/revising-the-select-query-i/solution_hackerrank.sql) |
| 2 | [Revising the Select Query II](basic-select/revising-the-select-query-ii/) | Easy | [README](basic-select/revising-the-select-query-ii/README.md) · [solution.sql](basic-select/revising-the-select-query-ii/solution.sql) · [HackerRank copy](basic-select/revising-the-select-query-ii/solution_hackerrank.sql) |
| 3 | [Select All](basic-select/select-all/) | Easy | [README](basic-select/select-all/README.md) · [solution.sql](basic-select/select-all/solution.sql) · [HackerRank copy](basic-select/select-all/solution_hackerrank.sql) |
| 4 | [Select By ID](basic-select/select-by-id/) | Easy | [README](basic-select/select-by-id/README.md) · [solution.sql](basic-select/select-by-id/solution.sql) · [HackerRank copy](basic-select/select-by-id/solution_hackerrank.sql) |
| 5 | [Japanese Cities' Attributes](basic-select/japanese-cities-attributes/) | Easy | [README](basic-select/japanese-cities-attributes/README.md) · [solution.sql](basic-select/japanese-cities-attributes/solution.sql) · [HackerRank copy](basic-select/japanese-cities-attributes/solution_hackerrank.sql) |
| 6 | [Japanese Cities' Names](basic-select/japanese-cities-names/) | Easy | [README](basic-select/japanese-cities-names/README.md) · [solution.sql](basic-select/japanese-cities-names/solution.sql) · [HackerRank copy](basic-select/japanese-cities-names/solution_hackerrank.sql) |
| 7 | [Weather Observation Station 1](basic-select/weather-observation-station-1/) | Easy | [README](basic-select/weather-observation-station-1/README.md) · [solution.sql](basic-select/weather-observation-station-1/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-1/solution_hackerrank.sql) |
| 8 | [Weather Observation Station 3](basic-select/weather-observation-station-3/) | Easy | [README](basic-select/weather-observation-station-3/README.md) · [solution.sql](basic-select/weather-observation-station-3/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-3/solution_hackerrank.sql) |
| 9 | [Weather Observation Station 4](basic-select/weather-observation-station-4/) | Easy | [README](basic-select/weather-observation-station-4/README.md) · [solution.sql](basic-select/weather-observation-station-4/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-4/solution_hackerrank.sql) |
| 10 | [Weather Observation Station 5](basic-select/weather-observation-station-5/) | Easy | [README](basic-select/weather-observation-station-5/README.md) · [solution.sql](basic-select/weather-observation-station-5/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-5/solution_hackerrank.sql) |
| 11 | [Weather Observation Station 6](basic-select/weather-observation-station-6/) | Easy | [README](basic-select/weather-observation-station-6/README.md) · [solution.sql](basic-select/weather-observation-station-6/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-6/solution_hackerrank.sql) |
| 12 | [Weather Observation Station 7](basic-select/weather-observation-station-7/) | Easy | [README](basic-select/weather-observation-station-7/README.md) · [solution.sql](basic-select/weather-observation-station-7/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-7/solution_hackerrank.sql) |
| 13 | [Weather Observation Station 8](basic-select/weather-observation-station-8/) | Easy | [README](basic-select/weather-observation-station-8/README.md) · [solution.sql](basic-select/weather-observation-station-8/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-8/solution_hackerrank.sql) |
| 14 | [Weather Observation Station 9](basic-select/weather-observation-station-9/) | Easy | [README](basic-select/weather-observation-station-9/README.md) · [solution.sql](basic-select/weather-observation-station-9/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-9/solution_hackerrank.sql) |
| 15 | [Weather Observation Station 10](basic-select/weather-observation-station-10/) | Easy | [README](basic-select/weather-observation-station-10/README.md) · [solution.sql](basic-select/weather-observation-station-10/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-10/solution_hackerrank.sql) |
| 16 | [Weather Observation Station 11](basic-select/weather-observation-station-11/) | Easy | [README](basic-select/weather-observation-station-11/README.md) · [solution.sql](basic-select/weather-observation-station-11/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-11/solution_hackerrank.sql) |
| 17 | [Weather Observation Station 12](basic-select/weather-observation-station-12/) | Easy | [README](basic-select/weather-observation-station-12/README.md) · [solution.sql](basic-select/weather-observation-station-12/solution.sql) · [HackerRank copy](basic-select/weather-observation-station-12/solution_hackerrank.sql) |
| 18 | [Higher Than 75 Marks](basic-select/higher-than-75-marks/) | Easy | [README](basic-select/higher-than-75-marks/README.md) · [solution.sql](basic-select/higher-than-75-marks/solution.sql) · [HackerRank copy](basic-select/higher-than-75-marks/solution_hackerrank.sql) |
| 19 | [Employee Names](basic-select/employee-names/) | Easy | [README](basic-select/employee-names/README.md) · [solution.sql](basic-select/employee-names/solution.sql) · [HackerRank copy](basic-select/employee-names/solution_hackerrank.sql) |
| 20 | [Employee Salaries](basic-select/employee-salaries/) | Easy | [README](basic-select/employee-salaries/README.md) · [solution.sql](basic-select/employee-salaries/solution.sql) · [HackerRank copy](basic-select/employee-salaries/solution_hackerrank.sql) |

## Advanced Select (5)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Type of Triangle](advanced-select/type-of-triangle/) | Easy | [README](advanced-select/type-of-triangle/README.md) · [solution.sql](advanced-select/type-of-triangle/solution.sql) · [HackerRank copy](advanced-select/type-of-triangle/solution_hackerrank.sql) |
| 2 | [The PADS](advanced-select/the-pads/) | Medium | [README](advanced-select/the-pads/README.md) · [solution.sql](advanced-select/the-pads/solution.sql) · [HackerRank copy](advanced-select/the-pads/solution_hackerrank.sql) |
| 3 | [Occupations](advanced-select/occupations/) | Medium | [README](advanced-select/occupations/README.md) · [solution.sql](advanced-select/occupations/solution.sql) · [HackerRank copy](advanced-select/occupations/solution_hackerrank.sql) |
| 4 | [Binary Tree Nodes](advanced-select/binary-tree-nodes/) | Medium | [README](advanced-select/binary-tree-nodes/README.md) · [solution.sql](advanced-select/binary-tree-nodes/solution.sql) · [HackerRank copy](advanced-select/binary-tree-nodes/solution_hackerrank.sql) |
| 5 | [New Companies](advanced-select/new-companies/) | Medium | [README](advanced-select/new-companies/README.md) · [solution.sql](advanced-select/new-companies/solution.sql) · [HackerRank copy](advanced-select/new-companies/solution_hackerrank.sql) |

## Aggregation (17)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Revising Aggregations - The Count Function](aggregation/revising-aggregations-the-count-function/) | Easy | [README](aggregation/revising-aggregations-the-count-function/README.md) · [solution.sql](aggregation/revising-aggregations-the-count-function/solution.sql) · [HackerRank copy](aggregation/revising-aggregations-the-count-function/solution_hackerrank.sql) |
| 2 | [Revising Aggregations - The Sum Function](aggregation/revising-aggregations-the-sum-function/) | Easy | [README](aggregation/revising-aggregations-the-sum-function/README.md) · [solution.sql](aggregation/revising-aggregations-the-sum-function/solution.sql) · [HackerRank copy](aggregation/revising-aggregations-the-sum-function/solution_hackerrank.sql) |
| 3 | [Revising Aggregations - Averages](aggregation/revising-aggregations-averages/) | Easy | [README](aggregation/revising-aggregations-averages/README.md) · [solution.sql](aggregation/revising-aggregations-averages/solution.sql) · [HackerRank copy](aggregation/revising-aggregations-averages/solution_hackerrank.sql) |
| 4 | [Average Population](aggregation/average-population/) | Easy | [README](aggregation/average-population/README.md) · [solution.sql](aggregation/average-population/solution.sql) · [HackerRank copy](aggregation/average-population/solution_hackerrank.sql) |
| 5 | [Japan Population](aggregation/japan-population/) | Easy | [README](aggregation/japan-population/README.md) · [solution.sql](aggregation/japan-population/solution.sql) · [HackerRank copy](aggregation/japan-population/solution_hackerrank.sql) |
| 6 | [Population Density Difference](aggregation/population-density-difference/) | Easy | [README](aggregation/population-density-difference/README.md) · [solution.sql](aggregation/population-density-difference/solution.sql) · [HackerRank copy](aggregation/population-density-difference/solution_hackerrank.sql) |
| 7 | [The Blunder](aggregation/the-blunder/) | Easy | [README](aggregation/the-blunder/README.md) · [solution.sql](aggregation/the-blunder/solution.sql) · [HackerRank copy](aggregation/the-blunder/solution_hackerrank.sql) |
| 8 | [Top Earners](aggregation/top-earners/) | Easy | [README](aggregation/top-earners/README.md) · [solution.sql](aggregation/top-earners/solution.sql) · [HackerRank copy](aggregation/top-earners/solution_hackerrank.sql) |
| 9 | [Weather Observation Station 2](aggregation/weather-observation-station-2/) | Easy | [README](aggregation/weather-observation-station-2/README.md) · [solution.sql](aggregation/weather-observation-station-2/solution.sql) · [HackerRank copy](aggregation/weather-observation-station-2/solution_hackerrank.sql) |
| 10 | [Weather Observation Station 13](aggregation/weather-observation-station-13/) | Easy | [README](aggregation/weather-observation-station-13/README.md) · [solution.sql](aggregation/weather-observation-station-13/solution.sql) · [HackerRank copy](aggregation/weather-observation-station-13/solution_hackerrank.sql) |
| 11 | [Weather Observation Station 14](aggregation/weather-observation-station-14/) | Easy | [README](aggregation/weather-observation-station-14/README.md) · [solution.sql](aggregation/weather-observation-station-14/solution.sql) · [HackerRank copy](aggregation/weather-observation-station-14/solution_hackerrank.sql) |
| 12 | [Weather Observation Station 15](aggregation/weather-observation-station-15/) | Easy | [README](aggregation/weather-observation-station-15/README.md) · [solution.sql](aggregation/weather-observation-station-15/solution.sql) · [HackerRank copy](aggregation/weather-observation-station-15/solution_hackerrank.sql) |
| 13 | [Weather Observation Station 16](aggregation/weather-observation-station-16/) | Easy | [README](aggregation/weather-observation-station-16/README.md) · [solution.sql](aggregation/weather-observation-station-16/solution.sql) · [HackerRank copy](aggregation/weather-observation-station-16/solution_hackerrank.sql) |
| 14 | [Weather Observation Station 17](aggregation/weather-observation-station-17/) | Easy | [README](aggregation/weather-observation-station-17/README.md) · [solution.sql](aggregation/weather-observation-station-17/solution.sql) · [HackerRank copy](aggregation/weather-observation-station-17/solution_hackerrank.sql) |
| 15 | [Weather Observation Station 18](aggregation/weather-observation-station-18/) | Medium | [README](aggregation/weather-observation-station-18/README.md) · [solution.sql](aggregation/weather-observation-station-18/solution.sql) · [HackerRank copy](aggregation/weather-observation-station-18/solution_hackerrank.sql) |
| 16 | [Weather Observation Station 19](aggregation/weather-observation-station-19/) | Medium | [README](aggregation/weather-observation-station-19/README.md) · [solution.sql](aggregation/weather-observation-station-19/solution.sql) · [HackerRank copy](aggregation/weather-observation-station-19/solution_hackerrank.sql) |
| 17 | [Weather Observation Station 20](aggregation/weather-observation-station-20/) | Medium | [README](aggregation/weather-observation-station-20/README.md) · [solution.sql](aggregation/weather-observation-station-20/solution.sql) · [HackerRank copy](aggregation/weather-observation-station-20/solution_hackerrank.sql) |

## Basic Join (8)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Population Census ](basic-join/population-census/) | Easy | [README](basic-join/population-census/README.md) · [solution.sql](basic-join/population-census/solution.sql) · [HackerRank copy](basic-join/population-census/solution_hackerrank.sql) |
| 2 | [African Cities](basic-join/african-cities/) | Easy | [README](basic-join/african-cities/README.md) · [solution.sql](basic-join/african-cities/solution.sql) · [HackerRank copy](basic-join/african-cities/solution_hackerrank.sql) |
| 3 | [Average Population of Each Continent](basic-join/average-population-of-each-continent/) | Easy | [README](basic-join/average-population-of-each-continent/README.md) · [solution.sql](basic-join/average-population-of-each-continent/solution.sql) · [HackerRank copy](basic-join/average-population-of-each-continent/solution_hackerrank.sql) |
| 4 | [The Report](basic-join/the-report/) | Medium | [README](basic-join/the-report/README.md) · [solution.sql](basic-join/the-report/solution.sql) · [HackerRank copy](basic-join/the-report/solution_hackerrank.sql) |
| 5 | [Top Competitors](basic-join/top-competitors/) | Medium | [README](basic-join/top-competitors/README.md) · [solution.sql](basic-join/top-competitors/solution.sql) · [HackerRank copy](basic-join/top-competitors/solution_hackerrank.sql) |
| 6 | [Ollivander's Inventory](basic-join/ollivanders-inventory/) | Medium | [README](basic-join/ollivanders-inventory/README.md) · [solution.sql](basic-join/ollivanders-inventory/solution.sql) · [HackerRank copy](basic-join/ollivanders-inventory/solution_hackerrank.sql) |
| 7 | [Challenges](basic-join/challenges/) | Medium | [README](basic-join/challenges/README.md) · [solution.sql](basic-join/challenges/solution.sql) · [HackerRank copy](basic-join/challenges/solution_hackerrank.sql) |
| 8 | [Contest Leaderboard](basic-join/contest-leaderboard/) | Medium | [README](basic-join/contest-leaderboard/README.md) · [solution.sql](basic-join/contest-leaderboard/solution.sql) · [HackerRank copy](basic-join/contest-leaderboard/solution_hackerrank.sql) |

## Advanced Join (5)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [SQL Project Planning](advanced-join/sql-project-planning/) | Medium | [README](advanced-join/sql-project-planning/README.md) · [solution.sql](advanced-join/sql-project-planning/solution.sql) · [HackerRank copy](advanced-join/sql-project-planning/solution_hackerrank.sql) |
| 2 | [Placements](advanced-join/placements/) | Medium | [README](advanced-join/placements/README.md) · [solution.sql](advanced-join/placements/solution.sql) · [HackerRank copy](advanced-join/placements/solution_hackerrank.sql) |
| 3 | [Symmetric Pairs](advanced-join/symmetric-pairs/) | Medium | [README](advanced-join/symmetric-pairs/README.md) · [solution.sql](advanced-join/symmetric-pairs/solution.sql) · [HackerRank copy](advanced-join/symmetric-pairs/solution_hackerrank.sql) |
| 4 | [Interviews](advanced-join/interviews/) | Hard | [README](advanced-join/interviews/README.md) · [solution.sql](advanced-join/interviews/solution.sql) · [HackerRank copy](advanced-join/interviews/solution_hackerrank.sql) |
| 5 | [15 Days of Learning SQL](advanced-join/15-days-of-learning-sql/) | Hard | [README](advanced-join/15-days-of-learning-sql/README.md) · [solution.sql](advanced-join/15-days-of-learning-sql/solution.sql) · [HackerRank copy](advanced-join/15-days-of-learning-sql/solution_hackerrank.sql) |

## Alternative Queries (3)

| # | Challenge | Difficulty | Files |
|---|---|---|---|
| 1 | [Draw The Triangle 1](alternative-queries/draw-the-triangle-1/) | Easy | [README](alternative-queries/draw-the-triangle-1/README.md) · [solution.sql](alternative-queries/draw-the-triangle-1/solution.sql) · [HackerRank copy](alternative-queries/draw-the-triangle-1/solution_hackerrank.sql) |
| 2 | [Draw The Triangle 2](alternative-queries/draw-the-triangle-2/) | Easy | [README](alternative-queries/draw-the-triangle-2/README.md) · [solution.sql](alternative-queries/draw-the-triangle-2/solution.sql) · [HackerRank copy](alternative-queries/draw-the-triangle-2/solution_hackerrank.sql) |
| 3 | [Print Prime Numbers](alternative-queries/print-prime-numbers/) | Medium | [README](alternative-queries/print-prime-numbers/README.md) · [solution.sql](alternative-queries/print-prime-numbers/solution.sql) · [HackerRank copy](alternative-queries/print-prime-numbers/solution_hackerrank.sql) |

---

**Back to:** [All Topics](../../Overview/All-Topics.md) · [Java exercises](../java/)
