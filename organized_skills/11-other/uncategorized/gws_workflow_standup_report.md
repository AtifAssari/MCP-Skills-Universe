---
rating: ⭐⭐
title: gws-workflow-standup-report
url: https://skills.sh/googleworkspace/cli/gws-workflow-standup-report
---

# gws-workflow-standup-report

skills/googleworkspace/cli/gws-workflow-standup-report
gws-workflow-standup-report
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-workflow-standup-report
Summary

Aggregates today's calendar meetings and open tasks into a single standup summary.

Combines Google Calendar agenda with task list data for a unified daily briefing
Supports multiple output formats: JSON (default), table, YAML, and CSV
Read-only operation that never modifies calendar or task data
Requires gws binary and authentication setup from the shared skill module
SKILL.md
workflow +standup-report

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Today's meetings + open tasks as a standup summary

Usage
gws workflow +standup-report

Flags
Flag	Required	Default	Description
--format	—	—	Output format: json (default), table, yaml, csv
Examples
gws workflow +standup-report
gws workflow +standup-report --format table

Tips
Read-only — never modifies data.
Combines calendar agenda (today) with tasks list.
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