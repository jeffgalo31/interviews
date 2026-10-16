# Data Engineering Interview Cheat Sheet

Java · Python · SQL · ETL · Data Modeling · Data Warehousing · Spark · Databricks · SQL DB · NoSQL DB · Data Lake · Graph DB

---

## Quick Overview

| Tech | What it is | Type | Use it for |
|---|---|---|---|
| **Java** | Statically typed, JVM language | Language | Backend services, Spark/Kafka/Hadoop internals, high-throughput systems |
| **Python** | Dynamic, high-level language | Language | Pipelines, PySpark, scripting, ML, orchestration (Airflow) |
| **SQL** | Declarative query language | Language | Querying/transforming relational data, analytics |
| **ETL** | Extract → Transform → Load pipelines | Process | Moving and shaping data from sources to targets |
| **Data Modeling** | Designing table structure and relationships | Design | Normalized (OLTP) and dimensional (OLAP) schemas |
| **Data Warehouse** | Central, structured store optimized for analytics | Storage | BI, reporting (Snowflake, Redshift, BigQuery) |
| **Apache Spark** | Distributed in-memory processing engine | Compute | Large-scale batch/stream processing |
| **Databricks** | Managed Spark platform + Delta Lake (lakehouse) | Platform | Unified analytics, ML, ETL on a lake |
| **SQL DB** | Relational DB, schema + ACID | Database | Transactions, joins, structured data |
| **NoSQL DB** | Non-relational (KV, document, column, graph) | Database | Scale, flexible schema, low latency |
| **Data Lake** | Raw data in any format on cheap object storage | Storage | Raw/semi-structured data, ML, schema-on-read |
| **Graph DB** | Nodes + edges stored natively | Database | Relationship-heavy queries (fraud, recommendations) |

**Typical architecture:** Sources (DBs, APIs, events) → Ingestion (Kafka/ADF/Fivetran) → Data Lake (raw/bronze) → Spark/Databricks transforms (silver/gold) → Warehouse/serving layer → BI/ML.

---

## 1. Java

**Key points**
- Compiled to bytecode, runs on the JVM; garbage collected; strongly/statically typed.
- Core: OOP, interfaces, generics, collections, streams/lambdas (Java 8+), exceptions, concurrency.
- Heavily used in data infra: Spark (Scala/Java), Kafka, Hadoop, Flink, Cassandra.
- Memory: heap (young/old gen) vs stack; GC options (G1, ZGC).

**Questions**
1. **HashMap vs ConcurrentHashMap vs Hashtable?** HashMap: not thread-safe, allows one null key. Hashtable: fully synchronized, legacy. ConcurrentHashMap: segment/bin-level locking, high concurrency, no null keys.
2. **How does HashMap work?** Array of buckets, hash(key) → index; collisions via linked list/tree (treeifies at 8). `equals`/`hashCode` contract matters; resizes at load factor 0.75.
3. **`equals` vs `==`?** `==` compares references; `equals` compares logical content.
4. **Abstract class vs interface?** Interface: contract, multiple implementation, default methods. Abstract class: shared state/partial implementation, single inheritance.
5. **Checked vs unchecked exceptions?** Checked must be handled/declared (IOException); unchecked extend RuntimeException.
6. **What are Streams?** Declarative, lazy pipelines (`map`, `filter`, `reduce`, `collect`); parallel streams exist but use carefully.
7. **How does garbage collection work?** Reachability from GC roots; generational collection; tune with heap size and collector choice.
8. **Threads and concurrency?** `ExecutorService`, `synchronized`, `volatile`, locks, `CompletableFuture`; avoid shared mutable state.
9. **`final`, `finally`, `finalize`?** Constant/non-overridable; always-run block; deprecated GC hook.
10. **Why does Java matter for Spark?** JVM-based, so serialization, GC tuning, and memory settings affect job performance.

---

## 2. Python

**Key points**
- Dynamic, interpreted; dominant in data engineering (pandas, PySpark, Airflow, dbt tooling).
- Core: list/dict/set/tuple, comprehensions, generators, decorators, context managers, OOP.
- **GIL** limits CPU-bound threading; use multiprocessing, async, or native libs for parallelism.
- Packaging: `venv`, `pip`, `poetry`; type hints.

**Questions**
1. **List vs tuple?** List mutable, tuple immutable (hashable if contents are, usable as dict keys).
2. **What is the GIL?** Mutex allowing one thread to execute bytecode at a time; fine for I/O-bound, bad for CPU-bound threading.
3. **Generators vs lists?** Generators yield lazily, use constant memory; ideal for large files/streams.
4. **Decorators?** Functions that wrap functions to add behavior (logging, retries, caching).
5. **`*args` / `**kwargs`?** Variable positional / keyword arguments.
6. **Deep vs shallow copy?** Shallow copies references to nested objects; deep copies recursively.
7. **pandas vs PySpark?** pandas: single machine, in-memory. PySpark: distributed, lazy, scales to TBs.
8. **How do you process a file too big for memory?** Read in chunks/generators, `pandas.read_csv(chunksize=)`, or use Spark/Dask.
9. **Mutable default arguments pitfall?** Default evaluated once; use `None` and create inside.
10. **How do you write idempotent, testable pipeline code?** Pure functions, config-driven, pytest with fixtures, retries with backoff, logging.

**Common coding tasks:** dedupe a list, count word frequency (`Counter`), merge intervals, group/aggregate records, parse JSON/CSV, two-sum.

---

## 3. SQL

**Key points**
- Execution order: `FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT`.
- **Joins:** INNER, LEFT, RIGHT, FULL, CROSS, SELF; anti-join (`LEFT JOIN ... IS NULL` / `NOT EXISTS`).
- **Window functions:** `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG/LEAD`, `SUM() OVER (PARTITION BY ... ORDER BY ...)`.
- CTEs, subqueries, `UNION` vs `UNION ALL`, `CASE WHEN`, `COALESCE`.
- Indexes (B-tree), query plans (`EXPLAIN`), transactions, isolation levels.

**Questions**
1. **WHERE vs HAVING?** WHERE filters rows before grouping; HAVING filters groups after aggregation.
2. **RANK vs DENSE_RANK vs ROW_NUMBER?** RANK skips numbers after ties, DENSE_RANK doesn't, ROW_NUMBER is unique.
3. **Find the 2nd highest salary?** `DENSE_RANK() OVER (ORDER BY salary DESC)` = 2, or subquery with `MAX(salary) < (SELECT MAX...)`.
4. **Find duplicates?** `GROUP BY cols HAVING COUNT(*) > 1`; delete with `ROW_NUMBER()` partition and keep rn=1.
5. **UNION vs UNION ALL?** UNION dedupes (slower); UNION ALL keeps all rows.
6. **Delete vs Truncate vs Drop?** DELETE: row-level, logged, filterable. TRUNCATE: fast, removes all rows. DROP: removes the table.
7. **How do indexes work / when do they hurt?** B-tree speeds reads; slow writes and use storage; ineffective on low-cardinality columns or with functions on the column.
8. **How do you optimize a slow query?** Read the execution plan, add/adjust indexes, avoid `SELECT *`, filter early, avoid functions on indexed columns, reduce joins, check stats.
9. **Running total / moving average?** `SUM(x) OVER (ORDER BY d ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)`.
10. **Consecutive days / gaps and islands?** `date - ROW_NUMBER()` grouping trick.
11. **NULL handling?** `NULL = NULL` is unknown; use `IS NULL`; aggregates ignore NULLs except `COUNT(*)`.
12. **ACID and isolation levels?** Read uncommitted → read committed → repeatable read → serializable (prevents dirty, non-repeatable, phantom reads).

---

## 4. ETL

**Key points**
- **ETL:** transform before loading (traditional, warehouse). **ELT:** load raw first, transform in the warehouse/lake (modern, cheap storage + compute).
- Batch vs streaming; full load vs **incremental** (watermark, CDC).
- Orchestration: Airflow, ADF, Step Functions, Dagster; transformations: dbt, Spark.
- Concerns: idempotency, retries, schema evolution, data quality, lineage, monitoring.

**Questions**
1. **ETL vs ELT?** ETL transforms in a separate engine before load; ELT loads raw then transforms in-target. ELT is the norm with cloud warehouses/lakes.
2. **Full vs incremental load?** Full reloads everything; incremental loads only new/changed rows (timestamp watermark, CDC, hash compare).
3. **What is CDC?** Change Data Capture: reading DB logs (Debezium, DMS) to stream inserts/updates/deletes.
4. **How do you make a pipeline idempotent?** Overwrite partitions, use `MERGE`/upserts, deterministic keys, avoid append-only duplicates.
5. **How do you handle late-arriving data?** Watermarks, reprocessing windows, partition overwrite, event-time vs processing-time.
6. **Data quality checks?** Row counts, null/uniqueness checks, schema validation, freshness, Great Expectations/dbt tests, quarantine bad records.
7. **How do you handle schema changes?** Schema registry, permissive/evolving formats (Parquet/Avro/Delta), alert on drift.
8. **Backfills?** Parameterize by date, rerun partitions, ensure idempotency.
9. **Batch vs streaming?** Batch: simpler, high throughput, latency in minutes+. Streaming: low latency, complexity (state, ordering, exactly-once).
10. **Airflow concepts?** DAG, tasks, operators, schedule, sensors, XComs, retries, backfill/catchup.
11. **SCD handling in pipelines?** Type 2 via `MERGE` with effective dates/current flag.

---

## 5. Data Modeling

**Key points**
- **OLTP:** normalized (3NF), many small transactions. **OLAP:** denormalized/dimensional, large scans.
- **Normal forms:** 1NF atomic values, 2NF no partial dependency, 3NF no transitive dependency.
- **Dimensional modeling (Kimball):** **fact** tables (measures, FKs) + **dimension** tables (descriptive context).
- Schemas: **Star** (denormalized dims) vs **Snowflake** (normalized dims).
- Grain: the level of detail of a fact row; define it first.

**Questions**
1. **Fact vs dimension?** Fact: numeric events (sales amount), large, grows fast. Dimension: descriptive attributes (customer, product, date), smaller.
2. **Star vs snowflake?** Star: fewer joins, faster queries, some redundancy. Snowflake: less redundancy, more joins.
3. **What is grain?** What one row represents (one order line per day). Mixing grains causes wrong aggregates.
4. **SCD types?** Type 1 overwrite; Type 2 new row with history (start/end date, current flag); Type 3 extra column for previous value.
5. **Surrogate vs natural key?** Surrogate: system-generated, stable, decoupled from source. Natural: business key, may change.
6. **Fact table types?** Transactional, periodic snapshot, accumulating snapshot, factless.
7. **Normalize or denormalize?** Normalize for OLTP integrity; denormalize for analytics read speed.
8. **Data Vault?** Hubs (keys), links (relationships), satellites (attributes); good for auditability and agile integration.
9. **Many-to-many relationships?** Bridge/junction table.
10. **Conformed dimensions?** Shared dimensions (e.g., date, customer) used across fact tables for cross-process analysis.
11. **Design a model for e-commerce.** Facts: order_lines, payments. Dims: customer, product, date, store/channel, promotion.

---

## 6. Data Warehousing

**Key points**
- Central, curated, structured store for analytics; **schema-on-write**; subject-oriented, integrated, time-variant.
- Cloud options: Snowflake, Redshift, BigQuery, Synapse, Databricks SQL.
- Architecture layers: staging → core (integrated) → marts (business-specific).
- Columnar storage, MPP (massively parallel processing), compression, partitioning/clustering.
- Snowflake: separate compute (virtual warehouses) and storage; Redshift: distribution/sort keys; BigQuery: serverless, partition/cluster.

**Questions**
1. **Data warehouse vs database?** Warehouse is OLAP, historical, read-heavy, denormalized. Operational DB is OLTP, current, write-heavy.
2. **Warehouse vs lake vs lakehouse?** Warehouse: structured, schema-on-write. Lake: raw, any format, schema-on-read. Lakehouse: lake storage + ACID/warehouse features (Delta, Iceberg, Hudi).
3. **Why columnar storage?** Reads only needed columns, compresses well, great for aggregations.
4. **What is MPP?** Work split across nodes that process data slices in parallel.
5. **Data mart?** Subject-specific subset of the warehouse (finance, marketing).
6. **Inmon vs Kimball?** Inmon: top-down, enterprise normalized warehouse first. Kimball: bottom-up, dimensional marts.
7. **How do you optimize warehouse queries?** Partition/cluster/sort keys, avoid `SELECT *`, pre-aggregate, materialized views, right-size compute, prune data.
8. **Snowflake basics?** Micro-partitions, virtual warehouses, time travel, zero-copy clone, separate storage and compute.
9. **Data skew / distribution?** Choose distribution keys that spread evenly (Redshift) to avoid hot nodes.
10. **How do you control cost?** Auto-suspend compute, partition pruning, retention policies, monitor expensive queries.

---

## 7. Apache Spark

**Key points**
- Distributed engine: **Driver** coordinates, **Executors** run tasks across a cluster (YARN, K8s, standalone, Databricks).
- APIs: RDD (low-level), **DataFrame/Dataset** (optimized via Catalyst + Tungsten), Spark SQL, Structured Streaming, MLlib.
- **Lazy evaluation:** transformations build a DAG; **actions** (`count`, `collect`, `write`) trigger execution.
- **Narrow** transformations (map, filter) vs **wide** (groupBy, join) that cause a **shuffle** (stage boundary).
- Hierarchy: Application → Job → Stage → Task (one task per partition).

**Questions**
1. **Transformation vs action?** Transformations are lazy (return a new DF); actions trigger computation and return/write results.
2. **Narrow vs wide transformation?** Narrow: no data movement between partitions. Wide: shuffle across the network (expensive).
3. **RDD vs DataFrame?** DataFrame has schema and Catalyst optimizer; faster and preferred. RDD is low-level and unoptimized.
4. **`repartition` vs `coalesce`?** `repartition` does a full shuffle (increase or decrease, even sizes). `coalesce` only decreases partitions, no full shuffle.
5. **What is a shuffle and how do you reduce it?** Redistribution of data by key. Reduce with broadcast joins, pre-partitioning, filtering early, `reduceByKey` over `groupByKey`.
6. **Broadcast join?** Ship the small table to all executors to avoid shuffling the big one (`broadcast(df)`, default threshold 10 MB).
7. **How do you handle data skew?** Salting keys, AQE skew join handling, broadcast, repartition by better key.
8. **`cache` vs `persist`?** `cache` = persist with default storage level; `persist` lets you choose (MEMORY_AND_DISK, etc.). Use when a DF is reused.
9. **What is Catalyst?** Query optimizer: logical plan → optimized plan (predicate pushdown, column pruning) → physical plan.
10. **What is AQE?** Adaptive Query Execution: re-optimizes at runtime (coalesce shuffle partitions, switch join strategy, skew handling).
11. **Spark Structured Streaming?** Treats streams as unbounded tables; micro-batch (or continuous); watermarks for late data; checkpoints for fault tolerance; exactly-once with idempotent sinks.
12. **How do you debug OOM / slow jobs?** Spark UI (stages, skew, spill), tune `spark.executor.memory`, `spark.sql.shuffle.partitions`, avoid `collect()`, check partition sizes.
13. **Fault tolerance?** Lineage lets lost partitions be recomputed; checkpointing for streaming.
14. **File formats?** Prefer columnar **Parquet**/ORC (compression, predicate pushdown); Avro for row-based/streaming; avoid many small files.
15. **UDF downsides?** Opaque to Catalyst and slow (esp. Python); prefer built-in functions or pandas UDFs.

---

## 8. Databricks

**Key points**
- Managed platform built by Spark's creators; runs on AWS/Azure/GCP.
- **Delta Lake:** open storage layer on Parquet adding **ACID transactions, schema enforcement/evolution, time travel, MERGE/upserts**.
- **Lakehouse:** warehouse reliability + lake flexibility on one copy of data.
- **Medallion architecture:** Bronze (raw) → Silver (cleaned/conformed) → Gold (business aggregates).
- Components: Notebooks, Jobs/Workflows, Clusters (all-purpose vs job), SQL Warehouses, **Unity Catalog** (governance), Delta Live Tables / Lakeflow, Auto Loader, MLflow.

**Questions**
1. **What is Delta Lake and why use it?** ACID, versioning, upserts, schema enforcement on a data lake; fixes the "data swamp" problem.
2. **Medallion architecture?** Bronze raw ingest, Silver cleaned and deduped, Gold aggregated for BI/ML.
3. **Time travel?** Query older versions (`VERSION AS OF` / `TIMESTAMP AS OF`), restore, audit.
4. **How do you upsert?** `MERGE INTO target USING source ON key WHEN MATCHED THEN UPDATE WHEN NOT MATCHED THEN INSERT`.
5. **`OPTIMIZE`, `ZORDER`, `VACUUM`?** OPTIMIZE compacts small files; ZORDER co-locates data for filter columns; VACUUM removes old unreferenced files (mind retention for time travel). Liquid clustering is the newer alternative to partitioning/ZORDER.
6. **What is Unity Catalog?** Central governance: catalog → schema → table hierarchy, access control, lineage, auditing.
7. **Auto Loader?** Incrementally and efficiently ingests new files from cloud storage with schema inference/evolution (`cloudFiles`).
8. **All-purpose vs job clusters?** All-purpose: interactive/dev, costlier. Job clusters: ephemeral per run, cheaper for production.
9. **Delta Live Tables (DLT)?** Declarative pipelines with built-in quality expectations, dependency handling, and auto-scaling.
10. **How do you do incremental processing?** Auto Loader, Structured Streaming with checkpoints, Change Data Feed, `MERGE`.
11. **Databricks vs plain Spark?** Managed infra, Delta, collaboration, governance, optimized runtime (Photon), job orchestration.
12. **Delta vs Parquet?** Delta = Parquet files + transaction log (`_delta_log`) giving ACID, versioning, and metadata handling.

---

## 9. SQL Databases (Relational)

**Key points**
- Tables, rows, fixed schema, relationships via PK/FK; **ACID** transactions.
- Engines: PostgreSQL, MySQL, SQL Server, Oracle, Aurora.
- Scaling: vertical, read replicas, partitioning (declarative), sharding (hard), caching.
- Indexes: B-tree, hash, composite, covering, clustered vs non-clustered.

**Questions**
1. **ACID?** Atomicity (all or nothing), Consistency (valid state), Isolation (concurrent txns don't interfere), Durability (committed = persisted).
2. **Clustered vs non-clustered index?** Clustered defines physical row order (one per table); non-clustered is a separate structure pointing to rows.
3. **Normalization trade-offs?** Less redundancy and better integrity, but more joins.
4. **What is a transaction deadlock?** Two transactions hold locks the other needs; DB aborts one. Prevent with consistent lock order and short transactions.
5. **Primary vs foreign vs unique key?** PK uniquely identifies rows (not null); FK references another table; unique enforces uniqueness (allows NULL).
6. **Partitioning vs sharding?** Partitioning splits a table within one DB; sharding spreads data across multiple DB servers.
7. **How do you scale reads/writes?** Reads: replicas, cache. Writes: vertical scale, sharding, queueing/batching.
8. **MVCC?** Multi-version concurrency control: readers see snapshots, don't block writers (Postgres, MySQL InnoDB).
9. **OLTP vs OLAP databases?** OLTP: row-store, short transactions. OLAP: columnar, large scans.
10. **Stored procedures, views, materialized views?** Reusable logic on server; virtual query; precomputed stored results (need refresh).

---

## 10. NoSQL Databases

**Key points**
- Flexible schema, horizontal scale, often **BASE** / eventual consistency.
- **Types:**
  - **Key-value:** Redis, DynamoDB: caching, sessions.
  - **Document:** MongoDB, Couchbase: JSON-like records, catalogs.
  - **Wide-column:** Cassandra, HBase: time-series, huge write throughput.
  - **Graph:** Neo4j: relationships (see section 12).
- **CAP theorem:** under a partition you choose Consistency or Availability (CP vs AP).

**Questions**
1. **SQL vs NoSQL?** SQL: structure, joins, ACID. NoSQL: scale-out, flexible schema, specific access patterns, often eventual consistency.
2. **CAP theorem?** A distributed system can guarantee only two of Consistency, Availability, Partition tolerance; P is mandatory, so choose CP or AP.
3. **ACID vs BASE?** BASE: Basically Available, Soft state, Eventually consistent.
4. **When to choose MongoDB?** Evolving JSON documents, flexible schema, developer velocity; avoid heavy multi-document joins.
5. **How does Cassandra work?** Masterless ring, consistent hashing, tunable consistency (`ONE`/`QUORUM`/`ALL`), LSM-tree writes, query-first modeling.
6. **How do you model data in NoSQL?** Start from queries/access patterns; denormalize; embed vs reference.
7. **What is sharding?** Splitting data across nodes by a shard key; a bad key causes hot spots.
8. **Redis use cases?** Cache, session store, rate limiting, leaderboards, pub/sub; in-memory with optional persistence.
9. **Eventual consistency?** Replicas converge over time; reads may be stale temporarily.
10. **Replication & quorum?** `R + W > N` ensures read-your-write consistency.
11. **When NOT to use NoSQL?** Complex joins, multi-row transactions, ad hoc analytics.

---

## 11. Data Lake

**Key points**
- Stores **raw data in native format** (structured, semi-structured, unstructured) on cheap object storage (S3, ADLS, GCS).
- **Schema-on-read** vs warehouse schema-on-write.
- Zones: raw/landing → cleansed → curated.
- Formats: Parquet, ORC, Avro, JSON, CSV; table formats: **Delta, Iceberg, Hudi** (ACID, time travel, schema evolution).
- Catalog/metadata: Glue Data Catalog, Hive Metastore, Unity Catalog; query: Athena, Presto/Trino, Spark.
- Risk: **data swamp** without governance, metadata, and quality.

**Questions**
1. **Data lake vs data warehouse?** Lake: raw, flexible, cheap, schema-on-read, ML-friendly. Warehouse: curated, structured, fast BI, schema-on-write.
2. **What is a lakehouse?** Lake storage with warehouse features (ACID, governance, BI performance) via Delta/Iceberg/Hudi.
3. **Why Parquet?** Columnar, compressed, splittable, supports predicate pushdown and schema evolution.
4. **How do you partition lake data?** By frequently filtered columns (date); avoid over-partitioning (too many small files).
5. **Small files problem?** Many tiny files slow reads/metadata; fix with compaction (`OPTIMIZE`), larger batch sizes, auto-compaction.
6. **How do you prevent a data swamp?** Catalog and metadata, naming conventions, quality checks, ownership, lifecycle policies, governance.
7. **Delta vs Iceberg vs Hudi?** All add ACID/time travel on object storage. Delta: Databricks-native; Iceberg: engine-agnostic, hidden partitioning; Hudi: strong upserts/streaming ingestion.
8. **How do you secure a lake?** IAM/bucket policies, encryption, column/row-level security, Lake Formation/Unity Catalog, auditing.
9. **How do you query a lake without a cluster?** Athena / Trino / serverless SQL over external tables.
10. **Handling PII?** Masking, tokenization, column-level access, separate zones, retention/deletion (GDPR).

---

## 12. Graph Databases

**Key points**
- Store **nodes** (entities), **edges** (relationships), and **properties**; relationships are first-class.
- **Property graph** (Neo4j, Neptune, TigerGraph) vs **RDF/triple store**.
- Query languages: **Cypher** (Neo4j), Gremlin, SPARQL, openCypher.
- **Index-free adjacency:** traversal cost depends on the local neighborhood, not total data size.
- Use cases: fraud detection, recommendations, social networks, knowledge graphs, network/IT topology.

**Questions**
1. **When graph over relational?** Deep, many-hop relationship queries where SQL would need many recursive self-joins.
2. **What is a property graph?** Nodes and edges with labels/types and key-value properties.
3. **Sample Cypher query?** `MATCH (a:Person)-[:FRIEND]->(b)-[:FRIEND]->(c) WHERE a.name='Ana' RETURN DISTINCT c.name`.
4. **Why are graph traversals fast?** Direct pointers between nodes, no join computation.
5. **Graph DB vs NoSQL document?** Document stores optimize per-record access; graph optimizes connected data traversal.
6. **Limitations?** Harder to scale/shard horizontally, less suited for bulk aggregations and simple tabular lookups.
7. **Fraud detection example?** Find accounts sharing devices/addresses/cards through connected components and shortest paths.
8. **Graph algorithms?** PageRank, community detection, shortest path, centrality, connected components.
9. **AWS option?** Amazon Neptune (supports Gremlin, openCypher, SPARQL).
10. **Graph processing in Spark?** GraphFrames / GraphX for batch graph analytics on large data.

---

## Cross-Technology / Scenario Questions

1. **Design a batch data pipeline.** Source DB → CDC/ingest to S3 raw (bronze) → Spark/Databricks cleans and dedupes (silver) → aggregates into gold/warehouse → BI; orchestrate with Airflow, add quality checks and alerts.
2. **Design a real-time pipeline.** Events → Kafka/Kinesis → Spark Structured Streaming/Flink → Delta/serving store (Redis/Druid) with watermarks and checkpoints.
3. **Warehouse vs lake vs lakehouse?** Pick warehouse for BI-first, lake for raw/ML, lakehouse to unify both on one copy.
4. **Which database for which job?** Transactions → SQL; massive key lookups → DynamoDB/Cassandra; flexible docs → MongoDB; relationships → Graph; analytics → warehouse.
5. **A Spark job is slow. What do you do?** Spark UI → find skewed or long stages → fix joins (broadcast), partitions, caching, file sizes, formats, AQE.
6. **How do you handle duplicates and late data?** Idempotent writes, `MERGE` on business keys, watermarks, dedupe with `ROW_NUMBER`.
7. **How do you ensure data quality?** Tests at ingest and transform (dbt/Great Expectations/DLT expectations), freshness SLAs, lineage, quarantine tables, alerts.
8. **How do you design a slowly changing dimension in Spark/Delta?** `MERGE` with effective dates and `is_current` flag (SCD2).
9. **How do you handle PII and compliance?** Encryption, masking, access control via Unity Catalog, audit logs, retention/deletion.
10. **How do you control cost?** Auto-terminating clusters, job clusters, spot instances, partition pruning, file compaction, lifecycle policies.
11. **Migrate an on-prem warehouse to the cloud?** Assess/inventory, choose target (lakehouse/warehouse), land data in object storage, replicate with CDC, validate with reconciliation, cut over incrementally.

---

## Core Concepts to Know Cold

- **ACID vs BASE** and **CAP theorem**.
- **OLTP vs OLAP**; row vs columnar storage.
- **Star schema, grain, SCD types**, surrogate keys.
- **ETL vs ELT; batch vs streaming; idempotency; incremental/CDC.**
- **Spark internals:** lazy evaluation, DAG, shuffle, partitions, broadcast join, skew, AQE.
- **Delta Lake + medallion architecture.**
- **Window functions, CTEs, joins, and query optimization** in SQL.
- **File formats:** Parquet/ORC (columnar), Avro (row, streaming), JSON/CSV.
- **Data quality, lineage, governance** and PII handling.
- **Related tools:** Kafka/Kinesis (streaming), Airflow/ADF (orchestration), dbt (transform), Snowflake/Redshift/BigQuery (warehouse), Iceberg/Hudi (table formats), Great Expectations (quality).
