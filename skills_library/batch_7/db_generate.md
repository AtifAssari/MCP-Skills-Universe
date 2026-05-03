---
title: db-generate
url: https://skills.sh/medusajs/medusa-agent-skills/db-generate
---

# db-generate

skills/medusajs/medusa-agent-skills/db-generate
db-generate
Installation
$ npx skills add https://github.com/medusajs/medusa-agent-skills --skill db-generate
Summary

Generate database migrations for Medusa modules with a single command.

Wraps the npx medusa db:generate CLI command to create migration files for specified Medusa modules
Accepts module name as an argument and reports migration file location, errors, and next steps
Automatically suggests running npx medusa db:migrate after generation to apply migrations
SKILL.md
Generate Database Migrations

Generate database migrations for the specified Medusa module.

The user will provide the module name as an argument (e.g., brand, product, custom-module).

For example: /medusa-dev:db-generate brand

Use the Bash tool to execute the command npx medusa db:generate <module-name>, replacing <module-name> with the provided argument.

Report the results to the user, including:

The module name for which migrations were generated
Migration file name or location
Any errors or warnings
Next steps (running npx medusa db:migrate to apply the migrations)
Weekly Installs
943
Repository
medusajs/medusa…t-skills
GitHub Stars
156
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass