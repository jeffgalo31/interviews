# AWS Interview Cheat Sheet

*Lambda · RDS · ECS · DynamoDB · API Gateway · S3 · Data & AI services (Glue, Athena, Redshift, Kinesis, Neptune, Bedrock)*

**Jump to:** [All Topics](All-Topics-Overview.md) · **AWS** · [Data](Data-Overview.md) · [Spring Boot](Frameworks-Overview.md) · [DevOps](DevOps-Overview.md) · [Practices](Practices-Overview.md) · [Gen AI](GenAI-Overview.md)

> [!TIP]
> Click any question to expand the answer. Try answering out loud first.

<details>
<summary><b>📑 Table of contents</b></summary>

1. [🧭 Quick Overview](#-quick-overview)
2. [⚡ 1. Lambda](#-1-lambda)
3. [🛢 2. RDS](#-2-rds)
4. [🐳 3. ECS](#-3-ecs)
5. [⚙ 4. DynamoDB](#-4-dynamodb)
6. [🚪 5. API Gateway](#-5-api-gateway)
7. [🪣 6. S3](#-6-s3)
8. [🤖 7. AWS Data & AI Services (Extension)](#-7-aws-data--ai-services-extension)
9. [🧩 Cross-Service / Scenario Questions](#-cross-service--scenario-questions)
10. [🎯 Core Concepts to Know Cold](#-core-concepts-to-know-cold)

</details>

---

## 🧭 Quick Overview

| Service | What it is | Type | Use it for |
|---|---|---|---|
| **Lambda** | Serverless functions, pay per invocation | Compute | Event-driven code, glue logic, small APIs |
| **RDS** | Managed relational DB (MySQL, Postgres, etc.) | Database (SQL) | Transactional apps needing joins/ACID |
| **ECS** | Managed container orchestrator (EC2 or Fargate) | Compute | Long-running services, microservices |
| **DynamoDB** | Managed NoSQL key-value/document DB | Database (NoSQL) | Low-latency, massive scale, simple access patterns |
| **API Gateway** | Managed front door for APIs | Networking/API | Expose Lambda/ECS/HTTP backends as REST/HTTP/WebSocket APIs |
| **S3** | Object storage (11 9s durability) | Storage | Files, static sites, backups, data lakes |

**Typical architecture:** Client → API Gateway → Lambda → DynamoDB/RDS, with S3 for files and ECS for heavier long-running services.

---

## ⚡ 1. Lambda

#### 📌 Key points
- Runs code in response to events (API Gateway, S3, SQS, SNS, DynamoDB Streams, EventBridge).
- Max timeout **15 min**; memory 128 MB–10 GB (CPU scales with memory).
- Stateless; local storage in `/tmp` (up to 10 GB) is ephemeral.
- Concurrency: default 1,000/region (account), can set reserved/provisioned concurrency.
- Execution role (IAM) controls what it can access.

#### ❓ Questions
<details>
<summary><b>1. What is a cold start and how do you reduce it?</b></summary>

New execution environment init. Reduce with provisioned concurrency, smaller packages, lighter runtimes, avoiding VPC overhead (less of an issue now), SnapStart (Java).

</details>

<details>
<summary><b>2. Lambda vs ECS/Fargate?</b></summary>

Lambda: short, spiky, event-driven. ECS: long-running, steady load, custom runtime, >15 min.

</details>

<details>
<summary><b>3. Sync vs async invocation?</b></summary>

Sync (API Gateway) returns result, caller handles errors. Async (S3, SNS) is queued with automatic retries (2) and DLQ/destinations.

</details>

<details>
<summary><b>4. How do you handle failures?</b></summary>

Retries, DLQ (SQS/SNS), on-failure destinations, idempotent handlers.

</details>

<details>
<summary><b>5. Reserved vs provisioned concurrency?</b></summary>

Reserved = guaranteed/capped capacity. Provisioned = pre-warmed instances (no cold start, costs more).

</details>

<details>
<summary><b>6. How to access RDS from Lambda?</b></summary>

Place in VPC; use **RDS Proxy** to pool connections and avoid exhausting DB connections.

</details>

<details>
<summary><b>7. What are layers?</b></summary>

Shared libraries/dependencies packaged separately from function code.

</details>

<details>
<summary><b>8. How do you manage secrets/config?</b></summary>

Environment variables (KMS encrypted), Secrets Manager, SSM Parameter Store.

</details>

---

## 🛢 2. RDS

#### 📌 Key points
- Managed engines: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Aurora.
- AWS handles patching, backups, failover, replication; you can't SSH into the host.
- **Multi-AZ** = high availability (synchronous standby, automatic failover).
- **Read replicas** = read scaling (asynchronous), can be cross-region.
- Automated backups (point-in-time restore, up to 35 days) + manual snapshots.

#### ❓ Questions
<details>
<summary><b>1. Multi-AZ vs Read Replica?</b></summary>

Multi-AZ: HA/failover, standby not readable. Read replica: performance, readable, async, can be promoted.

</details>

<details>
<summary><b>2. RDS vs Aurora?</b></summary>

Aurora: AWS-built, up to 5x MySQL / 3x Postgres perf, storage auto-scales to 128 TB, 6 copies across 3 AZs, faster failover; costs more.

</details>

<details>
<summary><b>3. RDS vs DynamoDB?</b></summary>

RDS: relational, joins, complex queries, ACID. DynamoDB: key-based access, scale, flexible schema.

</details>

<details>
<summary><b>4. How do you secure RDS?</b></summary>

Private subnets, security groups, encryption at rest (KMS) and in transit (SSL), IAM auth, Secrets Manager.

</details>

<details>
<summary><b>5. How to scale RDS?</b></summary>

Vertical (bigger instance), read replicas, caching (ElastiCache), Aurora Serverless.

</details>

<details>
<summary><b>6. What is RDS Proxy?</b></summary>

Connection pooling; essential for Lambda; improves failover time.

</details>

<details>
<summary><b>7. How do you recover from accidental deletion?</b></summary>

Point-in-time restore or snapshot restore (creates a new instance).

</details>

---

## 🐳 3. ECS

#### 📌 Key points
- Runs Docker containers. Concepts: **Cluster → Service → Task → Task Definition**.
- **Launch types:** EC2 (you manage instances) or **Fargate** (serverless, no servers to manage).
- Service keeps desired task count running; integrates with ALB, auto scaling.
- **Task role** (app permissions) vs **Task execution role** (pull image from ECR, write logs).
- Images stored in **ECR**.

#### ❓ Questions
<details>
<summary><b>1. ECS vs EKS?</b></summary>

ECS: simpler, AWS-native. EKS: managed Kubernetes, portable, more complex.

</details>

<details>
<summary><b>2. EC2 vs Fargate launch type?</b></summary>

Fargate: no infra management, pay per task. EC2: more control, cheaper at steady high scale, GPU/custom AMIs.

</details>

<details>
<summary><b>3. Task definition vs service?</b></summary>

Task def = blueprint (image, CPU/mem, ports, env). Service = maintains N running copies, handles deployment/load balancing.

</details>

<details>
<summary><b>4. How do you deploy with zero downtime?</b></summary>

Rolling update or blue/green (CodeDeploy) behind an ALB with health checks.

</details>

<details>
<summary><b>5. How does ECS scale?</b></summary>

Service Auto Scaling (target tracking on CPU/memory/ALB requests); for EC2 also capacity providers/cluster autoscaling.

</details>

<details>
<summary><b>6. Task role vs execution role?</b></summary>

See above.

</details>

<details>
<summary><b>7. How do containers talk to each other?</b></summary>

Service discovery (Cloud Map), Service Connect, or ALB; `awsvpc` mode gives each task its own ENI.

</details>

---

## ⚙ 4. DynamoDB

#### 📌 Key points
- Serverless NoSQL, single-digit ms latency, auto-scales.
- **Primary key:** Partition key (PK) or PK + Sort key (SK).
- Capacity modes: **On-demand** (unpredictable) or **Provisioned** (RCU/WCU, with auto scaling).
- **GSI** (different PK/SK, eventually consistent) vs **LSI** (same PK, different SK, must be created at table creation).
- Features: Streams, TTL, DAX (cache), Global Tables (multi-region), transactions.
- Item size limit **400 KB**.

#### ❓ Questions
<details>
<summary><b>1. Query vs Scan?</b></summary>

Query uses the key (efficient). Scan reads the entire table (slow, expensive; avoid).

</details>

<details>
<summary><b>2. GSI vs LSI?</b></summary>

See above. GSI can be added anytime, has its own throughput.

</details>

<details>
<summary><b>3. How do you choose a partition key?</b></summary>

High cardinality, even distribution, matches access patterns; avoids hot partitions.

</details>

<details>
<summary><b>4. Eventually vs strongly consistent reads?</b></summary>

Eventual (default, cheaper, 0.5 RCU) vs strong (latest data, 1 RCU, not on GSIs).

</details>

<details>
<summary><b>5. What is DynamoDB Streams used for?</b></summary>

Change data capture; trigger Lambda, replicate, audit.

</details>

<details>
<summary><b>6. How do you model data?</b></summary>

Start from access patterns; denormalize; single-table design.

</details>

<details>
<summary><b>7. When NOT to use DynamoDB?</b></summary>

Ad hoc queries, complex joins/aggregations, heavy relational needs.

</details>

<details>
<summary><b>8. How do you handle hot partitions?</b></summary>

Better key design, add random suffix/sharding, on-demand mode, DAX caching.

</details>

<details>
<summary><b>9. What is DAX?</b></summary>

In-memory write-through cache giving microsecond reads.

</details>

---

## 🚪 5. API Gateway

#### 📌 Key points
- Fully managed service to create, publish, secure, and monitor APIs.
- **Types:** REST API (full features), HTTP API (cheaper, faster, simpler), WebSocket API.
- Integrations: Lambda, HTTP endpoints, AWS services, VPC Link (private resources).
- **Auth:** IAM, Cognito authorizer, Lambda authorizer, JWT (HTTP API), API keys (+ usage plans).
- Features: throttling, caching (REST), stages, request/response transformation, CORS, custom domains, WAF integration.
- Limits: 29 sec integration timeout (default), 10 MB payload.

#### ❓ Questions
<details>
<summary><b>1. REST API vs HTTP API?</b></summary>

HTTP API: ~70% cheaper, lower latency, fewer features. REST API: caching, WAF, API keys/usage plans, request validation, more control.

</details>

<details>
<summary><b>2. How do you secure an API?</b></summary>

Cognito/JWT/Lambda authorizer, IAM, WAF, throttling, HTTPS, resource policies.

</details>

<details>
<summary><b>3. Lambda proxy vs non-proxy integration?</b></summary>

Proxy passes the entire request to Lambda and Lambda formats the response (simplest). Non-proxy uses mapping templates.

</details>

<details>
<summary><b>4. How do you handle rate limiting?</b></summary>

Throttling (account/stage/method level) and usage plans with API keys.

</details>

<details>
<summary><b>5. What are stages?</b></summary>

Named deployments (dev/prod) with their own settings and variables.

</details>

<details>
<summary><b>6. How do you handle CORS?</b></summary>

Enable on API Gateway and return correct headers from the backend.

</details>

<details>
<summary><b>7. What if the backend takes > 29 s?</b></summary>

Go async (SQS/Step Functions/WebSocket) and return a job ID.

</details>

---

## 🪣 6. S3

#### 📌 Key points
- Object storage in **buckets** (globally unique names); object max **5 TB**, multipart upload recommended > 100 MB.
- Strong read-after-write consistency.
- **Storage classes:** Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier Instant/Flexible/Deep Archive.
- Features: versioning, lifecycle rules, replication (CRR/SRR), event notifications, static website hosting, presigned URLs.
- **Security:** Block Public Access, bucket policies, IAM, ACLs (legacy), encryption (SSE-S3, SSE-KMS, SSE-C).

#### ❓ Questions
<details>
<summary><b>1. How do you secure an S3 bucket?</b></summary>

Block Public Access, least-privilege IAM/bucket policy, encryption, versioning + MFA delete, access logging, VPC endpoints.

</details>

<details>
<summary><b>2. What are presigned URLs?</b></summary>

Temporary URLs granting time-limited upload/download without AWS credentials.

</details>

<details>
<summary><b>3. Storage classes — when to use which?</b></summary>

Frequent: Standard. Unknown pattern: Intelligent-Tiering. Rare access: IA. Archive: Glacier.

</details>

<details>
<summary><b>4. How do you reduce cost over time?</b></summary>

Lifecycle rules to transition/expire objects.

</details>

<details>
<summary><b>5. Versioning vs replication?</b></summary>

Versioning keeps object history in one bucket; replication copies objects to another bucket/region (requires versioning).

</details>

<details>
<summary><b>6. How do you trigger processing on upload?</b></summary>

S3 Event Notifications → Lambda/SQS/SNS/EventBridge.

</details>

<details>
<summary><b>7. S3 as a file system?</b></summary>

No; it's flat object storage (prefixes only look like folders).

</details>

<details>
<summary><b>8. How do you serve a static site globally?</b></summary>

S3 + CloudFront (with OAC), HTTPS via ACM.

</details>

<details>
<summary><b>9. How do you upload large files?</b></summary>

Multipart upload, Transfer Acceleration.

</details>

---

## 🤖 7. AWS Data & AI Services (Extension)

#### 🗺 Quick map

| Service | What it is | Use it for |
|---|---|---|
| **Glue** | Serverless ETL + Data Catalog + crawlers | ETL jobs (Spark), schema discovery, metadata for the lake |
| **Athena** | Serverless SQL on S3 (Presto/Trino), pay per data scanned | Ad hoc queries on the data lake |
| **Redshift** | Columnar MPP data warehouse (+ Spectrum for S3, Serverless option) | BI/analytics on structured data |
| **Kinesis** | Streaming: Data Streams, Firehose (delivery), Managed Flink | Real-time ingestion and processing |
| **MSK** | Managed Kafka | Kafka-based event streaming |
| **EMR** | Managed Spark/Hadoop clusters (EC2, EKS, Serverless) | Big data processing with full control |
| **Lake Formation** | Governance layer for the lake (fine-grained access, tags) | Column/row-level security on S3 data |
| **Step Functions** | Serverless workflow orchestration (state machines) | Orchestrating Lambda/Glue/ECS, retries, long workflows |
| **DMS** | Database Migration Service (full load + CDC) | Migrating/replicating DBs into RDS, S3, Redshift |
| **Neptune** | Managed graph database (Gremlin, openCypher, SPARQL) | Relationship-heavy queries |
| **Bedrock** | Managed access to foundation models, Knowledge Bases (RAG), Agents, Guardrails | Gen AI and agentic apps on AWS |
| **SageMaker** | Build, train, and deploy ML models | Custom ML (training, endpoints, pipelines) |
| **OpenSearch** | Managed search/analytics, also vector search | Log search, full-text and RAG retrieval |
| **SQS / SNS / EventBridge** | Queue / pub-sub / event bus | Decoupling, fan-out, event-driven design |

**Typical data lake on AWS:** Sources → DMS/Kinesis/Firehose → **S3** (raw/curated, Parquet) → **Glue** (ETL + Catalog) → **Athena** / **Redshift Spectrum** / **Redshift** → BI (QuickSight); governed by **Lake Formation**, orchestrated by **Step Functions** or **MWAA** (managed Airflow).

### ▸ Amazon Neptune (Graph)

#### 📌 Key points
- Fully managed graph DB: query with **Gremlin** and **openCypher** (property graph) or **SPARQL** (RDF).
- Storage auto-scales to 128 TB, 6 copies across 3 AZs; up to 15 read replicas; Multi-AZ failover.
- Runs inside a **VPC** (no public endpoint); access via IAM auth, encryption at rest (KMS) and in transit (TLS).
- Options: **Neptune Database** (OLTP-style traversals), **Neptune Analytics** (in-memory graph analytics and vector search, GraphRAG), **Neptune ML** (GNN predictions via SageMaker).
- Bulk load from S3 (CSV/RDF); backups, point-in-time restore, snapshots.

#### ❓ Questions
<details>
<summary><b>1. When Neptune over RDS or DynamoDB?</b></summary>

Many-hop relationship queries (fraud rings, recommendations, knowledge graphs) that need heavy recursive joins in SQL and aren't key-based lookups.

</details>

<details>
<summary><b>2. Gremlin vs openCypher vs SPARQL?</b></summary>

Gremlin: imperative traversals. openCypher: declarative, SQL-like pattern matching. SPARQL: for RDF/semantic data.

</details>

<details>
<summary><b>3. How do you load data?</b></summary>

Neptune bulk loader from S3, or streams/DMS/Glue for ongoing ingestion.

</details>

<details>
<summary><b>4. How do you secure it?</b></summary>

Private subnets and security groups, IAM database auth, KMS encryption, TLS, VPC endpoints.

</details>

<details>
<summary><b>5. How does it scale?</b></summary>

Vertical instance sizing, up to 15 read replicas for reads, Serverless option; writes go through a single primary.

</details>

<details>
<summary><b>6. What is GraphRAG?</b></summary>

Combining graph relationships with vector search (Neptune Analytics + Bedrock Knowledge Bases) so retrieval follows connections, not just similarity.

</details>

<details>
<summary><b>7. Limitations?</b></summary>

Hard to shard writes horizontally, poor fit for bulk tabular aggregations; pick the right tool.

</details>

### ▸ Glue / Athena / Redshift

#### ❓ Questions
<details>
<summary><b>1. What is the Glue Data Catalog?</b></summary>

Central metadata store (databases, tables, schemas) used by Athena, Redshift Spectrum, EMR, and Glue; crawlers infer schemas.

</details>

<details>
<summary><b>2. Glue vs EMR?</b></summary>

Glue: serverless, less control, quick ETL. EMR: more control/tuning, custom frameworks, can be cheaper at steady large scale.

</details>

<details>
<summary><b>3. How do you cut Athena cost?</b></summary>

Parquet/ORC, partitioning, compression, query only needed columns, partition projection, workgroup limits (it charges per data scanned).

</details>

<details>
<summary><b>4. Athena vs Redshift?</b></summary>

Athena: ad hoc, serverless, S3-native. Redshift: consistent high-concurrency BI, complex joins, managed warehouse storage.

</details>

<details>
<summary><b>5. Redshift distribution/sort keys?</b></summary>

Dist key co-locates joined data to reduce shuffling (KEY, ALL, EVEN, AUTO); sort key speeds range-filtered scans.

</details>

<details>
<summary><b>6. Redshift Spectrum?</b></summary>

Query S3 external tables from Redshift without loading.

</details>

<details>
<summary><b>7. Kinesis Data Streams vs Firehose?</b></summary>

Streams: custom consumers, replay, shards. Firehose: managed delivery to S3/Redshift/OpenSearch with buffering, no consumers to write.

</details>

<details>
<summary><b>8. Kinesis vs SQS?</b></summary>

Kinesis: ordered, replayable stream with multiple consumers. SQS: queue where each message is processed by one consumer and deleted.

</details>

<details>
<summary><b>9. Step Functions vs Lambda chaining?</b></summary>

Step Functions give built-in retries, error handling, parallel/map states, and visibility; chaining Lambdas directly is brittle.

</details>

### ▸ Bedrock & AI on AWS

#### ❓ Questions
<details>
<summary><b>1. What is Bedrock?</b></summary>

Serverless API access to foundation models from multiple providers, with Knowledge Bases (managed RAG), Agents, Guardrails, and fine-tuning options, with data kept private in your account.

</details>

<details>
<summary><b>2. How do you build RAG on AWS?</b></summary>

S3 docs → Bedrock Knowledge Base (chunk + embed) → vector store (OpenSearch Serverless, Aurora pgvector, Neptune Analytics) → retrieval + model generation.

</details>

<details>
<summary><b>3. Bedrock Agents?</b></summary>

Managed agents that plan, call action groups (Lambda/OpenAPI tools), and query Knowledge Bases; alternatives are custom agents on Lambda/ECS using an SDK.

</details>

<details>
<summary><b>4. Bedrock Guardrails?</b></summary>

Configurable content filters, denied topics, PII redaction, and grounding checks applied to inputs and outputs.

</details>

<details>
<summary><b>5. Bedrock vs SageMaker?</b></summary>

Bedrock: consume/customize hosted foundation models. SageMaker: build, train, and host your own models end to end.

</details>

<details>
<summary><b>6. How do you secure Gen AI workloads on AWS?</b></summary>

IAM least privilege, VPC endpoints (PrivateLink), KMS, CloudTrail audit, Guardrails, no customer data used to train base models.

</details>

---

## 🧩 Cross-Service / Scenario Questions

<details>
<summary><b>1. Design a serverless REST API.</b></summary>

API Gateway → Lambda → DynamoDB; Cognito for auth; S3 for uploads; CloudWatch for logs.

</details>

<details>
<summary><b>2. Image upload & thumbnail pipeline?</b></summary>

Client uploads via presigned URL → S3 event → Lambda creates thumbnail → writes to S3 → metadata in DynamoDB.

</details>

<details>
<summary><b>3. SQL vs NoSQL on AWS?</b></summary>

RDS for relational/transactional; DynamoDB for scale, simple access patterns.

</details>

<details>
<summary><b>4. Lambda vs ECS vs EC2?</b></summary>

Lambda: event-driven, short. ECS/Fargate: containers, long-running. EC2: full control.

</details>

<details>
<summary><b>5. How do you make a system highly available?</b></summary>

Multi-AZ, load balancer, auto scaling, stateless services, replicas, S3/DynamoDB are inherently multi-AZ.

</details>

<details>
<summary><b>6. How do you secure the stack?</b></summary>

IAM least privilege, private subnets, VPC endpoints, KMS encryption, Secrets Manager, WAF, CloudTrail.

</details>

<details>
<summary><b>7. How do you monitor?</b></summary>

CloudWatch (metrics, logs, alarms), X-Ray (tracing), CloudTrail (audit).

</details>

<details>
<summary><b>8. How do you control cost?</b></summary>

Right-size, on-demand vs provisioned, S3 lifecycle, Fargate Spot, Savings Plans, budgets.

</details>

---

## 🎯 Core Concepts to Know Cold

- **IAM:** users, roles, policies; least privilege; roles over access keys.
- **VPC:** public vs private subnets, security groups (stateful) vs NACLs (stateless), NAT gateway, VPC endpoints.
- **Regions / AZs:** a Region has multiple isolated AZs; design for multi-AZ.
- **Shared responsibility model:** AWS secures the cloud; you secure what's in the cloud.
- **Well-Architected pillars:** Operational Excellence, Security, Reliability, Performance, Cost, Sustainability.
- **Related services:** CloudFront (CDN), SQS/SNS/EventBridge (messaging), Cognito (auth), CloudWatch (monitoring), CloudFormation/CDK (IaC), ElastiCache (cache).

---

**Jump to:** [All Topics](All-Topics-Overview.md) · **AWS** · [Data](Data-Overview.md) · [Spring Boot](Frameworks-Overview.md) · [DevOps](DevOps-Overview.md) · [Practices](Practices-Overview.md) · [Gen AI](GenAI-Overview.md)
