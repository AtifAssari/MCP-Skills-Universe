---
title: sqlc
url: https://skills.sh/kalbasit/ncps/sqlc
---

# sqlc

skills/kalbasit/ncps/sqlc
sqlc
Installation
$ npx skills add https://github.com/kalbasit/ncps --skill sqlc
SKILL.md
SQLC Skill

This skill provides instructions for working with sqlc and database queries in the NCPS repository. NCPS supports multiple database engines (SQLite, PostgreSQL, MySQL), and sqlc is used to generate type-safe Go code from SQL queries for each engine.

Configuration
SQLC Config: sqlc.yml
Queries:
SQLite: db/query.sqlite.sql
PostgreSQL: db/query.postgres.sql
MySQL: db/query.mysql.sql
Output:
SQLite: pkg/database/sqlitedb
PostgreSQL: pkg/database/postgresdb
MySQL: pkg/database/mysqldb
Workflow for Query Changes

Any time a query file (db/query.<engine>.sql) is updated, you MUST follow these steps:

1. Generate SQLC Code

Run the sqlc generate command to update the generated Go files for all engines.

sqlc generate

2. Regenerate Database Wrappers and Models

Run go generate for the pkg/database package. This command uses sqlc-multi-db (via go tool) to automatically:

Extract the Querier interface from the postgresdb backend.
Generate the common Querier interface in pkg/database/querier.go.
Generate common domain models in pkg/database/models.go.
Generate database wrappers (wrapper_sqlite.go, wrapper_postgres.go, wrapper_mysql.go).
go generate ./pkg/database


[!IMPORTANT] Do NOT manually edit pkg/database/querier.go or pkg/database/models.go. They are fully automated.

Best Practices

Consistency: Ensure that equivalent queries exist for all supported engines unless the feature is engine-specific.

Linting: Use sqlfluff to lint and format SQL files before running sqlc generate.

sqlfluff lint db/query.*.sql
sqlfluff format db/query.*.sql

Weekly Installs
90
Repository
kalbasit/ncps
GitHub Stars
297
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass