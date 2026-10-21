-- The PADS (HackerRank, Advanced Select). Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite).
-- HackerRank already has the OCCUPATIONS table filled in; locally we have to create
-- it ourselves, so this file first builds the sample table, then runs the 2 queries.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
--
-- HackerRank uses MySQL, SQLite has a few different function names:
--   MySQL CONCAT(a, b, c)  ->  SQLite  a || b || c
--   MySQL LEFT(s, 1)       ->  SQLite  SUBSTR(s, 1, 1)
-- The HackerRank copy (MySQL) is solution_hackerrank.sql.

-- ---------------------------------------------------------------------------
-- SETUP: the sample table from the problem (HackerRank does this for you)
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS OCCUPATIONS;   -- safe to re-run even on a saved database

CREATE TABLE OCCUPATIONS (
    Name       TEXT,
    Occupation TEXT    -- only Doctor, Professor, Singer or Actor
);

INSERT INTO OCCUPATIONS (Name, Occupation) VALUES
    ('Samantha',  'Doctor'),
    ('Julia',     'Actor'),
    ('Maria',     'Actor'),
    ('Meera',     'Singer'),
    ('Ashely',    'Professor'),
    ('Ketty',     'Professor'),
    ('Christeen', 'Professor'),
    ('Jane',      'Actor'),
    ('Jenny',     'Doctor'),
    ('Priya',     'Singer');

-- ---------------------------------------------------------------------------
-- QUERY 1: every name + first letter of its occupation, e.g. Ashely(P)
-- ---------------------------------------------------------------------------
SELECT Name                          -- Ashely
       || '('                        -- Ashely(
       || SUBSTR(Occupation, 1, 1)   -- Ashely(P      first letter of "Professor"
       || ')'                        -- Ashely(P)
       AS name_with_initial
FROM OCCUPATIONS
ORDER BY Name;                       -- alphabetical by name

-- ---------------------------------------------------------------------------
-- QUERY 2: one sentence per occupation, e.g. "There are a total of 3 actors."
-- ---------------------------------------------------------------------------
SELECT 'There are a total of '
       || COUNT(*)                   -- rows in this group: 3
       || ' '
       || LOWER(Occupation)          -- "Actor" -> "actor"
       || 's.'                       -- plural + period: "actors."
       AS occupation_total
FROM OCCUPATIONS
GROUP BY Occupation                  -- one group (one output row) per occupation
ORDER BY COUNT(*),                   -- smallest count first: 2, 2, 3, 3
         Occupation;                 -- ties: alphabetical (Doctor < Singer, Actor < Professor)
