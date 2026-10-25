-- SQL refresher for HackerRank: ranking functions + the most-used functions.
-- Run: open this file in VS Code -> Terminal -> Run Task -> Run SQL file (SQLite)
--      or in a terminal (sql folder):  sqlite3 -header -column :memory: < refresher/refresher.sql
-- Each query has a comment with what it does and the expected result.
-- SQLite here; HackerRank MySQL differences are noted as "MySQL:".

CREATE TABLE sales (dealer TEXT, region TEXT, amount INTEGER);
INSERT INTO sales VALUES
  ('D1', 'NORTH', 500), ('D2', 'NORTH', 500), ('D3', 'NORTH', 400), ('D4', 'NORTH', 300),
  ('D5', 'SOUTH', 700), ('D6', 'SOUTH', 200);

CREATE TABLE pings (machine TEXT, status TEXT, recorded_at TEXT, fuel REAL);
INSERT INTO pings VALUES
  ('M1', 'OK',     '2026-10-24 08:00', 80),
  ('M1', 'FAULT',  '2026-10-24 10:00', 35),
  ('M2', 'ACTIVE', '2026-10-24 09:30', NULL),
  ('M2', 'OK',     '2026-10-24 07:15', 60);

CREATE TABLE dealers (dealer TEXT, name TEXT);
INSERT INTO dealers VALUES ('D1', '  north farm  '), ('D2', 'Valley Equipment'), ('D9', 'New Dealer');


-- =====================================================================================
-- PART 1: RANKING (window functions)
-- The three only differ on TIES. Sorted by amount: 500, 500, 400, 300
--   ROW_NUMBER  1, 2, 3, 4   never ties           -> "latest / first / one row per X", remove duplicates
--   RANK        1, 1, 3, 4   ties, then SKIPS     -> only if the problem asks for "competition ranking"
--   DENSE_RANK  1, 1, 2, 3   ties, never skips    -> "top N", "2nd highest", "Nth highest"
-- PARTITION BY = restart the numbering per group.  ORDER BY = what decides the order.
-- =====================================================================================

.print '--- 1a. ROW_NUMBER vs RANK vs DENSE_RANK side by side (NORTH) ---'
SELECT dealer, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS row_num,
       RANK()       OVER (ORDER BY amount DESC) AS rnk,
       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rnk
FROM sales
WHERE region = 'NORTH';
-- D1 500 1 1 1 | D2 500 2 1 1 | D3 400 3 3 2 | D4 300 4 4 3
-- On a tie ROW_NUMBER picks either row: add a tie-breaker, e.g. ORDER BY amount DESC, dealer

.print '--- 1b. Latest ping per machine: ROW_NUMBER + PARTITION BY, then keep rn = 1 ---'
-- A window function can't go in WHERE: compute it in a CTE (WITH), then filter.
WITH ranked AS (
  SELECT machine, status, recorded_at,
         ROW_NUMBER() OVER (PARTITION BY machine ORDER BY recorded_at DESC) AS rn
  FROM pings
)
SELECT machine, status, recorded_at FROM ranked WHERE rn = 1;
-- M1 FAULT 10:00 | M2 ACTIVE 09:30

.print '--- 1c. Top 2 amounts per region: DENSE_RANK keeps ties and does not skip ---'
WITH ranked AS (
  SELECT region, dealer, amount,
         DENSE_RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS rnk
  FROM sales
)
SELECT region, dealer, amount, rnk FROM ranked WHERE rnk <= 2 ORDER BY region, rnk;
-- NORTH D1 500 1 | NORTH D2 500 1 | NORTH D3 400 2 | SOUTH D5 700 1 | SOUTH D6 200 2
-- With RANK, D3 would be 3 and drop out.

.print '--- 1d. LAG / LEAD: value from the previous / next row ---'
SELECT machine, recorded_at, status,
       LAG(status) OVER (PARTITION BY machine ORDER BY recorded_at) AS previous_status
FROM pings;
-- First row of each machine has no previous row -> NULL


-- =====================================================================================
-- PART 2: POPULAR FUNCTIONS
-- =====================================================================================

.print '--- 2a. Text: TRIM, UPPER, LOWER, LENGTH, SUBSTR, REPLACE, || ---'
SELECT TRIM(name)              AS trimmed,     -- remove spaces at both ends: 'north farm'
       UPPER(TRIM(name))       AS upper_name,  -- 'NORTH FARM'   (LOWER does the opposite)
       LENGTH(TRIM(name))      AS len,         -- 10
       SUBSTR(TRIM(name), 1, 5) AS first5,     -- 'north'  start at 1 (not 0!), take 5. MySQL: SUBSTRING or LEFT(x, 5)
       REPLACE(name, ' ', '')  AS no_spaces,   -- 'northfarm'
       dealer || '-' || TRIM(name) AS label    -- 'D1-north farm'. MySQL: CONCAT(dealer, '-', name)
FROM dealers WHERE dealer = 'D1';

.print '--- 2b. Aggregates: COUNT, SUM, AVG, MIN, MAX, ROUND ---'
SELECT region,
       COUNT(*)              AS rows_count,    -- number of rows in the group
       SUM(amount)           AS total,
       ROUND(AVG(amount), 2) AS average,       -- AVG + round to 2 decimals
       MIN(amount)           AS lowest,
       MAX(amount)           AS highest
FROM sales
GROUP BY region;                               -- one result row per region
-- NORTH 4 1700 425.0 300 500 | SOUTH 2 900 450.0 200 700

.print '--- 2c. HAVING filters groups (WHERE filters rows before grouping) ---'
SELECT region, SUM(amount) AS total
FROM sales
GROUP BY region
HAVING SUM(amount) > 1000;
-- NORTH 1700

.print '--- 2d. COUNT(*) vs COUNT(column) vs COUNT(DISTINCT column) ---'
SELECT COUNT(*) AS all_rows,                   -- 4: counts every row
       COUNT(fuel) AS with_fuel,               -- 3: skips NULLs
       COUNT(DISTINCT machine) AS machines     -- 2: unique values only
FROM pings;

.print '--- 2e. COALESCE (first non-NULL) after a LEFT JOIN ---'
-- LEFT JOIN keeps every dealer, even with no sales (their SUM is NULL -> COALESCE makes it 0)
SELECT d.dealer, COALESCE(SUM(s.amount), 0) AS total
FROM dealers d
LEFT JOIN sales s ON s.dealer = d.dealer
GROUP BY d.dealer;
-- D1 500 | D2 500 | D9 0

.print '--- 2f. NULLIF (avoid divide by zero) and integer division ---'
SELECT 7 / 2                AS int_division,   -- 3 here and in SQL Server (decimals cut). MySQL and Oracle give 3.5
       7 * 1.0 / 2          AS decimal_div,    -- 3.5 (multiply by 1.0 first)
       10 / NULLIF(0, 0)    AS safe_divide;    -- NULL instead of an error (NULLIF(a, b) = NULL when a = b)

.print '--- 2g. CASE WHEN (if/else) and counting by condition ---'
SELECT machine,
       SUM(CASE WHEN status = 'FAULT' THEN 1 ELSE 0 END) AS faults,
       CASE WHEN MAX(fuel) >= 70 THEN 'HIGH' ELSE 'LOW' END AS fuel_level
FROM pings
GROUP BY machine;
-- M1 1 HIGH | M2 0 LOW

.print '--- 2h. LIKE, IN, BETWEEN, DISTINCT, ORDER BY, LIMIT ---'
SELECT DISTINCT region                  -- unique values only
FROM sales
WHERE dealer LIKE 'D%'                  -- % = any text, _ = exactly one character
  AND amount BETWEEN 200 AND 600        -- inclusive on both ends
  AND region IN ('NORTH', 'SOUTH')
ORDER BY region DESC                    -- DESC = highest/Z first; ASC (default) = lowest/A first
LIMIT 1;                                -- first row only (Oracle/SQL Server: FETCH FIRST / TOP)
-- SOUTH

.print '--- 2i. Dates: part of a date, difference in days ---'
SELECT recorded_at,
       SUBSTR(recorded_at, 1, 10)  AS just_date,  -- MySQL: DATE(recorded_at)
       strftime('%H', recorded_at) AS hour,       -- MySQL: HOUR(recorded_at), YEAR(), MONTH()
       CAST(julianday('2026-10-31') - julianday(SUBSTR(recorded_at, 1, 10)) AS INTEGER) AS days_left
                                                  -- MySQL: DATEDIFF('2026-10-31', recorded_at)
FROM pings WHERE machine = 'M1';
-- 2026-10-24 08:00 2026-10-24 08 7 | 2026-10-24 10:00 2026-10-24 10 7
