---
rating: ⭐⭐
title: 421-frameworks-quarkus-testing-unit-tests
url: https://skills.sh/jabrena/cursor-rules-java/421-frameworks-quarkus-testing-unit-tests
---

# 421-frameworks-quarkus-testing-unit-tests

skills/jabrena/cursor-rules-java/421-frameworks-quarkus-testing-unit-tests
421-frameworks-quarkus-testing-unit-tests
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 421-frameworks-quarkus-testing-unit-tests
SKILL.md
Quarkus Unit Testing

Apply fast testing strategies for Quarkus: Mockito-first, QuarkusTest when CDI wiring matters.

What is covered in this Skill?

Pure JUnit 5 + Mockito without container boot (@ExtendWith(MockitoExtension.class))
@QuarkusTest with @InjectMock for full CDI bean replacement
@InjectSpy for partial mocking — real bean wrapped as spy, specific methods overridden
REST Assured for HTTP-level @QuarkusTest resource tests
@ParameterizedTest with @CsvSource (inline data) and @MethodSource (complex objects)
QuarkusTestProfile and @TestProfile for test-specific configuration overrides
Naming conventions: *Test → Surefire (fast phase), *IT → Failsafe (verify phase)
When to escalate to integration tests (@422)

Scope: Apply recommendations based on the reference rules and good/bad code examples.

Constraints

Compile before test refactors; verify the full suite after.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
PREREQUISITE: Project must compile before applying test improvements
SAFETY: If compilation fails, stop immediately
BLOCKING CONDITION: Compilation errors must be resolved by the user before proceeding
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed rules and examples
When to use this skill
Add or improve unit tests in a Quarkus project
Reduce slow @QuarkusTest usage with Mockito-first tests
Add @InjectSpy partial mocking or QuarkusTestProfile configuration in Quarkus tests
Convert repeated test methods to @ParameterizedTest with @CsvSource or @MethodSource
Workflow
Read reference and assess project context

Read references/421-frameworks-quarkus-testing-unit-tests.md and inspect the current project setup before proposing changes.

Gather scope and decide target improvements

Identify requested outcomes, constraints, and the minimum safe set of changes to apply.

Apply framework-aligned changes

Implement or refactor configuration/code following the reference patterns and project conventions.

Run verification and report results

Execute appropriate build/tests and summarize what changed, what was verified, and any follow-up actions.

Reference

For detailed guidance, examples, and constraints, see references/421-frameworks-quarkus-testing-unit-tests.md.

Weekly Installs
50
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass