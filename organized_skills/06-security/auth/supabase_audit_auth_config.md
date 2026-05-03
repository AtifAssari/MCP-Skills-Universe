---
rating: ⭐⭐⭐
title: supabase-audit-auth-config
url: https://skills.sh/yoanbernabeu/supabase-pentest-skills/supabase-audit-auth-config
---

# supabase-audit-auth-config

skills/yoanbernabeu/supabase-pentest-skills/supabase-audit-auth-config
supabase-audit-auth-config
Installation
$ npx skills add https://github.com/yoanbernabeu/supabase-pentest-skills --skill supabase-audit-auth-config
SKILL.md
Authentication Configuration Audit

🔴 CRITICAL: PROGRESSIVE FILE UPDATES REQUIRED

You MUST write to context files AS YOU GO, not just at the end.

Write to .sb-pentest-context.json IMMEDIATELY after each setting analyzed
Log to .sb-pentest-audit.log BEFORE and AFTER each test
DO NOT wait until the skill completes to update files
If the skill crashes or is interrupted, all prior findings must already be saved

This is not optional. Failure to write progressively is a critical error.

This skill analyzes the authentication configuration of a Supabase project.

When to Use This Skill
To review authentication security settings
Before production deployment
When auditing auth-related vulnerabilities
As part of comprehensive security review
Prerequisites
Supabase URL and anon key available
Detection completed
Auth Endpoints

Supabase Auth (GoTrue) exposes:

https://[project].supabase.co/auth/v1/

Endpoint	Purpose
/auth/v1/settings	Public settings (limited)
/auth/v1/signup	User registration
/auth/v1/token	Authentication
/auth/v1/user	Current user info
/auth/v1/recover	Password recovery
What Can Be Detected

From the public API, we can detect:

Setting	Detection Method
Email auth enabled	Attempt signup
Phone auth enabled	Check settings
OAuth providers	Check settings
Signup disabled	Attempt signup
Email confirmation	Signup response
Password requirements	Error messages
Usage
Basic Auth Audit
Audit authentication configuration

Check Specific Features
Check if signup is open and what providers are enabled

Output Format
═══════════════════════════════════════════════════════════
 AUTHENTICATION CONFIGURATION AUDIT
═══════════════════════════════════════════════════════════

 Project: abc123def.supabase.co
 Auth Endpoint: https://abc123def.supabase.co/auth/v1/

 ─────────────────────────────────────────────────────────
 Authentication Methods
 ─────────────────────────────────────────────────────────

 Email/Password: ✅ Enabled
 ├── Signup: ✅ Open (anyone can register)
 ├── Email Confirmation: ❌ NOT REQUIRED ← P1 Issue
 ├── Password Min Length: 6 characters ← P2 Consider longer
 └── Secure Password Check: Unknown

 Phone/SMS: ✅ Enabled
 └── Provider: Twilio

 Magic Link: ✅ Enabled
 └── OTP Expiry: 300 seconds (5 min)

 OAuth Providers Detected: 3
 ├── Google: ✅ Enabled
 ├── GitHub: ✅ Enabled
 └── Discord: ✅ Enabled

 Anonymous Auth: ✅ Enabled ← Review if intended

 ─────────────────────────────────────────────────────────
 Security Settings
 ─────────────────────────────────────────────────────────

 Rate Limiting:
 ├── Signup: 3/hour per IP (good)
 ├── Token: 30/hour per IP (good)
 └── Recovery: 3/hour per IP (good)

 Session Configuration:
 ├── JWT Expiry: 3600 seconds (1 hour)
 ├── Refresh Token Rotation: Unknown
 └── Inactivity Timeout: Unknown

 Security Headers:
 ├── CORS: Configured
 ├── Allowed Origins: * (wildcard) ← P2 Consider restricting
 └── Credentials: Allowed

 ─────────────────────────────────────────────────────────
 Findings
 ─────────────────────────────────────────────────────────

 🟠 P1: Email Confirmation Disabled

 Issue: Users can signup and immediately access the app
        without verifying their email address.

 Risks:
 ├── Fake accounts with invalid emails
 ├── Typosquatting (user@gmial.com)
 ├── No verified communication channel
 └── Potential for abuse

 Recommendation:
 Supabase Dashboard → Authentication → Email Templates
 → Enable "Confirm email"

 ─────────────────────────────────────────────────────────

 🟡 P2: Short Minimum Password Length

 Issue: Minimum password length is 6 characters.

 Recommendation: Increase to 8-12 characters minimum.
 Supabase Dashboard → Authentication → Settings
 → Minimum password length

 ─────────────────────────────────────────────────────────

 🟡 P2: Wildcard CORS Origin

 Issue: CORS allows requests from any origin (*).

 Recommendation: Restrict to your domains only.
 Supabase Dashboard → Authentication → URL Configuration
 → Site URL and Redirect URLs

 ─────────────────────────────────────────────────────────

 ℹ️ INFO: Anonymous Auth Enabled

 Note: Anonymous authentication is enabled.

 This is fine if intentional (guest access).
 Review if you expect all users to be authenticated.

 ─────────────────────────────────────────────────────────
 Summary
 ─────────────────────────────────────────────────────────

 Auth Methods: 5 enabled
 OAuth Providers: 3

 Findings:
 ├── P1 (High): 1 - Email confirmation disabled
 ├── P2 (Medium): 2 - Password length, CORS
 └── Info: 1 - Anonymous auth enabled

 Recommended Actions:
 1. Enable email confirmation
 2. Increase minimum password length
 3. Restrict CORS to specific domains
 4. Review if anonymous auth is needed

═══════════════════════════════════════════════════════════

Security Checklist
Email Authentication
Setting	Recommended	Risk if Wrong
Email Confirmation	✅ Required	Fake accounts
Password Length	≥8 chars	Weak passwords
Password Complexity	Enable	Easy to guess
Rate Limiting	Enable	Brute force
OAuth Configuration
Setting	Recommended	Risk if Wrong
Verified providers only	Yes	Account takeover
Proper redirect URLs	Specific URLs	OAuth redirect attacks
State parameter	Enabled	CSRF attacks
Session Security
Setting	Recommended	Risk if Wrong
Short JWT expiry	1 hour or less	Token theft
Refresh token rotation	Enabled	Token reuse
Secure cookie flags	HttpOnly, Secure, SameSite	XSS, CSRF
Context Output
{
  "auth_config": {
    "timestamp": "2025-01-31T12:30:00Z",
    "methods": {
      "email": {
        "enabled": true,
        "signup_open": true,
        "email_confirmation": false,
        "min_password_length": 6
      },
      "phone": {
        "enabled": true,
        "provider": "twilio"
      },
      "magic_link": {
        "enabled": true,
        "otp_expiry": 300
      },
      "oauth": {
        "enabled": true,
        "providers": ["google", "github", "discord"]
      },
      "anonymous": {
        "enabled": true
      }
    },
    "findings": [
      {
        "severity": "P1",
        "issue": "Email confirmation disabled",
        "recommendation": "Enable email confirmation in dashboard"
      }
    ]
  }
}

Common Auth Vulnerabilities
1. No Email Confirmation
// User can signup with any email
const { data, error } = await supabase.auth.signUp({
  email: 'fake@example.com',  // No verification needed
  password: 'password123'
})
// User is immediately authenticated

2. Weak Password Policy
// Weak password accepted
await supabase.auth.signUp({
  email: 'user@example.com',
  password: '123456'  // Accepted with min length 6
})

3. Open Signup When Not Needed

If your app should only have admin-created users:

-- Disable public signup via dashboard
-- Or use invite-only flow

Remediation Examples
Enable Email Confirmation
Supabase Dashboard → Authentication → Email Templates
Enable "Confirm email"
Customize confirmation email template
Handle unconfirmed users in your app
Strengthen Password Requirements
Dashboard → Authentication → Settings
Set minimum length to 8+
Consider enabling password strength checks
Restrict CORS
Dashboard → Authentication → URL Configuration
Set specific Site URL
Add only your domains to Redirect URLs
Remove wildcard entries
MANDATORY: Progressive Context File Updates

⚠️ This skill MUST update tracking files PROGRESSIVELY during execution, NOT just at the end.

Critical Rule: Write As You Go

DO NOT batch all writes at the end. Instead:

Before checking each auth method → Log the action to .sb-pentest-audit.log
After each configuration analyzed → Immediately update .sb-pentest-context.json
After each finding discovered → Log the severity immediately

This ensures that if the skill is interrupted, crashes, or times out, all findings up to that point are preserved.

Required Actions (Progressive)

Update .sb-pentest-context.json with results:

{
  "auth_config": {
    "timestamp": "...",
    "methods": { ... },
    "findings": [ ... ]
  }
}


Log to .sb-pentest-audit.log:

[TIMESTAMP] [supabase-audit-auth-config] [START] Auditing auth configuration
[TIMESTAMP] [supabase-audit-auth-config] [FINDING] P1: Email confirmation disabled
[TIMESTAMP] [supabase-audit-auth-config] [CONTEXT_UPDATED] .sb-pentest-context.json updated


If files don't exist, create them before writing.

FAILURE TO UPDATE CONTEXT FILES IS NOT ACCEPTABLE.

MANDATORY: Evidence Collection

📁 Evidence Directory: .sb-pentest-evidence/05-auth-audit/

Evidence Files to Create
File	Content
auth-settings.json	Complete auth configuration
Evidence Format
{
  "evidence_id": "AUTH-CFG-001",
  "timestamp": "2025-01-31T10:50:00Z",
  "category": "auth-audit",
  "type": "auth_configuration",

  "endpoint": "https://abc123def.supabase.co/auth/v1/",

  "configuration": {
    "email_auth": {
      "enabled": true,
      "signup_open": true,
      "email_confirmation_required": false,
      "min_password_length": 6
    },
    "phone_auth": {
      "enabled": true,
      "provider": "twilio"
    },
    "oauth_providers": ["google", "github", "discord"],
    "anonymous_auth": true
  },

  "security_settings": {
    "rate_limiting": {
      "signup": "3/hour",
      "token": "30/hour",
      "recovery": "3/hour"
    },
    "jwt_expiry": 3600,
    "cors_origins": "*"
  },

  "findings": [
    {
      "severity": "P1",
      "issue": "Email confirmation disabled",
      "impact": "Users can signup without verifying email",
      "recommendation": "Enable email confirmation"
    },
    {
      "severity": "P2",
      "issue": "Weak password policy",
      "impact": "Minimum 6 characters allows weak passwords",
      "recommendation": "Increase to 8+ characters"
    }
  ]
}

Add to curl-commands.sh
# === AUTH CONFIGURATION TESTS ===
# Test signup availability
curl -X POST "$SUPABASE_URL/auth/v1/signup" \
  -H "apikey: $ANON_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "test123456"}'

# Test password policy (weak password)
curl -X POST "$SUPABASE_URL/auth/v1/signup" \
  -H "apikey: $ANON_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email": "weak@example.com", "password": "123456"}'

Related Skills
supabase-audit-auth-signup — Test signup flow
supabase-audit-auth-users — Test user enumeration
supabase-audit-rls — Auth users need RLS protection
Weekly Installs
171
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