---
title: recipe-create-task-list
url: https://skills.sh/googleworkspace/cli/recipe-create-task-list
---

# recipe-create-task-list

skills/googleworkspace/cli/recipe-create-task-list
recipe-create-task-list
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill recipe-create-task-list
Summary

Initialize a Google Tasks list and populate it with multiple tasks via command sequence.

Requires the gws-tasks skill to execute task list and task management operations
Provides step-by-step commands to create a new task list, add tasks with optional notes and due dates, and display results in table format
Demonstrates task insertion with structured JSON payloads including title, notes, and ISO 8601 due date formatting
SKILL.md
Create a Task List and Add Tasks

PREREQUISITE: Load the following skills to execute this recipe: gws-tasks

Set up a new Google Tasks list with initial tasks.

Steps
Create task list: gws tasks tasklists insert --json '{"title": "Q2 Goals"}'
Add a task: gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Review Q1 metrics", "notes": "Pull data from analytics dashboard", "due": "2024-04-01T00:00:00Z"}'
Add another task: gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Draft Q2 OKRs"}'
List tasks: gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}' --format table
Weekly Installs
11.3K
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