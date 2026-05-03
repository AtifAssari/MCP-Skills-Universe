---
rating: ⭐⭐
title: analyzing-powershell-empire-artifacts
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-powershell-empire-artifacts
---

# analyzing-powershell-empire-artifacts

skills/mukul975/anthropic-cybersecurity-skills/analyzing-powershell-empire-artifacts
analyzing-powershell-empire-artifacts
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-powershell-empire-artifacts
SKILL.md
Analyzing PowerShell Empire Artifacts
Overview

PowerShell Empire is a post-exploitation framework consisting of listeners, stagers, and agents. Its artifacts leave detectable traces in Windows event logs, particularly PowerShell Script Block Logging (Event ID 4104) and Module Logging (Event ID 4103). This skill analyzes event logs for Empire's default launcher string (powershell -noP -sta -w 1 -enc), Base64 encoded payloads containing System.Net.WebClient and FromBase64String, known module invocations (Invoke-Mimikatz, Invoke-Kerberoast, Invoke-TokenManipulation), and staging URL patterns.

When to Use
When investigating security incidents that require analyzing powershell empire artifacts
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Python 3.9+ with access to Windows Event Log or exported EVTX files
PowerShell Script Block Logging (Event ID 4104) enabled via Group Policy
Module Logging (Event ID 4103) enabled for comprehensive coverage
Key Detection Patterns
Default launcher — powershell -noP -sta -w 1 -enc followed by Base64 blob
Stager indicators — System.Net.WebClient, DownloadData, DownloadString, FromBase64String
Module signatures — Invoke-Mimikatz, Invoke-Kerberoast, Invoke-TokenManipulation, Invoke-PSInject, Invoke-DCOM
User agent strings — default Empire user agents in HTTP listener configuration
Staging URLs — /login/process.php, /admin/get.php and similar default URI patterns
Output

JSON report with matched IOCs, decoded Base64 payloads, timeline of suspicious events, MITRE ATT&CK technique mappings, and severity scores.

Weekly Installs
40
Repository
mukul975/anthro…y-skills
GitHub Stars
5.9K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail