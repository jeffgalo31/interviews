# Challenges

**Difficulty:** Medium · **Section:** Basic Join · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/challenges/problem)

---

Julia asked her students to create some coding challenges. 
Write a query to print the _hacker\_id_, _name_, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by _hacker\_id_. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.

**Input Format**

The following tables contain challenge data:

- _Hackers:_ The _hacker\_id_ is the id of the hacker, and _name_ is the name of the hacker. <img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521004-cb4c077dd3-ScreenShot2016-03-21at6.06.54AM.png"/>

- _Challenges:_ The _challenge\_id_ is the id of the challenge, and _hacker\_id_ is the id of the student who created the challenge. <img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521079-549341d9ec-ScreenShot2016-03-21at6.07.03AM.png"/>

----

**Sample Input 0**		

_Hackers_ Table: <img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521384-34c6866dae-ScreenShot2016-03-21at6.07.15AM.png"/>
_Challenges_ Table: <img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521410-befa8e1cd9-ScreenShot2016-03-21at6.07.25AM.png"/>

**Sample Output 0**		

	21283 Angela 6
	88255 Patrick 5
	96196 Lisa 1

**Sample Input 1**

_Hackers_ Table: <img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521469-87036deea3-ScreenShot2016-03-21at6.07.48AM.png"/>
_Challenges_ Table: <img src="https://s3.amazonaws.com/hr-challenge-images/19506/1458521490-358215cf0b-ScreenShot2016-03-21at6.07.58AM.png"/>

**Sample Output 1**

	12299 Rose 6
	34856 Angela 6
	79345 Frank 4
	80491 Patrick 3
	81041 Lisa 1

## Solution

```sql
SELECT h.hacker_id, h.name, COUNT(c.challenge_id) AS total
FROM Hackers h
JOIN Challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total = (SELECT MAX(cnt)
                FROM (SELECT COUNT(*) AS cnt FROM Challenges GROUP BY hacker_id) m)
    OR total IN (SELECT cnt
                 FROM (SELECT COUNT(*) AS cnt FROM Challenges GROUP BY hacker_id) u
                 GROUP BY cnt
                 HAVING COUNT(*) = 1)
ORDER BY total DESC, h.hacker_id;
```

- Count challenges per hacker.
- Keep a hacker if their count is the **maximum** (ties allowed), **or** if no other hacker has the same count.
- `(SELECT COUNT(*) ... GROUP BY hacker_id)` is the list of all counts; grouping that list by count and `HAVING COUNT(*) = 1` gives counts used by exactly one hacker.

**Sample data in solution.sql:** rebuilt to reproduce HackerRank's Sample Output (the sample tables are images on HackerRank).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
