# John Deere Data Enablement: Technical Practice

A focused study set for the **Senior Software Engineer, OF/OM Data Enablement** role. Each exercise has its own Markdown file with a short prompt, solution, reasoning, complexity or design trade-offs, and source links.

The CI/CD exercise uses GitHub Actions and the AWS environment you described, including ECS and Lambda deployment considerations.

> HackerRank challenge statements are summarized rather than copied. Links point to the official challenge pages; sign-in may be required. Exercises labeled **Supplemental** are original practice tasks because HackerRank does not publish a matching standalone challenge for that technology.

## Study Tracks

| Track | Skills from the posting | Exercises |
|---|---|---|
| [Java Backend](Java-Backend/) | Java, collections, REST APIs, Spring Boot | [Comparator](Java-Backend/java-comparator.md) · [2D Array Sequences](Java-Backend/hackerrank-java-2d-array.md) · [Priority Queue](Java-Backend/java-priority-queue.md) · [Spring Boot REST API + TDD](Java-Backend/spring-boot-rest-products-api.md) |
| [SQL and Data Modeling](SQL-Data-Modeling/) | SQL, joins, aggregation, ETL reporting, warehousing, dimensional models | [Placements](SQL-Data-Modeling/hackerrank-placements.md) · [Interviews](SQL-Data-Modeling/hackerrank-interviews.md) · [Top Earners](SQL-Data-Modeling/hackerrank-top-earners.md) · [Star Schema](SQL-Data-Modeling/star-schema-sales.md) |
| [Python, Spark, and Databricks](Python-Spark-Databricks/) | Python, Apache Spark, Databricks, ETL, large datasets, data lakes | [Collections Counter](Python-Spark-Databricks/hackerrank-collections-counter.md) · [Bronze/Silver/Gold ETL](Python-Spark-Databricks/pyspark-bronze-silver-gold-etl.md) |
| [React Frontend](React-Frontend/) | React requested for your full-stack practice; **React is not listed in this job posting** | [Filterable Work Orders](React-Frontend/filterable-work-orders.md) · [HackerRank React Certification](https://www.hackerrank.com/skills-verification/frontend_developer_react) |
| [AWS Cloud](AWS-Cloud/) | Lambda, RDS, ECS, DynamoDB, API Gateway, S3, Security by Design | [Event-Driven Data API](AWS-Cloud/event-driven-data-api.md) · [Relational vs. NoSQL Access Patterns](AWS-Cloud/dynamodb-access-patterns.md) |
| [Graph Data](Graph-Data/) | Graph databases and graph traversal | [BFS: Shortest Reach](Graph-Data/hackerrank-bfs-shortest-reach.md) · [Neo4j Account Paths](Graph-Data/neo4j-account-paths.md) |
| [GenAI and Agentic Patterns](GenAI-Agentic/) | GenAI, tool use, agent boundaries, human approval | [Guarded Data Assistant](GenAI-Agentic/guarded-data-assistant.md) |
| [DevOps and TDD](DevOps-TDD/) | Git, GitHub Actions, CI/CD, lean delivery, test automation | [GitHub Actions to ECS](DevOps-TDD/github-actions-ecs-ci-cd.md) · TDD is also practiced in the [Spring Boot API exercise](Java-Backend/spring-boot-rest-products-api.md) |

## Suggested Order

1. Start with Java Comparator, Java 2D Array, Java Priority Queue, Python Collections Counter, and SQL Placements to warm up on the HackerRank platform.
2. Work through SQL Interviews, then the data-modeling and Spark ETL exercises.
3. Build the REST API test-first; use the AWS, graph, and agent exercises to practice trade-off explanations and Security by Design.
4. Finish with the GitHub Actions workflow and the React exercise. Treat React as supplementary to this role's stated requirements.

## Research Sources

HackerRank's public domains and skill page were used to select platform exercises. The company-specific design exercises are grounded in primary documentation:

- [HackerRank Java](https://www.hackerrank.com/domains/java), [SQL](https://www.hackerrank.com/domains/sql), [Python](https://www.hackerrank.com/domains/python), and [skills verification](https://www.hackerrank.com/skills-verification)
- [Spring: Building a RESTful Web Service](https://spring.io/guides/gs/rest-service)
- [React: Quick Start](https://react.dev/learn)
- [Apache Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Databricks: Medallion lakehouse architecture](https://docs.databricks.com/aws/en/lakehouse/medallion)
- [AWS Lambda with S3](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html), [Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html), [API Gateway proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html), [RDS overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), [ECS overview](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html), and [DynamoDB data modeling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-modeling-nosql.html)
- [Neo4j Cypher Manual](https://neo4j.com/docs/cypher-manual/current/)
- [GitHub Actions workflows](https://docs.github.com/en/actions/writing-workflows/about-workflows) and [workflow security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
- [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling)

The HackerRank exercise pages are authoritative challenge references. Solutions here are independently written study solutions, not copied editorials. This set is deliberately compact; it covers every technology named in the posting without implying each has a public HackerRank challenge.
