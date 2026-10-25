# DynamoDB: Design from Access Patterns

**Type:** Supplemental original data-modeling exercise
**Source:** [AWS: First steps for modeling relational data in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-modeling-nosql.html)
**Focus:** NoSQL modeling, partition/sort keys, denormalization, relational-vs-key-value trade-offs

## Exercise

An ingestion service needs to support these operations: get a file's processing state by file ID; list files for a customer in time order; and find a file by its idempotency key. Propose a DynamoDB key design and explain when the relational record belongs in RDS instead.

Example stored representations for one uploaded file:

| PK | SK | Attributes |
|---|---|---|
| `FILE#F42` | `STATE` | `customerId=C7, status=COMPLETE` |
| `CUSTOMER#C7` | `FILE#2026-10-12T10:00:00Z#F42` | `fileId=F42, status=COMPLETE` |
| `IDEMPOTENCY#upload-9` | `REQUEST` | `fileId=F42` |

Expected reads: querying `FILE#F42` returns its state; querying `CUSTOMER#C7` returns that customer's file collection in sort-key time order; conditionally writing `IDEMPOTENCY#upload-9` a second time must not create a second job.

## Solution

Use one table with a partition key (`PK`) and sort key (`SK`), documenting each access pattern before adding indexes:

| Access pattern | Key design | Example |
|---|---|---|
| Get state by file ID | `PK = FILE#<fileId>`, `SK = STATE` | `FILE#f-42 / STATE` |
| List customer files newest first | `PK = CUSTOMER#<customerId>`, `SK = FILE#<ISO-8601 timestamp>#<fileId>` | Query one customer partition, reverse sort order |
| Find idempotency key | `PK = IDEMPOTENCY#<key>`, `SK = REQUEST` | Conditional `PutItem` creates only if absent |

For both file and customer lookup, write the needed item representations transactionally or make the secondary item repairable. Add TTL only if the business retention policy allows expiry. Use a condition expression for idempotency rather than a read-then-write race. Choose and test partition keys to avoid hot partitions at expected scale.

Store the authoritative operational record with status transitions and relational constraints in **RDS** when transactions span related rows or teams need flexible SQL joins. Use **DynamoDB** for high-throughput, predictable key-based reads/writes where access patterns are known. Avoid duplicating mutable business truth without defining ownership, consistency, and reconciliation.

**Discussion:** Which pattern requires a GSI if queries must list files across customers? What consistency does the caller need after upload? How would you expire or archive audit data without violating retention rules?
