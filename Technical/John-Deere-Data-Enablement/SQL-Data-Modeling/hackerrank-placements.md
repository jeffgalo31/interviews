# HackerRank: Placements

**Type:** HackerRank SQL challenge
**Source:** [Placements](https://www.hackerrank.com/challenges/placements/problem)
**Focus:** relational joins, comparing related records, ordering by a joined value

## Exercise

For each student, compare their offered salary with the salary offered to their best friend. Return students whose friend received the higher offer, ordered by the friend's salary.

Example data:

**Students**

| ID | Name |
|---:|---|
| 1 | Alice |
| 2 | Bob |
| 3 | Cara |

**Friends**

| ID | Friend_ID |
|---:|---:|
| 1 | 2 |
| 2 | 3 |
| 3 | 1 |

**Packages**

| ID | Salary |
|---:|---:|
| 1 | 10 |
| 2 | 20 |
| 3 | 30 |

Alice's friend earns 20 and Bob's friend earns 30; Cara's friend earns less than Cara. Expected result, ordered by friend salary:

```text
Alice
Bob
```

## Solution

```sql
SELECT student.name
FROM Students AS student
JOIN Friends AS friend
  ON friend.ID = student.ID
JOIN Packages AS student_offer
  ON student_offer.ID = student.ID
JOIN Packages AS friend_offer
  ON friend_offer.ID = friend.Friend_ID
WHERE friend_offer.Salary > student_offer.Salary
ORDER BY friend_offer.Salary;
```

The `Packages` table is joined twice under different aliases: once for the student and once for the best friend.

**Complexity:** The logical query is linear in the participating rows; actual performance depends on indexes and the database optimizer. Index `Friends.ID` and `Packages.ID` in a production schema.
