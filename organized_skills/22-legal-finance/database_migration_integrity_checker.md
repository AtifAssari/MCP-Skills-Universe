---
rating: ⭐⭐
title: database-migration-integrity-checker
url: https://skills.sh/jorgealves/agent_skills/database-migration-integrity-checker
---

# database-migration-integrity-checker

skills/jorgealves/agent_skills/database-migration-integrity-checker
database-migration-integrity-checker
Installation
$ npx skills add https://github.com/jorgealves/agent_skills --skill database-migration-integrity-checker
SKILL.md
Database Migration Integrity Checker
Purpose and Intent

The database-migration-integrity-checker is a safety net for your most critical asset: your data. It catches dangerous SQL operations that might pass a standard code review but could cause production outages or data loss.

When to Use
CI/CD Pipelines: Block deployments if a migration contains a high-risk operation without manual override.
Local Development: Run before committing a new migration to ensure it follows safe DDL practices.
When NOT to Use
Data Querying: This is for schema changes, not for auditing standard SELECT/INSERT queries.
Security and Data-Handling Considerations
Reads SQL files only; no database access required.
Safe for local use.
Weekly Installs
82
Repository
jorgealves/agent_skills
GitHub Stars
1
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass