-- Revising Aggregations - Averages  (Easy · Aggregation)  https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- HackerRank copy (MySQL): solution_hackerrank.sql

-- ---------------------------------------------------------------------------
-- SETUP: sample data (made up: HackerRank shows no sample for this one)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS CITY;
CREATE TABLE CITY (ID INTEGER, NAME TEXT, COUNTRYCODE TEXT, DISTRICT TEXT, POPULATION INTEGER);
INSERT INTO CITY VALUES
    (6,    'Rotterdam',       'NLD', 'Zuid-Holland',  593321),
    (3878, 'Scottsdale',      'USA', 'Arizona',       202705),
    (3965, 'Corona',          'USA', 'California',    124966),
    (3973, 'Concord',         'USA', 'California',    121780),
    (3977, 'Cedar Rapids',    'USA', 'Iowa',          120758),
    (3982, 'Coral Springs',   'USA', 'Florida',       117549),
    (4054, 'Fairfield',       'USA', 'California',     92256),
    (4058, 'Boulder',         'USA', 'Colorado',       91238),
    (1532, 'Tokyo',           'JPN', 'Tokyo-to',     7980230),
    (1630, 'Ageo',            'JPN', 'Saitama',       209442),
    (1661, 'Sayama',          'JPN', 'Saitama',       162472),
    (1739, 'Tokuyama',        'JPN', 'Yamaguchi',     107078),
    (1890, 'Shanghai',        'CHN', 'Shanghai',     9696300),
    (1024, 'Mumbai (Bombay)', 'IND', 'Maharashtra', 10500000),
    (2457, 'Lagos',           'NGA', 'Lagos',        1518000),
    (608,  'Cairo',           'EGY', 'Kairo',        6789479);

-- ---------------------------------------------------------------------------
-- QUERY
-- ---------------------------------------------------------------------------
-- AVG = sum / number of rows, over the filtered rows.
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';
