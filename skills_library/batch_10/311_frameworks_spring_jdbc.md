---
title: 311-frameworks-spring-jdbc
url: https://skills.sh/jabrena/cursor-rules-java/311-frameworks-spring-jdbc
---

# 311-frameworks-spring-jdbc

skills/jabrena/cursor-rules-java/311-frameworks-spring-jdbc
311-frameworks-spring-jdbc
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 311-frameworks-spring-jdbc
SKILL.md
Spring JDBC — JdbcClient (Spring Framework 7+)

Apply Spring JDBC guidelines with JdbcClient as the default; use JdbcTemplate / NamedParameterJdbcTemplate only for legacy code or APIs not covered by JdbcClient (batch updates, KeyHolder, RowCallbackHandler streaming).

What is covered in this Skill?

Parameterized SQL (never concatenate user input)
JdbcClient fluent API (Spring Framework 7+) — preferred for queries and updates
Named parameters via JdbcClient; NamedParameterJdbcTemplate for legacy migration
RowMapper, query(Class), and records
Batch operations and generated keys (JdbcTemplate / JdbcOperations where needed)
Safe handling of generated keys (KeyHolder; single-row JdbcClient updates)
Service-layer @Transactional boundaries
Read-only transactions (@Transactional(readOnly = true))
Safe single-row access (optional() / findFirst() vs queryForObject)
Streaming large result sets (RowCallbackHandler, ResultSetExtractor)
DataAccessException handling (DuplicateKeyException, EmptyResultDataAccessException)
@JdbcTest slice testing with @Sql fixtures

Scope: Apply recommendations based on the reference rules and good/bad code examples.

Constraints

Before applying any Spring JDBC changes, ensure the project compiles. If compilation fails, stop immediately. After applying improvements, run full verification.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
SQL INJECTION: Never concatenate untrusted input into SQL strings — always use bind parameters
BEFORE APPLYING: Read the reference for detailed rules and good/bad patterns
When to use this skill
Review Java code for Spring JDBC (JdbcTemplate, JdbcClient, NamedParameterJdbcTemplate)
Apply best practices for Spring JDBC data access in Java code
Detect and fix SQL injection risks in JDBC code
Improve transaction boundaries or exception handling for JDBC operations
Workflow
Read reference and assess project context

Read references/311-frameworks-spring-jdbc.md and inspect the current project setup before proposing changes.

Gather scope and decide target improvements

Identify requested outcomes, constraints, and the minimum safe set of changes to apply.

Apply framework-aligned changes

Implement or refactor configuration/code following the reference patterns and project conventions.

Run verification and report results

Execute appropriate build/tests and summarize what changed, what was verified, and any follow-up actions.

Reference

For detailed guidance, examples, and constraints, see references/311-frameworks-spring-jdbc.md.

Weekly Installs
53
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass