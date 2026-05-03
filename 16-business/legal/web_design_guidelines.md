---
rating: ⭐⭐
title: web-design-guidelines
url: https://skills.sh/langgenius/dify/web-design-guidelines
---

# web-design-guidelines

skills/langgenius/dify/web-design-guidelines
web-design-guidelines
Originally fromvercel-labs/agent-skills
Installation
$ npx skills add https://github.com/langgenius/dify --skill web-design-guidelines
Summary

Audit UI code against Web Interface Guidelines for compliance and best practices.

Fetches the latest guidelines from Vercel Labs before each review to ensure current rule compliance
Accepts file paths or patterns as arguments; prompts for files if none specified
Outputs findings in concise file:line format for quick identification of violations
Covers accessibility, design patterns, and UX best practices as defined in the guidelines repository
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
689
Repository
langgenius/dify
GitHub Stars
139.9K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass