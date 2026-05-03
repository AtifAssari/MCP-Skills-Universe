---
title: repo-maintenance
url: https://skills.sh/igorwarzocha/opencode-workflows/repo-maintenance
---

# repo-maintenance

skills/igorwarzocha/opencode-workflows/repo-maintenance
repo-maintenance
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill repo-maintenance
SKILL.md
Repository Maintenance Skill

This skill provides the tools to act as a Repo Custodian.

Validate Repository

Ensure configuration files (agents, commands, skills) are valid.

Command: python3 .opencode/skill/repo-maintenance/scripts/audit_repo.py
Sync Documentation

Report on repository inventory and suggest whether docs need updating.

Command: python3 .opencode/skill/repo-maintenance/scripts/sync_docs.py
After a Failed Audit

When the audit reports errors or warnings:

Read affected files - MUST read each file listed in the output
Analyze issues - Understand what changes would fix each issue
Ask the user - MUST use question tool to confirm which fixes to apply
Apply selectively - Only fix what the user approves

MUST NOT auto-fix all issues. Mass changes can break working configurations.

Standards

Refer to references/validation-rules.md for:

YAML Frontmatter Schema
Description patterns (agents, commands, skills)
RFC+XML compliance requirements
Post-audit workflow details
Weekly Installs
43
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass