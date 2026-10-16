# High-Level Overview of All Topics

One-page map for quick review. Details live in the per-topic files: [Data-Overview.md](Data-Overview.md) · [Frameworks-Overview.md](Frameworks-Overview.md) · [AWS-Overview.md](AWS-Overview.md) · [DevOps-Overview.md](DevOps-Overview.md) · [Practices-Overview.md](Practices-Overview.md) · [GenAI-Overview.md](GenAI-Overview.md)

---

## The Big Picture

Build and operate **data-driven, API-backed systems on AWS**: ingest and transform large datasets, store them in the right database, expose them through **Spring Boot REST APIs**, ship them through **CI/CD** with **TDD** and **security by design**, and add **Gen AI/agentic** capabilities on top.

```
Sources → Ingest (CDC/Kafka/Kinesis) → Data Lake (S3) → Spark/Databricks ETL → Warehouse / NoSQL / Graph
                                                                         ↓
Client → API Gateway → Spring Boot (ECS) / Lambda → DBs ←→ RAG / Agents (LLM + tools)
                                   ↑
              Git → Jenkins CI/CD → tests, scans, deploy → monitor
```

---

## Topic Map

| Area | Topics | One-line takeaway | File |
|---|---|---|---|
| **Languages** | Java | JVM, OOP, collections, concurrency; Spark/Kafka run on it | Data |
| | Python | Pipelines and PySpark; GIL, generators, pandas vs Spark | Data |
| | SQL | Joins, window functions, CTEs, indexes, query tuning | Data |
| **Frameworks** | Spring Boot | Auto-config, DI, REST controllers, JPA, Security, Actuator, tests | Frameworks |
| **Data** | ETL | ETL vs ELT, incremental/CDC, idempotency, data quality | Data |
| | Data Modeling | Normalization (OLTP) vs star/snowflake (OLAP), grain, SCD | Data |
| | Data Warehousing | Columnar, MPP, schema-on-write, marts (Snowflake/Redshift/BigQuery) | Data |
| | Apache Spark | Lazy DAG, shuffle, partitions, broadcast joins, skew, AQE | Data |
| | Databricks | Delta Lake (ACID, time travel, MERGE), medallion, Unity Catalog | Data |
| | SQL DB | ACID, indexes, transactions, replicas, partitioning | Data |
| | NoSQL DB | KV/document/wide-column; CAP, BASE, access-pattern modeling | Data |
| | Data Lake | Raw files on object storage, Parquet, lakehouse (Delta/Iceberg/Hudi) | Data |
| | Graph DB | Nodes and edges, Cypher/Gremlin, multi-hop queries, Neptune | Data, AWS |
| **Cloud (AWS)** | Lambda | Serverless, event-driven, cold starts, 15-min limit | AWS |
| | RDS | Managed relational; Multi-AZ vs read replicas; Aurora; RDS Proxy | AWS |
| | ECS | Containers on Fargate/EC2; task def, service, roles | AWS |
| | DynamoDB | Key-based NoSQL; partition key design, GSI/LSI, streams | AWS |
| | API Gateway | REST/HTTP APIs, authorizers, throttling, 29 s timeout | AWS |
| | S3 | Object storage, storage classes, lifecycle, presigned URLs | AWS |
| | Data & AI services | Glue, Athena, Redshift, Kinesis, Step Functions, Neptune, Bedrock | AWS |
| **DevOps** | Git | Merge vs rebase, reset vs revert, branching strategies | DevOps |
| | Jenkins | Jenkinsfile, declarative pipelines, agents, credentials | DevOps |
| | CI/CD | Build once deploy many, blue/green, canary, rollback | DevOps |
| | Lean | Eliminate waste, small batches, WIP limits, fast feedback | DevOps |
| **Practices** | TDD | Red-Green-Refactor, test pyramid, mocks vs stubs | Practices |
| | Agile/Scrum | Roles, events, Definition of Done, velocity, user stories | Practices |
| | Pair programming | Driver/navigator, ping-pong, remote pairing | Practices |
| | Code reviews | Small PRs, constructive feedback, automate the trivial | Practices |
| | Security by Design | Least privilege, defense in depth, threat modeling, OWASP | Practices |
| **Emerging** | Gen AI | Tokens, context window, prompting, hallucination, RAG | GenAI |
| | Agentic patterns | Tool calling, ReAct, workflows vs agents, MCP, guardrails, evals | GenAI |

---

## 60-Second Answers

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

## How the Pieces Connect (Story for "Tell me about a system you'd build")

1. **Ingest** data via CDC/streams into an **S3 data lake** (Parquet/Delta).
2. **Transform** with Spark/Databricks (bronze → silver → gold), with data quality checks.
3. **Model** curated data in a star-schema warehouse; serve operational lookups from DynamoDB; relationships from Neptune.
4. **Expose** it through a **Spring Boot REST API** (ECS or Lambda behind API Gateway) with JWT auth.
5. **Add Gen AI:** RAG over documents/data (vector search) and an agent that calls the API as tools, with guardrails and evals.
6. **Ship** with Git + Jenkins CI/CD: TDD, code reviews, security scans, blue/green deploys, monitoring.
7. **Work** in Agile sprints with lean flow: small PRs, pairing, retros, continuous improvement.

---

## Last-Minute Checklist

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
