---
rating: ⭐⭐⭐
title: ghpm-suggest
url: https://skills.sh/jackchuka/ghpm/ghpm-suggest
---

# ghpm-suggest

skills/jackchuka/ghpm/ghpm-suggest
ghpm-suggest
Installation
$ npx skills add https://github.com/jackchuka/ghpm --skill ghpm-suggest
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

ghpm-suggest

PREREQUISITE: Read ../ghpm-shared/SKILL.md for prerequisites and error handling.

Recommend what to work on next by assembling session context and project state, then reasoning about the best options.

Arguments
/ghpm-suggest — open-ended recommendation
/ghpm-suggest <constraint> — any natural language constraint, e.g.:
"I have 2 hours"
"I want to switch context"
"I want to focus on frontend work"
"something small"
Session Context

The following is auto-injected at invocation time. If any value is empty, that context is unavailable — skip it gracefully.

Current repo: !git remote get-url origin 2>/dev/null
Current branch: !git branch --show-current 2>/dev/null
Recent commits: !git log --oneline -5 2>/dev/null
Changed files: !git diff --stat HEAD~5..HEAD 2>/dev/null
GitHub user: !gh api user --jq '.login' 2>/dev/null
Workflow
Phase 1: Gather Context

Project config (required): Follow the startup sequence in ../ghpm-shared/SKILL.md.

Project items (required): Load cache per ../ghpm-shared/references/cache.md. Focus on non-Done items: ReadyForDev, Planned, InProgress.

Session context: Use the auto-injected values above. If GitHub user is available, find items assigned to them in cache. Find items in Done status assigned to user (these indicate completed work, but no completion date is available).

Relevant views (optional — skip if session context unavailable):

If in a repo that matches a component, that component's view is relevant.
Team standup views that match the user's assignments are relevant.
Triage views are always relevant (unassigned work).

Degraded mode: If only project config and items are available (no git context, no user identity), suggest based purely on project state: prioritize ReadyForDev items with no assignee, then Planned items.

Phase 2: Reason and Suggest

With all context assembled, reason about what to suggest. Consider:

Proximity: items in the same repo/component as current work require less context-switching.
Momentum: items related to recently completed work — the user has warm context.
Status: ReadyForDev items are higher priority than Planned (already vetted).
Dependencies: items unblocked by the user's recent completions (parent/sub-issue relationships if visible in cache).
Size: if the user mentioned time constraints, prefer smaller items.
Breadth: if the user wants to switch context, suggest items in different components.
Assignee: prefer items already assigned to the user, then unassigned items.

User constraints from arguments adjust the reasoning:

"2 hours" / "something small" → prefer XS/S sized items
"switch context" → prefer items in DIFFERENT components than recent work
"" → filter to that component
No constraint → balance proximity with priority
Phase 3: Present Suggestions
Format per conventions in ../ghpm-shared/references/format.md. Present suggestions in tiers — a top recommendation, strong alternatives, and optionally a "change of pace" option. The exact count is flexible (3-5 is typical), but every suggestion should earn its place.

For each suggestion, explain why now — what makes this the right item at this moment. Be specific: mention deadlines, recent momentum, blocking relationships, or team context. Also explain how it fits the constraint (e.g., "2-hour fit: migrate a batch of test files, each is self-contained").

Based on your context:
  Repo: <current repo>
  Recent work: <summary of recent commits>
  <component/team> affinity: <inferred from context>

## Top Recommendation

### 1. <title>
- **Issue:** <repo>#<num>
- **URL:** <github url>
- **Status:** <status>
- **Why now:** <specific reasoning — deadlines, momentum, blocking, team needs>
- **<constraint> fit:** <how this fits the user's time/energy/focus constraint>

## Strong Alternatives

### 2. <title>
...

### 3. <title>
...

## If You Want a Change of Pace

### 4. <title>
- (optional tier for lower-priority or different-domain options)


Include a summary table at the end for quick scanning:

| Priority | Issue | Status | Rationale |
|----------|-------|--------|-----------|
| 1 | ... | ... | one-line why |

Include issue URL for easy navigation.
If user constraint was provided, note how it influenced the suggestions.
If no good candidates found, say so and suggest running /ghpm-view triage to find unassigned work.
Tips
Read-only — never modifies the project or its items.
See Also
ghpm-shared — Prerequisites and error handling
ghpm-status — Project health dashboard
ghpm-view — Drill into a specific view
ghpm-work — Start a work session on an issue
Weekly Installs
29
Repository
jackchuka/ghpm
GitHub Stars
19
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass