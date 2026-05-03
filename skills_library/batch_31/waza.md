---
title: waza
url: https://skills.sh/tw93/waza/waza
---

# waza

skills/tw93/waza/waza
waza
Installation
$ npx skills add https://github.com/tw93/waza --skill waza
SKILL.md
Waza: Engineering Skills Dispatcher

Prefix your first line with 🥷 inline, not as its own paragraph.

You have eight skills available. Match the user's intent to the right skill, read its SKILL.md, and execute it.

Routing Table
Intent	Skill	File
New feature, architecture, "how should I design this", value judgment	think	skills/think/SKILL.md
UI, component, page, visual interface, frontend	design	skills/design/SKILL.md
Code review, before merge, "review this", triage issues/PRs	check	skills/check/SKILL.md
Error, crash, test failure, unexpected behavior, "why broken"	hunt	skills/hunt/SKILL.md
Writing, editing prose, polish, remove AI tone	write	skills/write/SKILL.md
Deep research, unfamiliar domain, compile sources into output	learn	skills/learn/SKILL.md
Any URL or PDF to fetch, "read this", "fetch this page"	read	skills/read/SKILL.md
Claude ignoring instructions, config audit, hooks/MCP broken	health	skills/health/SKILL.md
How This Works
Read the user's message and match it to a skill from the table above.
Read the matched file from the routing table in full.
Execute that skill's instructions exactly.

If the message could match multiple skills, use these disambiguation rules:

Most specific wins: /design is more specific than /think for UI decisions.
URL in message: start with /read. If the content is research material, chain to /learn.
Code already done vs. code broken: done/PR -> /check; error/broken -> /hunt.
Config vs. code: Claude misbehaving/hooks/MCP -> /health; user code errors -> /hunt.
From scratch vs. editing: new long-form output -> /learn; existing draft to polish -> /write.
"Judge this" + error -> /hunt; "judge this" + should we keep it -> /think.
Still ambiguous: read both skills' "Not for" sections; use exclusion. If still unclear, ask the user.
Path Resolution

In this distribution, sub-skill scripts live at skills/{name}/scripts/. Resolve all relative paths from this file's directory, not from $HOME/.agents/.

Chaining

Skills chain manually, not automatically. Each skill completes and waits for the user's next action.

Common chains: /think -> implement -> /check | /read -> /learn -> /write | /hunt -> fix -> /check

Weekly Installs
149
Repository
tw93/waza
GitHub Stars
4.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn