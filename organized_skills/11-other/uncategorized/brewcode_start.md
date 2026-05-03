---
rating: ⭐⭐⭐
title: brewcode:start
url: https://skills.sh/kochetkov-ma/claude-brewcode/brewcode:start
---

# brewcode:start

skills/kochetkov-ma/claude-brewcode/brewcode:start
brewcode:start
Installation
$ npx skills add https://github.com/kochetkov-ma/claude-brewcode --skill brewcode:start
SKILL.md

Execute Task — [task-file-path]

How It Works
/brewcode:start -> Load PLAN.md -> Parse Phase Registry
   |
   v
TaskCreate for each row -> TaskUpdate dependencies
   |
   v
Execution Loop: TaskList() -> pending+unblocked -> spawn agents
   |
   v
Per agent: WRITE report -> CALL bc-coordinator (2-step, ALWAYS)
   |
   v
TaskUpdate(completed) -> repeat -> Finalize
   |
   v
After compact: TaskList() -> Read PLAN.md -> continue

Execution Steps
1. Resolve Task Path
If $ARGUMENTS has path -> use it
If $ARGUMENTS empty -> read .claude/TASK.md (first line = active path)
If neither -> STOP: No task path! Run: /brewcode:spec "description" then /brewcode:plan
2. Initialize via Coordinator (REQUIRED)
Task tool:
  subagent_type: "brewcode:bc-coordinator"
  prompt: "Mode: initialize. Task path: {TASK_PATH}"


Coordinator validates, creates lock, updates status -> in progress.

3. Load Context
Read PLAN.md (ONLY PLAN.md from the task directory)
Read KNOWLEDGE.jsonl if exists
Verify artifacts/ directory exists
DO NOT read phases/ files -- they are for agents, not the manager
4. Create Tasks from Phase Registry

Parse the ## Phase Registry table in PLAN.md.

FOR each row in Phase Registry:
  TaskCreate(
    subject  = "Phase {#}: {Subject}",
    description = "Phase {#}: {Summary}\n\nFull instructions: phases/{Phase File}\nTask dir: {TASK_DIR}\nArtifacts: artifacts/{Artifact Dir from Phase Registry}/\nKNOWLEDGE: KNOWLEDGE.jsonl",
    activeForm = "{Present continuous of Subject}"
  )


Sub-step 4a: Phase-to-TaskID Map Task IDs are auto-incremented (1,2,3...) and may NOT match Phase # (1,1V,2,3...). Build a map: {phase# -> taskId} during creation. Include phase # explicitly in description.

5. Set Dependencies
FOR each row where "Blocked By" column is non-empty:
  TaskUpdate(taskId, addBlockedBy=[mapped task IDs from Blocked By column])

6. Execution Loop
LOOP while pending tasks remain:
  a. TaskList() -> find tasks: status=pending, blockedBy=[]
  b. Same Parallel group -> spawn in ONE message (parallel Task calls)
  c. Per task:
     i.   TaskUpdate(taskId, status="in_progress")
     ii.  Task(subagent_type="{Agent from Phase Registry}", prompt from description)
     -- If agent FAILED (is_error=true):
        a. TaskUpdate(taskId, status="in_progress") -- keep in progress for retry
        b. Persist failure to KNOWLEDGE.jsonl:
           {"ts":"...","t":"❌","txt":"Phase {N} agent failed: {error_summary}. Attempt {I}/{MAX}.","src":"manager"}
        c. Retry once with same agent
        d. If retry fails: TaskUpdate(taskId, status="failed"), apply Escalation table
        e. Skip steps iii-v (no report to write, no coordinator to call)
     -- If agent SUCCEEDED:
        iii. WRITE report -> artifacts/{P}-{N}{T}/{AGENT}_output.md
        iv.  Task(subagent_type="brewcode:bc-coordinator",
                  prompt="Mode: standard. Task path: {TASK_PATH}. Report: {REPORT_PATH}")
             -- If coordinator FAILED (is_error=true): log warning, proceed to TaskUpdate(completed)
        v.   TaskUpdate(taskId, status="completed")
  d. On verification FAIL:
     i.   Read verification report from artifacts/{P}-{N}{T}/{VERIFY_AGENT}_output.md
          (manager can read artifacts/ — the rule is NEVER read phases/)
          Extract: {ISSUES_TABLE}, {FILES_TO_FIX} from the issues table in the report
          {VERIFY_AGENT} = agent from the verification row in Phase Registry
          {VERIFY_ARTIFACT_DIR} = artifact dir of the verification phase
     ii.  Write phases/{N}F{I}-fix-{name}.md using phase-fix.md.template
          (from .claude/tasks/templates/ or $BC_PLUGIN_ROOT/skills/setup/templates/)
          Fill: {PHASE_NUM}, {ITERATION}, {PHASE_NAME}, {FIX_AGENT}=original agent,
          {ORIGINAL_PHASE_FILE}, {VERIFY_ARTIFACT_DIR}, {VERIFY_AGENT},
          {ISSUES_TABLE} from verification report (step 6.d.i), {FILES_TO_FIX}, {ARTIFACT_DIR}
     iii. TaskCreate(subject="Fix phase {N} issues (iter {I})", ...)
     iv.  TaskCreate(subject="Re-verify phase {N} (iter {I+1})",
               addBlockedBy=[fix task ID])
     v.   Max 3 iterations -> Escalation
  e. Deadlock check after each iteration:
     TaskList() -> categorize:
     - ready = pending + blockedBy=[]
     - blocked = pending + blockedBy non-empty
     - active = in_progress
     If ready=0 AND active=0 AND blocked>0:
       DEADLOCK -> cascade failure to all blocked tasks, BREAK -> Finalize(status="failed")
     If ready=0 AND active=0 AND blocked=0:
       ALL DONE -> BREAK -> Finalize(status="finished")
     Else: continue loop


Escalation after repeated failures:

After	Action
1 fail	R&D task: explore root cause
2 fails	Split phase into sub-phases
3 fails	Upgrade model, reassign, AskUserQuestion
Failure Cascade

When escalation exhausted (task permanently failed):

TaskUpdate(failedTaskId, status="failed")
Persist to KNOWLEDGE.jsonl: {"ts":"...","t":"❌","txt":"Phase {N} permanently failed: {reason}","src":"manager"}
Cascade: TaskList() -> for each task T where failedTaskId in T.blockedBy (transitive): TaskUpdate(T.id, status="failed")
Log: "Phase {N} permanently failed. Cascaded to {count} dependent tasks."
Independent tasks (no dependency on failed task) continue normally
7. Finalize
Task(subagent_type="brewcode:bc-coordinator",
     prompt="Mode: finalize. Task path: {TASK_PATH}. Status: {finished|failed}")


Status is "finished" when all tasks completed, "failed" when deadlock/cascade occurred.

8. Extract Rules (REQUIRED)
Skill(skill="brewcode:rules", args="{KNOWLEDGE_PATH}")

9. Prune Knowledge (REQUIRED)
Task(subagent_type="brewcode:bc-knowledge-manager",
     prompt="mode: prune-rules\ntaskPath: {TASK_PATH}")

Handoff (After Compact)
TaskList() -- current task state (source of truth)
Read PLAN.md -- protocol and Phase Registry
DO NOT read phases/ -- they are for agents
Continue with current in_progress or next pending task
WRITE report -> CALL coordinator after EVERY agent (ALWAYS)
Weekly Installs
13
Repository
kochetkov-ma/cl…brewcode
GitHub Stars
25
First Seen
Mar 2, 2026