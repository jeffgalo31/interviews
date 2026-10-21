<!-- study-layout -->
# Ollivander's Inventory

🟡 **Medium** · 📁 **Basic Join** · 🗄️ HackerRank SQL · [Open on HackerRank ↗](https://www.hackerrank.com/challenges/harry-potter-and-wands/problem)

**On this page:** [📝 Problem](#-problem) · [📥 Input & output](#-input--output) · [🧪 Example](#-example) · [💡 Solution](#-solution) · [📂 Files](#-files)

---

## 📝 Problem

Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.

Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each *non-evil* wand of high power and age. Write a query to print the _id_, _age_, _coins\_needed_, and _power_ of the wands that Ron's interested in, sorted in order of descending _power_. If more than one wand has same power, sort the result in order of descending _age_.

## 📥 Input & output

### Input format

The following tables contain data on the wands in Ollivander's inventory:

- _Wands:_ The _id_ is the id of the wand, _code_ is the code of the wand, _coins\_needed_ is the total number of gold galleons needed to buy the wand, and _power_ denotes the quality of the wand (the higher the power, the better the wand is).

| Column | Type |
|---|---|
| id | Integer |
| code | Integer |
| coins_needed | Integer |
| power | Integer |

- _Wands\_Property:_ The _code_ is the code of the wand, _age_ is the age of the wand, and _is\_evil_ denotes whether the wand is good for the dark arts. If the value of _is\_evil_ is _0_, it means that the wand is not evil. The mapping between *code* and *age* is one-one, meaning that if there are two pairs, $(code_1,\ age_1)$ and $(code_2,\ age_2)$, then $code_1 \neq code_2$ and $age_1 \neq age_2$.

| Column | Type |
|---|---|
| code | Integer |
| age | Integer |
| is_evil | Integer |

----

## 🧪 Example

**Input**

Wands Table:

| id | code | coins_needed | power |
|---|---|---|---|
| 1 | 4 | 3688 | 8 |
| 2 | 3 | 9365 | 3 |
| 3 | 3 | 7187 | 10 |
| 4 | 3 | 734 | 8 |
| 5 | 1 | 6020 | 2 |
| 6 | 2 | 6773 | 7 |
| 7 | 3 | 9873 | 9 |
| 8 | 3 | 7721 | 7 |
| 9 | 1 | 1647 | 10 |
| 10 | 4 | 504 | 5 |
| 11 | 2 | 7587 | 5 |
| 12 | 5 | 9897 | 10 |
| 13 | 3 | 4651 | 8 |
| 14 | 2 | 5408 | 1 |
| 15 | 2 | 6018 | 7 |
| 16 | 4 | 7710 | 5 |
| 17 | 2 | 8798 | 7 |
| 18 | 2 | 3312 | 3 |
| 19 | 4 | 7651 | 6 |
| 20 | 5 | 5689 | 3 |

 Wands_Property Table:

| code | age | is_evil |
|---|---|---|
| 1 | 45 | 0 |
| 2 | 40 | 0 |
| 3 | 4 | 1 |
| 4 | 20 | 0 |
| 5 | 17 | 0 |

**Output**

```
9 45 1647 10
12 17 9897 10
1 20 3688 8
15 40 6018 7
19 20 7651 6
11 40 7587 5
10 20 504 5
18 40 3312 3
20 17 5689 3
5 45 6020 2
14 40 5408 1
```

**Why**

The data for wands of age 45 (code 1):

| id | age | coins_needed | power |
|---|---|---|---|
| 5 | 45 | 6020 | 2 |
| 9 | 45 | 1647 | 10 |

- The minimum number of galleons needed for wand(age = 45, power = 2) = 6020
- The minimum number of galleons needed for wand(age = 45, power = 10) = 1647

The data for wands of age 40 (code 2):

| id | age | coins_needed | power |
|---|---|---|---|
| 14 | 40 | 5408 | 1 |
| 18 | 40 | 3312 | 3 |
| 11 | 40 | 7587 | 5 |
| 15 | 40 | 6018 | 7 |
| 6 | 40 | 6773 | 7 |
| 17 | 40 | 8798 | 7 |

- The minimum number of galleons needed for wand(age = 40, power = 1) = 5408
- The minimum number of galleons needed for wand(age = 40, power = 3) = 3312
- The minimum number of galleons needed for wand(age = 40, power = 5) = 7587
- The minimum number of galleons needed for wand(age = 40, power = 7) = 6018

The data for wands of age 20 (code 4):

| id | age | coins_needed | power |
|---|---|---|---|
| 10 | 20 | 504 | 5 |
| 16 | 20 | 7710 | 5 |
| 19 | 20 | 7651 | 6 |
| 1 | 20 | 3688 | 8 |

- The minimum number of galleons needed for wand(age = 20, power = 5) = 504
- The minimum number of galleons needed for wand(age = 20, power = 6) = 7651
- The minimum number of galleons needed for wand(age = 20, power = 8) = 3688

The data for wands of age 17 (code 5):

| id | age | coins_needed | power |
|---|---|---|---|
| 20 | 17 | 5689 | 3 |
| 12 | 17 | 9897 | 10 |

- The minimum number of galleons needed for wand(age = 17, power = 3) = 5689
- The minimum number of galleons needed for wand(age = 17, power = 10) = 9897

> Numbers that appear as formulas on HackerRank are filled in here.

## 💡 Solution

> [!TIP]
> **Key idea:** Join each wand to its property row to get `age` and `is_evil`.

### ✍️ The query

```sql
SELECT w.id, p.age, w.coins_needed, w.power
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
ORDER BY w.power DESC, p.age DESC;
```

### 🔍 How it works

- For every (age, power) combination keep only the cheapest wand: the subquery finds that minimum for the current row's age and power.
- Exclude evil wands; sort by power, then age, both descending.

## 📂 Files

| | File | What it's for |
|---|---|---|
| ▶️ | [solution.sql](solution.sql) | Runnable, commented version on SQLite. In VS Code: **Terminal → Run Task → Run SQL file (SQLite)** |
| 📋 | [solution_hackerrank.sql](solution_hackerrank.sql) | Paste into HackerRank and choose **MySQL** in the language menu |

🧪 **Sample data in solution.sql:** the official HackerRank sample (transcribed from HackerRank's images), so the output matches the Example above.

---

⬅️ [Top Competitors](../top-competitors/README.md) · [🗄️ All SQL exercises](../../README.md) · [Challenges](../challenges/README.md) ➡️
