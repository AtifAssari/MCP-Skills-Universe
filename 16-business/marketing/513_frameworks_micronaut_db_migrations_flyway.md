---
rating: ⭐⭐
title: 513-frameworks-micronaut-db-migrations-flyway
url: https://skills.sh/jabrena/cursor-rules-java/513-frameworks-micronaut-db-migrations-flyway
---

# 513-frameworks-micronaut-db-migrations-flyway

skills/jabrena/cursor-rules-java/513-frameworks-micronaut-db-migrations-flyway
513-frameworks-micronaut-db-migrations-flyway
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 513-frameworks-micronaut-db-migrations-flyway
SKILL.md
Micronaut — Database migrations (Flyway)

Apply Flyway migration guidelines for Micronaut.

What is covered in this Skill?

micronaut-flyway with JDBC/Hikari and database drivers
Versioned SQL under src/main/resources/db/migration
flyway.datasources.* (per-datasource) configuration in YAML/properties
Tests with Testcontainers and real migration chains
Coordination with @511-frameworks-micronaut-jdbc and @512-frameworks-micronaut-data

Scope: Apply recommendations based on the reference rules and good/bad examples.

Constraints

Before applying Flyway or SQL changes, ensure the project compiles. After improvements, run full verification.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed rules and good/bad patterns
EDGE CASE: If the user goal is ambiguous, stop and ask a clarifying question before editing files or running project-wide commands
EDGE CASE: If required context, files, credentials, or tools are missing, report the blocker explicitly and ask whether to proceed with setup or fallback guidance
EDGE CASE: If requested changes conflict with project constraints or safety boundaries, explain the conflict and ask for user confirmation on the preferred trade-off
When to use this skill
Add or review Flyway migrations in a Micronaut project
Configure micronaut-flyway or db/migration layout
Workflow
Read reference and assess project context

Read references/513-frameworks-micronaut-db-migrations-flyway.md and inspect the current project setup before proposing changes.

Gather scope and decide target improvements

Identify requested outcomes, constraints, and the minimum safe set of changes to apply.

Apply framework-aligned changes

Implement or refactor configuration/code following the reference patterns and project conventions.

Run verification and report results

Execute appropriate build/tests and summarize what changed, what was verified, and any follow-up actions.

Reference

For detailed guidance, examples, and constraints, see references/513-frameworks-micronaut-db-migrations-flyway.md.

Weekly Installs
42
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass