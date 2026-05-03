---
rating: ⭐⭐
title: persona-customer-support
url: https://skills.sh/googleworkspace/cli/persona-customer-support
---

# persona-customer-support

skills/googleworkspace/cli/persona-customer-support
persona-customer-support
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill persona-customer-support
Summary

Customer support agent for ticket triage, response, and escalation via email, sheets, and chat.

Requires four Google Workspace utility skills: Gmail, Sheets, Chat, and Calendar for full functionality
Core workflows include email-to-task conversion, inbox triage by label, ticket status logging, and escalation to team Chat channels
Supports scheduling follow-up calls and generating standup reports alongside ticket management
Built-in commands for quick dashboard views and Gmail filter setup to automate support request categorization
SKILL.md
Customer Support Agent

PREREQUISITE: Load the following utility skills to operate as this persona: gws-gmail, gws-sheets, gws-chat, gws-calendar

Manage customer support — track tickets, respond, escalate issues.

Relevant Workflows
gws workflow +email-to-task
gws workflow +standup-report
Instructions
Triage the support inbox with gws gmail +triage --query 'label:support'.
Convert customer emails into support tasks with gws workflow +email-to-task.
Log ticket status updates in a tracking sheet with gws sheets +append.
Escalate urgent issues to the team Chat space.
Schedule follow-up calls with customers using gws calendar +insert.
Tips
Use gws gmail +triage --labels to see email categories at a glance.
Set up Gmail filters for auto-labeling support requests.
Use --format table for quick status dashboard views.
Weekly Installs
11.1K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn