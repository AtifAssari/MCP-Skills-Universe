---
title: cve-research
url: https://skills.sh/fusengine/agents/cve-research
---

# cve-research

skills/fusengine/agents/cve-research
cve-research
Installation
$ npx skills add https://github.com/fusengine/agents --skill cve-research
SKILL.md
CVE Research Skill
Overview

Research known vulnerabilities for project dependencies using multiple sources.

Data Sources
Source	API	Coverage
NVD	nvd.nist.gov/vuln/api	All CVEs
OSV.dev	api.osv.dev	npm, PyPI, Go, crates, Maven
GitHub Advisory	github.com/advisories	npm, pip, composer, cargo
Exa Search	Via MCP	Real-time web search
Workflow
Extract dependencies from project (package.json, etc.)
Query each source for known CVEs
Cross-reference findings across sources
Prioritize by CVSS score and exploitability
Report with fix versions and workarounds
Query Strategy

For each dependency:

Search OSV.dev first (fastest, most accurate for packages)
Cross-check NVD for CVSS scoring
Use Exa for recent advisories not yet in databases
Check GitHub Advisory for maintainer responses
Severity Mapping
CVSS Score	Severity	Action
9.0 - 10.0	CRITICAL	Fix immediately
7.0 - 8.9	HIGH	Fix before merge
4.0 - 6.9	MEDIUM	Plan fix
0.1 - 3.9	LOW	Document
References
CVE APIs Reference
Query Templates
Weekly Installs
39
Repository
fusengine/agents
GitHub Stars
11
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn