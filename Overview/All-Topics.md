# High-Level Overview of All Topics

*One-page map for quick review. Full details are in the per-topic sheets linked below.*

**Jump to:** [All Topics](All-Topics.md) · [AWS](AWS.md) · [Data](Data.md) · [Spring Boot](Frameworks.md) · [DevOps](DevOps.md) · [Practices](Practices.md) · [Gen AI](GenAI.md)

**Coding practice:** [Java exercises](../Code/java/) · [SQL exercises](../Code/sql/) · [React exercises](../Code/react/) (HackerRank-style, runnable in VS Code)

**Behavioral:** [Behavioral interview questions](../Behavior/Behavioral-Interview-Questions.md) (12 competencies, questions and probes, from a Staff Software Engineer guide)

**Technical practice:** [John Deere Data Enablement tracks](../Technical/John-Deere-Data-Enablement/README.md) (AWS, SQL, Spark, Java, Graph, Gen AI, DevOps, React)

<details>
<summary><b>📑 Table of contents</b></summary>

1. [🧭 The Big Picture](#-the-big-picture)
2. [🗺 Topic Map](#-topic-map)
3. [⏱ 60-Second Answers](#-60-second-answers)
4. [🔗 How the Pieces Connect (Story for "Tell me about a system you'd build")](#-how-the-pieces-connect-story-for-tell-me-about-a-system-youd-build)
5. [✅ Last-Minute Checklist](#-last-minute-checklist)

</details>

---

## 🧭 The Big Picture

Build and operate **data-driven, API-backed systems on AWS**: ingest and transform large datasets, store them in the right database, expose them through **Spring Boot REST APIs**, ship them through **CI/CD** with **TDD** and **security by design**, and add **Gen AI/agentic** capabilities on top.

```
Sources → Ingest (CDC/Kafka/Kinesis) → Data Lake (S3) → Spark/Databricks ETL → Warehouse / NoSQL / Graph
                                                                         ↓
Client → API Gateway → Spring Boot (ECS) / Lambda → DBs ←→ RAG / Agents (LLM + tools)
                                   ↑
              Git → Jenkins CI/CD → tests, scans, deploy → monitor
```

---

## 🗺 Topic Map

| Area | Topics | One-line takeaway | File |
|---|---|---|---|
| **Languages** | Java | JVM, OOP, collections, concurrency; Spark/Kafka run on it | [Data](Data.md) |
| | Python | Pipelines and PySpark; GIL, generators, pandas vs Spark | [Data](Data.md) |
| | SQL | Joins, window functions, CTEs, indexes, query tuning | [Data](Data.md) |
| **Frameworks** | Spring Boot | Auto-config, DI, REST controllers, JPA, Security, Actuator, tests | [Frameworks](Frameworks.md) |
| **Data** | ETL | ETL vs ELT, incremental/CDC, idempotency, data quality | [Data](Data.md) |
| | Data Modeling | Normalization (OLTP) vs star/snowflake (OLAP), grain, SCD | [Data](Data.md) |
| | Data Warehousing | Columnar, MPP, schema-on-write, marts (Snowflake/Redshift/BigQuery) | [Data](Data.md) |
| | Apache Spark | Lazy DAG, shuffle, partitions, broadcast joins, skew, AQE | [Data](Data.md) |
| | Databricks | Delta Lake (ACID, time travel, MERGE), medallion, Unity Catalog | [Data](Data.md) |
| | SQL DB | ACID, indexes, transactions, replicas, partitioning | [Data](Data.md) |
| | NoSQL DB | KV/document/wide-column; CAP, BASE, access-pattern modeling | [Data](Data.md) |
| | Data Lake | Raw files on object storage, Parquet, lakehouse (Delta/Iceberg/Hudi) | [Data](Data.md) |
| | Graph DB | Nodes and edges, Cypher/Gremlin, multi-hop queries, Neptune | [Data](Data.md), [AWS](AWS.md) |
| **Cloud (AWS)** | Lambda | Serverless, event-driven, cold starts, 15-min limit | [AWS](AWS.md) |
| | RDS | Managed relational; Multi-AZ vs read replicas; Aurora; RDS Proxy | [AWS](AWS.md) |
| | ECS | Containers on Fargate/EC2; task def, service, roles | [AWS](AWS.md) |
| | DynamoDB | Key-based NoSQL; partition key design, GSI/LSI, streams | [AWS](AWS.md) |
| | API Gateway | REST/HTTP APIs, authorizers, throttling, 29 s timeout | [AWS](AWS.md) |
| | S3 | Object storage, storage classes, lifecycle, presigned URLs | [AWS](AWS.md) |
| | Data & AI services | Glue, Athena, Redshift, Kinesis, Step Functions, Neptune, Bedrock | [AWS](AWS.md) |
| **DevOps** | Git | Merge vs rebase, reset vs revert, branching strategies | [DevOps](DevOps.md) |
| | Jenkins | Jenkinsfile, declarative pipelines, agents, credentials | [DevOps](DevOps.md) |
| | CI/CD | Build once deploy many, blue/green, canary, rollback | [DevOps](DevOps.md) |
| | Lean | Eliminate waste, small batches, WIP limits, fast feedback | [DevOps](DevOps.md) |
| **Practices** | TDD | Red-Green-Refactor, test pyramid, mocks vs stubs | [Practices](Practices.md) |
| | Agile/Scrum | Roles, events, Definition of Done, velocity, user stories | [Practices](Practices.md) |
| | Pair programming | Driver/navigator, ping-pong, remote pairing | [Practices](Practices.md) |
| | Code reviews | Small PRs, constructive feedback, automate the trivial | [Practices](Practices.md) |
| | Security by Design | Least privilege, defense in depth, threat modeling, OWASP | [Practices](Practices.md) |
| **Emerging** | Gen AI | Tokens, context window, prompting, hallucination, RAG | [GenAI](GenAI.md) |
| | Agentic patterns | Tool calling, ReAct, workflows vs agents, MCP, guardrails, evals | [GenAI](GenAI.md) |

---

## ⏱ 60-Second Answers

- **ETL vs ELT:** ETL transforms before loading; ELT loads raw data and transforms in the warehouse/lake (modern default).
- **Warehouse vs lake vs lakehouse:** structured and curated vs raw and flexible vs both on one copy with ACID (Delta/Iceberg).
- **SQL vs NoSQL:** joins and ACID vs horizontal scale and flexible schema built around access patterns.
- **When a graph DB:** deep relationship traversals (fraud, recommendations, knowledge graphs).
- **Spark performance:** avoid shuffles, broadcast small tables, fix skew, use Parquet/Delta, tune partitions.
- **Spring Boot REST:** controller → service → repository, DTOs, validation, global error handler, JWT security.
- **Lambda vs ECS:** short, spiky, event-driven vs long-running, steady, containerized.
- **CI vs CD:** integrate and test every change vs automated (or one-click) release of every passing change.
- **TDD:** write a failing test, make it pass, refactor.
- **Security by design:** least privilege, defense in depth, secrets management, scanning in CI.
- **RAG vs fine-tuning:** retrieve fresh private knowledge at query time vs change model behavior or style.
- **Agent vs workflow:** the model chooses its own steps vs fixed code path; prefer the simplest that works.

---

## 🔗 How the Pieces Connect (Story for "Tell me about a system you'd build")

1. **Ingest** data via CDC/streams into an **S3 data lake** (Parquet/Delta).
2. **Transform** with Spark/Databricks (bronze → silver → gold), with data quality checks.
3. **Model** curated data in a star-schema warehouse; serve operational lookups from DynamoDB; relationships from Neptune.
4. **Expose** it through a **Spring Boot REST API** (ECS or Lambda behind API Gateway) with JWT auth.
5. **Add Gen AI:** RAG over documents/data (vector search) and an agent that calls the API as tools, with guardrails and evals.
6. **Ship** with Git + Jenkins CI/CD: TDD, code reviews, security scans, blue/green deploys, monitoring.
7. **Work** in Agile sprints with lean flow: small PRs, pairing, retros, continuous improvement.

---

## ✅ Last-Minute Checklist

- [ ] ACID vs BASE, CAP theorem, OLTP vs OLAP
- [ ] Star schema, grain, SCD types
- [ ] Spark: lazy evaluation, shuffle, broadcast join, skew
- [ ] Delta Lake and medallion architecture
- [ ] SQL window functions and a duplicate-removal query
- [ ] Spring Boot: DI, auto-config, N+1, `@Transactional`, JWT
- [ ] AWS: Lambda cold starts, DynamoDB key design, S3 classes, API Gateway limits
- [ ] Git rebase vs merge, Jenkinsfile structure, deployment strategies
- [ ] TDD cycle, Scrum events, Definition of Done
- [ ] OWASP Top 10, least privilege, threat modeling
- [ ] RAG pipeline, agent loop, tool calling, MCP, guardrails
- [ ] 2-3 STAR stories (conflict, failure, delivery under pressure)

---

**Jump to:** [All Topics](All-Topics.md) · [AWS](AWS.md) · [Data](Data.md) · [Spring Boot](Frameworks.md) · [DevOps](DevOps.md) · [Practices](Practices.md) · [Gen AI](GenAI.md)
