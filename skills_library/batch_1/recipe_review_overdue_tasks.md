---
title: recipe-review-overdue-tasks
url: https://skills.sh/googleworkspace/cli/recipe-review-overdue-tasks
---

# recipe-review-overdue-tasks

skills/googleworkspace/cli/recipe-review-overdue-tasks
recipe-review-overdue-tasks
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-review-overdue-tasks
Summary

Identify and review overdue Google Tasks requiring immediate attention.

Requires the gws-tasks skill to query Google Tasks API
Three-step workflow: list all task lists, filter incomplete tasks by list ID, and review due dates for prioritization
Returns task data in table format for easy scanning of overdue items
SKILL.md
Review Overdue Tasks

PREREQUISITE: Load the following skills to execute this recipe: gws-tasks

Find Google Tasks that are past due and need attention.

Steps
List task lists: gws tasks tasklists list --format table
List tasks with status: gws tasks tasks list --params '{"tasklist": "TASKLIST_ID", "showCompleted": false}' --format table
Review due dates and prioritize overdue items
Weekly Installs
11.2K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass