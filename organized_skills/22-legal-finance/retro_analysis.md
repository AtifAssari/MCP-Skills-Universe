---
rating: ⭐⭐
title: retro-analysis
url: https://skills.sh/mohitagw15856/pm-claude-skills/retro-analysis
---

# retro-analysis

skills/mohitagw15856/pm-claude-skills/retro-analysis
retro-analysis
Installation
$ npx skills add https://github.com/mohitagw15856/pm-claude-skills --skill retro-analysis
SKILL.md
Retrospective Analysis Skill

Generate a data-grounded retrospective brief that separates facts from feelings, so the team spends retro time on solutions rather than debating what happened.

Required Inputs

Ask the user for these if not provided:

Sprint tickets: planned vs. completed
Carry-over tickets and reasons (if known)
Tickets reopened after closing (quality signal)
Any incidents or unplanned work (scope creep signal)
Sprint velocity vs. historical average (trend context)
Process
Calculate: completion rate, carry-over rate, unplanned work percentage
Identify patterns: which ticket types were most likely to carry over? Which caused blockers?
Note any process or communication breakdowns visible in the data
Prepare 3 "Start / Stop / Continue" prompts based on the data — not generic, specific to this sprint
Suggest 1 concrete experiment for the next sprint based on the biggest friction point
Validate — Confirm each prompt is specific to this sprint (not a recycled generic prompt), and that the recommended experiment is concrete and measurable
Output Structure
Sprint [Number] Retrospective Brief

By the Numbers:

Planned: [n] tickets | Completed: [n] | Carry-over: [n] | Completion rate: [%]
Unplanned work: [n] tickets ([%] of capacity)
Velocity: [points] vs. [average] average

What the Data Suggests: [2-3 observations grounded in the numbers above]

Discussion Prompts:

Start: [specific prompt based on this sprint's data]
Stop: [specific prompt based on this sprint's data]
Continue: [specific prompt based on this sprint's data]

Suggested Experiment for Next Sprint: [One concrete, testable process change — with a specific success metric]

Quality Checks
 Each Start/Stop/Continue prompt names a specific behaviour, not a vague category
 The recommended experiment is testable in one sprint
 Carry-over analysis identifies the ticket type or cause, not just the count
 Data observations don't assign blame — they describe patterns
 Velocity trend is mentioned in context (is this a one-off or a pattern?)
Weekly Installs
11
Repository
mohitagw15856/p…e-skills
GitHub Stars
293
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass