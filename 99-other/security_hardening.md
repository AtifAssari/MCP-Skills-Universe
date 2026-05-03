---
rating: ⭐⭐⭐
title: security-hardening
url: https://skills.sh/1mangesh1/dev-skills-collection/security-hardening
---

# security-hardening

skills/1mangesh1/dev-skills-collection/security-hardening
security-hardening
Installation
$ npx skills add https://github.com/1mangesh1/dev-skills-collection --skill security-hardening
SKILL.md
Security Hardening and Secure Coding
OWASP Top 10 (2021) -- Overview and Practical Mitigations
A01: Broken Access Control
Deny by default. Enforce server-side authorization on every request.
Use RBAC or ABAC. Disable directory listing. Log repeated access-control failures.
A02: Cryptographic Failures
Encrypt PII at rest (AES-256-GCM) and in transit (TLS 1.2+).
Hash passwords with bcrypt, scrypt, or Argon2id. Rotate encryption keys on schedule.
A03: Injection
Use parameterized queries or prepared statements for all database access.
Validate and sanitize every input server-side. Use ORMs with parameterized bindings.
A04: Insecure Design
Threat model (STRIDE, DREAD) during design. Apply least privilege, defense in depth, fail-safe defaults.
A05: Security Misconfiguration
Remove default credentials and debug endpoints in production. Automate configuration audits.
A06: Vulnerable and Outdated Components
Maintain an SBOM. Run dependency scanning in CI. Subscribe to security advisories.
A07: Identification and Authentication Failures
Enforce strong passwords (12+ characters, check breached-password lists). Require MFA for privileged accounts.
Regenerate session IDs after login. Set short idle timeouts.
A08: Software and Data Integrity Failures
Verify dependency integrity via lockfiles and checksums. Sign commits and releases.
A09: Security Logging and Monitoring Failures
Log auth attempts, authorization failures, and privilege changes. Centralize logs. Never log secrets or PII.
A10: Server-Side Request Forgery (SSRF)
Allowlist URLs before server-side requests. Block private IP ranges. Use network-level controls.
Input Validation

Always validate on the server side. Client-side validation is a convenience for users, not a security control.

Principles
Prefer allowlists over denylists. Define what is permitted, reject everything else.
Validate type, length, range, and format for every input field.
Reject unexpected input early, before it reaches business logic or data stores.
Canonicalize inputs before validation (decode URL encoding, normalize Unicode).
Example: Server-Side Validation
// Allowlist approach: only permit expected characters
function validateUsername(input) {
  const ALLOWED = /^[a-zA-Z0-9_]{3,30}$/;
  if (!ALLOWED.test(input)) {
    throw new Error('Invalid username format');
  }
  return input;
}

// Numeric validation with range checking
function validateAge(input) {
  const age = Number(input);
  if (!Number.isInteger(age) || age < 0 || age > 150) {
    throw new Error('Invalid age');
  }
  return age;
}

SQL Injection Prevention
Parameterized Queries
// VULNERABLE: string concatenation
const result = db.query(`SELECT * FROM users WHERE id = ${req.params.id}`);

// SAFE: parameterized query
const result = db.query('SELECT * FROM users WHERE id = $1', [req.params.id]);

# VULNERABLE
cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")

# SAFE: parameterized
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))

ORM Usage
ORMs generate parameterized queries by default. Use query builders instead of raw SQL.
When raw SQL is required, still use parameterized bindings. Audit ORM queries in development.
XSS Prevention
Output Encoding
Encode all dynamic content before inserting into HTML, JavaScript, CSS, or URL contexts.
Use context-aware encoding: HTML entity encoding for HTML body, JavaScript escaping for script contexts, URL encoding for URL parameters.
// HTML context: encode before insertion
function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;');
}

Content Security Policy (CSP)
Deploy CSP headers to restrict sources of scripts, styles, images, and other resources.
Avoid unsafe-inline and unsafe-eval. Use nonces or hashes for inline scripts when necessary.
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-{random}'; style-src 'self'; img-src 'self' data:; object-src 'none'; base-uri 'self'; frame-ancestors 'none'

Sanitization
For user-supplied HTML (rich text editors), use a proven library (DOMPurify, bleach). Never write custom sanitizers.
Strip javascript: URIs, event handler attributes, and dangerous elements (<script>, <iframe>, <object>).
CSRF Protection
Token-Based Protection
Generate a unique, unpredictable CSRF token per session. Include in a hidden form field or custom header.
Validate server-side on every state-changing request. Regenerate tokens on login.
SameSite Cookies
Set SameSite=Lax as a minimum on all session cookies. Use SameSite=Strict where cross-site navigation is not needed.
Combine SameSite with CSRF tokens for defense in depth. SameSite alone does not cover all browsers or scenarios.
Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Lax; Path=/

Security Headers

Apply these headers to every HTTP response in production.

Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self'; frame-ancestors 'none'
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()

Header	Purpose
Content-Security-Policy	Controls which resources the browser may load. Primary defense against XSS.
Strict-Transport-Security	Forces HTTPS for all future requests. Prevents protocol downgrade attacks.
X-Frame-Options	Prevents clickjacking by blocking framing of the page.
X-Content-Type-Options	Stops browsers from MIME-sniffing responses away from the declared content type.
Referrer-Policy	Controls how much referrer information is sent with requests.
Permissions-Policy	Restricts which browser features (camera, mic, geolocation) the page may use.
CORS Configuration
Default to the most restrictive policy: do not set CORS headers unless cross-origin access is required.
Never use Access-Control-Allow-Origin: * with Access-Control-Allow-Credentials: true. Browsers reject this, but the intent reveals a misunderstanding.
Allowlist specific origins. Validate the Origin header against the allowlist on every request.
Restrict Access-Control-Allow-Methods and Access-Control-Allow-Headers to only what is needed.
// Express example: explicit origin allowlist
const allowedOrigins = ['https://app.example.com', 'https://admin.example.com'];

app.use((req, res, next) => {
  const origin = req.headers.origin;
  if (allowedOrigins.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
    res.setHeader('Access-Control-Allow-Credentials', 'true');
  }
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});

Rate Limiting and Brute Force Protection
Apply rate limiting to authentication endpoints, password reset, and API routes.
Use sliding window or token bucket algorithms. Return 429 Too Many Requests with Retry-After.
Implement account lockout after repeated failures (e.g., 5 failures in 10 minutes, 15-minute lockout).
Rate limit by IP, by account, and by API key independently. Consider CAPTCHA after threshold failures.
File Upload Security
Validation
Validate file type by inspecting magic bytes, not just extension or client-provided MIME type.
Enforce maximum file size at web server and application level. Allowlist permitted extensions.
Storage
Store uploads outside the web root. Rename to random UUIDs; never use the original filename.
Scan uploads for malware (ClamAV or equivalent).
Serving
Set Content-Disposition: attachment for downloads. Serve uploads from a separate domain.
Set X-Content-Type-Options: nosniff to prevent MIME-type sniffing.
Environment Variable Security
.env Files
Never commit .env files. Add .env to .gitignore before the first commit.
Provide .env.example with placeholder values. Restrict file permissions in production (chmod 600).
Secrets Management
Use a dedicated secrets manager (Vault, AWS Secrets Manager, GCP Secret Manager) in production.
Rotate secrets on schedule and after any suspected compromise. Never log secrets.
Prefer short-lived, scoped credentials (IAM roles, OIDC tokens) over static API keys.
Pre-Commit Checks
Use git-secrets, TruffleHog, or gitleaks in pre-commit hooks.
Scan full repo history periodically; removed secrets persist in git history.
Dependency Security
Run npm audit, pip audit, or equivalent on every CI build. Fail on high/critical vulnerabilities.
Enable Dependabot or Renovate for automated dependency update PRs.
Use Snyk or Socket for transitive dependency and supply chain analysis.
Commit lockfiles (package-lock.json, yarn.lock, poetry.lock) and review changes to them.
Pin dependency versions in production. Audit new dependencies before adding them.
Docker Security
Image Construction
Use minimal base images (alpine, distroless, scratch) to reduce attack surface.
Run processes as a non-root user. Add a USER instruction in the Dockerfile.
Use multi-stage builds to exclude build tools and source code from the final image.
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY . .
RUN npm run build

FROM node:20-alpine
RUN addgroup -S app && adduser -S app -G app
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
USER app
EXPOSE 3000
CMD ["node", "dist/server.js"]

Secrets and Scanning
Never embed secrets in images (ENV, ARG, or COPY). They persist in image layers.
Pass secrets at runtime via mounted volumes or orchestrator secrets (Kubernetes Secrets, Docker Swarm).
Scan images with Trivy, Grype, or Snyk Container.
HTTPS Everywhere
Enforce TLS 1.2 minimum; prefer TLS 1.3. Redirect all HTTP to HTTPS with 301.
Deploy HSTS with max-age=63072000; includeSubDomains; preload. Submit to hstspreload.org.
Use strong cipher suites. Disable CBC-mode ciphers and anything below 128-bit.
Automate certificate renewal (Let's Encrypt/certbot). Test with SSL Labs for an A+ rating.
Logging Security Events
What to Log
Authentication successes and failures (username, IP, timestamp; never passwords).
Authorization failures, input validation failures, privilege escalation events, and admin actions.
How to Log Safely
Use structured logging (JSON). Never log secrets, tokens, passwords, or PII.
Send logs to a centralized system (ELK, Splunk, CloudWatch, Datadog). Set retention policies.
Alert on anomalous patterns: spikes in failed logins, unusual data access volumes.
Server Hardening
SSH Configuration
Disable password authentication; use SSH key pairs only. Disable root login (PermitRootLogin no).
Use AllowUsers or AllowGroups to restrict SSH access. Enable fail2ban to block brute force attempts.
Firewall Basics
Default-deny inbound traffic. Open only required ports (22, 80, 443).
Restrict management ports to specific IP ranges or VPN. Log denied connections.
General Hardening
Disable unused services and uninstall unnecessary packages. Automate OS patching.
Enable SELinux or AppArmor. Set filesystem permissions following least privilege.
Secrets Management
HashiCorp Vault
Access secrets via the Vault API. Authenticate using AppRole, Kubernetes auth, or cloud IAM.
Use dynamic secrets (short-lived database credentials on demand). Enable audit logging.
AWS Secrets Manager / GCP Secret Manager / Azure Key Vault
Store secrets in the cloud provider's manager. Use IAM policies to restrict access. Enable auto-rotation.
Environment-Based Secrets (When No Secrets Manager Is Available)
Inject secrets as environment variables at deploy time via CI/CD or orchestrator.
Never bake secrets into images, version-controlled config, or client-side code.
Rotate immediately after team member departure or suspected leak.
Security Checklist
 All inputs validated server-side with allowlist approach
 Parameterized queries used for all database access
 Output encoding applied in all rendering contexts
 CSP header deployed and tested
 CSRF tokens on all state-changing requests
 Security headers (HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy) configured
 CORS restricted to specific required origins
 Rate limiting on authentication and sensitive endpoints
 File uploads validated, stored outside web root, and served safely
 No secrets in version control; .env in .gitignore
 Dependency vulnerabilities scanned in CI
 Docker images run as non-root with minimal base
 TLS 1.2+ enforced; HSTS deployed with preload
 Security events logged without sensitive data leakage
 SSH hardened; firewall default-deny configured
 Secrets managed through a dedicated secrets manager or injected at deploy time
Tools
npm audit / pip audit / bundler-audit -- dependency vulnerability scanning
Snyk / Socket -- supply chain and transitive dependency analysis
Dependabot / Renovate -- automated dependency update PRs
TruffleHog / gitleaks / git-secrets -- secret scanning in repositories
Trivy / Grype -- container image vulnerability scanning
OWASP ZAP / Burp Suite -- dynamic application security testing
SonarQube -- static analysis for code quality and security
ClamAV -- malware scanning for file uploads
fail2ban -- brute force protection for SSH and other services
SSL Labs (ssllabs.com/ssltest) -- TLS configuration testing
HashiCorp Vault / AWS Secrets Manager -- secrets management
References
OWASP Top 10: https://owasp.org/www-project-top-ten/
OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
CWE/SANS Top 25: https://cwe.mitre.org/top25/
NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
Mozilla Web Security Guidelines: https://infosec.mozilla.org/guidelines/web_security
HSTS Preload List Submission: https://hstspreload.org/
Weekly Installs
9
Repository
1mangesh1/dev-s…llection
GitHub Stars
3
First Seen
Feb 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass