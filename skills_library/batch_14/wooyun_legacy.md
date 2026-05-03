---
title: wooyun-legacy
url: https://skills.sh/trailofbits/skills-curated/wooyun-legacy
---

# wooyun-legacy

skills/trailofbits/skills-curated/wooyun-legacy
wooyun-legacy
Installation
$ npx skills add https://github.com/trailofbits/skills-curated --skill wooyun-legacy
SKILL.md
WooYun Vulnerability Analysis Knowledge Base

Methodology and testing patterns extracted from 88,636 real-world vulnerability cases reported to the WooYun platform (2010-2016).

When to Use

All testing described here must be performed only against systems you have written authorization to test.

Penetration testing web applications
Security code review (server-side or client-side)
Vulnerability research against web targets you have explicit authorization to test
Building security test cases or checklists
Assessing web application attack surface
Reviewing remediation effectiveness
Training or education in authorized security testing contexts
When NOT to Use
Network infrastructure testing (firewalls, routers, switches)
Mobile application binary analysis
Malware analysis or reverse engineering
Compliance-only assessments (PCI-DSS, SOC2 checklists without testing)
Physical security assessments
Social engineering campaigns
Cloud infrastructure misconfigurations (IAM, S3 buckets) — these require cloud-specific tooling, not web vuln patterns
Rationalizations to Reject

These shortcuts lead to missed findings. Reject them:

"The WAF will catch it" — WAFs are bypass-able; test the application logic, not the middleware
"It's an internal app, so auth doesn't matter" — internal apps get compromised via SSRF, lateral movement, and credential reuse
"We already use parameterized queries everywhere" — check for ORM misuse, stored procedures with dynamic SQL, and second-order injection
"The framework handles XSS" — template engines have raw output modes, JavaScript contexts bypass HTML encoding, and DOM XSS lives entirely client-side
"File uploads are safe because we check the extension" — extension checks are bypassed via null bytes, double extensions, parser discrepancies, and race conditions
"We validate on the frontend" — client-side validation is a UX feature, not a security control
"Nobody would guess that URL" — security through obscurity fails against directory bruteforcing, referrer leaks, and JS source analysis
"Low severity, not worth reporting" — low-severity findings chain into critical attack paths
Core Mental Model
Vulnerability = Expected Behavior - Actual Behavior
             = Developer Assumptions + Attacker Input -> Unexpected State

Analysis chain:
1. Where does data come from?  (Input sources)
   -> GET/POST/Cookie/Header/File/WebSocket
2. Where does data flow?       (Data path)
   -> Validation -> Processing -> Storage -> Output
3. Where is data trusted?      (Trust boundaries)
   -> Client / Server / Database / OS / External service
4. How is data processed?      (Processing logic)
   -> Filter / Escape / Validate / Execute
5. Where does data end up?     (Output sinks)
   -> HTML / SQL / Shell / Filesystem / Log / Email

Attack Surface Mapping
              +-------------------------------------------+
              |         Application Attack Surface         |
              +-------------------------------------------+
                                  |
          +-----------------------+-----------------------+
          |                       |                       |
     +----v----+            +-----v-----+           +-----v-----+
     |  Input  |            | Processing|           |  Output   |
     +---------+            +-----------+           +-----------+
     | GET     |            | Input     |           | HTML page |
     | POST    |    ->      | validation|    ->     | JSON resp |
     | Cookie  |            | Biz logic |           | File DL   |
     | Headers |            | DB query  |           | Error msg |
     | File    |            | File op   |           | Log entry |
     | Upload  |            | Sys call  |           | Email     |
     +---------+            +-----------+           +-----------+

SQL Injection

Cases: 27,732 | Reference: sql-injection.md | Checklist: sql-injection-checklist.md

High-risk parameters: id, sort_id, username, password, search, keyword, page, order, cat_id

Injection point detection:

String terminators: ' " ) ') ") -- # /*
DB fingerprint: @@version (MSSQL), version() (MySQL), v$version (Oracle)

Bypass techniques:

Whitespace: /**/ %09 %0a ()
Keywords: SeLeCt sel%00ect /*!select*/
Equals: LIKE REGEXP BETWEEN IN
Quotes: 0x hex, char(), concat()

Core defense: parameterized queries (PreparedStatement / ORM binding).

Cross-Site Scripting (XSS)

Cases: 7,532 | Reference: xss.md | Checklist: xss-checklist.md

Output points: user profile fields (nickname, bio), search reflections, file metadata (filename, alt text), email content (subject, body)

Bypass techniques:

Tag mutation: <ScRiPt> <script/x> <script\n>
Event handlers: onerror onload onmouseover onfocus
Encoding: HTML entities, JS Unicode, URL encoding
Protocol handlers: javascript: data: vbscript:

Core defense: context-aware output encoding + Content Security Policy.

Command Execution

Cases: 6,826 | Reference: command-execution.md | Checklist: command-execution-checklist.md

Entry points: system command wrappers (ping, traceroute, nslookup), file operations (compress, decompress, image processing), code eval (eval, assert, preg_replace(/e)), framework vulnerabilities (Struts2, WebLogic, JBoss)

Command chaining:

Linux: ; | || && \ $()`
Windows: & | || &&

Bypass techniques:

Whitespace: ${IFS} $IFS$9 %09 < <>
Keywords: ca\t ca''t c$@at /???/??t
Encoding: $(printf "\x63\x61\x74"), `echo Y2F0|base64 -d`

Core defense: avoid shell invocation; use execFile over exec, allowlist acceptable inputs.

File Upload

Cases: 2,711 | Reference: file-upload.md | Checklist: file-upload-checklist.md

Bypass detection:

Client-side validation: modify JS or send request directly
Content-Type: image/gif header + PHP code body
Extension: .php5 .phtml .pht .php. .php::$DATA
Content inspection: GIF89a + <?php or image-based webshell
Parser discrepancy: /upload/1.asp;.jpg (IIS 6.0)

Parser-specific vulnerabilities:

IIS 6.0: /test.asp/1.jpg, test.asp;.jpg
Apache: .php.xxx (unknown extension fallback)
Nginx: /1.jpg/1.php (cgi.fix_pathinfo)
Tomcat: test.jsp%00.jpg

Core defense: allowlist extensions, rename uploads, store outside webroot, validate content type server-side.

Path Traversal

Cases: 2,854 | Reference: path-traversal.md | Checklist: path-traversal-checklist.md

High-risk parameters: file, path, filename, url, dir, template, page, include, download

Traversal payloads:

Basic: ../../../etc/passwd
Encoded: %2e%2e%2f, ..%252f, %c0%ae%c0%ae/
Null byte: ../../../etc/passwd%00.jpg
Windows: ..\..\..\windows\win.ini

Target files (Linux): /etc/passwd, /etc/shadow, /proc/self/environ, /var/log/apache2/access.log

Core defense: resolve canonical paths, validate against allowlisted directories, never use user input in file paths directly.

Unauthorized Access

Cases: 14,377 | Reference: unauthorized-access.md | Checklist: unauthorized-access-checklist.md

Access types:

Admin panel exposure: /admin, /manager, /console
API without authentication: missing token validation, predictable tokens
Exposed services: Redis (6379), MongoDB (27017), Elasticsearch (9200), Memcached (11211), Docker (2375)
IDOR: horizontal privilege escalation via ID enumeration

Core defense: authentication + authorization on every endpoint, session management, principle of least privilege.

Information Disclosure

Cases: 7,337 | Reference: info-disclosure.md | Checklist: info-disclosure-checklist.md

Disclosure sources: error messages with stack traces, exposed .git or .svn directories, backup files (.bak, .sql, .tar.gz), configuration files, debug endpoints, directory listings

Core defense: custom error pages, disable directory listing, remove debug endpoints in production, audit publicly accessible files.

Business Logic Flaws

Cases: 8,292 | Reference: logic-flaws.md | Checklist: logic-flaws-checklist.md

Vulnerability patterns:

Password reset: verification code in response body, step skipping, controllable reset tokens
Authorization bypass: horizontal (ID enumeration), vertical (role escalation)
Payment logic: amount tampering, quantity manipulation, coupon stacking
CAPTCHA: not refreshed, reusable, brute-forceable, client-side only

Testing approach:

Map the business flow -> draw state transition diagram
Identify critical checks -> which parameters determine outcomes
Attempt bypass -> modify parameters / skip steps / replay / race
Verify impact -> prove the scope of harm

Core defense: server-side validation of all business-critical logic.

Additional Categories

These categories are derived from case data without full reference documents. Each has a testing checklist extracted from real cases.

Category	Checklist
CSRF	csrf-checklist.md
SSRF	ssrf-checklist.md
Weak Passwords	weak-password-checklist.md
Misconfiguration	misconfig-checklist.md
Remote Code Execution	rce-checklist.md
XML External Entity (XXE)	xxe-checklist.md

Note: The RCE checklist covers deserialization, OGNL injection, and framework-specific remote code execution — distinct from the OS command injection focus of the Command Execution reference above.

Methodology Case Studies

Real-world penetration testing methodology examples (anonymized):

Case Study	Description
bank-penetration.md	Multi-stage attack chain against a financial institution
telecom-penetration.md	Infrastructure penetration of a telecom carrier

These demonstrate how individual vulnerabilities chain together into full compromise scenarios.

Testing Priority Framework
High Priority (test first)
SQL Injection — direct data access, highest case count (27,732)
Command Execution — OS-level compromise
File Upload — arbitrary code execution via webshell
Medium Priority
Unauthorized Access — second-highest case count (14,377)
Business Logic Flaws — application-specific, hard to automate
XSS — session hijacking, phishing
Lower Priority (but still important)
Path Traversal — file read, sometimes write
Information Disclosure — reconnaissance value, enables chaining
CSRF/SSRF/XXE — context-dependent severity
Defense Quick Reference
Vulnerability	Core Defense	Implementation
SQL Injection	Parameterized queries	PreparedStatement / ORM
XSS	Output encoding	Context-aware escaping + CSP
Command Execution	Avoid shell	execFile not exec, allowlist
File Upload	Strict validation	Allowlist ext, rename, isolate
Path Traversal	Canonical paths	Resolve + validate against allowlist
Unauthorized Access	Access control	AuthN + AuthZ + session mgmt
Logic Flaws	Server-side checks	Validate all business logic server-side
Info Disclosure	Minimize exposure	Custom errors, no debug in prod
Key Insight

All 88,636 vulnerabilities in this database share a common root cause: the gap between what developers assumed and what attackers actually provided. Effective security testing means systematically challenging every assumption at every trust boundary.

Four principles from the data:

Boundary thinking — all vulnerabilities occur at trust boundaries
Data flow tracing — follow data from input to output completely
Assumption challenging — question every "obvious" validation
Chain composition — individual low-severity findings combine into critical attack paths
Weekly Installs
51
Repository
trailofbits/ski…-curated
GitHub Stars
381
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail