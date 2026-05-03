---
title: gws-workflow
url: https://skills.sh/googleworkspace/cli/gws-workflow
---

# gws-workflow

skills/googleworkspace/cli/gws-workflow
gws-workflow
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-workflow
Summary

Cross-service productivity workflows connecting Google Workspace apps via CLI commands.

Includes five pre-built helper workflows: standup reports, meeting prep, email-to-task conversion, weekly digests, and file announcements
Requires gws binary and authentication setup from the shared gws-shared skill documentation
Discover available resources and methods with gws workflow --help and inspect method signatures using gws schema workflow.<resource>.<method>
Pass parameters via --params or --json flags based on schema inspection output
SKILL.md
workflow (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws workflow <resource> <method> [flags]

Helper Commands
Command	Description
+standup-report	Today's meetings + open tasks as a standup summary
+meeting-prep	Prepare for your next meeting: agenda, attendees, and linked docs
+email-to-task	Convert a Gmail message into a Google Tasks entry
+weekly-digest	Weekly summary: this week's meetings + unread email count
+file-announce	Announce a Drive file in a Chat space
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws workflow --help

# Inspect a method's required params, types, and defaults
gws schema workflow.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
12.8K
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