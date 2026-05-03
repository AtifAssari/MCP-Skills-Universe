---
rating: ⭐⭐
title: capgo-cli-usage
url: https://skills.sh/cap-go/capgo-skills/capgo-cli-usage
---

# capgo-cli-usage

skills/cap-go/capgo-skills/capgo-cli-usage
capgo-cli-usage
Installation
$ npx skills add https://github.com/cap-go/capgo-skills --skill capgo-cli-usage
SKILL.md
Capgo CLI Usage

Use this skill as the entry point for Capgo CLI command routing.

When to Use This Skill
User asks generally how to use the Capgo CLI
The request spans multiple Capgo command groups
The right Capgo sub-workflow is not obvious yet
Routing

Route specific workflows to the matching skill:

OTA bundles and channels -> capgo-release-management
native cloud builds -> capgo-native-builds
organizations and account commands -> capgo-organization-management
Common Commands
init
login
doctor
probe
app add
app list
app delete
app set
app debug
mcp

Prefer the current CLI form:

npx @capgo/cli@latest doctor

Error Handling
If the request is specific enough for a narrower Capgo skill, switch to that skill instead of staying at the routing layer.
For CLI auth issues, fix login first before troubleshooting downstream commands.
Weekly Installs
97
Repository
cap-go/capgo-skills
GitHub Stars
32
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass