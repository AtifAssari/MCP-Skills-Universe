---
title: compact
url: https://skills.sh/kelvinz/cobb/compact
---

# compact

skills/kelvinz/cobb/compact
compact
Installation
$ npx skills add https://github.com/kelvinz/cobb --skill compact
SKILL.md
compact

Keep tasks/context.md short and scannable by consolidating older entries into readable summaries.

Guardrails
Do not change product scope or implementation code.
Do not move or rename PRDs here; completed PRDs are archived during commit finalise.
Do not create separate context archive files.
Ask for explicit confirmation before applying consolidation edits.
Always propose retention/consolidation counts first; let the user choose the final numbers.
When asking for user decisions, provide numbered short-reply options (e.g. 1, 2, 3).
Workflow
Preflight:
Ensure tasks/ exists.
Inspect tasks/context.md.
Count entries to compact in tasks/context.md: Key decisions, Completed, Notes / gotchas.
Propose consolidation options and ask for a decision:
Suggest how many entries to keep in full detail vs consolidate into summary.
Provide recommended defaults, then allow user override (more or fewer).
Compact tasks/context.md in place:
Preserve Project and Current state sections.
Keep the user-selected number of most recent detailed entries (entries are newest-first, so keep from the top).
Before consolidating, extract still-relevant risks, open questions, or gotchas from older entries (bottom of each section).
Move them into Notes / gotchas or Current state: Blockers so they are not lost.
Replace older entries with a concise historical summary block appended at the bottom of each section.
Report results:
Show retained vs consolidated counts.
Call out any sections intentionally left untouched.
Suggested Defaults

Use these as initial recommendations, then ask the user to confirm or adjust:

tasks/context.md:
Keep the latest 10 entries in detail across historical sections.
Consolidate older entries into summary.
References
references/compact-templates.md: threshold-choice prompt and historical-summary examples.
Output
Update only tasks/context.md.
Return:
proposed numbers and user-selected numbers
retained vs consolidated counts
concise summary of what changed
End with a short status block:
Files changed: list of created/updated files
Key decisions: any assumptions or choices made (if any)
Next step: recommended next skill or action
Weekly Installs
30
Repository
kelvinz/cobb
First Seen
7 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass