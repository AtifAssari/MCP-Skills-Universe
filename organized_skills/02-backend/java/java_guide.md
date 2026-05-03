---
rating: ⭐⭐⭐
title: java-guide
url: https://skills.sh/ar4mirez/samuel/java-guide
---

# java-guide

skills/ar4mirez/samuel/java-guide
java-guide
Installation
$ npx skills add https://github.com/ar4mirez/samuel --skill java-guide
SKILL.md
Java Guide

Applies to: Java 17+, Spring Boot, Maven/Gradle, Enterprise Applications

Core Principles
Immutability by Default: Prefer records, final fields, and unmodifiable collections
Explicit Over Implicit: Clear type declarations, no raw types, no unchecked casts
Fail Fast: Validate inputs at boundaries, use Objects.requireNonNull liberally
Composition Over Inheritance: Favor delegation and interfaces over deep class hierarchies
Standard Library First: Use java.util, java.time, java.nio before adding dependencies
Guardrails
Version & Dependencies
Use Java 17+ (LTS) with preview features disabled in production
Manage dependencies with Maven (pom.xml) or Gradle (build.gradle.kts)
Pin dependency versions explicitly (no dynamic versions like 1.+)
Run mvn dependency:analyze or gradle dependencies to detect unused/undeclared deps
Check for vulnerabilities: mvn org.owasp:dependency-check-maven:check
Code Style
Follow Google Java Style Guide
Classes: PascalCase | Methods/fields: camelCase | Constants: UPPER_SNAKE_CASE
Packages: com.company.project.module (lowercase, no underscores)
One top-level class per file (name matches filename)
Use var for local variables only when the type is obvious from the right side
No wildcard imports (import java.util.* is forbidden)
Records & Sealed Classes
Use record for immutable data carriers instead of manual POJOs
Use sealed classes/interfaces for restricted type hierarchies
Add compact constructors for validation in records
Sealed classes enable exhaustive switch expressions with pattern matching
public record UserId(String value) {
    public UserId {
        Objects.requireNonNull(value, "UserId must not be null");
        if (value.isBlank()) {
            throw new IllegalArgumentException("UserId must not be blank");
        }
    }
}

public sealed interface PaymentResult
        permits PaymentResult.Success, PaymentResult.Declined, PaymentResult.Error {
    record Success(String transactionId, BigDecimal amount) implements PaymentResult {}
    record Declined(String reason) implements PaymentResult {}
    record Error(Exception cause) implements PaymentResult {}
}

Streams & Optional
Use streams for transformations, not for side effects
Never call Optional.get() -- use orElseThrow(), orElse(), map(), flatMap()
Do not use Optional as a method parameter or field type (only as a return type)
Avoid parallel streams unless measured to be faster (overhead is real)
Prefer toList() (Java 16+) over collect(Collectors.toList())
List<String> activeEmails = users.stream()
        .filter(User::isActive)
        .map(User::email)
        .toList();

String displayName = userRepository.findById(id)
        .map(User::displayName)
        .orElseThrow(() -> new UserNotFoundException(id));

Resource Management
Always use try-with-resources for AutoCloseable types
Never rely on finalize() (deprecated and unreliable)
Close resources in reverse order of acquisition
try (var connection = dataSource.getConnection();
     var statement = connection.prepareStatement(sql);
     var resultSet = statement.executeQuery()) {
    while (resultSet.next()) {
        results.add(mapRow(resultSet));
    }
}

Project Structure
myproject/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/com/company/project/
│   │   │   ├── Application.java        # Entry point
│   │   │   ├── config/                  # Configuration classes
│   │   │   ├── controller/              # REST controllers / API layer
│   │   │   ├── service/                 # Business logic
│   │   │   ├── repository/              # Data access
│   │   │   ├── model/                   # Domain entities and records
│   │   │   ├── dto/                     # Data transfer objects (records)
│   │   │   └── exception/               # Custom exceptions
│   │   └── resources/
│   │       ├── application.yml
│   │       └── db/migration/            # Flyway/Liquibase migrations
│   └── test/java/com/company/project/   # Mirrors main structure
└── target/                              # Build output (gitignored)

Packages map to bounded contexts (not technical layers at the top)
Test structure mirrors source structure
Keep resources/ flat; use db/migration/ for schema changes
Key Patterns
Sealed Classes with Pattern Matching
public static double area(Shape shape) {
    return switch (shape) {
        case Shape.Circle c -> Math.PI * c.radius() * c.radius();
        case Shape.Rectangle r -> r.width() * r.height();
        case Shape.Triangle t -> 0.5 * t.base() * t.height();
    };
}

Immutable Collections
List<String> roles = List.of("ADMIN", "USER", "GUEST");
Map<String, String> config = Map.ofEntries(
        Map.entry("host", "localhost"),
        Map.entry("port", "8080"));
List<Item> snapshot = List.copyOf(mutableList);

Text Blocks
String query = """
        SELECT u.id, u.email, u.created_at
        FROM users u
        WHERE u.active = true
        ORDER BY u.created_at DESC
        LIMIT ?
        """;

Optional Chaining
// Fallback chain: cache -> database -> remote
User user = cache.findUser(id)
        .or(() -> database.findUser(id))
        .or(() -> remoteService.fetchUser(id))
        .orElseThrow(() -> new UserNotFoundException(id));

// Conditional execution without get()
userRepository.findById(userId)
        .ifPresentOrElse(
            u -> log.info("Found user: {}", u.name()),
            () -> log.warn("User {} not found", userId));

Testing
Standards
Test files mirror source under src/test/java
Test class names: ClassNameTest (not TestClassName)
Test methods: @Test void shouldDescribeBehavior()
Use @DisplayName for complex scenarios, @Nested to group related tests
Coverage target: >80% for business logic, >60% overall
Prefer AssertJ over JUnit assertions for readability
Basic Test Structure
class UserServiceTest {

    private UserRepository userRepository;
    private UserService userService;

    @BeforeEach
    void setUp() {
        userRepository = mock(UserRepository.class);
        userService = new UserService(userRepository);
    }

    @Test
    void shouldReturnUserWhenFound() {
        var expected = new User("1", "alice@example.com", "Alice");
        when(userRepository.findById("1")).thenReturn(Optional.of(expected));

        User result = userService.getUser("1");

        assertThat(result).isEqualTo(expected);
        verify(userRepository).findById("1");
    }

    @Test
    void shouldThrowWhenUserNotFound() {
        when(userRepository.findById("999")).thenReturn(Optional.empty());

        assertThatThrownBy(() -> userService.getUser("999"))
                .isInstanceOf(UserNotFoundException.class)
                .hasMessageContaining("999");
    }
}

Parameterized Tests
@ParameterizedTest
@CsvSource({
    "alice@example.com, true",
    "bob@test.org, true",
    "invalid-email, false",
    "'', false",
})
void shouldValidateEmail(String email, boolean expected) {
    assertThat(EmailValidator.isValid(email)).isEqualTo(expected);
}

@ParameterizedTest
@MethodSource("provideMoneyAdditions")
void shouldAddMoneySameCurrency(Money a, Money b, Money expected) {
    assertThat(a.add(b)).isEqualTo(expected);
}

static Stream<Arguments> provideMoneyAdditions() {
    var usd = Currency.getInstance("USD");
    return Stream.of(
        Arguments.of(new Money(BigDecimal.ONE, usd),
                      new Money(BigDecimal.TEN, usd),
                      new Money(new BigDecimal("11"), usd))
    );
}

Tooling
Maven Commands
mvn clean install              # Build and install locally
mvn test                       # Run all tests
mvn verify                     # Run tests + integration tests
mvn dependency:tree            # Show dependency tree
mvn dependency:analyze         # Find unused/undeclared deps
mvn spotbugs:check             # Static analysis
mvn checkstyle:check           # Style check

Gradle Commands
./gradlew build                # Full build with tests
./gradlew test                 # Run unit tests
./gradlew check                # Run all verification tasks
./gradlew dependencies         # Show dependency tree
./gradlew jacocoTestReport     # Generate coverage report

References

For detailed patterns and examples, see:

references/patterns.md -- Spring patterns, Stream API recipes, Optional chaining, builder patterns
External References
Google Java Style Guide
Effective Java (3rd Edition) -- Joshua Bloch
Java Records (JEP 395)
Sealed Classes (JEP 409)
Pattern Matching for switch (JEP 441)
JUnit 5 User Guide
AssertJ Documentation
SpotBugs
Checkstyle
Weekly Installs
9
Repository
ar4mirez/samuel
GitHub Stars
8
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass