# Spring Boot REST API with TDD

**Type:** Supplemental original exercise
**Source:** [Spring: Building a RESTful Web Service](https://spring.io/guides/gs/rest-service)
**Focus:** Java, Spring Boot, REST semantics, validation, test-first development

## Exercise

Design `POST /api/products` and `GET /api/products/{id}`. A product has a generated ID, a nonblank name, and a positive price. Return `201 Created` with a `Location` header on creation, `400 Bad Request` for invalid input, and `404 Not Found` when the requested product is absent. Start with tests.

Example request:

```http
POST /api/products
Content-Type: application/json

{"name":"Bearing","price":12.50}
```

Expected response: `201 Created`, `Location: /api/products/1`, body `{"id":1,"name":"Bearing","price":12.50}`. A request with `"price":0` should return `400`; `GET /api/products/999` when that ID is absent should return `404`.

## TDD Plan

1. Write a test for a successful creation and its response code, body, and `Location` header.
2. Write a test that blank names and non-positive prices are rejected.
3. Write a test that an unknown ID returns `404`.
4. Implement the smallest controller/service behavior to make the tests pass; refactor while keeping them green.

## Solution

This in-memory implementation makes the exercise runnable without a database. In production, replace the map with a repository and keep the HTTP contract unchanged.

```java
import java.math.BigDecimal;
import java.net.URI;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

import jakarta.validation.Valid;
import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

record Product(long id, String name, BigDecimal price) {}

record CreateProductRequest(
        @NotBlank String name,
        @NotNull @DecimalMin("0.01") BigDecimal price) {}

@Service
class ProductService {
    private final AtomicLong nextId = new AtomicLong(1);
    private final Map<Long, Product> products = new ConcurrentHashMap<>();

    Product create(String name, BigDecimal price) {
        if (name == null || name.isBlank() || price == null
                || price.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Name and positive price are required");
        }

        long id = nextId.getAndIncrement();
        Product product = new Product(id, name.trim(), price);
        products.put(id, product);
        return product;
    }

    Optional<Product> findById(long id) {
        return Optional.ofNullable(products.get(id));
    }
}

@RestController
@RequestMapping("/api/products")
class ProductController {
    private final ProductService service;

    ProductController(ProductService service) {
        this.service = service;
    }

    @PostMapping
    ResponseEntity<Product> create(@Valid @RequestBody CreateProductRequest request) {
        Product product = service.create(request.name(), request.price());
        URI location = URI.create("/api/products/" + product.id());
        return ResponseEntity.created(location).body(product);
    }

    @GetMapping("/{id}")
    ResponseEntity<Product> findById(@PathVariable long id) {
        return service.findById(id)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }
}
```

Add `spring-boot-starter-validation` so `@Valid` activates Jakarta Bean Validation. Add `spring-boot-starter-test` for JUnit, MockMvc, and Mockito, then write HTTP tests before implementation:

```java
@WebMvcTest(ProductController.class)
class ProductControllerTest {
    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private ProductService service;

    @Test
    void createsProductAndReturnsLocation() throws Exception {
        when(service.create("Bearing", new BigDecimal("12.50")))
                .thenReturn(new Product(1, "Bearing", new BigDecimal("12.50")));

        mockMvc.perform(post("/api/products")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"name\":\"Bearing\",\"price\":12.50}"))
                .andExpect(status().isCreated())
                .andExpect(header().string("Location", "/api/products/1"))
                .andExpect(jsonPath("$.id").value(1))
                .andExpect(jsonPath("$.name").value("Bearing"));
    }

    @Test
    void rejectsInvalidPriceBeforeCallingService() throws Exception {
        mockMvc.perform(post("/api/products")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"name\":\"Bearing\",\"price\":0}"))
                .andExpect(status().isBadRequest());

        verifyNoInteractions(service);
    }

    @Test
    void returnsNotFoundForUnknownProduct() throws Exception {
        when(service.findById(999L)).thenReturn(Optional.empty());

        mockMvc.perform(get("/api/products/999"))
                .andExpect(status().isNotFound());
    }
}
```

Test imports: JUnit Jupiter, `@WebMvcTest`, `@Autowired`, `@MockBean`, `MockMvc`, `MediaType`, static MockMvc request/result matchers, `jsonPath`, Mockito `when`/`verifyNoInteractions`, `BigDecimal`, and `Optional`.

**Discussion points:** Why use `201` plus `Location`? Which errors should be handled centrally with `@ControllerAdvice`? What changes when persistence, concurrent requests, and authentication are added?
