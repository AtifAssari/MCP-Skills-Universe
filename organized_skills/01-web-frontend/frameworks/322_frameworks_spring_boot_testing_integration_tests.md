---
rating: ⭐⭐
title: 322-frameworks-spring-boot-testing-integration-tests
url: https://skills.sh/jabrena/cursor-rules-java/322-frameworks-spring-boot-testing-integration-tests
---

# 322-frameworks-spring-boot-testing-integration-tests

skills/jabrena/cursor-rules-java/322-frameworks-spring-boot-testing-integration-tests
322-frameworks-spring-boot-testing-integration-tests
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 322-frameworks-spring-boot-testing-integration-tests
SKILL.md
Spring Boot Integration Testing

Apply Spring Boot integration testing guidelines for Spring Boot 4.0.x.

What is covered in this Skill?

Integration test scope and purpose (verify wiring and contracts, not unit-test duplication)
Testcontainers with @ServiceConnection for zero-config wiring (preferred)
@DynamicPropertySource as fallback for containers without built-in service connection support
Static @Container instances shared across test methods for performance
MockMvcTester for fluent AssertJ-based HTTP assertions (Spring Boot 4.0.x)
TestRestTemplate for full HTTP stack testing
@DataJdbcTest / @DataJpaTest persistence slices (load only persistence layer, start faster)
Data isolation: each test owns its scenario; no shared mutable state or ordering assumptions
@MockitoBean for mock registration (Spring Boot 4.0.x — @MockBean removed)
Resource lifecycle: Testcontainers JUnit integration for teardown; *IT / integration test separation

Scope: Apply recommendations based on the reference rules and good/bad code examples.

Constraints

Before applying any integration test changes, ensure the project compiles. If compilation fails, stop immediately. After applying improvements, run full verification.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed rules and good/bad patterns
EDGE CASE: If request scope is ambiguous, stop and ask a clarifying question before applying changes
EDGE CASE: If required inputs, files, or tooling are missing, report what is missing and ask whether to proceed with setup guidance
When to use this skill
Review Java code for Spring Boot integration tests
Apply best practices for Spring Boot integration tests in Java code
Workflow
Read reference and assess project context

Read references/322-frameworks-spring-boot-testing-integration-tests.md and inspect the current project setup before proposing changes.

Gather scope and decide target improvements

Identify requested outcomes, constraints, and the minimum safe set of changes to apply.

Apply framework-aligned changes

Implement or refactor configuration/code following the reference patterns and project conventions.

Run verification and report results

Execute appropriate build/tests and summarize what changed, what was verified, and any follow-up actions.

Reference

For detailed guidance, examples, and constraints, see references/322-frameworks-spring-boot-testing-integration-tests.md.

Weekly Installs
58
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass