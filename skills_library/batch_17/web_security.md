---
title: web-security
url: https://skills.sh/kiwamizamurai/cctf/web-security
---

# web-security

skills/kiwamizamurai/cctf/web-security
web-security
Installation
$ npx skills add https://github.com/kiwamizamurai/cctf --skill web-security
SKILL.md
Web Security Skill
Quick Workflow
Progress:
- [ ] Identify technology stack
- [ ] Check common files (robots.txt, .git)
- [ ] Test injection points (SQLi, XSS, SSTI)
- [ ] Check authentication/session flaws
- [ ] Develop exploit
- [ ] Extract flag

Quick Recon
# Directory enumeration
gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt
ffuf -u http://target/FUZZ -w wordlist.txt

# Technology detection
whatweb http://target
curl -I http://target

# Check robots.txt, .git exposure
curl http://target/robots.txt
curl http://target/.git/HEAD

Vulnerability Reference
Vulnerability	Reference File
SQL Injection	reference/sqli.md
XSS	reference/xss.md
SSTI	reference/ssti.md
Command Injection	reference/command-injection.md
SSRF / Path Traversal	reference/ssrf-lfi.md
Auth Bypass / Deserialization	reference/auth-deser.md
Tools Quick Reference
Tool	Purpose	Command
sqlmap	SQLi automation	sqlmap -u URL --dbs
commix	Command injection	commix -u URL
tplmap	SSTI automation	tplmap -u URL
ffuf	Fuzzing	ffuf -u URL/FUZZ -w wordlist
Burp Suite	Proxy/intercept	GUI
jwt_tool	JWT attacks	jwt_tool TOKEN
Weekly Installs
24
Repository
kiwamizamurai/cctf
GitHub Stars
7
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykWarn