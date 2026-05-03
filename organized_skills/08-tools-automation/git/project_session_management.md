---
rating: ⭐⭐⭐
title: project-session-management
url: https://skills.sh/jezweb/claude-skills/project-session-management
---

# project-session-management

skills/jezweb/claude-skills/project-session-management
project-session-management
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill project-session-management
Summary

Track progress across work sessions using SESSION.md with git checkpoints and concrete next actions.

Converts IMPLEMENTATION_PHASES.md into a living SESSION.md document that maps phases to sessions, tracks current stage (Implementation/Verification/Debugging), and maintains concrete "Next Action" pointers with file locations and line numbers
Provides /wrap-session command to update SESSION.md, create git checkpoints, and output summaries; /continue-session command to load context, show git history, and resume from the last action
Distinguishes phases (units of work with exit criteria) from sessions (units of context), allowing multi-session phases and mid-context checkpoints without losing progress
Uses emoji status icons (⏸️ pending, 🔄 in progress, ✅ complete, 🚫 blocked) and structured checkpoint commits to enable reliable context handoff and phase transitions
SKILL.md
Project Session Management Skill

Track progress across work sessions using SESSION.md with git checkpoints and concrete next actions.

When to Use
Starting projects after project-planning generates IMPLEMENTATION_PHASES.md
Resuming work after context clears
Mid-phase checkpoints when context is full
Phase transitions
Tracking Implementation → Verification → Debugging cycle
Phases vs Sessions

Phases (IMPLEMENTATION_PHASES.md): Units of WORK (e.g., "Database Schema", "Auth API"). Have verification/exit criteria. May span multiple sessions.

Sessions (SESSION.md): Units of CONTEXT. Complete before clearing/compacting context. Can complete a phase, part of a phase, or multiple small phases.

Example: Phase 3 (Tasks API) → Session 1 (GET/POST) → Session 2 (PATCH/DELETE) → Session 3 (verify) ✅

Workflow

Starting New Project:

After project-planning creates IMPLEMENTATION_PHASES.md, offer: "Create SESSION.md to track progress?"
Generate SESSION.md from phases, set Phase 1 as 🔄 (in progress), set concrete "Next Action"

Ending Session:

Automated: /wrap-session (updates SESSION.md, creates checkpoint commit, outputs summary)
Manual: Update SESSION.md → git checkpoint → set concrete "Next Action"

Resuming:

Automated: /continue-session (loads context, shows summary, continues from "Next Action")
Manual: Read SESSION.md → check "Next Action" → continue
Automation Commands

/wrap-session: Analyzes state → updates SESSION.md → updates related docs → creates checkpoint commit → outputs summary → optionally pushes

/continue-session: Loads SESSION.md + planning docs → shows git history + summary → displays verification criteria (if in Verification stage) → opens "Next Action" file → asks permission to continue

SESSION.md Structure

Purpose: Navigation hub referencing planning docs, tracking current progress Target: <200 lines in project root Update: After significant progress (not every change)

Template
# Session State

**Current Phase**: Phase 3
**Current Stage**: Implementation (or Verification/Debugging)
**Last Checkpoint**: abc1234 (2025-10-23)
**Planning Docs**: `docs/IMPLEMENTATION_PHASES.md`, `docs/ARCHITECTURE.md`

---

## Phase 1: Setup ✅
**Completed**: 2025-10-15 | **Checkpoint**: abc1234
**Summary**: Vite + React + Tailwind v4 + D1 binding

## Phase 2: Database ✅
**Completed**: 2025-10-18 | **Checkpoint**: def5678
**Summary**: D1 schema + migrations + seed data

## Phase 3: Tasks API 🔄
**Type**: API | **Started**: 2025-10-23
**Spec**: `docs/IMPLEMENTATION_PHASES.md#phase-3`

**Progress**:
- [x] GET /api/tasks endpoint (commit: ghi9012)
- [x] POST /api/tasks endpoint (commit: jkl3456)
- [ ] PATCH /api/tasks/:id ← **CURRENT**
- [ ] DELETE /api/tasks/:id
- [ ] Verify all endpoints (see IMPLEMENTATION_PHASES.md for criteria)

**Next Action**: Implement PATCH /api/tasks/:id in src/routes/tasks.ts:47, handle validation and ownership check

**Key Files**:
- `src/routes/tasks.ts`
- `src/lib/schemas.ts`

**Known Issues**: None

## Phase 4: Task UI ⏸️
**Spec**: `docs/IMPLEMENTATION_PHASES.md#phase-4`

Status Icons

Use these emoji status icons consistently:

⏸️ = Not started (pending)
🔄 = In progress
✅ = Complete
🚫 = Blocked
Stages Within a Phase
Implementation → Writing code
Verification → Testing against criteria
Debugging → Fixing issues

Update SESSION.md with current stage and progress. Example:

**Current Stage**: Verification

**Verification Progress**:
- [x] GET /api/tasks returns 200 ✅
- [x] POST /api/tasks creates task ✅
- [ ] POST with invalid data returns 400 ❌ (returns 500)

**Current Issue**: Invalid data returning 500. Check src/middleware/validate.ts

SESSION.md Guidelines

✅ Collapse completed phases (2-3 lines), concrete "Next Action" (file+line+task), reference planning docs, checkpoint at phase end or when context full

❌ No code copying, no duplicating IMPLEMENTATION_PHASES.md, no vague actions, keep <200 lines

Git Checkpoint Format
checkpoint: Phase [N] [Status] - [Brief Description]

Phase: [N] - [Name]
Status: [Complete/In Progress/Paused]
Session: [What was accomplished this session]

Files Changed:
- path/to/file.ts (what changed)

Next: [Concrete next action]


Example (Phase Complete):

checkpoint: Phase 3 Complete - Tasks API

Phase: 3 - Tasks API
Status: Complete
Session: Completed all CRUD endpoints and verified functionality

Files Changed:
- src/routes/tasks.ts (all CRUD operations)
- src/lib/schemas.ts (task validation)

Next: Phase 4 - Start building Task List UI component

Expected Uncommitted Files (CRITICAL)

Checkpoint Cycle: /wrap-session creates commit → gets hash → updates SESSION.md with hash. Therefore SESSION.md is always uncommitted when resuming (BY DESIGN).

Expected uncommitted files (no warning):

SESSION.md - Checkpoint hash updated post-commit, always uncommitted between sessions (NORMAL)
CLAUDE.md - Often updated during dev, may be uncommitted (NORMAL)
.roomodes - Editor/IDE state, not relevant to session handoff (SAFE TO IGNORE)

Warning triggers (unexpected):

Source files (.ts, .tsx, .js)
Config files (vite.config.ts, wrangler.jsonc)
Planning docs (IMPLEMENTATION_PHASES.md, ARCHITECTURE.md)
New untracked files

/continue-session behavior:

ℹ️ Info message when only SESSION.md/CLAUDE.md/.roomodes uncommitted
⚠️ Warning when code/doc changes uncommitted (shows filtered list excluding expected files)
Context Management

Context full mid-phase: Update SESSION.md → checkpoint → clear context → read SESSION.md + planning docs → continue from "Next Action"

Phase complete: Check verification criteria → mark 🔄→✅ → checkpoint → move next phase ⏸️→🔄

Troubleshooting: Update to "Debugging" stage → document "Current Issue" → when fixed, return to "Verification" or "Implementation"

Integration with project-planning

project-planning generates IMPLEMENTATION_PHASES.md (the plan) → project-session-management creates SESSION.md (the tracker) → work through phases → git checkpoints → resume from SESSION.md

Planning docs (/docs): Reference material, rarely change SESSION.md (root): Living document, updates constantly

Creating SESSION.md for New Project

After project-planning runs:

Read IMPLEMENTATION_PHASES.md
Create SESSION.md in root: Phase 1 as 🔄, others as ⏸️
Expand Phase 1 with task checklist
Set concrete "Next Action"
Output for review

Offer: "Would you like me to create SESSION.md to track progress through these phases? (clear current phase, progress tracking, easy resume, git checkpoint format)"

Bundled Resources

Templates: SESSION.md.template, checkpoint-commit-format.md, CLAUDE-session-snippet.md

Scripts: resume.sh (show current state)

References: session-handoff-protocol.md, best-practices.md

Weekly Installs
383
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass