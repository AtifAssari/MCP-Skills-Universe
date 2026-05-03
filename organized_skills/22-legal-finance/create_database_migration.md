---
rating: ⭐⭐
title: create database migration
url: https://skills.sh/tryghost/ghost/create-database-migration
---

# create database migration

skills/tryghost/ghost/Create database migration
Create database migration
Installation
$ npx skills add https://github.com/tryghost/ghost --skill 'Create database migration'
SKILL.md
Create Database Migration
Instructions
Create a new, empty migration file: cd ghost/core && yarn migrate:create <kebab-case-slug>. IMPORTANT: do not create the migration file manually; always use this script to create the initial empty migration file. The slug must be kebab-case (e.g. add-column-to-posts).
The above command will create a new directory in ghost/core/core/server/data/migrations/versions if needed, create the empty migration file with the appropriate name, and bump the core and admin package versions to RC if this is the first migration after a release.
Update the migration file with the changes you want to make in the database, following the existing patterns in the codebase. Where appropriate, prefer to use the utility functions in ghost/core/core/server/data/migrations/utils/*.
Update the schema definition file in ghost/core/core/server/data/schema/schema.js, and make sure it aligns with the latest changes from the migration.
Test the migration manually: yarn knex-migrator migrate --v {version directory} --force
If adding or dropping a table, update ghost/core/core/server/data/exporter/table-lists.js as appropriate.
If adding or dropping a table, also add or remove the table name from the expected tables list in ghost/core/test/integration/exporter/exporter.test.js. This test has a hardcoded alphabetically-sorted array of all database tables — it runs in CI integration tests (not unit tests) and will fail if the new table is missing.
Run the schema integrity test, and update the hash: yarn test:single test/unit/server/data/schema/integrity.test.js
Run unit tests in Ghost core, and iterate until they pass: cd ghost/core && yarn test:unit
Examples

See examples.md for example migrations.

Rules

See rules.md for rules that should always be followed when creating database migrations.

Weekly Installs
–
Repository
tryghost/ghost
GitHub Stars
52.7K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass