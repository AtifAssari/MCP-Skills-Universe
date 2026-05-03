---
title: ask-multi
url: https://skills.sh/tony363/superclaude/ask-multi
---

# ask-multi

skills/tony363/superclaude/ask-multi
ask-multi
Installation
$ npx skills add https://github.com/tony363/superclaude --skill ask-multi
SKILL.md
Ask Multi Skill

Multi-select variant of the AskUserQuestion tool.

Usage
/ask-multi "Question" "Option 1" "Option 2" ["Option 3"] ["Option 4"]

Instructions

When this skill is invoked:

First quoted argument = question text
Remaining arguments = options (2-4 required)
Invoke AskUserQuestion tool with parsed arguments
Set multiSelect: true
Constraints
Minimum 2 options, maximum 4 options
If constraints violated, inform user of limits
Examples
/ask-multi "Which features to enable?" "Auth" "Logging" "Caching" "Metrics"
/ask-multi "Select environments to deploy:" "dev" "staging" "prod"
/ask-multi "Install which extras?" "test" "dev" "docs"

Weekly Installs
27
Repository
tony363/superclaude
GitHub Stars
17
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass