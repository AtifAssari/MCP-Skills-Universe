---
rating: ⭐⭐
title: design-web-guidelines
url: https://skills.sh/baotoq/agent-skills/design-web-guidelines
---

# design-web-guidelines

skills/baotoq/agent-skills/design-web-guidelines
design-web-guidelines
Installation
$ npx skills add https://github.com/baotoq/agent-skills --skill design-web-guidelines
SKILL.md
Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

How It Works
Fetch the latest guidelines from the source URL below
Read the specified files (or prompt user for files/pattern)
Check against all rules in the fetched guidelines
Output findings in the terse file:line format
Guidelines Source

Fetch fresh guidelines before each review:

https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md


Use WebFetch to retrieve the latest rules. The fetched content contains all the rules and output format instructions.

Usage

When a user provides a file or pattern argument:

Fetch guidelines from the source URL above
Read the specified files
Apply all rules from the fetched guidelines
Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.

Weekly Installs
8
Repository
baotoq/agent-skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn