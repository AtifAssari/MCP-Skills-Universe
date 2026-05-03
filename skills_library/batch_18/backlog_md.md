---
title: backlog-md
url: https://skills.sh/nickcrew/claude-ctx-plugin/backlog-md
---

# backlog-md

skills/nickcrew/claude-ctx-plugin/backlog-md
backlog-md
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill backlog-md
SKILL.md
Backlog.md Task Tracking for Agents

Task tracking system optimized for agent workflows via Backlog.md CLI.

Three Primary Use Cases
1. Implementer: Deferring Issues During Feature Work

File P2-P4 issues discovered during implementation. Use label remediation for deferred review findings.

Create with plan: You have implementation context at filing time
Assign priority: See priority guide
Add type label (required) + app labels (optional)
2. Reviewer: Audit Findings

Create structured issues from security/audit reviews. Link dependencies and assign to milestones.

Create with plan: You're creating from audit context
Link dependencies as needed
Assign priority: Ask user if uncertain (label priority-review)
Set milestones
3. Worker: Executing Assigned Tasks

Read task fully, understand all fields, follow acceptance criteria and definition of done.

Claim task: backlog task edit 42 -s "In Progress" -a @myself
Read everything: All fields, attached files/URLs, linked documentation
Complete systematically: AC → Implementation Notes → Final Summary → DoD → Done
Absolute Rules
CLI only for writes. backlog task edit and backlog task create only. Never edit files directly.
Always use --plain flag when reading: backlog task 42 --plain, backlog task list --plain
Type label required (bug|feature|documentation|refactor|remediation), single value only
App labels optional, can be multiple: synapse-pingora, signal-horizon-ui, signal-horizon-api, etc.
Custom labels allowed as agent-useful (priority-review, performance, security, etc.)
Implementation Plans: When Required
Scenario	Include Plan?	Reason
Deferred review issues	✅ YES	You have audit/review context now
Reporting found issues	❌ NO	Implementer will plan when they work it
Explicitly asked to plan work	✅ YES (detailed)	Required per instruction
Regular task work	After claiming, before coding	Don't add at creation, add after starting

Never update an existing plan unless explicitly instructed.

Priority System (See references/priority-labels.md for details)
P0: Critical problems, major breakage
P1: Legitimate bugs impacting users
P2: Bugs, edge cases
P3: Nice-to-have improvements, features we want
P4: Backlog, future ideas

Unsure about P0-P1? Label with priority-review and let user decide.

Task Completion Checklist
Status: "In Progress" + assign self
Read: All fields, attached documentation
Plan: Add implementation plan (if not deferred from review)
Work: Code implementation, mark AC as you complete each
Notes: Append progress notes as you go
Summary: Add final summary (PR-style)
DoD: Check all definition-of-done items
Done: Set status "Done"
Essential Commands
# Create issue (required: title, type label, priority)
backlog task create "Title" -d "Description" -l bug -p 2 --ac "AC 1"

# Work a task
backlog task edit 42 -s "In Progress" -a @myself
backlog task 42 --plain              # Read everything
backlog task edit 42 --check-ac 1    # Mark AC complete
backlog task edit 42 --append-notes "Progress here"
backlog task edit 42 --final-summary "PR description"
backlog task edit 42 -s Done

# Search and filter
backlog task list -s "To Do" --plain
backlog search "topic" --plain


See references/cli-reference.md for complete command reference. See references/priority-labels.md for priority and labeling guidelines. See references/issue-creation-guide.md for detailed issue creation patterns.

Weekly Installs
28
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn