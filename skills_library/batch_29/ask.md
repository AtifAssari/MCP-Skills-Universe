---
title: ask
url: https://skills.sh/tony363/superclaude/ask
---

# ask

skills/tony363/superclaude/ask
ask
Installation
$ npx skills add https://github.com/tony363/superclaude --skill ask
SKILL.md
Ask Skill

Quick invocation of the AskUserQuestion tool for single-select questions.

Usage
/ask "Question" "Option 1" "Option 2" ["Option 3"] ["Option 4"]

Instructions

When this skill is invoked:

First quoted argument = question text
Remaining arguments = options (2-4 required)
Invoke AskUserQuestion tool with parsed arguments
Set multiSelect: false
Constraints
Minimum 2 options, maximum 4 options
If constraints violated, inform user of limits
Examples
/ask "Which testing framework?" "pytest" "unittest" "nose2"
/ask "Deploy to which environment?" "staging" "production"
/ask "Database choice?" "PostgreSQL" "MySQL" "SQLite" "MongoDB"

Weekly Installs
29
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