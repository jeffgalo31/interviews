-- Binary Tree Nodes  (Medium · Advanced Select)  https://www.hackerrank.com/challenges/binary-search-tree-1/problem
-- Description: README.md (same folder).
--
-- RUNNABLE LOCAL VERSION (SQLite).
-- HackerRank already has the BST table filled in; locally we build the sample first.
-- Run: Terminal -> Run Task -> "Run SQL file (SQLite)"  (fresh in-memory DB every time)
-- This query is plain SQL, so it is the same in SQLite and MySQL.
-- The HackerRank copy is solution_hackerrank.sql.

-- ---------------------------------------------------------------------------
-- SETUP: the sample tree (HackerRank does this for you)
--         5            N = node value, P = its parent
--       /   \          the root has no parent -> P is NULL
--      2     8
--     / \   / \
--    1   3 6   9
-- ---------------------------------------------------------------------------
DROP TABLE IF EXISTS BST;

CREATE TABLE BST (N INTEGER, P INTEGER);

INSERT INTO BST (N, P) VALUES
    (1, 2),
    (3, 2),
    (6, 8),
    (9, 8),
    (2, 5),
    (8, 5),
    (5, NULL);

-- ---------------------------------------------------------------------------
-- QUERY: label every node Root / Inner / Leaf
-- Expected: 1 Leaf, 2 Inner, 3 Leaf, 5 Root, 6 Leaf, 8 Inner, 9 Leaf
-- ---------------------------------------------------------------------------
SELECT N,
       CASE
           -- 1) No parent -> Root. Must be checked FIRST: the root is also a parent,
           --    and CASE stops at the first WHEN that is true.
           --    Use IS NULL: "P = NULL" is never true in SQL.
           WHEN P IS NULL THEN 'Root'

           -- 2) My value appears in the P column -> I'm somebody's parent -> Inner.
           --    SELECT P FROM BST = (2, 2, 8, 8, 5, 5, NULL)
           WHEN N IN (SELECT P FROM BST) THEN 'Inner'

           -- 3) Not root, nobody's parent -> Leaf.
           --    (Don't write this as "N NOT IN (SELECT P FROM BST)": the list contains
           --     the root's NULL, and NOT IN with a NULL in the list is never true.)
           ELSE 'Leaf'
       END AS node_type
FROM BST
ORDER BY N;    -- ordered by node value
