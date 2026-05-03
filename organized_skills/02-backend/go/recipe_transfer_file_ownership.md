---
rating: ⭐⭐
title: recipe-transfer-file-ownership
url: https://skills.sh/googleworkspace/cli/recipe-transfer-file-ownership
---

# recipe-transfer-file-ownership

skills/googleworkspace/cli/recipe-transfer-file-ownership
recipe-transfer-file-ownership
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-transfer-file-ownership
Summary

Transfer ownership of Google Drive files between users with a two-step workflow.

Requires the gws-drive skill and gws binary to execute
Lists files owned by a specific user, then transfers ownership to a new owner via the Google Drive permissions API
Ownership transfer is irreversible without the new owner's cooperation
SKILL.md
Transfer File Ownership

PREREQUISITE: Load the following skills to execute this recipe: gws-drive

Transfer ownership of Google Drive files from one user to another.

[!CAUTION] Transferring ownership is irreversible without the new owner's cooperation.

Steps
List files owned by the user: gws drive files list --params '{"q": "'\''user@company.com'\'' in owners"}'
Transfer ownership: gws drive permissions create --params '{"fileId": "FILE_ID", "transferOwnership": true}' --json '{"role": "owner", "type": "user", "emailAddress": "newowner@company.com"}'
Weekly Installs
589
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