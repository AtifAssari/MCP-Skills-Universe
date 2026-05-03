---
rating: ⭐⭐⭐⭐⭐
title: supabase-audit-auth-users
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-audit-auth-users
---

# supabase-audit-auth-users

skills/yoanbernabeu/supabase-pentest-skills/supabase-audit-auth-users
supabase-audit-auth-users
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-audit-auth-users
SKILL.md
User Enumeration Audit

🔴 CRITICAL: PROGRESSIVE FILE UPDATES REQUIRED

You MUST write to context files AS YOU GO, not just at the end.

Write to .sb-pentest-context.json IMMEDIATELY after each endpoint tested
Log to .sb-pentest-audit.log BEFORE and AFTER each test
DO NOT wait until the skill completes to update files
If the skill crashes or is interrupted, all prior findings must already be saved

This is not optional. Failure to write progressively is a critical error.

This skill tests for user enumeration vulnerabilities in authentication flows.

When to Use This Skill
To check if user existence can be detected
To test login, signup, and recovery flows for information leakage
As part of authentication security audit
Before production deployment
Prerequisites
Supabase URL and anon key available
Auth endpoints accessible
What is User Enumeration?

User enumeration occurs when an application reveals whether a user account exists through:

Vector	Indicator
Different error messages	"User not found" vs "Wrong password"
Response timing	Fast for non-existent, slow for existing
Response codes	404 vs 401
Signup response	"Email already registered"
Why It Matters
Risk	Impact
Targeted attacks	Attackers know valid accounts
Phishing	Confirm targets have accounts
Credential stuffing	Reduce attack scope
Privacy	Reveal user presence
Tests Performed
Endpoint	Test Method
/auth/v1/signup	Try registering existing email
/auth/v1/token	Try login with various emails
/auth/v1/recover	Try password reset
/auth/v1/otp	Try OTP for various emails
Usage
Basic Enumeration Test
Test for user enumeration vulnerabilities

Test Specific Endpoint
Test login endpoint for user enumeration

Output Format
═══════════════════════════════════════════════════════════
 USER ENUMERATION AUDIT
═══════════════════════════════════════════════════════════

 Project: abc123def.supabase.co

 ─────────────────────────────────────────────────────────
 Signup Endpoint (/auth/v1/signup)
 ─────────────────────────────────────────────────────────

 Test: POST with known existing email
 Response for existing: "User already registered"
 Response for new email: User object returned

 Status: 🟠 P2 - ENUMERABLE

 The response clearly indicates if an email is registered.

 Exploitation:
 ```bash
 curl -X POST https://abc123def.supabase.co/auth/v1/signup \
   -H "apikey: [anon-key]" \
   -H "Content-Type: application/json" \
   -d '{"email": "target@example.com", "password": "test123"}'

 # If user exists: {"msg": "User already registered"}
 # If new user: User created or confirmation needed


───────────────────────────────────────────────────────── Login Endpoint (/auth/v1/token) ─────────────────────────────────────────────────────────

Test: POST with different email scenarios

Existing email, wrong password: ├── Response: {"error": "Invalid login credentials"} ├── Time: 245ms └── Code: 400

Non-existing email: ├── Response: {"error": "Invalid login credentials"} ├── Time: 52ms ← Significantly faster! └── Code: 400

Status: 🟠 P2 - ENUMERABLE VIA TIMING

Although the error message is the same, the response time is noticeably different: ├── Existing user: ~200-300ms (password hashing) └── Non-existing: ~50-100ms (no hash check)

Timing Attack PoC:

import requests
import time

def check_user(email):
    start = time.time()
    requests.post(
        'https://abc123def.supabase.co/auth/v1/token',
        params={'grant_type': 'password'},
        json={'email': email, 'password': 'wrong'},
        headers={'apikey': '[anon-key]'}
    )
    elapsed = time.time() - start
    return elapsed > 0.15  # Threshold

exists = check_user('target@example.com')


───────────────────────────────────────────────────────── Password Recovery (/auth/v1/recover) ─────────────────────────────────────────────────────────

Test: POST recovery request for different emails

Existing email: ├── Response: {"message": "Password recovery email sent"} ├── Time: 1250ms (email actually sent) └── Code: 200

Non-existing email: ├── Response: {"message": "Password recovery email sent"} ├── Time: 85ms ← Much faster (no email sent) └── Code: 200

Status: 🟠 P2 - ENUMERABLE VIA TIMING

Same message, but timing reveals existence. Existing users trigger actual email sending (~1s+).

───────────────────────────────────────────────────────── Magic Link / OTP (/auth/v1/otp) ─────────────────────────────────────────────────────────

Test: Request OTP for different emails

Existing email: ├── Response: {"message": "OTP sent"} ├── Time: 1180ms └── Code: 200

Non-existing email: ├── Response: {"error": "User not found"} ├── Time: 95ms └── Code: 400

Status: 🔴 P1 - DIRECTLY ENUMERABLE

The error message explicitly states user doesn't exist.

───────────────────────────────────────────────────────── Summary ─────────────────────────────────────────────────────────

Endpoints Tested: 4 Enumerable: 4 (100%)

Vulnerability Severity: ├── 🔴 P1: OTP endpoint (explicit message) ├── 🟠 P2: Signup endpoint (explicit message) ├── 🟠 P2: Login endpoint (timing attack) └── 🟠 P2: Recovery endpoint (timing attack)

Overall User Enumeration Risk: HIGH

An attacker can determine if any email address has an account in your application.

───────────────────────────────────────────────────────── Mitigation Recommendations ─────────────────────────────────────────────────────────

CONSISTENT RESPONSES Return identical messages for all scenarios: "If an account exists, you will receive an email"

CONSISTENT TIMING Add artificial delay to normalize response times:

const MIN_RESPONSE_TIME = 1000; // 1 second
const start = Date.now();
// ... perform auth operation ...
const elapsed = Date.now() - start;
await new Promise(r => setTimeout(r,
  Math.max(0, MIN_RESPONSE_TIME - elapsed)
));
return response;


RATE LIMITING Already enabled: 3/hour per IP Consider per-email rate limiting too.

CAPTCHA Add CAPTCHA for repeated attempts:

After 3 failed logins
For password recovery
For signup

MONITORING Alert on enumeration patterns:

Many requests with different emails
Sequential email patterns (user1@, user2@, ...)

═══════════════════════════════════════════════════════════


## Timing Analysis

The skill measures response times to detect timing-based enumeration:



Existing user: ├── Password hash verification: ~200-300ms ├── Email sending: ~1000-2000ms └── Database lookup: ~5-20ms

Non-existing user: ├── No hash verification: 0ms ├── No email sending: 0ms └── Database lookup: ~5-20ms (not found)


Threshold detection:
- Difference > 100ms: Possible timing leak
- Difference > 500ms: Definite timing leak

## Context Output

```json
{
  "user_enumeration": {
    "timestamp": "2025-01-31T13:30:00Z",
    "endpoints_tested": 4,
    "vulnerabilities": [
      {
        "endpoint": "/auth/v1/otp",
        "severity": "P1",
        "type": "explicit_message",
        "existing_response": "OTP sent",
        "missing_response": "User not found"
      },
      {
        "endpoint": "/auth/v1/signup",
        "severity": "P2",
        "type": "explicit_message",
        "existing_response": "User already registered",
        "missing_response": "User created"
      },
      {
        "endpoint": "/auth/v1/token",
        "severity": "P2",
        "type": "timing_attack",
        "existing_time_ms": 245,
        "missing_time_ms": 52
      },
      {
        "endpoint": "/auth/v1/recover",
        "severity": "P2",
        "type": "timing_attack",
        "existing_time_ms": 1250,
        "missing_time_ms": 85
      }
    ]
  }
}

Mitigation Code Examples
Consistent Response Time
// Edge Function with normalized timing
const MIN_RESPONSE_TIME = 1500; // 1.5 seconds

Deno.serve(async (req) => {
  const start = Date.now();

  try {
    // Perform actual auth operation
    const result = await handleAuth(req);

    // Normalize response time
    const elapsed = Date.now() - start;
    await new Promise(r => setTimeout(r,
      Math.max(0, MIN_RESPONSE_TIME - elapsed)
    ));

    return new Response(JSON.stringify(result));
  } catch (error) {
    // Same timing for errors
    const elapsed = Date.now() - start;
    await new Promise(r => setTimeout(r,
      Math.max(0, MIN_RESPONSE_TIME - elapsed)
    ));

    // Generic error message
    return new Response(JSON.stringify({
      message: "Check your email if you have an account"
    }));
  }
});

Generic Error Messages
// Don't reveal user existence
async function requestPasswordReset(email: string) {
  // Always return success message
  const response = {
    message: "If an account with that email exists, " +
             "you will receive a password reset link."
  };

  // Perform actual reset in background (don't await)
  supabase.auth.resetPasswordForEmail(email).catch(() => {});

  return response;
}

MANDATORY: Progressive Context File Updates

⚠️ This skill MUST update tracking files PROGRESSIVELY during execution, NOT just at the end.

Critical Rule: Write As You Go

DO NOT batch all writes at the end. Instead:

Before testing each endpoint → Log the action to .sb-pentest-audit.log
After each timing measurement → Immediately update .sb-pentest-context.json
After each enumeration vector found → Log the finding immediately

This ensures that if the skill is interrupted, crashes, or times out, all findings up to that point are preserved.

Required Actions (Progressive)

Update .sb-pentest-context.json with results:

{
  "user_enumeration": {
    "timestamp": "...",
    "endpoints_tested": 4,
    "vulnerabilities": [ ... ]
  }
}


Log to .sb-pentest-audit.log:

[TIMESTAMP] [supabase-audit-auth-users] [START] Testing user enumeration
[TIMESTAMP] [supabase-audit-auth-users] [FINDING] P1: OTP endpoint enumerable
[TIMESTAMP] [supabase-audit-auth-users] [CONTEXT_UPDATED] .sb-pentest-context.json updated


If files don't exist, create them before writing.

FAILURE TO UPDATE CONTEXT FILES IS NOT ACCEPTABLE.

MANDATORY: Evidence Collection

📁 Evidence Directory: .sb-pentest-evidence/05-auth-audit/enumeration-tests/

Evidence Files to Create
File	Content
enumeration-tests/login-timing.json	Login endpoint timing analysis
enumeration-tests/recovery-timing.json	Recovery endpoint timing
enumeration-tests/otp-enumeration.json	OTP endpoint message analysis
Evidence Format
{
  "evidence_id": "AUTH-ENUM-001",
  "timestamp": "2025-01-31T11:00:00Z",
  "category": "auth-audit",
  "type": "user_enumeration",

  "tests": [
    {
      "endpoint": "/auth/v1/token",
      "test_type": "timing_attack",
      "severity": "P2",

      "existing_user_test": {
        "email": "[KNOWN_EXISTING]@example.com",
        "response_time_ms": 245,
        "response": {"error": "Invalid login credentials"}
      },

      "nonexisting_user_test": {
        "email": "definitely-not-exists@example.com",
        "response_time_ms": 52,
        "response": {"error": "Invalid login credentials"}
      },

      "timing_difference_ms": 193,
      "result": "ENUMERABLE",
      "impact": "Can determine if email has account via timing"
    },
    {
      "endpoint": "/auth/v1/otp",
      "test_type": "explicit_message",
      "severity": "P1",

      "existing_user_response": {"message": "OTP sent"},
      "nonexisting_user_response": {"error": "User not found"},

      "result": "ENUMERABLE",
      "impact": "Error message explicitly reveals user existence"
    }
  ],

  "curl_commands": [
    "# Timing test - existing user\ntime curl -X POST '$URL/auth/v1/token?grant_type=password' -H 'apikey: $ANON_KEY' -d '{\"email\": \"existing@example.com\", \"password\": \"wrong\"}'",
    "# Timing test - non-existing user\ntime curl -X POST '$URL/auth/v1/token?grant_type=password' -H 'apikey: $ANON_KEY' -d '{\"email\": \"nonexistent@example.com\", \"password\": \"wrong\"}'"
  ]
}

Related Skills
supabase-audit-auth-config — Full auth configuration
supabase-audit-auth-signup — Signup flow testing
supabase-report — Include in final report
Weekly Installs
146
Repository
yoanbernabeu/su…t-skills
GitHub Stars
37
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn