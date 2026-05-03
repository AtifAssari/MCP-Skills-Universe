---
title: spring-boot-testing
url: https://skills.sh/github/awesome-copilot/spring-boot-testing
---

# spring-boot-testing

skills/github/awesome-copilot/spring-boot-testing
spring-boot-testing
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill spring-boot-testing
SKILL.md
Spring Boot Testing

This skill provides expert guide for testing Spring Boot 4 applications with modern patterns and best practices.

Core Principles
Test Pyramid: Unit (fast) > Slice (focused) > Integration (complete)
Right Tool: Use the narrowest slice that gives you confidence
AssertJ Style: Fluent, readable assertions over verbose matchers
Modern APIs: Prefer MockMvcTester and RestTestClient over legacy alternatives
Which Test Slice?
Scenario	Annotation	Reference
Controller + HTTP semantics	@WebMvcTest	references/webmvctest.md
Repository + JPA queries	@DataJpaTest	references/datajpatest.md
REST client + external APIs	@RestClientTest	references/restclienttest.md
JSON (de)serialization	@JsonTest	references/test-slices-overview.md
Full application	@SpringBootTest	references/test-slices-overview.md
Test Slices Reference
references/test-slices-overview.md - Decision matrix and comparison
references/webmvctest.md - Web layer with MockMvc
references/datajpatest.md - Data layer with Testcontainers
references/restclienttest.md - REST client testing
Testing Tools Reference
references/mockmvc-tester.md - AssertJ-style MockMvc (3.2+)
references/mockmvc-classic.md - Traditional MockMvc (pre-3.2)
references/resttestclient.md - Spring Boot 4+ REST client
references/mockitobean.md - Mocking dependencies
Assertion Libraries
references/assertj-basics.md - Scalars, strings, booleans, dates
references/assertj-collections.md - Lists, Sets, Maps, arrays
Testcontainers
references/testcontainers-jdbc.md - PostgreSQL, MySQL, etc.
Test Data Generation
references/instancio.md - Generate complex test objects (3+ properties)
Performance & Migration
references/context-caching.md - Speed up test suites
references/sb4-migration.md - Spring Boot 4.0 changes
Quick Decision Tree
Testing a controller endpoint?
  Yes → @WebMvcTest with MockMvcTester

Testing repository queries?
  Yes → @DataJpaTest with Testcontainers (real DB)

Testing business logic in service?
  Yes → Plain JUnit + Mockito (no Spring context)

Testing external API client?
  Yes → @RestClientTest with MockRestServiceServer

Testing JSON mapping?
  Yes → @JsonTest

Need full integration test?
  Yes → @SpringBootTest with minimal context config

Spring Boot 4 Highlights
RestTestClient: Modern alternative to TestRestTemplate
@MockitoBean: Replaces @MockBean (deprecated)
MockMvcTester: AssertJ-style assertions for web tests
Modular starters: Technology-specific test starters
Context pausing: Automatic pausing of cached contexts (Spring Framework 7)
Testing Best Practices
Code Complexity Assessment

When a method or class is too complex to test effectively:

Analyze complexity - If you need more than 5-7 test cases to cover a single method, it's likely too complex
Recommend refactoring - Suggest breaking the code into smaller, focused functions
User decision - If the user agrees to refactor, help identify extraction points
Proceed if needed - If the user decides to continue with the complex code, implement tests despite the difficulty

Example of refactoring recommendation:

// Before: Complex method hard to test
public Order processOrder(OrderRequest request) {
  // Validation, discount calculation, payment, inventory, notification...
  // 50+ lines of mixed concerns
}

// After: Refactored into testable units
public Order processOrder(OrderRequest request) {
  validateOrder(request);
  var order = createOrder(request);
  applyDiscount(order);
  processPayment(order);
  updateInventory(order);
  sendNotification(order);
  return order;
}

Avoid Code Redundancy

Create helper methods for commonly used objects and mock setup to enhance readability and maintainability.

Test Organization with @DisplayName

Use descriptive display names to clarify test intent:

@Test
@DisplayName("Should calculate discount for VIP customer")
void shouldCalculateDiscountForVip() { }

@Test
@DisplayName("Should reject order when customer has insufficient credit")
void shouldRejectOrderForInsufficientCredit() { }

Test Coverage Order

Always structure tests in this order:

Main scenario - The happy path, most common use case
Other paths - Alternative valid scenarios, edge cases
Exceptions/Errors - Invalid inputs, error conditions, failure modes
Test Production Scenarios

Write tests with real production scenarios in mind. This makes tests more relatable and helps understand code behavior in actual production cases.

Test Coverage Goals

Aim for 80% code coverage as a practical balance between quality and effort. Higher coverage is beneficial but not the only goal.

Use Jacoco maven plugin for coverage reporting and tracking.

Coverage Rules:

80+% coverage minimum
Focus on meaningful assertions, not just execution

What to Prioritize:

Business-critical paths (payment processing, order validation)
Complex algorithms (pricing, discount calculations)
Error handling (exceptions, edge cases)
Integration points (external APIs, databases)
Dependencies (Spring Boot 4)
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-test</artifactId>
  <scope>test</scope>
</dependency>

<!-- For WebMvc tests -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-webmvc-test</artifactId>
  <scope>test</scope>
</dependency>

<!-- For Testcontainers -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-testcontainers</artifactId>
  <scope>test</scope>
</dependency>

Weekly Installs
1.3K
Repository
github/awesome-copilot
GitHub Stars
31.9K
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass