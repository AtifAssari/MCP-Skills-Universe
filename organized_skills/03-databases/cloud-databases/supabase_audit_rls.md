---
rating: ⭐⭐⭐⭐⭐
title: supabase-audit-rls
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-audit-rls
---

# supabase-audit-rls

skills/yoanbernabeu/supabase-pentest-skills/supabase-audit-rls
supabase-audit-rls
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-audit-rls
SKILL.md
RLS Policy Audit

🔴 CRITICAL: PROGRESSIVE FILE UPDATES REQUIRED

You MUST write to context files AS YOU GO, not just at the end.

Write to .sb-pentest-context.json IMMEDIATELY after each finding
Log to .sb-pentest-audit.log BEFORE and AFTER each test
DO NOT wait until the skill completes to update files
If the skill crashes or is interrupted, all prior findings must already be saved

This is not optional. Failure to write progressively is a critical error.

This skill tests Row Level Security (RLS) policies for common vulnerabilities and misconfigurations.

When to Use This Skill
After discovering data exposure in tables
To verify RLS policies are correctly implemented
To test for common RLS bypass techniques
As part of a comprehensive security audit
Prerequisites
Tables listed
Anon key available
Preferably also test with an authenticated user token
Understanding RLS

Row Level Security in Supabase/PostgreSQL:

-- Enable RLS on a table
ALTER TABLE posts ENABLE ROW LEVEL SECURITY;

-- Create a policy
CREATE POLICY "Users see own posts"
  ON posts FOR SELECT
  USING (auth.uid() = author_id);


If RLS is enabled but no policies exist, ALL access is blocked.

Common RLS Issues
Issue	Description	Severity
RLS Disabled	Table has no RLS protection	P0
Missing Policy	RLS enabled but no SELECT policy	Variable
Overly Permissive	Policy allows too much access	P0-P1
Missing Operation	SELECT policy but no INSERT/UPDATE/DELETE	P1
USING vs WITH CHECK	Read allowed but write inconsistent	P1
Test Vectors

The skill tests these common bypass scenarios:

1. Unauthenticated Access
GET /rest/v1/users?select=*
# No Authorization header or with anon key only

2. Cross-User Access
# As user A, try to access user B's data
GET /rest/v1/orders?user_id=eq.[user-b-id]
Authorization: Bearer [user-a-token]

3. Filter Bypass
# Try to bypass filters with OR conditions
GET /rest/v1/posts?or=(published.eq.true,published.eq.false)

4. Join Exploitation
# Try to access data through related tables
GET /rest/v1/comments?select=*,posts(*)

5. RPC Bypass
# Check if RPC functions bypass RLS
POST /rest/v1/rpc/get_all_users

Usage
Basic RLS Audit
Audit RLS policies on my Supabase project

Specific Table
Test RLS on the users table

With Authenticated User
Test RLS policies using this user token: eyJ...

Output Format
═══════════════════════════════════════════════════════════
 RLS POLICY AUDIT
═══════════════════════════════════════════════════════════

 Project: abc123def.supabase.co
 Tables Audited: 8

 ─────────────────────────────────────────────────────────
 RLS Status by Table
 ─────────────────────────────────────────────────────────

 1. users
    RLS Enabled: ❌ NO
    Status: 🔴 P0 - NO RLS PROTECTION

    All operations allowed without restriction!
    Test Results:
    ├── Anon SELECT: ✓ Returns all 1,247 rows
    ├── Anon INSERT: ✓ Succeeds (tested with rollback)
    ├── Anon UPDATE: ✓ Would succeed
    └── Anon DELETE: ✓ Would succeed

    Immediate Fix:
    ```sql
    ALTER TABLE users ENABLE ROW LEVEL SECURITY;

    CREATE POLICY "Users see own data"
      ON users FOR ALL
      USING (auth.uid() = id);
    ```

 2. posts
    RLS Enabled: ✅ YES
    Policies Found: 2
    Status: ✅ PROPERLY CONFIGURED

    Policies:
    ├── "Public sees published" (SELECT)
    │   └── USING: (published = true)
    └── "Authors manage own" (ALL)
        └── USING: (auth.uid() = author_id)

    Test Results:
    ├── Anon SELECT: Only published posts (correct)
    ├── Anon INSERT: ❌ Blocked (correct)
    ├── Cross-user access: ❌ Blocked (correct)
    └── Filter bypass: ❌ Blocked (correct)

 3. orders
    RLS Enabled: ✅ YES
    Policies Found: 1
    Status: 🟠 P1 - PARTIAL ISSUE

    Policies:
    └── "Users see own orders" (SELECT)
        └── USING: (auth.uid() = user_id)

    Issue Found:
    ├── No INSERT policy - users can't create orders via API
    ├── No UPDATE policy - users can't modify their orders
    └── This may be intentional (orders via Edge Functions)

    Recommendation: Document if intentional, or add policies:
    ```sql
    CREATE POLICY "Users insert own orders"
      ON orders FOR INSERT
      WITH CHECK (auth.uid() = user_id);
    ```

 4. comments
    RLS Enabled: ✅ YES
    Policies Found: 2
    Status: 🟠 P1 - BYPASS POSSIBLE

    Policies:
    ├── "Anyone can read" (SELECT)
    │   └── USING: (true)  ← Too permissive
    └── "Users comment on posts" (INSERT)
        └── WITH CHECK: (auth.uid() = user_id)

    Issue Found:
    └── SELECT policy allows reading all comments
        including user_id, enabling user correlation

    Recommendation:
    ```sql
    -- Use a view to hide user_id
    CREATE VIEW public.comments_public AS
      SELECT id, post_id, content, created_at FROM comments;
    ```

 5. settings
    RLS Enabled: ❌ NO
    Status: 🔴 P0 - NO RLS PROTECTION

    Contains sensitive configuration!
    Immediate action required.

 ─────────────────────────────────────────────────────────
 Summary
 ─────────────────────────────────────────────────────────

 RLS Disabled: 2 tables (users, settings) ← CRITICAL
 RLS Enabled: 6 tables
   ├── Properly Configured: 3
   ├── Partial Issues: 2
   └── Major Issues: 1

 Bypass Tests:
 ├── Unauthenticated access: 2 tables vulnerable
 ├── Cross-user access: 0 tables vulnerable
 ├── Filter bypass: 0 tables vulnerable
 └── Join exploitation: 1 table allows data leakage

═══════════════════════════════════════════════════════════

Context Output
{
  "rls_audit": {
    "timestamp": "2025-01-31T10:45:00Z",
    "tables_audited": 8,
    "summary": {
      "rls_disabled": 2,
      "rls_enabled": 6,
      "properly_configured": 3,
      "partial_issues": 2,
      "major_issues": 1
    },
    "findings": [
      {
        "table": "users",
        "rls_enabled": false,
        "severity": "P0",
        "issue": "No RLS protection",
        "operations_exposed": ["SELECT", "INSERT", "UPDATE", "DELETE"]
      },
      {
        "table": "comments",
        "rls_enabled": true,
        "severity": "P1",
        "issue": "Overly permissive SELECT policy",
        "detail": "user_id exposed enabling correlation"
      }
    ]
  }
}

Common RLS Patterns
Good: User owns their data
CREATE POLICY "Users own their data"
  ON user_data FOR ALL
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

Good: Public read, authenticated write
-- Anyone can read
CREATE POLICY "Public read" ON posts
  FOR SELECT USING (published = true);

-- Only authors can write
CREATE POLICY "Author write" ON posts
  FOR INSERT WITH CHECK (auth.uid() = author_id);

CREATE POLICY "Author update" ON posts
  FOR UPDATE USING (auth.uid() = author_id);

Bad: Using (true)
-- ❌ Too permissive
CREATE POLICY "Anyone" ON secrets
  FOR SELECT USING (true);

Bad: Forgetting WITH CHECK
-- ❌ Users can INSERT any user_id
CREATE POLICY "Insert" ON posts
  FOR INSERT WITH CHECK (true);  -- Should check user_id!

RLS Bypass Documentation

For each bypass found, the skill provides:

Description of the vulnerability
Proof of concept query
Impact assessment
Fix with SQL code
Documentation link
MANDATORY: Progressive Context File Updates

⚠️ This skill MUST update tracking files PROGRESSIVELY during execution, NOT just at the end.

Critical Rule: Write As You Go

DO NOT batch all writes at the end. Instead:

Before testing each table → Log the action to .sb-pentest-audit.log
After each RLS finding → Immediately update .sb-pentest-context.json
After each test completes → Log the result to .sb-pentest-audit.log

This ensures that if the skill is interrupted, crashes, or times out, all findings up to that point are preserved.

Required Actions (Progressive)

Update .sb-pentest-context.json with results:

{
  "rls_audit": {
    "timestamp": "...",
    "tables_audited": 8,
    "summary": { "rls_disabled": 2, ... },
    "findings": [ ... ]
  }
}


Log to .sb-pentest-audit.log:

[TIMESTAMP] [supabase-audit-rls] [START] Auditing RLS policies
[TIMESTAMP] [supabase-audit-rls] [FINDING] P0: users table has no RLS
[TIMESTAMP] [supabase-audit-rls] [CONTEXT_UPDATED] .sb-pentest-context.json updated


If files don't exist, create them before writing.

FAILURE TO UPDATE CONTEXT FILES IS NOT ACCEPTABLE.

MANDATORY: Evidence Collection

📁 Evidence Directory: .sb-pentest-evidence/03-api-audit/rls-tests/

Evidence Files to Create
File	Content
rls-tests/[table]-anon.json	Anonymous access test results
rls-tests/[table]-auth.json	Authenticated access test results
rls-tests/cross-user-test.json	Cross-user access attempts
Evidence Format (RLS Bypass)
{
  "evidence_id": "RLS-001",
  "timestamp": "2025-01-31T10:25:00Z",
  "category": "api-audit",
  "type": "rls_test",
  "severity": "P0",

  "table": "users",
  "rls_enabled": false,

  "tests": [
    {
      "test_name": "anon_select",
      "description": "Anonymous user SELECT access",
      "request": {
        "curl_command": "curl -s '$URL/rest/v1/users?select=*&limit=5' -H 'apikey: $ANON_KEY'"
      },
      "response": {
        "status": 200,
        "rows_returned": 5,
        "total_accessible": 1247
      },
      "result": "VULNERABLE",
      "impact": "All user data accessible without authentication"
    },
    {
      "test_name": "anon_insert",
      "description": "Anonymous user INSERT access",
      "request": {
        "curl_command": "curl -X POST '$URL/rest/v1/users' -H 'apikey: $ANON_KEY' -d '{...}'"
      },
      "response": {
        "status": 201
      },
      "result": "VULNERABLE",
      "impact": "Can create arbitrary user records"
    }
  ],

  "remediation_sql": "ALTER TABLE users ENABLE ROW LEVEL SECURITY;\nCREATE POLICY \"Users see own data\" ON users FOR SELECT USING (auth.uid() = id);"
}

Add to curl-commands.sh
# === RLS BYPASS TESTS ===
# Test anon access to users table
curl -s "$SUPABASE_URL/rest/v1/users?select=*&limit=5" \
  -H "apikey: $ANON_KEY" -H "Authorization: Bearer $ANON_KEY"

# Test filter bypass
curl -s "$SUPABASE_URL/rest/v1/posts?or=(published.eq.true,published.eq.false)" \
  -H "apikey: $ANON_KEY"

Related Skills
supabase-audit-tables-list — List tables first
supabase-audit-tables-read — See actual data exposure
supabase-audit-rpc — RPC functions can bypass RLS
supabase-report — Full security report
Weekly Installs
329
Repository
yoanbernabeu/su…t-skills
GitHub Stars
37
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn