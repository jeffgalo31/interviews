-- New Companies (HackerRank, Advanced Select). Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite).
-- HackerRank already has the 5 tables filled in; locally we build the sample data
-- first, then run the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- This query is plain SQL, so it is the same in SQLite and MySQL.
-- The HackerRank copy is solution_hackerrank.sql.

-- ---------------------------------------------------------------------------
-- SETUP: sample tables (HackerRank does this for you)
-- Hierarchy: Founder -> Lead Manager -> Senior Manager -> Manager -> Employee
-- Every table carries company_code, which is what makes the query simple.
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Lead_Manager;
DROP TABLE IF EXISTS Senior_Manager;
DROP TABLE IF EXISTS Manager;
DROP TABLE IF EXISTS Employee;

CREATE TABLE Company        (company_code TEXT, founder TEXT);
CREATE TABLE Lead_Manager   (lead_manager_code TEXT, company_code TEXT);
CREATE TABLE Senior_Manager (senior_manager_code TEXT, lead_manager_code TEXT, company_code TEXT);
CREATE TABLE Manager        (manager_code TEXT, senior_manager_code TEXT, lead_manager_code TEXT, company_code TEXT);
CREATE TABLE Employee       (employee_code TEXT, manager_code TEXT, senior_manager_code TEXT, lead_manager_code TEXT, company_code TEXT);

INSERT INTO Company VALUES ('C1', 'Monika'), ('C2', 'Samantha');

INSERT INTO Lead_Manager VALUES ('LM1', 'C1'), ('LM2', 'C2');

INSERT INTO Senior_Manager VALUES
    ('SM1', 'LM1', 'C1'),
    ('SM2', 'LM1', 'C1'),
    ('SM3', 'LM2', 'C2');

INSERT INTO Manager VALUES
    ('M1', 'SM1', 'LM1', 'C1'),
    ('M2', 'SM3', 'LM2', 'C2'),
    ('M3', 'SM3', 'LM2', 'C2');

INSERT INTO Employee VALUES
    ('E1', 'M1', 'SM1', 'LM1', 'C1'),
    ('E2', 'M1', 'SM1', 'LM1', 'C1'),
    ('E3', 'M2', 'SM3', 'LM2', 'C2'),
    ('E4', 'M3', 'SM3', 'LM2', 'C2');

-- Try it: uncomment to add a DUPLICATE row. The answer must not change,
-- which is why the query uses COUNT(DISTINCT ...) instead of COUNT(*).
-- INSERT INTO Senior_Manager VALUES ('SM1', 'LM1', 'C1');

-- ---------------------------------------------------------------------------
-- QUERY: one row per company + 4 counts
-- Expected:  C1 Monika 1 2 1 2  /  C2 Samantha 1 1 2 2
-- ---------------------------------------------------------------------------
SELECT c.company_code,
       c.founder,

       -- Each (SELECT ...) runs once per company row "c" (correlated subquery):
       -- "count the distinct codes in this table that belong to company c".
       (SELECT COUNT(DISTINCT lm.lead_manager_code)      -- DISTINCT: ignore duplicate rows
          FROM Lead_Manager lm
         WHERE lm.company_code = c.company_code) AS lead_managers,

       (SELECT COUNT(DISTINCT sm.senior_manager_code)
          FROM Senior_Manager sm
         WHERE sm.company_code = c.company_code) AS senior_managers,

       (SELECT COUNT(DISTINCT m.manager_code)
          FROM Manager m
         WHERE m.company_code = c.company_code) AS managers,

       (SELECT COUNT(DISTINCT e.employee_code)
          FROM Employee e
         WHERE e.company_code = c.company_code) AS employees

FROM Company c
ORDER BY c.company_code;   -- text sort: C_1, C_10, C_2 (what the problem wants)
