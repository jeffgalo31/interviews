<!-- study-layout -->
# Top Competitors

🟡 **Medium** · 📁 **Basic Join** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/full-score/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective _hacker\_id_ and _name_ of hackers who achieved full scores for *more than one* challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending _hacker\_id_.

----

## 📥 Input & output

### Input format

The following tables contain contest data:

- _Hackers:_ The _hacker\_id_ is the id of the hacker, and _name_ is the name of the hacker.

| Column | Type |
|---|---|
| hacker_id | Integer |
| name | String |

- _Difficulty:_ The _difficult\_level_ is the level of difficulty of the challenge,  and _score_ is the maximum score that can be achieved for a challenge at that difficulty level.

| Column | Type |
|---|---|
| difficulty_level | Integer |
| score | Integer |

- _Challenges:_ The _challenge\_id_ is the id of the challenge, the _hacker\_id_ is the id of the hacker who created the challenge, and _difficulty\_level_ is the level of difficulty of the challenge.

| Column | Type |
|---|---|
| challenge_id | Integer |
| hacker_id | Integer |
| difficulty_level | Integer |

- _Submissions:_ The _submission\_id_ is the id of the submission, _hacker\_id_ is the id of the hacker who made the submission, _challenge\_id_ is the id of the challenge that the submission belongs to, and _score_ is the score of the submission.

| Column | Type |
|---|---|
| submission_id | Integer |
| hacker_id | Integer |
| challenge_id | Integer |
| score | Integer |

----

## 🧪 Example

**Input**

Hackers Table:

| hacker_id | name |
|---|---|
| 5580 | Rose |
| 8439 | Angela |
| 27205 | Frank |
| 52243 | Patrick |
| 52348 | Lisa |
| 57645 | Kimberly |
| 77726 | Bonnie |
| 83082 | Michael |
| 86870 | Todd |
| 90411 | Joe |

 Difficulty Table:

| difficulty_level | score |
|---|---|
| 1 | 20 |
| 2 | 30 |
| 3 | 40 |
| 4 | 60 |
| 5 | 80 |
| 6 | 100 |
| 7 | 120 |

 Challenges Table:

| challenge_id | hacker_id | difficulty_level |
|---|---|---|
| 4810 | 77726 | 4 |
| 21089 | 27205 | 1 |
| 36566 | 5580 | 7 |
| 66730 | 52243 | 6 |
| 71055 | 52243 | 2 |

 Submissions Table:

| submission_id | hacker_id | challenge_id | score |
|---|---|---|---|
| 68628 | 77726 | 36566 | 30 |
| 65300 | 77726 | 21089 | 10 |
| 40326 | 52243 | 36566 | 77 |
| 8941 | 27205 | 4810 | 4 |
| 83554 | 77726 | 66730 | 30 |
| 43353 | 52243 | 66730 | 0 |
| 55385 | 52348 | 71055 | 20 |
| 39784 | 27205 | 71055 | 23 |
| 94613 | 86870 | 71055 | 30 |
| 45788 | 52348 | 36566 | 0 |
| 93058 | 86870 | 36566 | 30 |
| 7344 | 8439 | 66730 | 92 |
| 2721 | 8439 | 4810 | 36 |
| 523 | 5580 | 71055 | 4 |
| 49105 | 52348 | 66730 | 0 |
| 55877 | 57645 | 66730 | 80 |
| 38355 | 27205 | 66730 | 35 |
| 3924 | 8439 | 36566 | 80 |
| 97397 | 90411 | 66730 | 100 |
| 84162 | 83082 | 4810 | 40 |
| 97431 | 90411 | 71055 | 30 |

**Output**

```
90411 Joe
```

**Why**

Hacker 86870 got a score of 30 for challenge 71055 with a difficulty level of 2, so 86870 earned a full score for this challenge.

Hacker 90411 got a score of 30 for challenge 71055 with a difficulty level of 2, so 90411 earned a full score for this challenge.

Hacker 90411 got a score of 100 for challenge 66730 with a difficulty level of 6, so 90411 earned a full score for this challenge.

Only hacker 90411 managed to earn a full score for more than one challenge, so we print the their hacker_id and name as 2 space-separated values.

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** Chain the joins: submission → its challenge → that challenge's difficulty (max score) → the hacker.

### ✍️ The query

```sql
SELECT h.hacker_id, h.name
FROM Submissions s
JOIN Challenges c ON s.challenge_id = c.challenge_id
JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
JOIN Hackers h    ON s.hacker_id = h.hacker_id
WHERE s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(DISTINCT s.challenge_id) > 1
ORDER BY COUNT(DISTINCT s.challenge_id) DESC, h.hacker_id;
```

### 🔍 How it works

- `WHERE s.score = d.score` keeps only full-score submissions.
- `HAVING` filters groups (after counting): more than one full-score challenge.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [The Report](../the-report/README.md) · [🗄️ All SQL exercises](../../README.md) · [Ollivander's Inventory](../ollivanders-inventory/README.md) ➡️
