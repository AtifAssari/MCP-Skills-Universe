---
rating: ⭐⭐⭐
title: replay-learnings
url: https://skills.sh/rohitg00/pro-workflow/replay-learnings
---

# replay-learnings

skills/rohitg00/pro-workflow/replay-learnings
replay-learnings
Installation
$ npx skills add https://github.com/rohitg00/pro-workflow --skill replay-learnings
SKILL.md
Replay Learnings

Like muscle memory for your coding sessions. Find and surface relevant learnings before you start working.

Trigger

Use when starting a new task, saying "what do I know about", "before I start", "replay", or "remind me about".

Workflow
Extract keywords from the task description (e.g. "auth refactor" → auth, middleware, refactor).
Search learnings/memory for matching patterns:
grep -i "auth\|middleware" .claude/LEARNED.md 2>/dev/null
grep -i "auth\|middleware" .claude/learning-log.md 2>/dev/null
grep -A2 "\[LEARN\]" CLAUDE.md | grep -i "auth\|middleware"

Check session history for similar work — what was the correction rate?
Surface the top learnings ranked by relevance.
If no learnings found, suggest starting with the scout agent to explore first.
Output
REPLAY BRIEFING: <task>
=======================

Past learnings (ranked by relevance):
  1. [Testing] Always mock external APIs in auth tests (applied 8x)
     Mistake: Called live API in tests, caused flaky failures
  2. [Navigation] Auth middleware is in src/middleware/ not src/auth/ (applied 5x)
  3. [Quality] Add error boundary around auth state changes (applied 3x)

Session history for similar work:
  - 2026-02-01: auth refactor — 23 edits, 2 corrections (8.7% rate)
  - 2026-01-28: auth middleware — 15 edits, 4 corrections (26.7% rate)
    ^ Higher correction rate — review patterns before starting

Suggested approach:
  - Mock external APIs (learning #1)
  - Check src/middleware/ first for auth code (learning #2)

Guardrails
Rank by relevance, not recency.
Include the original mistake context so the learning is actionable.
Flag high correction-rate sessions as areas requiring extra care.
If no learnings match, say so explicitly rather than forcing irrelevant results.
Weekly Installs
24
Repository
rohitg00/pro-workflow
GitHub Stars
2.0K
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass