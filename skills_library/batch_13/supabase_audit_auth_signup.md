---
title: supabase-audit-auth-signup
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-audit-auth-signup
---

# supabase-audit-auth-signup

skills/yoanbernabeu/supabase-pentest-skills/supabase-audit-auth-signup
supabase-audit-auth-signup
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-audit-auth-signup
SKILL.md
Signup Flow Audit

🔴 CRITICAL: PROGRESSIVE FILE UPDATES REQUIRED

You MUST write to context files AS YOU GO, not just at the end.

Write to .sb-pentest-context.json IMMEDIATELY after each test completed
Log to .sb-pentest-audit.log BEFORE and AFTER each test
DO NOT wait until the skill completes to update files
If the skill crashes or is interrupted, all prior findings must already be saved

This is not optional. Failure to write progressively is a critical error.

This skill tests the user registration flow for security issues and misconfigurations.

When to Use This Skill
To verify if signup is appropriately restricted
To test for signup abuse vectors
To check rate limiting on registration
As part of authentication security audit
Prerequisites
Supabase URL and anon key available
Auth config audit completed (recommended)
Why Signup Security Matters

Open signup can lead to:

Risk	Description
Spam accounts	Bots creating fake accounts
Resource abuse	Free tier exploitation
Email spam	Using your service to send emails
Data pollution	Fake data in your database
Attack surface	More accounts = more attack vectors
Tests Performed
Test	Purpose
Signup availability	Is registration open?
Email validation	Does it accept invalid emails?
Rate limiting	Can we create many accounts?
Disposable emails	Are temp emails blocked?
Password policy	What passwords are accepted?
Response information	What info is leaked?
Usage
Basic Signup Test
Test signup security on my Supabase project

Check Specific Aspects
Test if disposable emails are blocked for signup

Output Format
═══════════════════════════════════════════════════════════
 SIGNUP FLOW AUDIT
═══════════════════════════════════════════════════════════

 Project: abc123def.supabase.co
 Endpoint: /auth/v1/signup

 ─────────────────────────────────────────────────────────
 Signup Availability
 ─────────────────────────────────────────────────────────

 Status: ✅ OPEN (Anyone can register)

 Test Result:
 POST /auth/v1/signup
 Body: {"email": "test-xxxxx@example.com", "password": "TestPass123!"}
 Response: 200 OK - Account created

 Assessment: Signup is publicly available.
             Review if this is intended.

 ─────────────────────────────────────────────────────────
 Email Validation
 ─────────────────────────────────────────────────────────

 Valid email formats:
 ├── user@domain.com: ✅ Accepted (expected)
 ├── user+tag@domain.com: ✅ Accepted (expected)
 └── user@subdomain.domain.com: ✅ Accepted (expected)

 Invalid email formats:
 ├── user@: ❌ Rejected (good)
 ├── @domain.com: ❌ Rejected (good)
 ├── user@.com: ❌ Rejected (good)
 └── not-an-email: ❌ Rejected (good)

 Disposable Email Test:
 ├── user@mailinator.com: ✅ Accepted ← 🟠 P2
 ├── user@tempmail.com: ✅ Accepted ← 🟠 P2
 └── user@guerrillamail.com: ✅ Accepted ← 🟠 P2

 Finding: Disposable emails are not blocked.
 Risk: Users can create throwaway accounts.

 Recommendation: Consider using an email validation
 service or blocklist in your application logic.

 ─────────────────────────────────────────────────────────
 Password Policy
 ─────────────────────────────────────────────────────────

 Minimum Length Test:
 ├── "12345" (5 chars): ❌ Rejected
 ├── "123456" (6 chars): ✅ Accepted ← P2 Short
 └── "1234567890" (10 chars): ✅ Accepted

 Current Policy: Minimum 6 characters

 Weak Password Test:
 ├── "password": ✅ Accepted ← 🟠 P2
 ├── "123456": ✅ Accepted ← 🟠 P2
 ├── "qwerty123": ✅ Accepted ← 🟠 P2
 └── "letmein": ✅ Accepted ← 🟠 P2

 Finding: Common weak passwords are accepted.

 Recommendation:
 1. Increase minimum length to 8+ characters
 2. Consider password strength requirements
 3. Check against common password lists

 ─────────────────────────────────────────────────────────
 Rate Limiting
 ─────────────────────────────────────────────────────────

 Signup Rate Test (same IP):
 ├── Request 1: ✅ 200 OK
 ├── Request 2: ✅ 200 OK
 ├── Request 3: ✅ 200 OK
 ├── Request 4: ❌ 429 Too Many Requests
 └── Retry-After: 3600 seconds

 Rate Limit: 3 signups/hour per IP
 Assessment: ✅ Rate limiting is active (good)

 ─────────────────────────────────────────────────────────
 Information Disclosure
 ─────────────────────────────────────────────────────────

 Existing Email Test:
 POST /auth/v1/signup (with existing email)
 Response: "User already registered"

 Finding: 🟠 P2 - Response reveals email existence

 This allows:
 ├── Email enumeration attacks
 ├── Knowing if someone has an account
 └── Targeted phishing attempts

 Recommendation: Use generic message like
 "Check your email to continue" for both new
 and existing accounts.

 ─────────────────────────────────────────────────────────
 Email Confirmation
 ─────────────────────────────────────────────────────────

 Status: ❌ NOT REQUIRED (confirmed in auth-config)

 Test: Created account and checked session
 Result: User immediately authenticated without
         email confirmation.

 ─────────────────────────────────────────────────────────
 Summary
 ─────────────────────────────────────────────────────────

 Signup: Open to public
 Rate Limiting: ✅ Active (3/hour)
 Email Confirmation: ❌ Not required

 Findings:
 ├── P1: Email confirmation disabled
 ├── P2: Disposable emails accepted
 ├── P2: Weak passwords accepted
 └── P2: Email enumeration possible

 Security Score: 5/10

 Priority Actions:
 1. Enable email confirmation
 2. Strengthen password policy
 3. Consider disposable email blocking
 4. Use generic error messages

═══════════════════════════════════════════════════════════

Test Details
Disposable Email Detection

Common disposable email domains tested:

mailinator.com
tempmail.com
guerrillamail.com
10minutemail.com
throwaway.email
Weak Password List

Common passwords tested:

password, password123
123456, 12345678
qwerty, qwerty123
letmein, welcome
admin, administrator
Rate Limit Testing
Attempt 1: 200 OK
Attempt 2: 200 OK
Attempt 3: 200 OK
Attempt 4: 429 Too Many Requests

Context Output
{
  "signup_audit": {
    "timestamp": "2025-01-31T13:00:00Z",
    "signup_open": true,
    "rate_limit": {
      "enabled": true,
      "limit": 3,
      "period": "hour"
    },
    "email_validation": {
      "basic_validation": true,
      "disposable_blocked": false
    },
    "password_policy": {
      "min_length": 6,
      "weak_passwords_blocked": false
    },
    "information_disclosure": {
      "email_enumeration": true
    },
    "findings": [
      {
        "severity": "P1",
        "issue": "Email confirmation disabled"
      },
      {
        "severity": "P2",
        "issue": "Disposable emails accepted"
      },
      {
        "severity": "P2",
        "issue": "Weak passwords accepted"
      },
      {
        "severity": "P2",
        "issue": "Email enumeration possible"
      }
    ]
  }
}

Remediation Examples
Block Disposable Emails
// In your signup handler or Edge Function
import { isDisposable } from 'email-validator-package';

if (isDisposable(email)) {
  throw new Error('Please use a permanent email address');
}

Strengthen Password Requirements
// Custom password validation
function validatePassword(password: string): boolean {
  if (password.length < 8) return false;
  if (!/[A-Z]/.test(password)) return false;
  if (!/[a-z]/.test(password)) return false;
  if (!/[0-9]/.test(password)) return false;
  return true;
}

Prevent Email Enumeration
// Always return same message
async function signup(email, password) {
  try {
    await supabase.auth.signUp({ email, password });
  } catch (error) {
    // Don't reveal if email exists
  }
  return { message: 'Check your email to continue' };
}

Restrict Signup

If signup should be invite-only:

// Use admin API to invite users
const { data, error } = await supabaseAdmin.auth.admin.inviteUserByEmail(
  'user@example.com'
);

// Or disable signup in dashboard and use:
const { data, error } = await supabaseAdmin.auth.admin.createUser({
  email: 'user@example.com',
  email_confirm: true
});

MANDATORY: Progressive Context File Updates

⚠️ This skill MUST update tracking files PROGRESSIVELY during execution, NOT just at the end.

Critical Rule: Write As You Go

DO NOT batch all writes at the end. Instead:

Before each signup test → Log the action to .sb-pentest-audit.log
After each vulnerability found → Immediately update .sb-pentest-context.json
After rate limit tests → Log the results immediately

This ensures that if the skill is interrupted, crashes, or times out, all findings up to that point are preserved.

Required Actions (Progressive)

Update .sb-pentest-context.json with results:

{
  "signup_audit": {
    "timestamp": "...",
    "signup_open": true,
    "rate_limit": { ... },
    "findings": [ ... ]
  }
}


Log to .sb-pentest-audit.log:

[TIMESTAMP] [supabase-audit-auth-signup] [START] Testing signup security
[TIMESTAMP] [supabase-audit-auth-signup] [FINDING] P2: Weak passwords accepted
[TIMESTAMP] [supabase-audit-auth-signup] [CONTEXT_UPDATED] .sb-pentest-context.json updated


If files don't exist, create them before writing.

FAILURE TO UPDATE CONTEXT FILES IS NOT ACCEPTABLE.

MANDATORY: Evidence Collection

📁 Evidence Directory: .sb-pentest-evidence/05-auth-audit/signup-tests/

Evidence Files to Create
File	Content
signup-tests/open-signup.json	Signup availability test
signup-tests/weak-password.json	Weak password acceptance test
signup-tests/disposable-email.json	Disposable email test
signup-tests/rate-limit.json	Rate limiting test
Evidence Format
{
  "evidence_id": "AUTH-SIGNUP-001",
  "timestamp": "2025-01-31T10:55:00Z",
  "category": "auth-audit",
  "type": "signup_test",

  "tests": [
    {
      "test_name": "weak_password_acceptance",
      "severity": "P2",
      "request": {
        "method": "POST",
        "url": "https://abc123def.supabase.co/auth/v1/signup",
        "body": {"email": "test@example.com", "password": "123456"},
        "curl_command": "curl -X POST '$URL/auth/v1/signup' -H 'apikey: $ANON_KEY' -H 'Content-Type: application/json' -d '{\"email\": \"test@example.com\", \"password\": \"123456\"}'"
      },
      "response": {
        "status": 200,
        "message": "User created"
      },
      "result": "VULNERABLE",
      "impact": "Weak passwords (6 chars) accepted"
    },
    {
      "test_name": "disposable_email",
      "severity": "P2",
      "request": {
        "body": {"email": "test@mailinator.com", "password": "Test123456!"}
      },
      "response": {
        "status": 200,
        "message": "User created"
      },
      "result": "VULNERABLE",
      "impact": "Disposable emails not blocked"
    }
  ]
}

Related Skills
supabase-audit-auth-config — Full auth configuration
supabase-audit-auth-users — User enumeration testing
supabase-audit-rls — Protect user data with RLS
Weekly Installs
145
Repository
yoanbernabeu/su…t-skills
GitHub Stars
37
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass