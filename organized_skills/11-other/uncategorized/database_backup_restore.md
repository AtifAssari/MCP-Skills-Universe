---
rating: ⭐⭐⭐
title: database-backup-restore
url: https://skills.sh/aj-geddes/useful-ai-prompts/database-backup-restore
---

# database-backup-restore

skills/aj-geddes/useful-ai-prompts/database-backup-restore
database-backup-restore
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill database-backup-restore
SKILL.md
Database Backup & Restore
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive backup and disaster recovery strategies. Covers backup types, retention policies, restore testing, and recovery time objectives (RTO/RPO).

When to Use
Backup automation setup
Disaster recovery planning
Recovery testing procedures
Backup retention policies
Point-in-time recovery (PITR)
Cross-region backup replication
Compliance and audit requirements
Quick Start

pg_dump - Text Format:

# Simple full backup
pg_dump -h localhost -U postgres -F p database_name > backup.sql

# With compression
pg_dump -h localhost -U postgres -F p database_name | gzip > backup.sql.gz

# Backup with verbose output
pg_dump -h localhost -U postgres -F p -v database_name > backup.sql 2>&1

# Exclude specific tables
pg_dump -h localhost -U postgres database_name \
  --exclude-table=temp_* --exclude-table=logs > backup.sql

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Full Database Backup	Full Database Backup
Incremental & Differential Backups	Incremental & Differential Backups
Full Database Backup	Full Database Backup
Binary Log Backups	Binary Log Backups
PostgreSQL Restore	PostgreSQL Restore
MySQL Restore	MySQL Restore
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
330
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