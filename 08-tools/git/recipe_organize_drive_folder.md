---
rating: ⭐⭐
title: recipe-organize-drive-folder
url: https://skills.sh/googleworkspace/cli/recipe-organize-drive-folder
---

# recipe-organize-drive-folder

skills/googleworkspace/cli/recipe-organize-drive-folder
recipe-organize-drive-folder
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-organize-drive-folder
Summary

Automate Google Drive folder creation and file organization into structured hierarchies.

Creates nested folder structures and moves existing files into designated locations using gws-drive commands
Supports parent-child folder relationships and file reparenting across Drive locations
Includes verification steps to list and confirm folder contents after organization
SKILL.md
Organize Files into Google Drive Folders

PREREQUISITE: Load the following skills to execute this recipe: gws-drive

Create a Google Drive folder structure and move files into the right locations.

Steps
Create a project folder: gws drive files create --json '{"name": "Q2 Project", "mimeType": "application/vnd.google-apps.folder"}'
Create sub-folders: gws drive files create --json '{"name": "Documents", "mimeType": "application/vnd.google-apps.folder", "parents": ["PARENT_FOLDER_ID"]}'
Move existing files into folder: gws drive files update --params '{"fileId": "FILE_ID", "addParents": "FOLDER_ID", "removeParents": "OLD_PARENT_ID"}'
Verify structure: gws drive files list --params '{"q": "FOLDER_ID in parents"}' --format table
Weekly Installs
11.6K
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