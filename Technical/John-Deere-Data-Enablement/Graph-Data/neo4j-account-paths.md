# Neo4j: Find Short Account Transfer Paths

**Type:** Supplemental original graph-database exercise
**Source:** [Neo4j Cypher Manual](https://neo4j.com/docs/cypher-manual/current/)
**Focus:** property-graph modeling, Cypher traversal, parameterized queries

## Exercise

Model transfers between accounts. Find destination accounts reachable from a source account in one to three settled transfers, and return hop count and total transferred amount. Exclude the starting account.

Example graph data:

| From | To | Amount | Status |
|---|---|---:|---|
| A-1 | A-2 | 10.00 | SETTLED |
| A-2 | A-3 | 5.00 | SETTLED |
| A-1 | A-4 | 50.00 | PENDING |

For source `A-1`, the expected results are `A-2, 1, 10.00` and `A-3, 2, 15.00`. `A-4` is excluded because its transfer is pending; the source account is never returned.

## Solution

Create directed `TRANSFER_TO` relationships with amount, timestamp, and status properties. Enforce a unique account identifier.

```cypher
CREATE CONSTRAINT account_id IF NOT EXISTS
FOR (account:Account)
REQUIRE account.accountId IS UNIQUE;
```

Parameterized traversal:

```cypher
MATCH path = (source:Account {accountId: $sourceAccountId})
              -[:TRANSFER_TO*1..3]->(destination:Account)
WHERE destination.accountId <> $sourceAccountId
  AND all(transfer IN relationships(path)
          WHERE transfer.status = 'SETTLED')
RETURN destination.accountId AS destinationAccountId,
       length(path) AS transferCount,
       reduce(total = 0.0, transfer IN relationships(path) | total + transfer.amount)
           AS totalTransferred
ORDER BY transferCount, destinationAccountId;
```

Use bound parameters rather than concatenating user input into Cypher. For production, define time/status filters, access control, maximum traversal depth, and an index/constraint plan; inspect `EXPLAIN`/`PROFILE` with representative data.

**Trade-off:** A graph traversal is natural when relationship paths are the question. For a simple account-by-ID lookup or ledger aggregation, a relational model may be clearer and easier to constrain.
