---
title: 523-frameworks-micronaut-testing-acceptance-tests
url: https://skills.sh/jabrena/cursor-rules-java/523-frameworks-micronaut-testing-acceptance-tests
---

# 523-frameworks-micronaut-testing-acceptance-tests

skills/jabrena/cursor-rules-java/523-frameworks-micronaut-testing-acceptance-tests
523-frameworks-micronaut-testing-acceptance-tests
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 523-frameworks-micronaut-testing-acceptance-tests
SKILL.md
Micronaut acceptance tests from Gherkin

Implement happy-path acceptance tests from Gherkin for Micronaut using real HTTP and infrastructure.

What is covered in this Skill?

Preconditions: .feature file in context; Micronaut project confirmed
Parsing scenarios tagged @acceptance / @acceptance-tests
BaseAcceptanceTest: @MicronautTest, random port, @Client(/) HttpClient, TestPropertyProvider merging DB + WireMock URLs
wireMock.resetAll() in @BeforeEach when sharing context
Concrete *AT classes: Given/When/Then → setup, HttpClient exchange, AssertJ assertions
Maven three-tier split: *Test → Surefire, *IT + *AT → Failsafe
Happy-path scope by default

Scope: Apply recommendations based on the reference rules and step workflow.

Constraints

Do not generate without a .feature file; compile before and verify after.

PRECONDITION: Gherkin .feature file must be in context — stop and ask if not provided
PRECONDITION: The project must use Micronaut — direct the user to @133, @323, or @423 otherwise
MANDATORY: Run ./mvnw compile or mvn compile before applying any change
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed steps and safeguards
When to use this skill
Implement Micronaut acceptance tests from a Gherkin feature file
Set up BaseAcceptanceTest with Testcontainers and WireMock for Micronaut
Workflow
Read reference and assess project context

Read references/523-frameworks-micronaut-testing-acceptance-tests.md and inspect the current project setup before proposing changes.

Gather scope and decide target improvements

Identify requested outcomes, constraints, and the minimum safe set of changes to apply.

Apply framework-aligned changes

Implement or refactor configuration/code following the reference patterns and project conventions.

Run verification and report results

Execute appropriate build/tests and summarize what changed, what was verified, and any follow-up actions.

Reference

For detailed guidance, examples, and constraints, see references/523-frameworks-micronaut-testing-acceptance-tests.md.

Weekly Installs
46
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