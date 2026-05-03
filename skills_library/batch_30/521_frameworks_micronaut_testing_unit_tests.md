---
title: 521-frameworks-micronaut-testing-unit-tests
url: https://skills.sh/jabrena/cursor-rules-java/521-frameworks-micronaut-testing-unit-tests
---

# 521-frameworks-micronaut-testing-unit-tests

skills/jabrena/cursor-rules-java/521-frameworks-micronaut-testing-unit-tests
521-frameworks-micronaut-testing-unit-tests
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 521-frameworks-micronaut-testing-unit-tests
SKILL.md
Micronaut Unit Testing

Apply fast testing strategies for Micronaut: Mockito-first, narrow @MicronautTest when HTTP or DI replacement is required.

What is covered in this Skill?

Pure JUnit 5 + Mockito without container boot
@MicronautTest with @MockBean factory methods for collaborators
HttpClient blocking exchanges against the embedded server
@Property for deterministic configuration in tests
@ParameterizedTest with @CsvSource / @MethodSource
Naming: *Test → Surefire; *IT → Failsafe when configured
When to escalate to @522

Scope: Apply recommendations based on the reference rules and good/bad code examples.

Constraints

Compile before test refactors; verify the full suite after.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed rules and examples
EDGE CASE: If request scope is ambiguous, stop and ask a clarifying question before applying changes
EDGE CASE: If required inputs, files, or tooling are missing, report what is missing and ask whether to proceed with setup guidance
When to use this skill
Add or improve unit tests in a Micronaut project
Reduce unnecessary @MicronautTest usage with Mockito-first tests
Workflow
Read reference and assess project context

Read references/521-frameworks-micronaut-testing-unit-tests.md and inspect the current project setup before proposing changes.

Gather scope and decide target improvements

Identify requested outcomes, constraints, and the minimum safe set of changes to apply.

Apply framework-aligned changes

Implement or refactor configuration/code following the reference patterns and project conventions.

Run verification and report results

Execute appropriate build/tests and summarize what changed, what was verified, and any follow-up actions.

Reference

For detailed guidance, examples, and constraints, see references/521-frameworks-micronaut-testing-unit-tests.md.

Weekly Installs
47
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass