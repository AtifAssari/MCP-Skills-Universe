---
title: production-ready
url: https://skills.sh/adamos486/skills/production-ready
---

# production-ready

skills/adamos486/skills/production-ready
production-ready
Installation
$ npx skills add https://github.com/adamos486/skills --skill production-ready
SKILL.md
Production Ready

Comprehensive production readiness, security hardening, and professional release preparation for any project.

When to Use
Before deploying to production for the first time
After major changes before release
When conducting security audits
When open-sourcing a project
During compliance reviews
When onboarding to a new codebase
Quick Start

First, ask the user which mode:

Which level of audit do you need?

1. **Quick** - Fast CI-suitable checks (~2 min)
   - Secret scanning
   - Critical vulnerabilities only

2. **Security** - Deep security audit (~10 min)
   - All vulnerability severities
   - SBOM generation
   - Configuration hardening

3. **Full** - Comprehensive audit (~15 min)
   - All security checks
   - Documentation review
   - CI/CD validation
   - Monitoring setup check

Step 1: Detect Tech Stack

Before scanning, identify the project's tech stack and dependencies:

# Detect project files to determine stack
ls -la | grep -E "package.json|requirements.txt|Cargo.toml|go.mod|Gemfile|pom.xml|build.gradle|composer.json|pubspec.yaml|*.csproj"

File Detected	Stack	Primary Security Tools
package.json	Node.js/JavaScript	npm audit, snyk, retire.js
requirements.txt / pyproject.toml	Python	pip-audit, safety, bandit
Cargo.toml	Rust	cargo-audit, cargo-deny
go.mod	Go	govulncheck, gosec
Gemfile	Ruby	bundle-audit, brakeman
pom.xml / build.gradle	Java	OWASP Dependency-Check, SpotBugs
composer.json	PHP	composer audit, phpstan
*.csproj	.NET	dotnet list package --vulnerable
pubspec.yaml	Dart/Flutter	dart pub outdated
Step 2: Recommend Security Tools

Based on detected stack, recommend appropriate tools. ALWAYS ask the user before installing any tools.

Universal Tools (All Projects)

Free/Open-Source (Industry Standard):

Tool	Purpose	Install Command
gitleaks	Secret detection in git history	brew install gitleaks or curl -sSfL https://raw.githubusercontent.com/gitleaks/gitleaks/main/scripts/install.sh | sh
trufflehog	Deep secret scanning with verification	brew install trufflehog or curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh
syft	SBOM generation	brew install syft or curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh
grype	Vulnerability scanner (multi-language)	brew install grype or curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh
trivy	Comprehensive security scanner	brew install trivy or see trivy docs
semgrep	Static analysis (SAST)	brew install semgrep or pip install semgrep

Paid/Enterprise (State of the Art):

Tool	Purpose	Notes
Snyk	Full-spectrum security (SCA, SAST, containers)	Free tier available, enterprise features paid
Sonatype Nexus Lifecycle	Enterprise dependency management	Industry leader in SCA
Checkmarx	Enterprise SAST/DAST	Comprehensive enterprise solution
Veracode	Application security platform	Enterprise-grade scanning
GitHub Advanced Security	Integrated security (CodeQL, Dependabot)	Native GitHub integration
Language-Specific Tools

JavaScript/Node.js:

Free: npm audit, yarn audit, retire.js, eslint-plugin-security
Paid: Snyk (free tier), Socket.dev

Python:

Free: pip-audit, safety, bandit
Paid: Snyk, PyUp.io

Go:

Free: govulncheck, gosec
Paid: Snyk

Rust:

Free: cargo-audit, cargo-deny

Ruby:

Free: bundle-audit, brakeman
Paid: Snyk

Java:

Free: OWASP Dependency-Check, SpotBugs
Paid: Sonatype, Snyk
Step 3: Ask User to Install Tools

CRITICAL: ALWAYS ask the user before installing any tools.

Present the recommended tools based on detected stack:

I've detected your project uses [STACK]. Here are the recommended security scanning tools:

**Required (Universal):**
- gitleaks - Secret detection
- grype - Vulnerability scanning
- syft - SBOM generation

**Stack-Specific ([STACK]):**
- [tool1] - [purpose]
- [tool2] - [purpose]

**Optional (Enhanced Coverage):**
- trivy - Comprehensive scanner
- semgrep - Static analysis

Would you like me to install these tools?
1. Yes, install all recommended tools
2. Yes, but only the required universal tools
3. Let me select which ones to install
4. No, I'll install them manually


If user selects option 1, 2, or 3: Proceed with installation using the appropriate package manager, then continue to Step 4.

If user selects option 4: Provide installation commands and proceed to Step 4 when they confirm tools are installed.

Step 4: Run Security Scans

Execute scans based on installed tools and audit mode:

Quick Mode
# Secret scanning
gitleaks detect --source=. --no-banner

# Critical vulnerabilities only
grype dir:. --fail-on=critical --only-fixed

Security Mode (includes Quick)
# Deep secret scan with verification
trufflehog filesystem . --only-verified

# All high+ vulnerabilities
grype dir:. --fail-on=high --only-fixed

# Generate SBOM
syft dir:. -o cyclonedx-json=sbom.json

# Static analysis (if semgrep installed)
semgrep --config auto --error

Full Mode (includes Security)

All security checks plus documentation, CI/CD, and observability validation.

Step 5: Generate Report

Reports MUST be written to docs/reports/ directory.

Create the directory if it doesn't exist:

mkdir -p docs/reports


Generate a markdown report with today's date:

# Report filename format
REPORT_FILE="docs/reports/security-audit-$(date +%Y-%m-%d).md"

Report Template

The generated report should follow this structure:

# Security Audit Report

**Project:** [project-name]
**Date:** [YYYY-MM-DD]
**Audit Mode:** [Quick|Security|Full]
**Auditor:** Claude Code (production-ready skill)

## Executive Summary

- **Total Checks:** X
- **Passed:** X
- **Failed:** X
- **Warnings:** X

## Tech Stack Detected

- Primary Language: [language]
- Package Manager: [manager]
- Frameworks: [frameworks]

## Tools Used

| Tool | Version | Purpose |
|------|---------|---------|
| gitleaks | X.X.X | Secret detection |
| grype | X.X.X | Vulnerability scanning |
| ... | ... | ... |

## Findings

### Critical Issues (Must Fix)

1. **[Issue Title]**
   - Severity: Critical
   - Location: [file:line]
   - Description: [description]
   - Remediation: [steps to fix]

### High Severity Issues

...

### Medium/Low Severity Issues

...

## Dependency Vulnerabilities

| Package | Current | Fixed In | Severity | CVE |
|---------|---------|----------|----------|-----|
| ... | ... | ... | ... | ... |

## SBOM Summary

- Total Packages: X
- Direct Dependencies: X
- Transitive Dependencies: X
- SBOM Location: `docs/reports/sbom-[date].json`

## Recommendations

1. [Prioritized recommendation]
2. [Prioritized recommendation]
...

## Next Steps

- [ ] Fix critical vulnerabilities
- [ ] Review and remediate high-severity issues
- [ ] Update dependencies with known fixes
- [ ] Re-run audit after fixes

---
*Generated by production-ready skill v2.0.0*

Audit Mode Checklists
Quick Mode Checklist
 Secrets: Run gitleaks detect --source=.
 Critical Vulns: Run grype dir:. --fail-on=critical
 Config Basics: Verify .gitignore includes .env, *.key, *.pem
 Generate Report: Write findings to docs/reports/security-audit-[date].md
Security Mode Checklist (includes Quick)
 All vulnerabilities: grype dir:. --fail-on=high
 SBOM generation: syft dir:. -o cyclonedx-json=docs/reports/sbom-[date].json
 Secret deep scan: trufflehog filesystem . --only-verified
 Static analysis: semgrep --config auto (if installed)
 Dependency review: Check for outdated/unmaintained packages
 Configuration hardening:
No hardcoded localhost/ports in config files
Environment variables for all secrets
.env.example exists with placeholder values
 Docker security (if applicable):
Non-root user specified
Pinned base image versions
.dockerignore exists
 Generate Report: Write comprehensive findings to docs/reports/security-audit-[date].md
Full Mode Checklist (includes Security)

Documentation:

 README.md exists with setup instructions
 LICENSE file present
 CHANGELOG.md maintained
 SECURITY.md with vulnerability reporting process
 CONTRIBUTING.md (for open source)

CI/CD:

 CI pipeline configured (GitHub Actions, GitLab CI, etc.)
 Automated tests run on PR/push
 Security scanning in pipeline
 Build artifacts validated

Observability:

 Health check endpoint (/health or /healthz)
 Structured logging configured
 Error tracking setup (Sentry, etc.)
 Metrics collection (if applicable)

Operational:

 Environment-specific configs separated
 Backup/restore procedures documented
 Rollback plan documented
 On-call runbook (for critical services)

Generate Report: Write comprehensive findings to docs/reports/security-audit-[date].md

Web Search for Latest Tools

If the detected tech stack requires specialized tools not listed above, search the internet for current (2025+) industry-standard security scanners for that specific technology. Prioritize:

Tools recommended by official language/framework documentation
OWASP-recommended tools
Tools with active maintenance (commits in last 6 months)
Tools with significant GitHub stars (>1000) and community adoption
Security Standards Reference

Based on OWASP Top 10 2025:

Risk	Key Mitigations
A01: Broken Access Control	Deny by default, validate permissions server-side
A02: Security Misconfiguration	Automated hardening, remove defaults, security headers
A03: Supply Chain	SBOM, dependency scanning, signed builds
A04: Injection	Parameterized queries, input validation
A05: Cryptographic Failures	TLS everywhere, strong algorithms, no hardcoded keys
Common Issues & Fixes
Secrets Found
# Rotate the compromised credential immediately
# Then remove from git history:
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH/TO/FILE" \
  --prune-empty --tag-name-filter cat -- --all

# Or use BFG Repo-Cleaner (faster):
bfg --delete-files "*.env"

Vulnerable Dependencies
# Update to patched version
npm update PACKAGE  # or
pip install PACKAGE --upgrade  # or
cargo update PACKAGE

# If no patch available, evaluate alternatives

Exit Criteria

The project is production-ready when:

Zero high/critical vulnerabilities with available fixes
Zero hardcoded secrets detected
All required documentation present
CI/CD pipeline passes all security checks
SBOM generated and stored in docs/reports/
Health checks operational
Security audit report generated in docs/reports/security-audit-[date].md
References

See references/ directory for:

research.md - Detailed research findings
sources.md - Authoritative sources and links
Weekly Installs
38
Repository
adamos486/skills
GitHub Stars
7
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass