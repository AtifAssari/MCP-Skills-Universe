---
title: clarifying-assumptions
url: https://skills.sh/b-mendoza/agent-skills/clarifying-assumptions
---

# clarifying-assumptions

skills/b-mendoza/agent-skills/clarifying-assumptions
clarifying-assumptions
Installation
$ npx skills add https://github.com/b-mendoza/agent-skills --skill clarifying-assumptions
SKILL.md
Clarifying Assumptions

This skill is the conversation layer for workflow orchestration. It accepts a TICKET_KEY that can be a Jira ticket key (JNS-6065) or a GitHub issue slug (acme-app-42). The orchestrator does exactly three things: think about the current question and the developer's reasoning, decide what to ask or defer next, and dispatch subagents for artifact reading, critique generation, manifest assembly, and file updates. critique-analyzer writes its full report to a workflow artifact before manifest assembly so the orchestrator carries only summaries, manifest rows, and artifact paths instead of raw planning content.

Inputs
Input	Required	Example
TICKET_KEY	Yes	JNS-6065 or acme-app-42
MODE	Yes	upfront or critique
TASK_NUMBER	Required for MODE=critique	3
ITERATION	No	1, 2, or 3

<KEY> in path examples below is the same value as TICKET_KEY.

The main task plan must already exist at docs/<TICKET_KEY>-tasks.md. The required plan sections and artifact contracts are part of this skill's preconditions and are defined below.

When MODE=critique, these per-task artifacts must also exist:

docs/<KEY>-task-<N>-brief.md
docs/<KEY>-task-<N>-execution-plan.md
docs/<KEY>-task-<N>-test-spec.md
docs/<KEY>-task-<N>-refactoring-plan.md

The skill derives these additional subagent handoff inputs from the top-level inputs:

Dispatch target	Derived inputs
critique-analyzer	MAIN_PLAN_FILE, ARTIFACTS, CRITIQUE_REPORT_FILE, PRIOR_DECISIONS_FILE, PRIOR_DECISIONS_KIND (main-log in MODE=upfront, per-task in MODE=critique), and in MODE=critique TASK_NUMBER
question-manifest-builder	PLAN_FILE, CRITIQUE_REPORT_FILE, and in MODE=critique TASK_NUMBER plus CURRENT_TASK_ARTIFACTS
decision-recorder	ITERATION, DECISIONS, optional DEFERRED_QUESTIONS, optional IMPLEMENTATION_UPDATES, and in MODE=critique TASK_NUMBER, TASK_TITLE, plus RESOLVED_IRRELEVANT
Input and Output Contracts
Input contract

The main plan file at docs/<TICKET_KEY>-tasks.md must contain these sections:

Section	Used for
## Ticket Summary or ## Issue Summary	Platform-native summary section consumed upstream; either heading satisfies this input contract
## Problem Framing	Tier 3 hard-gate questions and user-impact context
## Assumptions and Constraints	Assumptions to confirm, revise, or defer
## Cross-Cutting Open Questions	Plan-wide blocking questions
## Tasks	Task-specific questions and assumptions
## Validation Report	Validation FAIL and WARN items
## Dependency Graph	Impact mapping and downstream task references

Additional upstream artifacts:

MODE=upfront: docs/<KEY>-stage-1-detailed.md, docs/<KEY>-stage-2-prioritized.md
MODE=critique: task brief, execution plan, test spec, and refactoring plan

These sections and upstream artifacts are required input preconditions for the skill. This skill requires only the paths above plus readable markdown at those locations.

Output contract

This skill updates orchestration artifacts only. It does not produce implementation code.

Artifact	Required result
docs/<KEY>-upfront-critique.md or docs/<KEY>-task-<N>-critique.md	Full critique report written before manifest assembly so later steps consume the artifact path instead of the full report body
docs/<KEY>-tasks.md updates	Main plan updated so downstream execution consumes resolved decisions instead of open ambiguity
## Decisions Log rows	Durable audit trail for plan-wide and task-level clarification decisions
Deferred question tags	Later critique-mode runs can identify which questions must be revisited later
docs/<KEY>-task-<N>-decisions.md	Critique-mode record of task-level decisions for re-planning and execution
RE_PLAN_NEEDED in the final summary	Signals whether planning should be re-run before execution
BLOCKERS_PRESENT in the final summary	Signals that clarification ended with unresolved items and execution must not proceed

These are orchestration artifacts. Keep them out of version control.

Final summary contract

Every successful run ends with a concise final summary that includes at minimum these fields in a stable shape:

Critique artifact: <path>
Files updated: <path list or ->
RE_PLAN_NEEDED: <true|false>
BLOCKERS_PRESENT: <true|false>

If clarification stops early because a subagent returned BLOCKED, FAIL, or ERROR, still emit the same minimum fields with Files updated: - plus the blocking verdict and reason.

Canonical Pipeline Stages

Use the same stage names and ordering regardless of whether the caller is a Jira workflow or a GitHub workflow.

Stage	Name	Purpose
1	Load guidance	Read the design-thinking reference and the active mode playbook
2	Analyze artifacts	Dispatch critique-analyzer to read artifacts, consult the Decisions Log, inspect the codebase, and write the critique artifact
3	Build manifest	Dispatch question-manifest-builder to turn the critique artifact plus plan context into the ordered manifest
4	Clarify inline	Walk the manifest one item at a time with the developer and capture decisions
5	Record decisions	Dispatch decision-recorder to update workflow artifacts, validate them, and return the final write summary

Manifest preview belongs inside Stage 4. Final user-facing recap belongs inside Stage 5 after the recorder returns. Do not invent extra pipeline stages for those two presentation steps.

Pipeline / Workflow Overview
Mode	Goal	Delegated work	Inline work
upfront	Challenge the whole plan before execution starts	critique generation with Decisions Log dedup, manifest assembly, file updates	Socratic questioning and decision capture
critique	Challenge one task just before execution	critique generation with Decisions Log dedup, manifest assembly, file updates	Evaluate reasoning and make final task-level decisions
Subagent Registry
Subagent	Path	Purpose
critique-analyzer	./subagents/critique-analyzer.md	Reads planning artifacts, consults the Decisions Log on every run, verifies the real codebase, searches the web, writes the critique artifact, and returns a concise verdict plus artifact path
question-manifest-builder	./subagents/question-manifest-builder.md	Reads the task plan plus the critique report and returns an ordered manifest of what to ask now, what to defer, and what is no longer relevant
decision-recorder	./subagents/decision-recorder.md	Writes clarification artifacts, updates the main task plan, creates per-task decisions files when needed, and validates the result
How This Skill Works

Keep only these items inline while the skill is running:

The current manifest item
The developer's response
The accumulated decision list
The RE_PLAN_NEEDED flag
The BLOCKERS_PRESENT flag
The active critique artifact path

Everything else comes from delegated subagents through concise verdicts, manifest rows, and artifact paths. The manifest is the source of truth for what gets asked once execution starts, but critique-analyzer is the source of truth for whether a concern still needs to be raised at all in the current run.

MODE=upfront is the plan-wide clarification pass and MODE=critique is the per-task clarification pass just before execution. The mode names, inputs, and artifact paths are the runtime contract; any parent-workflow phase numbers are outside this skill's contract.

On retries or later iterations, re-dispatch each subagent with the current artifact paths and inputs. Do not treat prior subagent output as authoritative state once the underlying artifacts or decisions have changed.

Manifest IDs and wording can drift between iterations. Because of that, critique-analyzer must re-read the Decisions Log every run and decide by substance whether a candidate question has already been answered. Do not leave that judgment to Stage 3.

Run the workflow in this order:

Stage 1 Load guidance: load the design-thinking reference and the current mode's playbook.
Stage 2 Analyze artifacts: dispatch critique-analyzer to read artifacts, consult the current Decisions Log, inspect the codebase, search the web, and write the critique artifact. Always include PRIOR_DECISIONS_FILE and PRIOR_DECISIONS_KIND, even on ITERATION=1.
Stage 3 Build manifest: dispatch question-manifest-builder with the critique artifact path and the plan path to build the ordered manifest. In MODE=critique, also include TASK_NUMBER and CURRENT_TASK_ARTIFACTS. If the manifest returns Questions now: 0, treat that as a valid no-op and skip directly to Stage 5 without emitting a placeholder prompt.
Stage 4 Clarify inline: walk the manifest one question at a time inline, deciding what to confirm, revise, defer, or block. Carry each manifest Item ID unchanged into the decision list so later recording and plan annotations stay traceable.
Stage 5 Record decisions: dispatch decision-recorder with the resolved decisions and let it update the workflow artifacts plus validate the result. Include ITERATION and IMPLEMENTATION_UPDATES when present. In MODE=upfront, also include DEFERRED_QUESTIONS. In MODE=critique, also include TASK_NUMBER, TASK_TITLE, RESOLVED_IRRELEVANT, and any new DEFERRED_QUESTIONS created during the discussion.

The inline questioning loop uses two reasoning patterns:

Model A — Socratic. Used only for Tier 3 problem-framing hard gates. The developer answers first, then sees the critique.
Model B — evaluate the reasoning. Used for all other items. Present the original decision, the critique, and ask the developer whether the reasoning holds up.
Reference Loading

Read ./references/design-thinking-mindset.md first for both modes.

Then load only the mode-specific playbook for the active run:

Mode	Reference file	When to load
upfront	./references/upfront-mode.md	During Stage 1, before the plan-wide clarification run starts
critique	./references/critique-mode.md	During Stage 1, before the task-level clarification run starts
Behavioral Guardrails
Ask one question per message.
Ask only from the manifest; if a new item emerges, add it before asking it.
Defer future-task questions instead of speculating about them now.
Be direct about shallow thinking on Tier 3 items, but keep the tone mentor-like.
Present every critique item; do not silently accept a subagent recommendation.
Respect skip only for Tier 2 items. Tier 3 hard gates cannot be skipped. Tier definitions come from ./subagents/critique-analyzer-rubric.md.
When the interface supports structured choices, use them for discrete options; otherwise use numbered options.
Keep question blocks scannable. Use tables or diagrams only when they clarify a real trade-off.
Escalation

Expect parseable verdicts from subagents and route them like this:

Source	Verdicts to expect	Orchestrator action
critique-analyzer	CRITIQUE: FAIL	Stop and surface the required Reason: line to the user
critique-analyzer	CRITIQUE: WARN	Continue only if the missing context does not invalidate the critique
question-manifest-builder	MANIFEST: BLOCKED or MANIFEST: FAIL	Stop and surface the manifest issue
question-manifest-builder	MANIFEST: WARN	Continue, but mention what was omitted or guessed
decision-recorder	RECORDING: BLOCKED or RECORDING: ERROR	Stop and ask the user how to proceed
decision-recorder	RECORDING: WARN	Present the warnings in the final summary and continue
Example
<example>
Input: TICKET_KEY=JNS-6065, MODE=upfront, ITERATION=1

1. Read `./references/design-thinking-mindset.md`
2. Read `./references/upfront-mode.md`
3. Dispatch `critique-analyzer` with the plan file, stage artifacts, and
   `docs/JNS-6065-upfront-critique.md`, plus `docs/JNS-6065-tasks.md` as
   `PRIOR_DECISIONS_FILE` and `PRIOR_DECISIONS_KIND=main-log`
4. Receive:
   CRITIQUE: PASS
   Ticket: JNS-6065 | Mode: upfront | Task: -
   Artifact: docs/JNS-6065-upfront-critique.md
   
   ## Critique Summary
   
   - Problem-framing items: 2
   - Technology critique items: 3
   - User-impact items: 0
5. Dispatch `question-manifest-builder` with
   `docs/JNS-6065-upfront-critique.md` and `docs/JNS-6065-tasks.md`
6. Receive:
   MANIFEST: PASS
   Ticket: JNS-6065 | Mode: upfront | Task: -
   Task title: -
   Questions now: 8 | Deferred: 4 | Irrelevant: 1
7. Walk the 8 questions one at a time
8. Dispatch `decision-recorder` with resolved decisions and deferred items
9. Receive:
   RECORDING: PASS
   Ticket: JNS-6065 | Mode: upfront | Task: -
   
   ## Recording Summary
   
   ### Files Updated
   
   - `docs/JNS-6065-tasks.md`
   
   ### Counts
   
   - Decisions recorded: 8
   - Deferred questions tagged: 4
   - Questions marked irrelevant: 0
   - Implementation notes updated: 1
   
   ### Validation
   
   - PASS
10. Present final summary:
    Critique artifact: docs/JNS-6065-upfront-critique.md
    Files updated: docs/JNS-6065-tasks.md
    RE_PLAN_NEEDED: true
    BLOCKERS_PRESENT: false
</example>

<example>
Input: TICKET_KEY=acme-app-42, MODE=critique, TASK_NUMBER=3, ITERATION=2

1. Read `./references/design-thinking-mindset.md`
2. Read `./references/critique-mode.md`
3. Dispatch `critique-analyzer` with the task artifacts and
   `docs/acme-app-42-task-3-critique.md`, plus
   `docs/acme-app-42-task-3-decisions.md` as `PRIOR_DECISIONS_FILE` and
   `PRIOR_DECISIONS_KIND=per-task`
4. Receive:
   CRITIQUE: PASS
   Ticket: acme-app-42 | Mode: critique | Task: 3
   Artifact: docs/acme-app-42-task-3-critique.md
5. Dispatch `question-manifest-builder` with
   `docs/acme-app-42-task-3-critique.md`,
   `docs/acme-app-42-tasks.md`, and `CURRENT_TASK_ARTIFACTS`
6. Receive:
   MANIFEST: BLOCKED
   Reason: docs/acme-app-42-task-3-test-spec.md is missing
7. Stop clarification and present final summary:
   Critique artifact: docs/acme-app-42-task-3-critique.md
   Files updated: -
   RE_PLAN_NEEDED: false
   BLOCKERS_PRESENT: true
   Blocking verdict: MANIFEST: BLOCKED
   Reason: docs/acme-app-42-task-3-test-spec.md is missing
</example>

Weekly Installs
53
Repository
b-mendoza/agent-skills
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn