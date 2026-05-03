---
title: oracle-db-skills
url: https://skills.sh/krisrice/oracle-db-skills/oracle-db-skills
---

# oracle-db-skills

skills/krisrice/oracle-db-skills/oracle-db-skills
oracle-db-skills
Installation
$ npx skills add https://github.com/krisrice/oracle-db-skills --skill oracle-db-skills
SKILL.md
Oracle DB Skills

A collection of 103 standalone reference guides for Oracle Database. Each file covers one topic with explanations, practical examples, best practices, and common mistakes.

How to Use
Find the right skill using the category routing table below.
Read only the file(s) relevant to the user's task — do not load all files at once.
Apply the guidance to answer questions, generate code, or review existing work.
Category Routing
User asks about…	Read from
Backup, recovery, RMAN, Data Guard, redo/undo logs, users	skills/admin/
JDBC, connection pooling, JSON, XML, spatial, full-text, transactions	skills/appdev/
RAC, CDB/PDB, Exadata, In-Memory, OCI, ATP/ADW	skills/architecture/
ERD, data modeling, partitioning, tablespaces	skills/design/
Liquibase, Flyway, online operations, EBR, utPLSQL, git for SQL	skills/devops/
Advanced Queuing, DBMS_SCHEDULER, materialized views, DBLinks, APEX	skills/features/
Migrating from PostgreSQL, MySQL, SQL Server, MongoDB, etc.	skills/migrations/
Alert log, ADR, adrci, space, top SQL, health checks	skills/monitoring/
ORDS, REST APIs, OAuth2, AutoREST, PL/SQL gateway	skills/ords/
AWR, ASH, explain plan, indexes, optimizer stats, wait events, memory	skills/performance/
Packages, cursors, collections, error handling, unit testing, debugging	skills/plsql/
Privileges, VPD, TDE, encryption, auditing, network security	skills/security/
SQL patterns, window functions, CTEs, dynamic SQL, injection	skills/sql-dev/
SQLcl commands, scripting, Liquibase CLI, MCP server, CI/CD	skills/sqlcl/
Skills Directory
skills/
├── admin/          Database administration (backup, recovery, users, redo/undo)
├── appdev/         Application development (JSON, XML, spatial, text, pooling)
├── architecture/   Infrastructure (RAC, Multitenant, Exadata, In-Memory, OCI)
├── design/         Schema design (ERD, modeling, partitioning, tablespaces)
├── devops/         CI/CD and DevOps (migrations, EBR, testing, version control)
├── features/       Oracle features (AQ, Scheduler, MVs, DBLinks, APEX)
├── migrations/     Migrating from other databases to Oracle
├── monitoring/     Diagnostics (alert log, ADR, health, space, top SQL)
├── ords/           Oracle REST Data Services
├── performance/    Tuning (AWR, ASH, indexes, optimizer, wait events, memory)
├── plsql/          PL/SQL development (packages, cursors, collections, testing)
├── security/       Security (privileges, VPD, TDE, auditing, network)
├── sql-dev/        SQL development (tuning, patterns, dynamic SQL, injection)
└── sqlcl/          SQLcl CLI tool (basics, scripting, Liquibase, MCP server)

Key Starting Points
skills/sqlcl/sqlcl-mcp-server.md — connecting AI assistants to Oracle via the SQLcl MCP server
skills/migrations/migration-assessment.md — start here for any database migration project
skills/performance/explain-plan.md — foundation for all SQL performance work
skills/plsql/plsql-package-design.md — foundation for PL/SQL architecture questions
skills/devops/schema-migrations.md — Liquibase/Flyway with Oracle in CI/CD pipelines
Weekly Installs
272
Repository
krisrice/oracle…b-skills
GitHub Stars
410
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass