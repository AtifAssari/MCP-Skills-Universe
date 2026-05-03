---
rating: ⭐⭐⭐
title: skill-scanner
url: https://skills.sh/bvinci1-design/skill-scanner/skill-scanner
---

# skill-scanner

skills/bvinci1-design/skill-scanner/skill-scanner
skill-scanner
Installation
$ npx skills add https://github.com/bvinci1-design/skill-scanner --skill skill-scanner
SKILL.md
Skill Scanner

Security audit tool for Clawdbot/MCP skills - scans for malware, spyware, crypto-mining, and malicious patterns.

Capabilities
Scan skill folders for security threats
Detect data exfiltration patterns
Identify system modification attempts
Catch crypto-mining indicators
Flag arbitrary code execution risks
Find backdoors and obfuscation techniques
Output reports in Markdown or JSON format
Provide Web UI via Streamlit
Usage
Command Line
python skill_scanner.py /path/to/skill-folder

Within Clawdbot
"Scan the [skill-name] skill for security issues using skill-scanner"
"Use skill-scanner to check the youtube-watcher skill"
"Run a security audit on the remotion skill"

Web UI
pip install streamlit
streamlit run streamlit_ui.py

Requirements
Python 3.7+
No additional dependencies (uses Python standard library)
Streamlit (optional, for Web UI)
Entry Point
CLI: skill_scanner.py
Web UI: streamlit_ui.py
Tags

#security #malware #spyware #crypto-mining #scanner #audit #code-analysis #mcp #clawdbot #agent-skills #safety #threat-detection #vulnerability

Weekly Installs
70
Repository
bvinci1-design/…-scanner
GitHub Stars
1
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass