---
title: recipe-bulk-download-folder
url: https://skills.sh/googleworkspace/cli/recipe-bulk-download-folder
---

# recipe-bulk-download-folder

skills/googleworkspace/cli/recipe-bulk-download-folder
recipe-bulk-download-folder
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-bulk-download-folder
Summary

Bulk download all files from a Google Drive folder with automatic format conversion.

Requires the gws-drive skill and gws binary to execute
Lists folder contents by querying parent folder ID, then downloads each file individually
Supports exporting Google Docs and Sheets as PDF or other formats during download
Workflow: query folder, iterate through results, download or export each file to local storage
SKILL.md
Bulk Download Drive Folder

PREREQUISITE: Load the following skills to execute this recipe: gws-drive

List and download all files from a Google Drive folder.

Steps
List files in folder: gws drive files list --params '{"q": "'\''FOLDER_ID'\'' in parents"}' --format json
Download each file: gws drive files get --params '{"fileId": "FILE_ID", "alt": "media"}' -o filename.ext
Export Google Docs as PDF: gws drive files export --params '{"fileId": "FILE_ID", "mimeType": "application/pdf"}' -o document.pdf
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
SnykWarn