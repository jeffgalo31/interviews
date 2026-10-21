#!/usr/bin/env python3
"""Generate HackerRank SQL exercises: README.md, solution.sql (SQLite, runnable), solution_hackerrank.sql (MySQL)."""
import json, os, re, sqlite3, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from images import IMG, EXPLAIN, sql_values, CH0_H, CH0_C, CH1_H, CH1_C, CL_H, CL_S, OL_W, OL_P, IV_CT, IV_CO, IV_CH, IV_V, IV_S, FD_H, FD_S, OCC_ROWS

SRC, OUT = sys.argv[1], sys.argv[2]
CH = {c["slug"]: c for c in json.load(open(SRC))}

SECTION_DIR = {"Basic Select": "basic-select", "Advanced Select": "advanced-select", "Aggregation": "aggregation",
               "Basic Join": "basic-join", "Advanced Join": "advanced-join", "Alternative Queries": "alternative-queries"}
EXISTING = {"the-pads": "the-pads", "the-company": "new-companies", "binary-search-tree-1": "binary-tree-nodes"}

def folder(name):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", name.lower().replace("'", ""))).strip("-")

# ----------------------------------------------------------------------------- shared sample tables
CITY = """CREATE TABLE CITY (ID INTEGER, NAME TEXT, COUNTRYCODE TEXT, DISTRICT TEXT, POPULATION INTEGER);
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
    (608,  'Cairo',           'EGY', 'Kairo',        6789479);"""

COUNTRY = """-- (simplified: HackerRank's COUNTRY has more columns, only these are used)
CREATE TABLE COUNTRY (CODE TEXT, NAME TEXT, CONTINENT TEXT, REGION TEXT, POPULATION INTEGER);
INSERT INTO COUNTRY VALUES
    ('NLD', 'Netherlands',   'Europe',        'Western Europe',   15864000),
    ('USA', 'United States', 'North America', 'North America',   278357000),
    ('JPN', 'Japan',         'Asia',          'Eastern Asia',    126714000),
    ('CHN', 'China',         'Asia',          'Eastern Asia',   1277558000),
    ('IND', 'India',         'Asia',          'Southern Asia',  1013662000),
    ('NGA', 'Nigeria',       'Africa',        'Western Africa',  111506000),
    ('EGY', 'Egypt',         'Africa',        'Northern Africa',  68470000);"""

STATION = """CREATE TABLE STATION (ID INTEGER, CITY TEXT, STATE TEXT, LAT_N REAL, LONG_W REAL);
INSERT INTO STATION VALUES
    (1, 'Acme',         'LA',  36.7,   41.2),
    (2, 'Ozark',        'AL',  50.9,   86.6),
    (3, 'Upton',        'WY', 103.2,  122.1),
    (4, 'Amo',          'IN',  75.5,   57.9),
    (5, 'Kissee Mills', 'MO', 139.65,  73.42),
    (6, 'Ozark',        'AL',  62.3,   45.9),
    (7, 'Loma Mar',     'CA',  48.69, 130.33),
    (8, 'Eros',         'LA', 137.2,   69.1),
    (9, 'Gustine',      'CA',  38.9,  140.5);"""

EMPLOYEE = """CREATE TABLE Employee (employee_id INTEGER, name TEXT, months INTEGER, salary INTEGER);
INSERT INTO Employee VALUES
    (12228, 'Rose',     15, 1968),
    (33645, 'Angela',    1, 3443),
    (45692, 'Frank',    17, 1608),
    (56118, 'Patrick',   7, 1345),
    (59725, 'Lisa',     11, 2330),
    (74197, 'Kimberly', 16, 4372),
    (78454, 'Bonnie',    8, 1771),
    (83565, 'Michael',   6, 2017),
    (98607, 'Todd',      5, 3396),
    (99989, 'Joe',       9, 3573);"""

EX = []
def ex(slug, setup, local, notes, hr=None, expected=None, sample="made-up", local_note=None, second=None):
    EX.append(dict(slug=slug, setup=setup, local=local.strip(), hr=(hr or local).strip(), notes=notes,
                   expected=expected, sample=sample, local_note=local_note, second=second))

# ============================================================================ BASIC SELECT
ex("revising-the-select-query", CITY,
   "SELECT *\nFROM CITY\nWHERE COUNTRYCODE = 'USA'\n  AND POPULATION > 100000;",
   ["`SELECT *` returns every column.", "`WHERE` keeps only rows where **both** conditions are true (`AND`)."])
ex("revising-the-select-query-2", CITY,
   "SELECT NAME\nFROM CITY\nWHERE COUNTRYCODE = 'USA'\n  AND POPULATION > 120000;",
   ["Same filter idea as part I, but only the `NAME` column is selected."])
ex("select-all-sql", CITY, "SELECT *\nFROM CITY;", ["No `WHERE`: every row, every column."])
ex("select-by-id", CITY, "SELECT *\nFROM CITY\nWHERE ID = 1661;", ["Filter on the primary key: returns one row."])
ex("japanese-cities-attributes", CITY, "SELECT *\nFROM CITY\nWHERE COUNTRYCODE = 'JPN';",
   ["Text values go in single quotes: `'JPN'`."])
ex("japanese-cities-name", CITY, "SELECT NAME\nFROM CITY\nWHERE COUNTRYCODE = 'JPN';", ["Same filter, only the `NAME` column."])
ex("weather-observation-station-1", STATION, "SELECT CITY, STATE\nFROM STATION;", ["List the two columns, separated by a comma."])
ex("weather-observation-station-3", STATION,
   "SELECT DISTINCT CITY\nFROM STATION\nWHERE ID % 2 = 0;",
   ["`ID % 2 = 0`: the remainder of dividing by 2 is 0, so the ID is even (`MOD(ID, 2) = 0` also works in MySQL).",
    "`DISTINCT` removes duplicate city names."])
ex("weather-observation-station-4", STATION,
   "SELECT COUNT(CITY) - COUNT(DISTINCT CITY)\nFROM STATION;",
   ["`COUNT(CITY)` counts all rows, `COUNT(DISTINCT CITY)` counts unique names; the difference is the number of repeats."])
ex("weather-observation-station-5",
   "CREATE TABLE STATION (ID INTEGER, CITY TEXT, STATE TEXT, LAT_N REAL, LONG_W REAL);\n"
   "INSERT INTO STATION (ID, CITY) VALUES (1, 'DEF'), (2, 'ABC'), (3, 'PQRS'), (4, 'WXY');",
   "SELECT CITY, LENGTH(CITY)\nFROM STATION\nORDER BY LENGTH(CITY), CITY\nLIMIT 1;\n\n"
   "SELECT CITY, LENGTH(CITY)\nFROM STATION\nORDER BY LENGTH(CITY) DESC, CITY\nLIMIT 1;",
   ["Two separate queries (allowed by the note).",
    "Shortest: sort by length ascending, ties alphabetically, keep the first row (`LIMIT 1`).",
    "Longest: sort by length **descending**, ties still alphabetically, keep the first row."],
   expected=["ABC 3", "PQRS 4"], sample="official")

VOW = "('a', 'e', 'i', 'o', 'u')"
first, last = "LOWER(SUBSTR(CITY, 1, 1))", "LOWER(SUBSTR(CITY, -1, 1))"
vowel_notes = ["`SUBSTR(CITY, 1, 1)` is the first character, `SUBSTR(CITY, -1, 1)` the last (negative = count from the end).",
               "`LOWER(...)` so `A` and `a` both match the vowel list.", "`DISTINCT` because the result cannot contain duplicates."]
ex("weather-observation-station-6", STATION, f"SELECT DISTINCT CITY\nFROM STATION\nWHERE {first} IN {VOW};", vowel_notes)
ex("weather-observation-station-7", STATION, f"SELECT DISTINCT CITY\nFROM STATION\nWHERE {last} IN {VOW};", vowel_notes)
ex("weather-observation-station-8", STATION,
   f"SELECT DISTINCT CITY\nFROM STATION\nWHERE {first} IN {VOW}\n  AND {last} IN {VOW};",
   vowel_notes + ["Both conditions must hold: `AND`."])
ex("weather-observation-station-9", STATION, f"SELECT DISTINCT CITY\nFROM STATION\nWHERE {first} NOT IN {VOW};",
   vowel_notes + ["`NOT IN` flips the test: first letter is **not** a vowel."])
ex("weather-observation-station-10", STATION, f"SELECT DISTINCT CITY\nFROM STATION\nWHERE {last} NOT IN {VOW};",
   vowel_notes + ["`NOT IN`: last letter is **not** a vowel."])
ex("weather-observation-station-11", STATION,
   f"SELECT DISTINCT CITY\nFROM STATION\nWHERE {first} NOT IN {VOW}\n   OR {last} NOT IN {VOW};",
   vowel_notes + ["\"either ... or\" = `OR`: one failing check is enough."])
ex("weather-observation-station-12", STATION,
   f"SELECT DISTINCT CITY\nFROM STATION\nWHERE {first} NOT IN {VOW}\n  AND {last} NOT IN {VOW};",
   vowel_notes + ["\"do not start and do not end\" = `AND`: both checks must fail."])
ex("more-than-75-marks",
   "CREATE TABLE STUDENTS (ID INTEGER, NAME TEXT, MARKS INTEGER);\n"
   "INSERT INTO STUDENTS VALUES (1, 'Ashley', 81), (2, 'Samantha', 75), (4, 'Julia', 76), (3, 'Belvet', 84);",
   "SELECT NAME\nFROM STUDENTS\nWHERE MARKS > 75\nORDER BY SUBSTR(NAME, -3), ID;",
   ["`SUBSTR(NAME, -3)` = last three characters (`RIGHT(NAME, 3)` is the same in MySQL).",
    "Second sort key `ID` breaks ties when two names end the same way.", "`> 75` excludes Samantha's exact 75."],
   expected=["Ashley", "Julia", "Belvet"], sample="official")
ex("name-of-employees", EMPLOYEE, "SELECT name\nFROM Employee\nORDER BY name;", ["`ORDER BY name` sorts alphabetically (ascending is the default)."],
   expected="Angela Bonnie Frank Joe Kimberly Lisa Michael Patrick Rose Todd".split(), sample="official")
ex("salary-of-employees", EMPLOYEE,
   "SELECT name\nFROM Employee\nWHERE salary > 2000\n  AND months < 10\nORDER BY employee_id;",
   ["Both conditions with `AND`.", "Output is sorted by `employee_id`, even though only `name` is printed."],
   expected=["Angela", "Michael", "Todd", "Joe"], sample="official")

# ============================================================================ ADVANCED SELECT
ex("what-type-of-triangle",
   "CREATE TABLE TRIANGLES (A INTEGER, B INTEGER, C INTEGER);\n"
   "INSERT INTO TRIANGLES VALUES (20, 20, 23), (20, 20, 20), (20, 21, 22), (13, 14, 30);",
   """SELECT CASE
           WHEN A + B <= C OR A + C <= B OR B + C <= A THEN 'Not A Triangle'
           WHEN A = B AND B = C                       THEN 'Equilateral'
           WHEN A = B OR B = C OR A = C               THEN 'Isosceles'
           ELSE 'Scalene'
       END
FROM TRIANGLES;""",
   ["Check **Not A Triangle first**: `CASE` stops at the first true `WHEN`, and (13, 13, 30) would otherwise be labeled Isosceles.",
    "A triangle needs every pair of sides to add up to more than the third side.",
    "Then all three equal, then any two equal, otherwise all different."],
   expected=["Isosceles", "Equilateral", "Scalene", "Not A Triangle"], sample="official")
ex("occupations", "CREATE TABLE OCCUPATIONS (Name TEXT, Occupation TEXT);\nINSERT INTO OCCUPATIONS VALUES\n" + sql_values(OCC_ROWS),
   """SELECT MAX(CASE WHEN Occupation = 'Doctor'    THEN Name END) AS Doctor,
       MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS Professor,
       MAX(CASE WHEN Occupation = 'Singer'    THEN Name END) AS Singer,
       MAX(CASE WHEN Occupation = 'Actor'     THEN Name END) AS Actor
FROM (
    SELECT Name, Occupation,
           ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS rn
    FROM OCCUPATIONS
) ranked
GROUP BY rn
ORDER BY rn;""",
   ["`ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name)` numbers the names 1, 2, 3... inside each occupation, alphabetically.",
    "`GROUP BY rn` makes one output row per position: row 1 holds the 1st doctor, 1st professor, ...",
    "`MAX(CASE WHEN ... THEN Name END)` picks the one name for that column; when an occupation has no name at that position it is NULL.",
    "Window functions need MySQL 8 (HackerRank's MySQL) / SQLite 3.25+.",
    "HackerRank's sample table spells the name **Ashely** while its Sample Output says **Ashley** (a typo on HackerRank); the local run prints Ashely."],
   expected=["Jenny Ashely Meera Jane", "Samantha Christeen Priya Julia", "NULL Ketty NULL Maria"], sample="official")

# ============================================================================ AGGREGATION
ex("revising-aggregations-the-count-function", CITY, "SELECT COUNT(*)\nFROM CITY\nWHERE POPULATION > 100000;",
   ["`COUNT(*)` counts the rows that pass the `WHERE` filter."])
ex("revising-aggregations-sum", CITY, "SELECT SUM(POPULATION)\nFROM CITY\nWHERE DISTRICT = 'California';",
   ["`SUM` adds the column over the filtered rows."])
ex("revising-aggregations-the-average-function", CITY, "SELECT AVG(POPULATION)\nFROM CITY\nWHERE DISTRICT = 'California';",
   ["`AVG` = sum / number of rows, over the filtered rows."])
ex("average-population", CITY, "SELECT CAST(AVG(POPULATION) AS INTEGER)\nFROM CITY;",
   ["Rounded **down**: `FLOOR(AVG(...))` in MySQL.", "Local SQLite has no `FLOOR` by default; `CAST(... AS INTEGER)` cuts off the decimals, which is the same for positive numbers."],
   hr="SELECT FLOOR(AVG(POPULATION))\nFROM CITY;", local_note="`FLOOR(x)` → `CAST(x AS INTEGER)`")
ex("japan-population", CITY, "SELECT SUM(POPULATION)\nFROM CITY\nWHERE COUNTRYCODE = 'JPN';", ["Filter to Japan, then `SUM`."])
ex("population-density-difference", CITY, "SELECT MAX(POPULATION) - MIN(POPULATION)\nFROM CITY;",
   ["Two aggregates in one expression: largest minus smallest."])
ex("the-blunder",
   "CREATE TABLE EMPLOYEES (ID INTEGER, Name TEXT, Salary INTEGER);\n"
   "INSERT INTO EMPLOYEES VALUES (1, 'Kristeen', 1420), (2, 'Ashley', 2006), (3, 'Julia', 2210), (4, 'Maria', 3000);",
   """SELECT CAST(err AS INTEGER) + (err > CAST(err AS INTEGER))   -- round UP (CEIL)
FROM (
    SELECT AVG(Salary)
         - AVG(CAST(REPLACE(CAST(Salary AS TEXT), '0', '') AS INTEGER)) AS err
    FROM EMPLOYEES
) t;""",
   ["Samantha's salaries = the real salaries with every `0` removed: `REPLACE(Salary, '0', '')` (1420 → 142).",
    "Error = real average − miscalculated average, then round **up** with `CEIL`.",
    "Local SQLite: no `CEIL`, so it adds 1 when there is a decimal part."],
   hr="SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, '0', '')))\nFROM EMPLOYEES;",
   expected=["2061"], sample="official", local_note="`CEIL(x)` → integer part + 1 if there are decimals")
ex("earnings-of-employees", EMPLOYEE,
   "SELECT salary * months AS earnings, COUNT(*)\nFROM Employee\nGROUP BY earnings\nORDER BY earnings DESC\nLIMIT 1;",
   ["Group employees by their total earnings and count each group.",
    "Highest earnings first, keep only that row: the max and how many employees have it."],
   expected=["69952 1"], sample="official")
ex("weather-observation-station-2", STATION, "SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2)\nFROM STATION;",
   ["`ROUND(x, 2)` keeps 2 decimal places."])
ex("weather-observation-station-13", STATION,
   "SELECT CAST(SUM(LAT_N) * 10000 AS INTEGER) / 10000.0\nFROM STATION\nWHERE LAT_N > 38.7880\n  AND LAT_N < 137.2345;",
   ["**Truncate** (cut off) to 4 decimals, not round: `TRUNCATE(x, 4)` in MySQL.",
    "Local SQLite: multiply by 10000, drop the decimals, divide back."],
   hr="SELECT TRUNCATE(SUM(LAT_N), 4)\nFROM STATION\nWHERE LAT_N > 38.7880\n  AND LAT_N < 137.2345;",
   local_note="`TRUNCATE(x, 4)` → `CAST(x * 10000 AS INTEGER) / 10000.0`")
ex("weather-observation-station-14", STATION,
   "SELECT CAST(MAX(LAT_N) * 10000 AS INTEGER) / 10000.0\nFROM STATION\nWHERE LAT_N < 137.2345;",
   ["Largest value **below** the limit: filter first, then `MAX`.", "Truncate to 4 decimals (`TRUNCATE` in MySQL)."],
   hr="SELECT TRUNCATE(MAX(LAT_N), 4)\nFROM STATION\nWHERE LAT_N < 137.2345;",
   local_note="`TRUNCATE(x, 4)` → `CAST(x * 10000 AS INTEGER) / 10000.0`")
ex("weather-observation-station-15", STATION,
   "SELECT ROUND(LONG_W, 4)\nFROM STATION\nWHERE LAT_N < 137.2345\nORDER BY LAT_N DESC\nLIMIT 1;",
   ["We need a value from the **row** with the largest LAT_N, so sort instead of using `MAX`: largest LAT_N first, keep 1 row."])
ex("weather-observation-station-16", STATION, "SELECT ROUND(MIN(LAT_N), 4)\nFROM STATION\nWHERE LAT_N > 38.7780;",
   ["Smallest value **above** the limit: filter, then `MIN`, then round."])
ex("weather-observation-station-17", STATION,
   "SELECT ROUND(LONG_W, 4)\nFROM STATION\nWHERE LAT_N > 38.7780\nORDER BY LAT_N\nLIMIT 1;",
   ["Value from the row with the smallest LAT_N above the limit: sort ascending, keep 1 row."])
ex("weather-observation-station-18", STATION,
   "SELECT ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)), 4)\nFROM STATION;",
   ["Manhattan distance = |a − c| + |b − d|.", "a, c are MIN/MAX of LAT_N; b, d are MIN/MAX of LONG_W."])
ex("weather-observation-station-19", STATION,
   """SELECT ROUND(SQRT((MAX(LAT_N) - MIN(LAT_N)) * (MAX(LAT_N) - MIN(LAT_N))
                + (MAX(LONG_W) - MIN(LONG_W)) * (MAX(LONG_W) - MIN(LONG_W))), 4)
FROM STATION;""",
   ["Euclidean distance = √((b − a)² + (d − c)²) with a, b = min/max LAT_N and c, d = min/max LONG_W.",
    "Local SQLite needs `SQRT` (built in on most current builds); if yours says \"no such function\", the HackerRank version still works."],
   hr="SELECT ROUND(SQRT(POWER(MAX(LAT_N) - MIN(LAT_N), 2) + POWER(MAX(LONG_W) - MIN(LONG_W), 2)), 4)\nFROM STATION;",
   local_note="`POWER(x, 2)` → `x * x`")
ex("weather-observation-station-20", STATION,
   """SELECT ROUND(s.LAT_N, 4)
FROM STATION s
WHERE (SELECT COUNT(*) FROM STATION WHERE LAT_N < s.LAT_N)
    = (SELECT COUNT(*) FROM STATION WHERE LAT_N > s.LAT_N);""",
   ["The median is the value with as many values below it as above it.",
    "For each row, count the smaller and the larger LAT_N values; keep the row where both counts are equal.",
    "Works when the row count is odd (HackerRank's STATION has 499 rows)."])

# ============================================================================ BASIC JOIN
J = CITY + "\n\n" + COUNTRY
ex("asian-population", J,
   "SELECT SUM(CITY.POPULATION)\nFROM CITY\nJOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE\nWHERE COUNTRY.CONTINENT = 'Asia';",
   ["`JOIN ... ON` attaches each city's country row, so we can filter on CONTINENT.", "Then `SUM` the city populations."])
ex("african-cities", J,
   "SELECT CITY.NAME\nFROM CITY\nJOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE\nWHERE COUNTRY.CONTINENT = 'Africa';",
   ["Join on the matching key columns, filter on the continent, select the city name."])
ex("average-population-of-each-continent", J,
   "SELECT COUNTRY.CONTINENT, CAST(AVG(CITY.POPULATION) AS INTEGER)\nFROM CITY\nJOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE\nGROUP BY COUNTRY.CONTINENT;",
   ["`GROUP BY CONTINENT`: one row per continent with the average of its cities.", "Rounded down: `FLOOR` in MySQL."],
   hr="SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))\nFROM CITY\nJOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE\nGROUP BY COUNTRY.CONTINENT;",
   local_note="`FLOOR(x)` → `CAST(x AS INTEGER)`")
ex("the-report",
   "CREATE TABLE Students (ID INTEGER, Name TEXT, Marks INTEGER);\n"
   "INSERT INTO Students VALUES (1, 'Julia', 88), (2, 'Samantha', 68), (3, 'Maria', 99), (4, 'Scarlet', 78), (5, 'Ashley', 63), (6, 'Jane', 81);\n\n"
   "CREATE TABLE Grades (Grade INTEGER, Min_Mark INTEGER, Max_Mark INTEGER);\n"
   "INSERT INTO Grades VALUES (1, 0, 9), (2, 10, 19), (3, 20, 29), (4, 30, 39), (5, 40, 49),\n"
   "                          (6, 50, 59), (7, 60, 69), (8, 70, 79), (9, 80, 89), (10, 90, 100);",
   """SELECT CASE WHEN g.Grade >= 8 THEN s.Name ELSE NULL END AS Name,
       g.Grade,
       s.Marks
FROM Students s
JOIN Grades g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY g.Grade DESC,
         CASE WHEN g.Grade >= 8 THEN s.Name END,
         s.Marks;""",
   ["The join is a **range**: each mark matches the grade row whose `Min_Mark`..`Max_Mark` contains it.",
    "`CASE` hides names below grade 8 (prints NULL).",
    "Sort: grade high → low; then name (only for grades 8-10, NULL for the rest); then marks ascending, which orders the NULL rows."],
   expected=["Maria 10 99", "Jane 9 81", "Julia 9 88", "Scarlet 8 78", "NULL 7 63", "NULL 7 68"], sample="official")
ex("full-score",
   """CREATE TABLE Hackers (hacker_id INTEGER, name TEXT);
INSERT INTO Hackers VALUES (5580, 'Rose'), (8439, 'Angela'), (27205, 'Frank'), (52243, 'Patrick'), (52348, 'Lisa'),
                           (57645, 'Kimberly'), (77726, 'Bonnie'), (83082, 'Michael'), (86870, 'Todd'), (90411, 'Joe');

CREATE TABLE Difficulty (difficulty_level INTEGER, score INTEGER);
INSERT INTO Difficulty VALUES (1, 20), (2, 30), (3, 40), (4, 60), (5, 80), (6, 100), (7, 120);

CREATE TABLE Challenges (challenge_id INTEGER, hacker_id INTEGER, difficulty_level INTEGER);
INSERT INTO Challenges VALUES (4810, 77726, 4), (21089, 27205, 1), (36566, 5580, 7), (66730, 52243, 6), (71055, 52243, 2);

CREATE TABLE Submissions (submission_id INTEGER, hacker_id INTEGER, challenge_id INTEGER, score INTEGER);
INSERT INTO Submissions VALUES
    (68628, 77726, 36566, 30), (65300, 77726, 21089, 10), (40326, 52243, 36566, 77), (8941, 27205, 4810, 4),
    (83554, 77726, 66730, 30), (43353, 52243, 66730, 0),  (55385, 52348, 71055, 20), (39784, 27205, 71055, 23),
    (94613, 86870, 71055, 30), (45788, 52348, 36566, 0),  (93058, 86870, 36566, 30), (7344, 8439, 66730, 92),
    (2721, 8439, 4810, 36),    (523, 5580, 71055, 4),     (49105, 52348, 66730, 0),  (55877, 57645, 66730, 80),
    (38355, 27205, 66730, 35), (3924, 8439, 36566, 80),   (97397, 90411, 66730, 100), (84162, 83082, 4810, 40),
    (97431, 90411, 71055, 30);""",
   """SELECT h.hacker_id, h.name
FROM Submissions s
JOIN Challenges c ON s.challenge_id = c.challenge_id
JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
JOIN Hackers h    ON s.hacker_id = h.hacker_id
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(DISTINCT s.challenge_id) > 1
ORDER BY COUNT(DISTINCT s.challenge_id) DESC, h.hacker_id;""",
   ["Chain the joins: submission → its challenge → that challenge's difficulty (max score) → the hacker.",
    "`WHERE s.score = d.score` keeps only full-score submissions.",
    "`HAVING` filters groups (after counting): more than one full-score challenge."],
   expected=["90411 Joe"], sample="official")
ex("harry-potter-and-wands", "CREATE TABLE Wands (id INTEGER, code INTEGER, coins_needed INTEGER, power INTEGER);\nINSERT INTO Wands VALUES\n" + sql_values(OL_W) + "\n\nCREATE TABLE Wands_Property (code INTEGER, age INTEGER, is_evil INTEGER);\nINSERT INTO Wands_Property VALUES\n" + sql_values(OL_P),
   """SELECT w.id, p.age, w.coins_needed, w.power
FROM Wands w
JOIN Wands_Property p ON w.code = p.code
WHERE p.is_evil = 0
  AND w.coins_needed = (
        SELECT MIN(w2.coins_needed)
        FROM Wands w2
        JOIN Wands_Property p2 ON w2.code = p2.code
        WHERE p2.age = p.age
          AND w2.power = w.power
      )
ORDER BY w.power DESC, p.age DESC;""",
   ["Join each wand to its property row to get `age` and `is_evil`.",
    "For every (age, power) combination keep only the cheapest wand: the subquery finds that minimum for the current row's age and power.",
    "Exclude evil wands; sort by power, then age, both descending."],
   expected=["9 45 1647 10", "12 17 9897 10", "1 20 3688 8", "15 40 6018 7", "19 20 7651 6", "11 40 7587 5",
             "10 20 504 5", "18 40 3312 3", "20 17 5689 3", "5 45 6020 2", "14 40 5408 1"], sample="official")
ex("challenges", "-- Sample Input 0 (Sample Input 1 is loaded further down)\nCREATE TABLE Hackers (hacker_id INTEGER, name TEXT);\nINSERT INTO Hackers VALUES\n" + sql_values(CH0_H) + "\n\nCREATE TABLE Challenges (challenge_id INTEGER, hacker_id INTEGER);\nINSERT INTO Challenges VALUES\n" + sql_values(CH0_C),
   """SELECT h.hacker_id, h.name, COUNT(c.challenge_id) AS total
FROM Hackers h
JOIN Challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total = (SELECT MAX(cnt)
                FROM (SELECT COUNT(*) AS cnt FROM Challenges GROUP BY hacker_id) m)
    OR total IN (SELECT cnt
                 FROM (SELECT COUNT(*) AS cnt FROM Challenges GROUP BY hacker_id) u
                 GROUP BY cnt
                 HAVING COUNT(*) = 1)
ORDER BY total DESC, h.hacker_id;""",
   ["Count challenges per hacker.",
    "Keep a hacker if their count is the **maximum** (ties allowed), **or** if no other hacker has the same count.",
    "`(SELECT COUNT(*) ... GROUP BY hacker_id)` is the list of all counts; grouping that list by count and `HAVING COUNT(*) = 1` gives counts used by exactly one hacker."],
   expected=["21283 Angela 6", "88255 Patrick 5", "96196 Lisa 1", "12299 Rose 6", "34856 Angela 6", "79345 Frank 4", "80491 Patrick 3", "81041 Lisa 1"],
   sample="official", second=("DELETE FROM Hackers;\nDELETE FROM Challenges;\nINSERT INTO Hackers VALUES\n" + sql_values(CH1_H) +
                              "\nINSERT INTO Challenges VALUES\n" + sql_values(CH1_C)))
ex("contest-leaderboard", "CREATE TABLE Hackers (hacker_id INTEGER, name TEXT);\nINSERT INTO Hackers VALUES\n" + sql_values(CL_H) + "\n\nCREATE TABLE Submissions (submission_id INTEGER, hacker_id INTEGER, challenge_id INTEGER, score INTEGER);\nINSERT INTO Submissions VALUES\n" + sql_values(CL_S),
   """SELECT h.hacker_id, h.name, SUM(m.max_score) AS total_score
FROM Hackers h
JOIN (
    SELECT hacker_id, challenge_id, MAX(score) AS max_score
    FROM Submissions
    GROUP BY hacker_id, challenge_id
) m ON h.hacker_id = m.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total_score > 0
ORDER BY total_score DESC, h.hacker_id;""",
   ["Step 1 (subquery): best score per hacker per challenge, so retries don't count twice.",
    "Step 2: sum those best scores per hacker.", "`HAVING total_score > 0` removes hackers whose total is 0."],
   expected=["4071 Rose 191", "74842 Lisa 174", "84072 Bonnie 100", "4806 Angela 89", "26071 Frank 85",
             "80305 Kimberly 67", "49438 Patrick 43"], sample="official")

# ============================================================================ ADVANCED JOIN
ex("sql-projects",
   "CREATE TABLE Projects (Task_ID INTEGER, Start_Date TEXT, End_Date TEXT);\nINSERT INTO Projects VALUES\n"
   "    (1, '2015-10-01', '2015-10-02'), (2, '2015-10-02', '2015-10-03'), (3, '2015-10-03', '2015-10-04'),\n"
   "    (4, '2015-10-13', '2015-10-14'), (5, '2015-10-14', '2015-10-15'), (6, '2015-10-28', '2015-10-29'),\n"
   "    (7, '2015-10-30', '2015-10-31');",
   """SELECT s.Start_Date, MIN(e.End_Date) AS End_Date
FROM (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) s,
     (SELECT End_Date   FROM Projects WHERE End_Date   NOT IN (SELECT Start_Date FROM Projects)) e
WHERE s.Start_Date < e.End_Date
GROUP BY s.Start_Date
ORDER BY julianday(MIN(e.End_Date)) - julianday(s.Start_Date), s.Start_Date;""",
   ["A project **starts** on a Start_Date that is nobody's End_Date (no task right before it).",
    "A project **ends** on an End_Date that is nobody's Start_Date (no task right after it).",
    "Pair each start with the **first** end after it (`MIN`).",
    "Sort by length in days (`DATEDIFF` in MySQL, `julianday` difference in SQLite), then by start date."],
   hr="""SELECT s.Start_Date, MIN(e.End_Date)
FROM (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) s,
     (SELECT End_Date   FROM Projects WHERE End_Date   NOT IN (SELECT Start_Date FROM Projects)) e
WHERE s.Start_Date < e.End_Date
GROUP BY s.Start_Date
ORDER BY DATEDIFF(MIN(e.End_Date), s.Start_Date), s.Start_Date;""",
   expected=["2015-10-28 2015-10-29", "2015-10-30 2015-10-31", "2015-10-13 2015-10-15", "2015-10-01 2015-10-04"],
   sample="official", local_note="`DATEDIFF(a, b)` → `julianday(a) - julianday(b)`")
ex("placements",
   """CREATE TABLE Students (ID INTEGER, Name TEXT);
INSERT INTO Students VALUES (1, 'Ashley'), (2, 'Samantha'), (3, 'Julia'), (4, 'Scarlet');

CREATE TABLE Friends (ID INTEGER, Friend_ID INTEGER);
INSERT INTO Friends VALUES (1, 2), (2, 3), (3, 4), (4, 1);

CREATE TABLE Packages (ID INTEGER, Salary REAL);
INSERT INTO Packages VALUES (1, 15.20), (2, 10.06), (3, 11.55), (4, 12.12);""",
   """SELECT s.Name
FROM Students s
JOIN Friends  f  ON s.ID = f.ID
JOIN Packages me ON s.ID = me.ID
JOIN Packages fr ON f.Friend_ID = fr.ID
WHERE fr.Salary > me.Salary
ORDER BY fr.Salary;""",
   ["Join **Packages twice** with different aliases: `me` = the student's salary, `fr` = the best friend's salary.",
    "Keep students whose friend earns more; sort by the friend's salary."],
   expected=["Samantha", "Julia", "Scarlet"], sample="official")
ex("symmetric-pairs",
   "CREATE TABLE Functions (X INTEGER, Y INTEGER);\n"
   "INSERT INTO Functions VALUES (20, 20), (20, 20), (20, 21), (23, 22), (22, 23), (21, 20);",
   """SELECT f1.X, f1.Y
FROM Functions f1
JOIN Functions f2 ON f1.X = f2.Y AND f1.Y = f2.X
GROUP BY f1.X, f1.Y
HAVING f1.X < f1.Y OR COUNT(*) > 1
ORDER BY f1.X;""",
   ["Self-join: find a row whose (X, Y) is this row flipped.",
    "`X < Y` keeps one of each pair (20 21, not 21 20).",
    "When X = Y a row matches **itself**, so it only counts if that pair appears at least twice: `COUNT(*) > 1`."],
   expected=["20 20", "20 21", "22 23"], sample="official")
ex("interviews", "CREATE TABLE Contests (contest_id INTEGER, hacker_id INTEGER, name TEXT);\nINSERT INTO Contests VALUES\n" + sql_values(IV_CT) + "\n\nCREATE TABLE Colleges (college_id INTEGER, contest_id INTEGER);\nINSERT INTO Colleges VALUES\n" + sql_values(IV_CO) + "\n\nCREATE TABLE Challenges (challenge_id INTEGER, college_id INTEGER);\nINSERT INTO Challenges VALUES\n" + sql_values(IV_CH) + "\n\nCREATE TABLE View_Stats (challenge_id INTEGER, total_views INTEGER, total_unique_views INTEGER);\nINSERT INTO View_Stats VALUES\n" + sql_values(IV_V) + "\n\nCREATE TABLE Submission_Stats (challenge_id INTEGER, total_submissions INTEGER, total_accepted_submissions INTEGER);\nINSERT INTO Submission_Stats VALUES\n" + sql_values(IV_S),
   """SELECT c.contest_id, c.hacker_id, c.name,
       SUM(COALESCE(s.ts, 0))  AS total_submissions,
       SUM(COALESCE(s.tas, 0)) AS total_accepted_submissions,
       SUM(COALESCE(v.tv, 0))  AS total_views,
       SUM(COALESCE(v.tuv, 0)) AS total_unique_views
FROM Contests c
JOIN Colleges   col ON c.contest_id = col.contest_id
JOIN Challenges ch  ON col.college_id = ch.college_id
LEFT JOIN (SELECT challenge_id, SUM(total_views) AS tv, SUM(total_unique_views) AS tuv
           FROM View_Stats GROUP BY challenge_id) v ON ch.challenge_id = v.challenge_id
LEFT JOIN (SELECT challenge_id, SUM(total_submissions) AS ts, SUM(total_accepted_submissions) AS tas
           FROM Submission_Stats GROUP BY challenge_id) s ON ch.challenge_id = s.challenge_id
GROUP BY c.contest_id, c.hacker_id, c.name
HAVING SUM(COALESCE(s.ts, 0)) + SUM(COALESCE(s.tas, 0)) + SUM(COALESCE(v.tv, 0)) + SUM(COALESCE(v.tuv, 0)) > 0
ORDER BY c.contest_id;""",
   ["Path: contest → colleges → challenges → stats.",
    "**Aggregate each stats table per challenge first** (the subqueries). Joining both raw stats tables directly would multiply rows and inflate the sums.",
    "`LEFT JOIN` + `COALESCE(..., 0)`: challenges without stats count as 0 instead of disappearing.",
    "`HAVING ... > 0` drops contests where all four sums are 0."],
   expected=["66406 17973 Rose 111 39 156 56", "66556 79153 Angela 0 0 11 10", "94828 80275 Frank 150 38 41 15"], sample="official")
FIFTEEN_SETUP = """-- The sample assumes the contest ended on March 06, 2016.
CREATE TABLE Hackers (hacker_id INTEGER, name TEXT);
INSERT INTO Hackers VALUES (15758, 'Rose'), (20703, 'Angela'), (36396, 'Frank'), (38289, 'Patrick'),
                           (44065, 'Lisa'), (53473, 'Kimberly'), (62529, 'Bonnie'), (79722, 'Michael');

CREATE TABLE Submissions (submission_date TEXT, submission_id INTEGER, hacker_id INTEGER, score INTEGER);
INSERT INTO Submissions VALUES
    ('2016-03-01', 8494, 20703, 0),  ('2016-03-01', 22403, 53473, 15), ('2016-03-01', 23965, 79722, 60), ('2016-03-01', 30173, 36396, 70),
    ('2016-03-02', 34928, 20703, 0), ('2016-03-02', 38740, 15758, 60), ('2016-03-02', 42769, 79722, 25), ('2016-03-02', 44364, 79722, 60),
    ('2016-03-03', 45440, 20703, 0), ('2016-03-03', 49050, 36396, 70), ('2016-03-03', 50273, 79722, 5),
    ('2016-03-04', 50344, 20703, 0), ('2016-03-04', 51360, 44065, 90), ('2016-03-04', 54404, 53473, 65), ('2016-03-04', 61533, 79722, 45),
    ('2016-03-04', 61534, 20703, 10),
    ('2016-03-05', 72852, 20703, 0), ('2016-03-05', 74546, 38289, 0),  ('2016-03-05', 76487, 62529, 0), ('2016-03-05', 82439, 36396, 10),
    ('2016-03-05', 90006, 36396, 40),
    ('2016-03-06', 90404, 20703, 0), ('2016-03-06', 90405, 38289, 5);"""
FIFTEEN = """SELECT d.submission_date,
       -- hackers who submitted every single day from 03-01 up to this date
       (SELECT COUNT(DISTINCT s2.hacker_id)
          FROM Submissions s2
         WHERE s2.submission_date = d.submission_date
           AND (SELECT COUNT(DISTINCT s3.submission_date)
                  FROM Submissions s3
                 WHERE s3.hacker_id = s2.hacker_id
                   AND s3.submission_date < d.submission_date) = {days}) AS streak_hackers,
       -- hacker with the most submissions that day (lowest id on ties)
       (SELECT s4.hacker_id
          FROM Submissions s4
         WHERE s4.submission_date = d.submission_date
         GROUP BY s4.hacker_id
         ORDER BY COUNT(*) DESC, s4.hacker_id
         LIMIT 1) AS top_hacker_id,
       (SELECT h.name
          FROM Hackers h
         WHERE h.hacker_id = (SELECT s5.hacker_id
                                FROM Submissions s5
                               WHERE s5.submission_date = d.submission_date
                               GROUP BY s5.hacker_id
                               ORDER BY COUNT(*) DESC, s5.hacker_id
                               LIMIT 1)) AS top_hacker_name
FROM (SELECT DISTINCT submission_date FROM Submissions) d
ORDER BY d.submission_date;"""
ex("15-days-of-learning-sql", "-- The sample assumes the contest ended on March 06, 2016.\nCREATE TABLE Hackers (hacker_id INTEGER, name TEXT);\nINSERT INTO Hackers VALUES\n" + sql_values(FD_H) + "\n\nCREATE TABLE Submissions (submission_date TEXT, submission_id INTEGER, hacker_id INTEGER, score INTEGER);\nINSERT INTO Submissions VALUES\n" + sql_values(FD_S),
   FIFTEEN.format(days="CAST(julianday(d.submission_date) - julianday('2016-03-01') AS INTEGER)"),
   ["One output row per contest day (`SELECT DISTINCT submission_date`).",
    "**Streak count:** a hacker is still in on day N if they submitted on all N−1 earlier days, i.e. their number of distinct earlier submission dates equals the days since March 1.",
    "**Top hacker:** group that day's submissions by hacker, most submissions first, lowest id on ties, `LIMIT 1`; the same subquery is reused to look up the name.",
    "Days since start: `DATEDIFF(date, '2016-03-01')` in MySQL, `julianday` difference in SQLite."],
   hr=FIFTEEN.format(days="DATEDIFF(d.submission_date, '2016-03-01')"),
   expected=["2016-03-01 4 20703 Angela", "2016-03-02 2 79722 Michael", "2016-03-03 2 20703 Angela",
             "2016-03-04 2 20703 Angela", "2016-03-05 1 36396 Frank", "2016-03-06 1 20703 Angela"], sample="official",
   local_note="`DATEDIFF(a, b)` → `CAST(julianday(a) - julianday(b) AS INTEGER)`")

# ============================================================================ ALTERNATIVE QUERIES
ex("draw-the-triangle-1", "-- No table needed.",
   """WITH RECURSIVE rows_(n) AS (
    SELECT 20
    UNION ALL
    SELECT n - 1 FROM rows_ WHERE n > 1
)
SELECT TRIM(REPLACE(HEX(ZEROBLOB(n)), '00', '* '))
FROM rows_;""",
   ["MySQL: a user variable `@n` starts at 21 and goes down by 1 on every row; `REPEAT('* ', n)` draws the row.",
    "`information_schema.tables` is just any table with at least 20 rows to loop over; `LIMIT 20` stops at 20 rows.",
    "SQLite has no `REPEAT`: a recursive CTE counts 20 → 1 and `HEX(ZEROBLOB(n))` makes n copies of `00`, replaced by `* `."],
   hr="SET @n := 21;\nSELECT REPEAT('* ', @n := @n - 1)\nFROM information_schema.tables\nLIMIT 20;",
   local_note="`REPEAT('* ', n)` + variables → recursive CTE + `REPLACE(HEX(ZEROBLOB(n)), '00', '* ')`")
ex("draw-the-triangle-2", "-- No table needed.",
   """WITH RECURSIVE rows_(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM rows_ WHERE n < 20
)
SELECT TRIM(REPLACE(HEX(ZEROBLOB(n)), '00', '* '))
FROM rows_;""",
   ["Same as Draw The Triangle 1, counting **up** from 1 to 20 instead of down."],
   hr="SET @n := 0;\nSELECT REPEAT('* ', @n := @n + 1)\nFROM information_schema.tables\nLIMIT 20;",
   local_note="`REPEAT('* ', n)` + variables → recursive CTE + `REPLACE(HEX(ZEROBLOB(n)), '00', '* ')`")
PRIMES = """WITH RECURSIVE nums AS (
    SELECT 2 AS n
    UNION ALL
    SELECT n + 1 FROM nums WHERE n < 1000
)
SELECT {concat}
FROM nums
WHERE NOT EXISTS (
    SELECT 1
    FROM nums d
    WHERE d.n * d.n <= nums.n      -- only divisors up to the square root
      AND nums.n % d.n = 0         -- d divides n -> not prime
);"""
ex("print-prime-numbers", "-- No table needed.",
   PRIMES.format(concat="GROUP_CONCAT(n, '&')"),
   ["A recursive CTE generates the numbers 2..1000.",
    "`NOT EXISTS`: keep n if no number d with d² ≤ n divides it evenly (`%` = remainder).",
    "`GROUP_CONCAT(... SEPARATOR '&')` joins them on one line (SQLite: `GROUP_CONCAT(n, '&')`).",
    "`WITH RECURSIVE` needs MySQL 8 (HackerRank's MySQL)."],
   hr=PRIMES.format(concat="GROUP_CONCAT(n ORDER BY n SEPARATOR '&')"),
   local_note="`GROUP_CONCAT(n ORDER BY n SEPARATOR '&')` → `GROUP_CONCAT(n, '&')`")

# ----------------------------------------------------------------------------- rendering
_UNUSED_GAPPY = {"weather-observation-station-5", "more-than-75-marks", "salary-of-employees", "what-type-of-triangle",
                     "the-blunder", "earnings-of-employees", "full-score", "harry-potter-and-wands", "contest-leaderboard",
                     "interviews", "15-days-of-learning-sql"}
SAMPLE_NOTE = {
    "official": "the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Sample Output above.",
    "rebuilt": "rebuilt to reproduce HackerRank's Sample Output (the sample tables are images on HackerRank).",
    "made-up": "made up for local practice (HackerRank shows no sample data for this challenge, so your results will differ from HackerRank's hidden data).",
}

IMG_RE = re.compile(r'!\[[^\]]*\]\((https://s3\.amazonaws\.com/hr-challenge-images/[^)\s]+)\)|<img[^>]*src="(https://s3\.amazonaws\.com/hr-challenge-images/[^"]+)"[^>]*/?>')

def transcribe(m):
    url = m.group(1) or m.group(2)
    key = url.split("hr-challenge-images/", 1)[1]
    if key not in IMG:
        raise KeyError("no transcription for image " + key)
    return "\n\n" + IMG[key] + "\n\n"

def clean_statement(slug, s):
    s = s.replace("\r", "")
    if slug in EXPLAIN:
        m = re.search(r"\n_*\**Explanation\**_*\s*\n", s)
        s = (s[:m.start()] if m else s) + "\n\n**Explanation**\n\n" + EXPLAIN[slug] + \
            "\n\n> Numbers that appear as formulas on HackerRank are filled in here."
    s = IMG_RE.sub(transcribe, s)
    s = re.sub(r"[ \t]+\n", "\n", s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()

def comment_block(lines):
    return "\n".join("-- " + l for l in lines)

def strip_md(t):
    return t.replace("`", "").replace("**", "")

def render(e):
    c = CH[e["slug"]]
    name, diff, sec = c["name"], c["difficulty"], c["subdomain"]
    d = os.path.join(OUT, SECTION_DIR[sec], folder(name))
    os.makedirs(d, exist_ok=True)
    same = e["hr"] == e["local"]
    readme = [f"# {name}", "",
              f"**Difficulty:** {diff} · **Section:** {sec} · **Track:** HackerRank SQL · [Open on HackerRank]({c['url']})", "",
              "---", "", clean_statement(e["slug"], c["statement"]), "", "## Solution", "",
              "```sql", e["hr"], "```", ""]
    readme += [f"- {n}" for n in e["notes"]]
    if not same:
        readme += ["", f"**Local SQLite version** ([solution.sql](solution.sql)) differs only where SQLite lacks a MySQL function: {e['local_note']}."]
    readme += ["", f"**Sample data in solution.sql:** {SAMPLE_NOTE[e['sample']]}", "",
               "Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) "
               "(paste into HackerRank and **choose MySQL** in the language menu)", ""]
    open(os.path.join(d, "README.md"), "w").write("\n".join(readme))

    tables = re.findall(r"CREATE TABLE (\w+)", e["setup"])
    drops = "".join(f"DROP TABLE IF EXISTS {t};\n" for t in tables)
    exp = ("Expected (HackerRank sample): " + " / ".join(e["expected"])) if e["expected"] else None
    sql = [f"-- {name}  ({diff} · {sec})  {c['url']}",
           "-- Description: README.md (same folder).", "--",
           "-- RUNNABLE LOCAL VERSION (SQLite): builds sample tables, then runs the query.",
           "-- Run: Terminal -> Run Task -> \"Run SQL file (SQLite)\"  (fresh in-memory DB every time)",
           "-- HackerRank copy (MySQL): solution_hackerrank.sql" + ("" if same else "  (differs: " + strip_md(e["local_note"]) + ")"),
           "", "-- " + "-" * 75,
           "-- SETUP: sample data " + {"official": "(official HackerRank sample)", "rebuilt": "(rebuilt from HackerRank's sample output)", "made-up": "(made up: HackerRank shows no sample for this one)"}[e["sample"]],
           "-- " + "-" * 75, drops + e["setup"], "", "-- " + "-" * 75, "-- QUERY"]
    if exp:
        sql.append("-- " + exp)
    sql += ["-- " + "-" * 75, comment_block([strip_md(n) for n in e["notes"]]), e["local"], ""]
    if e.get("second"):
        sql += ["-- " + "-" * 75, "-- SAMPLE INPUT 1: replace the data and run the same query again", "-- " + "-" * 75,
                e["second"], "", e["local"], ""]
    open(os.path.join(d, "solution.sql"), "w").write("\n".join(sql))
    open(os.path.join(d, "solution_hackerrank.sql"), "w").write(
        "-- HackerRank submission copy: paste as-is and pick MySQL in the language menu (it opens on DB2).\n"
        f"-- {name} ({diff} · {sec}). Explained version: solution.sql\n" + e["hr"] + "\n")
    return d

def run_sql(path):
    con, buf, out = sqlite3.connect(":memory:"), "", []
    for line in open(path):
        buf += line
        if sqlite3.complete_statement(buf):
            cur = con.execute(buf); buf = ""
            if cur.description:
                out += [" ".join("NULL" if v is None else str(v) for v in r) for r in cur]
    return out

results = []
for e in EX:
    d = render(e)
    try:
        got = run_sql(os.path.join(d, "solution.sql"))
        ok = (got == e["expected"]) if e["expected"] else bool(got)
        if e["slug"] == "print-prime-numbers":
            ok = got[0].startswith("2&3&5&7&11") and got[0].endswith("&997") and len(got[0].split("&")) == 168
        if e["slug"].startswith("draw-the-triangle"):
            ok = len(got) == 20 and {len(r.split()) for r in got} == set(range(1, 21))
        results.append((e["slug"], "PASS" if ok else "FAIL", got[:3] if not ok else ""))
    except Exception as x:
        results.append((e["slug"], "ERROR", str(x)))

for r in results:
    print(*r)
print(f"{sum(r[1] == 'PASS' for r in results)}/{len(results)} pass; with official/rebuilt sample check:",
      sum(1 for e in EX if e['expected']))
missing = set(CH) - {e["slug"] for e in EX} - set(EXISTING)
print("not generated:", sorted(missing))

# index README for Code/sql
order = list(SECTION_DIR)
idx = ["# SQL Coding Practice", "",
       "All 58 challenges of the [HackerRank SQL track](https://www.hackerrank.com/domains/sql), grouped by HackerRank section,",
       "with the same name and difficulty as on HackerRank.", "",
       "Each exercise folder has:", "",
       "- `README.md`: the problem (from HackerRank) and how the solution works.",
       "- `solution.sql`: the runnable, commented version. It creates sample tables first, then runs the query.",
       "  Written for **SQLite** (built into macOS), so there's nothing to install.",
       "- `solution_hackerrank.sql`: the copy to paste into HackerRank (**MySQL**; pick MySQL in the language menu, it opens on DB2).", "",
       "## Running", "",
       "Open the `interviews` folder (or this `sql` folder) in VS Code, open a `solution.sql`, then",
       "**Terminal → Run Task → Run SQL file (SQLite)**. It runs on a fresh in-memory database every time.", "",
       "From the terminal: `sqlite3 -header -column :memory: < basic-select/select-all/solution.sql`", "",
       "## SQLite vs MySQL", "",
       "HackerRank uses MySQL; the local files use SQLite. Most SQL is identical. Where it isn't, the README of that exercise says so:", "",
       "| MySQL (HackerRank) | SQLite (local) | Meaning |", "|---|---|---|",
       "| `CONCAT(a, b, c)` | `a \\|\\| b \\|\\| c` | join strings |",
       "| `LEFT(s, 1)` | `SUBSTR(s, 1, 1)` | first character |",
       "| `FLOOR(x)` / `CEIL(x)` | `CAST(x AS INTEGER)` (+1 if decimals for CEIL) | round down / up |",
       "| `TRUNCATE(x, 4)` | `CAST(x * 10000 AS INTEGER) / 10000.0` | cut to 4 decimals |",
       "| `DATEDIFF(a, b)` | `julianday(a) - julianday(b)` | days between dates |",
       "| `REPEAT(s, n)` | `REPLACE(HEX(ZEROBLOB(n)), '00', s)` | repeat a string |", ""]
counts = {}
for sec in order:
    rows = sorted([c for c in CH.values() if c["subdomain"] == sec], key=lambda c: list(CH).index(c["slug"]))
    counts[sec] = len(rows)
    idx += [f"## {sec} ({len(rows)})", "", "| # | Challenge | Difficulty | Files |", "|---|---|---|---|"]
    for i, c in enumerate(rows, 1):
        f = f"{SECTION_DIR[sec]}/{EXISTING.get(c['slug'], folder(c['name']))}"
        idx.append(f"| {i} | [{c['name']}]({f}/) | {c['difficulty']} | [README]({f}/README.md) · [solution.sql]({f}/solution.sql) · "
                   f"[HackerRank copy]({f}/solution_hackerrank.sql) |")
    idx.append("")
idx += ["---", "", "How this was built (and how to do the same for another tech): [HACKERRANK-IMPORT.md](../HACKERRANK-IMPORT.md) · generator: [_tools/gen.py](_tools/gen.py)", "",
        "**Back to:** [All Topics](../../Overview/All-Topics.md) · [Java exercises](../java/)", ""]
open(os.path.join(OUT, "README.md"), "w").write("\n".join(idx))
print(counts)
