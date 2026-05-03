---
title: database-sharding
url: https://skills.sh/aj-geddes/useful-ai-prompts/database-sharding
---

# database-sharding

skills/aj-geddes/useful-ai-prompts/database-sharding
database-sharding
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill database-sharding
SKILL.md
Database Sharding
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement horizontal data partitioning across multiple database servers. Covers sharding strategies, consistent hashing, shard key selection, and cross-shard querying patterns.

When to Use
Database size exceeds single server capacity
Read/write throughput needs horizontal scaling
Geographic data distribution requirements
Multi-tenant data isolation
Cost optimization through distributed architecture
Load balancing across database instances
Quick Start

Minimal working example:

-- Define shard ranges
-- Shard 0: user_id 0-999999
-- Shard 1: user_id 1000000-1999999
-- Shard 2: user_id 2000000-2999999

CREATE TABLE users_shard_0 (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id BIGINT NOT NULL,
  email VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  CONSTRAINT shard_0_range CHECK (user_id BETWEEN 0 AND 999999)
);

CREATE TABLE users_shard_1 (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id BIGINT NOT NULL,
  email VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  CONSTRAINT shard_1_range CHECK (user_id BETWEEN 1000000 AND 1999999)
);

-- Function to determine shard
CREATE OR REPLACE FUNCTION get_shard_id(p_user_id BIGINT)
RETURNS INT AS $$
BEGIN
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Range-Based Sharding	Range-Based Sharding
Hash-Based Sharding	Hash-Based Sharding
Directory-Based Sharding	Directory-Based Sharding
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
270
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