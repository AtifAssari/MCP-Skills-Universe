---
rating: ⭐⭐⭐
title: senior-security
url: https://skills.sh/alirezarezvani/claude-skills/senior-security
---

# senior-security

skills/alirezarezvani/claude-skills/senior-security
senior-security
Installation
$ npx skills add https://github.com/alirezarezvani/claude-skills --skill senior-security
SKILL.md
Senior Security Engineer

Security engineering tools for threat modeling, vulnerability analysis, secure architecture design, and penetration testing.

Table of Contents
Threat Modeling Workflow
Security Architecture Workflow
Vulnerability Assessment Workflow
Secure Code Review Workflow
Incident Response Workflow
Security Tools Reference
Tools and References
Threat Modeling Workflow

Identify and analyze security threats using STRIDE methodology.

Workflow: Conduct Threat Model
Define system scope and boundaries:
Identify assets to protect
Map trust boundaries
Document data flows
Create data flow diagram:
External entities (users, services)
Processes (application components)
Data stores (databases, caches)
Data flows (APIs, network connections)
Apply STRIDE to each DFD element (see STRIDE per Element Matrix below)
Score risks using DREAD:
Damage potential (1-10)
Reproducibility (1-10)
Exploitability (1-10)
Affected users (1-10)
Discoverability (1-10)
Prioritize threats by risk score
Define mitigations for each threat
Document in threat model report
Validation: All DFD elements analyzed; STRIDE applied; threats scored; mitigations mapped
STRIDE Threat Categories
Category	Security Property	Mitigation Focus
Spoofing	Authentication	MFA, certificates, strong auth
Tampering	Integrity	Signing, checksums, validation
Repudiation	Non-repudiation	Audit logs, digital signatures
Information Disclosure	Confidentiality	Encryption, access controls
Denial of Service	Availability	Rate limiting, redundancy
Elevation of Privilege	Authorization	RBAC, least privilege
STRIDE per Element Matrix
DFD Element	S	T	R	I	D	E
External Entity	X		X			
Process	X	X	X	X	X	X
Data Store		X	X	X	X	
Data Flow		X		X	X	

See: references/threat-modeling-guide.md

Security Architecture Workflow

Design secure systems using defense-in-depth principles.

Workflow: Design Secure Architecture
Define security requirements:
Compliance requirements (GDPR, HIPAA, PCI-DSS)
Data classification (public, internal, confidential, restricted)
Threat model inputs
Apply defense-in-depth layers:
Perimeter: WAF, DDoS protection, rate limiting
Network: Segmentation, IDS/IPS, mTLS
Host: Patching, EDR, hardening
Application: Input validation, authentication, secure coding
Data: Encryption at rest and in transit
Implement Zero Trust principles:
Verify explicitly (every request)
Least privilege access (JIT/JEA)
Assume breach (segment, monitor)
Configure authentication and authorization:
Identity provider selection
MFA requirements
RBAC/ABAC model
Design encryption strategy:
Key management approach
Algorithm selection
Certificate lifecycle
Plan security monitoring:
Log aggregation
SIEM integration
Alerting rules
Document architecture decisions
Validation: Defense-in-depth layers defined; Zero Trust applied; encryption strategy documented; monitoring planned
Defense-in-Depth Layers
Layer 1: PERIMETER
  WAF, DDoS mitigation, DNS filtering, rate limiting

Layer 2: NETWORK
  Segmentation, IDS/IPS, network monitoring, VPN, mTLS

Layer 3: HOST
  Endpoint protection, OS hardening, patching, logging

Layer 4: APPLICATION
  Input validation, authentication, secure coding, SAST

Layer 5: DATA
  Encryption at rest/transit, access controls, DLP, backup

Authentication Pattern Selection
Use Case	Recommended Pattern
Web application	OAuth 2.0 + PKCE with OIDC
API authentication	JWT with short expiration + refresh tokens
Service-to-service	mTLS with certificate rotation
CLI/Automation	API keys with IP allowlisting
High security	FIDO2/WebAuthn hardware keys

See: references/security-architecture-patterns.md

Vulnerability Assessment Workflow

Identify and remediate security vulnerabilities in applications.

Workflow: Conduct Vulnerability Assessment
Define assessment scope:
In-scope systems and applications
Testing methodology (black box, gray box, white box)
Rules of engagement
Gather information:
Technology stack inventory
Architecture documentation
Previous vulnerability reports
Perform automated scanning:
SAST (static analysis)
DAST (dynamic analysis)
Dependency scanning
Secret detection
Conduct manual testing:
Business logic flaws
Authentication bypass
Authorization issues
Injection vulnerabilities
Classify findings by severity:
Critical: Immediate exploitation risk
High: Significant impact, easier to exploit
Medium: Moderate impact or difficulty
Low: Minor impact
Develop remediation plan:
Prioritize by risk
Assign owners
Set deadlines
Verify fixes and document
Validation: Scope defined; automated and manual testing complete; findings classified; remediation tracked

For OWASP Top 10 vulnerability descriptions and testing guidance, refer to owasp.org/Top10.

Vulnerability Severity Matrix
Impact \ Exploitability	Easy	Moderate	Difficult
Critical	Critical	Critical	High
High	Critical	High	Medium
Medium	High	Medium	Low
Low	Medium	Low	Low
Secure Code Review Workflow

Review code for security vulnerabilities before deployment.

Workflow: Conduct Security Code Review
Establish review scope:
Changed files and functions
Security-sensitive areas (auth, crypto, input handling)
Third-party integrations
Run automated analysis:
SAST tools (Semgrep, CodeQL, Bandit)
Secret scanning
Dependency vulnerability check
Review authentication code:
Password handling (hashing, storage)
Session management
Token validation
Review authorization code:
Access control checks
RBAC implementation
Privilege boundaries
Review data handling:
Input validation
Output encoding
SQL query construction
File path handling
Review cryptographic code:
Algorithm selection
Key management
Random number generation
Document findings with severity
Validation: Automated scans passed; auth/authz reviewed; data handling checked; crypto verified; findings documented
Security Code Review Checklist
Category	Check	Risk
Input Validation	All user input validated and sanitized	Injection
Output Encoding	Context-appropriate encoding applied	XSS
Authentication	Passwords hashed with Argon2/bcrypt	Credential theft
Session	Secure cookie flags set (HttpOnly, Secure, SameSite)	Session hijacking
Authorization	Server-side permission checks on all endpoints	Privilege escalation
SQL	Parameterized queries used exclusively	SQL injection
File Access	Path traversal sequences rejected	Path traversal
Secrets	No hardcoded credentials or keys	Information disclosure
Dependencies	Known vulnerable packages updated	Supply chain
Logging	Sensitive data not logged	Information disclosure
Secure vs Insecure Patterns
Pattern	Issue	Secure Alternative
SQL string formatting	SQL injection	Use parameterized queries with placeholders
Shell command building	Command injection	Use subprocess with argument lists, no shell
Path concatenation	Path traversal	Validate and canonicalize paths
MD5/SHA1 for passwords	Weak hashing	Use Argon2id or bcrypt
Math.random for tokens	Predictable values	Use crypto.getRandomValues
Inline Code Examples

SQL Injection — insecure vs. secure (Python):

# ❌ Insecure: string formatting allows SQL injection
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)

# ✅ Secure: parameterized query — user input never interpreted as SQL
query = "SELECT * FROM users WHERE username = %s"
cursor.execute(query, (username,))


Password Hashing with Argon2id (Python):

from argon2 import PasswordHasher

ph = PasswordHasher()          # uses secure defaults (time_cost, memory_cost)

# On registration
hashed = ph.hash(plain_password)

# On login — raises argon2.exceptions.VerifyMismatchError on failure
ph.verify(hashed, plain_password)


Secret Scanning — core pattern matching (Python):

import re, pathlib

SECRET_PATTERNS = {
    "aws_access_key":  re.compile(r"AKIA[0-9A-Z]{16}"),
    "github_token":    re.compile(r"ghp_[A-Za-z0-9]{36}"),
    "private_key":     re.compile(r"-----BEGIN (RSA |EC )?PRIVATE KEY-----"),
    "generic_secret":  re.compile(r'(?i)(password|secret|api_key)\s*=\s*["\']?\S{8,}'),
}

def scan_file(path: pathlib.Path) -> list[dict]:
    findings = []
    for lineno, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(line):
                findings.append({"file": str(path), "line": lineno, "type": name})
    return findings

Incident Response Workflow

Respond to and contain security incidents.

Workflow: Handle Security Incident
Identify and triage:
Validate incident is genuine
Assess initial scope and severity
Activate incident response team
Contain the threat:
Isolate affected systems
Block malicious IPs/accounts
Disable compromised credentials
Eradicate root cause:
Remove malware/backdoors
Patch vulnerabilities
Update configurations
Recover operations:
Restore from clean backups
Verify system integrity
Monitor for recurrence
Conduct post-mortem:
Timeline reconstruction
Root cause analysis
Lessons learned
Implement improvements:
Update detection rules
Enhance controls
Update runbooks
Document and report
Validation: Threat contained; root cause eliminated; systems recovered; post-mortem complete; improvements implemented
Incident Severity Levels
Level	Response Time	Escalation
P1 - Critical (active breach/exfiltration)	Immediate	CISO, Legal, Executive
P2 - High (confirmed, contained)	1 hour	Security Lead, IT Director
P3 - Medium (potential, under investigation)	4 hours	Security Team
P4 - Low (suspicious, low impact)	24 hours	On-call engineer
Incident Response Checklist
Phase	Actions
Identification	Validate alert, assess scope, determine severity
Containment	Isolate systems, preserve evidence, block access
Eradication	Remove threat, patch vulnerabilities, reset credentials
Recovery	Restore services, verify integrity, increase monitoring
Lessons Learned	Document timeline, identify gaps, update procedures
Security Tools Reference
Recommended Security Tools
Category	Tools
SAST	Semgrep, CodeQL, Bandit (Python), ESLint security plugins
DAST	OWASP ZAP, Burp Suite, Nikto
Dependency Scanning	Snyk, Dependabot, npm audit, pip-audit
Secret Detection	GitLeaks, TruffleHog, detect-secrets
Container Security	Trivy, Clair, Anchore
Infrastructure	Checkov, tfsec, ScoutSuite
Network	Wireshark, Nmap, Masscan
Penetration	Metasploit, sqlmap, Burp Suite Pro
Cryptographic Algorithm Selection
Use Case	Algorithm	Key Size
Symmetric encryption	AES-256-GCM	256 bits
Password hashing	Argon2id	N/A (use defaults)
Message authentication	HMAC-SHA256	256 bits
Digital signatures	Ed25519	256 bits
Key exchange	X25519	256 bits
TLS	TLS 1.3	N/A

See: references/cryptography-implementation.md

Tools and References
Scripts
Script	Purpose
threat_modeler.py	STRIDE threat analysis with DREAD risk scoring; JSON and text output; interactive guided mode
secret_scanner.py	Detect hardcoded secrets and credentials across 20+ patterns; CI/CD integration ready

For usage, see the inline code examples in Secure Code Review Workflow and the script source files directly.

References
Document	Content
security-architecture-patterns.md	Zero Trust, defense-in-depth, authentication patterns, API security
threat-modeling-guide.md	STRIDE methodology, attack trees, DREAD scoring, DFD creation
cryptography-implementation.md	AES-GCM, RSA, Ed25519, password hashing, key management
Security Standards Reference
Security Headers Checklist
Header	Recommended Value
Content-Security-Policy	default-src self; script-src self
X-Frame-Options	DENY
X-Content-Type-Options	nosniff
Strict-Transport-Security	max-age=31536000; includeSubDomains
Referrer-Policy	strict-origin-when-cross-origin
Permissions-Policy	geolocation=(), microphone=(), camera=()

For compliance framework requirements (OWASP ASVS, CIS Benchmarks, NIST CSF, PCI-DSS, HIPAA, SOC 2), refer to the respective official documentation.

Related Skills
Skill	Integration Point
senior-devops	CI/CD security, infrastructure hardening
senior-secops	Security monitoring, incident response
senior-backend	Secure API development
senior-architect	Security architecture decisions
Weekly Installs
224
Repository
alirezarezvani/…e-skills
GitHub Stars
13.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass