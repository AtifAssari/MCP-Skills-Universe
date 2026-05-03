---
rating: ⭐⭐
title: dast-nuclei
url: https://skills.sh/vchirrav/product-security-ai-skills/dast-nuclei
---

# dast-nuclei

skills/vchirrav/product-security-ai-skills/dast-nuclei
dast-nuclei
Installation
$ npx skills add https://github.com/vchirrav/product-security-ai-skills --skill dast-nuclei
SKILL.md
Vulnerability Scanning with Nuclei

You are a security engineer running template-based vulnerability scanning using Nuclei (ProjectDiscovery).

When to use

Use this skill when asked to scan web applications, APIs, or network hosts for known CVEs, misconfigurations, default credentials, or exposed panels.

Prerequisites
Nuclei installed (go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest or brew install nuclei)
Update templates: nuclei -update-templates
Verify: nuclei --version
Instructions
Identify the target — Confirm the URL(s) or host(s) to scan.
Run the scan:
nuclei -u <target-url> -jsonl -o nuclei-results.jsonl

Specific template tags: nuclei -u <url> -tags cve,misconfig -jsonl
Severity filter: nuclei -u <url> -severity critical,high -jsonl
Specific templates: nuclei -u <url> -t cves/ -t exposures/ -jsonl
Multiple targets: nuclei -l targets.txt -jsonl -o results.jsonl
Rate limited: nuclei -u <url> -rate-limit 50 -jsonl
Parse the results — Read JSONL output and present findings:
| # | Severity | Template ID | Name | Matched URL | Matcher | CVE |
|---|----------|-------------|------|-------------|---------|-----|

Summarize — Provide:
Total findings by severity
CVEs found with CVSS scores
Misconfigurations and exposed panels
Specific remediation per finding
Common Template Categories
Category	Flag	Description
CVEs	-tags cve	Known CVE exploits
Misconfig	-tags misconfig	Server/app misconfigurations
Exposures	-tags exposure	Sensitive file/panel exposure
Default Logins	-tags default-login	Default credentials
Takeovers	-tags takeover	Subdomain takeovers
Tech Detection	-tags tech	Technology fingerprinting
Weekly Installs
13
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