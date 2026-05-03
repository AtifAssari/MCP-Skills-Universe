---
title: 411-frameworks-quarkus-jdbc
url: https://skills.sh/jabrena/cursor-rules-java/411-frameworks-quarkus-jdbc
---

# 411-frameworks-quarkus-jdbc

skills/jabrena/cursor-rules-java/411-frameworks-quarkus-jdbc
411-frameworks-quarkus-jdbc
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 411-frameworks-quarkus-jdbc
SKILL.md
Quarkus JDBC — programmatic SQL

Apply programmatic JDBC patterns in Quarkus with safe SQL and clear transactions.

What is covered in this Skill?

Injected javax.sql.DataSource (Agroal-backed) and try-with-resources for Connection / PreparedStatement
PreparedStatement with bind parameters — never string concatenation
Mapping ResultSet rows to Java records (dedicated mapRow method)
Safe single-row queries with Optional; never assume rs.next() succeeds
SQLException translation to domain exceptions (catch-translate-rethrow)
Streaming large result sets with setFetchSize to avoid OOM
Batch updates with addBatch / executeBatch for bulk inserts
@Transactional service boundaries and propagation types (TxType.REQUIRES_NEW for independent commits)
CDI self-invocation pitfall: always call transactional methods through the injected proxy
Dev Services for databases in dev/test
When to prefer Panache (@412) vs raw JDBC

Scope: Apply recommendations based on the reference rules and good/bad code examples.

Constraints

Compile before JDBC refactors; verify after changes.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
PREREQUISITE: Project must compile before applying JDBC improvements
SAFETY: If compilation fails, stop immediately
BLOCKING CONDITION: Compilation errors must be resolved by the user before proceeding
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed rules and examples
When to use this skill
Review JDBC or SQL data access in a Quarkus project
Improve transactions and parameter binding for Quarkus JDBC
Translate SQLException to domain exceptions or stream large result sets
Fix CDI self-invocation bypassing @Transactional in Quarkus
Workflow
Read reference and assess project context

Read references/411-frameworks-quarkus-jdbc.md and inspect the current project setup before proposing changes.

Gather scope and decide target improvements

Identify requested outcomes, constraints, and the minimum safe set of changes to apply.

Apply framework-aligned changes

Implement or refactor configuration/code following the reference patterns and project conventions.

Run verification and report results

Execute appropriate build/tests and summarize what changed, what was verified, and any follow-up actions.

Reference

For detailed guidance, examples, and constraints, see references/411-frameworks-quarkus-jdbc.md.

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