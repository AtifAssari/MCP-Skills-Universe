---
rating: ⭐⭐
title: data-migration-scripts
url: https://skills.sh/aj-geddes/useful-ai-prompts/data-migration-scripts
---

# data-migration-scripts

skills/aj-geddes/useful-ai-prompts/data-migration-scripts
data-migration-scripts
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill data-migration-scripts
SKILL.md
Data Migration Scripts
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create robust, safe, and reversible data migration scripts for database schema changes and data transformations with minimal downtime.

When to Use
Database schema changes
Adding/removing/modifying columns
Migrating between database systems
Data transformations and cleanup
Splitting or merging tables
Changing data types
Adding indexes and constraints
Backfilling data
Multi-tenant data migrations
Quick Start

Minimal working example:

import { Knex } from "knex";

// migrations/20240101000000_add_user_preferences.ts
export async function up(knex: Knex): Promise<void> {
  // Create new table
  await knex.schema.createTable("user_preferences", (table) => {
    table.uuid("id").primary().defaultTo(knex.raw("gen_random_uuid()"));
    table
      .uuid("user_id")
      .notNullable()
      .references("id")
      .inTable("users")
      .onDelete("CASCADE");
    table.jsonb("preferences").defaultTo("{}");
    table.timestamp("created_at").defaultTo(knex.fn.now());
    table.timestamp("updated_at").defaultTo(knex.fn.now());

    table.index("user_id");
  });

  // Migrate existing data
  await knex.raw(`
    INSERT INTO user_preferences (user_id, preferences)
    SELECT id, jsonb_build_object(
      'theme', COALESCE(theme, 'light'),
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Knex.js Migrations (Node.js)	Knex.js Migrations (Node.js)
Alembic Migrations (Python/SQLAlchemy)	Alembic Migrations (Python/SQLAlchemy)
Large Data Migration with Batching	Large Data Migration with Batching
Zero-Downtime Migration Pattern	Zero-Downtime Migration Pattern
Migration Validation	Migration Validation
Cross-Database Migration	Cross-Database Migration
Best Practices
✅ DO
Always write both up and down migrations
Test migrations on production-like data
Use transactions for atomic operations
Process large datasets in batches
Add indexes after data insertion
Validate data after migration
Log progress and errors
Use feature flags for application code changes
Back up database before running migrations
Test rollback procedures
Document migration side effects
Version control all migrations
Use idempotent operations
❌ DON'T
Run untested migrations on production
Make breaking changes without backwards compatibility
Process millions of rows in single transaction
Skip rollback implementation
Ignore migration failures
Modify old migrations
Delete data without backups
Run migrations manually in production
Weekly Installs
264
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass