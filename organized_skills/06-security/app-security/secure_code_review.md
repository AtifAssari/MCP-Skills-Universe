---
rating: ⭐⭐
title: secure-code-review
url: https://skills.sh/hack23/homepage/secure-code-review
---

# secure-code-review

skills/hack23/homepage/secure-code-review
secure-code-review
Installation
$ npx skills add https://github.com/hack23/homepage --skill secure-code-review
SKILL.md
Secure Code Review Skill
Purpose

Establish security-focused code review practices across all Hack23 projects, ensuring security vulnerabilities, insecure patterns, and compliance violations are identified and remediated before code reaches production.

Rules
Review Requirements

MUST:

Review all code changes for security implications before merging
Use automated security scanning (CodeQL, Dependabot) as first line of defense
Check for OWASP Top 10 vulnerabilities in every review
Verify proper input validation and output encoding
Confirm no secrets, credentials, or keys in code or configuration
Validate proper error handling (no information leakage)
Check authorization controls on new endpoints or resources
Verify proper use of cryptographic functions
Review dependency additions for known vulnerabilities

MUST NOT:

Approve code with known Critical/High vulnerabilities
Skip security review for "minor" changes (attackers exploit small changes)
Approve code that disables security controls without documented justification
Allow self-approval on security-sensitive changes
Security Review Checklist

For every pull request, verify:

Authentication & Authorization:

 Authentication enforced for non-public resources
 Authorization checked at each access point
 Principle of least privilege applied

Input/Output:

 All input validated (allowlist approach)
 Output properly encoded for context
 No raw user input reflected without sanitization

Data Protection:

 Sensitive data encrypted at rest and in transit
 No secrets in source code or configuration files
 Data classification appropriate for handling

Error Handling:

 No stack traces exposed to users
 Errors logged securely (no sensitive data in logs)
 Graceful failure without security bypass

Dependencies:

 New dependencies checked for vulnerabilities
 Dependency versions pinned to specific versions
 No unnecessary dependencies added
Automated Scanning Integration

MUST configure on all repositories:

GitHub CodeQL analysis on push and PR
Dependabot alerts enabled
Secret scanning enabled
Branch protection requiring status checks to pass
Hack23 ISMS Policy References
Secure Development Policy
Information Security Policy
Change Management
Compliance Mapping
ISO 27001:2022: A.8.25 (Secure Development Lifecycle), A.8.4 (Access to Source Code)
NIST CSF 2.0: PR.DS (Data Security), PR.IP (Information Protection)
CIS Controls v8.1: Control 16 (Application Software Security)
Weekly Installs
25
Repository
hack23/homepage
GitHub Stars
6
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass