---
title: zendesk
url: https://skills.sh/jdrhyne/agent-skills/zendesk
---

# zendesk

skills/jdrhyne/agent-skills/Zendesk
Zendesk
Installation
$ npx skills add https://github.com/jdrhyne/agent-skills --skill Zendesk
SKILL.md
Zendesk

Manage Zendesk tickets, users, and support workflows through the authenticated Zendesk API.

When to Use
search tickets or support history
create or update tickets
inspect user details
export queue data for analysis
summarize current support state
Setup

Use these environment variables:

ZENDESK_SUBDOMAIN
ZENDESK_EMAIL
ZENDESK_TOKEN

Build the Zendesk auth context from those variables and confirm access before trying ticket operations.

Workflow Rules
Search before creating a ticket to avoid duplicates.
Use views or targeted search instead of listing entire queues.
Add internal notes when changing status or ownership.
Confirm destructive or customer-visible actions before sending them.
Respect Zendesk rate limits during bulk work.
Common Operations
Search tickets by status, priority, assignee, or subject before creating a new one.
Create tickets with a clear subject, customer-visible comment, and correct priority.
Update status with an internal note that explains what changed and why.
Look up users by email before editing ownership, organization, or requester fields.
Export queue data only when the user explicitly asked for a saved report.
Safety Boundaries
Do not read credentials from ad hoc files, memory stores, or chat history; use only the documented environment variables.
Do not close, merge, delete, or publicly reply to tickets without explicit confirmation.
Do not export ticket or user data to files unless the user asked for a saved artifact.
Do not send Zendesk data to any service other than the authenticated Zendesk API.
Weekly Installs
20
Repository
jdrhyne/agent-skills
GitHub Stars
232
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass