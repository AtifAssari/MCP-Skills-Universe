---
rating: ⭐⭐
title: postgresql-optimization
url: https://skills.sh/sickn33/antigravity-awesome-skills/postgresql-optimization
---

# postgresql-optimization

skills/sickn33/antigravity-awesome-skills/postgresql-optimization
postgresql-optimization
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill postgresql-optimization
SKILL.md
PostgreSQL Optimization Workflow
Overview

Specialized workflow for PostgreSQL database optimization including query tuning, indexing strategies, performance analysis, vacuum management, and production database administration.

When to Use This Workflow

Use this workflow when:

Optimizing slow PostgreSQL queries
Designing indexing strategies
Analyzing database performance
Tuning PostgreSQL configuration
Managing production databases
Workflow Phases
Phase 1: Performance Assessment
Skills to Invoke
database-optimizer - Database optimization
postgres-best-practices - PostgreSQL best practices
Actions
Check database version
Review configuration
Analyze slow queries
Check resource usage
Identify bottlenecks
Copy-Paste Prompts
Use @database-optimizer to assess PostgreSQL performance

Phase 2: Query Analysis
Skills to Invoke
sql-optimization-patterns - SQL optimization
postgres-best-practices - PostgreSQL patterns
Actions
Run EXPLAIN ANALYZE
Identify scan types
Check join strategies
Analyze execution time
Find optimization opportunities
Copy-Paste Prompts
Use @sql-optimization-patterns to analyze and optimize queries

Phase 3: Indexing Strategy
Skills to Invoke
database-design - Index design
postgresql - PostgreSQL indexing
Actions
Identify missing indexes
Create B-tree indexes
Add composite indexes
Consider partial indexes
Review index usage
Copy-Paste Prompts
Use @database-design to design PostgreSQL indexing strategy

Phase 4: Query Optimization
Skills to Invoke
sql-optimization-patterns - Query tuning
sql-pro - SQL expertise
Actions
Rewrite inefficient queries
Optimize joins
Add CTEs where helpful
Implement pagination
Test improvements
Copy-Paste Prompts
Use @sql-optimization-patterns to optimize SQL queries

Phase 5: Configuration Tuning
Skills to Invoke
postgres-best-practices - Configuration
database-admin - Database administration
Actions
Tune shared_buffers
Configure work_mem
Set effective_cache_size
Adjust checkpoint settings
Configure autovacuum
Copy-Paste Prompts
Use @postgres-best-practices to tune PostgreSQL configuration

Phase 6: Maintenance
Skills to Invoke
database-admin - Database maintenance
postgresql - PostgreSQL maintenance
Actions
Schedule VACUUM
Run ANALYZE
Check table bloat
Monitor autovacuum
Review statistics
Copy-Paste Prompts
Use @database-admin to schedule PostgreSQL maintenance

Phase 7: Monitoring
Skills to Invoke
grafana-dashboards - Monitoring dashboards
prometheus-configuration - Metrics collection
Actions
Set up monitoring
Create dashboards
Configure alerts
Track key metrics
Review trends
Copy-Paste Prompts
Use @grafana-dashboards to create PostgreSQL monitoring

Optimization Checklist
 Slow queries identified
 Indexes optimized
 Configuration tuned
 Maintenance scheduled
 Monitoring active
 Performance improved
Quality Gates
 Query performance improved
 Indexes effective
 Configuration optimized
 Maintenance automated
 Monitoring in place
Related Workflow Bundles
database - Database operations
cloud-devops - Infrastructure
performance-optimization - Performance
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
110
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass