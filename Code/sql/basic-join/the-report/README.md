# The Report

**Difficulty:** Medium · **Section:** Basic Join · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/the-report/problem)

---

You are given two tables:&nbsp;<em>Students</em>&nbsp;and <em>Grades</em>.&nbsp;<em>Students</em>&nbsp;contains three columns <em>ID</em>, <em>Name</em> and <em>Marks</em>.

| Column | Type |
|---|---|
| ID | Integer |
| Name | String |
| Marks | Integer |

<em>Grades</em> contains the following data:

| Grade | Min_Mark | Max_Mark |
|---|---|---|
| 1 | 0 | 9 |
| 2 | 10 | 19 |
| 3 | 20 | 29 |
| 4 | 30 | 39 |
| 5 | 40 | 49 |
| 6 | 50 | 59 |
| 7 | 60 | 69 |
| 8 | 70 | 79 |
| 9 | 80 | 89 |
| 10 | 90 | 100 |

<em>Ketty</em> gives <em>Eve</em> a task to generate a report containing three columns: <em>Name</em>, <em>Grade</em> and <em>Mark</em>. <em>Ketty</em> doesn't want the NAMES of those students who received a grade lower than <em>8</em>. The report must be in descending order by grade -- i.e.  higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

Write a query to help Eve.

__Sample Input__

| ID | Name | Marks |
|---|---|---|
| 1 | Julia | 88 |
| 2 | Samantha | 68 |
| 3 | Maria | 99 |
| 4 | Scarlet | 78 |
| 5 | Ashley | 63 |
| 6 | Jane | 81 |

__Sample Output__

    Maria 10 99
    Jane 9 81
    Julia 9 88
    Scarlet 8 78
    NULL 7 63
    NULL 7 68

<br>
__Note__

Print &quot;NULL&quot;&nbsp; as the name if the grade is less than 8.

__Explanation__

Consider the following table with the grades assigned to the students:

| ID | Name | Marks | Grade |
|---|---|---|---|
| 1 | Julia | 88 | 9 |
| 2 | Samantha | 68 | 7 |
| 3 | Maria | 99 | 10 |
| 4 | Scarlet | 78 | 8 |
| 5 | Ashley | 63 | 7 |
| 6 | Jane | 81 | 9 |

So, the following students got <em>8</em>, <em>9</em> or <em>10</em> grades:

<ul>
	<li><em>Maria (grade 10)</em></li>
	<li><em>Jane (grade 9)</em></li>
	<li><em>Julia (grade 9)</em></li>
	<li><em>Scarlet (grade 8)</em></li>
</ul>

## Solution

```sql
SELECT CASE WHEN g.Grade >= 8 THEN s.Name ELSE NULL END AS Name,
       g.Grade,
       s.Marks
FROM Students s
JOIN Grades g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY g.Grade DESC,
         CASE WHEN g.Grade >= 8 THEN s.Name END,
         s.Marks;
```

- The join is a **range**: each mark matches the grade row whose `Min_Mark`..`Max_Mark` contains it.
- `CASE` hides names below grade 8 (prints NULL).
- Sort: grade high → low; then name (only for grades 8-10, NULL for the rest); then marks ascending, which orders the NULL rows.

**Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
