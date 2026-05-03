---
title: feishu
url: https://skills.sh/tzwm/feishu-skill/feishu
---

# feishu

skills/tzwm/feishu-skill/feishu
feishu
Installation
$ npx skills add https://github.com/tzwm/feishu-skill --skill feishu
SKILL.md
Feishu Skill

A skill for interacting with the Feishu (Lark) API for advanced management of Documents, Wiki, Drive, and Permissions.

Setup

First time setup:

cd skills/feishu
pnpm install


Requires the following environment variables to be set in your terminal or .env:

LARK_APP_ID
LARK_APP_SECRET
Usage

Use the pnpm start command with various subcommands.

Documents (doc)

Read document:

cd skills/feishu
pnpm start doc read -t <doc_token_or_url>


Write to document (replaces all content with Markdown):

pnpm start doc write -t <doc_token> --content "# Title\nNew content"


List comments on a document:

pnpm start doc list-comments -t <doc_token>

Wiki (wiki)

List accessible wiki spaces:

cd skills/feishu
pnpm start wiki spaces


Get details of a Wiki node (returns underlying obj_token for docs):

pnpm start wiki get -t <wiki_token_or_url>

Drive (drive)

List folder contents:

cd skills/feishu
pnpm start drive list -f <folder_token>

Permissions (perm)

List collaborators:

cd skills/feishu
pnpm start perm list -t <file_token> --type docx

IM (instant message)

List messages from a chat or thread:

cd skills/feishu
pnpm start im messages -c <chat_id>


Use --help on any command for more options:

pnpm start im --help

Weekly Installs
18
Repository
tzwm/feishu-skill
GitHub Stars
3
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn