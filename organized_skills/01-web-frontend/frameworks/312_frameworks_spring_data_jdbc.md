---
rating: ⭐⭐
title: 312-frameworks-spring-data-jdbc
url: https://skills.sh/jabrena/cursor-rules-java/312-frameworks-spring-data-jdbc
---

# 312-frameworks-spring-data-jdbc

skills/jabrena/cursor-rules-java/312-frameworks-spring-data-jdbc
312-frameworks-spring-data-jdbc
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 312-frameworks-spring-data-jdbc
SKILL.md
Spring Data JDBC with Records

Apply Spring Data JDBC guidelines with Java records.

What is covered in this Skill?

Records for entity classes (immutable, constructor-friendly)
@Table for naming when record name differs from the table name
@Embedded to inline value-object columns into the parent row without a separate table
Repository pattern
Immutable updates with static factories for new rows and with* helpers for updates
save() INSERT vs UPDATE semantics driven by @Id nullability
Aggregate boundaries: one repository per aggregate root, Set for one-to-many inside the root, foreign keys between aggregates
Custom queries with @Query and named parameters (no user-input concatenation)
Transaction management (@Transactional on services; readOnly where appropriate)
Single query loading (N+1 avoidance)

Scope: Apply recommendations based on the reference rules and good/bad code examples.

Constraints

Before applying any Spring Data JDBC changes, ensure the project compiles. If compilation fails, stop immediately. After applying improvements, run full verification.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed rules and good/bad patterns
EDGE CASE: If request scope is ambiguous, stop and ask a clarifying question before applying changes
EDGE CASE: If required inputs, files, or tooling are missing, report what is missing and ask whether to proceed with setup guidance
When to use this skill
Review Java code for Spring Data JDBC
Apply best practices for Spring Data JDBC in Java code
Workflow
Read reference and assess project context

Read references/312-frameworks-spring-data-jdbc.md and inspect the current project setup before proposing changes.

Gather scope and decide target improvements

Identify requested outcomes, constraints, and the minimum safe set of changes to apply.

Apply framework-aligned changes

Implement or refactor configuration/code following the reference patterns and project conventions.

Run verification and report results

Execute appropriate build/tests and summarize what changed, what was verified, and any follow-up actions.

Reference

For detailed guidance, examples, and constraints, see references/312-frameworks-spring-data-jdbc.md.

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