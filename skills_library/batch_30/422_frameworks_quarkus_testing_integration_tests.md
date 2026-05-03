---
title: 422-frameworks-quarkus-testing-integration-tests
url: https://skills.sh/jabrena/cursor-rules-java/422-frameworks-quarkus-testing-integration-tests
---

# 422-frameworks-quarkus-testing-integration-tests

skills/jabrena/cursor-rules-java/422-frameworks-quarkus-testing-integration-tests
422-frameworks-quarkus-testing-integration-tests
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 422-frameworks-quarkus-testing-integration-tests
SKILL.md
Quarkus Integration Testing

Apply integration testing patterns for Quarkus with real wiring and reproducible infrastructure.

What is covered in this Skill?

@QuarkusTest for in-JVM integration with real CDI wiring
Dev Services for automatic container provisioning (%test.quarkus.datasource.devservices)
Testcontainers via QuarkusTestResourceLifecycleManager (start/stop lifecycle, dynamic config injection)
WireMock for stubbing external HTTP services via QuarkusTestResourceLifecycleManager
@QuarkusIntegrationTest for black-box testing against the packaged JAR or native binary
HTTP testing with REST Assured against the Quarkus test port
Data isolation: @TestTransaction for automatic rollback; @BeforeEach cleanup for HTTP tests
Maven three-tier split: *Test → Surefire (fast), *IT + *AT → Failsafe (verify)
Native-image test considerations with @DisabledOnNativeImage

Scope: Apply recommendations based on the reference rules and good/bad code examples.

Constraints

Compile before changes; verify after; Docker may be required for containers.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
PREREQUISITE: Project must compile before applying integration test improvements
SAFETY: If compilation fails, stop immediately
BLOCKING CONDITION: Compilation errors must be resolved by the user before proceeding
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements; Docker is required for Testcontainers and Dev Services
BEFORE APPLYING: Read the reference for detailed rules and examples
When to use this skill
Add or improve integration tests in a Quarkus project
Configure Testcontainers or Dev Services for Quarkus tests
Add WireMock stubs for external HTTP dependencies in Quarkus integration tests
Set up @QuarkusIntegrationTest for packaged artifact or native binary testing
Fix test data isolation or configure Maven Surefire/Failsafe split
Workflow
Read reference and assess project context

Read references/422-frameworks-quarkus-testing-integration-tests.md and inspect the current project setup before proposing changes.

Gather scope and decide target improvements

Identify requested outcomes, constraints, and the minimum safe set of changes to apply.

Apply framework-aligned changes

Implement or refactor configuration/code following the reference patterns and project conventions.

Run verification and report results

Execute appropriate build/tests and summarize what changed, what was verified, and any follow-up actions.

Reference

For detailed guidance, examples, and constraints, see references/422-frameworks-quarkus-testing-integration-tests.md.

Weekly Installs
49
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