---
title: analyzing-powershell-script-block-logging
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-powershell-script-block-logging
---

# analyzing-powershell-script-block-logging

skills/mukul975/anthropic-cybersecurity-skills/analyzing-powershell-script-block-logging
analyzing-powershell-script-block-logging
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-powershell-script-block-logging
SKILL.md
Analyzing PowerShell Script Block Logging
When to Use
When investigating security incidents that require analyzing powershell script block logging
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Familiarity with security operations concepts and tools
Access to a test or lab environment for safe execution
Python 3.8+ with required dependencies installed
Appropriate authorization for any testing activities
Instructions
Install dependencies: pip install python-evtx lxml
Collect PowerShell Operational logs: Microsoft-Windows-PowerShell%4Operational.evtx
Parse Event ID 4104 entries using python-evtx to extract ScriptBlockText, ScriptBlockId, and MessageNumber/MessageTotal for multi-part script reconstruction.
Apply detection heuristics:
Base64-encoded commands (-EncodedCommand, FromBase64String)
Download cradles (DownloadString, DownloadFile, Invoke-WebRequest, Net.WebClient)
AMSI bypass patterns (AmsiUtils, amsiInitFailed)
Obfuscation indicators (high entropy, tick-mark insertion, string concatenation)
Generate a report with reconstructed scripts, risk scores, and MITRE ATT&CK mappings.
python scripts/agent.py --evtx-file /path/to/PowerShell-Operational.evtx --output ps_analysis.json

Examples
Detect Encoded Command Execution
import base64
if "-encodedcommand" in script_text.lower():
    encoded = script_text.split()[-1]
    decoded = base64.b64decode(encoded).decode("utf-16-le")

Reconstruct Multi-Block Script

Scripts split across multiple 4104 events share a ScriptBlockId. Concatenate blocks ordered by MessageNumber to recover the full script.

Weekly Installs
45
Repository
mukul975/anthro…y-skills
GitHub Stars
5.9K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass