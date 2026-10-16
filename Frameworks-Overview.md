# Spring Boot Interview Cheat Sheet

Spring Boot · REST APIs · Spring Data JPA · Spring Security · Testing

---

## Quick Overview

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

## 1. Spring Boot Core

**Key points**
- **Auto-configuration** (`@EnableAutoConfiguration`) configures beans based on classpath and properties.
- `@SpringBootApplication` = `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`.
- **Starters** (`spring-boot-starter-web`, `-data-jpa`, `-security`) bundle dependencies.
- Embedded Tomcat by default; runs as an executable JAR.
- Config: `application.yml/properties`, profiles (`dev`, `prod`), env vars, `@ConfigurationProperties`.
- **IoC / DI:** the container creates and wires beans; prefer **constructor injection**.

**Questions**
1. **Spring vs Spring Boot?** Spring is the framework (DI, MVC, etc.); Boot adds auto-config, starters, embedded server, and opinionated defaults.
2. **How does auto-configuration work?** Conditional configuration classes (`@ConditionalOnClass`, `@ConditionalOnMissingBean`) load from `AutoConfiguration.imports` based on classpath and properties.
3. **Constructor vs field injection?** Constructor: immutable, testable, explicit required dependencies. Field (`@Autowired`) hides dependencies and hampers testing.
4. **Bean scopes?** Singleton (default), prototype, request, session.
5. **`@Component` vs `@Service` vs `@Repository` vs `@Configuration`?** All stereotypes; `@Repository` adds exception translation; `@Configuration` holds `@Bean` methods.
6. **How do profiles work?** `spring.profiles.active=prod` loads `application-prod.yml` and `@Profile` beans.
7. **Bean lifecycle?** Instantiate → inject → `@PostConstruct` → ready → `@PreDestroy`.
8. **Dependency conflicts / circular dependencies?** Use `@Qualifier`/`@Primary`; fix circular deps by redesign (avoid `@Lazy` hacks).
9. **Where do you keep secrets?** Env vars, Secrets Manager/Vault, never in the repo.

---

## 2. REST APIs

**Key points**
- Annotations: `@RestController`, `@RequestMapping`, `@GetMapping/@PostMapping/...`, `@PathVariable`, `@RequestParam`, `@RequestBody`.
- Return `ResponseEntity<T>` for status/headers control.
- **HTTP methods:** GET (safe, idempotent), POST (create), PUT (replace, idempotent), PATCH (partial), DELETE (idempotent).
- **Status codes:** 200, 201, 204, 400, 401, 403, 404, 409, 422, 500.
- Validation: `@Valid` + Bean Validation (`@NotNull`, `@Size`, `@Email`).
- Global error handling: `@RestControllerAdvice` + `@ExceptionHandler` (or `ProblemDetail`).

**Questions**
1. **`@Controller` vs `@RestController`?** `@RestController` = `@Controller` + `@ResponseBody` (serializes to JSON).
2. **`@PathVariable` vs `@RequestParam`?** Path segment (`/users/{id}`) vs query string (`?page=1`).
3. **PUT vs PATCH vs POST?** PUT replaces the whole resource, PATCH updates part, POST creates (not idempotent).
4. **What does idempotent mean?** Repeating the request yields the same result (GET, PUT, DELETE).
5. **How do you handle exceptions globally?** `@RestControllerAdvice` mapping exceptions to consistent error bodies and status codes.
6. **How do you validate input?** DTO annotations + `@Valid`; handle `MethodArgumentNotValidException`.
7. **Why use DTOs instead of entities?** Decouple API from DB schema, avoid over-posting and lazy-loading leaks.
8. **How do you version APIs?** URI (`/v1/`), header, or media type; prefer backward-compatible changes.
9. **How do you implement pagination?** Spring Data `Pageable` (`page`, `size`, `sort`) returning `Page<T>`; consider cursor pagination for large sets.
10. **REST best practices?** Nouns for resources, proper status codes, statelessness, HATEOAS optional, consistent errors, OpenAPI docs (springdoc).
11. **Synchronous calls to other services?** `RestClient`/`WebClient`/Feign with timeouts, retries, circuit breakers (Resilience4j).

---

## 3. Data Access (Spring Data JPA)

**Key points**
- `JpaRepository<Entity, Id>` gives CRUD, paging, and derived queries (`findByEmail`).
- `@Query` for JPQL/native; `@Transactional` for transaction boundaries.
- Entity mapping: `@Entity`, `@Id`, `@OneToMany`, `@ManyToOne`, fetch types (LAZY vs EAGER).
- Migrations: Flyway or Liquibase.

**Questions**
1. **What is the N+1 problem?** One query for parents plus N for children. Fix with `JOIN FETCH`, `@EntityGraph`, or batch fetching.
2. **Lazy vs eager loading?** Lazy loads on access (default for collections); eager always loads. Prefer lazy + explicit fetch.
3. **How does `@Transactional` work?** Proxy-based; rolls back on unchecked exceptions by default; self-invocation bypasses the proxy.
4. **Propagation / isolation?** `REQUIRED` (default) joins existing; `REQUIRES_NEW` starts a new one. Isolation controls dirty/phantom reads.
5. **Optimistic vs pessimistic locking?** `@Version` detects conflicts at commit (optimistic); `SELECT ... FOR UPDATE` blocks (pessimistic).
6. **`save()` vs `saveAndFlush()`?** Flush forces immediate DB sync; `save` defers until commit.
7. **Why use Flyway/Liquibase?** Versioned, repeatable schema migrations in CI/CD instead of `ddl-auto=update`.

---

## 4. Security

**Key points**
- Spring Security is a **filter chain**; configure with a `SecurityFilterChain` bean.
- AuthN: JWT, OAuth2/OIDC (resource server), session; passwords hashed with BCrypt.
- AuthZ: `@PreAuthorize`, role/authority checks.
- Protections: CSRF (needed for cookie sessions, often disabled for stateless JWT APIs), CORS, HTTPS, security headers.

**Questions**
1. **How do you secure a REST API?** Stateless JWT/OAuth2 resource server, HTTPS, role-based access, input validation, rate limiting.
2. **Authentication vs authorization?** Who you are vs what you can do.
3. **How does JWT validation work?** Verify signature, expiry, issuer/audience, then build the authentication from claims.
4. **CSRF and when to disable it?** Attacks on cookie-based sessions; safe to disable for stateless token APIs.
5. **How do you store passwords?** Salted adaptive hash (BCrypt/Argon2), never plain or fast hashes.
6. **CORS?** Browser policy; configure allowed origins/methods explicitly, not `*` with credentials.

---

## 5. Testing, Observability & Ops

**Key points**
- Unit tests: JUnit 5 + Mockito. Slice tests: `@WebMvcTest`, `@DataJpaTest`. Full: `@SpringBootTest`.
- **Testcontainers** for real DB/Kafka in integration tests.
- Actuator: `/health`, `/metrics`, `/info`; Micrometer → Prometheus/CloudWatch.
- Logging via SLF4J; correlation IDs; structured JSON logs.
- Packaging: layered JAR, Docker image, `bootBuildImage`.

**Questions**
1. **`@WebMvcTest` vs `@SpringBootTest`?** Web slice (controller + MockMvc, fast) vs full application context (slow, integration).
2. **`@Mock` vs `@MockBean`?** Plain Mockito mock vs mock registered in the Spring context (`@MockitoBean` in newer Boot).
3. **How do you test with a real DB?** Testcontainers for production-like behavior, not H2 mismatches.
4. **How do you monitor a Spring Boot app?** Actuator + Micrometer metrics, health probes, distributed tracing (OpenTelemetry).
5. **Startup time/performance tips?** Lazy init, trim dependencies, GraalVM native image, virtual threads (Java 21: `spring.threads.virtual.enabled=true`).
6. **MVC vs WebFlux?** MVC: blocking thread-per-request, simpler. WebFlux: reactive, non-blocking, for high-concurrency I/O.

---

## Cross-Topic / Scenario Questions

1. **Design a CRUD REST service.** Controller (DTO + validation) → Service (business logic, `@Transactional`) → Repository (JPA); `@RestControllerAdvice` for errors; Flyway for schema; OpenAPI docs.
2. **API is slow, what do you check?** N+1 queries, missing indexes, payload size, connection pool, caching (`@Cacheable`), external call timeouts, profiling.
3. **How do you make it resilient?** Timeouts, retries with backoff, circuit breaker, bulkheads, idempotency keys.
4. **Monolith vs microservices?** Start modular monolith; split on clear bounded contexts, with the cost of distributed complexity.
5. **How do you deploy it?** Dockerize → CI builds/tests → push to ECR → ECS/Fargate behind ALB, config from env/Secrets Manager.
6. **Secure it end to end.** Auth via JWT, least-privilege, validated input, secrets externalized, dependency scanning, HTTPS.

---

## Core Concepts to Know Cold

- **IoC/DI**, bean lifecycle, constructor injection.
- **Auto-configuration** and starters.
- **REST semantics:** methods, idempotency, status codes, DTOs, validation, error handling.
- **JPA pitfalls:** N+1, lazy loading, transaction proxies.
- **Security basics:** JWT, OAuth2, BCrypt, CSRF/CORS.
- **Test pyramid:** unit → slice → integration (Testcontainers).
