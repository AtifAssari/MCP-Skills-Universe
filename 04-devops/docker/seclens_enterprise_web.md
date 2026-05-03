---
title: seclens-enterprise-web
url: https://skills.sh/jd-opensource/joysafeter/seclens-enterprise-web
---

# seclens-enterprise-web

skills/jd-opensource/joysafeter/seclens-enterprise-web
seclens-enterprise-web
Installation
$ npx skills add https://github.com/jd-opensource/joysafeter --skill seclens-enterprise-web
SKILL.md
Pentest Enterprise Web
Purpose

Perform comprehensive vulnerability assessments on web applications and APIs (REST/GraphQL) to identify security flaws, logic errors, and compliance issues.

Prerequisites
Authorization Requirements
Written authorization (scope document signed by asset owner)
Target environment classification: Internal / External / Hybrid
Rules of Engagement: Testing hours, notification procedures, emergency contacts
Evasion Profile Selection
Profile	Use Case	Characteristics
Quiet	Production systems, WAF-protected targets	Low request rate, header rotation, timing jitter
Standard	Staging environments, time-limited tests	Balanced speed/stealth
Aggressive	Internal networks, comprehensive coverage	Maximum parallelism, full payloads
Environment Setup
Docker container with network_mode: host for complete network access
Volume mount for persistent reports: ./reports:/data
Minimum 4GB RAM allocated
Core Workflow
Scope & Recon: Identify target scope, technologies, and entry points using httpx and whatweb.
Content Discovery: Enumerate endpoints, hidden directories, and API routes using dirsearch, ffuf, and katana.
Vulnerability Scanning: Automated scanning for common flaws (XSS, SQLi, CVEs) using nuclei and nikto.
Authentication Testing: Test login flows, JWT handling, session management, MFA bypass vectors.
Business Logic Testing: Manual testing for price manipulation, race conditions, IDOR, workflow bypass.
Dependency Scanning: Analyze third-party components for known CVEs using pip-audit, trivy.
Manual Verification: Verify automated findings and test complex business logic using burpsuite or zap.
Exploitation (Safe): Demonstrate impact of critical findings (e.g., SQLi, RCE) using sqlmap or custom scripts.
Reporting: Aggregate findings into structured report using references/report-template.md.
OWASP Top 10 (2021) Coverage
Category	Workflow	Primary Tools	Status
A01 Broken Access Control	business_logic_testing	browser_agent, http_repeater, IDOR enumeration	✅
A02 Cryptographic Failures	vulnerability_assessment	nuclei (crypto tags), manual TLS review	✅
A03 Injection	vulnerability_assessment	sqlmap, dalfox, nuclei (injection templates)	✅
A04 Insecure Design	business_logic_testing	manual testing, race condition scripts	✅
A05 Security Misconfiguration	web_reconnaissance	nuclei (misconfig tags), nikto, httpx	✅
A06 Vulnerable Components	dependency_scanning	pip-audit, npm-audit, trivy	✅
A07 Auth Failures	authentication_testing	jwt_analyzer, http_intruder, browser_agent	✅
A08 Software/Data Integrity	dependency_scanning	trivy (image scan), gitleaks	✅
A09 Logging Failures	vulnerability_assessment	manual review, log injection testing	⚠️ Partial
A10 SSRF	vulnerability_assessment	nuclei (ssrf tags), interactsh (OOB)	✅
Tool Categories
Category	Tools	Purpose
Reconnaissance	httpx, katana, gau, waybackurls	Asset discovery, technology fingerprinting
Content Discovery	dirsearch, ffuf, gobuster, feroxbuster	Hidden endpoints, directories
Vulnerability Scanning	nuclei, nikto, jaeles	Automated CVE/misconfiguration detection
Injection Testing	sqlmap, dalfox, xsser	SQL, XSS, command injection
API Security	arjun, graphql_scanner, jwt_analyzer	API-specific vulnerabilities
Auth Testing	http_intruder, browser_agent	Credential stuffing, session attacks
Dependency Scanning	pip-audit, npm-audit, trivy	Third-party component CVEs
OOB Detection	interactsh	Blind SSRF, RCE, XXE verification
Interactive	burpsuite, zaproxy, browser_agent	Manual testing, complex flows
Reporting	pandoc, wkhtmltopdf	PDF/HTML report generation
References
references/tools.md - Tool function signatures and parameters
references/workflows.md - Attack pattern definitions
references/report-template.md - Vulnerability report template
Weekly Installs
25
Repository
jd-opensource/joysafeter
GitHub Stars
267
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn