---
title: database-monitoring
url: https://skills.sh/aj-geddes/useful-ai-prompts/database-monitoring
---

# database-monitoring

skills/aj-geddes/useful-ai-prompts/database-monitoring
database-monitoring
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill database-monitoring
SKILL.md
Database Monitoring
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive database monitoring for performance analysis, health checks, and proactive alerting. Covers metrics collection, analysis, and troubleshooting strategies.

When to Use
Performance baseline establishment
Real-time health monitoring
Capacity planning
Query performance analysis
Resource utilization tracking
Alerting rule configuration
Incident response and troubleshooting
Quick Start

Minimal working example:

-- View current connections
SELECT
  pid,
  usename,
  application_name,
  client_addr,
  state,
  query_start,
  state_change
FROM pg_stat_activity
WHERE state != 'idle'
ORDER BY query_start DESC;

-- Count connections per database
SELECT
  datname,
  COUNT(*) as connection_count,
  MAX(EXTRACT(EPOCH FROM (NOW() - query_start))) as max_query_duration_sec
FROM pg_stat_activity
GROUP BY datname;

-- Find idle transactions
SELECT
  pid,
  usename,
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Connection Monitoring	Connection Monitoring
Query Performance Monitoring	Query Performance Monitoring
Table & Index Monitoring	Table & Index Monitoring
Performance Schema	Performance Schema
InnoDB Monitoring	InnoDB Monitoring
PostgreSQL Monitoring Setup	PostgreSQL Monitoring Setup
Automated Monitoring Dashboard	Automated Monitoring Dashboard
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
294
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn