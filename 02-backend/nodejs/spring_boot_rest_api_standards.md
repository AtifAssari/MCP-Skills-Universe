---
rating: ⭐⭐
title: spring-boot-rest-api-standards
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/spring-boot-rest-api-standards
---

# spring-boot-rest-api-standards

skills/giuseppe-trisciuoglio/developer-kit/spring-boot-rest-api-standards
spring-boot-rest-api-standards
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill spring-boot-rest-api-standards
Summary

Comprehensive REST API design standards and best practices for Spring Boot applications.

Covers resource-based URL design, HTTP method conventions, status codes, DTOs, validation, and error handling with global exception strategies
Includes pagination, filtering, sorting, security headers, CORS policies, and HATEOAS implementation patterns
Provides constructor injection, immutable DTO patterns, transaction management, and logging best practices with code examples
Enforces API versioning, input validation at controller boundaries, and separation of concerns between controllers, services, and repositories
SKILL.md
Spring Boot REST API Standards
Overview

REST API design standards for Spring Boot covering URL design, HTTP methods, status codes, DTOs, validation, error handling, pagination, and security headers.

When to Use
Creating REST endpoints and API routes
Designing DTOs and API contracts
Implementing error handling and validation
Setting up pagination and filtering
Configuring security headers and CORS
Reviewing REST API architecture
Instructions
To Build RESTful API Endpoints

Follow these steps to create well-designed REST API endpoints:

Design Resource-Based URLs

Use plural nouns for resource names
Follow REST conventions: GET /users, POST /users, PUT /users/{id}
Avoid action-based URLs like /getUserList

Implement Proper HTTP Methods

GET: Retrieve resources (safe, idempotent)
POST: Create resources (not idempotent)
PUT: Replace entire resources (idempotent)
PATCH: Partial updates (not idempotent)
DELETE: Remove resources (idempotent)

Use Appropriate Status Codes

200 OK: Successful GET/PUT/PATCH
201 Created: Successful POST with Location header
204 No Content: Successful DELETE
400 Bad Request: Invalid request data
404 Not Found: Resource doesn't exist
409 Conflict: Duplicate resource
500 Internal Server Error: Unexpected errors

Create Request/Response DTOs

Separate API contracts from domain entities
Use Java records or Lombok @Data/@Value
Apply Jakarta validation annotations
Keep DTOs immutable when possible

Implement Validation

Use @Valid annotation on @RequestBody parameters
Apply validation constraints (@NotBlank, @Email, @Size, etc.)
Handle validation errors with MethodArgumentNotValidException

Set Up Error Handling

Use @RestControllerAdvice for global exception handling
Return standardized error responses with status, error, message, and timestamp
Use ResponseStatusException for specific HTTP status codes

Configure Pagination

Use Pageable for large datasets
Include page, size, sort parameters
Return metadata with total elements, totalPages, etc.

Add Security Headers

Configure CORS policies
Set content security policy
Include X-Frame-Options, X-Content-Type-Options

Validation checkpoints:

After step 1-2: Verify URL structure follows REST conventions (/users not /getUsers)
After step 3: Test each endpoint returns correct status codes
After step 4-5: Validate DTOs with curl or HTTPie before proceeding
After step 6: Confirm error responses match standardized format
Examples
Basic CRUD Controller
@RestController
@RequestMapping("/v1/users")
@RequiredArgsConstructor
@Slf4j
public class UserController {
    private final UserService userService;

    @GetMapping
    public ResponseEntity<Page<UserResponse>> getAllUsers(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int pageSize) {
        log.debug("Fetching users page {} size {}", page, pageSize);
        Page<UserResponse> users = userService.getAll(page, pageSize);
        return ResponseEntity.ok(users);
    }

    @GetMapping("/{id}")
    public ResponseEntity<UserResponse> getUserById(@PathVariable Long id) {
        return ResponseEntity.ok(userService.getById(id));
    }

    @PostMapping
    public ResponseEntity<UserResponse> createUser(@Valid @RequestBody CreateUserRequest request) {
        UserResponse created = userService.create(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }

    @PutMapping("/{id}")
    public ResponseEntity<UserResponse> updateUser(
            @PathVariable Long id,
            @Valid @RequestBody UpdateUserRequest request) {
        return ResponseEntity.ok(userService.update(id, request));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.delete(id);
        return ResponseEntity.noContent().build();
    }
}

Request/Response DTOs
// Request DTO
@Data
@NoArgsConstructor
@AllArgsConstructor
public class CreateUserRequest {
    @NotBlank(message = "User name cannot be blank")
    private String name;

    @Email(message = "Valid email required")
    private String email;
}

// Response DTO
@Data
@NoArgsConstructor
@AllArgsConstructor
public class UserResponse {
    private Long id;
    private String name;
    private String email;
    private LocalDateTime createdAt;
}

Global Exception Handler
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidationException(
            MethodArgumentNotValidException ex, WebRequest request) {
        String errors = ex.getBindingResult().getFieldErrors().stream()
                .map(f -> f.getField() + ": " + f.getDefaultMessage())
                .collect(Collectors.joining(", "));

        ErrorResponse errorResponse = new ErrorResponse(
                HttpStatus.BAD_REQUEST.value(),
                "Validation Error",
                "Validation failed: " + errors,
                request.getDescription(false).replaceFirst("uri=", "")
        );
        return new ResponseEntity<>(errorResponse, HttpStatus.BAD_REQUEST);
    }

    @ExceptionHandler(ResponseStatusException.class)
    public ResponseEntity<ErrorResponse> handleResponseStatusException(
            ResponseStatusException ex, WebRequest request) {
        ErrorResponse error = new ErrorResponse(
            ex.getStatusCode().value(),
            ex.getStatusCode().toString(),
            ex.getReason(),
            request.getDescription(false).replaceFirst("uri=", "")
        );
        return new ResponseEntity<>(error, ex.getStatusCode());
    }
}

Best Practices
1. Use Constructor Injection
@Service
@RequiredArgsConstructor
public class UserService {
    private final UserRepository userRepository;
}

2. Prefer Immutable DTOs (Java Records or @Value)
public record UserResponse(Long id, String name, String email) {}

3. Implement Proper Transaction Management
@Service
@Transactional
public class UserService {
    @Transactional(readOnly = true)
    public Optional<User> findById(Long id) { return userRepository.findById(id); }

    @Transactional
    public User create(User user) { return userRepository.save(user); }
}

Constraints and Warnings
Never expose entities directly - Use DTOs to separate API contracts from domain models
Follow REST conventions - Use nouns for resources (/users), correct HTTP methods, plural names, proper status codes
Handle all exceptions globally - Use @RestControllerAdvice, never let raw exceptions bubble up
Always paginate large result sets - Prevent performance issues and DDoS vulnerabilities
Validate all input data - Use Jakarta validation annotations on request DTOs
Never expose sensitive data - Don't log or expose passwords, tokens, PII
References
See references/ directory for comprehensive reference material including HTTP status codes, Spring annotations, and detailed examples
Refer to the developer-kit-java:spring-boot-code-review-expert agent for code review guidelines
Review spring-boot-dependency-injection/SKILL.md for dependency injection patterns
Check ../spring-boot-test-patterns/SKILL.md for testing REST APIs
Weekly Installs
903
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass