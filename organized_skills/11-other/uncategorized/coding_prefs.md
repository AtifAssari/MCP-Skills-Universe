---
rating: ⭐⭐
title: coding-prefs
url: https://skills.sh/langchain-ai/deepagents/coding-prefs
---

# coding-prefs

skills/langchain-ai/deepagents/coding-prefs
coding-prefs
Installation
$ npx skills add https://github.com/langchain-ai/deepagents --skill coding-prefs
SKILL.md
Coding Preferences Skill

Use this skill to keep /memory/coding-prefs.md in sync with how this specific user wants you to work. This file is user-scoped, so each user has their own copy — anything you write here only affects future conversations with the same user.

When to Read
Before picking a code style, test framework, or commit message format
Before deciding whether to add comments, type hints, or docstrings
Before refactoring beyond what was asked
When to Write

Append a new entry whenever the user gives feedback that should apply to future work:

"Don't add docstrings unless I ask" → save it
"I prefer pytest over unittest" → save it
"Stop summarizing what you did at the end" → save it

Each entry should be one line: the rule, then a brief reason if the user gave one.

How to Write

Read the file first (it may not exist yet), then append. Don't overwrite — preferences accumulate over time. If a new preference contradicts an existing one, replace the old line and note the change.

Weekly Installs
42
Repository
langchain-ai/deepagents
GitHub Stars
22.1K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass