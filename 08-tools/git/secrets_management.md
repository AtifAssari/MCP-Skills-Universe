---
title: secrets-management
url: https://skills.sh/hack23/homepage/secrets-management
---

# secrets-management

skills/hack23/homepage/secrets-management
secrets-management
Installation
$ npx skills add https://github.com/hack23/homepage --skill secrets-management
SKILL.md
Secrets Management Skill
Purpose

Ensure secure handling of sensitive credentials, API keys, tokens, and cryptographic keys throughout development and deployment lifecycle across all Hack23 projects. Enforces zero-tolerance for hardcoded secrets.

Rules
Golden Rules

MUST:

Use environment variables or secrets managers for all credentials
Use GitHub Actions secrets for CI/CD credentials
Include .env, *.key, *.pem, *.p12 in .gitignore
Rotate secrets on a defined schedule (quarterly minimum)
Use pre-commit hooks to detect secrets before they reach the repository
Log all secret access and rotation events
Immediately rotate any secret suspected of compromise

MUST NOT:

Hard-code secrets, credentials, API keys, or tokens in source code
Commit .env files, private keys, or certificates to git
Store secrets in comments, documentation, or issue descriptions
Share secrets via email, chat, or unencrypted channels
Use the same secret across multiple environments
Use default or well-known credentials in any environment
Secret Types and Storage
Secret Type	Recommended Storage	Rotation
API Keys	GitHub Secrets / AWS Secrets Manager	Quarterly
Database Credentials	AWS Secrets Manager / Vault	Quarterly
JWT Signing Keys	AWS Secrets Manager	Annually
TLS Certificates	AWS Certificate Manager	Auto-renewed
Encryption Keys	AWS KMS	Annually
Service Tokens	GitHub Secrets	Quarterly
Detection and Prevention

Pre-commit scanning:

Use git-secrets, gitleaks, or trufflehog for automated detection
GitHub Secret Scanning alerts must be enabled on all repositories
Block push if secrets are detected

CI/CD scanning:

Enable GitHub Advanced Security secret scanning
Run gitleaks in CI pipeline
Fail builds on secret detection
Incident Response for Exposed Secrets
Immediately rotate the compromised secret
Revoke old secret from all systems
Review access logs for unauthorized use
Notify security team
Document incident per Incident Response Plan
Hack23 ISMS Policy References
Cryptography Policy
Access Control Policy
Secure Development Policy
Incident Response Plan
Compliance Mapping
ISO 27001:2022: A.8.4 (Access to Source Code), A.8.24 (Cryptography)
NIST CSF 2.0: PR.AC-1 (Credentials), PR.DS-5 (Data Leak Protection)
CIS Controls v8.1: Control 3.11 (Encrypt Sensitive Data), Control 4.7 (Manage Credentials)
Weekly Installs
21
Repository
hack23/homepage
GitHub Stars
6
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass