# Spring Boot Interview Cheat Sheet

*Spring Boot · REST APIs · Spring Data JPA · Spring Security · Testing*

**Jump to:** [All Topics](All-Topics-Overview.md) · [AWS](AWS-Overview.md) · [Data](Data-Overview.md) · [Spring Boot](Frameworks-Overview.md) · [DevOps](DevOps-Overview.md) · [Practices](Practices-Overview.md) · [Gen AI](GenAI-Overview.md)

> [!TIP]
> Click any question to expand the answer. Try answering out loud first.

<details>
<summary><b>📑 Table of contents</b></summary>

1. [🧭 Quick Overview](#-quick-overview)
2. [🍃 1. Spring Boot Core](#-1-spring-boot-core)
3. [🔌 2. REST APIs](#-2-rest-apis)
4. [💾 3. Data Access (Spring Data JPA)](#-3-data-access-spring-data-jpa)
5. [🔐 4. Security](#-4-security)
6. [🧪 5. Testing, Observability & Ops](#-5-testing-observability--ops)
7. [🧩 Cross-Topic / Scenario Questions](#-cross-topic--scenario-questions)
8. [🎯 Core Concepts to Know Cold](#-core-concepts-to-know-cold)

</details>

---

## 🧭 Quick Overview

| Topic | What it is | Use it for |
|---|---|---|
| **Spring Boot** | Opinionated Spring setup with auto-configuration and embedded server | Fast, production-ready Java apps |
| **Spring MVC / REST** | `@RestController` request handling on top of the servlet stack | Building REST APIs |
| **Spring Data JPA** | Repository abstraction over JPA/Hibernate | DB access without boilerplate |
| **Spring Security** | AuthN/AuthZ framework (filter chain) | JWT/OAuth2, role-based access |
| **Actuator** | Production endpoints (health, metrics) | Monitoring, readiness/liveness |
| **Spring Test** | `@SpringBootTest`, `@WebMvcTest`, MockMvc, Mockito | TDD and integration tests |

**Typical layering:** Controller → Service → Repository → DB, with DTOs at the edge, validation on input, and a global exception handler.

---

## 🍃 1. Spring Boot Core

#### 📌 Key points
- **Auto-configuration** (`@EnableAutoConfiguration`) configures beans based on classpath and properties.
- `@SpringBootApplication` = `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`.
- **Starters** (`spring-boot-starter-web`, `-data-jpa`, `-security`) bundle dependencies.
- Embedded Tomcat by default; runs as an executable JAR.
- Config: `application.yml/properties`, profiles (`dev`, `prod`), env vars, `@ConfigurationProperties`.
- **IoC / DI:** the container creates and wires beans; prefer **constructor injection**.

#### ❓ Questions
<details>
<summary><b>1. Spring vs Spring Boot?</b></summary>

Spring is the framework (DI, MVC, etc.); Boot adds auto-config, starters, embedded server, and opinionated defaults.

</details>

<details>
<summary><b>2. How does auto-configuration work?</b></summary>

Conditional configuration classes (`@ConditionalOnClass`, `@ConditionalOnMissingBean`) load from `AutoConfiguration.imports` based on classpath and properties.

</details>

<details>
<summary><b>3. Constructor vs field injection?</b></summary>

Constructor: immutable, testable, explicit required dependencies. Field (`@Autowired`) hides dependencies and hampers testing.

</details>

<details>
<summary><b>4. Bean scopes?</b></summary>

Singleton (default), prototype, request, session.

</details>

<details>
<summary><b>5. `@Component` vs `@Service` vs `@Repository` vs `@Configuration`?</b></summary>

All stereotypes; `@Repository` adds exception translation; `@Configuration` holds `@Bean` methods.

</details>

<details>
<summary><b>6. How do profiles work?</b></summary>

`spring.profiles.active=prod` loads `application-prod.yml` and `@Profile` beans.

</details>

<details>
<summary><b>7. Bean lifecycle?</b></summary>

Instantiate → inject → `@PostConstruct` → ready → `@PreDestroy`.

</details>

<details>
<summary><b>8. Dependency conflicts / circular dependencies?</b></summary>

Use `@Qualifier`/`@Primary`; fix circular deps by redesign (avoid `@Lazy` hacks).

</details>

<details>
<summary><b>9. Where do you keep secrets?</b></summary>

Env vars, Secrets Manager/Vault, never in the repo.

</details>

---

## 🔌 2. REST APIs

#### 📌 Key points
- Annotations: `@RestController`, `@RequestMapping`, `@GetMapping/@PostMapping/...`, `@PathVariable`, `@RequestParam`, `@RequestBody`.
- Return `ResponseEntity<T>` for status/headers control.
- **HTTP methods:** GET (safe, idempotent), POST (create), PUT (replace, idempotent), PATCH (partial), DELETE (idempotent).
- **Status codes:** 200, 201, 204, 400, 401, 403, 404, 409, 422, 500.
- Validation: `@Valid` + Bean Validation (`@NotNull`, `@Size`, `@Email`).
- Global error handling: `@RestControllerAdvice` + `@ExceptionHandler` (or `ProblemDetail`).

#### ❓ Questions
<details>
<summary><b>1. `@Controller` vs `@RestController`?</b></summary>

`@RestController` = `@Controller` + `@ResponseBody` (serializes to JSON).

</details>

<details>
<summary><b>2. `@PathVariable` vs `@RequestParam`?</b></summary>

Path segment (`/users/{id}`) vs query string (`?page=1`).

</details>

<details>
<summary><b>3. PUT vs PATCH vs POST?</b></summary>

PUT replaces the whole resource, PATCH updates part, POST creates (not idempotent).

</details>

<details>
<summary><b>4. What does idempotent mean?</b></summary>

Repeating the request yields the same result (GET, PUT, DELETE).

</details>

<details>
<summary><b>5. How do you handle exceptions globally?</b></summary>

`@RestControllerAdvice` mapping exceptions to consistent error bodies and status codes.

</details>

<details>
<summary><b>6. How do you validate input?</b></summary>

DTO annotations + `@Valid`; handle `MethodArgumentNotValidException`.

</details>

<details>
<summary><b>7. Why use DTOs instead of entities?</b></summary>

Decouple API from DB schema, avoid over-posting and lazy-loading leaks.

</details>

<details>
<summary><b>8. How do you version APIs?</b></summary>

URI (`/v1/`), header, or media type; prefer backward-compatible changes.

</details>

<details>
<summary><b>9. How do you implement pagination?</b></summary>

Spring Data `Pageable` (`page`, `size`, `sort`) returning `Page<T>`; consider cursor pagination for large sets.

</details>

<details>
<summary><b>10. REST best practices?</b></summary>

Nouns for resources, proper status codes, statelessness, HATEOAS optional, consistent errors, OpenAPI docs (springdoc).

</details>

<details>
<summary><b>11. Synchronous calls to other services?</b></summary>

`RestClient`/`WebClient`/Feign with timeouts, retries, circuit breakers (Resilience4j).

</details>

---

## 💾 3. Data Access (Spring Data JPA)

#### 📌 Key points
- `JpaRepository<Entity, Id>` gives CRUD, paging, and derived queries (`findByEmail`).
- `@Query` for JPQL/native; `@Transactional` for transaction boundaries.
- Entity mapping: `@Entity`, `@Id`, `@OneToMany`, `@ManyToOne`, fetch types (LAZY vs EAGER).
- Migrations: Flyway or Liquibase.

#### ❓ Questions
<details>
<summary><b>1. What is the N+1 problem?</b></summary>

One query for parents plus N for children. Fix with `JOIN FETCH`, `@EntityGraph`, or batch fetching.

</details>

<details>
<summary><b>2. Lazy vs eager loading?</b></summary>

Lazy loads on access (default for collections); eager always loads. Prefer lazy + explicit fetch.

</details>

<details>
<summary><b>3. How does `@Transactional` work?</b></summary>

Proxy-based; rolls back on unchecked exceptions by default; self-invocation bypasses the proxy.

</details>

<details>
<summary><b>4. Propagation / isolation?</b></summary>

`REQUIRED` (default) joins existing; `REQUIRES_NEW` starts a new one. Isolation controls dirty/phantom reads.

</details>

<details>
<summary><b>5. Optimistic vs pessimistic locking?</b></summary>

`@Version` detects conflicts at commit (optimistic); `SELECT ... FOR UPDATE` blocks (pessimistic).

</details>

<details>
<summary><b>6. `save()` vs `saveAndFlush()`?</b></summary>

Flush forces immediate DB sync; `save` defers until commit.

</details>

<details>
<summary><b>7. Why use Flyway/Liquibase?</b></summary>

Versioned, repeatable schema migrations in CI/CD instead of `ddl-auto=update`.

</details>

---

## 🔐 4. Security

#### 📌 Key points
- Spring Security is a **filter chain**; configure with a `SecurityFilterChain` bean.
- AuthN: JWT, OAuth2/OIDC (resource server), session; passwords hashed with BCrypt.
- AuthZ: `@PreAuthorize`, role/authority checks.
- Protections: CSRF (needed for cookie sessions, often disabled for stateless JWT APIs), CORS, HTTPS, security headers.

#### ❓ Questions
<details>
<summary><b>1. How do you secure a REST API?</b></summary>

Stateless JWT/OAuth2 resource server, HTTPS, role-based access, input validation, rate limiting.

</details>

<details>
<summary><b>2. Authentication vs authorization?</b></summary>

Who you are vs what you can do.

</details>

<details>
<summary><b>3. How does JWT validation work?</b></summary>

Verify signature, expiry, issuer/audience, then build the authentication from claims.

</details>

<details>
<summary><b>4. CSRF and when to disable it?</b></summary>

Attacks on cookie-based sessions; safe to disable for stateless token APIs.

</details>

<details>
<summary><b>5. How do you store passwords?</b></summary>

Salted adaptive hash (BCrypt/Argon2), never plain or fast hashes.

</details>

<details>
<summary><b>6. CORS?</b></summary>

Browser policy; configure allowed origins/methods explicitly, not `*` with credentials.

</details>

---

## 🧪 5. Testing, Observability & Ops

#### 📌 Key points
- Unit tests: JUnit 5 + Mockito. Slice tests: `@WebMvcTest`, `@DataJpaTest`. Full: `@SpringBootTest`.
- **Testcontainers** for real DB/Kafka in integration tests.
- Actuator: `/health`, `/metrics`, `/info`; Micrometer → Prometheus/CloudWatch.
- Logging via SLF4J; correlation IDs; structured JSON logs.
- Packaging: layered JAR, Docker image, `bootBuildImage`.

#### ❓ Questions
<details>
<summary><b>1. `@WebMvcTest` vs `@SpringBootTest`?</b></summary>

Web slice (controller + MockMvc, fast) vs full application context (slow, integration).

</details>

<details>
<summary><b>2. `@Mock` vs `@MockBean`?</b></summary>

Plain Mockito mock vs mock registered in the Spring context (`@MockitoBean` in newer Boot).

</details>

<details>
<summary><b>3. How do you test with a real DB?</b></summary>

Testcontainers for production-like behavior, not H2 mismatches.

</details>

<details>
<summary><b>4. How do you monitor a Spring Boot app?</b></summary>

Actuator + Micrometer metrics, health probes, distributed tracing (OpenTelemetry).

</details>

<details>
<summary><b>5. Startup time/performance tips?</b></summary>

Lazy init, trim dependencies, GraalVM native image, virtual threads (Java 21: `spring.threads.virtual.enabled=true`).

</details>

<details>
<summary><b>6. MVC vs WebFlux?</b></summary>

MVC: blocking thread-per-request, simpler. WebFlux: reactive, non-blocking, for high-concurrency I/O.

</details>

---

## 🧩 Cross-Topic / Scenario Questions

<details>
<summary><b>1. Design a CRUD REST service.</b></summary>

Controller (DTO + validation) → Service (business logic, `@Transactional`) → Repository (JPA); `@RestControllerAdvice` for errors; Flyway for schema; OpenAPI docs.

</details>

<details>
<summary><b>2. API is slow, what do you check?</b></summary>

N+1 queries, missing indexes, payload size, connection pool, caching (`@Cacheable`), external call timeouts, profiling.

</details>

<details>
<summary><b>3. How do you make it resilient?</b></summary>

Timeouts, retries with backoff, circuit breaker, bulkheads, idempotency keys.

</details>

<details>
<summary><b>4. Monolith vs microservices?</b></summary>

Start modular monolith; split on clear bounded contexts, with the cost of distributed complexity.

</details>

<details>
<summary><b>5. How do you deploy it?</b></summary>

Dockerize → CI builds/tests → push to ECR → ECS/Fargate behind ALB, config from env/Secrets Manager.

</details>

<details>
<summary><b>6. Secure it end to end.</b></summary>

Auth via JWT, least-privilege, validated input, secrets externalized, dependency scanning, HTTPS.

</details>

---

## 🎯 Core Concepts to Know Cold

- **IoC/DI**, bean lifecycle, constructor injection.
- **Auto-configuration** and starters.
- **REST semantics:** methods, idempotency, status codes, DTOs, validation, error handling.
- **JPA pitfalls:** N+1, lazy loading, transaction proxies.
- **Security basics:** JWT, OAuth2, BCrypt, CSRF/CORS.
- **Test pyramid:** unit → slice → integration (Testcontainers).

---

**Jump to:** [All Topics](All-Topics-Overview.md) · [AWS](AWS-Overview.md) · [Data](Data-Overview.md) · [Spring Boot](Frameworks-Overview.md) · [DevOps](DevOps-Overview.md) · [Practices](Practices-Overview.md) · [Gen AI](GenAI-Overview.md)
