---
rating: ⭐⭐⭐
title: grepai-storage-postgres
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-storage-postgres
---

# grepai-storage-postgres

skills/yoanbernabeu/grepai-skills/grepai-storage-postgres
grepai-storage-postgres
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-storage-postgres
SKILL.md
GrepAI Storage with PostgreSQL

This skill covers using PostgreSQL with the pgvector extension as the storage backend for GrepAI.

When to Use This Skill
Team environments with shared index
Large codebases (10K+ files)
Need concurrent access
Integration with existing PostgreSQL infrastructure
Prerequisites
PostgreSQL 14+ with pgvector extension
Database user with create table permissions
Network access to PostgreSQL server
Advantages
Benefit	Description
👥 Team sharing	Multiple users can access same index
📏 Scalable	Handles large codebases
🔄 Concurrent	Multiple simultaneous searches
💾 Persistent	Data survives machine restarts
🔧 Familiar	Standard database tooling
Setting Up PostgreSQL with pgvector
Option 1: Docker (Recommended for Development)
# Run PostgreSQL with pgvector
docker run -d \
  --name grepai-postgres \
  -e POSTGRES_USER=grepai \
  -e POSTGRES_PASSWORD=grepai \
  -e POSTGRES_DB=grepai \
  -p 5432:5432 \
  pgvector/pgvector:pg16

Option 2: Install on Existing PostgreSQL
# Install pgvector extension (Ubuntu/Debian)
sudo apt install postgresql-16-pgvector

# Or compile from source
git clone https://github.com/pgvector/pgvector.git
cd pgvector
make
sudo make install


Then enable the extension:

-- Connect to your database
CREATE EXTENSION IF NOT EXISTS vector;

Option 3: Managed Services
Supabase: pgvector included by default
Neon: pgvector available
AWS RDS: Install pgvector extension
Azure Database: pgvector available
Configuration
Basic Configuration
# .grepai/config.yaml
store:
  backend: postgres
  postgres:
    dsn: postgres://user:password@localhost:5432/grepai

With Environment Variable
store:
  backend: postgres
  postgres:
    dsn: ${DATABASE_URL}


Set the environment variable:

export DATABASE_URL="postgres://user:password@localhost:5432/grepai"

Full DSN Options
store:
  backend: postgres
  postgres:
    dsn: postgres://user:password@host:5432/database?sslmode=require


DSN components:

user: Database username
password: Database password
host: Server hostname or IP
5432: Port (default: 5432)
database: Database name
sslmode: SSL mode (disable, require, verify-full)
SSL Modes
Mode	Description	Use Case
disable	No SSL	Local development
require	SSL required	Production
verify-full	SSL + verify certificate	High security
# Production with SSL
store:
  backend: postgres
  postgres:
    dsn: postgres://user:pass@prod.db.com:5432/grepai?sslmode=require

Database Schema

GrepAI automatically creates these tables:

-- Vector embeddings table
CREATE TABLE IF NOT EXISTS embeddings (
    id SERIAL PRIMARY KEY,
    file_path TEXT NOT NULL,
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    start_line INTEGER,
    end_line INTEGER,
    embedding vector(768),  -- Dimension matches your model
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(file_path, chunk_index)
);

-- Index for vector similarity search
CREATE INDEX ON embeddings USING ivfflat (embedding vector_cosine_ops);

Verifying Setup
Check pgvector Extension
-- Connect to database
psql -U grepai -d grepai

-- Check extension is installed
SELECT * FROM pg_extension WHERE extname = 'vector';

-- Check GrepAI tables exist (after first grepai watch)
\dt

Test Connection from GrepAI
# Check status
grepai status

# Should show PostgreSQL backend info

Performance Tuning
PostgreSQL Configuration

For better vector search performance:

-- Increase work memory for vector operations
SET work_mem = '256MB';

-- Adjust for your hardware
SET effective_cache_size = '4GB';
SET shared_buffers = '1GB';

Index Tuning

For large indices, tune the IVFFlat index:

-- More lists = faster search, more memory
CREATE INDEX ON embeddings
USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);  -- Adjust based on row count


Rule of thumb: lists = sqrt(rows)

Concurrent Access

PostgreSQL handles concurrent access automatically:

Multiple grepai search commands work simultaneously
One grepai watch daemon per codebase
Many users can share the same index
Team Setup
Shared Database

All team members point to the same database:

# Each developer's .grepai/config.yaml
store:
  backend: postgres
  postgres:
    dsn: postgres://team:secret@shared-db.company.com:5432/grepai

Per-Project Databases

For isolated projects, use separate databases:

# Create databases
createdb -U postgres grepai_projecta
createdb -U postgres grepai_projectb

# Project A config
store:
  backend: postgres
  postgres:
    dsn: postgres://user:pass@localhost:5432/grepai_projecta

Backup and Restore
Backup
pg_dump -U grepai -d grepai > grepai_backup.sql

Restore
psql -U grepai -d grepai < grepai_backup.sql

Migrating from GOB
Set up PostgreSQL with pgvector
Update configuration:
store:
  backend: postgres
  postgres:
    dsn: postgres://user:pass@localhost:5432/grepai

Delete old index:
rm .grepai/index.gob

Re-index:
grepai watch

Common Issues

❌ Problem: FATAL: password authentication failed ✅ Solution: Check DSN credentials and pg_hba.conf

❌ Problem: ERROR: extension "vector" is not available ✅ Solution: Install pgvector:

sudo apt install postgresql-16-pgvector
# Then: CREATE EXTENSION vector;


❌ Problem: ERROR: type "vector" does not exist ✅ Solution: Enable extension in the database:

CREATE EXTENSION IF NOT EXISTS vector;


❌ Problem: Connection refused ✅ Solution:

Check PostgreSQL is running
Verify host and port
Check firewall rules

❌ Problem: Slow searches ✅ Solution:

Add IVFFlat index
Increase work_mem
Vacuum and analyze tables
Best Practices
Use environment variables: Don't commit credentials
Enable SSL: For remote databases
Regular backups: pg_dump before major changes
Monitor performance: Check query times
Index maintenance: Regular VACUUM ANALYZE
Output Format

PostgreSQL storage status:

✅ PostgreSQL Storage Configured

   Backend: PostgreSQL + pgvector
   Host: localhost:5432
   Database: grepai
   SSL: disabled

   Contents:
   - Files: 2,450
   - Chunks: 12,340
   - Vector dimension: 768

   Performance:
   - Connection: OK
   - IVFFlat index: Yes
   - Search latency: ~50ms

Weekly Installs
347
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail