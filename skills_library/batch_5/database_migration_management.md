---
title: database-migration-management
url: https://skills.sh/aj-geddes/useful-ai-prompts/database-migration-management
---

# database-migration-management

skills/aj-geddes/useful-ai-prompts/database-migration-management
database-migration-management
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill database-migration-management
SKILL.md
Database Migration Management
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement robust database migration systems with version control, rollback capabilities, and data transformation strategies. Includes migration frameworks and production deployment patterns.

When to Use
Schema versioning and evolution
Data transformations and cleanup
Adding/removing tables and columns
Index creation and optimization
Migration testing and validation
Rollback planning and execution
Multi-environment deployments
Quick Start

Minimal working example:

-- Create migrations tracking table
CREATE TABLE schema_migrations (
  version BIGINT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  duration_ms INTEGER,
  checksum VARCHAR(64)
);

-- Create migration log table
CREATE TABLE migration_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  version BIGINT NOT NULL,
  status VARCHAR(20) NOT NULL,
  error_message TEXT,
  rolled_back_at TIMESTAMP,
  executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Function to record migration
CREATE OR REPLACE FUNCTION record_migration(
  p_version BIGINT,
  p_name VARCHAR,
  p_duration_ms INTEGER
) RETURNS void AS $$
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Adding Columns	Adding Columns
Renaming Columns	Renaming Columns
Creating Indexes Non-blocking	Creating Indexes Non-blocking
Data Transformations	Data Transformations
Table Structure Changes	Table Structure Changes
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
325
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass