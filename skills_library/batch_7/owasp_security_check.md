---
title: owasp-security-check
url: https://skills.sh/sergiodxa/agent-skills/owasp-security-check
---

# owasp-security-check

skills/sergiodxa/agent-skills/owasp-security-check
owasp-security-check
Installation
$ npx skills add https://github.com/sergiodxa/agent-skills --skill owasp-security-check
Summary

Security audit framework for web applications and REST APIs covering OWASP Top 10 vulnerabilities.

20 rules organized across 5 categories: Authentication & Authorization, Data Protection, Input/Output Security, Configuration & Headers, and API & Monitoring
Covers critical vulnerabilities including injection attacks, broken access control, cryptographic failures, CSRF, SSRF, and insecure deserialization with code examples for both vulnerable and secure patterns
Includes systematic audit workflow prioritized by severity (CRITICAL, HIGH, MEDIUM, LOW) with structured reporting format for findings and remediation
Provides quick-reference patterns for common vulnerabilities like SQL injection, XSS, hardcoded secrets, weak crypto, and insecure cookies
SKILL.md
OWASP Security Check

Comprehensive security audit patterns for web applications and REST APIs. Contains 20 rules across 5 categories covering OWASP Top 10 and common web vulnerabilities.

When to Apply

Use this skill when:

Auditing a codebase for security vulnerabilities
Reviewing user-provided file or folder for security issues
Checking authentication/authorization implementations
Evaluating REST API security
Assessing data protection measures
Reviewing configuration and deployment settings
Before production deployment
After adding new features that handle sensitive data
How to Use This Skill
Identify application type - Web app, REST API, SPA, SSR, or mixed
Scan by priority - Start with CRITICAL rules, then HIGH, then MEDIUM
Review relevant rule files - Load specific rules from @rules/ directory
Report findings - Note severity, file location, and impact
Provide remediation - Give concrete code examples for fixes
Audit Workflow
Step 1: Systematic Review by Priority

Work through categories by priority:

CRITICAL: Authentication & Authorization, Data Protection, Input/Output Security
HIGH: Configuration & Headers
MEDIUM: API & Monitoring
Step 2: Generate Report

Format findings as:

Severity: CRITICAL | HIGH | MEDIUM | LOW
Category: Rule name
File: Path and line number
Issue: What's wrong
Impact: Security consequence
Fix: Code example of remediation
Rules Summary
Authentication & Authorization (CRITICAL)
broken-access-control - @rules/broken-access-control.md

Check for missing authorization, IDOR, privilege escalation.

// Bad: No authorization check
async function getUser(req: Request): Promise<Response> {
  let url = new URL(req.url);
  let userId = url.searchParams.get("id");
  let user = await db.user.findUnique({ where: { id: userId } });
  return new Response(JSON.stringify(user));
}

// Good: Verify ownership
async function getUser(req: Request): Promise<Response> {
  let session = await getSession(req);
  let url = new URL(req.url);
  let userId = url.searchParams.get("id");

  if (session.userId !== userId && !session.isAdmin) {
    return new Response("Forbidden", { status: 403 });
  }

  let user = await db.user.findUnique({ where: { id: userId } });
  return new Response(JSON.stringify(user));
}

authentication-failures - @rules/authentication-failures.md

Check for weak authentication, missing MFA, session issues.

// Bad: Weak password check
if (password.length >= 6) {
  /* allow */
}

// Good: Strong password requirements
function validatePassword(password: string) {
  if (password.length < 12) return false;
  if (!/[A-Z]/.test(password)) return false;
  if (!/[a-z]/.test(password)) return false;
  if (!/[0-9]/.test(password)) return false;
  if (!/[^A-Za-z0-9]/.test(password)) return false;
  return true;
}

Data Protection (CRITICAL)
cryptographic-failures - @rules/cryptographic-failures.md

Check for weak encryption, plaintext storage, bad hashing.

// Bad: MD5 for passwords
let hash = crypto.createHash("md5").update(password).digest("hex");

// Good: bcrypt with salt
let hash = await bcrypt(password, 12);

sensitive-data-exposure - @rules/sensitive-data-exposure.md

Check for PII in logs/responses, error messages leaking info.

// Bad: Exposing sensitive data
return new Response(JSON.stringify(user)); // Contains password hash, email, etc.

// Good: Return only needed fields
return new Response(
  JSON.stringify({
    id: user.id,
    username: user.username,
    displayName: user.displayName,
  }),
);

data-integrity-failures - @rules/data-integrity-failures.md

Check for unsigned data, insecure deserialization.

// Bad: Trusting unsigned JWT
let decoded = JSON.parse(atob(token.split(".")[1]));
if (decoded.isAdmin) {
  /* grant access */
}

// Good: Verify signature
let payload = await verifyJWT(token, secret);

secrets-management - @rules/secrets-management.md

Check for hardcoded secrets, exposed env vars.

// Bad: Hardcoded secret
const API_KEY = "sk_live_a1b2c3d4e5f6";

// Good: Environment variables
let API_KEY = process.env.API_KEY;
if (!API_KEY) throw new Error("API_KEY not configured");

Input/Output Security (CRITICAL)
injection-attacks - @rules/injection-attacks.md

Check for SQL, XSS, NoSQL, Command, Path Traversal injection.

// Bad: SQL injection
let query = `SELECT * FROM users WHERE email = '${email}'`;

// Good: Parameterized query
let user = await db.user.findUnique({ where: { email } });

ssrf-attacks - @rules/ssrf-attacks.md

Check for unvalidated URLs, internal network access.

// Bad: Fetching user-provided URL
let url = await req.json().then((d) => d.url);
let response = await fetch(url);

// Good: Validate against allowlist
const ALLOWED_DOMAINS = ["api.example.com", "cdn.example.com"];
let url = new URL(await req.json().then((d) => d.url));
if (!ALLOWED_DOMAINS.includes(url.hostname)) {
  return new Response("Invalid URL", { status: 400 });
}

file-upload-security - @rules/file-upload-security.md

Check for unrestricted uploads, MIME validation.

// Bad: No file type validation
let file = await req.formData().then((fd) => fd.get("file"));
await writeFile(`./uploads/${file.name}`, file);

// Good: Validate type and extension
const ALLOWED_TYPES = ["image/jpeg", "image/png", "image/webp"];
const ALLOWED_EXTS = [".jpg", ".jpeg", ".png", ".webp"];
let file = await req.formData().then((fd) => fd.get("file") as File);

if (!ALLOWED_TYPES.includes(file.type)) {
  return new Response("Invalid file type", { status: 400 });
}

redirect-validation - @rules/redirect-validation.md

Check for open redirects, unvalidated redirect URLs.

// Bad: Unvalidated redirect
let returnUrl = new URL(req.url).searchParams.get("return");
return Response.redirect(returnUrl);

// Good: Validate redirect URL
let returnUrl = new URL(req.url).searchParams.get("return");
let allowed = ["/dashboard", "/profile", "/settings"];
if (!allowed.includes(returnUrl)) {
  return Response.redirect("/");
}

Configuration & Headers (HIGH)
insecure-design - @rules/insecure-design.md

Check for security anti-patterns in architecture.

// Bad: Security by obscurity
let isAdmin = req.headers.get("x-admin-secret") === "admin123";

// Good: Proper role-based access control
let session = await getSession(req);
let isAdmin = await db.user
  .findUnique({
    where: { id: session.userId },
  })
  .then((u) => u.role === "ADMIN");

security-misconfiguration - @rules/security-misconfiguration.md

Check for default configs, debug mode, error handling.

// Bad: Exposing stack traces
catch (error) {
  return new Response(error.stack, { status: 500 });
}

// Good: Generic error message
catch (error) {
  console.error(error); // Log server-side only
  return new Response("Internal server error", { status: 500 });
}

security-headers - @rules/security-headers.md

Check for CSP, HSTS, X-Frame-Options, etc.

// Bad: No security headers
return new Response(html);

// Good: Security headers set
return new Response(html, {
  headers: {
    "Content-Security-Policy": "default-src 'self'",
    "X-Frame-Options": "DENY",
    "X-Content-Type-Options": "nosniff",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
  },
});

cors-configuration - @rules/cors-configuration.md

Check for overly permissive CORS.

// Bad: Wildcard with credentials
headers.set("Access-Control-Allow-Origin", "*");
headers.set("Access-Control-Allow-Credentials", "true");

// Good: Specific origin
let allowedOrigins = ["https://app.example.com"];
let origin = req.headers.get("origin");
if (origin && allowedOrigins.includes(origin)) {
  headers.set("Access-Control-Allow-Origin", origin);
}

csrf-protection - @rules/csrf-protection.md

Check for CSRF tokens, SameSite cookies.

// Bad: No CSRF protection
let cookies = parseCookies(req.headers.get("cookie"));
let session = await getSession(cookies.sessionId);

// Good: SameSite cookie + token validation
return new Response("OK", {
  headers: {
    "Set-Cookie": "session=abc; SameSite=Strict; Secure; HttpOnly",
  },
});

session-security - @rules/session-security.md

Check for cookie flags, JWT issues, token storage.

// Bad: Insecure cookie
return new Response("OK", {
  headers: { "Set-Cookie": "session=abc123" },
});

// Good: Secure cookie with all flags
return new Response("OK", {
  headers: {
    "Set-Cookie":
      "session=abc123; Secure; HttpOnly; SameSite=Strict; Path=/; Max-Age=3600",
  },
});

API & Monitoring (MEDIUM-HIGH)
api-security - @rules/api-security.md

Check for REST API vulnerabilities, mass assignment.

// Bad: Mass assignment vulnerability
let userData = await req.json();
await db.user.update({ where: { id }, data: userData });

// Good: Explicitly allow fields
let { displayName, bio } = await req.json();
await db.user.update({
  where: { id },
  data: { displayName, bio }, // Only allowed fields
});

rate-limiting - @rules/rate-limiting.md

Check for missing rate limits, brute force prevention.

// Bad: No rate limiting
async function login(req: Request): Promise<Response> {
  let { email, password } = await req.json();
  // Allows unlimited login attempts
}

// Good: Rate limiting
let ip = req.headers.get("x-forwarded-for");
let { success } = await ratelimit.limit(ip);
if (!success) {
  return new Response("Too many requests", { status: 429 });
}

logging-monitoring - @rules/logging-monitoring.md

Check for insufficient logging, sensitive data in logs.

// Bad: Logging sensitive data
console.log("User login:", { email, password, ssn });

// Good: Log events without sensitive data
console.log("User login attempt", {
  email,
  ip: req.headers.get("x-forwarded-for"),
  timestamp: new Date().toISOString(),
});

vulnerable-dependencies - @rules/vulnerable-dependencies.md

Check for outdated packages, known CVEs.

# Bad: No dependency checking
npm install

# Good: Regular audits
npm audit
npm audit fix

Common Vulnerability Patterns

Quick reference of patterns to look for:

User input without validation: req.json() → immediate use
Missing auth checks: Routes without authorization middleware
Hardcoded secrets: Strings containing "password", "secret", "key"
SQL injection: String concatenation in queries
XSS: dangerouslySetInnerHTML, .innerHTML
Weak crypto: md5, sha1 for passwords
Missing headers: No CSP, HSTS, or security headers
CORS wildcards: Access-Control-Allow-Origin: * with credentials
Insecure cookies: Missing Secure, HttpOnly, SameSite flags
Path traversal: User input in file paths without validation
Severity Quick Reference

Fix Immediately (CRITICAL):

SQL/XSS/Command Injection
Missing authentication on sensitive endpoints
Hardcoded secrets in code
Plaintext password storage
IDOR vulnerabilities

Fix Soon (HIGH):

Missing CSRF protection
Weak password requirements
Missing security headers
Overly permissive CORS
Insecure session management

Fix When Possible (MEDIUM):

Missing rate limiting
Incomplete logging
Outdated dependencies (no known exploits)
Missing input validation on non-critical fields

Improve (LOW):

Missing optional security headers
Verbose error messages (non-production)
Suboptimal crypto parameters
Weekly Installs
757
Repository
sergiodxa/agent-skills
GitHub Stars
83
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass