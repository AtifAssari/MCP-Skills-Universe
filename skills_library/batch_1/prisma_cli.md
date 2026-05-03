---
title: prisma-cli
url: https://skills.sh/prisma/skills/prisma-cli
---

# prisma-cli

skills/prisma/skills/prisma-cli
prisma-cli
Installation
$ npx skills add https://github.com/prisma/skills --skill prisma-cli
Summary

Complete reference for Prisma CLI commands, options, and workflows across setup, migrations, and database operations.

Covers 20+ commands organized by priority: setup (init), generation (generate), development (dev), database operations (db pull/push/seed/execute), and migrations (migrate dev/deploy/reset/status/diff/resolve)
Includes Prisma 7.x changes: new prisma.config.ts configuration file, removed flags (--skip-generate, --skip-seed, --schema, --url), and explicit environment variable loading via dotenv
Supports local Prisma Postgres development (prisma dev), schema introspection (db pull), direct schema application (db push), and database seeding
Provides Bun runtime support with --bun flag and utility commands for schema validation, formatting, and Prisma Studio access
SKILL.md
Prisma CLI Reference

Complete reference for all Prisma CLI commands. This skill provides guidance on command usage, options, and best practices for current Prisma releases.

When to Apply

Reference this skill when:

Setting up a new Prisma project (prisma init)
Generating Prisma Client (prisma generate)
Running database migrations (prisma migrate)
Managing database state (prisma db push/pull)
Using local development database (prisma dev)
Debugging Prisma issues (prisma debug)
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Setup	HIGH	init
2	Generation	HIGH	generate
3	Development	HIGH	dev
4	Database	HIGH	db-
5	Migrations	CRITICAL	migrate-
6	Utility	MEDIUM	studio, validate, format, debug, mcp
Command Categories
Category	Commands	Purpose
Setup	init	Bootstrap new Prisma project
Generation	generate	Generate Prisma Client
Validation	validate, format	Schema validation and formatting
Development	dev	Local Prisma Postgres for development
Database	db pull, db push, db seed, db execute	Direct database operations
Migrations	migrate dev, migrate deploy, migrate reset, migrate status, migrate diff, migrate resolve	Schema migrations
Utility	studio, mcp, version, debug	Development and AI tooling
Quick Reference
Project Setup
# Initialize new project (creates prisma/ folder and prisma.config.ts)
prisma init

# Initialize with specific database
prisma init --datasource-provider postgresql
prisma init --datasource-provider mysql
prisma init --datasource-provider sqlite

# Initialize with Prisma Postgres (cloud)
prisma init --db

# Initialize with an example model
prisma init --with-model

Client Generation
# Generate Prisma Client
prisma generate

# Watch mode for development
prisma generate --watch

# Generate specific generator only
prisma generate --generator client

Bun Runtime

When using Bun, always add the --bun flag so Prisma runs with the Bun runtime (otherwise it falls back to Node.js because of the CLI shebang):

bunx --bun prisma init
bunx --bun prisma generate

Local Development Database
# Start local Prisma Postgres
prisma dev

# Start with specific name
prisma dev --name myproject

# Start in background (detached)
prisma dev --detach

# List all local instances
prisma dev ls

# Stop instance
prisma dev stop myproject

# Remove instance data
prisma dev rm myproject

Database Operations
# Pull schema from existing database
prisma db pull

# Push schema to database (no migrations)
prisma db push

# Seed database
prisma db seed

# Execute raw SQL
prisma db execute --file ./script.sql

Migrations (Development)
# Create and apply migration
prisma migrate dev

# Create migration with name
prisma migrate dev --name add_users_table

# Create migration without applying
prisma migrate dev --create-only

# Reset database and apply all migrations
prisma migrate reset

Migrations (Production)
# Apply pending migrations (CI/CD)
prisma migrate deploy

# Check migration status
prisma migrate status

# Compare schemas and generate diff
prisma migrate diff --from-config-datasource --to-schema schema.prisma --script

Utility Commands
# Open Prisma Studio (database GUI)
prisma studio

# Start Prisma's MCP server for AI tools
prisma mcp

# Show version info
prisma version
prisma -v

# Debug information
prisma debug

# Validate schema
prisma validate

# Format schema
prisma format

Current Prisma CLI Setup
New Configuration File

Use prisma.config.ts for CLI configuration:

import 'dotenv/config'
import { defineConfig, env } from 'prisma/config'

export default defineConfig({
  schema: 'prisma/schema.prisma',
  migrations: {
    path: 'prisma/migrations',
    seed: 'tsx prisma/seed.ts',
  },
  datasource: {
    url: env('DATABASE_URL'),
  },
})

Current Command Behavior
Run prisma generate explicitly after migrate dev, db push, or other schema syncs when you need fresh client output
Run prisma db seed explicitly after migrate dev or migrate reset when you need seed data
Use prisma db execute --file ... for raw SQL scripts
Environment Variables

Load environment variables explicitly in prisma.config.ts, commonly with dotenv:

// prisma.config.ts
import 'dotenv/config'

Rule Files

See individual rule files for detailed command documentation:

references/init.md           - Project initialization
references/generate.md       - Client generation
references/dev.md            - Local development database
references/db-pull.md        - Database introspection
references/db-push.md        - Schema push
references/db-seed.md        - Database seeding
references/db-execute.md     - Raw SQL execution
references/migrate-dev.md    - Development migrations
references/migrate-deploy.md - Production migrations
references/migrate-reset.md  - Database reset
references/migrate-status.md - Migration status
references/migrate-resolve.md - Migration resolution
references/migrate-diff.md   - Schema diffing
references/studio.md         - Database GUI
references/mcp.md            - Prisma MCP server
references/validate.md       - Schema validation
references/format.md         - Schema formatting
references/debug.md          - Debug info

How to Use

Use the command categories above for navigation, then open the specific command reference file you need.

Weekly Installs
6.2K
Repository
prisma/skills
GitHub Stars
34
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass