<!-- study-layout -->
# Contest Leaderboard

🟡 **Medium** · 📁 **Basic Join** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/contest-leaderboard/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too!

The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the _hacker\_id_, _name_, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending _hacker\_id_. Exclude all hackers with a total score of $0$ from your result.

## 📥 Input & output

### Input format

The following tables contain contest data:

- _Hackers:_ The _hacker\_id_ is the id of the hacker, and _name_ is the name of the hacker.

| Column | Type |
|---|---|
| hacker_id | Integer |
| name | String |

- _Submissions:_ The _submission\_id_ is the id of the submission, _hacker\_id_ is the id of the hacker who made the submission, _challenge\_id_ is the id of the challenge for which the submission belongs to, and _score_ is the score of the submission.

| Column | Type |
|---|---|
| submission_id | Integer |
| hacker_id | Integer |
| challenge_id | Integer |
| score | Integer |

## 🧪 Example

**Input**

Hackers Table:

| hacker_id | name |
|---|---|
| 4071 | Rose |
| 4806 | Angela |
| 26071 | Frank |
| 49438 | Patrick |
| 74842 | Lisa |
| 80305 | Kimberly |
| 84072 | Bonnie |
| 87868 | Michael |
| 92118 | Todd |
| 95895 | Joe |

Submissions Table:

| submission_id | hacker_id | challenge_id | score |
|---|---|---|---|
| 67194 | 74842 | 63132 | 76 |
| 64479 | 74842 | 19797 | 98 |
| 40742 | 26071 | 49593 | 20 |
| 17513 | 4806 | 49593 | 32 |
| 69846 | 80305 | 19797 | 19 |
| 41002 | 26071 | 89343 | 36 |
| 52826 | 49438 | 49593 | 9 |
| 31093 | 26071 | 19797 | 2 |
| 81614 | 84072 | 49593 | 100 |
| 44829 | 26071 | 89343 | 17 |
| 75147 | 80305 | 49593 | 48 |
| 14115 | 4806 | 49593 | 76 |
| 6943 | 4071 | 19797 | 95 |
| 12855 | 4806 | 25917 | 13 |
| 73343 | 80305 | 49593 | 42 |
| 84264 | 84072 | 63132 | 0 |
| 9951 | 4071 | 49593 | 43 |
| 45104 | 49438 | 25917 | 34 |
| 53795 | 74842 | 19797 | 5 |
| 26363 | 26071 | 19797 | 29 |
| 10063 | 4071 | 49593 | 96 |

**Output**

```
4071 Rose 191
74842 Lisa 174
84072 Bonnie 100
4806 Angela 89
26071 Frank 85
80305 Kimberly 67
49438 Patrick 43
```

**Why**

Hacker 4071 submitted solutions for challenges 19797 and 49593, so the total score = 95 + max(43, 96) = 191.

Hacker 74842 submitted solutions for challenges 19797 and 63132, so the total score = max(98, 5) + 76 = 174.

Hacker 84072 submitted solutions for challenges 49593 and 63132, so the total score = 100 + 0 = 100.

The total scores for hackers 4806, 26071, 80305, and 49438 can be similarly calculated.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** Step 1 (subquery): best score per hacker per challenge, so retries don't count twice.

### ✍️ The query

```sql
SELECT h.hacker_id, h.name, SUM(m.max_score) AS total_score
FROM Hackers h
JOIN (
    SELECT hacker_id, challenge_id, MAX(score) AS max_score
    FROM Submissions
    GROUP BY hacker_id, challenge_id
) m ON h.hacker_id = m.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total_score > 0
ORDER BY total_score DESC, h.hacker_id;
```

### 🔍 How it works

- Step 2: sum those best scores per hacker.
- `HAVING total_score > 0` removes hackers whose total is 0.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [Challenges](../challenges/README.md) · [🗄️ All SQL exercises](../../README.md) · [SQL Project Planning](../../advanced-join/sql-project-planning/README.md) ➡️
