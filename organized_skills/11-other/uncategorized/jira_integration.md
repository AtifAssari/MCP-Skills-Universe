---
rating: ⭐⭐
title: jira-integration
url: https://skills.sh/questnova502/claude-skills-sync/jira-integration
---

# jira-integration

skills/questnova502/claude-skills-sync/jira-integration
jira-integration
Installation
$ npx skills add https://github.com/questnova502/claude-skills-sync --skill jira-integration
SKILL.md
Jira Integration Skill

Comprehensive Jira integration through lightweight Python CLI scripts.

Note: Run scripts from skills/jira-communication/, or use full paths from repo root.

Auto-Trigger Patterns

AUTOMATICALLY ACTIVATE when user mentions:

Jira URLs: https://jira.*/browse/*, https://*.atlassian.net/browse/*
Issue keys: Pattern like PROJ-123, NRS-4167, ABC-1
Keywords: "Jira issue", "Jira ticket", "search Jira"
Authentication Failure Handling

CRITICAL: When authentication fails, DO NOT just display the error. Instead:

Detect failure - Look for "Missing required variable" or 401/403 responses
Offer help - Ask: "Would you like me to help configure Jira credentials?"
Run interactive setup - uv run skills/jira-communication/scripts/core/jira-setup.py
Sub-Skills
Skill	Purpose
jira-communication	API operations via Python CLI scripts
jira-syntax	Wiki markup syntax, templates, validation
Scripts Reference
Core Operations
Script	Purpose
jira-setup.py	Interactive credential setup
jira-validate.py	Verify connection
jira-issue.py	Get/update issue details
jira-search.py	Search with JQL
jira-worklog.py	Time tracking
jira-attachment.py	Download attachments
Workflow Operations
Script	Purpose
jira-create.py	Create issues
jira-transition.py	Change status
jira-comment.py	Comments
jira-link.py	Issue links
jira-sprint.py	Sprint management
jira-board.py	Board operations
Syntax Note

Jira uses wiki markup, NOT Markdown. See skills/jira-syntax/SKILL.md for syntax guide.

Contributing: https://github.com/netresearch/jira-skill

Weekly Installs
11
Repository
questnova502/cl…lls-sync
GitHub Stars
3
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass