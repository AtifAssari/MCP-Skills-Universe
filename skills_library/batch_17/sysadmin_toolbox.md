---
title: sysadmin-toolbox
url: https://skills.sh/jdrhyne/agent-skills/sysadmin-toolbox
---

# sysadmin-toolbox

skills/jdrhyne/agent-skills/sysadmin-toolbox
sysadmin-toolbox
Installation
$ npx skills add https://github.com/jdrhyne/agent-skills --skill sysadmin-toolbox
SKILL.md
Sysadmin Toolbox

Curated tool recommendations and practical shell one-liners for operational work.

When to Auto-Consult

Load relevant references when user is:

Debugging network connectivity, ports, traffic
Troubleshooting DNS or SSL/TLS
Analyzing processes, memory, disk usage
Working with logs or system diagnostics
Writing shell scripts or one-liners
Asking "what's a good tool for..."
Doing security audits or pentesting
Working with containers/Docker/K8s
Bundled Guides
File	Use When
shell-oneliners.md in this skill's references folder	Need practical commands for: terminal, networking, SSL, curl, ssh, tcpdump, git, awk, sed, grep, find
cli-tools.md in this skill's references folder	Recommending CLI tools: shells, file managers, network utils, databases, security tools
web-tools.md in this skill's references folder	Web-based tools: SSL checkers, DNS lookup, performance testing, OSINT, scanners
security-tools.md in this skill's references folder	Pentesting, vulnerability scanning, exploit databases, CTF resources
shell-tricks.md in this skill's references folder	Shell scripting patterns and tricks
Safety Boundaries
Do not run destructive system commands, privilege-escalation steps, or offensive tooling unless the user explicitly asked for that scope.
Do not scan hosts, domains, or networks the user does not control or have permission to assess.
Do not assume a command is safe to paste into production without explaining what it does.
Do not persist logs, captures, or credentials outside the user's requested troubleshooting workflow.
Quick Tool Index
Network Debugging
mtr - traceroute + ping combined
tcpdump / tshark - packet capture
netstat / ss - connection monitoring
nmap - port scanning
curl / httpie - HTTP testing
DNS
dig / host - DNS queries
dnsdiag - DNS diagnostics
subfinder / amass - subdomain enumeration
SSL/TLS
openssl - certificate inspection
testssl.sh - TLS testing
sslyze - SSL scanning
certbot - Let's Encrypt
Process/System
htop / btop - process monitoring
strace / ltrace - syscall/library tracing
lsof - open files/connections
ncdu - disk usage
Log Analysis
lnav - log navigator
GoAccess - web log analyzer
angle-grinder - log slicing
Containers
dive - Docker image analysis
ctop - container top
lazydocker - Docker TUI
Keeping Current

References auto-refresh weekly (Sundays 5am ET) from the upstream repo:

~/clawd-duke-leto/skills/sysadmin-toolbox/scripts/refresh.sh


Manual refresh anytime:

./scripts/refresh.sh [skill-dir]

Example Queries → Actions

"Why is this port not responding?" → Load shell-oneliners.md, search for netstat/ss/lsof commands

"What's a good tool for testing SSL?" → Load cli-tools.md SSL section, recommend testssl.sh or sslyze

"Show me how to find large files" → Load shell-oneliners.md, search for find/ncdu/du commands

"I need to debug DNS resolution" → Load shell-oneliners.md dig section + recommend dnsdiag from cli-tools.md

Weekly Installs
88
Repository
jdrhyne/agent-skills
GitHub Stars
232
First Seen
Feb 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn