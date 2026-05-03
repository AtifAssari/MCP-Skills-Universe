---
title: supabase-extract-service-key
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-extract-service-key
---

# supabase-extract-service-key

skills/yoanbernabeu/supabase-pentest-skills/supabase-extract-service-key
supabase-extract-service-key
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-extract-service-key
SKILL.md
Supabase Service Key Detection

🔴 CRITICAL: PROGRESSIVE FILE UPDATES REQUIRED

You MUST write to context files AS YOU GO, not just at the end.

Write to .sb-pentest-context.json IMMEDIATELY after each discovery
Log to .sb-pentest-audit.log BEFORE and AFTER each action
DO NOT wait until the skill completes to update files
If the skill crashes or is interrupted, all prior findings must already be saved

This is not optional. Failure to write progressively is a critical error.

This skill detects if the service_role key (admin key) is accidentally exposed in client-side code.

When to Use This Skill
As part of every security audit (this is critical)
When reviewing code before production deployment
After detecting Supabase usage to check for this common mistake
Prerequisites
Target application accessible
Supabase detection completed (auto-invokes if needed)
Why This Is Critical

The service_role key bypasses ALL Row Level Security (RLS) policies. If exposed:

Impact	Description
🔴 Full DB Access	Read/write/delete all data in all tables
🔴 Auth Bypass	Access all user data without authentication
🔴 Storage Access	Read/write all files in all buckets
🔴 User Impersonation	Generate tokens for any user

This is a P0 (Critical) finding that requires immediate action.

Service Key vs Anon Key
Aspect	Anon Key	Service Key
Role claim	"role": "anon"	"role": "service_role"
RLS	✅ Respects RLS	❌ Bypasses RLS
Client-side	✅ Expected	❌ NEVER
Server-side	✅ Can use	✅ Should use
Detection Patterns

The skill searches for:

1. Key with service_role Claim
// Decoded JWT payload contains:
{
  "role": "service_role",  // ❌ CRITICAL if in client code
  "iss": "supabase",
  "ref": "abc123def"
}

2. Variable Names
// Common naming patterns
SUPABASE_SERVICE_KEY
SUPABASE_SERVICE_ROLE_KEY
SUPABASE_ADMIN_KEY
SUPABASE_SECRET_KEY
SERVICE_ROLE_KEY

3. Accidental Exposure
// Sometimes exposed alongside anon key
const keys = {
  anon: 'eyJ...',
  service: 'eyJ...'  // ❌ Should not be here
}

Usage
Basic Check
Check for service key leak on https://myapp.example.com

Deep Scan
Deep scan for service key exposure on https://myapp.example.com

Output Format
No Service Key Found (Good)
═══════════════════════════════════════════════════════════
 SERVICE KEY CHECK
═══════════════════════════════════════════════════════════

 Status: ✅ No service_role key detected in client code

 Scanned:
 ├── HTML source: Clean
 ├── JavaScript bundles: 5 files, 2.3MB analyzed
 ├── Inline scripts: 12 blocks checked
 └── Source maps: Not exposed (good)

 JWT Analysis:
 └── 1 key found, confirmed role=anon (safe)

 Result: PASS - No critical key exposure
═══════════════════════════════════════════════════════════

Service Key FOUND (Critical)
═══════════════════════════════════════════════════════════
 🔴 CRITICAL: SERVICE KEY EXPOSED
═══════════════════════════════════════════════════════════

 Severity: P0 - CRITICAL
 Status: ❌ service_role key found in client-side code!

 ⚠️  IMMEDIATE ACTION REQUIRED ⚠️

 Exposed Key:
 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBh
 YmFzZSIsInJlZiI6ImFiYzEyM2RlZiIsInJvbGUiOiJzZXJ2aWNlX3
 JvbGUiLCJpYXQiOjE2NDAwMDAwMDAsImV4cCI6MTk1NTM2MDAwMH0
 .xxxxxxxxxxxxx

 Location:
 └── /static/js/admin.chunk.js (line 89)
     const SUPABASE_KEY = 'eyJhbG...'  // Used in createClient()

 Decoded Payload:
 ├── role: service_role ← CRITICAL
 ├── ref: abc123def
 └── exp: 2031-12-20

 Impact Assessment:
 ├── 🔴 Full database access possible
 ├── 🔴 All RLS policies bypassed
 ├── 🔴 All user data exposed
 └── 🔴 All storage buckets accessible

 ═══════════════════════════════════════════════════════════
 IMMEDIATE REMEDIATION STEPS
 ═══════════════════════════════════════════════════════════

 1. ROTATE THE KEY NOW
    → Supabase Dashboard > Settings > API > Regenerate service_role key

 2. REMOVE FROM CLIENT CODE
    → Delete the key from your source code
    → Redeploy your application

 3. AUDIT FOR ABUSE
    → Check Supabase logs for unauthorized access
    → Review database for unexpected changes

 4. USE EDGE FUNCTIONS
    → Move privileged operations to Edge Functions
    → Client calls Edge Function, which uses service key server-side

 Documentation:
 → https://supabase.com/docs/guides/api/api-keys
 → https://supabase.com/docs/guides/functions

═══════════════════════════════════════════════════════════

Context Output

Saved to .sb-pentest-context.json:

{
  "findings": [
    {
      "id": "SERVICE_KEY_EXPOSED",
      "severity": "P0",
      "title": "Service Role Key Exposed in Client Code",
      "description": "The service_role key was found in client-side JavaScript",
      "location": {
        "file": "/static/js/admin.chunk.js",
        "line": 89
      },
      "evidence": {
        "key_prefix": "eyJhbGciOiJIUzI1NiI...",
        "role": "service_role",
        "project_ref": "abc123def"
      },
      "remediation": {
        "immediate": "Rotate key in Supabase Dashboard",
        "long_term": "Move to Edge Functions",
        "docs": "https://supabase.com/docs/guides/api/api-keys"
      }
    }
  ],
  "supabase": {
    "service_key_exposed": true,
    "service_key_location": "/static/js/admin.chunk.js:89"
  }
}

Source Maps Check

The skill also checks for exposed source maps that might reveal keys:

Source Maps Analysis:
├── main.js.map: ❌ Exposed (may contain secrets)
├── vendor.js.map: ❌ Exposed
└── Recommendation: Disable source maps in production

To check source maps content:
→ Add .map to JS URLs: /static/js/main.js.map

Common Causes
Cause	Solution
Wrong env variable	Use NEXT_PUBLIC_ only for anon key
Copy-paste error	Double-check which key you're using
Debug code left in	Remove before production build
Misconfigured bundler	Ensure service key env vars are not included
Remediation Code Examples
Before (Wrong)
// ❌ WRONG - Service key in client
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_SERVICE_KEY  // ❌ NEVER DO THIS
)

After (Correct)
// ✅ CORRECT - Only anon key in client
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY  // ✅ Safe for client
)

// For privileged operations, call an Edge Function:
const { data } = await supabase.functions.invoke('admin-action', {
  body: { action: 'delete-user', userId: '123' }
})

Edge Function (Server-Side)
// supabase/functions/admin-action/index.ts
import { createClient } from '@supabase/supabase-js'

Deno.serve(async (req) => {
  // ✅ Service key only on server
  const supabase = createClient(
    Deno.env.get('SUPABASE_URL'),
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')  // ✅ Safe on server
  )

  // Perform privileged operation
  // ...
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
    "service_key_exposed": true/false,
    "service_key_location": "path:line"
  },
  "findings": [
    {
      "id": "SERVICE_KEY_EXPOSED",
      "severity": "P0",
      "title": "Service Role Key Exposed",
      ...
    }
  ]
}


Log to .sb-pentest-audit.log:

[TIMESTAMP] [supabase-extract-service-key] [START] Checking for service key exposure
[TIMESTAMP] [supabase-extract-service-key] [CRITICAL] Service key EXPOSED at path:line
[TIMESTAMP] [supabase-extract-service-key] [CONTEXT_UPDATED] .sb-pentest-context.json updated


If files don't exist, create them before writing.

FAILURE TO UPDATE CONTEXT FILES IS NOT ACCEPTABLE.

MANDATORY: Evidence Collection

📁 Evidence Directory: .sb-pentest-evidence/02-extraction/service-key-exposure/

Evidence Files to Create (if service key found)
File	Content
service-key-exposure/location.txt	File path and line number
service-key-exposure/decoded-payload.json	Decoded JWT proving it's service_role
service-key-exposure/code-snippet.txt	Code context (redacted)
Evidence Format (P0 Finding)
{
  "evidence_id": "EXT-SVC-001",
  "timestamp": "2025-01-31T10:10:00Z",
  "category": "extraction",
  "type": "service_key_exposure",
  "severity": "P0",
  "finding_id": "P0-001",

  "key_data": {
    "key_prefix": "eyJhbGciOiJIUzI1NiI...",
    "key_suffix": "...xxxx",
    "role": "service_role"
  },

  "decoded_payload": {
    "iss": "supabase",
    "ref": "abc123def",
    "role": "service_role",
    "iat": "2021-12-20T00:00:00Z",
    "exp": "2031-12-20T00:00:00Z"
  },

  "location": {
    "file": "/static/js/admin.chunk.js",
    "line": 89,
    "context": "const SUPABASE_KEY = 'eyJhbG...' // [REDACTED]"
  },

  "impact": {
    "rls_bypass": true,
    "full_db_access": true,
    "auth_users_access": true,
    "storage_access": true
  },

  "curl_command": "curl -X GET 'https://abc123def.supabase.co/rest/v1/users' -H 'apikey: [SERVICE_KEY]' -H 'Authorization: Bearer [SERVICE_KEY]'"
}

Add to timeline.md (P0)
## [TIMESTAMP] - 🔴 P0 CRITICAL: Service Role Key Exposed
- Service role key found in client-side code
- Location: [file]:[line]
- Impact: Full database access, RLS bypass
- Evidence: `02-extraction/service-key-exposure/`
- **IMMEDIATE ACTION REQUIRED**

Related Skills
supabase-extract-anon-key — Extract the (expected) anon key
supabase-audit-tables-read — Test what data is accessible
supabase-report — Generate full report including this finding
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