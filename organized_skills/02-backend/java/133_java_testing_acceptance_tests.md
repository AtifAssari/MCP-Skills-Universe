---
rating: ⭐⭐
title: 133-java-testing-acceptance-tests
url: https://skills.sh/jabrena/cursor-rules-java/133-java-testing-acceptance-tests
---

# 133-java-testing-acceptance-tests

skills/jabrena/cursor-rules-java/133-java-testing-acceptance-tests
133-java-testing-acceptance-tests
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 133-java-testing-acceptance-tests
SKILL.md
Java acceptance tests from Gherkin

Implement acceptance tests from Gherkin feature files. Given a .feature file in context, find @acceptance-tagged scenarios and implement happy-path tests with RestAssured, Testcontainers, and WireMock.

What is covered in this Skill?

Parse Gherkin .feature files to find scenarios tagged @acceptance or @acceptance-tests
Implement happy-path acceptance tests (one test per scenario)
RestAssured for REST API testing (given/when/then, status codes, JSON body assertions)
Testcontainers for databases (PostgreSQL, etc.) and Kafka
WireMock for stubbing external REST APIs
BaseAcceptanceTest base class with @BeforeAll coordinate propagation via System.setProperty
Given-When-Then structure mapping Gherkin steps to setup, request, and assertions
Maven dependencies: rest-assured, testcontainers, wiremock-standalone

Preconditions: (1) The Gherkin .feature file must be in context. (2) The project must NOT use Spring Boot, Quarkus, or Micronaut — for those frameworks, use @323-frameworks-spring-boot-testing-acceptance-tests or framework-specific rules.

Scope: Implements only happy-path scenarios. Use the reference for detailed examples and constraints.

Constraints

Before applying any acceptance test changes, ensure the Gherkin .feature file is in context and the project compiles. If compilation fails or the feature file is missing, stop immediately.

PRECONDITION: The Gherkin .feature file MUST be in context; the project MUST NOT use Spring Boot, Quarkus, or Micronaut
MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately and do not proceed
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed examples, good/bad patterns, and constraints
When to use this skill
Review Java code for acceptance tests
Apply best practices for acceptance tests in Java code
Workflow
Validate preconditions and compile project

Confirm .feature file is in context and framework scope is valid, then run ./mvnw compile or mvn compile; stop if any precondition fails.

Read acceptance-testing reference and parse scenarios

Read references/133-java-testing-acceptance-tests.md and extract @acceptance scenarios for happy-path implementation.

Implement acceptance test infrastructure and scenarios

Create or update base test infrastructure (RestAssured, Testcontainers, WireMock) and implement one happy-path test per accepted scenario.

Verify with full build

Run ./mvnw clean verify or mvn clean verify after applying improvements.

Reference

For detailed guidance, examples, and constraints, see references/133-java-testing-acceptance-tests.md.

Weekly Installs
57
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