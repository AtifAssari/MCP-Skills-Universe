---
title: gws-events-renew
url: https://skills.sh/googleworkspace/cli/gws-events-renew
---

# gws-events-renew

skills/googleworkspace/cli/gws-events-renew
gws-events-renew
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-events-renew
Summary

Renew or reactivate Google Workspace Events subscriptions before expiration.

Renew individual subscriptions by name or bulk-renew all subscriptions expiring within a specified time window
Supports flexible time windows (e.g., 1h, 30m, 2d) for batch renewal operations
Designed for automation via cron jobs to maintain continuous subscription activity
Requires Google Workspace authentication and the gws CLI tool with shared skill dependencies
SKILL.md
events +renew

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

Renew/reactivate Workspace Events subscriptions

Usage
gws events +renew

Flags
Flag	Required	Default	Description
--name	—	—	Subscription name to reactivate (e.g., subscriptions/SUB_ID)
--all	—	—	Renew all subscriptions expiring within --within window
--within	—	1h	Time window for --all (e.g., 1h, 30m, 2d)
Examples
gws events +renew --name subscriptions/SUB_ID
gws events +renew --all --within 2d

Tips
Subscriptions expire if not renewed periodically.
Use --all with a cron job to keep subscriptions alive.
See Also
gws-shared — Global flags and auth
gws-events — All subscribe to google workspace events commands
Weekly Installs
11.5K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass