---
title: python-scripting
url: https://skills.sh/89jobrien/steve/python-scripting
---

# python-scripting

skills/89jobrien/steve/python-scripting
python-scripting
Installation
$ npx skills add https://github.com/89jobrien/steve --skill python-scripting
SKILL.md
Python Scripting Skill

Creates self-contained Python scripts using uv and PEP 723 inline script metadata.

What This Skill Does
Creates standalone Python scripts
Uses PEP 723 inline dependencies
Sets up argument parsing
Handles input/output
Configures reproducible builds
When to Use
Standalone utility scripts
One-off automation tasks
Quick data processing
CLI tools
Scripts that need dependencies
Reference Files
references/UV_SCRIPT.template.py - Python script template with PEP 723 metadata
PEP 723 Format
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "requests",
#   "rich",
# ]
# ///

Running Scripts
uv run script.py [args]


Dependencies install automatically on first run.

Best Practices
Use exclude-newer for reproducibility
Include docstring with usage examples
Use argparse for CLI arguments
Return exit codes (0 success, non-zero error)
Keep scripts focused on one task
Weekly Installs
65
Repository
89jobrien/steve
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass