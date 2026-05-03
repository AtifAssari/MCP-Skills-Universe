---
rating: ⭐⭐
title: unit-test-bean-validation
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/unit-test-bean-validation
---

# unit-test-bean-validation

skills/giuseppe-trisciuoglio/developer-kit/unit-test-bean-validation
unit-test-bean-validation
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill unit-test-bean-validation
Summary

Unit testing Jakarta Bean Validation constraints and custom validators without Spring context.

Covers testing built-in constraints (@NotNull, @Email, @Min, @Max, @Size) and custom @Constraint implementations with violation assertion patterns
Includes cross-field validation, validation groups for conditional rules, and parameterized test scenarios for multiple inputs
Provides setup patterns using Validation.buildDefaultValidatorFactory().getValidator() and assertion helpers to extract property paths, messages, and invalid values
Emphasizes testing both valid and invalid cases, edge cases (null, empty, whitespace), and error message verification at the unit level before service or controller testing
SKILL.md
Unit Testing Jakarta Bean Validation
Overview

This skill provides executable patterns for unit testing Jakarta Bean Validation annotations and custom validators using JUnit 5. Covers built-in constraints (@NotNull, @Email, @Min, @Max, @Size), custom @Constraint implementations, cross-field validation, and validation groups. Tests run in isolation without Spring context.

When to Use
Writing unit tests for Jakarta Bean Validation or JSR-380 constraints
Testing custom @Constraint validators and constraint violation messages
Testing bean validation logic in DTOs and request objects
Verifying cross-field validation (e.g., password matching)
Testing conditional validation with validation groups
Fast validation tests without Spring Boot context
Instructions
Add dependencies: Include jakarta.validation-api and hibernate-validator in test scope
Create base test class: Build Validator once in @BeforeEach using Validation.buildDefaultValidatorFactory()
Test valid cases first: Verify objects pass without violations
Test invalid cases: Assert constraint violations include correct property path and message
Extract violation details: Use getPropertyPath(), getMessage(), getInvalidValue()
Test custom validators: See references/custom-validators.md for patterns
Use parameterized tests: Test multiple inputs efficiently with @ParameterizedTest
Group validation tests: Use validation groups for conditional rules (see references/advanced-patterns.md)
Examples
Maven Setup
<dependency>
  <groupId>jakarta.validation</groupId>
  <artifactId>jakarta.validation-api</artifactId>
</dependency>
<dependency>
  <groupId>org.hibernate.validator</groupId>
  <artifactId>hibernate-validator</artifactId>
  <scope>test</scope>
</dependency>
<dependency>
  <groupId>org.assertj</groupId>
  <artifactId>assertj-core</artifactId>
  <scope>test</scope>
</dependency>

Common Test Setup
import jakarta.validation.*;
import jakarta.validation.ConstraintViolation;
import jakarta.validation.path.Path;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.*;

class BaseValidationTest {
  protected Validator validator;

  @BeforeEach
  void setUpValidator() {
    validator = Validation.buildDefaultValidatorFactory().getValidator();
  }
}

Testing Basic Constraints
class UserDtoTest extends BaseValidationTest {

  @Test
  void shouldPassValidationWithValidUser() {
    UserDto user = new UserDto("Alice", "alice@example.com", 25);
    assertThat(validator.validate(user)).isEmpty();
  }

  @Test
  void shouldFailWhenNameIsNull() {
    UserDto user = new UserDto(null, "alice@example.com", 25);
    assertThat(validator.validate(user))
      .extracting(ConstraintViolation::getMessage)
      .contains("must not be blank");
  }

  @Test
  void shouldFailWhenEmailIsInvalid() {
    UserDto user = new UserDto("Alice", "invalid-email", 25);
    Set<ConstraintViolation<UserDto>> violations = validator.validate(user);
    assertThat(violations)
      .extracting(ConstraintViolation::getPropertyPath)
      .extracting(Path::toString)
      .contains("email");
  }

  @Test
  void shouldFailWhenAgeIsBelowMinimum() {
    UserDto user = new UserDto("Alice", "alice@example.com", -1);
    assertThat(validator.validate(user))
      .extracting(ConstraintViolation::getMessage)
      .contains("must be greater than or equal to 0");
  }

  @Test
  void shouldFailWhenMultipleConstraintsViolated() {
    UserDto user = new UserDto(null, "invalid", -5);
    assertThat(validator.validate(user)).hasSize(3);
  }
}

Testing Custom Validators

For custom constraint patterns, see references/custom-validators.md:

Creating @Constraint annotations
Implementing ConstraintValidator
Cross-field validation (password matching)
Stateless validator best practices
Testing Validation Groups

For validation groups and parameterized tests, see references/advanced-patterns.md:

Defining validation group interfaces
Conditional validation with groups parameter
@ParameterizedTest with @ValueSource and @CsvSource
Debugging failed validation tests
Best Practices
Test both valid and invalid: Every constraint needs both passing and failing test cases
Assert violation details: Verify property path, message, and constraint type
Test edge cases: null, empty string, whitespace-only, boundary values
Keep validators stateless: Custom validators must not maintain state
Use clear messages: Constraint messages should be user-friendly
Group related tests: Extend BaseValidationTest to share validator setup
Test error messages: Ensure messages match requirements
Common Pitfalls
Forgetting to test null values (most constraints ignore null by default)
Not verifying the property path in constraint violations
Testing validation at service/controller level instead of unit level
Creating overly complex custom validators
Missing @NotNull for mandatory fields combined with other constraints
Constraints and Warnings
Null handling: Most constraints ignore null by default — combine @NotNull with other constraints for mandatory fields
Thread safety: Validator instances are thread-safe and can be shared
Message localization: Test with different locales if i18n is required
Cascading validation: Use @Valid on nested objects for recursive validation
Custom validators: Must be stateless and return true for null values
Test isolation: Validation unit tests should not depend on Spring context or database
Troubleshooting

ValidatorFactory not found: Ensure jakarta.validation-api and hibernate-validator are on test classpath.

Custom validator not invoked: Verify @Constraint(validatedBy = YourValidator.class) annotation is correct.

Null values pass validation: This is expected behavior — constraints ignore null unless @NotNull is present.

Wrong violation count: Use hasSize() to verify exact count, check all fields in the object.

Property path incorrect: Ensure the field, not the getter, has the constraint annotation.

References
Jakarta Bean Validation Spec
Hibernate Validator
Custom validators and cross-field validation: references/custom-validators.md
Validation groups and parameterized tests: references/advanced-patterns.md
Weekly Installs
1.9K
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