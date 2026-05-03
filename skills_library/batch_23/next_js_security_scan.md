---
title: next.js security scan
url: https://skills.sh/sugarforever/01coder-agent-skills/next.js-security-scan
---

# next.js security scan

skills/sugarforever/01coder-agent-skills/Next.js Security Scan
Next.js Security Scan
Installation
$ npx skills add https://github.com/sugarforever/01coder-agent-skills --skill 'Next.js Security Scan'
SKILL.md
Next.js Security Scan Skill

This skill enables comprehensive security scanning of Next.js and TypeScript/JavaScript projects based on OWASP guidelines and industry best practices.

When to Use This Skill
Security audits of Next.js applications
Code review for security vulnerabilities
Pre-deployment security checks
Dependency vulnerability assessment
Detecting hardcoded secrets and credentials
Scan Types
1. Quick Scan

Fast scan focusing on critical vulnerabilities:

Hardcoded secrets and API keys
Dangerous function usage (dangerouslySetInnerHTML, eval)
Missing authentication in Server Actions
Known vulnerable dependencies
2. Full Scan

Comprehensive security assessment covering:

All OWASP Top 10:2025 categories
XSS vulnerability patterns
Injection vulnerabilities (SQL, NoSQL, Command)
Authentication and authorization flaws
Security misconfigurations
Cryptographic failures
Next.js-specific vulnerabilities
Dependency audit (CVE check)
Environment variable exposure
3. Targeted Scan

Focus on specific vulnerability categories:

--xss - Cross-site scripting patterns
--injection - SQL/NoSQL/Command injection
--auth - Authentication/authorization issues
--secrets - Hardcoded credentials
--deps - Dependency vulnerabilities
--nextjs - Next.js specific issues
Scan Procedure
Step 1: Project Discovery
Identify project type (Next.js App Router, Pages Router, or plain React)
Locate configuration files (next.config.js, package.json, .env*)
Map the codebase structure
Step 2: Dependency Audit

Run the dependency audit script:

./scripts/dependency-audit.sh


Or manually:

npm audit --json
# or
yarn audit --json

Step 3: Secret Scanning

Scan for hardcoded secrets:

python scripts/secret-scanner.py /path/to/project


Important: Environment File Handling

By default, real .env files are SKIPPED (.env, .env.local, .env.production, etc.)
These files contain actual secrets and should not be in version control
Only .env.example and .env.template files are analyzed for documentation quality
Use --include-env-files flag only if explicitly requested by user

The scanner will:

Scan source code for hardcoded secrets
Analyze .env.example templates to check:
Which sensitive variables are documented
Whether variables have descriptions (comments)
If placeholder values look like real secrets
Suggestions for missing common variables
Step 4: Pattern Analysis

For each file in the codebase, check against patterns in:

references/xss-patterns.md - XSS vulnerabilities
references/injection-patterns.md - Injection flaws
references/auth-vulnerabilities.md - Auth issues
references/nextjs-specific.md - Next.js vulnerabilities
Step 5: Report Generation

Generate a security report using:

assets/report-template.md - Report structure
Severity Classification
Severity	Description	Action Required
CRITICAL	Exploitable vulnerability with severe impact	Immediate fix required
HIGH	Significant security risk	Fix before deployment
MEDIUM	Potential security issue	Fix in next release
LOW	Minor security concern	Consider fixing
INFO	Security best practice suggestion	Optional improvement
Key Files to Scan
Always Check
**/*.ts, **/*.tsx, **/*.js, **/*.jsx - Source code
next.config.js, next.config.mjs - Next.js configuration
package.json, package-lock.json - Dependencies
middleware.ts, middleware.js - Middleware security
Environment Files
.env.example, .env.template - SCAN for template analysis
.env, .env.local, .env.production - SKIP by default (contain real secrets)

Note: Real .env files should never be committed to version control. The scanner analyzes .env.example templates to ensure proper documentation of required variables.

High Priority Locations
app/api/**/* - API routes (App Router)
pages/api/**/* - API routes (Pages Router)
**/actions.ts, **/*-actions.ts - Server Actions
lib/auth*, utils/auth* - Authentication code
**/middleware.* - Middleware files
Output Format

Findings should be reported as:

[SEVERITY] Category: Description
  File: path/to/file.ts:lineNumber
  Code: <relevant code snippet>
  Risk: <explanation of the security risk>
  Fix: <recommended remediation>

Integration with CI/CD

This skill can generate output compatible with:

GitHub Security Advisories
SARIF format for GitHub Code Scanning
JSON for custom integrations
References

Load additional context as needed:

references/owasp-top-10.md - OWASP Top 10:2025 quick reference
references/xss-patterns.md - XSS detection patterns
references/injection-patterns.md - Injection vulnerability patterns
references/auth-vulnerabilities.md - Authentication security patterns
references/nextjs-specific.md - Next.js specific vulnerabilities and CVEs
Weekly Installs
–
Repository
sugarforever/01…t-skills
GitHub Stars
91
First Seen
–