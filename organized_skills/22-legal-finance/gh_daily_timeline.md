---
rating: ⭐⭐⭐
title: gh-daily-timeline
url: https://skills.sh/ericmjl/skills/gh-daily-timeline
---

# gh-daily-timeline

skills/ericmjl/skills/gh-daily-timeline
gh-daily-timeline
Installation
$ npx skills add https://github.com/ericmjl/skills --skill gh-daily-timeline
SKILL.md
GitHub Activity Reporter

This skill reports your GitHub activity for a specific day using the gh CLI.

Usage

Run the script with an optional date argument (defaults to today):

# Get today's activity
bash gh-activity.sh

# Get activity for a specific date
bash gh-activity.sh 2025-12-15


The date format must be YYYY-MM-DD.

Requirements
gh (GitHub CLI) - must be authenticated with your GitHub account
jq - for JSON processing
What It Reports

Commits: Lists all commits you made with their actual commit messages, grouped by repository and branch.

Issues: Shows all issues you created, commented on, or interacted with, including issue titles and the type of interaction.

Activity Timeline: A chronological view of all your GitHub events for the day (pushes, PRs, issue comments, etc.).

How It Works
Verifies you're authenticated with GitHub CLI
Fetches your events using gh api /users/{username}/events
Filters events to the specified date
For each push event, fetches actual commits using gh api /repos/{repo}/compare/{before}...{head}
Extracts and displays issue information from issue events
Formats everything into a clear, organized report
Weekly Installs
10
Repository
ericmjl/skills
GitHub Stars
32
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn