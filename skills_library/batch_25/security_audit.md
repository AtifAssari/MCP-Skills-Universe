---
title: security-audit
url: https://skills.sh/ruvnet/ruflo/security-audit
---

# security-audit

skills/ruvnet/ruflo/security-audit
security-audit
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill security-audit
SKILL.md
Security Audit Skill
Purpose

Comprehensive security scanning and vulnerability detection. Includes input validation, path traversal prevention, CVE detection, and secure coding pattern enforcement.

When to Trigger
authentication implementation
authorization logic
payment processing
user data handling
API endpoint creation
file upload handling
database queries
external API integration
When to Skip
read-only operations on public data
internal development tooling
static documentation
styling changes
Commands
Full Security Scan

Run comprehensive security analysis on the codebase

npx @claude-flow/cli security scan --depth full


Example:

npx @claude-flow/cli security scan --depth full --output security-report.json

Input Validation Check

Check for input validation issues

npx @claude-flow/cli security scan --check input-validation


Example:

npx @claude-flow/cli security scan --check input-validation --path ./src/api

Path Traversal Check

Check for path traversal vulnerabilities

npx @claude-flow/cli security scan --check path-traversal

SQL Injection Check

Check for SQL injection vulnerabilities

npx @claude-flow/cli security scan --check sql-injection

XSS Check

Check for cross-site scripting vulnerabilities

npx @claude-flow/cli security scan --check xss

CVE Scan

Scan dependencies for known CVEs

npx @claude-flow/cli security cve --scan


Example:

npx @claude-flow/cli security cve --scan --severity high

Security Audit Report

Generate full security audit report

npx @claude-flow/cli security audit --report


Example:

npx @claude-flow/cli security audit --report --format markdown --output SECURITY.md

Threat Modeling

Run threat modeling analysis

npx @claude-flow/cli security threats --analyze

Validate Secrets

Check for hardcoded secrets

npx @claude-flow/cli security validate --check secrets

Scripts
Script	Path	Description
security-scan	.agents/scripts/security-scan.sh	Run full security scan pipeline
cve-remediate	.agents/scripts/cve-remediate.sh	Auto-remediate known CVEs
References
Document	Path	Description
Security Checklist	docs/security-checklist.md	Security review checklist
OWASP Guide	docs/owasp-top10.md	OWASP Top 10 mitigation guide
Best Practices
Check memory for existing patterns before starting
Use hierarchical topology for coordination
Store successful patterns after completion
Document any new learnings
Weekly Installs
205
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn