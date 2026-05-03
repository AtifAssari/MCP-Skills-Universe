---
title: feishu-drive
url: https://skills.sh/m1heng/clawdbot-feishu/feishu-drive
---

# feishu-drive

skills/m1heng/clawdbot-feishu/feishu-drive
feishu-drive
Installation
$ npx skills add https://github.com/m1heng/clawdbot-feishu --skill feishu-drive
Summary

Feishu cloud storage file management with folder browsing, file operations, and token-based access.

Supports five core actions: list folder contents, get file info, create folders, move files, and delete files
Handles eight file types including documents, spreadsheets, multi-dimensional tables, mind maps, and uploaded files
Requires folder or file tokens extracted from Feishu URLs; bots can only access shared folders, not root directory
Two permission levels available: full access (create, move, delete) or read-only (list, info)
SKILL.md
Feishu Drive Tool

Single tool feishu_drive for cloud storage operations.

Token Extraction

From URL https://xxx.feishu.cn/drive/folder/ABC123 → folder_token = ABC123

Actions
List Folder Contents
{ "action": "list" }


Root directory (no folder_token).

{ "action": "list", "folder_token": "fldcnXXX" }


Returns: files with token, name, type, url, timestamps.

Get File Info
{ "action": "info", "file_token": "ABC123", "type": "docx" }


Searches for the file in the root directory. Note: file must be in root or use list to browse folders first.

type: doc, docx, sheet, bitable, folder, file, mindnote, shortcut

Create Folder
{ "action": "create_folder", "name": "New Folder" }


In parent folder:

{ "action": "create_folder", "name": "New Folder", "folder_token": "fldcnXXX" }

Move File
{ "action": "move", "file_token": "ABC123", "type": "docx", "folder_token": "fldcnXXX" }

Delete File
{ "action": "delete", "file_token": "ABC123", "type": "docx" }

File Types
Type	Description
doc	Old format document
docx	New format document
sheet	Spreadsheet
bitable	Multi-dimensional table
folder	Folder
file	Uploaded file
mindnote	Mind map
shortcut	Shortcut
Configuration
channels:
  feishu:
    tools:
      drive: true  # default: true

Permissions
drive:drive - Full access (create, move, delete)
drive:drive:readonly - Read only (list, info)
Known Limitations
Bots have no root folder: Feishu bots use tenant_access_token and don't have their own "My Space". The root folder concept only exists for user accounts. This means:
create_folder without folder_token will fail (400 error)
Bot can only access files/folders that have been shared with it
Workaround: User must first create a folder manually and share it with the bot, then bot can create subfolders inside it
Weekly Installs
834
Repository
m1heng/clawdbot-feishu
GitHub Stars
4.3K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass