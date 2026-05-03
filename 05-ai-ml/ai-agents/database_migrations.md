---
title: database-migrations
url: https://skills.sh/langchain-ai/skills-benchmarks/database-migrations
---

# database-migrations

skills/langchain-ai/skills-benchmarks/database-migrations
database-migrations
Installation
$ npx skills add https://github.com/langchain-ai/skills-benchmarks --skill database-migrations
SKILL.md
Database Migration Patterns

Manage database schema changes safely and reliably.

Migration File Structure
migrations/
  001_create_users.sql
  002_add_email_index.sql
  003_create_orders.sql

Writing Safe Migrations
Adding Columns
-- migrations/004_add_user_status.sql
-- Up
ALTER TABLE users ADD COLUMN status VARCHAR(20) DEFAULT 'active';
CREATE INDEX idx_users_status ON users(status);

-- Down
DROP INDEX idx_users_status;
ALTER TABLE users DROP COLUMN status;

Creating Tables
-- migrations/005_create_audit_log.sql
-- Up
CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY,
    table_name VARCHAR(100) NOT NULL,
    record_id INTEGER NOT NULL,
    action VARCHAR(20) NOT NULL,
    changed_by INTEGER REFERENCES users(id),
    changed_at TIMESTAMP DEFAULT NOW(),
    old_values JSONB,
    new_values JSONB
);

CREATE INDEX idx_audit_log_table ON audit_log(table_name, record_id);
CREATE INDEX idx_audit_log_time ON audit_log(changed_at);

-- Down
DROP TABLE audit_log;

Best Practices
Always include rollback (down) migrations
Never modify existing migrations - create new ones
Test migrations on a copy of production data
Use transactions for atomic changes
Add indexes concurrently in production: CREATE INDEX CONCURRENTLY
Weekly Installs
19
Repository
langchain-ai/sk…nchmarks
GitHub Stars
95
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass