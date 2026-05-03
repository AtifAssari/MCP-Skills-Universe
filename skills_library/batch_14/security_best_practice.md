---
title: security-best-practice
url: https://skills.sh/himself65/auth-spec/security-best-practice
---

# security-best-practice

skills/himself65/auth-spec/security-best-practice
security-best-practice
Installation
$ npx skills add https://github.com/himself65/auth-spec --skill security-best-practice
SKILL.md
Security Best Practice

You are auditing and hardening authentication code against modern (2024-2026) security best practices.

Rules

Individual security rules are in the rules/ directory, organized by impact priority. Read rules/_sections.md for the full taxonomy, and read individual rule files for checklists and fix patterns.

Critical Impact:

rules/credential-storage.md — Password hashing (argon2id first), HIBP breach-check, pepper, secret management
rules/error-handling.md — User enumeration, timing attacks, status/size symmetry, stack trace leaks

High Impact:

rules/session-security.md — Token generation, __Host-/Partitioned cookies, JWT pitfalls, session fixation, rotation on state change
rules/input-validation.md — SQL/NoSQL injection, XSS, SSRF, open redirect, schema validation
rules/oauth-oidc.md — Code + PKCE, state/nonce, redirect-URI allow-list, account-linking pre-takeover
rules/mfa-passkeys.md — TOTP replay prevention, WebAuthn verification, step-up, recovery codes
rules/token-lifecycle.md — Password reset, email verification, magic link, OTP hashing & one-time use

Medium Impact:

rules/rate-limiting.md — Multi-dim throttling (account + IP), SMS pumping, credential stuffing
rules/csrf-protection.md — Origin / Fetch-Metadata, double-submit, SameSite caveats, CORS pitfalls

Lower Priority:

rules/http-security-headers.md — HSTS, nonce-CSP, COOP/COEP/CORP, Clear-Site-Data, Trusted Types
Step 1: Detect Project Context

Before starting, scan the user's project to understand their stack:

Framework config files (next.config.*, package.json, go.mod, Cargo.toml, pyproject.toml, build.gradle*, pom.xml)
Existing auth code — route handlers for sign-up, sign-in, session, sign-out, password reset, email verification
Database/ORM setup and session storage (DB table, Redis, JWT)
Existing security measures (rate limiting, CSRF tokens, CSP headers, MFA, OAuth providers)
Whether the app uses cookies, Bearer tokens, or both (determines which rules apply)
Step 2: Choose Audit Scope

Use the AskUserQuestion tool to ask the user what they want to harden. Use multiSelect: true so they can pick multiple areas at once.

Ask "Which security areas do you want to audit and harden?" with header "Security audit scope".

Credential storage — "Password hashing (argon2id/bcrypt), breach check, pepper, secret management"
Session security — "Token generation, cookie flags, expiry, fixation, JWT pitfalls"
Input validation — "SQL/NoSQL injection, XSS, SSRF, open redirect, schema validation"
OAuth / OIDC — "Code + PKCE, state/nonce, redirect URIs, account linking pre-takeover"
MFA & passkeys — "TOTP, WebAuthn, recovery codes, step-up flows"
Short-lived tokens — "Password reset, email verification, magic link, OTP"
Rate limiting & brute-force protection — "Multi-dim throttling, SMS pumping, credential stuffing"
CSRF protection — "Cross-site request forgery for cookie-based auth"
HTTP security headers — "CSP, HSTS, COOP/COEP, Clear-Site-Data"
Error handling & information leakage — "Generic errors, no timing/size leaks, no user enumeration"
Full audit (all of the above) — "Comprehensive security review"
Step 3: Run the Audit

For each selected area, read the corresponding rule file from rules/ and review the user's code against its checklist. Report findings as:

PASS — implementation is correct
FAIL — vulnerability or misconfiguration found (include file path, line number, and fix)
MISSING — security control is absent (include where to add it and sample code)

After the audit, apply fixes directly to the code. For each fix, explain what was wrong and why the fix is necessary. Link to the relevant rule file for reference.

Step 4: Generate Report

After applying fixes, produce a summary table:

Area	Status	Issues Found	Fixed
Credential storage	PASS/FAIL	description	Yes/No
Session security	PASS/FAIL	description	Yes/No
OAuth / OIDC	PASS/FAIL	description	Yes/No
MFA & passkeys	PASS/FAIL	description	Yes/No
Token lifecycle	PASS/FAIL	description	Yes/No
...	...	...	...

For any issues that cannot be auto-fixed (e.g., require infrastructure changes like adding Redis for rate limiting, configuring HSTS preload at the edge, registering OAuth redirect URIs with the IdP), list them as manual action items with clear instructions.

Step 5: Verify Fixes

After applying fixes:

If the project has tests, run them to ensure nothing broke
If the project has a linter, run it to verify code style
If the project has a build step, run it to check for compilation errors
If feasible, exercise the auth flows end-to-end (sign-up, sign-in, reset, logout) to confirm behavior
Implementation Rules
Never weaken existing security. If the code already uses argon2id, do not downgrade to bcrypt. If cookies already have SameSite=Strict and the __Host- prefix, do not loosen them.
Follow the project's existing patterns. If they use middleware for other concerns, add security middleware the same way. Match naming conventions, file structure, and error handling style.
Do not add dependencies without asking. If a fix requires a new library (e.g. argon2, helmet, @simplewebauthn/server, hibp), ask the user before adding it.
Adapt to the language/framework idioms. Use the canonical approach for each ecosystem (e.g. helmet middleware in Express, SecurityFilterChain in Spring Boot, middleware in Go/Chi).
Be conservative with CSP. A too-strict Content-Security-Policy can break the application. Start in report-only mode, collect violations for 1–2 weeks, then enforce.
Be conservative with HSTS preload. Removal takes weeks. Only preload once every subdomain serves HTTPS.
Respect the auth-spec project rules. All auth code must be hand-written — no auth libraries (better-auth, next-auth, Auth.js, lucia, passport, etc.). Only allowed deps: web framework, ORM, password-hashing lib, WebAuthn verification lib, security-header/CSRF utility libs, and a rate-limit store client (e.g. Redis).
Sources
OWASP Authentication Cheat Sheet
OWASP Session Management Cheat Sheet
OWASP Password Storage Cheat Sheet
OWASP Multifactor Authentication Cheat Sheet
OWASP Forgot Password Cheat Sheet
OWASP Credential Stuffing Prevention Cheat Sheet
OWASP API Security Top 10 (2023)
NIST SP 800-63B rev.4 — Digital Identity Guidelines
OAuth 2.0 Security Best Current Practice
OAuth 2.1 (draft)
W3C WebAuthn Level 3
RFC 8725 — JWT BCP
MDN HTTP Security Headers
Weekly Installs
12
Repository
himself65/auth-spec
GitHub Stars
22
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass