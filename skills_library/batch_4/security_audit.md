---
title: security-audit
url: https://skills.sh/sickn33/antigravity-awesome-skills/security-audit
---

# security-audit

skills/sickn33/antigravity-awesome-skills/security-audit
security-audit
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill security-audit
SKILL.md
Security Auditing Workflow Bundle
Overview

Comprehensive security auditing workflow for web applications, APIs, and infrastructure. This bundle orchestrates skills for penetration testing, vulnerability assessment, security scanning, and remediation.

When to Use This Workflow

Use this workflow when:

Performing security audits on web applications
Testing API security
Conducting penetration tests
Scanning for vulnerabilities
Hardening application security
Compliance security assessments
Workflow Phases
Phase 1: Reconnaissance
Skills to Invoke
scanning-tools - Security scanning
shodan-reconnaissance - Shodan searches
top-web-vulnerabilities - OWASP Top 10
Actions
Identify target scope
Gather intelligence
Map attack surface
Identify technologies
Document findings
Copy-Paste Prompts
Use @scanning-tools to perform initial reconnaissance

Use @shodan-reconnaissance to find exposed services

Phase 2: Vulnerability Scanning
Skills to Invoke
vulnerability-scanner - Vulnerability analysis
security-scanning-security-sast - Static analysis
security-scanning-security-dependencies - Dependency scanning
Actions
Run automated scanners
Perform static analysis
Scan dependencies
Identify misconfigurations
Document vulnerabilities
Copy-Paste Prompts
Use @vulnerability-scanner to scan for OWASP Top 10 vulnerabilities

Use @security-scanning-security-dependencies to audit dependencies

Phase 3: Web Application Testing
Skills to Invoke
top-web-vulnerabilities - OWASP vulnerabilities
sql-injection-testing - SQL injection
xss-html-injection - XSS testing
broken-authentication - Authentication testing
idor-testing - IDOR testing
file-path-traversal - Path traversal
burp-suite-testing - Burp Suite testing
Actions
Test for injection flaws
Test authentication mechanisms
Test session management
Test access controls
Test input validation
Test security headers
Copy-Paste Prompts
Use @sql-injection-testing to test for SQL injection vulnerabilities

Use @xss-html-injection to test for cross-site scripting

Use @broken-authentication to test authentication security

Phase 4: API Security Testing
Skills to Invoke
api-fuzzing-bug-bounty - API fuzzing
api-security-best-practices - API security
Actions
Enumerate API endpoints
Test authentication/authorization
Test rate limiting
Test input validation
Test error handling
Document API vulnerabilities
Copy-Paste Prompts
Use @api-fuzzing-bug-bounty to fuzz API endpoints

Phase 5: Penetration Testing
Skills to Invoke
pentest-commands - Penetration testing commands
pentest-checklist - Pentest planning
ethical-hacking-methodology - Ethical hacking
metasploit-framework - Metasploit
Actions
Plan penetration test
Execute attack scenarios
Exploit vulnerabilities
Document proof of concept
Assess impact
Copy-Paste Prompts
Use @pentest-checklist to plan penetration test

Use @pentest-commands to execute penetration testing

Phase 6: Security Hardening
Skills to Invoke
security-scanning-security-hardening - Security hardening
auth-implementation-patterns - Authentication
api-security-best-practices - API security
Actions
Implement security controls
Configure security headers
Set up authentication
Implement authorization
Configure logging
Apply patches
Copy-Paste Prompts
Use @security-scanning-security-hardening to harden application security

Phase 7: Reporting
Skills to Invoke
reporting-standards - Security reporting
Actions
Document findings
Assess risk levels
Provide remediation steps
Create executive summary
Generate technical report
Security Testing Checklist
OWASP Top 10
 Injection (SQL, NoSQL, OS, LDAP)
 Broken Authentication
 Sensitive Data Exposure
 XML External Entities (XXE)
 Broken Access Control
 Security Misconfiguration
 Cross-Site Scripting (XSS)
 Insecure Deserialization
 Using Components with Known Vulnerabilities
 Insufficient Logging & Monitoring
API Security
 Authentication mechanisms
 Authorization checks
 Rate limiting
 Input validation
 Error handling
 Security headers
Quality Gates
 All planned tests executed
 Vulnerabilities documented
 Proof of concepts captured
 Risk assessments completed
 Remediation steps provided
 Report generated
Related Workflow Bundles
development - Secure development practices
wordpress - WordPress security
cloud-devops - Cloud security
testing-qa - Security testing
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
454
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass