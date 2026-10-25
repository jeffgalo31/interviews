# 🗄️ SQL Refresher

Code: [refresher.sql](refresher.sql) · Run: **Terminal → Run Task → Run SQL file (SQLite)**. HackerRank uses MySQL; differences are noted below.

## Ranking: ROW_NUMBER vs RANK vs DENSE_RANK

All three number rows in order. They only differ when values **tie**.

| dealer | amount | ROW_NUMBER | RANK | DENSE_RANK |
|---|---|---|---|---|
| D1 | 500 | 1 | 1 | 1 |
| D2 | 500 | 2 | 1 | 1 |
| D3 | 400 | 3 | **3** (skips 2) | **2** (no gap) |
| D4 | 300 | 4 | 4 | 3 |

| Function | Ties | Use it for |
|---|---|---|
| `ROW_NUMBER()` | Never: always 1, 2, 3… | "Latest / first row per X", removing duplicates (`WHERE rn = 1`) |
| `DENSE_RANK()` | Same number, no gap | "Top N", "2nd highest" (`WHERE rnk <= N`) |
| `RANK()` | Same number, then skips | Only when asked for "competition ranking" |

- `PARTITION BY x` restarts the numbering for each `x` (per machine, per region). `ORDER BY` decides who is first.
- A window function can't go in `WHERE`: compute it in a `WITH` (CTE), then filter.
- On a tie `ROW_NUMBER` picks either row, so add a tie-breaker: `ORDER BY amount DESC, dealer`.

**Latest ping per machine** (`ROW_NUMBER() OVER (PARTITION BY machine ORDER BY recorded_at DESC)`, keep `rn = 1`):

| machine | status | recorded_at |
|---|---|---|
| M1 | FAULT | 2026-10-24 10:00 |
| M2 | ACTIVE | 2026-10-24 09:30 |

**Top 2 per region** (`DENSE_RANK() OVER (PARTITION BY region ORDER BY amount DESC)`, keep `rnk <= 2`):

| region | dealer | amount | rnk |
|---|---|---|---|
| NORTH | D1 | 500 | 1 |
| NORTH | D2 | 500 | 1 |
| NORTH | D3 | 400 | 2 |
| SOUTH | D5 | 700 | 1 |
| SOUTH | D6 | 200 | 2 |

With `RANK`, D3 would be 3 and drop out.

**`LAG(col)` / `LEAD(col)`**: the value from the previous / next row (`NULL` for the first / last row).

| machine | recorded_at | status | previous_status |
|---|---|---|---|
| M1 | 08:00 | OK | NULL |
| M1 | 10:00 | FAULT | OK |

## Popular functions

### Text
| Function | What it does | Example → result |
|---|---|---|
| `TRIM(x)` | Remove spaces at both ends | `'  north farm  '` → `'north farm'` |
| `UPPER` / `LOWER` | Change case | `'north farm'` → `'NORTH FARM'` |
| `LENGTH(x)` | Number of characters | `'north farm'` → `10` |
| `SUBSTR(x, start, n)` | Part of text; **starts at 1** | `SUBSTR('north farm', 1, 5)` → `'north'` (MySQL: `SUBSTRING`, `LEFT(x, 5)`) |
| `REPLACE(x, a, b)` | Replace text | `REPLACE('north farm', ' ', '')` → `'northfarm'` |
| `a \|\| b` | Join text | `'D1' \|\| '-' \|\| 'north'` → `'D1-north'` (MySQL: `CONCAT(a, b)`) |

### Aggregates (one result per group)
| Function | What it does |
|---|---|
| `COUNT(*)` / `COUNT(col)` / `COUNT(DISTINCT col)` | All rows / rows where col isn't NULL / unique values. Example: `4 / 3 / 2` |
| `SUM`, `AVG`, `MIN`, `MAX` | Total, average, lowest, highest |
| `ROUND(x, 2)` | Round to 2 decimals |

```
region  rows  total  average  lowest  highest      (GROUP BY region)
NORTH   4     1700   425.0    300     500
SOUTH   2     900    450.0    200     700
```

**`WHERE` vs `HAVING`:** `WHERE` filters rows **before** grouping; `HAVING` filters groups **after**. `HAVING SUM(amount) > 1000` → only `NORTH 1700`.

### NULLs and conditions
| Function | What it does | Example → result |
|---|---|---|
| `COALESCE(a, b)` | First value that isn't NULL | After a `LEFT JOIN`, a dealer with no sales: `COALESCE(SUM(amount), 0)` → `0` instead of `NULL` |
| `NULLIF(a, b)` | NULL when `a = b` | `10 / NULLIF(0, 0)` → `NULL` instead of an error |
| `CASE WHEN … THEN … ELSE … END` | if / else | `SUM(CASE WHEN status = 'FAULT' THEN 1 ELSE 0 END)` counts faults |

**`LEFT JOIN` vs `JOIN`:** `LEFT JOIN` keeps every row from the left table even without a match (D9 with 0 sales); `JOIN` drops it.

**Division:** `7 / 2` → `3` in SQLite and SQL Server, `3.5` in MySQL. To be safe write `7 * 1.0 / 2` → `3.5`.

### Filtering and sorting
| Keyword | What it does |
|---|---|
| `LIKE 'D%'` | Pattern: `%` = any text, `_` = one character |
| `IN ('A', 'B')` | Matches any value in the list |
| `BETWEEN 200 AND 600` | Range, both ends included |
| `DISTINCT` | Unique rows only |
| `ORDER BY x DESC` | Sort; `ASC` (default) is lowest / A first |
| `LIMIT n` | First n rows (SQL Server: `TOP n`) |

### Dates
| Need | SQLite | MySQL |
|---|---|---|
| Date part | `SUBSTR(d, 1, 10)` | `DATE(d)` |
| Hour, year, month | `strftime('%H', d)` | `HOUR(d)`, `YEAR(d)`, `MONTH(d)` |
| Days between | `julianday(a) - julianday(b)` | `DATEDIFF(a, b)` |
