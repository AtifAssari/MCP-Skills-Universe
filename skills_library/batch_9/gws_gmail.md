---
title: gws-gmail
url: https://skills.sh/googleworkspace/cli/gws-gmail
---

# gws-gmail

skills/googleworkspace/cli/gws-gmail
gws-gmail
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-gmail
Summary

Send, read, and manage Gmail messages, drafts, labels, and account settings.

Seven helper commands cover common workflows: send, triage unread messages, reply, reply-all, forward, read message bodies, and watch for new emails in real-time
Full Gmail API access via users resource with methods for profiles, drafts, history, labels, messages, settings, threads, and push notifications
Use gws schema to inspect method signatures and required parameters before building CLI calls with --params and --json flags
Requires gws binary and authentication setup documented in gws-shared/SKILL.md
SKILL.md
gmail (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws gmail <resource> <method> [flags]

Helper Commands
Command	Description
+send	Send an email
+triage	Show unread inbox summary (sender, subject, date)
+reply	Reply to a message (handles threading automatically)
+reply-all	Reply-all to a message (handles threading automatically)
+forward	Forward a message to new recipients
+read	Read a message and extract its body or headers
+watch	Watch for new emails and stream them as NDJSON
API Resources
users
getProfile — Gets the current user's Gmail profile.
stop — Stop receiving push notifications for the given user mailbox.
watch — Set up or update a push notification watch on the given user mailbox.
drafts — Operations on the 'drafts' resource
history — Operations on the 'history' resource
labels — Operations on the 'labels' resource
messages — Operations on the 'messages' resource
settings — Operations on the 'settings' resource
threads — Operations on the 'threads' resource
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws gmail --help

# Inspect a method's required params, types, and defaults
gws schema gmail.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
23.6K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn