---
title: auditing-python-security
url: https://skills.sh/wdm0006/python-skills/auditing-python-security
---

# auditing-python-security

skills/wdm0006/python-skills/auditing-python-security
auditing-python-security
Installation
$ npx skills add https://github.com/wdm0006/python-skills --skill auditing-python-security
SKILL.md
Python Security Auditing
Quick Start
# Static analysis
bandit -r src/ -ll                    # High severity only
pip-audit                             # Dependency vulnerabilities
detect-secrets scan > .secrets.baseline  # Secrets detection

Tool Configuration

Bandit (.bandit):

exclude_dirs: [tests/, docs/, .venv/]
skips: [B101]  # assert_used - OK in tests


pip-audit:

pip-audit -r requirements.txt         # Scan requirements
pip-audit --fix                       # Auto-fix vulnerabilities

Common Vulnerabilities
Issue	Bandit ID	Fix
SQL injection	B608	Use parameterized queries
Command injection	B602	subprocess without shell=True
Hardcoded secrets	B105, B106	Environment variables
Weak crypto	B303	Use SHA-256+, bcrypt for passwords
Pickle untrusted data	B301	Use JSON instead
Path traversal	B108	Validate with Path.resolve()
Secure Patterns
# SQL - Parameterized query
conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# Commands - No shell
subprocess.run(["cat", filename], check=True)

# Secrets - Environment
API_KEY = os.environ.get("API_KEY")

# Paths - Validate
base = Path("/data").resolve()
file_path = (base / filename).resolve()
if not file_path.is_relative_to(base):
    raise ValueError("Invalid path")

CI Integration
# .github/workflows/security.yml
- run: bandit -r src/ -ll
- run: pip-audit
- run: detect-secrets scan --all-files


For detailed patterns, see:

VULNERABILITIES.md - Full vulnerability examples
CI_SECURITY.md - Complete CI workflow
Audit Checklist
Code:
- [ ] No SQL injection (parameterized queries)
- [ ] No command injection (no shell=True)
- [ ] No hardcoded secrets
- [ ] No weak crypto (MD5/SHA1)
- [ ] Input validation on external data
- [ ] Path traversal prevention

Dependencies:
- [ ] pip-audit clean
- [ ] Minimal dependencies
- [ ] From trusted sources

CI:
- [ ] Security scan on every PR
- [ ] Weekly dependency scan

Learn More

This skill is based on the Security section of the Guide to Developing High-Quality Python Libraries by Will McGinnis. See these posts for deeper coverage:

Avoiding Injection Flaws
Intro to Bandit
Advanced Bandit Configuration
SQL Injection Detection
Dependency Security with pip-audit
Handling Sensitive Data
Secure Coding Practices
Weekly Installs
26
Repository
wdm0006/python-skills
GitHub Stars
24
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass