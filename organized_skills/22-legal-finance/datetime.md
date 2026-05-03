---
rating: ⭐⭐⭐
title: datetime
url: https://skills.sh/cadrianmae/claude-marketplace/datetime
---

# datetime

skills/cadrianmae/claude-marketplace/datetime
datetime
Installation
$ npx skills add https://github.com/cadrianmae/claude-marketplace --skill datetime
SKILL.md
DateTime Natural Language Parser

Parse natural language date and time expressions using GNU date command (native Linux utility).

IMPORTANT: For Claude Code

DO NOT invoke slash commands (/datetime:parse, /datetime:now, /datetime:calc) - those are for users only.

Instead, use the date command directly via the Bash tool:

# Get current date/time
date '+%Y-%m-%d %H:%M:%S (%A)'

# Parse natural language
date -d "tomorrow" '+%Y-%m-%d %H:%M:%S (%A)'
date -d "next monday at 9am" '+%Y-%m-%d %H:%M:%S (%A)'
date -d "3 days" '+%Y-%m-%d %H:%M:%S (%A)'


This skill provides the command patterns and when to use them. The slash commands are for users to invoke manually.

Quick Example
date -d "next Friday" '+%Y-%m-%d %H:%M:%S (%A)'
# 2026-02-06 00:00:00 (Friday)

When to Use This Skill

Automatically invoke when:

User mentions temporal expressions: "tomorrow", "next week", "in 3 days"
Need to verify current date/time
User references deadlines or time-sensitive tasks
context shows incorrect dates
How to Use

Use the Bash tool with date -d command:

Get current date/time:

date '+%Y-%m-%d %H:%M:%S (%A)'


Parse natural language:

date -d "tomorrow" '+%Y-%m-%d %H:%M:%S (%A)'
date -d "next wednesday" '+%Y-%m-%d %H:%M:%S (%A)'
date -d "3 days" '+%Y-%m-%d %H:%M:%S (%A)'
date -d "next monday 9am" '+%Y-%m-%d %H:%M:%S (%A)'


Important: The date command doesn't understand "in" keyword. When user says "in 3 days", use "3 days" instead.

Output Format

Returns single line: YYYY-MM-DD HH:MM:SS (DayName)

Example: 2024-10-29 14:23:45 (Tuesday)

Supported Expressions
Relative: "today", "tomorrow", "yesterday"
Named days: "next monday", "this wednesday", "last friday"
Offsets: "3 days", "2 weeks", "5 months ago"
Complex: "tomorrow 3pm", "next monday at 9am"
Past: "3 days ago", "last week"
Error Handling

If date -d fails with an invalid expression:

Recognize the failure: If the command returns an error, inform the user the expression couldn't be parsed
Try alternative approaches: Check references/reference.md for:
Date arithmetic examples (if user wants relative calculations)
Complex expression syntax (if user wants compound dates)
Unix timestamp calculations (if user wants day differences)
Fallback to current date: If no alternative works:
date '+%Y-%m-%d %H:%M:%S (%A)'


Example error handling:

# Try parsing
date -d "user expression" '+%Y-%m-%d %H:%M:%S (%A)' 2>&1
# If error message appears, tell user and suggest checking references/reference.md for advanced patterns

Advanced Usage

For relative calculations, week numbers, and complex date arithmetic, see references/reference.md.

Weekly Installs
69
Repository
cadrianmae/clau…ketplace
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass