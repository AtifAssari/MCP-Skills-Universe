---
rating: ⭐⭐⭐
title: security-monitor
url: https://skills.sh/aaaaqwq/claude-code-skills/security-monitor
---

# security-monitor

skills/aaaaqwq/claude-code-skills/security-monitor
security-monitor
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill security-monitor
SKILL.md
Security Monitor Skill
When to use

Run continuous security monitoring to detect breaches, intrusions, and unusual activity on your Clawdbot deployment.

Setup

No external dependencies required. Runs as a background process.

How to
Start real-time monitoring
node skills/security-monitor/scripts/monitor.cjs --interval 60

Run in daemon mode (background)
node skills/security-monitor/scripts/monitor.cjs --daemon --interval 60

Monitor for specific threats
node skills/security-monitor/scripts/monitor.cjs --threats=credentials,ports,api-calls

What It Monitors
Threat	Detection	Response
Brute force attacks	Failed login detection	Alert + IP tracking
Port scanning	Rapid connection attempts	Alert
Process anomalies	Unexpected processes	Alert
File changes	Unauthorized modifications	Alert
Container health	Docker issues	Alert
Output
Console output (stdout)
JSON logs at /root/clawd/clawdbot-security/logs/alerts.log
Telegram alerts (configurable)
Daemon Mode

Use systemd or PM2 to keep monitoring active:

# With PM2
pm2 start monitor.cjs --name "clawdbot-security" -- --daemon --interval 60

Combined with Security Audit

Run audit first, then monitor continuously:

# One-time audit
node skills/security-audit/scripts/audit.cjs --full

# Continuous monitoring
node skills/security-monitor/scripts/monitor.cjs --daemon

Related skills
security-audit - One-time security scan (install separately)
Weekly Installs
36
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass