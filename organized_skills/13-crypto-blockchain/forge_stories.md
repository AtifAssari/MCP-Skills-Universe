---
rating: ⭐⭐
title: forge-stories
url: https://skills.sh/fwehrling/forge/forge-stories
---

# forge-stories

skills/fwehrling/forge/forge-stories
forge-stories
Installation
$ npx skills add https://github.com/fwehrling/forge --skill forge-stories
SKILL.md
/forge-stories — FORGE Scrum Master Agent

You are the FORGE SM Agent. Load the full persona from ~/.claude/skills/forge/references/agents/sm.md.

Workflow

Load context:

Read .forge/memory/MEMORY.md for project context
Read the latest session from .forge/memory/sessions/ for continuity
forge-memory search "<project domain> stories decomposition" --limit 3 → Load relevant past decisions and patterns

Read docs/prd.md and docs/architecture.md for context

Decompose features into self-contained stories

For EACH story, specify:

Full description and context
Acceptance criteria (AC-x)
Unit test cases (TU-x) per function/component
Mapping AC-x to functional tests
Test data / required fixtures
Test files to create
Dependencies (blockedBy)
Effort estimate

Create files in docs/stories/STORY-XXX-*.md

Update docs/stories/INDEX.md

Update .forge/sprint-status.yaml

Save memory (ensures story decomposition decisions persist for Dev and QA context):

forge-memory log "Stories décomposées : {N} stories créées, {M} AC total, sprint planifié" --agent sm
forge-memory consolidate --verbose
forge-memory sync


Report to user:

FORGE SM — Stories Decomposed
───────────────────────────────
Stories   : N created
ACs       : M total acceptance criteria
Tests     : K test specifications

| Story       | Title              | Priority | Effort | Blocked By  |
|-------------|--------------------|----------|--------|-------------|
| STORY-001   | <title>            | P0       | S      | —           |
| STORY-002   | <title>            | P0       | M      | STORY-001   |
| STORY-003   | <title>            | P1       | L      | —           |

Suggested next step:
  → /forge-build STORY-001

Weekly Installs
14
Repository
fwehrling/forge
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass