---
title: catalog-browser
url: https://skills.sh/jsonlee12138/agent-team/catalog-browser
---

# catalog-browser

skills/jsonlee12138/agent-team/catalog-browser
catalog-browser
Installation
$ npx skills add https://github.com/jsonlee12138/agent-team --skill catalog-browser
SKILL.md
catalog-browser
Audience
human
controller
Triggers
search catalog
browse roles
show catalog role
catalog stats
CLI Binding
agent-team catalog search
agent-team catalog show
agent-team catalog list
agent-team catalog repo
agent-team catalog stats
Required Entry
MUST read .agent-team/rules/index.md first.
Expansion
Load only the catalog results needed for the current read-only browsing request.
Boundary
This skill exposes only the browsing subset of catalog commands.
Do not absorb role source installation or update flows; those belong to role-repo-manager.
Do not expose normalize, discover, or serve through this skill.
Weekly Installs
22
Repository
jsonlee12138/agent-team
GitHub Stars
24
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass