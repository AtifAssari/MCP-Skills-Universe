---
rating: ⭐⭐⭐
title: backup-disaster-recovery
url: https://skills.sh/aj-geddes/useful-ai-prompts/backup-disaster-recovery
---

# backup-disaster-recovery

skills/aj-geddes/useful-ai-prompts/backup-disaster-recovery
backup-disaster-recovery
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill backup-disaster-recovery
SKILL.md
Backup and Disaster Recovery
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Design and implement comprehensive backup and disaster recovery strategies to ensure data protection, business continuity, and rapid recovery from infrastructure failures.

When to Use
Data protection and compliance
Business continuity planning
Disaster recovery planning
Point-in-time recovery
Cross-region failover
Data migration
Compliance and audit requirements
Recovery time objective (RTO) optimization
Quick Start

Minimal working example:

# postgres-backup-cronjob.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: backup-script
  namespace: databases
data:
  backup.sh: |
    #!/bin/bash
    set -euo pipefail

    BACKUP_DIR="/backups/postgresql"
    RETENTION_DAYS=30
    DB_HOST="${POSTGRES_HOST}"
    DB_PORT="${POSTGRES_PORT:-5432}"
    DB_USER="${POSTGRES_USER}"
    DB_PASSWORD="${POSTGRES_PASSWORD}"

    export PGPASSWORD="$DB_PASSWORD"

    # Create backup directory
    mkdir -p "$BACKUP_DIR"

    # Full backup
    BACKUP_FILE="$BACKUP_DIR/full-$(date +%Y%m%d-%H%M%S).sql"
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Database Backup Configuration	Database Backup Configuration
Disaster Recovery Plan Template	Disaster Recovery Plan Template
Backup and Restore Script	Backup and Restore Script
Cross-Region Failover	Cross-Region Failover
Best Practices
✅ DO
Perform regular backup testing
Use multiple backup locations
Implement automated backups
Document recovery procedures
Test failover procedures regularly
Monitor backup completion
Use immutable backups
Encrypt backups at rest and in transit
❌ DON'T
Rely on a single backup location
Ignore backup failures
Store backups with production data
Skip testing recovery procedures
Over-compress backups beyond recovery speed needs
Forget to verify backup integrity
Store encryption keys with backups
Assume backups are automatically working
Weekly Installs
367
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykPass