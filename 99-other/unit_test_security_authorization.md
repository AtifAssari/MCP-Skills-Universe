---
rating: ⭐⭐
title: unit-test-security-authorization
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/unit-test-security-authorization
---

# unit-test-security-authorization

skills/giuseppe-trisciuoglio/developer-kit/unit-test-security-authorization
unit-test-security-authorization
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill unit-test-security-authorization
Summary

Unit testing patterns for Spring Security authorization annotations and role-based access control.

Covers @PreAuthorize, @Secured, and @RolesAllowed method-level security with @WithMockUser test fixtures
Includes role-based access control (RBAC), expression-based authorization, and custom PermissionEvaluator testing
Provides MockMvc patterns for testing secured REST endpoints and parameterized role testing strategies
Demonstrates both allow and deny scenarios, owner-based access checks, and null authentication handling
SKILL.md
Unit Testing Security and Authorization
Overview

This skill provides patterns for unit testing Spring Security authorization logic using @PreAuthorize, @Secured, @RolesAllowed, and custom permission evaluators. It covers testing role-based access control (RBAC), expression-based authorization, custom permission evaluators, and verifying access denied scenarios without full Spring Security context.

When to Use

Use this skill when:

Testing @PreAuthorize and @Secured method-level security
Testing role-based access control (RBAC)
Testing custom permission evaluators
Verifying access denied scenarios
Testing authorization with authenticated principals
Want fast authorization tests without full Spring Security context
Instructions

Follow these steps to test Spring Security authorization:

1. Set Up Security Testing Dependencies

Add spring-security-test to your test dependencies:

<dependency>
  <groupId>org.springframework.security</groupId>
  <artifactId>spring-security-test</artifactId>
  <scope>test</scope>
</dependency>

2. Enable Method Security in Test Configuration
@Configuration
@EnableMethodSecurity
class TestSecurityConfig { }

3. Test with @WithMockUser
@Test
@WithMockUser(roles = "ADMIN")
void shouldAllowAdminAccess() {
  assertThatCode(() -> service.deleteUser(1L))
    .doesNotThrowAnyException();
}

@Test
@WithMockUser(roles = "USER")
void shouldDenyUserAccess() {
  assertThatThrownBy(() -> service.deleteUser(1L))
    .isInstanceOf(AccessDeniedException.class);
}

4. Test Custom Permission Evaluators
@Test
void shouldGrantPermissionToOwner() {
  Authentication auth = new UsernamePasswordAuthenticationToken(
    "alice", null, List.of(new SimpleGrantedAuthority("ROLE_USER"))
  );
  Document doc = new Document(1L, "Test", new User("alice"));

  boolean result = evaluator.hasPermission(auth, doc, "WRITE");
  assertThat(result).isTrue();
}

5. Validate Security is Active

If tests pass unexpectedly, add this assertion to verify security is enforced:

@Test
void shouldRejectUnauthorizedWhenSecurityEnabled() {
  assertThatThrownBy(() -> service.deleteUser(1L))
    .isInstanceOf(AccessDeniedException.class);
}

Quick Reference
Annotation	Description	Example
@PreAuthorize	Pre-invocation authorization	@PreAuthorize("hasRole('ADMIN')")
@PostAuthorize	Post-invocation authorization	@PostAuthorize("returnObject.owner == authentication.name")
@Secured	Simple role-based security	@Secured("ROLE_ADMIN")
@RolesAllowed	JSR-250 standard	@RolesAllowed({"ADMIN", "MANAGER"})
@WithMockUser	Test annotation	@WithMockUser(roles = "ADMIN")
Examples
Basic @PreAuthorize Test
@Service
public class UserService {
  @PreAuthorize("hasRole('ADMIN')")
  public void deleteUser(Long userId) {
    // delete logic
  }
}

// Test
@Test
@WithMockUser(roles = "ADMIN")
void shouldAllowAdminToDeleteUser() {
  assertThatCode(() -> service.deleteUser(1L))
    .doesNotThrowAnyException();
}

@Test
@WithMockUser(roles = "USER")
void shouldDenyUserFromDeletingUser() {
  assertThatThrownBy(() -> service.deleteUser(1L))
    .isInstanceOf(AccessDeniedException.class);
}

Expression-Based Security Test
@PreAuthorize("#userId == authentication.principal.id")
public UserProfile getUserProfile(Long userId) {
  // get profile
}

// For custom principal properties, use @WithUserDetails with a custom UserDetailsService
@Test
@WithUserDetails("alice")
void shouldAllowUserToAccessOwnProfile() {
  assertThatCode(() -> service.getUserProfile(1L))
    .doesNotThrowAnyException();
}


Validation tip: If a security test passes unexpectedly, verify that @EnableMethodSecurity is active on the test configuration — a missing annotation causes all @PreAuthorize checks to be bypassed silently.

See references/basic-testing.md for more basic patterns and references/advanced-authorization.md for complex expressions and custom evaluators.

Best Practices
Use @WithMockUser for setting authenticated user context
Test both allow and deny cases for each security rule
Test with different roles to verify role-based decisions
Test expression-based security comprehensively
Mock external dependencies (permission evaluators, etc.)
Test anonymous access separately from authenticated access
Use @EnableGlobalMethodSecurity in configuration for method-level security
Common Pitfalls
Forgetting to enable method security in test configuration
Not testing both allow and deny scenarios
Testing framework code instead of authorization logic
Not handling null authentication in tests
Mixing authentication and authorization tests unnecessarily
Constraints and Warnings
Method security requires proxy: @PreAuthorize works via proxies; direct method calls bypass security
@EnableGlobalMethodSecurity: Must be enabled for @PreAuthorize, @Secured to work
Role prefix: Spring adds "ROLE_" prefix automatically; use hasRole('ADMIN') not hasRole('ROLE_ADMIN')
Authentication context: Security context is thread-local; be careful with async tests
@WithMockUser limitations: Creates a simple Authentication; complex auth scenarios need custom setup
SpEL expressions: Complex SpEL in @PreAuthorize can be difficult to debug; test thoroughly
Performance impact: Method security adds overhead; consider security at layer boundaries
References
Setup and Configuration
references/setup.md - Maven/Gradle dependencies and security configuration
Testing Patterns
references/basic-testing.md - Basic patterns for @PreAuthorize, @Secured, MockMvc testing, and parameterized tests
Advanced Topics
references/advanced-authorization.md - Expression-based authorization, custom permission evaluators, SpEL expressions
Complete Examples
references/complete-examples.md - Before/after examples showing transition from manual to declarative security
Weekly Installs
703
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