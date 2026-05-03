---
title: gws-keep
url: https://skills.sh/googleworkspace/cli/gws-keep
---

# gws-keep

skills/googleworkspace/cli/gws-keep
gws-keep
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-keep
Summary

Create, retrieve, list, delete, and manage permissions for Google Keep notes via CLI.

Supports five core note operations: create, get, list, delete, and manage permissions on notes
List command includes pagination support with page_token and page_size parameters for handling large note collections
Download attachments from notes using the media resource with MIME type specification
Requires Google Workspace authentication via the shared gws CLI tool; inspect command schemas with gws schema before execution
SKILL.md
keep (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws keep <resource> <method> [flags]

API Resources
media
download — Gets an attachment. To download attachment media via REST requires the alt=media query parameter. Returns a 400 bad request error if attachment media is not available in the requested MIME type.
notes
create — Creates a new note.
delete — Deletes a note. Caller must have the OWNER role on the note to delete. Deleting a note removes the resource immediately and cannot be undone. Any collaborators will lose access to the note.
get — Gets a note.
list — Lists notes. Every list call returns a page of results with page_size as the upper bound of returned items. A page_size of zero allows the server to choose the upper bound. The ListNotesResponse contains at most page_size entries. If there are more things left to list, it provides a next_page_token value. (Page tokens are opaque values.) To get the next page of results, copy the result's next_page_token into the next request's page_token.
permissions — Operations on the 'permissions' resource
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws keep --help

# Inspect a method's required params, types, and defaults
gws schema keep.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
13.9K
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