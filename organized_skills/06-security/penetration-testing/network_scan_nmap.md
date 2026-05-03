---
rating: ⭐⭐
title: network-scan-nmap
url: https://skills.sh/vchirrav/product-security-ai-skills/network-scan-nmap
---

# network-scan-nmap

skills/vchirrav/product-security-ai-skills/network-scan-nmap
network-scan-nmap
Installation
$ npx skills add https://github.com/vchirrav/product-security-ai-skills --skill network-scan-nmap
SKILL.md
Network Scanning with Nmap

You are a security engineer performing network discovery and security auditing using Nmap.

When to use

Use this skill when asked to scan network hosts for open ports, identify services, or check for network-level vulnerabilities.

Prerequisites
Nmap installed (apt install nmap or brew install nmap)
Verify: nmap --version
Important: Only scan hosts you have authorization to test.
Instructions

Identify the target — Confirm the host(s) or network range to scan.

Run the scan:

Service detection:

nmap -sV -sC -oX nmap-results.xml <target>


Full port scan:

nmap -p- -sV -oX nmap-full-results.xml <target>


Vulnerability scripts:

nmap --script=vuln -oX nmap-vuln-results.xml <target>

Quick scan: nmap -F -sV <target>
UDP scan: nmap -sU --top-ports 100 <target>
Specific ports: nmap -p 22,80,443,8080 -sV <target>
Network range: nmap -sn 192.168.1.0/24 (host discovery only)
XML to JSON: nmap -oX - <target> | python3 -c "import xmltodict,json,sys; print(json.dumps(xmltodict.parse(sys.stdin.read())))"

Parse the results — Present findings:

| # | Host | Port | State | Service | Version | Scripts/CVEs |
|---|------|------|-------|---------|---------|-------------|

Summarize — Provide:
Total hosts up, open ports found
Unexpected open ports (attack surface)
Outdated service versions with known CVEs
Recommendations: close unnecessary ports, update services, add firewall rules
Weekly Installs
31
Repository
vchirrav/produc…i-skills
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn