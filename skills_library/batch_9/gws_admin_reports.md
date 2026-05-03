---
title: gws-admin-reports
url: https://skills.sh/googleworkspace/cli/gws-admin-reports
---

# gws-admin-reports

skills/googleworkspace/cli/gws-admin-reports
gws-admin-reports
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-admin-reports
Summary

Query Google Workspace audit logs, activity feeds, and usage reports across customers and users.

Access five resource types: activities (with list and watch for push notifications), channels, customer usage reports, entity usage reports, and user usage reports
Retrieve audit logs for specific applications, customer account statistics, and per-user activity and usage metrics
Requires Google Workspace Admin SDK authentication; see shared gws documentation for auth setup and security rules
Use gws schema to inspect required parameters and data types before constructing API calls
SKILL.md
admin-reports (reports_v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws admin-reports <resource> <method> [flags]

API Resources
activities
list — Retrieves a list of activities for a specific customer's account and application such as the Admin console application or the Google Drive application. For more information, see the guides for administrator and Google Drive activity reports. For more information about the activity report's parameters, see the activity parameters reference guides.
watch — Start receiving notifications for account activities. For more information, see Receiving Push Notifications.
channels
stop — Stop watching resources through this channel.
customerUsageReports
get — Retrieves a report which is a collection of properties and statistics for a specific customer's account. For more information, see the Customers Usage Report guide. For more information about the customer report's parameters, see the Customers Usage parameters reference guides.
entityUsageReports
get — Retrieves a report which is a collection of properties and statistics for entities used by users within the account. For more information, see the Entities Usage Report guide. For more information about the entities report's parameters, see the Entities Usage parameters reference guides.
userUsageReport
get — Retrieves a report which is a collection of properties and statistics for a set of users with the account. For more information, see the User Usage Report guide. For more information about the user report's parameters, see the Users Usage parameters reference guides.
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws admin-reports --help

# Inspect a method's required params, types, and defaults
gws schema admin-reports.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
11.4K
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