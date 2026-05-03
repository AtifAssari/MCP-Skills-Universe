---
title: security-audit
url: https://skills.sh/srstomp/pokayokay/security-audit
---

# security-audit

skills/srstomp/pokayokay/security-audit
security-audit
Installation
$ npx skills add https://github.com/srstomp/pokayokay --skill security-audit
SKILL.md
Security Audit

Systematic security review for application code, dependencies, and configuration.

Not a replacement for professional penetration testing. Identifies common vulnerabilities within scope of code review.

Audit Types
Type	Focus	When to Use
Code Review	OWASP Top 10, injection, auth	New features, PRs, suspicious code
Dependency	CVEs, outdated packages	Before deploy, periodic, CI/CD
Configuration	Secrets, permissions, hardening	Infrastructure changes, new envs
Architecture	Attack surface, data flow	Design phase, major refactors
API Security	Auth, authz, rate limiting	New endpoints, public APIs
When NOT to Use
Designing new auth flows — Use api-design for designing OAuth2/JWT endpoints from scratch
Performance issues — Use performance-optimization even if caused by auth overhead
CI/CD pipeline security — Use ci-cd for pipeline hardening (secret management, permissions)
Key Principles
Scope first — Define audit area, depth, and constraints before scanning
Classify severity — Critical (24-48h), High (1 week), Medium (2-4 weeks), Low (backlog)
Remediate or track — Fix critical issues immediately, create ohno tasks for the rest
No secrets in code — Scan for hardcoded credentials, API keys, connection strings
Quick Start Checklist
Define audit scope and type (code, dependency, config, architecture, API)
Run automated scans (npm audit, grep patterns, secret detection)
Review findings and classify severity using decision tree in references
Remediate critical/high findings immediately
Create ohno tasks for medium/low findings with appropriate priority
Document findings in audit report
References
Reference	Description
owasp-top-10.md	OWASP vulnerabilities with detection and fixes
dependency-security.md	npm audit, pip-audit, Snyk, CI/CD integration
auth-patterns.md	Secure authentication and authorization patterns
api-security.md	API-specific security concerns
secrets-management.md	Handling sensitive configuration
Weekly Installs
44
Repository
srstomp/pokayokay
GitHub Stars
6
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn