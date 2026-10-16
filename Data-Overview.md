<h1 align="center">Data Engineering Interview Cheat Sheet</h1>

<p align="center"><i>Java · Python · SQL · ETL · Data Modeling · Data Warehousing · Spark · Databricks · SQL DB · NoSQL DB · Data Lake · Graph DB</i></p>

<p align="center">

![Interview Prep](https://img.shields.io/badge/Interview-Prep-0A66C2?style=for-the-badge) ![Questions](https://img.shields.io/badge/Questions-143-2ea44f?style=for-the-badge) ![Sections](https://img.shields.io/badge/Sections-15-555?style=for-the-badge)

</p>

<p align="center">

[All Topics](All-Topics-Overview.md) · [AWS](AWS-Overview.md) · **Data** · [Spring Boot](Frameworks-Overview.md) · [DevOps](DevOps-Overview.md) · [Practices](Practices-Overview.md) · [Gen AI](GenAI-Overview.md)

</p>

> [!TIP]
> Click any question to expand the answer. Try answering out loud first.

<details>
<summary><b>📑 Table of contents</b></summary>

1. [🧭 Quick Overview](#-quick-overview)
2. [☕ 1. Java](#-1-java)
3. [🐍 2. Python](#-2-python)
4. [🧮 3. SQL](#-3-sql)
5. [🔄 4. ETL](#-4-etl)
6. [📐 5. Data Modeling](#-5-data-modeling)
7. [🏢 6. Data Warehousing](#-6-data-warehousing)
8. [⚡ 7. Apache Spark](#-7-apache-spark)
9. [🧱 8. Databricks](#-8-databricks)
10. [🗄 9. SQL Databases (Relational)](#-9-sql-databases-relational)
11. [🗄 10. NoSQL Databases](#-10-nosql-databases)
12. [🌊 11. Data Lake](#-11-data-lake)
13. [🕸 12. Graph Databases](#-12-graph-databases)
14. [🧩 Cross-Technology / Scenario Questions](#-cross-technology--scenario-questions)
15. [🎯 Core Concepts to Know Cold](#-core-concepts-to-know-cold)

</details>

---

## 🧭 Quick Overview

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

## ☕ 1. Java

#### 📌 Key points
- Compiled to bytecode, runs on the JVM; garbage collected; strongly/statically typed.
- Core: OOP, interfaces, generics, collections, streams/lambdas (Java 8+), exceptions, concurrency.
- Heavily used in data infra: Spark (Scala/Java), Kafka, Hadoop, Flink, Cassandra.
- Memory: heap (young/old gen) vs stack; GC options (G1, ZGC).

#### ❓ Questions
<details>
<summary><b>1. HashMap vs ConcurrentHashMap vs Hashtable?</b></summary>

HashMap: not thread-safe, allows one null key. Hashtable: fully synchronized, legacy. ConcurrentHashMap: segment/bin-level locking, high concurrency, no null keys.

</details>

<details>
<summary><b>2. How does HashMap work?</b></summary>

Array of buckets, hash(key) → index; collisions via linked list/tree (treeifies at 8). `equals`/`hashCode` contract matters; resizes at load factor 0.75.

</details>

<details>
<summary><b>3. `equals` vs `==`?</b></summary>

`==` compares references; `equals` compares logical content.

</details>

<details>
<summary><b>4. Abstract class vs interface?</b></summary>

Interface: contract, multiple implementation, default methods. Abstract class: shared state/partial implementation, single inheritance.

</details>

<details>
<summary><b>5. Checked vs unchecked exceptions?</b></summary>

Checked must be handled/declared (IOException); unchecked extend RuntimeException.

</details>

<details>
<summary><b>6. What are Streams?</b></summary>

Declarative, lazy pipelines (`map`, `filter`, `reduce`, `collect`); parallel streams exist but use carefully.

</details>

<details>
<summary><b>7. How does garbage collection work?</b></summary>

Reachability from GC roots; generational collection; tune with heap size and collector choice.

</details>

<details>
<summary><b>8. Threads and concurrency?</b></summary>

`ExecutorService`, `synchronized`, `volatile`, locks, `CompletableFuture`; avoid shared mutable state.

</details>

<details>
<summary><b>9. `final`, `finally`, `finalize`?</b></summary>

Constant/non-overridable; always-run block; deprecated GC hook.

</details>

<details>
<summary><b>10. Why does Java matter for Spark?</b></summary>

JVM-based, so serialization, GC tuning, and memory settings affect job performance.

</details>

---

## 🐍 2. Python

#### 📌 Key points
- Dynamic, interpreted; dominant in data engineering (pandas, PySpark, Airflow, dbt tooling).
- Core: list/dict/set/tuple, comprehensions, generators, decorators, context managers, OOP.
- **GIL** limits CPU-bound threading; use multiprocessing, async, or native libs for parallelism.
- Packaging: `venv`, `pip`, `poetry`; type hints.

#### ❓ Questions
<details>
<summary><b>1. List vs tuple?</b></summary>

List mutable, tuple immutable (hashable if contents are, usable as dict keys).

</details>

<details>
<summary><b>2. What is the GIL?</b></summary>

Mutex allowing one thread to execute bytecode at a time; fine for I/O-bound, bad for CPU-bound threading.

</details>

<details>
<summary><b>3. Generators vs lists?</b></summary>

Generators yield lazily, use constant memory; ideal for large files/streams.

</details>

<details>
<summary><b>4. Decorators?</b></summary>

Functions that wrap functions to add behavior (logging, retries, caching).

</details>

<details>
<summary><b>5. `*args` / `**kwargs`?</b></summary>

Variable positional / keyword arguments.

</details>

<details>
<summary><b>6. Deep vs shallow copy?</b></summary>

Shallow copies references to nested objects; deep copies recursively.

</details>

<details>
<summary><b>7. pandas vs PySpark?</b></summary>

pandas: single machine, in-memory. PySpark: distributed, lazy, scales to TBs.

</details>

<details>
<summary><b>8. How do you process a file too big for memory?</b></summary>

Read in chunks/generators, `pandas.read_csv(chunksize=)`, or use Spark/Dask.

</details>

<details>
<summary><b>9. Mutable default arguments pitfall?</b></summary>

Default evaluated once; use `None` and create inside.

</details>

<details>
<summary><b>10. How do you write idempotent, testable pipeline code?</b></summary>

Pure functions, config-driven, pytest with fixtures, retries with backoff, logging.

</details>

**Common coding tasks:** dedupe a list, count word frequency (`Counter`), merge intervals, group/aggregate records, parse JSON/CSV, two-sum.

---

## 🧮 3. SQL

#### 📌 Key points
- Execution order: `FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT`.
- **Joins:** INNER, LEFT, RIGHT, FULL, CROSS, SELF; anti-join (`LEFT JOIN ... IS NULL` / `NOT EXISTS`).
- **Window functions:** `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG/LEAD`, `SUM() OVER (PARTITION BY ... ORDER BY ...)`.
- CTEs, subqueries, `UNION` vs `UNION ALL`, `CASE WHEN`, `COALESCE`.
- Indexes (B-tree), query plans (`EXPLAIN`), transactions, isolation levels.

#### ❓ Questions
<details>
<summary><b>1. WHERE vs HAVING?</b></summary>

WHERE filters rows before grouping; HAVING filters groups after aggregation.

</details>

<details>
<summary><b>2. RANK vs DENSE_RANK vs ROW_NUMBER?</b></summary>

RANK skips numbers after ties, DENSE_RANK doesn't, ROW_NUMBER is unique.

</details>

<details>
<summary><b>3. Find the 2nd highest salary?</b></summary>

`DENSE_RANK() OVER (ORDER BY salary DESC)` = 2, or subquery with `MAX(salary) < (SELECT MAX...)`.

</details>

<details>
<summary><b>4. Find duplicates?</b></summary>

`GROUP BY cols HAVING COUNT(*) > 1`; delete with `ROW_NUMBER()` partition and keep rn=1.

</details>

<details>
<summary><b>5. UNION vs UNION ALL?</b></summary>

UNION dedupes (slower); UNION ALL keeps all rows.

</details>

<details>
<summary><b>6. Delete vs Truncate vs Drop?</b></summary>

DELETE: row-level, logged, filterable. TRUNCATE: fast, removes all rows. DROP: removes the table.

</details>

<details>
<summary><b>7. How do indexes work / when do they hurt?</b></summary>

B-tree speeds reads; slow writes and use storage; ineffective on low-cardinality columns or with functions on the column.

</details>

<details>
<summary><b>8. How do you optimize a slow query?</b></summary>

Read the execution plan, add/adjust indexes, avoid `SELECT *`, filter early, avoid functions on indexed columns, reduce joins, check stats.

</details>

<details>
<summary><b>9. Running total / moving average?</b></summary>

`SUM(x) OVER (ORDER BY d ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)`.

</details>

<details>
<summary><b>10. Consecutive days / gaps and islands?</b></summary>

`date - ROW_NUMBER()` grouping trick.

</details>

<details>
<summary><b>11. NULL handling?</b></summary>

`NULL = NULL` is unknown; use `IS NULL`; aggregates ignore NULLs except `COUNT(*)`.

</details>

<details>
<summary><b>12. ACID and isolation levels?</b></summary>

Read uncommitted → read committed → repeatable read → serializable (prevents dirty, non-repeatable, phantom reads).

</details>

---

## 🔄 4. ETL

#### 📌 Key points
- **ETL:** transform before loading (traditional, warehouse). **ELT:** load raw first, transform in the warehouse/lake (modern, cheap storage + compute).
- Batch vs streaming; full load vs **incremental** (watermark, CDC).
- Orchestration: Airflow, ADF, Step Functions, Dagster; transformations: dbt, Spark.
- Concerns: idempotency, retries, schema evolution, data quality, lineage, monitoring.

#### ❓ Questions
<details>
<summary><b>1. ETL vs ELT?</b></summary>

ETL transforms in a separate engine before load; ELT loads raw then transforms in-target. ELT is the norm with cloud warehouses/lakes.

</details>

<details>
<summary><b>2. Full vs incremental load?</b></summary>

Full reloads everything; incremental loads only new/changed rows (timestamp watermark, CDC, hash compare).

</details>

<details>
<summary><b>3. What is CDC?</b></summary>

Change Data Capture: reading DB logs (Debezium, DMS) to stream inserts/updates/deletes.

</details>

<details>
<summary><b>4. How do you make a pipeline idempotent?</b></summary>

Overwrite partitions, use `MERGE`/upserts, deterministic keys, avoid append-only duplicates.

</details>

<details>
<summary><b>5. How do you handle late-arriving data?</b></summary>

Watermarks, reprocessing windows, partition overwrite, event-time vs processing-time.

</details>

<details>
<summary><b>6. Data quality checks?</b></summary>

Row counts, null/uniqueness checks, schema validation, freshness, Great Expectations/dbt tests, quarantine bad records.

</details>

<details>
<summary><b>7. How do you handle schema changes?</b></summary>

Schema registry, permissive/evolving formats (Parquet/Avro/Delta), alert on drift.

</details>

<details>
<summary><b>8. Backfills?</b></summary>

Parameterize by date, rerun partitions, ensure idempotency.

</details>

<details>
<summary><b>9. Batch vs streaming?</b></summary>

Batch: simpler, high throughput, latency in minutes+. Streaming: low latency, complexity (state, ordering, exactly-once).

</details>

<details>
<summary><b>10. Airflow concepts?</b></summary>

DAG, tasks, operators, schedule, sensors, XComs, retries, backfill/catchup.

</details>

<details>
<summary><b>11. SCD handling in pipelines?</b></summary>

Type 2 via `MERGE` with effective dates/current flag.

</details>

---

## 📐 5. Data Modeling

#### 📌 Key points
- **OLTP:** normalized (3NF), many small transactions. **OLAP:** denormalized/dimensional, large scans.
- **Normal forms:** 1NF atomic values, 2NF no partial dependency, 3NF no transitive dependency.
- **Dimensional modeling (Kimball):** **fact** tables (measures, FKs) + **dimension** tables (descriptive context).
- Schemas: **Star** (denormalized dims) vs **Snowflake** (normalized dims).
- Grain: the level of detail of a fact row; define it first.

#### ❓ Questions
<details>
<summary><b>1. Fact vs dimension?</b></summary>

Fact: numeric events (sales amount), large, grows fast. Dimension: descriptive attributes (customer, product, date), smaller.

</details>

<details>
<summary><b>2. Star vs snowflake?</b></summary>

Star: fewer joins, faster queries, some redundancy. Snowflake: less redundancy, more joins.

</details>

<details>
<summary><b>3. What is grain?</b></summary>

What one row represents (one order line per day). Mixing grains causes wrong aggregates.

</details>

<details>
<summary><b>4. SCD types?</b></summary>

Type 1 overwrite; Type 2 new row with history (start/end date, current flag); Type 3 extra column for previous value.

</details>

<details>
<summary><b>5. Surrogate vs natural key?</b></summary>

Surrogate: system-generated, stable, decoupled from source. Natural: business key, may change.

</details>

<details>
<summary><b>6. Fact table types?</b></summary>

Transactional, periodic snapshot, accumulating snapshot, factless.

</details>

<details>
<summary><b>7. Normalize or denormalize?</b></summary>

Normalize for OLTP integrity; denormalize for analytics read speed.

</details>

<details>
<summary><b>8. Data Vault?</b></summary>

Hubs (keys), links (relationships), satellites (attributes); good for auditability and agile integration.

</details>

<details>
<summary><b>9. Many-to-many relationships?</b></summary>

Bridge/junction table.

</details>

<details>
<summary><b>10. Conformed dimensions?</b></summary>

Shared dimensions (e.g., date, customer) used across fact tables for cross-process analysis.

</details>

<details>
<summary><b>11. Design a model for e-commerce.</b></summary>

Facts: order_lines, payments. Dims: customer, product, date, store/channel, promotion.

</details>

---

## 🏢 6. Data Warehousing

#### 📌 Key points
- Central, curated, structured store for analytics; **schema-on-write**; subject-oriented, integrated, time-variant.
- Cloud options: Snowflake, Redshift, BigQuery, Synapse, Databricks SQL.
- Architecture layers: staging → core (integrated) → marts (business-specific).
- Columnar storage, MPP (massively parallel processing), compression, partitioning/clustering.
- Snowflake: separate compute (virtual warehouses) and storage; Redshift: distribution/sort keys; BigQuery: serverless, partition/cluster.

#### ❓ Questions
<details>
<summary><b>1. Data warehouse vs database?</b></summary>

Warehouse is OLAP, historical, read-heavy, denormalized. Operational DB is OLTP, current, write-heavy.

</details>

<details>
<summary><b>2. Warehouse vs lake vs lakehouse?</b></summary>

Warehouse: structured, schema-on-write. Lake: raw, any format, schema-on-read. Lakehouse: lake storage + ACID/warehouse features (Delta, Iceberg, Hudi).

</details>

<details>
<summary><b>3. Why columnar storage?</b></summary>

Reads only needed columns, compresses well, great for aggregations.

</details>

<details>
<summary><b>4. What is MPP?</b></summary>

Work split across nodes that process data slices in parallel.

</details>

<details>
<summary><b>5. Data mart?</b></summary>

Subject-specific subset of the warehouse (finance, marketing).

</details>

<details>
<summary><b>6. Inmon vs Kimball?</b></summary>

Inmon: top-down, enterprise normalized warehouse first. Kimball: bottom-up, dimensional marts.

</details>

<details>
<summary><b>7. How do you optimize warehouse queries?</b></summary>

Partition/cluster/sort keys, avoid `SELECT *`, pre-aggregate, materialized views, right-size compute, prune data.

</details>

<details>
<summary><b>8. Snowflake basics?</b></summary>

Micro-partitions, virtual warehouses, time travel, zero-copy clone, separate storage and compute.

</details>

<details>
<summary><b>9. Data skew / distribution?</b></summary>

Choose distribution keys that spread evenly (Redshift) to avoid hot nodes.

</details>

<details>
<summary><b>10. How do you control cost?</b></summary>

Auto-suspend compute, partition pruning, retention policies, monitor expensive queries.

</details>

---

## ⚡ 7. Apache Spark

#### 📌 Key points
- Distributed engine: **Driver** coordinates, **Executors** run tasks across a cluster (YARN, K8s, standalone, Databricks).
- APIs: RDD (low-level), **DataFrame/Dataset** (optimized via Catalyst + Tungsten), Spark SQL, Structured Streaming, MLlib.
- **Lazy evaluation:** transformations build a DAG; **actions** (`count`, `collect`, `write`) trigger execution.
- **Narrow** transformations (map, filter) vs **wide** (groupBy, join) that cause a **shuffle** (stage boundary).
- Hierarchy: Application → Job → Stage → Task (one task per partition).

#### ❓ Questions
<details>
<summary><b>1. Transformation vs action?</b></summary>

Transformations are lazy (return a new DF); actions trigger computation and return/write results.

</details>

<details>
<summary><b>2. Narrow vs wide transformation?</b></summary>

Narrow: no data movement between partitions. Wide: shuffle across the network (expensive).

</details>

<details>
<summary><b>3. RDD vs DataFrame?</b></summary>

DataFrame has schema and Catalyst optimizer; faster and preferred. RDD is low-level and unoptimized.

</details>

<details>
<summary><b>4. `repartition` vs `coalesce`?</b></summary>

`repartition` does a full shuffle (increase or decrease, even sizes). `coalesce` only decreases partitions, no full shuffle.

</details>

<details>
<summary><b>5. What is a shuffle and how do you reduce it?</b></summary>

Redistribution of data by key. Reduce with broadcast joins, pre-partitioning, filtering early, `reduceByKey` over `groupByKey`.

</details>

<details>
<summary><b>6. Broadcast join?</b></summary>

Ship the small table to all executors to avoid shuffling the big one (`broadcast(df)`, default threshold 10 MB).

</details>

<details>
<summary><b>7. How do you handle data skew?</b></summary>

Salting keys, AQE skew join handling, broadcast, repartition by better key.

</details>

<details>
<summary><b>8. `cache` vs `persist`?</b></summary>

`cache` = persist with default storage level; `persist` lets you choose (MEMORY_AND_DISK, etc.). Use when a DF is reused.

</details>

<details>
<summary><b>9. What is Catalyst?</b></summary>

Query optimizer: logical plan → optimized plan (predicate pushdown, column pruning) → physical plan.

</details>

<details>
<summary><b>10. What is AQE?</b></summary>

Adaptive Query Execution: re-optimizes at runtime (coalesce shuffle partitions, switch join strategy, skew handling).

</details>

<details>
<summary><b>11. Spark Structured Streaming?</b></summary>

Treats streams as unbounded tables; micro-batch (or continuous); watermarks for late data; checkpoints for fault tolerance; exactly-once with idempotent sinks.

</details>

<details>
<summary><b>12. How do you debug OOM / slow jobs?</b></summary>

Spark UI (stages, skew, spill), tune `spark.executor.memory`, `spark.sql.shuffle.partitions`, avoid `collect()`, check partition sizes.

</details>

<details>
<summary><b>13. Fault tolerance?</b></summary>

Lineage lets lost partitions be recomputed; checkpointing for streaming.

</details>

<details>
<summary><b>14. File formats?</b></summary>

Prefer columnar **Parquet**/ORC (compression, predicate pushdown); Avro for row-based/streaming; avoid many small files.

</details>

<details>
<summary><b>15. UDF downsides?</b></summary>

Opaque to Catalyst and slow (esp. Python); prefer built-in functions or pandas UDFs.

</details>

---

## 🧱 8. Databricks

#### 📌 Key points
- Managed platform built by Spark's creators; runs on AWS/Azure/GCP.
- **Delta Lake:** open storage layer on Parquet adding **ACID transactions, schema enforcement/evolution, time travel, MERGE/upserts**.
- **Lakehouse:** warehouse reliability + lake flexibility on one copy of data.
- **Medallion architecture:** Bronze (raw) → Silver (cleaned/conformed) → Gold (business aggregates).
- Components: Notebooks, Jobs/Workflows, Clusters (all-purpose vs job), SQL Warehouses, **Unity Catalog** (governance), Delta Live Tables / Lakeflow, Auto Loader, MLflow.

#### ❓ Questions
<details>
<summary><b>1. What is Delta Lake and why use it?</b></summary>

ACID, versioning, upserts, schema enforcement on a data lake; fixes the "data swamp" problem.

</details>

<details>
<summary><b>2. Medallion architecture?</b></summary>

Bronze raw ingest, Silver cleaned and deduped, Gold aggregated for BI/ML.

</details>

<details>
<summary><b>3. Time travel?</b></summary>

Query older versions (`VERSION AS OF` / `TIMESTAMP AS OF`), restore, audit.

</details>

<details>
<summary><b>4. How do you upsert?</b></summary>

`MERGE INTO target USING source ON key WHEN MATCHED THEN UPDATE WHEN NOT MATCHED THEN INSERT`.

</details>

<details>
<summary><b>5. `OPTIMIZE`, `ZORDER`, `VACUUM`?</b></summary>

OPTIMIZE compacts small files; ZORDER co-locates data for filter columns; VACUUM removes old unreferenced files (mind retention for time travel). Liquid clustering is the newer alternative to partitioning/ZORDER.

</details>

<details>
<summary><b>6. What is Unity Catalog?</b></summary>

Central governance: catalog → schema → table hierarchy, access control, lineage, auditing.

</details>

<details>
<summary><b>7. Auto Loader?</b></summary>

Incrementally and efficiently ingests new files from cloud storage with schema inference/evolution (`cloudFiles`).

</details>

<details>
<summary><b>8. All-purpose vs job clusters?</b></summary>

All-purpose: interactive/dev, costlier. Job clusters: ephemeral per run, cheaper for production.

</details>

<details>
<summary><b>9. Delta Live Tables (DLT)?</b></summary>

Declarative pipelines with built-in quality expectations, dependency handling, and auto-scaling.

</details>

<details>
<summary><b>10. How do you do incremental processing?</b></summary>

Auto Loader, Structured Streaming with checkpoints, Change Data Feed, `MERGE`.

</details>

<details>
<summary><b>11. Databricks vs plain Spark?</b></summary>

Managed infra, Delta, collaboration, governance, optimized runtime (Photon), job orchestration.

</details>

<details>
<summary><b>12. Delta vs Parquet?</b></summary>

Delta = Parquet files + transaction log (`_delta_log`) giving ACID, versioning, and metadata handling.

</details>

---

## 🗄 9. SQL Databases (Relational)

#### 📌 Key points
- Tables, rows, fixed schema, relationships via PK/FK; **ACID** transactions.
- Engines: PostgreSQL, MySQL, SQL Server, Oracle, Aurora.
- Scaling: vertical, read replicas, partitioning (declarative), sharding (hard), caching.
- Indexes: B-tree, hash, composite, covering, clustered vs non-clustered.

#### ❓ Questions
<details>
<summary><b>1. ACID?</b></summary>

Atomicity (all or nothing), Consistency (valid state), Isolation (concurrent txns don't interfere), Durability (committed = persisted).

</details>

<details>
<summary><b>2. Clustered vs non-clustered index?</b></summary>

Clustered defines physical row order (one per table); non-clustered is a separate structure pointing to rows.

</details>

<details>
<summary><b>3. Normalization trade-offs?</b></summary>

Less redundancy and better integrity, but more joins.

</details>

<details>
<summary><b>4. What is a transaction deadlock?</b></summary>

Two transactions hold locks the other needs; DB aborts one. Prevent with consistent lock order and short transactions.

</details>

<details>
<summary><b>5. Primary vs foreign vs unique key?</b></summary>

PK uniquely identifies rows (not null); FK references another table; unique enforces uniqueness (allows NULL).

</details>

<details>
<summary><b>6. Partitioning vs sharding?</b></summary>

Partitioning splits a table within one DB; sharding spreads data across multiple DB servers.

</details>

<details>
<summary><b>7. How do you scale reads/writes?</b></summary>

Reads: replicas, cache. Writes: vertical scale, sharding, queueing/batching.

</details>

<details>
<summary><b>8. MVCC?</b></summary>

Multi-version concurrency control: readers see snapshots, don't block writers (Postgres, MySQL InnoDB).

</details>

<details>
<summary><b>9. OLTP vs OLAP databases?</b></summary>

OLTP: row-store, short transactions. OLAP: columnar, large scans.

</details>

<details>
<summary><b>10. Stored procedures, views, materialized views?</b></summary>

Reusable logic on server; virtual query; precomputed stored results (need refresh).

</details>

---

## 🗄 10. NoSQL Databases

#### 📌 Key points
- Flexible schema, horizontal scale, often **BASE** / eventual consistency.
- **Types:**
  - **Key-value:** Redis, DynamoDB: caching, sessions.
  - **Document:** MongoDB, Couchbase: JSON-like records, catalogs.
  - **Wide-column:** Cassandra, HBase: time-series, huge write throughput.
  - **Graph:** Neo4j: relationships (see section 12).
- **CAP theorem:** under a partition you choose Consistency or Availability (CP vs AP).

#### ❓ Questions
<details>
<summary><b>1. SQL vs NoSQL?</b></summary>

SQL: structure, joins, ACID. NoSQL: scale-out, flexible schema, specific access patterns, often eventual consistency.

</details>

<details>
<summary><b>2. CAP theorem?</b></summary>

A distributed system can guarantee only two of Consistency, Availability, Partition tolerance; P is mandatory, so choose CP or AP.

</details>

<details>
<summary><b>3. ACID vs BASE?</b></summary>

BASE: Basically Available, Soft state, Eventually consistent.

</details>

<details>
<summary><b>4. When to choose MongoDB?</b></summary>

Evolving JSON documents, flexible schema, developer velocity; avoid heavy multi-document joins.

</details>

<details>
<summary><b>5. How does Cassandra work?</b></summary>

Masterless ring, consistent hashing, tunable consistency (`ONE`/`QUORUM`/`ALL`), LSM-tree writes, query-first modeling.

</details>

<details>
<summary><b>6. How do you model data in NoSQL?</b></summary>

Start from queries/access patterns; denormalize; embed vs reference.

</details>

<details>
<summary><b>7. What is sharding?</b></summary>

Splitting data across nodes by a shard key; a bad key causes hot spots.

</details>

<details>
<summary><b>8. Redis use cases?</b></summary>

Cache, session store, rate limiting, leaderboards, pub/sub; in-memory with optional persistence.

</details>

<details>
<summary><b>9. Eventual consistency?</b></summary>

Replicas converge over time; reads may be stale temporarily.

</details>

<details>
<summary><b>10. Replication & quorum?</b></summary>

`R + W > N` ensures read-your-write consistency.

</details>

<details>
<summary><b>11. When NOT to use NoSQL?</b></summary>

Complex joins, multi-row transactions, ad hoc analytics.

</details>

---

## 🌊 11. Data Lake

#### 📌 Key points
- Stores **raw data in native format** (structured, semi-structured, unstructured) on cheap object storage (S3, ADLS, GCS).
- **Schema-on-read** vs warehouse schema-on-write.
- Zones: raw/landing → cleansed → curated.
- Formats: Parquet, ORC, Avro, JSON, CSV; table formats: **Delta, Iceberg, Hudi** (ACID, time travel, schema evolution).
- Catalog/metadata: Glue Data Catalog, Hive Metastore, Unity Catalog; query: Athena, Presto/Trino, Spark.
- Risk: **data swamp** without governance, metadata, and quality.

#### ❓ Questions
<details>
<summary><b>1. Data lake vs data warehouse?</b></summary>

Lake: raw, flexible, cheap, schema-on-read, ML-friendly. Warehouse: curated, structured, fast BI, schema-on-write.

</details>

<details>
<summary><b>2. What is a lakehouse?</b></summary>

Lake storage with warehouse features (ACID, governance, BI performance) via Delta/Iceberg/Hudi.

</details>

<details>
<summary><b>3. Why Parquet?</b></summary>

Columnar, compressed, splittable, supports predicate pushdown and schema evolution.

</details>

<details>
<summary><b>4. How do you partition lake data?</b></summary>

By frequently filtered columns (date); avoid over-partitioning (too many small files).

</details>

<details>
<summary><b>5. Small files problem?</b></summary>

Many tiny files slow reads/metadata; fix with compaction (`OPTIMIZE`), larger batch sizes, auto-compaction.

</details>

<details>
<summary><b>6. How do you prevent a data swamp?</b></summary>

Catalog and metadata, naming conventions, quality checks, ownership, lifecycle policies, governance.

</details>

<details>
<summary><b>7. Delta vs Iceberg vs Hudi?</b></summary>

All add ACID/time travel on object storage. Delta: Databricks-native; Iceberg: engine-agnostic, hidden partitioning; Hudi: strong upserts/streaming ingestion.

</details>

<details>
<summary><b>8. How do you secure a lake?</b></summary>

IAM/bucket policies, encryption, column/row-level security, Lake Formation/Unity Catalog, auditing.

</details>

<details>
<summary><b>9. How do you query a lake without a cluster?</b></summary>

Athena / Trino / serverless SQL over external tables.

</details>

<details>
<summary><b>10. Handling PII?</b></summary>

Masking, tokenization, column-level access, separate zones, retention/deletion (GDPR).

</details>

---

## 🕸 12. Graph Databases

#### 📌 Key points
- Store **nodes** (entities), **edges** (relationships), and **properties**; relationships are first-class.
- **Property graph** (Neo4j, Neptune, TigerGraph) vs **RDF/triple store**.
- Query languages: **Cypher** (Neo4j), Gremlin, SPARQL, openCypher.
- **Index-free adjacency:** traversal cost depends on the local neighborhood, not total data size.
- Use cases: fraud detection, recommendations, social networks, knowledge graphs, network/IT topology.

#### ❓ Questions
<details>
<summary><b>1. When graph over relational?</b></summary>

Deep, many-hop relationship queries where SQL would need many recursive self-joins.

</details>

<details>
<summary><b>2. What is a property graph?</b></summary>

Nodes and edges with labels/types and key-value properties.

</details>

<details>
<summary><b>3. Sample Cypher query?</b></summary>

`MATCH (a:Person)-[:FRIEND]->(b)-[:FRIEND]->(c) WHERE a.name='Ana' RETURN DISTINCT c.name`.

</details>

<details>
<summary><b>4. Why are graph traversals fast?</b></summary>

Direct pointers between nodes, no join computation.

</details>

<details>
<summary><b>5. Graph DB vs NoSQL document?</b></summary>

Document stores optimize per-record access; graph optimizes connected data traversal.

</details>

<details>
<summary><b>6. Limitations?</b></summary>

Harder to scale/shard horizontally, less suited for bulk aggregations and simple tabular lookups.

</details>

<details>
<summary><b>7. Fraud detection example?</b></summary>

Find accounts sharing devices/addresses/cards through connected components and shortest paths.

</details>

<details>
<summary><b>8. Graph algorithms?</b></summary>

PageRank, community detection, shortest path, centrality, connected components.

</details>

<details>
<summary><b>9. AWS option?</b></summary>

Amazon Neptune (supports Gremlin, openCypher, SPARQL).

</details>

<details>
<summary><b>10. Graph processing in Spark?</b></summary>

GraphFrames / GraphX for batch graph analytics on large data.

</details>

---

## 🧩 Cross-Technology / Scenario Questions

<details>
<summary><b>1. Design a batch data pipeline.</b></summary>

Source DB → CDC/ingest to S3 raw (bronze) → Spark/Databricks cleans and dedupes (silver) → aggregates into gold/warehouse → BI; orchestrate with Airflow, add quality checks and alerts.

</details>

<details>
<summary><b>2. Design a real-time pipeline.</b></summary>

Events → Kafka/Kinesis → Spark Structured Streaming/Flink → Delta/serving store (Redis/Druid) with watermarks and checkpoints.

</details>

<details>
<summary><b>3. Warehouse vs lake vs lakehouse?</b></summary>

Pick warehouse for BI-first, lake for raw/ML, lakehouse to unify both on one copy.

</details>

<details>
<summary><b>4. Which database for which job?</b></summary>

Transactions → SQL; massive key lookups → DynamoDB/Cassandra; flexible docs → MongoDB; relationships → Graph; analytics → warehouse.

</details>

<details>
<summary><b>5. A Spark job is slow. What do you do?</b></summary>

Spark UI → find skewed or long stages → fix joins (broadcast), partitions, caching, file sizes, formats, AQE.

</details>

<details>
<summary><b>6. How do you handle duplicates and late data?</b></summary>

Idempotent writes, `MERGE` on business keys, watermarks, dedupe with `ROW_NUMBER`.

</details>

<details>
<summary><b>7. How do you ensure data quality?</b></summary>

Tests at ingest and transform (dbt/Great Expectations/DLT expectations), freshness SLAs, lineage, quarantine tables, alerts.

</details>

<details>
<summary><b>8. How do you design a slowly changing dimension in Spark/Delta?</b></summary>

`MERGE` with effective dates and `is_current` flag (SCD2).

</details>

<details>
<summary><b>9. How do you handle PII and compliance?</b></summary>

Encryption, masking, access control via Unity Catalog, audit logs, retention/deletion.

</details>

<details>
<summary><b>10. How do you control cost?</b></summary>

Auto-terminating clusters, job clusters, spot instances, partition pruning, file compaction, lifecycle policies.

</details>

<details>
<summary><b>11. Migrate an on-prem warehouse to the cloud?</b></summary>

Assess/inventory, choose target (lakehouse/warehouse), land data in object storage, replicate with CDC, validate with reconciliation, cut over incrementally.

</details>

---

## 🎯 Core Concepts to Know Cold

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

---

<p align="center">

[All Topics](All-Topics-Overview.md) · [AWS](AWS-Overview.md) · **Data** · [Spring Boot](Frameworks-Overview.md) · [DevOps](DevOps-Overview.md) · [Practices](Practices-Overview.md) · [Gen AI](GenAI-Overview.md)

</p>
