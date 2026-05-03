---
rating: ⭐⭐
title: unit-test-service-layer
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/unit-test-service-layer
---

# unit-test-service-layer

skills/giuseppe-trisciuoglio/developer-kit/unit-test-service-layer
unit-test-service-layer
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill unit-test-service-layer
Summary

Isolated unit testing patterns for Spring service layer using Mockito and JUnit 5.

Covers mocking injected dependencies, verifying service interactions, and testing business logic without database or external API calls
Includes patterns for exception handling, complex workflows, argument capturing, and verification of call order and frequency
Supports testing async/reactive services with CompletableFuture and provides best practices for constructor injection and spy-based partial mocking
Demonstrates common anti-patterns to avoid and troubleshooting guidance for typical Mockito and JUnit 5 issues
SKILL.md
Unit Testing Service Layer with Mockito
Overview

Provides patterns for unit testing @Service classes using Mockito. Mocks repository calls, verifies method invocations, tests exception scenarios, and stubs external API responses. Enables fast, isolated tests without Spring container or database.

When to Use
Testing business logic in @Service classes
Mocking repository and external client dependencies
Verifying service interactions with mocked collaborators
Testing error handling and edge cases in services
Writing fast, isolated unit tests (no database, no API calls)
Instructions

Follow this workflow to test service layer with Mockito, including validation checkpoints:

1. Setup Test Class

Use @ExtendWith(MockitoExtension.class) to enable Mockito annotations.

2. Declare Mocks with @Mock and @InjectMocks

Use @Mock for dependencies (repositories, clients) and @InjectMocks for the service under test.

3. Arrange-Act-Assert with Validation

Arrange: Create test data and configure mock return values using when().thenReturn().

Act: Execute the service method being tested.

Assert:

Verify returned values with AssertJ assertions
Verify mock interactions with verify()
Validation checkpoint: Run test and confirm green bar
4. Test Exception Scenarios

Configure mocks to throw exceptions with when().thenThrow().

Validation checkpoint: Verify exception type and message

5. Verify Complete Coverage
Run full test suite: mvn test or gradle test
Check coverage report: mvn test jacoco:report
Validation checkpoint: Confirm all service methods have corresponding tests
Examples
Basic Service Test Pattern
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

  @Mock
  private UserRepository userRepository;

  @InjectMocks
  private UserService userService;

  @Test
  void shouldReturnUserWhenFound() {
    // Arrange
    User expected = new User(1L, "Alice");
    when(userRepository.findById(1L)).thenReturn(Optional.of(expected));

    // Act
    User result = userService.getUser(1L);

    // Assert
    assertThat(result.getName()).isEqualTo("Alice");
    verify(userRepository).findById(1L);
  }

  @Test
  void shouldThrowWhenUserNotFound() {
    // Arrange
    when(userRepository.findById(999L)).thenReturn(Optional.empty());

    // Act & Assert
    assertThatThrownBy(() -> userService.getUser(999L))
      .isInstanceOf(UserNotFoundException.class);
  }
}

Verify Method Invocations
@Test
void shouldSendEmailOnUserCreation() {
  User newUser = new User(1L, "Alice", "alice@example.com");
  when(userRepository.save(any(User.class))).thenReturn(newUser);

  enrichmentService.registerNewUser("Alice", "alice@example.com");

  verify(userRepository).save(any(User.class));
  verify(emailService).sendWelcomeEmail("alice@example.com");
}


For additional patterns (multiple dependencies, argument captors, async services, InOrder verification), see references/examples.md.

Best Practices
Use @ExtendWith(MockitoExtension.class) for JUnit 5 integration
Mock only direct dependencies of the service under test
Verify interactions to ensure correct collaboration
Test one behavior per test method - keep tests focused
Use descriptive variable names: expectedUser, actualUser, captor
Create real instances for value objects and DTOs (don't mock them)
Constraints and Warnings
Do not mock value objects or DTOs; create real instances with test data.
Avoid mocking too many dependencies; consider refactoring if a service has too many collaborators.
Tests must be independent; do not rely on execution order.
Be cautious with @Spy; partial mocking is harder to understand and maintain.
Do not test private methods directly; test them through public method behavior.
Argument matchers (any(), eq()) cannot be mixed with actual values in the same stub.
Avoid over-verifying; verify only interactions important to the test scenario.
References
Mockito Documentation
JUnit 5 User Guide
AssertJ Assertions
Weekly Installs
743
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass