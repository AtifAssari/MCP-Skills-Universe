---
title: gws-slides
url: https://skills.sh/googleworkspace/cli/gws-slides
---

# gws-slides

skills/googleworkspace/cli/gws-slides
gws-slides
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-slides
Summary

Read, write, and batch-update Google Slides presentations programmatically.

Supports core presentation operations: create blank presentations, retrieve presentation data, and apply batch updates to multiple elements in a single validated request
All updates are atomic; if any request in a batch is invalid, the entire operation fails and nothing is applied
Use gws schema to inspect method signatures, required parameters, and data types before constructing API calls
Requires Google Workspace authentication and the gws binary; see shared auth documentation for security rules and global flags
SKILL.md
slides (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws slides <resource> <method> [flags]

API Resources
presentations
batchUpdate — Applies one or more updates to the presentation. Each request is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests.
create — Creates a blank presentation using the title given in the request. If a presentationId is provided, it is used as the ID of the new presentation. Otherwise, a new ID is generated. Other fields in the request, including any provided content, are ignored. Returns the created presentation.
get — Gets the latest version of the specified presentation.
pages — Operations on the 'pages' resource
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws slides --help

# Inspect a method's required params, types, and defaults
gws schema slides.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
16.9K
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