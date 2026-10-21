# Binary Tree Nodes

**Difficulty:** Medium · **Section:** Advanced Select · **Track:** HackerRank SQL · [Open on HackerRank](https://www.hackerrank.com/challenges/binary-search-tree-1/problem)

You are given a table, **BST**, containing two columns: **N** and **P**, where **N** represents the value of a node in Binary Tree, and **P** is the parent of **N**.

| Column | Type |
|---|---|
| N | Integer |
| P | Integer |

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

- **Root:** If node is root node.
- **Leaf:** If node is leaf node.
- **Inner:** If node is neither root nor leaf node.

## Sample Input

> On HackerRank the schema, sample table and tree are images; transcribed here as text.

| N | P |
|---|---|
| 1 | 2 |
| 3 | 2 |
| 6 | 8 |
| 9 | 8 |
| 2 | 5 |
| 8 | 5 |
| 5 | NULL |

## Sample Output

```
1 Leaf
2 Inner
3 Leaf
5 Root
6 Leaf
8 Inner
9 Leaf
```

## Explanation

The Binary Tree below illustrates the sample:

```
        5
      /   \
     2     8
    / \   / \
   1   3 6   9
```

## Solution

```sql
SELECT N,
       CASE
           WHEN P IS NULL                  THEN 'Root'
           WHEN N IN (SELECT P FROM BST)   THEN 'Inner'
           ELSE 'Leaf'
       END
FROM BST
ORDER BY N;
```

Each node is checked with two questions, **in this order**:

| Question | How in SQL | Type |
|---|---|---|
| Has no parent? | `P IS NULL` | Root |
| Is it someone's parent? | `N IN (SELECT P FROM BST)` (its value appears in the P column) | Inner |
| Neither | `ELSE` | Leaf |

- **Order matters:** the root is also someone's parent (5 is the parent of 2 and 8), so `Root` must be checked first. `CASE` stops at the first `WHEN` that is true.
- **`P IS NULL`, never `P = NULL`:** comparing with `=` to NULL is never true in SQL.
- **Watch out for `NOT IN`:** writing the leaf test as `N NOT IN (SELECT P FROM BST)` returns nothing, because the P column contains a NULL (the root's) and `NOT IN` with a NULL in the list is never true. Testing `IN` for Inner and letting `ELSE` catch leaves avoids that trap.

Walkthrough of the sample (P column values = 2, 2, 8, 8, 5, 5, NULL):

| N | P | P IS NULL? | N in P column? | Result |
|---|---|---|---|---|
| 1 | 2 | no | no | Leaf |
| 2 | 5 | no | yes | Inner |
| 3 | 2 | no | no | Leaf |
| 5 | NULL | **yes** | (yes, not checked) | Root |
| 6 | 8 | no | no | Leaf |
| 8 | 5 | no | yes | Inner |
| 9 | 8 | no | no | Leaf |

Files: [solution.sql](solution.sql) (runs locally on SQLite) · [solution_hackerrank.sql](solution_hackerrank.sql) (paste into HackerRank, **choose MySQL** in the language menu; it opens on DB2)
