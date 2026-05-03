---
rating: ⭐⭐⭐
title: security-check
url: https://skills.sh/bjesuiter/skills/security-check
---

# security-check

skills/bjesuiter/skills/security-check
security-check
Installation
$ npx skills add https://github.com/bjesuiter/skills --skill security-check
SKILL.md
Security Check

Red-team style security review for code changes. Think like an attacker.

Modes
1. Pending Changes (default)

Review uncommitted changes in the current working directory:

git diff HEAD
git diff --cached  # staged changes

2. Branch vs Main

Review all commits on a branch against main:

git log main..<branch> --oneline  # list commits
git diff main...<branch>          # three dots = merge-base diff

3. Specific Commit Range
git diff <commit1>..<commit2>

Review Checklist
Input Validation
 User input sanitized before use?
 SQL injection vectors?
 Command injection (shell escapes)?
 Path traversal (../ in file paths)?
 XSS in HTML/JS output?
 Prototype pollution (JS objects)?
Authentication & Authorization
 Auth checks on all sensitive endpoints?
 Permission escalation paths?
 Session handling flaws?
 Token exposure in logs/URLs?
 Missing rate limiting?
Secrets & Configuration
 Hardcoded credentials/API keys?
 Secrets in logs or error messages?
 Insecure defaults?
 Debug mode left enabled?
 .env files committed?
Data Exposure
 Sensitive data in responses?
 PII leaked in logs?
 Stack traces exposed to users?
 Internal paths/IPs revealed?
Cryptography
 Weak algorithms (MD5, SHA1 for security)?
 Hardcoded IVs/salts?
 Predictable random values?
 Missing HTTPS enforcement?
Dependencies
 Known vulnerable packages?
 Unpinned versions?
 Typosquatting risk?
File Operations
 Arbitrary file read/write?
 Unsafe deserialization?
 Temp file races?
 Symlink attacks?
Process & Network
 SSRF vectors?
 Open redirects?
 Unsafe subprocess calls?
 Missing timeouts?
Output Format

For each finding:

🔴 [CRITICAL|HIGH|MEDIUM|LOW] <Title>

📍 Location: <file:line>

💀 Attack Vector:
<How an attacker would exploit this>

📝 Code:
<relevant snippet>

✅ Fix:
<suggested remediation>

Workflow
Identify scope — Ask which mode (pending/branch/commit range)
Get the diff — Run appropriate git commands
Analyze systematically — Go through checklist
Prioritize findings — CRITICAL > HIGH > MEDIUM > LOW
Suggest fixes — Concrete code changes, not vague advice
Summary — Executive summary with risk assessment
Quick Commands
# Pending changes
git diff HEAD

# Branch review
git diff main...feature-branch

# Check for secrets (basic)
git diff HEAD | grep -iE "(password|secret|api.?key|token|credential)"

# Check for dangerous functions
git diff HEAD | grep -iE "(eval|exec|system|shell_exec|passthru|popen)"

Risk Levels
CRITICAL: Exploitable now, high impact (RCE, auth bypass, data breach)
HIGH: Likely exploitable, significant impact
MEDIUM: Exploitable under specific conditions
LOW: Defense-in-depth issues, minor exposure
Weekly Installs
14
Repository
bjesuiter/skills
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail