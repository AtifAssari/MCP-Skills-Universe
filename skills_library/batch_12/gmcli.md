---
title: gmcli
url: https://skills.sh/badlogic/pi-skills/gmcli
---

# gmcli

skills/badlogic/pi-skills/gmcli
gmcli
Installation
$ npx skills add https://github.com/badlogic/pi-skills --skill gmcli
SKILL.md
Gmail CLI

Command-line interface for Gmail operations.

Installation
npm install -g @mariozechner/gmcli

Setup
Google Cloud Console (one-time)
Create a new project (or select existing)
Enable the Gmail API
Set app name in OAuth branding
Add test users (all Gmail addresses you want to use)
Create OAuth client:
Click "Create Client"
Application type: "Desktop app"
Download the JSON file
Configure gmcli

First check if already configured:

gmcli accounts list


If no accounts, guide the user through setup:

Ask if they have a Google Cloud project with Gmail API enabled
If not, walk them through the Google Cloud Console steps above
Have them download the OAuth credentials JSON
Run: gmcli accounts credentials ~/path/to/credentials.json
Run: gmcli accounts add <email> (use --manual for browserless OAuth)
Usage

Run gmcli --help for full command reference.

Common operations:

gmcli <email> search "<query>" - Search emails using Gmail query syntax
gmcli <email> thread <threadId> - Read a thread with all messages
gmcli <email> send --to <emails> --subject <s> --body <b> - Send email
gmcli <email> labels list - List all labels
gmcli <email> drafts list - List drafts
Data Storage
~/.gmcli/credentials.json - OAuth client credentials
~/.gmcli/accounts.json - Account tokens
~/.gmcli/attachments/ - Downloaded attachments
Weekly Installs
65
Repository
badlogic/pi-skills
GitHub Stars
1.5K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn