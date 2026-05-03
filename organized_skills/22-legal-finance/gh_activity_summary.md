---
rating: ⭐⭐⭐
title: gh-activity-summary
url: https://skills.sh/ericmjl/skills/gh-activity-summary
---

# gh-activity-summary

skills/ericmjl/skills/gh-activity-summary
gh-activity-summary
Installation
$ npx skills add https://github.com/ericmjl/skills --skill gh-activity-summary
SKILL.md
GitHub activity report

This skill generates a markdown-friendly report of your GitHub activity over a date range using the gh CLI.

Usage

Run the bundled script with optional START_DATE and END_DATE (format: YYYY-MM-DD).

# Default: last 7 days
bash skills/gh-activity-summary/activity-report.sh

# Specific range
bash skills/gh-activity-summary/activity-report.sh 2026-01-01 2026-01-07

Requirements
gh (GitHub CLI) - must be authenticated (gh auth login)
jq - used for JSON counting and formatting
What It Does
Lists commits you authored in the date range.
Lists pull requests you created and merged.
Lists pull requests you reviewed.
Lists issues you created.
Prints simple summary counts for quick status updates.
How It Works
Uses gh search to query commits, PRs, and issues scoped to @me.
Uses platform-aware date defaults (macOS vs Linux) when you omit dates.
Formats output as readable markdown so you can paste it into status updates or pipe it into an LLM for summarization.

To generate a short natural-language summary, you can pipe the report into your preferred model:

bash skills/gh-activity-summary/activity-report.sh 2026-01-01 2026-01-07 | claude "Summarize this in 2-3 sentences"

Weekly Installs
13
Repository
ericmjl/skills
GitHub Stars
32
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn