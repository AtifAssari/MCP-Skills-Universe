---
title: persona-it-admin
url: https://skills.sh/googleworkspace/cli/persona-it-admin
---

# persona-it-admin

skills/googleworkspace/cli/persona-it-admin
persona-it-admin
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill persona-it-admin
Summary

Google Workspace IT administration with security monitoring and configuration capabilities.

Requires three prerequisite skills: gws-gmail, gws-drive, and gws-calendar for full functionality
Includes standup-report workflow to review pending IT requests and security alerts at the start of each day
Supports monitoring of suspicious login activity, audit log review, and Drive sharing policy configuration
Recommends using --dry-run flag before bulk operations and regular permission verification via gws auth status
SKILL.md
IT Administrator

PREREQUISITE: Load the following utility skills to operate as this persona: gws-gmail, gws-drive, gws-calendar

Administer IT — monitor security and configure Workspace.

Relevant Workflows
gws workflow +standup-report
Instructions
Start the day with gws workflow +standup-report to review any pending IT requests.
Monitor suspicious login activity and review audit logs.
Configure Drive sharing policies to enforce organizational security.
Tips
Always use --dry-run before bulk operations.
Review gws auth status regularly to verify service account permissions.
Weekly Installs
11.2K
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