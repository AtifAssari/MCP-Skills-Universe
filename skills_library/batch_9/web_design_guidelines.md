---
title: web-design-guidelines
url: https://skills.sh/vercel-labs/agent-skills/web-design-guidelines
---

# web-design-guidelines

skills/vercel-labs/agent-skills/web-design-guidelines
web-design-guidelines
Installation
$ npx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines
Summary

Audit UI code against Vercel's Web Interface Guidelines for design and accessibility compliance.

Fetches the latest guidelines from a remote source before each review, ensuring rules stay current
Accepts file paths or patterns as arguments; prompts for files if none provided
Outputs findings in a terse file:line format for quick scanning and remediation
Covers design, accessibility, and UX best practices as defined in the guidelines repository
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
291.8K
Repository
vercel-labs/agent-skills
GitHub Stars
26.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn