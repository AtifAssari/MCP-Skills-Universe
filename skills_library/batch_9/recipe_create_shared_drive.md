---
title: recipe-create-shared-drive
url: https://skills.sh/googleworkspace/cli/recipe-create-shared-drive
---

# recipe-create-shared-drive

skills/googleworkspace/cli/recipe-create-shared-drive
recipe-create-shared-drive
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-shared-drive
Summary

Create a Google Shared Drive and manage member access with role-based permissions.

Requires the gws-drive skill and gws binary to execute
Supports three core operations: creating shared drives, adding members with specific roles (writer, reader, etc.), and listing current members
Uses Google Workspace API parameters for drive ID and permission management across shared drive resources
SKILL.md
Create and Configure a Shared Drive

PREREQUISITE: Load the following skills to execute this recipe: gws-drive

Create a Google Shared Drive and add members with appropriate roles.

Steps
Create shared drive: gws drive drives create --params '{"requestId": "unique-id-123"}' --json '{"name": "Project X"}'
Add a member: gws drive permissions create --params '{"fileId": "DRIVE_ID", "supportsAllDrives": true}' --json '{"role": "writer", "type": "user", "emailAddress": "member@company.com"}'
List members: gws drive permissions list --params '{"fileId": "DRIVE_ID", "supportsAllDrives": true}'
Weekly Installs
11.4K
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