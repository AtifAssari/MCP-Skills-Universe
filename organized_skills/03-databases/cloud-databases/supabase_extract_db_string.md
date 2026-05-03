---
rating: ⭐⭐⭐
title: supabase-extract-db-string
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-extract-db-string
---

# supabase-extract-db-string

skills/yoanbernabeu/supabase-pentest-skills/supabase-extract-db-string
supabase-extract-db-string
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-extract-db-string
SKILL.md
Database Connection String Detection

🔴 CRITICAL: PROGRESSIVE FILE UPDATES REQUIRED

You MUST write to context files AS YOU GO, not just at the end.

Write to .sb-pentest-context.json IMMEDIATELY after each discovery
Log to .sb-pentest-audit.log BEFORE and AFTER each action
DO NOT wait until the skill completes to update files
If the skill crashes or is interrupted, all prior findings must already be saved

This is not optional. Failure to write progressively is a critical error.

This skill detects if PostgreSQL database connection strings are accidentally exposed in client-side code.

When to Use This Skill
As part of every security audit
When reviewing code before production
When Supabase database access is suspected
Prerequisites
Target application accessible
Supabase detection completed (auto-invokes if needed)
Why This Is Critical

Exposed database connection strings allow:

Impact	Description
🔴 Direct DB Access	Bypass API, connect directly to PostgreSQL
🔴 Full Data Access	Read/write all data without RLS
🔴 Schema Access	View and modify database structure
🔴 User Enumeration	Access auth.users table directly

This is a P0 (Critical) finding requiring immediate action.

Connection String Patterns
Supabase Database URL
postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres

Connection String Components
Component	Example	Sensitivity
Host	db.abc123.supabase.co	Medium
Port	5432	Low
Database	postgres	Low
Username	postgres	Medium
Password	[your-password]	🔴 Critical
Pooler Connection (Supavisor)
postgresql://postgres.[project-ref]:[password]@aws-0-us-east-1.pooler.supabase.com:6543/postgres

Detection Patterns
1. Full Connection Strings
// ❌ CRITICAL - Full connection string
const dbUrl = 'postgresql://postgres:MySecretPass123@db.abc123.supabase.co:5432/postgres'

2. Environment Variable Leaks
// ❌ Exposed in client bundle
process.env.DATABASE_URL
process.env.POSTGRES_URL
process.env.SUPABASE_DB_URL

3. Partial Exposure
// ⚠️ Password exposed separately
const DB_PASSWORD = 'MySecretPass123'
const DB_HOST = 'db.abc123.supabase.co'

4. ORM Configuration
// ❌ Database config in client code
const prisma = new PrismaClient({
  datasources: {
    db: {
      url: 'postgresql://postgres:pass@db.abc123.supabase.co:5432/postgres'
    }
  }
})

Usage
Basic Check
Check for database connection strings on https://myapp.example.com

Deep Scan
Deep scan for DB credentials on https://myapp.example.com

Output Format
No Connection String Found (Good)
═══════════════════════════════════════════════════════════
 DATABASE CONNECTION STRING CHECK
═══════════════════════════════════════════════════════════

 Status: ✅ No database connection strings detected

 Scanned:
 ├── JavaScript bundles: 5 files analyzed
 ├── PostgreSQL patterns: None found
 ├── Connection strings: None found
 └── Password patterns: None found

 Result: PASS - No direct database credentials exposed
═══════════════════════════════════════════════════════════

Connection String FOUND (Critical)
═══════════════════════════════════════════════════════════
 🔴 CRITICAL: DATABASE CONNECTION STRING EXPOSED
═══════════════════════════════════════════════════════════

 Severity: P0 - CRITICAL
 Status: ❌ PostgreSQL connection string found in client code!

 ⚠️  IMMEDIATE ACTION REQUIRED ⚠️

 Connection String:
 postgresql://postgres:MySecr***@db.abc123def.supabase.co:5432/postgres
 (Password partially redacted in display, full value in context file)

 Parsed Components:
 ├── Host: db.abc123def.supabase.co
 ├── Port: 5432
 ├── Database: postgres
 ├── Username: postgres
 └── Password: [EXPOSED] ← CRITICAL

 Location:
 └── /static/js/api.chunk.js (line 234)
     const DATABASE_URL = 'postgresql://postgres:...'

 Impact Assessment:
 ├── 🔴 Direct PostgreSQL access possible
 ├── 🔴 All RLS policies bypassed
 ├── 🔴 Can access auth.users table
 ├── 🔴 Can modify database schema
 └── 🔴 Full data exfiltration possible

 ═══════════════════════════════════════════════════════════
 IMMEDIATE REMEDIATION STEPS
 ═══════════════════════════════════════════════════════════

 1. CHANGE DATABASE PASSWORD NOW
    → Supabase Dashboard > Settings > Database > Reset database password

 2. REMOVE FROM CLIENT CODE
    → Delete connection string from source code
    → Ensure DATABASE_URL is not in NEXT_PUBLIC_* or VITE_* env vars
    → Redeploy application

 3. AUDIT FOR ABUSE
    → Check Supabase logs for direct PostgreSQL connections
    → Review for unauthorized data access or modifications

 4. USE PROPER ARCHITECTURE
    → Client should ONLY use Supabase client library (REST API)
    → Direct DB access should ONLY be from:
      - Edge Functions
      - Server-side code
      - Migration tools

 Documentation:
 → https://supabase.com/docs/guides/database/connecting-to-postgres
 → https://supabase.com/docs/guides/functions

═══════════════════════════════════════════════════════════

Context Output
{
  "findings": [
    {
      "id": "DB_CONNECTION_STRING_EXPOSED",
      "severity": "P0",
      "title": "PostgreSQL Connection String Exposed",
      "description": "Database connection string with password found in client-side code",
      "location": {
        "file": "/static/js/api.chunk.js",
        "line": 234
      },
      "evidence": {
        "host": "db.abc123def.supabase.co",
        "port": 5432,
        "database": "postgres",
        "username": "postgres",
        "password_exposed": true
      },
      "remediation": {
        "immediate": "Reset database password in Supabase Dashboard",
        "long_term": "Move DB operations to Edge Functions",
        "docs": "https://supabase.com/docs/guides/database/connecting-to-postgres"
      }
    }
  ],
  "supabase": {
    "db_string_exposed": true,
    "db_host": "db.abc123def.supabase.co"
  }
}

Partial Exposure

Even partial exposure is concerning:

═══════════════════════════════════════════════════════════
 ⚠️ PARTIAL DATABASE CREDENTIALS FOUND
═══════════════════════════════════════════════════════════

 Severity: P1 - High

 Found:
 ├── Database host: db.abc123def.supabase.co (line 45)
 ├── Database password: [16 char string] (line 89)
 └── Could potentially be combined for access

 Recommendation:
 → Rotate database password as precaution
 → Remove all DB-related values from client code
═══════════════════════════════════════════════════════════

Common Causes
Cause	Solution
Wrong env prefix	Never use NEXT_PUBLIC_DATABASE_URL
SSR code in client	Ensure server-only code stays server-side
Bundler misconfiguration	Review webpack/vite config for env exposure
Copy-paste error	Double-check what you're committing
Architecture Guidance
Wrong (Direct DB in Client)
// ❌ NEVER in client code
import { Pool } from 'pg'
const pool = new Pool({
  connectionString: process.env.DATABASE_URL  // ❌
})

Correct (API or Edge Function)
// ✅ Client uses Supabase client
const { data } = await supabase
  .from('products')
  .select('*')

// OR call an Edge Function for complex queries
const { data } = await supabase.functions.invoke('complex-query')

Edge Function (Server-Side)
// supabase/functions/complex-query/index.ts
import { createClient } from '@supabase/supabase-js'

Deno.serve(async (req) => {
  // ✅ Direct DB access only on server
  const supabase = createClient(
    Deno.env.get('SUPABASE_URL'),
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
  )

  // Complex query that can't be done via REST
  const { data } = await supabase.rpc('complex_function')
  return new Response(JSON.stringify(data))
})

MANDATORY: Progressive Context File Updates

⚠️ This skill MUST update tracking files PROGRESSIVELY during execution, NOT just at the end.

Critical Rule: Write As You Go

DO NOT batch all writes at the end. Instead:

Before starting any action → Log the action to .sb-pentest-audit.log
After each discovery → Immediately update .sb-pentest-context.json
After each significant step → Log completion to .sb-pentest-audit.log

This ensures that if the skill is interrupted, crashes, or times out, all findings up to that point are preserved.

Required Actions (Progressive)

Update .sb-pentest-context.json with findings:

{
  "supabase": {
    "db_string_exposed": true/false,
    "db_host": "db.[ref].supabase.co"
  },
  "findings": [
    {
      "id": "DB_CONNECTION_STRING_EXPOSED",
      "severity": "P0",
      ...
    }
  ]
}


Log to .sb-pentest-audit.log:

[TIMESTAMP] [supabase-extract-db-string] [START] Checking for DB connection strings
[TIMESTAMP] [supabase-extract-db-string] [CRITICAL] Connection string EXPOSED
[TIMESTAMP] [supabase-extract-db-string] [CONTEXT_UPDATED] .sb-pentest-context.json updated


If files don't exist, create them before writing.

FAILURE TO UPDATE CONTEXT FILES IS NOT ACCEPTABLE.

MANDATORY: Evidence Collection

📁 Evidence Directory: .sb-pentest-evidence/02-extraction/db-string-exposure/

Evidence Files to Create (if DB string found)
File	Content
db-string-exposure/connection-details.json	Parsed connection string (password redacted)
db-string-exposure/location.txt	File path and line number
Evidence Format (P0 Finding)
{
  "evidence_id": "EXT-DB-001",
  "timestamp": "2025-01-31T10:12:00Z",
  "category": "extraction",
  "type": "db_connection_string",
  "severity": "P0",
  "finding_id": "P0-002",

  "connection_string": {
    "pattern": "postgresql://postgres:[REDACTED]@db.abc123def.supabase.co:5432/postgres",
    "host": "db.abc123def.supabase.co",
    "port": 5432,
    "database": "postgres",
    "username": "postgres",
    "password_exposed": true,
    "password_length": 24
  },

  "location": {
    "file": "/static/js/api.chunk.js",
    "line": 234,
    "context": "const DATABASE_URL = 'postgresql://postgres:...' // [REDACTED]"
  },

  "impact": {
    "direct_db_access": true,
    "rls_bypass": true,
    "schema_access": true,
    "auth_users_access": true
  },

  "remediation": {
    "immediate": "Reset database password in Supabase Dashboard",
    "remove_from_code": "Delete DATABASE_URL from client code",
    "verify_env_vars": "Ensure not using NEXT_PUBLIC_DATABASE_URL or similar"
  }
}

Add to timeline.md (P0)
## [TIMESTAMP] - 🔴 P0 CRITICAL: Database Connection String Exposed
- PostgreSQL connection string with password found in client code
- Location: [file]:[line]
- Impact: Direct database access, full RLS bypass
- Evidence: `02-extraction/db-string-exposure/`
- **IMMEDIATE PASSWORD ROTATION REQUIRED**

Related Skills
supabase-extract-service-key — Check for service key exposure
supabase-audit-tables-read — Test data access via API
supabase-report — Generate comprehensive report
Weekly Installs
143
Repository
yoanbernabeu/su…t-skills
GitHub Stars
37
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail