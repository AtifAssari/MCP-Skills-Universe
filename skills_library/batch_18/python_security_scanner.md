---
title: python-security-scanner
url: https://skills.sh/jorgealves/agent_skills/python-security-scanner
---

# python-security-scanner

skills/jorgealves/agent_skills/python-security-scanner
python-security-scanner
Installation
$ npx skills add https://github.com/jorgealves/agent_skills --skill python-security-scanner
SKILL.md
Python Security Scanner
Purpose and Intent

Detect common Python vulnerabilities such as SQL injection, unsafe deserialization, and hardcoded secrets. Use as part of a secure SDLC for Python projects.

When to Use
Project Setup: When initializing a new Python project.
Continuous Integration: As part of automated build and test pipelines.
Legacy Refactoring: When updating older Python codebases to modern standards.
When NOT to Use
Non-Python Projects: This tool is specialized for the Python ecosystem.
Error Conditions and Edge Cases
Missing Requirements: If the project lacks a requirements.txt or pyproject.toml.
Incompatible Versions: If the project uses a Python version not supported by the tools.
Security and Data-Handling Considerations
All analysis is performed locally.
No source code or credentials are ever transmitted externally.
Weekly Installs
169
Repository
jorgealves/agent_skills
GitHub Stars
1
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass