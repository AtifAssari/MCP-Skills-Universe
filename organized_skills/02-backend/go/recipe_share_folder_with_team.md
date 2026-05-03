---
rating: ⭐⭐
title: recipe-share-folder-with-team
url: https://skills.sh/googleworkspace/cli/recipe-share-folder-with-team
---

# recipe-share-folder-with-team

skills/googleworkspace/cli/recipe-share-folder-with-team
recipe-share-folder-with-team
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-share-folder-with-team
Summary

Batch-share Google Drive folders with multiple collaborators at specified permission levels.

Requires the gws-drive skill to execute folder sharing and permission management operations
Supports role-based access control: assign editor (writer) or viewer (reader) permissions to individual collaborators
Includes folder discovery by name and permission verification steps to confirm successful sharing
Designed as a multi-step recipe for programmatic team collaboration workflows
SKILL.md
Share a Google Drive Folder with a Team

PREREQUISITE: Load the following skills to execute this recipe: gws-drive

Share a Google Drive folder and all its contents with a list of collaborators.

Steps
Find the folder: gws drive files list --params '{"q": "name = '\''Project X'\'' and mimeType = '\''application/vnd.google-apps.folder'\''"}'
Share as editor: gws drive permissions create --params '{"fileId": "FOLDER_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "colleague@company.com"}'
Share as viewer: gws drive permissions create --params '{"fileId": "FOLDER_ID"}' --json '{"role": "reader", "type": "user", "emailAddress": "stakeholder@company.com"}'
Verify permissions: gws drive permissions list --params '{"fileId": "FOLDER_ID"}' --format table
Weekly Installs
11.0K
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