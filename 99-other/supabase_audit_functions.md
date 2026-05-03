---
title: supabase-audit-functions
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-audit-functions
---

# supabase-audit-functions

skills/yoanbernabeu/supabase-pentest-skills/supabase-audit-functions
supabase-audit-functions
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-audit-functions
SKILL.md
Edge Functions Audit

🔴 CRITICAL: PROGRESSIVE FILE UPDATES REQUIRED

You MUST write to context files AS YOU GO, not just at the end.

Write to .sb-pentest-context.json IMMEDIATELY after each function tested
Log to .sb-pentest-audit.log BEFORE and AFTER each function test
DO NOT wait until the skill completes to update files
If the skill crashes or is interrupted, all prior findings must already be saved

This is not optional. Failure to write progressively is a critical error.

This skill discovers and tests Supabase Edge Functions for security issues.

When to Use This Skill
To discover exposed Edge Functions
To test function authentication requirements
To check for input validation issues
As part of comprehensive security audit
Prerequisites
Supabase URL available
Detection completed
Understanding Edge Functions

Supabase Edge Functions are Deno-based serverless functions:

https://[project].supabase.co/functions/v1/[function-name]

Security Aspect	Consideration
Authentication	Functions can require JWT or be public
CORS	Cross-origin access control
Input Validation	User input handling
Secrets	Environment variable exposure
Tests Performed
Test	Purpose
Function discovery	Find exposed functions
Auth requirements	Check if JWT required
Input validation	Test for injection
Error handling	Check for information disclosure
Usage
Basic Function Audit
Audit Edge Functions on my Supabase project

Test Specific Function
Test the process-payment Edge Function for security issues

Output Format
═══════════════════════════════════════════════════════════
 EDGE FUNCTIONS AUDIT
═══════════════════════════════════════════════════════════

 Project: abc123def.supabase.co
 Endpoint: https://abc123def.supabase.co/functions/v1/

 ─────────────────────────────────────────────────────────
 Function Discovery
 ─────────────────────────────────────────────────────────

 Discovery Method: Common name enumeration + client code analysis

 Functions Found: 5

 ─────────────────────────────────────────────────────────
 1. hello-world
 ─────────────────────────────────────────────────────────

 Endpoint: /functions/v1/hello-world
 Method: GET, POST

 Authentication Test:
 ├── Without JWT: ✅ 200 OK
 └── Status: ℹ️ Public function (no auth required)

 Response:
 ```json
 {"message": "Hello, World!"}


Assessment: ✅ APPROPRIATE Simple public endpoint, no sensitive operations.

───────────────────────────────────────────────────────── 2. process-payment ─────────────────────────────────────────────────────────

Endpoint: /functions/v1/process-payment Method: POST

Authentication Test: ├── Without JWT: ❌ 401 Unauthorized ├── With valid JWT: ✅ 200 OK └── Status: ✅ Authentication required

Input Validation Test: ├── Missing amount: ❌ 400 Bad Request (good) ├── Negative amount: ❌ 400 Bad Request (good) ├── String amount: ❌ 400 Bad Request (good) └── Valid input: ✅ 200 OK

Error Response Test: ├── Error format: Generic message (good) └── Stack trace: ❌ Not exposed (good)

Assessment: ✅ PROPERLY SECURED Requires auth, validates input, safe error handling.

───────────────────────────────────────────────────────── 3. get-user-data ─────────────────────────────────────────────────────────

Endpoint: /functions/v1/get-user-data Method: GET

Authentication Test: ├── Without JWT: ❌ 401 Unauthorized └── Status: ✅ Authentication required

Authorization Test: ├── Request own data: ✅ 200 OK ├── Request other user's data: ✅ 200 OK ← 🔴 P0! └── Status: 🔴 BROKEN ACCESS CONTROL

Test:

# As user A, request user B's data
curl https://abc123def.supabase.co/functions/v1/get-user-data?user_id=user-b-id \
  -H "Authorization: Bearer [user-a-token]"

# Returns user B's data!


Finding: 🔴 P0 - IDOR VULNERABILITY Function accepts user_id parameter without verifying that the authenticated user is requesting their own data.

Fix:

// In Edge Function
const { user_id } = await req.json();
const jwt_user = getUser(req); // From JWT

// Verify ownership
if (user_id !== jwt_user.id) {
  return new Response('Forbidden', { status: 403 });
}


───────────────────────────────────────────────────────── 4. admin-panel ─────────────────────────────────────────────────────────

Endpoint: /functions/v1/admin-panel Method: GET, POST

Authentication Test: ├── Without JWT: ❌ 401 Unauthorized ├── With regular user JWT: ✅ 200 OK ← 🔴 P0! └── Status: 🔴 MISSING ROLE CHECK

Finding: 🔴 P0 - PRIVILEGE ESCALATION Admin function accessible to any authenticated user. No role verification in function code.

Fix:

// Verify admin role
const user = getUser(req);
const { data: profile } = await supabase
  .from('profiles')
  .select('is_admin')
  .eq('id', user.id)
  .single();

if (!profile?.is_admin) {
  return new Response('Forbidden', { status: 403 });
}


───────────────────────────────────────────────────────── 5. webhook-handler ─────────────────────────────────────────────────────────

Endpoint: /functions/v1/webhook-handler Method: POST

Authentication Test: ├── Without JWT: ✅ 200 OK (expected for webhooks) └── Status: ℹ️ Public (webhook endpoints are typically public)

Webhook Security Test: ├── Signature validation: ⚠️ Unable to test (need valid signature) └── Rate limiting: Unknown

Error Response Test:

{
  "error": "Invalid signature",
  "expected": "sha256=abc123...",
  "received": "sha256=xyz789..."
}


Finding: 🟠 P1 - INFORMATION DISCLOSURE Error response reveals expected signature format. Could help attacker understand validation mechanism.

Fix:

// Generic error, log details server-side
if (!validSignature) {
  console.error(`Invalid signature: expected ${expected}, got ${received}`);
  return new Response('Unauthorized', { status: 401 });
}


───────────────────────────────────────────────────────── Summary ─────────────────────────────────────────────────────────

Functions Found: 5

Security Assessment: ├── ✅ Secure: 2 (hello-world, process-payment) ├── 🔴 P0: 2 (get-user-data IDOR, admin-panel privilege escalation) └── 🟠 P1: 1 (webhook-handler info disclosure)

Critical Findings:

IDOR in get-user-data - any user can access any user's data
Missing role check in admin-panel - any user is admin

Priority Actions:

Fix get-user-data to verify user owns requested data
Add admin role verification to admin-panel
Fix webhook-handler error messages

═══════════════════════════════════════════════════════════


## Common Function Vulnerabilities

| Vulnerability | Description | Severity |
|---------------|-------------|----------|
| No auth | Function accessible without JWT | P0-P2 |
| IDOR | User can access other users' data | P0 |
| Missing role check | Regular user accesses admin functions | P0 |
| Input injection | User input not validated | P0-P1 |
| Info disclosure | Errors reveal internal details | P1-P2 |
| CORS misconfigured | Accessible from unintended origins | P1-P2 |

## Function Discovery Methods

### 1. Client Code Analysis

```javascript
// Look for function invocations in client code
supabase.functions.invoke('function-name', {...})
fetch('/functions/v1/function-name', {...})

2. Common Name Enumeration

Tested function names:

hello-world, hello, test
process-payment, payment, checkout
get-user-data, user, profile
admin, admin-panel, dashboard
webhook, webhook-handler, stripe-webhook
send-email, notify, notification
3. Error Response Analysis
404 Not Found → Function doesn't exist
401 Unauthorized → Function exists, needs auth
200 OK → Function exists, accessible

Context Output
{
  "functions_audit": {
    "timestamp": "2025-01-31T14:30:00Z",
    "functions_found": 5,
    "findings": [
      {
        "function": "get-user-data",
        "severity": "P0",
        "vulnerability": "IDOR",
        "description": "Any authenticated user can access any user's data",
        "remediation": "Verify user owns requested resource"
      },
      {
        "function": "admin-panel",
        "severity": "P0",
        "vulnerability": "Privilege Escalation",
        "description": "No role check, any authenticated user is admin",
        "remediation": "Add admin role verification"
      }
    ]
  }
}

Secure Function Patterns
Authentication Check
import { createClient } from '@supabase/supabase-js'

Deno.serve(async (req) => {
  // Get JWT from header
  const authHeader = req.headers.get('Authorization');
  if (!authHeader) {
    return new Response('Unauthorized', { status: 401 });
  }

  // Verify JWT with Supabase
  const supabase = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_ANON_KEY')!,
    { global: { headers: { Authorization: authHeader } } }
  );

  const { data: { user }, error } = await supabase.auth.getUser();
  if (error || !user) {
    return new Response('Unauthorized', { status: 401 });
  }

  // User is authenticated
  // ...
});

Authorization Check (IDOR Prevention)
// For user-specific resources
const requestedUserId = body.user_id;
const authenticatedUserId = user.id;

if (requestedUserId !== authenticatedUserId) {
  return new Response('Forbidden', { status: 403 });
}

Role Check (Admin)
// Check admin role
const { data: profile } = await supabase
  .from('profiles')
  .select('role')
  .eq('id', user.id)
  .single();

if (profile?.role !== 'admin') {
  return new Response('Forbidden', { status: 403 });
}

Input Validation
import { z } from 'zod';

const PaymentSchema = z.object({
  amount: z.number().positive().max(10000),
  currency: z.enum(['usd', 'eur', 'gbp']),
  description: z.string().max(200).optional()
});

// Validate input
const result = PaymentSchema.safeParse(body);
if (!result.success) {
  return new Response(
    JSON.stringify({ error: 'Invalid input' }),
    { status: 400 }
  );
}

MANDATORY: Progressive Context File Updates

⚠️ This skill MUST update tracking files PROGRESSIVELY during execution, NOT just at the end.

Critical Rule: Write As You Go

DO NOT batch all writes at the end. Instead:

Before testing each function → Log the action to .sb-pentest-audit.log
After each vulnerability found → Immediately update .sb-pentest-context.json
After each function test completes → Log the result immediately

This ensures that if the skill is interrupted, crashes, or times out, all findings up to that point are preserved.

Required Actions (Progressive)

Update .sb-pentest-context.json with results:

{
  "functions_audit": {
    "timestamp": "...",
    "functions_found": 5,
    "findings": [ ... ]
  }
}


Log to .sb-pentest-audit.log:

[TIMESTAMP] [supabase-audit-functions] [START] Auditing Edge Functions
[TIMESTAMP] [supabase-audit-functions] [FINDING] P0: IDOR in get-user-data
[TIMESTAMP] [supabase-audit-functions] [CONTEXT_UPDATED] .sb-pentest-context.json updated


If files don't exist, create them before writing.

FAILURE TO UPDATE CONTEXT FILES IS NOT ACCEPTABLE.

MANDATORY: Evidence Collection

📁 Evidence Directory: .sb-pentest-evidence/07-functions-audit/

Evidence Files to Create
File	Content
discovered-functions.json	List of discovered Edge Functions
function-tests/[name].json	Test results per function
Evidence Format (IDOR Vulnerability)
{
  "evidence_id": "FN-001",
  "timestamp": "2025-01-31T11:10:00Z",
  "category": "functions-audit",
  "type": "idor_vulnerability",
  "severity": "P0",

  "function": "get-user-data",
  "endpoint": "https://abc123def.supabase.co/functions/v1/get-user-data",

  "tests": [
    {
      "test_name": "auth_required",
      "request": {
        "method": "GET",
        "headers": {},
        "curl_command": "curl '$URL/functions/v1/get-user-data'"
      },
      "response": {"status": 401},
      "result": "PASS"
    },
    {
      "test_name": "idor_test",
      "description": "As user A, request user B's data",
      "request": {
        "method": "GET",
        "url": "$URL/functions/v1/get-user-data?user_id=user-b-id",
        "headers": {"Authorization": "Bearer [USER_A_TOKEN]"},
        "curl_command": "curl '$URL/functions/v1/get-user-data?user_id=user-b-id' -H 'Authorization: Bearer [USER_A_TOKEN]'"
      },
      "response": {
        "status": 200,
        "body": {"id": "user-b-id", "email": "[REDACTED]", "data": "[REDACTED]"}
      },
      "result": "VULNERABLE",
      "impact": "Any authenticated user can access any other user's data"
    }
  ],

  "remediation": "Add ownership check: if (user_id !== jwt_user.id) return 403"
}

Evidence Format (Privilege Escalation)
{
  "evidence_id": "FN-002",
  "timestamp": "2025-01-31T11:15:00Z",
  "category": "functions-audit",
  "type": "privilege_escalation",
  "severity": "P0",

  "function": "admin-panel",

  "test": {
    "description": "Regular user accessing admin function",
    "request": {
      "method": "GET",
      "headers": {"Authorization": "Bearer [REGULAR_USER_TOKEN]"},
      "curl_command": "curl '$URL/functions/v1/admin-panel' -H 'Authorization: Bearer [REGULAR_USER_TOKEN]'"
    },
    "response": {
      "status": 200,
      "body": {"admin_data": "[REDACTED]"}
    },
    "result": "VULNERABLE",
    "impact": "Any authenticated user has admin access"
  }
}

Related Skills
supabase-audit-rpc — Database functions (different from Edge Functions)
supabase-audit-auth-config — Auth configuration
supabase-report — Include in final report
Weekly Installs
166
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