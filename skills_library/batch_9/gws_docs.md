---
title: gws-docs
url: https://skills.sh/googleworkspace/cli/gws-docs
---

# gws-docs

skills/googleworkspace/cli/gws-docs
gws-docs
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-docs
Summary

Read and write Google Docs through the Google Workspace API.

Supports three core operations: create (new blank documents), get (retrieve document content), and batchUpdate (apply multiple validated updates in a single request)
Uses a schema-driven CLI with gws schema inspection to discover required parameters, types, and defaults before executing commands
Requires Google Workspace authentication and shared security rules documented in gws-shared/SKILL.md
Includes a helper command +write for appending text to documents as a convenience wrapper
SKILL.md
docs (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws docs <resource> <method> [flags]

Helper Commands
Command	Description
+write	Append text to a document
API Resources
documents
batchUpdate — Applies one or more updates to the document. Each request is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests.
create — Creates a blank document using the title given in the request. Other fields in the request, including any provided content, are ignored. Returns the created document.
get — Gets the latest version of the specified document.
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws docs --help

# Inspect a method's required params, types, and defaults
gws schema docs.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
23.4K
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