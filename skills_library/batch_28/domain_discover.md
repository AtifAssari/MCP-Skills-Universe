---
title: domain-discover
url: https://skills.sh/delexw/claude-code-misc/domain-discover
---

# domain-discover

skills/delexw/claude-code-misc/domain-discover
domain-discover
Installation
$ npx skills add https://github.com/delexw/claude-code-misc --skill domain-discover
SKILL.md
Discover Domain Knowledge

You are tasked with creating a comprehensive domain knowledge file for a codebase that will help future Claude Code instances work effectively with this repository.

Inputs

Raw arguments: $ARGUMENTS

Infer from the arguments:

DOMAIN_NAME: the domain name, used as the output filename
OUT_DIR: output directory, or . (project root) if not provided
Output Location
Creates or updates OUT_DIR/{DOMAIN_NAME}.md
Run mkdir -p OUT_DIR before writing to ensure the directory exists.
Objective

Analyze the provided codebase and create or update a {DOMAIN}.md file containing essential information for productive development.

Analysis Approach
First, scan the repository structure to understand the project type and technology stack
Read key configuration files (package.json, requirements.txt, Makefile, etc.) to identify build/test commands
Examine main application files to understand the high-level architecture
Review existing documentation (README.md, docs/) for important context
Execution

Follow references/rules.md for content requirements, guidelines, and safety rules. Use references/output-format.md for the output template and validation criteria.

Weekly Installs
47
Repository
delexw/claude-code-misc
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass