# Ollivander's Inventory

**Difficulty:** Medium · **Section:** Basic Join · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/harry-potter-and-wands/problem)

---

Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand. 

Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each *non-evil* wand of high power and age. Write a query to print the _id_, _age_, _coins\_needed_, and _power_ of the wands that Ron's interested in, sorted in order of descending _power_. If more than one wand has same power, sort the result in order of descending _age_.

**Input Format**

The following tables contain data on the wands in Ollivander's inventory:

- _Wands:_ The _id_ is the id of the wand, _code_ is the code of the wand, _coins\_needed_ is the total number of gold galleons needed to buy the wand, and _power_ denotes the quality of the wand (the higher the power, the better the wand is). <img src="https://s3.amazonaws.com/hr-challenge-images/19502/1458538092-b2a8163a74-ScreenShot2016-03-08at12.13.39AM.png"/>

- _Wands\_Property:_ The _code_ is the code of the wand, _age_ is the age of the wand, and _is\_evil_ denotes whether the wand is good for the dark arts. If the value of _is\_evil_ is _0_, it means that the wand is not evil. The mapping between *code* and *age* is one-one, meaning that if there are two pairs, $(code_1,\ age_1)$ and $(code_2,\ age_2)$, then $code_1 \neq code_2$ and $age_1 \neq age_2$.<img src="https://s3.amazonaws.com/hr-challenge-images/19502/1458538221-18c4092b7d-ScreenShot2016-03-08at12.13.53AM.png"/>

----

**Sample Input**

Wands Table: ![](https://s3.amazonaws.com/hr-challenge-images/19502/1458538559-51bf29644e-ScreenShot2016-03-21at10.34.41AM.png) Wands_Property Table: ![](https://s3.amazonaws.com/hr-challenge-images/19502/1458538583-fd514566f9-ScreenShot2016-03-21at10.34.28AM.png)

**Sample Output**

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

**Explanation**

> The explanation on HackerRank uses formulas that don't copy as text; see the [problem page](https://www.hackerrank.com/challenges/harry-potter-and-wands/problem). The Solution section below walks through it.

## Solution

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

- Join each wand to its property row to get `age` and `is_evil`.
- For every (age, power) combination keep only the cheapest wand: the subquery finds that minimum for the current row's age and power.
- Exclude evil wands; sort by power, then age, both descending.

**Sample data in solution.sql:** rebuilt to reproduce HackerRank's Sample Output (the sample tables are images on HackerRank).

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank and **choose MySQL** in the language menu)
