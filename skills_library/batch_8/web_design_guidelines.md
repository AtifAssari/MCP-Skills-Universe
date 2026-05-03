---
title: web-design-guidelines
url: https://skills.sh/sickn33/antigravity-awesome-skills/web-design-guidelines
---

# web-design-guidelines

skills/sickn33/antigravity-awesome-skills/web-design-guidelines
web-design-guidelines
Originally fromvercel-labs/agent-skills
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill web-design-guidelines
Summary

Audit UI code against Web Interface Guidelines with automated compliance checking.

Fetches the latest guidelines from a remote source before each review, ensuring rules stay current
Accepts file paths or patterns to review, or prompts the user if none are specified
Outputs findings in a concise file:line format for quick issue identification
Covers all rules defined in the fetched guidelines, including design, accessibility, and UX patterns
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

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
531
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn