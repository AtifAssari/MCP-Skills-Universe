---
rating: ⭐⭐
title: security-engineering
url: https://skills.sh/89jobrien/steve/security-engineering
---

# security-engineering

skills/89jobrien/steve/security-engineering
security-engineering
Installation
$ npx skills add https://github.com/89jobrien/steve --skill security-engineering
SKILL.md
Security Engineering

Comprehensive security engineering skill covering application security, infrastructure security, compliance, and incident response.

When to Use This Skill
Designing security architecture
Implementing authentication and authorization
Conducting threat modeling
Security code review
Implementing compliance controls (SOC2, HIPAA, PCI-DSS)
Incident response planning
Security monitoring and alerting
Security Architecture
Defense in Depth

Layer security controls at multiple levels:

Layer	Controls
Perimeter	Firewall, WAF, DDoS protection
Network	Segmentation, IDS/IPS, VPN
Host	Hardening, EDR, patch management
Application	Input validation, secure coding, SAST/DAST
Data	Encryption, access control, DLP
Identity	MFA, SSO, privileged access management
Zero Trust Architecture

Core Principles:

Never trust, always verify
Assume breach mentality
Least privilege access
Micro-segmentation
Continuous verification

Implementation:

Identity-based access (not network-based)
Device health verification
Continuous authentication
Encrypted communications everywhere
Detailed logging and monitoring
Authentication Patterns
OAuth 2.0 / OIDC

Grant Types:

Grant	Use Case
Authorization Code + PKCE	Web/mobile apps
Client Credentials	Service-to-service
Device Code	CLI tools, IoT

Token Best Practices:

Short-lived access tokens (15 min - 1 hour)
Secure refresh token storage
Token rotation on use
Revocation capabilities
Session Management
Secure, HttpOnly, SameSite cookies
Session timeout (idle and absolute)
Session invalidation on logout
Concurrent session limits
Session binding to device/IP
Multi-Factor Authentication
TOTP (authenticator apps)
WebAuthn/FIDO2 (hardware keys)
Push notifications
SMS (last resort, vulnerable to SIM swap)
Authorization Patterns
RBAC (Role-Based Access Control)
Users → Roles → Permissions


Best for: Well-defined organizational hierarchies

ABAC (Attribute-Based Access Control)
If user.department == "engineering" AND
   resource.classification == "internal" AND
   time.hour BETWEEN 9 AND 17
THEN allow


Best for: Complex, dynamic access requirements

Policy as Code

Use OPA/Rego or Cedar for externalized policy:

Version controlled policies
Testable access rules
Audit trail
Separation of concerns
Secure Development
OWASP Top 10 Mitigations
Risk	Mitigation
Injection	Parameterized queries, input validation
Broken Auth	Strong password policy, MFA, rate limiting
Sensitive Data	Encryption, minimal data collection
XXE	Disable external entities
Broken Access	Authorization checks, default deny
Misconfig	Secure defaults, hardening guides
XSS	Output encoding, CSP
Deserialization	Integrity checks, avoid untrusted data
Components	Dependency scanning, updates
Logging	Centralized logging, alerting
Security Testing

SAST (Static Analysis):

Run on every commit
Block high-severity findings
Tools: Semgrep, CodeQL, SonarQube

DAST (Dynamic Analysis):

Run against staging/dev
Tools: OWASP ZAP, Burp Suite

Dependency Scanning:

Check for known vulnerabilities
Tools: Snyk, Dependabot, npm audit
Secrets Management

Never:

Commit secrets to git
Log secrets
Pass secrets in URLs
Hardcode secrets

Do:

Use secret managers (Vault, AWS Secrets Manager)
Rotate secrets regularly
Audit secret access
Use short-lived credentials
Compliance Frameworks
Common Requirements
Framework	Focus Area
SOC 2	Trust services (security, availability, etc.)
HIPAA	Healthcare data protection
PCI-DSS	Payment card data
GDPR	EU personal data protection
ISO 27001	Information security management
Key Controls
Access control and authentication
Encryption (at rest and in transit)
Logging and monitoring
Incident response procedures
Business continuity planning
Vendor management
Employee security training
Incident Response
Response Phases
Preparation: Runbooks, tools, training
Detection: Monitoring, alerting, triage
Containment: Isolate, preserve evidence
Eradication: Remove threat, patch vulnerabilities
Recovery: Restore services, verify clean
Lessons Learned: Post-mortem, improvements
Severity Levels
Level	Description	Response Time
P1	Active breach, data exfiltration	Immediate
P2	Vulnerability being exploited	< 4 hours
P3	High-risk vulnerability discovered	< 24 hours
P4	Security improvement needed	Next sprint
Reference Files
references/threat_modeling.md - STRIDE methodology and examples
references/compliance_controls.md - Framework-specific control mappings
Integration with Other Skills
cloud-infrastructure - For cloud security
debugging - For security incident investigation
testing - For security testing patterns
Weekly Installs
28
Repository
89jobrien/steve
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass