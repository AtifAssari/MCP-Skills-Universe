---
rating: ⭐⭐
title: recipe-triage-security-alerts
url: https://skills.sh/googleworkspace/cli/recipe-triage-security-alerts
---

# recipe-triage-security-alerts

skills/googleworkspace/cli/recipe-triage-security-alerts
recipe-triage-security-alerts
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-triage-security-alerts
Summary

Triage and review Google Workspace security alerts from Alert Center.

Lists active security alerts with table formatting for quick overview
Retrieves detailed information for specific alerts by ID
Acknowledges alerts to mark them as reviewed or resolved
Requires the gws-alertcenter skill as a prerequisite
SKILL.md
Triage Google Workspace Security Alerts

PREREQUISITE: Load the following skills to execute this recipe: gws-alertcenter

List and review Google Workspace security alerts from Alert Center.

Steps
List active alerts: gws alertcenter alerts list --format table
Get alert details: gws alertcenter alerts get --params '{"alertId": "ALERT_ID"}'
Acknowledge an alert: gws alertcenter alerts undelete --params '{"alertId": "ALERT_ID"}'
Weekly Installs
590
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass