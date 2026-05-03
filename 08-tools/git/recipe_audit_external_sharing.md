---
rating: ⭐⭐
title: recipe-audit-external-sharing
url: https://skills.sh/googleworkspace/cli/recipe-audit-external-sharing
---

# recipe-audit-external-sharing

skills/googleworkspace/cli/recipe-audit-external-sharing
recipe-audit-external-sharing
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-audit-external-sharing
Summary

Audit Google Drive files shared outside your organization and manage external access permissions.

Requires the gws-drive skill to execute; queries Google Drive for files with external sharing enabled
Three core operations: list externally shared files, review permissions on specific files, and revoke access when needed
Includes a safety caution recommending confirmation with file owners before revoking permissions to prevent unintended access loss
SKILL.md
Audit External Drive Sharing

PREREQUISITE: Load the following skills to execute this recipe: gws-drive

Find and review Google Drive files shared outside the organization.

[!CAUTION] Revoking permissions immediately removes access. Confirm with the file owner first.

Steps
List externally shared files: gws drive files list --params '{"q": "visibility = '\''anyoneWithLink'\''"}'
Check permissions on a file: gws drive permissions list --params '{"fileId": "FILE_ID"}'
Revoke if needed: gws drive permissions delete --params '{"fileId": "FILE_ID", "permissionId": "PERM_ID"}'
Weekly Installs
610
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