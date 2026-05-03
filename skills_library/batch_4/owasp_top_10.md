---
title: owasp-top-10
url: https://skills.sh/nickcrew/claude-ctx-plugin/owasp-top-10
---

# owasp-top-10

skills/nickcrew/claude-ctx-plugin/owasp-top-10
owasp-top-10
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill owasp-top-10
Summary

Expert guidance for identifying, preventing, and remediating OWASP Top 10 web application security risks.

Covers all 10 critical vulnerabilities ranked by severity, including broken access control, cryptographic failures, injection, insecure design, and security misconfiguration
Provides detailed reference files for each vulnerability category with vulnerable and secure code patterns, detection methods, and remediation strategies
Includes a structured security audit workflow covering scope identification, code analysis, finding documentation, and verification testing
Outlines core security principles (defense in depth, secure by default, input validation) and documents eight common implementation mistakes
References industry-standard testing tools (SAST, DAST, SCA, secrets scanning) and links to OWASP resources, NIST frameworks, and vulnerability databases
SKILL.md
OWASP Top 10 Security Vulnerabilities

Expert guidance for identifying, preventing, and remediating the most critical web application security risks based on OWASP Top 10 2021.

When to Use This Skill
Conducting security audits and code reviews
Implementing secure coding practices in new features
Reviewing authentication and authorization systems
Assessing input validation and sanitization
Evaluating third-party dependencies for vulnerabilities
Designing security controls and defense-in-depth strategies
Preparing for security certifications or compliance audits
Investigating security incidents or suspicious behavior
OWASP Top 10 2021 Overview

Ranked by Risk Severity:

A01 - Broken Access Control (↑ from #5)
A02 - Cryptographic Failures (formerly Sensitive Data Exposure)
A03 - Injection (↓ from #1)
A04 - Insecure Design (NEW)
A05 - Security Misconfiguration
A06 - Vulnerable and Outdated Components
A07 - Identification and Authentication Failures
A08 - Software and Data Integrity Failures (NEW)
A09 - Security Logging and Monitoring Failures
A10 - Server-Side Request Forgery (SSRF) (NEW)
Quick Reference

Load detailed guidance for each vulnerability:

Vulnerability	Reference File
Broken Access Control	skills/owasp-top-10/references/broken-access-control.md
Cryptographic Failures	skills/owasp-top-10/references/cryptographic-failures.md
Injection	skills/owasp-top-10/references/injection.md
Insecure Design	skills/owasp-top-10/references/insecure-design.md
Security Misconfiguration	skills/owasp-top-10/references/security-misconfiguration.md
Vulnerable Components	skills/owasp-top-10/references/vulnerable-components.md
Authentication Failures	skills/owasp-top-10/references/authentication-failures.md
Integrity Failures	skills/owasp-top-10/references/integrity-failures.md
Logging & Monitoring	skills/owasp-top-10/references/logging-monitoring.md
SSRF	skills/owasp-top-10/references/ssrf.md
Prevention Strategies	skills/owasp-top-10/references/prevention-strategies.md
Assessment Workflow	skills/owasp-top-10/references/assessment-workflow.md
Security Audit Workflow
Identify Scope: Determine application components and attack surface
Select Vulnerabilities: Choose relevant OWASP categories based on features
Load Reference: Read appropriate reference file(s) for detailed patterns
Analyze Code: Review code against vulnerable and secure patterns
Document Findings: Record vulnerabilities with severity and remediation
Verify Fixes: Test that remediations properly address issues
Test Security: Run automated security testing (SAST, DAST, SCA)
Core Security Principles
Defense in Depth
Layer security controls at network, application, data, and monitoring levels
Ensure failure of one control doesn't compromise entire system
Secure by Default
Deny all access by default, explicitly grant permissions
Fail securely (errors don't expose sensitive information)
Minimize attack surface (disable unused features)
Apply least privilege to all accounts and services
Input Validation
Validate type, length, format, and allowed values
Use allow-lists over deny-lists
Sanitize for specific context (SQL, HTML, shell, etc.)
Never trust client input
Common Mistakes
Trusting User Input: Always validate and sanitize all user-supplied data
Rolling Your Own Crypto: Use established libraries (bcrypt, AES-256)
Exposing Errors: Log detailed errors internally, show generic messages to users
Missing Authorization: Check permissions on every request, not just UI
Weak Session Management: Use secure, httpOnly, sameSite cookies with HTTPS
Ignoring Dependencies: Regularly audit and update third-party libraries
No Logging: Log security events for detection and incident response
Default Configurations: Harden all systems, disable defaults
Security Testing Tools

SAST (Static): SonarQube, Semgrep, ESLint security plugins DAST (Dynamic): OWASP ZAP, Burp Suite SCA (Dependencies): npm audit, Snyk, Dependabot Secrets Scanning: GitGuardian, TruffleHog Penetration Testing: Metasploit, Kali Linux tools

Resources
OWASP Top 10 2021: https://owasp.org/Top10/
OWASP Cheat Sheets: https://cheatsheetseries.owasp.org/
OWASP ASVS: Application Security Verification Standard
CWE Top 25: Common Weakness Enumeration
NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
CVE Database: https://cve.mitre.org/
Snyk Vulnerability DB: https://snyk.io/vuln/
Weekly Installs
396
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass