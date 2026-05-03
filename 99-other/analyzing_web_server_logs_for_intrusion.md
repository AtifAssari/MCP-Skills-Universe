---
title: analyzing-web-server-logs-for-intrusion
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-web-server-logs-for-intrusion
---

# analyzing-web-server-logs-for-intrusion

skills/mukul975/anthropic-cybersecurity-skills/analyzing-web-server-logs-for-intrusion
analyzing-web-server-logs-for-intrusion
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-web-server-logs-for-intrusion
SKILL.md
Analyzing Web Server Logs for Intrusion
When to Use
When investigating security incidents that require analyzing web server logs for intrusion
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Familiarity with security operations concepts and tools
Access to a test or lab environment for safe execution
Python 3.8+ with required dependencies installed
Appropriate authorization for any testing activities
Instructions
Install dependencies: pip install geoip2 user-agents
Collect web server access logs in Combined Log Format (Apache) or Nginx default format.
Parse each log entry extracting: IP, timestamp, method, URI, status code, response size, user-agent, referer.
Apply detection rules:
SQL injection: UNION SELECT, OR 1=1, ' OR ', hex encoding patterns
LFI/Path traversal: ../, /etc/passwd, /proc/self, php://filter
XSS: <script>, javascript:, onerror=, onload=
Scanner signatures: nikto, sqlmap, dirbuster, gobuster, wfuzz user-agents
Brute force: >50 POST requests to login endpoints from same IP in 5 minutes
Enrich with GeoIP data and generate a prioritized findings report.
python scripts/agent.py --log-file /var/log/nginx/access.log --geoip-db GeoLite2-City.mmdb --output web_intrusion_report.json

Examples
Detect SQLi in URI
192.168.1.100 - - [15/Jan/2024:10:30:45 +0000] "GET /products?id=1' UNION SELECT username,password FROM users-- HTTP/1.1" 200 4532

Scanner User-Agent Detection
Nikto/2.1.6, sqlmap/1.7, DirBuster-1.0-RC1, gobuster/3.1.0

Weekly Installs
43
Repository
mukul975/anthro…y-skills
GitHub Stars
5.9K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn