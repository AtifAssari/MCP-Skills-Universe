---
title: security-audit
url: https://skills.sh/s-hiraoku/synapse-a2a/security-audit
---

# security-audit

skills/s-hiraoku/synapse-a2a/security-audit
security-audit
Installation
$ npx skills add https://github.com/s-hiraoku/synapse-a2a --skill security-audit
SKILL.md
Security Audit Skill

This skill provides a comprehensive framework for security auditing, ensuring that common vulnerabilities are identified and addressed during development and review.

Audit Checklist
1. OWASP Top 10 & Common Vulnerabilities
Injection: Check for SQL, Command, or NoSQL injection points. Ensure parameterized queries or proper escaping is used.
Broken Access Control: Verify that users cannot access resources outside of their intended permissions.
Insecure Design: Evaluate the overall architecture for security flaws.
Cryptographic Failures: Ensure sensitive data (passwords, PII) is encrypted at rest and in transit using modern algorithms (e.g., AES-256, TLS 1.3).
2. Dependency Management
Vulnerability Scanning: Check for known vulnerabilities in third-party libraries (e.g., using npm audit, pip-audit, or snyk).
Outdated Packages: Identify and update significantly outdated dependencies.
3. Authentication & Authorization
Credential Management: Ensure passwords are never stored in plain text (use Argon2, bcrypt, or scrypt).
Session Management: Verify secure session handling (HttpOnly, Secure, SameSite flags for cookies).
MFA/2FA: Check for the implementation or requirement of multi-factor authentication where appropriate.
4. Input Validation & Data Handling
Sanitization: Validate and sanitize all user-supplied data at the trust boundary.
Encoding: Ensure output encoding is used to prevent Cross-Site Scripting (XSS).
Secret Management: Confirm that API keys, secrets, and credentials are NOT committed to the repository (use environment variables or secret managers).
Usage Guidelines

When asked to "audit" or "perform a security review":

Systematically go through each category above.
For each finding, categorize it by severity (Critical, High, Medium, Low).
Provide clear remediation steps for every identified issue.
Document any positive security practices already in place.
Weekly Installs
136
Repository
s-hiraoku/synapse-a2a
GitHub Stars
4
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass