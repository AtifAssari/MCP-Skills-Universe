---
rating: ⭐⭐
title: recipe-find-large-files
url: https://skills.sh/googleworkspace/cli/recipe-find-large-files
---

# recipe-find-large-files

skills/googleworkspace/cli/recipe-find-large-files
recipe-find-large-files
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-find-large-files
Summary

Identify large Google Drive files consuming storage quota.

Lists files sorted by size in descending order to quickly spot storage hogs
Returns file metadata including ID, name, size, MIME type, and owners for informed deletion or archival decisions
Requires the gws-drive skill to be loaded before execution
SKILL.md
Find Largest Files in Drive

PREREQUISITE: Load the following skills to execute this recipe: gws-drive

Identify large Google Drive files consuming storage quota.

Steps
List files sorted by size: gws drive files list --params '{"orderBy": "quotaBytesUsed desc", "pageSize": 20, "fields": "files(id,name,size,mimeType,owners)"}' --format table
Review the output and identify files to archive or move
Weekly Installs
11.3K
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