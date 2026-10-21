# Placements

**Difficulty:** Medium · **Section:** Advanced Join · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/placements/problem)

---

You are given three&nbsp;tables:&nbsp;<em>Students</em>,<em> Friends </em>and<em> Packages.</em>&nbsp;<em>Students</em> contains two columns: <em>ID</em>&nbsp;and <em>Name</em>. <em>Friends</em> contains two columns: <em>ID</em> and <em>Friend_ID</em> (<em>ID</em> of the ONLY best friend). <em>Packages</em>&nbsp;contains two columns: <em>ID</em> and <em>Salary</em> (offered salary in $&nbsp;thousands&nbsp;per month).

*Students*

| Column | Type |
|---|---|
| ID | Integer |
| Name | String |

*Friends*

| Column | Type |
|---|---|
| ID | Integer |
| Friend_ID | Integer |

*Packages*

| Column | Type |
|---|---|
| ID | Integer |
| Salary | Float |

Write a query to output the names of those students whose&nbsp;best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.

__Sample Input__

*Students*

| ID | Name |
|---|---|
| 1 | Ashley |
| 2 | Samantha |
| 3 | Julia |
| 4 | Scarlet |

*Friends*

| ID | Friend_ID |
|---|---|
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 1 |

*Packages*

| ID | Salary |
|---|---|
| 1 | 15.20 |
| 2 | 10.06 |
| 3 | 11.55 |
| 4 | 12.12 |

__Sample Output__

    Samantha
    Julia
    Scarlet

<br>
__Explanation__

See the following table:

| ID | Name | Salary | Friend ID | Friend Salary |
|---|---|---|---|---|
| 1 | Ashley | 15.20 | 2 | 10.06 |
| 2 | Samantha | 10.06 | 3 | 11.55 |
| 3 | Julia | 11.55 | 4 | 12.12 |
| 4 | Scarlet | 12.12 | 1 | 15.20 |

Now,

<ul>
	<li><em>Samantha&#39;s</em> best friend got offered a higher salary than her at 11.55</li>
	<li><em>Julia&#39;s</em> best friend got offered a higher salary than her at 12.12</li>
	<li><em>Scarlet&#39;s</em> best friend got offered a higher salary than her at 15.2</li>
    <li><em>Ashley&#39;s</em> best friend did NOT get offered a higher salary than her</li>
</ul>

The name output, when ordered by the salary offered to their friends, will be:

<ul>
	<li><em>Samantha</em></li>
	<li><em>Julia</em></li>
	<li><em>Scarlet</em></li>
</ul>

## Solution

```sql
SELECT s.Name
FROM Students s
JOIN Friends  f  ON s.ID = f.ID
JOIN Packages me ON s.ID = me.ID
JOIN Packages fr ON f.Friend_ID = fr.ID
WHERE fr.Salary > me.Salary
ORDER BY fr.Salary;
```

- Join **Packages twice** with different aliases: `me` = the student's salary, `fr` = the best friend's salary.
- Keep students whose friend earns more; sort by the friend's salary.

**Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Sample Output above.

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
