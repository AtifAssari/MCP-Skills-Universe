---
rating: ⭐⭐
title: data-replication-setup
url: https://skills.sh/aj-geddes/useful-ai-prompts/data-replication-setup
---

# data-replication-setup

skills/aj-geddes/useful-ai-prompts/data-replication-setup
data-replication-setup
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill data-replication-setup
SKILL.md
Data Replication Setup
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Configure database replication for disaster recovery, load distribution, and high availability. Covers master-slave, multi-master replication, and monitoring strategies.

When to Use
High availability setup
Disaster recovery planning
Read replica configuration
Multi-region replication
Replication monitoring and maintenance
Failover automation
Cross-region backup strategies
Quick Start

PostgreSQL - Configure Primary Server:

-- On primary server: postgresql.conf
-- wal_level = replica
-- max_wal_senders = 10
-- wal_keep_size = 1GB

-- Create replication user
CREATE ROLE replication_user WITH REPLICATION ENCRYPTED PASSWORD 'secure_password';

-- Allow replication connections: pg_hba.conf
-- host    replication     replication_user   standby_ip/32    md5

-- Enable WAL archiving for continuous backup
-- archive_mode = on
-- archive_command = 'test ! -f /archive/%f && cp %p /archive/%f'

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Master-Slave (Primary-Standby) Setup	Master-Slave (Primary-Standby) Setup
Logical Replication	Logical Replication
Master-Slave Setup	Master-Slave Setup
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
262
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail