---
rating: ⭐⭐⭐
title: forge-auto
url: https://skills.sh/fwehrling/forge/forge-auto
---

# forge-auto

skills/fwehrling/forge/forge-auto
forge-auto
Installation
$ npx skills add https://github.com/fwehrling/forge --skill forge-auto
SKILL.md
/forge-auto — FORGE Autopilot Mode

FORGE takes full control of the development pipeline. It analyzes, decides, executes, verifies, and iterates automatically until the objective is complete.

Principle
The user provides an objective → FORGE handles EVERYTHING else.
Planning → Architecture → Stories → Code → Tests → Verification → Deployment

Workflow

Load memory:

Read .forge/memory/MEMORY.md for project context
Read the latest session from .forge/memory/sessions/ for continuity
Read .forge/sprint-status.yaml for the current state
Read .forge/config.yml for configuration
forge-memory search "<current objective>" --limit 3 → Load relevant past decisions and context

Analyze state and determine the phase:

Inspect the project artifacts and sprint status, then execute the appropriate phase:

No artifacts exist → Start with /forge-plan (generates the PRD)
PRD exists, no architecture → Launch /forge-architect
Architecture exists, no UX design → Launch /forge-ux
UX exists, no stories → Launch /forge-stories
Stories exist with "pending" status:
Count unblocked pending stories
2+ unblocked stories AND Agent Teams available → Delegate to /forge-team build [STORY-IDs] (parallel execution), then continue with QA
Otherwise → Pick the next unblocked story, launch /forge-build STORY-XXX (sequential)
"in_progress" story exists → Resume /forge-build STORY-XXX
Story implemented (Dev tests pass) → Launch /forge-verify STORY-XXX
QA verdict = FAIL → Increment failure counter. Under 3 failures: fix and re-verify. At 3+ failures: escalate to /forge-loop "Fix STORY-XXX: [summary]" --mode hitl which iterates with sandbox guardrails until tests pass
QA verdict = PASS or CONCERNS → Launch /forge-review on the story's source code (adversarial analysis)
Review raises CRITICAL issues → Fix, re-run /forge-verify, re-run /forge-review
Review is clean → Move to the next story
All stories completed → Propose /forge-deploy or new stories

Execute with the appropriate agents:

Each phase invokes the corresponding agent (PM, Architect, UX, SM, Dev, QA)
The agent loads its persona from ~/.claude/skills/forge/references/agents/
The agent produces its artifacts in docs/ or src/
Agent Teams acceleration: when entering the build phase with 2+ unblocked stories, and CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 is set, autopilot delegates to /forge-team build for parallel story implementation (up to 4 Dev + 1 QA). If Agent Teams is not available, stories are built sequentially as before.

Automatic quality gates:

After each story: lint + typecheck + tests > 80% coverage
After each /forge-verify: mandatory QA verdict
After QA PASS/CONCERNS: mandatory /forge-review (adversarial review)
If /forge-review raises critical issues: fix → re-verify → re-review
Loop escalation: if 3 consecutive failures on the same story, autopilot delegates to /forge-loop in HITL mode with the QA failure summary as task. forge-loop iterates with sandbox guardrails (cost cap, circuit breaker, rollback) until tests pass, then returns control to autopilot for re-verification.
Ultimate circuit breaker: if forge-loop also fails (hits its own circuit breaker) → pause + report to user

Save memory:

forge-memory log for each story completed during this session:
forge-memory log "{STORY_ID} terminée : {N} tests, couverture {X}%" --agent dev --story {STORY_ID}

forge-memory log for the session summary:
forge-memory log "Session autopilot terminée : {completed}/{total} stories, phase {PHASE}"

Consolidate session logs into MEMORY.md:
forge-memory consolidate --verbose

Sync the full memory index:
forge-memory sync

Update .forge/sprint-status.yaml

Human checkpoints (configurable):

Default: checkpoint after each major phase (plan, architecture, stories)
--no-pause mode: no checkpoints (full autopilot)
--pause-stories mode: pause after story decomposition
--pause-each mode: pause after each story
Options
# Full autopilot — FORGE decides everything
/forge-auto

# Autopilot with a specific objective
/forge-auto "Implement the authentication system"

# Autopilot without pauses (warning: fully autonomous)
/forge-auto --no-pause

# Autopilot with pause after stories
/forge-auto --pause-stories

# Autopilot with pause after each story
/forge-auto --pause-each

# Resume autopilot after a pause
/forge-auto --resume

Progress Report

At each step, FORGE displays:

FORGE AUTOPILOT — Progress
──────────────────────────────
Phase     : Development (Story 3/8)
Last      : STORY-002 ✓ (QA: PASS)
Current   : STORY-003 — Implementation
Next      : STORY-004 (pending)

Metrics:
  Stories   : 2 completed / 1 in_progress / 5 pending
  Tests     : 47 pass / 0 fail
  Coverage  : 87%

Memory    : .forge/memory/MEMORY.md (up to date)
Session   : .forge/memory/sessions/YYYY-MM-DD.md

How /forge-auto Uses Other FORGE Tools
Situation	Autopilot delegates to	Condition
2+ unblocked stories ready	/forge-team build (parallel)	Agent Teams enabled
1 story ready	/forge-build STORY-XXX (sequential)	Always
Story implemented (Dev tests pass)	/forge-verify STORY-XXX (QA audit)	Always
QA verdict PASS/CONCERNS	/forge-review src/{MODULE}/ (adversarial review)	Always
Review raises critical issues	Fix → /forge-verify → /forge-review	Always
3 consecutive failures on a story	/forge-loop (iterative fix)	Always
forge-loop also fails	Pause + report to user	Ultimate circuit breaker
Difference with /forge-loop
Aspect	/forge-loop	/forge-auto
Scope	A specific task	The entire project
Decision	The user chooses the task	FORGE decides the next action
Agents	A single one (usually Dev)	All agents depending on the phase
Memory	Local fix_plan.md	Persistent project memory
Progression	Linear (iterations)	Full pipeline (plan → deploy)
Use case	"Implement this feature"	"Build this project from A to Z"
Relation	Standalone or called by auto	Calls /forge-loop on difficult stories
Coexistence with Manual Mode

Autopilot and manual commands are 100% compatible:

You can start with /forge-auto, pause, then continue manually
You can work manually then launch /forge-auto --resume to continue
Memory is shared: both modes read/write the same files
/forge-status works in both modes
Notes
Autopilot ALWAYS respects quality gates (no shortcuts)
The circuit breaker protects against infinite loops
Persistent memory ensures continuity between sessions
Compatible with projects initialized via /forge-init
Also works for resuming existing projects (analyzes the state)
Weekly Installs
15
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