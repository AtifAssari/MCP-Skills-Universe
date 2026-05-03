---
title: super-save
url: https://skills.sh/supermemoryai/claude-supermemory/super-save
---

# super-save

skills/supermemoryai/claude-supermemory/super-save
super-save
Installation
$ npx skills add https://github.com/supermemoryai/claude-supermemory --skill super-save
SKILL.md
Super Save

Save important project knowledge based on what the user wants to preserve.

Step 1: Understand User Request

Analyze what the user is asking to save from the conversation.

Step 2: Format Content
[SAVE:<username>:<date>]

<Username> wanted to <goal/problem>.

Claude suggested <approach/solution>.

<Username> decided to <decision made>.

<key details, files if relevant>

[/SAVE]


Example:

[SAVE:prasanna:2026-02-04]

Prasanna wanted to create a skill for saving project knowledge.

Claude suggested using a separate container tag (repo_<hash>) for shared team knowledge.

Prasanna decided to keep it simple - no transcript fetching, just save what user asks for.

Files: src/save-project-memory.js, src/lib/container-tag.js

[/SAVE]


Keep it natural. Capture the conversation flow.

Step 3: Save
node "${CLAUDE_PLUGIN_ROOT}/scripts/save-project-memory.cjs" "FORMATTED_CONTENT"

Weekly Installs
329
Repository
supermemoryai/c…ermemory
GitHub Stars
2.6K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail