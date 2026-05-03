---
title: database-migration
url: https://skills.sh/dauquangthanh/hanoi-rainbow/database-migration
---

# database-migration

skills/dauquangthanh/hanoi-rainbow/database-migration
database-migration
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill database-migration
SKILL.md
Database Migration

Provides comprehensive guidance for migrating databases between engines, versions, platforms, and architectures. Covers both schema and data migration with strategies for minimizing downtime and ensuring data integrity.

Migration Decision Tree

1. Identify Migration Type:

Same engine (PostgreSQL → PostgreSQL)? → Homogeneous migration
Different engine (Oracle → PostgreSQL)? → Heterogeneous migration
Version upgrade only? → In-place or dump/restore
Cloud migration? → Consider cloud-native tools

2. Assess Downtime Requirements:

Can tolerate hours of downtime? → Dump and restore
Need minimal downtime (minutes)? → Replication with cutover
Require zero downtime? → See zero-downtime-migration-strategies.md

3. Choose Migration Path:

Load migration-types.md for detailed migration approaches
For cloud migrations, load cloud-specific-migrations.md
Core Migration Workflow
Step 1: Assessment and Planning

Analyze Source Database:

Document current database version, size, and complexity
Identify dependencies (applications, services, integrations)
Review schema: tables, indexes, constraints, triggers, procedures
Assess data volume and growth rate
Document current performance baselines

Define Requirements:

Migration type (homogeneous vs heterogeneous)
Acceptable downtime window
Data integrity requirements
Compliance and security requirements
Rollback criteria

Output: Migration plan with approach, timeline, and resources

Step 2: Environment Setup

Prepare Target Environment:

Provision target database with appropriate sizing
Configure network connectivity and security
Set up monitoring and logging
Create test and staging environments matching production

Prepare Migration Tools:

Native tools (pg_dump, mysqldump, SQL Server bcp)
Cloud provider tools (AWS DMS, GCP Database Migration Service)
Third-party tools (see tools-reference.md)
Step 3: Schema Migration

For Homogeneous Migration:

Export schema using native tools
Review and optimize schema for target version
Apply schema to target database
Verify all objects created successfully

For Heterogeneous Migration:

Analyze schema compatibility issues
Convert data types, stored procedures, triggers
Adapt SQL dialects and syntax
Test converted schema thoroughly

Load migration-types.md for engine-specific schema conversion guidance.

Step 4: Data Migration

Choose Data Migration Strategy:

Option A: Dump and Restore (Full Downtime)

1. Stop application writes
2. Create full backup of source database
3. Transfer backup to target environment
4. Restore to target database
5. Verify data integrity (row counts, checksums)
6. Update application connection strings
7. Resume operations


Best for: Smaller databases, acceptable downtime windows

Option B: Replication (Minimal Downtime)

1. Set up replication from source to target
2. Monitor replication lag until synchronized
3. Schedule cutover window
4. Stop writes briefly (minutes)
5. Verify replication is caught up
6. Promote target to primary
7. Update application connections
8. Resume operations


Best for: Large databases, minimal downtime requirements

Load zero-downtime-migration-strategies.md for advanced zero-downtime patterns.

Step 5: Validation and Testing

Validate Data Migration:

Compare row counts between source and target
Verify data integrity (checksums, sample queries)
Test application functionality against target database
Validate performance meets requirements
Check all constraints, indexes, and relationships

Testing Checklist:

 All tables migrated with correct row counts
 Schema objects (indexes, constraints, triggers) present
 Data types converted correctly
 Application queries execute successfully
 Performance meets or exceeds baseline
 Backup and restore procedures work

Load common-issues-and-solutions.md if encountering problems.

Step 6: Cutover Planning
Create detailed cutover runbook with specific timings
Define rollback criteria and procedures (load rollback-procedures.md)
Coordinate with stakeholders (apps, operations, business)
Schedule maintenance window
Prepare communication plan

Load migration-phases.md for detailed phase-by-phase execution guidance.

Step 7: Post-Migration

Immediate (Day 1):

Monitor performance metrics and error rates
Validate application functionality
Keep source database available (read-only) as safety net
Document any issues and resolutions

Short-term (Week 1-2):

Continue monitoring for issues
Optimize indexes and queries if needed
Tune database configuration for workload
Conduct parallel run if applicable

Long-term:

Validate backup and restore procedures
Update disaster recovery plans
Document final configuration and lessons learned
Decommission source database after retention period
Key Considerations

Planning Guidelines:

Allow 2-3x estimated time for heterogeneous migrations
Plan for extended parallel run period (1-4 weeks minimum)
Database migration often triggers application code changes
Coordinate with application migration when possible
Consider phased approach: read replica → read/write split → full cutover

Critical Success Factors:

✅ Multiple backups before migration
✅ Test migration in staging environment first
✅ Monitor metrics during migration (lag, throughput, errors)
✅ Always have rollback plan ready
✅ Document all steps, issues, and decisions
✅ Encrypt data in transit and at rest
✅ Rotate credentials after migration

Load best-practices.md for comprehensive best practices.

Reference Files

Load these references based on specific needs:

migration-types.md - Detailed guidance on homogeneous vs heterogeneous migrations, engine-specific conversion patterns
migration-phases.md - Phase-by-phase execution details with timelines and dependencies
zero-downtime-migration-strategies.md - Advanced patterns for zero-downtime migrations (dual writes, event streaming, phased cutover)
cloud-specific-migrations.md - AWS DMS, GCP Database Migration Service, Azure Database Migration Service
tools-reference.md - Native tools, cloud provider services, third-party migration tools
rollback-procedures.md - Step-by-step rollback procedures for different migration strategies
common-issues-and-solutions.md - Troubleshooting guide for common migration problems
best-practices.md - Comprehensive best practices checklist
Weekly Installs
15
Repository
dauquangthanh/h…-rainbow
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass