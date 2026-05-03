---
title: agent-kanban
url: https://skills.sh/benyue1978/agent-kanban/agent-kanban
---

# agent-kanban

skills/benyue1978/agent-kanban/agent-kanban
agent-kanban
Installation
$ npx skills add https://github.com/benyue1978/agent-kanban --skill agent-kanban
SKILL.md
Agent Kanban Skill
Overview

This skill defines how an agent interacts with the agent-kanban system to track and complete work.

Core principles:

Repo is implementation truth - code, tests, docs are authoritative
Kanban is process truth - state, ownership, comments live in Kanban
Comments are timeline - record progress, do not replace Final Summary
Never test against production - verify DATABASE_URL targets port 5434/dev
Understanding Progress

At the start of a session, understand the full board state:

kanban cards list --project <id> --state new - new cards (unowned)
kanban cards list --project <id> --state ready - ready to pick up
kanban cards list --project <id> --state in-progress - currently working
kanban cards list --project <id> --state in-review - awaiting review
kanban cards list --project <id> --state done - completed
kanban config - check current config
Pushing Cards Through Kanban
State Machine
New → Ready → In Progress → In Review → Done

New → Ready

Agent must:

Collaborate with human to fill in: Goal, Context, Scope, Definition of Done
Ensure all four sections have real content (not placeholder text)
Get human approval on the plan
Run: kanban cards set-state --id <id> --to ready --actor human --revision <n>

Don't:

Don't transition without human sign-off on the plan
Don't use --actor agent - human must own this decision
Don't skip any of the four required sections

If error missing_required_section:

Fetch card: kanban cards show --id <id>
Check which section is missing: Goal, Context, Scope, Definition of Done
Update: kanban cards update --id <id> --file card.md --revision <n>
Retry with --actor human
Ready → In Progress

Agent must:

Claim ownership: kanban cards set-state --id <id> --to in-progress --owner <owner-id> --revision <n>
Implementation begins only after claiming

Don't:

Don't start implementation before claiming the card
In Progress → In Review

Agent must:

Verify implementation is complete and tests pass
Spawn subagent to review code changes (MANDATORY, cannot skip)
Move to In Review: kanban cards set-state --id <id> --to in-review --owner <owner-id> --revision <n>
Document review findings as comments

Don't:

Don't skip the reviewer subagent - it's required

If review finds issues:

Move back to In Progress: kanban cards set-state --id <id> --to in-progress ...
Fix issues
Re-review before moving to Done
In Review → Done

Agent must:

Final Summary exists with:
What was done
Key Decisions
Result / Links (commit URL, PR, etc.)
DoD Check
Verification evidence recorded as verification kind comment
Run: kanban cards set-state --id <id> --to done --actor human --revision <n>

Don't:

Don't move without Final Summary
Don't move without verification evidence (test output, logs, screenshots)
Don't link to commits that don't exist
Command Reference
Discovery & Config
kanban discovery - show available commands and flags
kanban config - show current config
Card Commands
kanban cards list --project <id> --state <state> - list cards
kanban cards show --id <id> - show card details
kanban cards create --project <id> --title <title> --description-file <path> - create card
kanban cards update --id <id> --file <path> --revision <n> - update card
kanban cards append-summary --id <id> --file <path> - append summary (use --replace to overwrite)
State Transitions
kanban cards set-state --id <id> --to <state> - transition card state
Comments
kanban cards comment --id <id> --body "..." --kind <kind> --author <id> - add comment
Comment Kinds
Kind	Use for
progress	implementation done, tests added, artifact created
question	asking human for decision, clarification needed
decision	design decision, review outcome, direction change
note	handoff, minor context
verification	test output, screenshots, logs as evidence

If a decision affects final understanding, reflect it in Final Summary before Done.

Quick Reference
State Machine
New → Ready → In Progress → In Review → Done

Required Fields Per Transition
Transition	Required
New → Ready	Goal, Context, Scope, Definition of Done
Ready → In Progress	ownership claimed
In Progress → In Review	implementation complete, tests pass, reviewer subagent spawned
In Review → Done	Final Summary (What was done, Key Decisions, Result/Links, DoD Check) + verification comment
Error Handling
Error	Action
revision_conflict	Re-fetch card, inspect changes, re-apply
claim_conflict	Choose another card
missing_required_section	Complete missing section, don't bypass
summary_required	Add Final Summary before Done
cli_usage_error	Run kanban discovery to verify flags

Use --dry-run to validate before destructive updates.

Anti-Patterns

Do not:

Treat comments as final deliverable
Overwrite Goal or Definition of Done casually
Rename protected markdown headings
Bypass structured commands for critical updates
Create temp .md files in workspace root
Move to Done without Final Summary and verification evidence
Move to Done without linking to real commits
Use --actor agent for New → Ready transition
Skip the reviewer subagent for In Progress → In Review
Weekly Installs
8
Repository
benyue1978/agent-kanban
First Seen
Apr 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass