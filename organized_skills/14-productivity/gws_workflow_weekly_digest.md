---
rating: ⭐⭐
title: gws-workflow-weekly-digest
url: https://skills.sh/googleworkspace/cli/gws-workflow-weekly-digest
---

# gws-workflow-weekly-digest

skills/googleworkspace/cli/gws-workflow-weekly-digest
gws-workflow-weekly-digest
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-workflow-weekly-digest
Summary

Weekly summary combining this week's calendar meetings and unread email count.

Aggregates two data sources: upcoming meetings from Google Calendar and unread message count from Gmail
Read-only operation that never modifies any data
Supports multiple output formats: JSON (default), table, YAML, and CSV for flexible integration with other tools
Requires prior authentication setup via the shared gws-shared skill module
SKILL.md
workflow +weekly-digest

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Weekly summary: this week's meetings + unread email count

Usage
gws workflow +weekly-digest

Flags
Flag	Required	Default	Description
--format	—	—	Output format: json (default), table, yaml, csv
Examples
gws workflow +weekly-digest
gws workflow +weekly-digest --format table

Tips
Read-only — never modifies data.
Combines calendar agenda (week) with gmail triage summary.
See Also
gws-shared — Global flags and auth
gws-workflow — All cross-service productivity workflows commands
Weekly Installs
12.0K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass