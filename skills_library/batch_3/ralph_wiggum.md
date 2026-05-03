---
title: ralph-wiggum
url: https://skills.sh/fstandhartinger/ralph-wiggum/ralph-wiggum
---

# ralph-wiggum

skills/fstandhartinger/ralph-wiggum/ralph-wiggum
ralph-wiggum
Installation
$ npx skills add https://github.com/fstandhartinger/ralph-wiggum --skill ralph-wiggum
Summary

Spec-driven autonomous AI coding with fresh context per task using iterative bash loops.

Implements Geoffrey Huntley's methodology where each loop iteration starts a new agent process with a clean context window, preventing degradation over long sessions
Requires clear, testable acceptance criteria in specification files; agent outputs <promise>DONE</promise> only when all criteria are verified and tests pass
Maintains shared state on disk via specs/, ralph_history.txt, and optional IMPLEMENTATION_PLAN.md for persistence across iterations
Supports two modes: build (default, for implementation) and plan (for task breakdown); works with Claude Code and Codex CLI
SKILL.md
Ralph Wiggum

Autonomous AI coding with spec-driven development

What is Ralph Wiggum?

Ralph Wiggum combines Geoffrey Huntley's iterative bash loop with spec-driven development for fully autonomous AI-assisted software development.

The key insight: Fresh context each iteration. Each loop starts a new agent process with a clean context window, preventing context overflow and degradation.

When to Use This Skill

Use Ralph Wiggum when:

You have multiple specifications/features to implement
You want the AI to work autonomously through tasks
You need consistent, verifiable completion of acceptance criteria
You want to avoid context window problems in long sessions
How It Works
┌─────────────────────────────────────────────────────────────┐
│                     RALPH LOOP                              │
├─────────────────────────────────────────────────────────────┤
│  Loop 1: Pick spec A → Implement → Test → Commit → DONE    │
│  Loop 2: Pick spec B → Implement → Test → Commit → DONE    │
│  Loop 3: Pick spec C → Implement → Test → Commit → DONE    │
│  ...                                                        │
│                                                             │
│  Each iteration = Fresh context window                      │
│  Shared state = Files on disk (specs, plan, history)        │
└─────────────────────────────────────────────────────────────┘

Installation
Quick Install (via Skill Installers)
# Using Vercel's add-skill
npx add-skill fstandhartinger/ralph-wiggum

# Using OpenSkills
openskills install fstandhartinger/ralph-wiggum

Full Setup (Recommended)

For full Ralph Wiggum setup with constitution and interview:

# Tell your AI agent:
"Set up Ralph Wiggum using https://github.com/fstandhartinger/ralph-wiggum"


The agent will guide you through a lightweight, pleasant setup:

Quick Setup (~1 min) — Create directories, download scripts
Project Interview — Focus on your vision and goals (not tech details)
Constitution — Create a guiding document for all sessions
Next Steps — Clear guidance on creating specs and starting Ralph

For existing projects, the agent detects your tech stack automatically. The interview prioritizes understanding what you're building and why.

Core Concepts
1. Fresh Context Each Loop

Each iteration of the Ralph loop starts a new AI agent process. This means:

No context window overflow
No degradation over time
Clean slate for each task
2. Shared State on Disk

State persists between loops via files:

specs/ — Feature specifications with acceptance criteria
ralph_history.txt — Log of breakthroughs, blockers, learnings
IMPLEMENTATION_PLAN.md — Optional detailed task breakdown
3. Completion Signal

The agent outputs <promise>DONE</promise> ONLY when:

All acceptance criteria are verified
Tests pass
Changes are committed and pushed

The bash loop checks for this phrase. If not found, it retries.

4. Backpressure via Tests

Tests, lints, and builds act as guardrails. The agent must fix issues before outputting the completion signal.

Usage
Creating Specifications

The key to success: Each spec needs clear, testable acceptance criteria. This is what tells Ralph when a task is truly "done."

# Feature: User Authentication

## Requirements
- OAuth login with Google
- Session management
- Logout functionality

## Acceptance Criteria
- [ ] User can log in with Google
- [ ] Session persists across page reloads
- [ ] User can log out
- [ ] Tests pass

**Output when complete:** `<promise>DONE</promise>`


Good criteria: "User can log in with Google and session persists" Bad criteria: "Auth works correctly"

The more specific your acceptance criteria, the better Ralph performs.

Running the Loop
# Start building (Claude Code)
./scripts/ralph-loop.sh

# With max iterations
./scripts/ralph-loop.sh 20

# Using Codex CLI
./scripts/ralph-loop-codex.sh

Logging (All Output Captured)

Every loop run writes all output to log files in logs/:

Session log: logs/ralph_*_session_YYYYMMDD_HHMMSS.log (entire run, including CLI output)
Iteration logs: logs/ralph_*_iter_N_YYYYMMDD_HHMMSS.log (per-iteration CLI output)
Codex last message: logs/ralph_codex_output_iter_N_*.txt
Two Modes
Mode	Purpose	Command
build (default)	Pick spec, implement, test, commit	./scripts/ralph-loop.sh
plan (optional)	Create detailed task breakdown	./scripts/ralph-loop.sh plan
Key Principles
Let Ralph Ralph

Trust the AI to self-identify, self-correct, and self-improve. Observe patterns and adjust prompts.

YOLO Mode

For Ralph to work effectively, enable full autonomy:

Claude Code: --dangerously-skip-permissions
Codex: --dangerously-bypass-approvals-and-sandbox

⚠️ Use at your own risk. Only in sandboxed environments.

Links
GitHub: https://github.com/fstandhartinger/ralph-wiggum
Website: https://ralph-wiggum.ai
Original methodology: Geoffrey Huntley's how-to-ralph-wiggum
Weekly Installs
751
Repository
fstandhartinger…h-wiggum
GitHub Stars
228
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn