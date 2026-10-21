<!-- study-layout -->
# Challenges

🟡 **Medium** · 📁 **Basic Join** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/challenges/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Examples](#-examples) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Julia asked her students to create some coding challenges.
Write a query to print the _hacker\_id_, _name_, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by _hacker\_id_. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.

## 📥 Input & output

### Input format

The following tables contain challenge data:

- _Hackers:_ The _hacker\_id_ is the id of the hacker, and _name_ is the name of the hacker.

| Column | Type |
|---|---|
| hacker_id | Integer |
| name | String |

- _Challenges:_ The _challenge\_id_ is the id of the challenge, and _hacker\_id_ is the id of the student who created the challenge.

| Column | Type |
|---|---|
| challenge_id | Integer |
| hacker_id | Integer |

----

## 🧪 Examples

### Example 1

**Input**

_Hackers_ Table:

| hacker_id | name |
|---|---|
| 5077 | Rose |
| 21283 | Angela |
| 62743 | Frank |
| 88255 | Patrick |
| 96196 | Lisa |

_Challenges_ Table:

| challenge_id | hacker_id |
|---|---|
| 61654 | 5077 |
| 58302 | 21283 |
| 40587 | 88255 |
| 29477 | 5077 |
| 1220 | 21283 |
| 69514 | 21283 |
| 46561 | 62743 |
| 58077 | 62743 |
| 18483 | 88255 |
| 76766 | 21283 |
| 52382 | 5077 |
| 74467 | 21283 |
| 33625 | 96196 |
| 26053 | 88255 |
| 42665 | 62743 |
| 12859 | 62743 |
| 70094 | 21283 |
| 34599 | 88255 |
| 54680 | 88255 |
| 61881 | 5077 |

**Output**

	21283 Angela 6
	88255 Patrick 5
	96196 Lisa 1

### Example 2

**Input**

_Hackers_ Table:

| hacker_id | name |
|---|---|
| 12299 | Rose |
| 34856 | Angela |
| 79345 | Frank |
| 80491 | Patrick |
| 81041 | Lisa |

_Challenges_ Table:

| challenge_id | hacker_id |
|---|---|
| 63963 | 81041 |
| 63117 | 79345 |
| 28225 | 34856 |
| 21989 | 12299 |
| 4653 | 12299 |
| 70070 | 79345 |
| 36905 | 34856 |
| 61136 | 80491 |
| 17234 | 12299 |
| 80308 | 79345 |
| 40510 | 34856 |
| 79820 | 80491 |
| 22720 | 12299 |
| 21394 | 12299 |
| 36261 | 34856 |
| 15334 | 12299 |
| 71435 | 79345 |
| 23157 | 34856 |
| 54102 | 34856 |
| 69065 | 80491 |

**Output**

	12299 Rose 6
	34856 Angela 6
	79345 Frank 4
	80491 Patrick 3
	81041 Lisa 1

## 💡 Solution

> [!TIP]
> **Key idea:** Count challenges per hacker.

### ✍️ The query

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

### 🔍 How it works

- Keep a hacker if their count is the **maximum** (ties allowed), **or** if no other hacker has the same count.
- `(SELECT COUNT(*) ... GROUP BY hacker_id)` is the list of all counts; grouping that list by count and `HAVING COUNT(*) = 1` gives counts used by exactly one hacker.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [Ollivander's Inventory](../ollivanders-inventory/README.md) · [🗄️ All SQL exercises](../../README.md) · [Contest Leaderboard](../contest-leaderboard/README.md) ➡️
