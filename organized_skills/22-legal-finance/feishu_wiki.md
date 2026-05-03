---
rating: ⭐⭐⭐
title: feishu-wiki
url: https://skills.sh/m1heng/clawdbot-feishu/feishu-wiki
---

# feishu-wiki

skills/m1heng/clawdbot-feishu/feishu-wiki
feishu-wiki
Installation
$ npx skills add https://github.com/m1heng/clawdbot-feishu --skill feishu-wiki
Summary

Navigate and manage Feishu knowledge base spaces, nodes, and wiki pages.

Four core actions: list spaces and nodes, retrieve node details, create new pages (docx, sheet, bitable, mindnote, file, doc, slides), and move or rename existing nodes
Extract wiki tokens from Feishu URLs and use them to fetch node metadata including object tokens for content editing
Requires feishu_doc skill to be enabled for reading and writing wiki page content; use feishu_wiki for navigation, then hand off to feishu_doc for document operations
Supports hierarchical organization with parent node tokens, allowing creation and movement of pages within nested wiki structures
SKILL.md
Feishu Wiki Tool

Single tool feishu_wiki for knowledge base operations.

Token Extraction

From URL https://xxx.feishu.cn/wiki/ABC123def → token = ABC123def

Actions
List Knowledge Spaces
{ "action": "spaces" }


Returns all accessible wiki spaces.

List Nodes
{ "action": "nodes", "space_id": "7xxx" }


With parent:

{ "action": "nodes", "space_id": "7xxx", "parent_node_token": "wikcnXXX" }

Get Node Details
{ "action": "get", "token": "ABC123def" }


Returns: node_token, obj_token, obj_type, etc. Use obj_token with feishu_doc to read/write the document.

Create Node
{ "action": "create", "space_id": "7xxx", "title": "New Page" }


With type and parent:

{ "action": "create", "space_id": "7xxx", "title": "Sheet", "obj_type": "sheet", "parent_node_token": "wikcnXXX" }


obj_type: docx (default), sheet, bitable, mindnote, file, doc, slides

Move Node
{ "action": "move", "space_id": "7xxx", "node_token": "wikcnXXX" }


To different location:

{ "action": "move", "space_id": "7xxx", "node_token": "wikcnXXX", "target_space_id": "7yyy", "target_parent_token": "wikcnYYY" }

Rename Node
{ "action": "rename", "space_id": "7xxx", "node_token": "wikcnXXX", "title": "New Title" }

Wiki-Doc Workflow

To edit a wiki page:

Get node: { "action": "get", "token": "wiki_token" } → returns obj_token
Read doc: feishu_doc { "action": "read", "doc_token": "obj_token" }
Write doc: feishu_doc { "action": "write", "doc_token": "obj_token", "content": "..." }
Configuration
channels:
  feishu:
    tools:
      wiki: true  # default: true
      doc: true   # required - wiki content uses feishu_doc


Dependency: This tool requires feishu_doc to be enabled. Wiki pages are documents - use feishu_wiki to navigate, then feishu_doc to read/edit content.

Permissions

Required: wiki:wiki or wiki:wiki:readonly

Weekly Installs
426
Repository
m1heng/clawdbot-feishu
GitHub Stars
4.3K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass