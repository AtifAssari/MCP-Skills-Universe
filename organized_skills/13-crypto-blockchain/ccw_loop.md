---
rating: ⭐⭐⭐
title: ccw-loop
url: https://skills.sh/catlog22/claude-code-workflow/ccw-loop
---

# ccw-loop

skills/catlog22/claude-code-workflow/ccw-loop
ccw-loop
Installation
$ npx skills add https://github.com/catlog22/claude-code-workflow --skill ccw-loop
SKILL.md
CCW Loop - Stateless Iterative Development Workflow

Stateless iterative development loop using Codex single-agent deep interaction pattern. One agent handles all phases (develop → debug → validate → complete) via send_input, with file-based state tracking and Dashboard integration.

Architecture Overview
+-------------------------------------------------------------+
|                     Dashboard (UI)                           |
|  [Create] [Start] [Pause] [Resume] [Stop] [View Progress]  |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|              loop-v2-routes.ts (Control Plane)               |
|                                                              |
|  State: {projectRoot}/.workflow/.loop/{loopId}.json (MASTER)  |
|  Tasks: {projectRoot}/.workflow/.loop/{loopId}.tasks.jsonl   |
|                                                              |
|  /start  -> Trigger ccw-loop skill with --loop-id           |
|  /pause  -> Set status='paused' (skill checks before action) |
|  /stop   -> Set status='failed' (skill terminates)          |
|  /resume -> Set status='running' (skill continues)          |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|               ccw-loop Skill (Execution Plane)               |
|                                                              |
|  Single Agent Deep Interaction:                              |
|    spawn_agent -> wait -> send_input -> ... -> close_agent   |
|                                                              |
|  Actions: INIT -> DEVELOP -> DEBUG -> VALIDATE -> COMPLETE   |
+-------------------------------------------------------------+

Key Design Principles
Single Agent Deep Interaction: One agent handles entire loop lifecycle via send_input (no multi-agent overhead)
Unified State: API and Skill share {projectRoot}/.workflow/.loop/{loopId}.json state file
Control Signals: Skill checks status field before each action (paused/stopped → graceful exit)
File-Driven Progress: All progress documented in {projectRoot}/.workflow/.loop/{loopId}.progress/
Resumable: Continue any loop with --loop-id
Dual Trigger: Supports API trigger (--loop-id) and direct call (task description)
Arguments
Arg	Required	Description
TASK	One of TASK or --loop-id	Task description (for new loop)
--loop-id	One of TASK or --loop-id	Existing loop ID to continue
--auto	No	Auto-cycle mode (develop → debug → validate → complete)
Execution Modes
Mode 1: Interactive

User manually selects each action via menu.

User -> MENU -> Select action -> Execute -> View results -> MENU -> ...

Mode 2: Auto-Loop

Automatic execution using selectNextAction logic.

INIT -> DEVELOP -> ... -> VALIDATE -> (if fail) -> DEBUG -> VALIDATE -> COMPLETE

Execution Flow
Input Parsing:
   └─ Parse arguments (TASK | --loop-id + --auto)
   └─ Convert to structured context (loopId, state, progressDir)

Phase 1: Session Initialization
   └─ Ref: phases/01-session-init.md
      ├─ Create new loop OR resume existing loop
      ├─ Initialize state file and directory structure
      └─ Output: loopId, state, progressDir

Phase 2: Orchestration Loop
   └─ Ref: phases/02-orchestration-loop.md
      ├─ Spawn single executor agent
      ├─ Main while loop: wait → parse → dispatch → send_input
      ├─ Handle: COMPLETED / PAUSED / STOPPED / WAITING_INPUT / next action
      ├─ Update iteration count per cycle
      └─ close_agent on exit


Phase Reference Documents (read on-demand when phase executes):

Phase	Document	Purpose
1	phases/01-session-init.md	Argument parsing, state creation/resume, directory init
2	phases/02-orchestration-loop.md	Agent spawn, main loop, result parsing, send_input dispatch
Data Flow
User Input (TASK | --loop-id + --auto)
    ↓
[Parse Arguments]
    ↓ loopId, state, progressDir

Phase 1: Session Initialization
    ↓ loopId, state (initialized/resumed), progressDir

Phase 2: Orchestration Loop
    ↓ spawn agent → [INIT] → wait → parse
    ↓
    ┌─── Main Loop (while iteration < max) ──────────┐
    │ wait() → parseActionResult(output)               │
    │   ├─ COMPLETED → close_agent, return             │
    │   ├─ PAUSED → close_agent, return                │
    │   ├─ STOPPED → close_agent, return               │
    │   ├─ WAITING_INPUT → collect input → send_input  │
    │   └─ next_action → send_input(continue)          │
    │ Update iteration in state file                   │
    └──────────────────────────────────────────────────┘
    ↓
close_agent → return finalState

Session Structure
{projectRoot}/.workflow/.loop/
├── {loopId}.json              # Master state file (API + Skill shared)
├── {loopId}.tasks.jsonl       # Task list (API managed)
└── {loopId}.progress/         # Skill progress files
    ├── develop.md             # Development progress timeline
    ├── debug.md               # Understanding evolution document
    ├── validate.md            # Validation report
    ├── changes.log            # Code changes log (NDJSON)
    ├── debug.log              # Debug log (NDJSON)
    ├── hypotheses.json        # Debug hypotheses tracking
    ├── test-results.json      # Test execution results
    ├── coverage.json          # Coverage data
    └── summary.md             # Completion summary

State Management

Master state file: {projectRoot}/.workflow/.loop/{loopId}.json

{
  "loop_id": "loop-v2-20260122T100000-abc123",
  "title": "Task title",
  "description": "Full task description",
  "max_iterations": 10,
  "status": "created | running | paused | completed | failed | user_exit",
  "current_iteration": 0,
  "created_at": "ISO8601",
  "updated_at": "ISO8601",
  "completed_at": "ISO8601 (optional)",
  "failure_reason": "string (optional)",

  "skill_state": {
    "current_action": "init | develop | debug | validate | complete | null",
    "last_action": "string | null",
    "completed_actions": [],
    "mode": "interactive | auto",

    "develop": {
      "total": 0, "completed": 0, "current_task": null,
      "tasks": [{ "id": "task-001", "description": "...", "tool": "gemini", "mode": "write", "status": "pending", "files_changed": [], "created_at": "ISO8601", "completed_at": null }],
      "last_progress_at": null
    },

    "debug": {
      "active_bug": null, "hypotheses_count": 0,
      "hypotheses": [{ "id": "H1", "description": "...", "testable_condition": "...", "logging_point": "file:func:line", "evidence_criteria": { "confirm": "...", "reject": "..." }, "likelihood": 1, "status": "pending", "evidence": null, "verdict_reason": null }],
      "confirmed_hypothesis": null, "iteration": 0, "last_analysis_at": null
    },

    "validate": {
      "pass_rate": 0, "coverage": 0,
      "test_results": [{ "test_name": "...", "suite": "...", "status": "passed | failed | skipped", "duration_ms": 0, "error_message": null, "stack_trace": null }],
      "passed": false, "failed_tests": [], "last_run_at": null
    },

    "errors": [{ "action": "...", "message": "...", "timestamp": "ISO8601" }],

    "summary": { "duration": 0, "iterations": 0, "develop": {}, "debug": {}, "validate": {} }
  }
}


Control Signal Checking: Agent checks state.status before every action:

running → continue
paused → exit gracefully, wait for resume
failed → terminate
Other → stop

Recovery: If state corrupted, rebuild skill_state from {projectRoot}/.workflow/.loop/{loopId}.progress/ markdown files and logs.

Action Catalog
Action	Purpose	Preconditions	Output Files	Trigger
INIT	Initialize session	status=running, skill_state=null	develop.md, state.json	First run
DEVELOP	Execute dev task	pending tasks > 0	develop.md, changes.log	Has pending tasks
DEBUG	Hypothesis debug	needs debugging	debug.md, debug.log	Test failures
VALIDATE	Run tests	needs validation	validate.md, test-results.json	After develop/debug
COMPLETE	Finish loop	all done	summary.md	All tasks done
MENU	Display menu	interactive mode	-	Interactive mode
Action Flow
spawn_agent (ccw-loop-executor)
       |
       v
   +-------+
   |  INIT |  (if skill_state is null)
   +-------+
       |
       v
   +-------+    send_input
   |  MENU | <------------- (user selection in interactive mode)
   +-------+
       |
   +---+---+---+---+
   |   |   |   |   |
   v   v   v   v   v
 DEV DBG VAL CMP EXIT
       |
       v
   wait() -> get result
       |
       v
   [Loop continues via send_input]
       |
       v
  close_agent()

Action Dependencies
Action	Depends On	Leads To
INIT	-	MENU or DEVELOP
MENU	INIT	User selection
DEVELOP	INIT	DEVELOP, DEBUG, VALIDATE
DEBUG	INIT	DEVELOP, VALIDATE
VALIDATE	DEVELOP or DEBUG	COMPLETE, DEBUG, DEVELOP
COMPLETE	-	Terminal
Action Sequences
Happy Path (Auto):  INIT → DEVELOP → DEVELOP → VALIDATE (pass) → COMPLETE
Debug Iteration:    INIT → DEVELOP → VALIDATE (fail) → DEBUG → VALIDATE (pass) → COMPLETE
Interactive Path:   INIT → MENU → DEVELOP → MENU → VALIDATE → MENU → COMPLETE

Auto Mode Selection Logic
function selectNextAction(state) {
  const skillState = state.skill_state

  // 1. Terminal conditions
  if (state.status === 'completed') return null
  if (state.status === 'failed') return null
  if (state.current_iteration >= state.max_iterations) return 'COMPLETE'

  // 2. Initialization check
  if (!skillState) return 'INIT'

  // 3. Auto selection based on state
  const hasPendingDevelop = skillState.develop.tasks.some(t => t.status === 'pending')

  if (hasPendingDevelop) return 'DEVELOP'

  if (skillState.last_action === 'DEVELOP') {
    if (skillState.develop.completed < skillState.develop.total) return 'DEBUG'
  }

  if (skillState.last_action === 'DEBUG' || skillState.debug.confirmed_hypothesis) {
    return 'VALIDATE'
  }

  if (skillState.last_action === 'VALIDATE') {
    if (!skillState.validate.passed) return 'DEVELOP'
  }

  if (skillState.validate.passed && !hasPendingDevelop) return 'COMPLETE'

  return 'DEVELOP'
}

Coordination Protocol
Agent → Orchestrator (ACTION_RESULT)

Every action MUST output:

ACTION_RESULT:
- action: {ACTION_NAME}
- status: success | failed | needs_input
- message: {user-facing message}
- state_updates: { ... }

FILES_UPDATED:
- {file_path}: {description}

NEXT_ACTION_NEEDED: {ACTION_NAME} | WAITING_INPUT | COMPLETED | PAUSED

Orchestrator → Agent (send_input)

Auto mode continuation:

## CONTINUE EXECUTION

Previous action completed: {action}
Result: {status}

## EXECUTE NEXT ACTION

Continue with: {next_action}
Read action instructions and execute.
Output ACTION_RESULT when complete.


Interactive mode user input:

## USER INPUT RECEIVED

Action selected: {action}

## EXECUTE SELECTED ACTION

Read action instructions and execute: {action}
Update state and progress files accordingly.
Output ACTION_RESULT when complete.

Codex Subagent API
API	Purpose
spawn_agent({ message })	Create subagent, returns agent_id
wait({ ids, timeout_ms })	Wait for results (only way to get output)
send_input({ id, message })	Continue interaction / follow-up
close_agent({ id })	Close and reclaim (irreversible)

Rules: Single agent for entire loop. send_input for multi-phase. close_agent only after confirming no more interaction needed.

TodoWrite Pattern
Phase-Level Tracking (Attached)
[
  {"content": "Phase 1: Session Initialization", "status": "completed"},
  {"content": "Phase 2: Orchestration Loop", "status": "in_progress"},
  {"content": "  → Action: INIT", "status": "completed"},
  {"content": "  → Action: DEVELOP (task 1/3)", "status": "in_progress"},
  {"content": "  → Action: VALIDATE", "status": "pending"},
  {"content": "  → Action: COMPLETE", "status": "pending"}
]

Iteration Tracking (Collapsed)
[
  {"content": "Phase 1: Session Initialization", "status": "completed"},
  {"content": "Iteration 1: DEVELOP x3 + VALIDATE (pass)", "status": "completed"},
  {"content": "Phase 2: COMPLETE", "status": "in_progress"}
]

Core Rules
Start Immediately: First action is TodoWrite initialization, then Phase 1 execution
Progressive Phase Loading: Read phase docs ONLY when that phase is about to execute
Parse Every Output: Extract ACTION_RESULT from agent output for next decision
Auto-Continue: After each action, execute next pending action automatically (auto mode)
Track Progress: Update TodoWrite dynamically with attachment/collapse pattern
Single Writer: Orchestrator updates master state file; agent writes to progress files
File References: Pass file paths between orchestrator and agent, not content
DO NOT STOP: Continuous execution until COMPLETED, PAUSED, STOPPED, or max iterations
Error Handling
Error Type	Recovery
Agent timeout	send_input requesting convergence, then retry
State corrupted	Rebuild from progress markdown files and logs
Agent closed unexpectedly	Re-spawn with previous output in message
Action failed	Log error, continue or prompt user
Tests fail	Loop back to DEVELOP or DEBUG
Max iterations reached	Generate summary with remaining issues documented
Session not found	Create new session
Coordinator Checklist
Before Each Phase
 Read phase reference document
 Check current state for dependencies
 Update TodoWrite with phase tasks
After Each Phase
 Parse agent outputs (ACTION_RESULT)
 Update master state file (iteration count, updated_at)
 Collapse TodoWrite sub-tasks
 Determine next action (continue / iterate / complete)
Reference Documents
Document	Purpose
actions/	Action definitions (INIT, DEVELOP, DEBUG, VALIDATE, COMPLETE, MENU)
Usage
# Start new loop (direct call)
/ccw-loop TASK="Implement user authentication"

# Auto-cycle mode
/ccw-loop --auto TASK="Fix login bug and add tests"

# Continue existing loop
/ccw-loop --loop-id=loop-v2-20260122-abc123

# API triggered auto-cycle
/ccw-loop --loop-id=loop-v2-20260122-abc123 --auto

Weekly Installs
12
Repository
catlog22/claude…workflow
GitHub Stars
1.9K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass