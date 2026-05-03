---
rating: ⭐⭐⭐
title: security-testing
url: https://skills.sh/aj-geddes/useful-ai-prompts/security-testing
---

# security-testing

skills/aj-geddes/useful-ai-prompts/security-testing
security-testing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill security-testing
SKILL.md
Security Testing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Security testing identifies vulnerabilities, weaknesses, and threats in applications to ensure data protection, prevent unauthorized access, and maintain system integrity. It combines automated scanning (SAST, DAST) with manual penetration testing and code review.

When to Use
Testing for OWASP Top 10 vulnerabilities
Scanning dependencies for known vulnerabilities
Testing authentication and authorization
Validating input sanitization
Testing API security
Checking for sensitive data exposure
Validating security headers
Testing session management
Quick Start

Minimal working example:

# security_scan.py
from zapv2 import ZAPv2
import time

class SecurityScanner:
    def __init__(self, target_url, api_key=None):
        self.zap = ZAPv2(apikey=api_key, proxies={
            'http': 'http://localhost:8080',
            'https': 'http://localhost:8080'
        })
        self.target = target_url

    def scan(self):
        """Run full security scan."""
        print(f"Scanning {self.target}...")

        # Spider the application
        print("Spidering...")
        scan_id = self.zap.spider.scan(self.target)
        while int(self.zap.spider.status(scan_id)) < 100:
            time.sleep(2)
            print(f"Spider progress: {self.zap.spider.status(scan_id)}%")

        # Active scan
        print("Running active scan...")
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
OWASP ZAP (DAST)	OWASP ZAP (DAST)
SQL Injection Testing	SQL Injection Testing
XSS Testing	XSS Testing
Authentication & Authorization Testing	Authentication & Authorization Testing
CSRF Protection Testing	CSRF Protection Testing
Dependency Vulnerability Scanning	Dependency Vulnerability Scanning
Security Headers Testing	Security Headers Testing
Secrets Detection	Secrets Detection
Best Practices
✅ DO
Run security scans in CI/CD
Test with real attack vectors
Scan dependencies regularly
Use security headers
Implement rate limiting
Validate and sanitize all input
Use parameterized queries
Test authentication/authorization thoroughly
❌ DON'T
Store secrets in code
Trust user input
Expose detailed error messages
Skip dependency updates
Use default credentials
Ignore security warnings
Test only happy paths
Commit sensitive data
Weekly Installs
387
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass