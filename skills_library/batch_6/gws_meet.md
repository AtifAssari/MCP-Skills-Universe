---
title: gws-meet
url: https://skills.sh/googleworkspace/cli/gws-meet
---

# gws-meet

skills/googleworkspace/cli/gws-meet
gws-meet
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-meet
Summary

Create, manage, and query Google Meet conferences and meeting spaces via the Google Meet API.

Supports two main resource types: conferenceRecords for accessing meeting history, participants, recordings, and transcripts; spaces for creating and managing meeting spaces
Requires Google Workspace authentication and the gws CLI tool; see shared auth documentation for setup and security rules
Use gws schema to inspect method signatures, required parameters, and data types before constructing API calls
All commands follow the pattern gws meet <resource> <method> [flags] with structured parameter and JSON input support
SKILL.md
meet (v2)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws meet <resource> <method> [flags]

API Resources
conferenceRecords
get — Gets a conference record by conference ID.
list — Lists the conference records. By default, ordered by start time and in descending order.
participants — Operations on the 'participants' resource
recordings — Operations on the 'recordings' resource
smartNotes — Operations on the 'smartNotes' resource
transcripts — Operations on the 'transcripts' resource
spaces
create — Creates a space.
endActiveConference — Ends an active conference (if there's one). For an example, see End active conference.
get — Gets details about a meeting space. For an example, see Get a meeting space.
patch — Updates details about a meeting space. For an example, see Update a meeting space.
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws meet --help

# Inspect a method's required params, types, and defaults
gws schema meet.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
14.9K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass