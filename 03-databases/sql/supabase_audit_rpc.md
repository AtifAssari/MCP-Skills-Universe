---
rating: ⭐⭐⭐⭐⭐
title: supabase-audit-rpc
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-audit-rpc
---

# supabase-audit-rpc

skills/yoanbernabeu/supabase-pentest-skills/supabase-audit-rpc
supabase-audit-rpc
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-audit-rpc
SKILL.md
RPC Functions Audit

🔴 CRITICAL: PROGRESSIVE FILE UPDATES REQUIRED

You MUST write to context files AS YOU GO, not just at the end.

Write to .sb-pentest-context.json IMMEDIATELY after each function tested
Log to .sb-pentest-audit.log BEFORE and AFTER each function test
DO NOT wait until the skill completes to update files
If the skill crashes or is interrupted, all prior findings must already be saved

This is not optional. Failure to write progressively is a critical error.

This skill discovers and tests PostgreSQL functions exposed via Supabase's RPC endpoint.

When to Use This Skill
To discover exposed database functions
To test if functions bypass RLS
To check for SQL injection in function parameters
As part of comprehensive API security testing
Prerequisites
Supabase URL and anon key available
Tables audit completed (recommended)
Understanding Supabase RPC

Supabase exposes PostgreSQL functions via:

POST https://[project].supabase.co/rest/v1/rpc/[function_name]


Functions can:

✅ Respect RLS (if using auth.uid() and proper security)
❌ Bypass RLS (if SECURITY DEFINER without checks)
❌ Execute arbitrary SQL (if poorly written)
Risk Levels for Functions
Type	Risk	Description
SECURITY INVOKER	Lower	Runs with caller's permissions
SECURITY DEFINER	Higher	Runs with definer's permissions
Accepts text/json	Higher	Potential for injection
Returns setof	Higher	Can return multiple rows
Usage
Basic RPC Audit
Audit RPC functions on my Supabase project

Test Specific Function
Test the get_user_data RPC function

Output Format
═══════════════════════════════════════════════════════════
 RPC FUNCTIONS AUDIT
═══════════════════════════════════════════════════════════

 Project: abc123def.supabase.co
 Functions Found: 6

 ─────────────────────────────────────────────────────────
 Function Inventory
 ─────────────────────────────────────────────────────────

 1. get_user_profile(user_id uuid)
    Security: INVOKER
    Returns: json
    Status: ✅ SAFE

    Analysis:
    ├── Uses auth.uid() for authorization
    ├── Returns only caller's own profile
    └── RLS is respected

 2. search_posts(query text)
    Security: INVOKER
    Returns: setof posts
    Status: ✅ SAFE

    Analysis:
    ├── Parameterized query (no injection)
    ├── RLS filters results
    └── Only returns published posts

 3. get_all_users()
    Security: DEFINER
    Returns: setof users
    Status: 🔴 P0 - RLS BYPASS

    Analysis:
    ├── SECURITY DEFINER runs as owner
    ├── No auth.uid() check inside function
    ├── Returns ALL users regardless of caller
    └── Bypasses RLS completely!

    Test Result:
    POST /rest/v1/rpc/get_all_users
    → Returns 1,247 user records with PII

    Immediate Fix:
    ```sql
    -- Add authorization check
    CREATE OR REPLACE FUNCTION get_all_users()
    RETURNS setof users
    LANGUAGE sql
    SECURITY INVOKER  -- Change to INVOKER
    AS $$
      SELECT * FROM users
      WHERE auth.uid() = id;  -- Add RLS-like check
    $$;
    ```

 4. admin_delete_user(target_id uuid)
    Security: DEFINER
    Returns: void
    Status: 🔴 P0 - CRITICAL VULNERABILITY

    Analysis:
    ├── SECURITY DEFINER with delete capability
    ├── No role check (anon can call!)
    ├── Can delete any user
    └── No audit trail

    Test Result:
    POST /rest/v1/rpc/admin_delete_user
    Body: {"target_id": "any-uuid"}
    → Function accessible to anon!

    Immediate Fix:
    ```sql
    CREATE OR REPLACE FUNCTION admin_delete_user(target_id uuid)
    RETURNS void
    LANGUAGE plpgsql
    SECURITY DEFINER
    AS $$
    BEGIN
      -- Add role check
      IF NOT (SELECT is_admin FROM profiles WHERE id = auth.uid()) THEN
        RAISE EXCEPTION 'Unauthorized';
      END IF;

      DELETE FROM users WHERE id = target_id;
    END;
    $$;

    -- Or better: restrict to authenticated only
    REVOKE EXECUTE ON FUNCTION admin_delete_user FROM anon;
    ```

 5. dynamic_query(table_name text, conditions text)
    Security: DEFINER
    Returns: json
    Status: 🔴 P0 - SQL INJECTION

    Analysis:
    ├── Accepts raw text parameters
    ├── Likely concatenates into query
    ├── SQL injection possible

    Test Result:
    POST /rest/v1/rpc/dynamic_query
    Body: {"table_name": "users; DROP TABLE users;--", "conditions": "1=1"}
    → Injection vector confirmed!

    Immediate Action:
    → DELETE THIS FUNCTION IMMEDIATELY

    ```sql
    DROP FUNCTION IF EXISTS dynamic_query;
    ```

    Never build queries from user input. Use parameterized queries.

 6. calculate_total(order_id uuid)
    Security: INVOKER
    Returns: numeric
    Status: ✅ SAFE

    Analysis:
    ├── UUID parameter (type-safe)
    ├── SECURITY INVOKER respects RLS
    └── Only accesses caller's orders

 ─────────────────────────────────────────────────────────
 Summary
 ─────────────────────────────────────────────────────────

 Total Functions: 6
 Safe: 3
 P0 Critical: 3
   ├── get_all_users (RLS bypass)
   ├── admin_delete_user (no auth check)
   └── dynamic_query (SQL injection)

 Priority Actions:
 1. DELETE dynamic_query function immediately
 2. Add auth checks to admin_delete_user
 3. Fix get_all_users to respect RLS

═══════════════════════════════════════════════════════════

Injection Testing

The skill tests for SQL injection in text/varchar parameters:

Safe (Parameterized)
-- ✅ Safe: uses parameter placeholder
CREATE FUNCTION search_posts(query text)
RETURNS setof posts
AS $$
  SELECT * FROM posts WHERE title ILIKE '%' || query || '%';
$$ LANGUAGE sql;

Vulnerable (Concatenation)
-- ❌ Vulnerable: dynamic SQL execution
CREATE FUNCTION dynamic_query(tbl text, cond text)
RETURNS json
AS $$
DECLARE result json;
BEGIN
  EXECUTE format('SELECT json_agg(t) FROM %I t WHERE %s', tbl, cond)
  INTO result;
  RETURN result;
END;
$$ LANGUAGE plpgsql;

Context Output
{
  "rpc_audit": {
    "timestamp": "2025-01-31T11:00:00Z",
    "functions_found": 6,
    "summary": {
      "safe": 3,
      "p0_critical": 3,
      "p1_high": 0
    },
    "findings": [
      {
        "function": "get_all_users",
        "severity": "P0",
        "issue": "RLS bypass via SECURITY DEFINER",
        "impact": "All user data accessible",
        "remediation": "Change to SECURITY INVOKER or add auth checks"
      },
      {
        "function": "dynamic_query",
        "severity": "P0",
        "issue": "SQL injection vulnerability",
        "impact": "Arbitrary SQL execution possible",
        "remediation": "Delete function, use parameterized queries"
      }
    ]
  }
}

Best Practices for RPC Functions
1. Prefer SECURITY INVOKER
CREATE FUNCTION my_function()
RETURNS ...
SECURITY INVOKER  -- Respects RLS
AS $$ ... $$;

2. Always Check auth.uid()
CREATE FUNCTION get_my_data()
RETURNS json
AS $$
  SELECT json_agg(d) FROM data d
  WHERE d.user_id = auth.uid();  -- Always filter by caller
$$ LANGUAGE sql SECURITY INVOKER;

3. Use REVOKE for Sensitive Functions
-- Remove anon access
REVOKE EXECUTE ON FUNCTION admin_function FROM anon;

-- Only authenticated users
GRANT EXECUTE ON FUNCTION admin_function TO authenticated;

4. Avoid Text Parameters for Dynamic Queries
-- ❌ Bad
CREATE FUNCTION query(tbl text) ...

-- ✅ Good: use specific functions per table
CREATE FUNCTION get_users() ...
CREATE FUNCTION get_posts() ...

MANDATORY: Progressive Context File Updates

⚠️ This skill MUST update tracking files PROGRESSIVELY during execution, NOT just at the end.

Critical Rule: Write As You Go

DO NOT batch all writes at the end. Instead:

Before testing each function → Log the action to .sb-pentest-audit.log
After each function analyzed → Immediately update .sb-pentest-context.json
After each vulnerability found → Log the finding immediately

This ensures that if the skill is interrupted, crashes, or times out, all findings up to that point are preserved.

Required Actions (Progressive)

Update .sb-pentest-context.json with results:

{
  "rpc_audit": {
    "timestamp": "...",
    "functions_found": 6,
    "summary": { "safe": 3, "p0_critical": 3 },
    "findings": [ ... ]
  }
}


Log to .sb-pentest-audit.log:

[TIMESTAMP] [supabase-audit-rpc] [START] Auditing RPC functions
[TIMESTAMP] [supabase-audit-rpc] [FINDING] P0: dynamic_query has SQL injection
[TIMESTAMP] [supabase-audit-rpc] [CONTEXT_UPDATED] .sb-pentest-context.json updated


If files don't exist, create them before writing.

FAILURE TO UPDATE CONTEXT FILES IS NOT ACCEPTABLE.

MANDATORY: Evidence Collection

📁 Evidence Directory: .sb-pentest-evidence/03-api-audit/rpc-tests/

Evidence Files to Create
File	Content
function-list.json	All discovered RPC functions
vulnerable-functions/[name].json	Details for each vulnerable function
Evidence Format (Vulnerable Function)
{
  "evidence_id": "RPC-001",
  "timestamp": "2025-01-31T10:30:00Z",
  "category": "api-audit",
  "type": "rpc_vulnerability",
  "severity": "P0",

  "function": "get_all_users",

  "analysis": {
    "security_definer": true,
    "auth_check": false,
    "rls_bypass": true
  },

  "test": {
    "request": {
      "method": "POST",
      "url": "https://abc123def.supabase.co/rest/v1/rpc/get_all_users",
      "curl_command": "curl -X POST '$URL/rest/v1/rpc/get_all_users' -H 'apikey: $ANON_KEY' -H 'Content-Type: application/json'"
    },
    "response": {
      "status": 200,
      "rows_returned": 1247,
      "sample_data": "[REDACTED - contains user PII]"
    }
  },

  "impact": "Bypasses RLS, returns all 1,247 user records",
  "remediation": "Change to SECURITY INVOKER or add auth.uid() check"
}

Add to curl-commands.sh
# === RPC FUNCTION TESTS ===
# Test get_all_users function (P0 if accessible)
curl -X POST "$SUPABASE_URL/rest/v1/rpc/get_all_users" \
  -H "apikey: $ANON_KEY" \
  -H "Content-Type: application/json"

# Test admin_delete_user function
curl -X POST "$SUPABASE_URL/rest/v1/rpc/admin_delete_user" \
  -H "apikey: $ANON_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target_id": "test-uuid"}'

Related Skills
supabase-audit-tables-list — List exposed tables
supabase-audit-rls — Test RLS policies
supabase-audit-auth-users — User enumeration tests
Weekly Installs
154
Repository
yoanbernabeu/su…t-skills
GitHub Stars
37
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn