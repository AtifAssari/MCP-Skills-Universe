---
rating: ⭐⭐
title: feishu-perm
url: https://skills.sh/m1heng/clawdbot-feishu/feishu-perm
---

# feishu-perm

skills/m1heng/clawdbot-feishu/feishu-perm
feishu-perm
Installation
$ npx skills add https://github.com/m1heng/clawdbot-feishu --skill feishu-perm
SKILL.md
Feishu Permission Tool

Single tool feishu_perm for managing file/document permissions.

Actions
List Collaborators
{ "action": "list", "token": "ABC123", "type": "docx" }


Returns: members with member_type, member_id, perm, name.

Add Collaborator
{ "action": "add", "token": "ABC123", "type": "docx", "member_type": "email", "member_id": "user@example.com", "perm": "edit" }

Remove Collaborator
{ "action": "remove", "token": "ABC123", "type": "docx", "member_type": "email", "member_id": "user@example.com" }

Token Types
Type	Description
doc	Old format document
docx	New format document
sheet	Spreadsheet
bitable	Multi-dimensional table
folder	Folder
file	Uploaded file
wiki	Wiki node
mindnote	Mind map
Member Types
Type	Description
email	Email address
openid	User open_id
userid	User user_id
unionid	User union_id
openchat	Group chat open_id
opendepartmentid	Department open_id
Permission Levels
Perm	Description
view	View only
edit	Can edit
full_access	Full access (can manage permissions)
Examples

Share document with email:

{ "action": "add", "token": "doxcnXXX", "type": "docx", "member_type": "email", "member_id": "alice@company.com", "perm": "edit" }


Share folder with group:

{ "action": "add", "token": "fldcnXXX", "type": "folder", "member_type": "openchat", "member_id": "oc_xxx", "perm": "view" }

Configuration
channels:
  feishu:
    tools:
      perm: true  # default: false (disabled)


Note: This tool is disabled by default because permission management is a sensitive operation. Enable explicitly if needed.

Permissions

Required: drive:permission

Weekly Installs
237
Repository
m1heng/clawdbot-feishu
GitHub Stars
4.3K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail