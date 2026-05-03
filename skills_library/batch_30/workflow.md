---
title: workflow
url: https://skills.sh/jsonlee12138/agent-team/workflow
---

# workflow

skills/jsonlee12138/agent-team/workflow
workflow
Installation
$ npx skills add https://github.com/jsonlee12138/agent-team --skill workflow
SKILL.md
Workflow
Overview

Create and execute controller-side delivery workflows that sit above agent-team. Keep workflow templates reusable, keep run state separate, and use the Go-based agent-team workflow helpers in this repository for template generation, validation, and run-state persistence.

Hard Rules
Act as the main controller only. Do not use this skill inside a worker session.
Do not modify agent-team source code, config schema, or internal protocol.
Require an approved brainstorming/design artifact before writing a new workflow file.
Keep template files and run-state files separate at all times.
Use existing agent-team commands as the only execution backend.
Persist state after every node transition and before every pause or confirmation gate.
Default Paths

Use these defaults unless the user explicitly chooses another project-local path:

Workflow templates: .agents/workflow/<workflow-name>.yaml
Run-state files: .agents/workflow/runs/<workflow-name>/<run-id>.yaml

Prefer a single reusable workflow template and one run-state file per execution.

Action Routing
Create Workflow

Use this flow when the user asks to create a workflow file.

Verify there is an approved brainstorming/design artifact.
If no approved design exists, stop and invoke brainstorming first.
Choose the smallest preset that matches the design:
branching for controller dispatch with explicit dev_first / test_first
dev-first for a linear implement-then-verify loop
test-first for tests-before-implementation
Generate the template with agent-team workflow create.
Validate it immediately with agent-team workflow validate.
Summarize the generated roles, entry node, branches, and output path.

Example:

agent-team workflow create feature-delivery \
  --preset branching \
  --output .agents/workflow/feature-delivery.yaml

agent-team workflow validate .agents/workflow/feature-delivery.yaml

Run Workflow

Use this flow when the user asks to run workflow.yaml, resume a run, or inspect workflow progress.

Validate the workflow template before execution.
Initialize run state with agent-team workflow state init unless resuming an existing run.
Resolve each workflow role alias to a concrete worker at runtime.
Create or reuse workers with agent-team worker create and agent-team worker open.
Execute the current node, then persist state with agent-team workflow state ....
Pause on worker wait states, proactive worker replies, ambiguous outcomes, or controller confirmations.
Resume by reading the run-state file and continuing from current_node.

Example bootstrap:

agent-team workflow validate .agents/workflow/feature-delivery.yaml
agent-team workflow state init .agents/workflow/feature-delivery.yaml

Execution Loop

Follow this controller loop for every run:

Read the template and current run-state.
Start the current node with agent-team workflow state start.
Execute the node action:
controller_task: do the task directly, then complete or confirm it.
assign_role_task: assign work to the mapped worker with agent-team worker assign, then move the run into a waiting state for worker feedback.
wait_for_completion: wait for the worker's reply-main message as the default completion signal.
decision: choose an explicit branch outcome and record it.
handoff: assign the follow-up task to the next role and capture the transfer in state.
verify_or_test: run verification or dispatch QA verification, then branch on outcome.
merge: run agent-team worker merge <worker-id> only after explicit controller approval.
Persist one of these outcomes:
wait when waiting on worker feedback or external verification
block when the run cannot advance without controller intervention
complete when the node finishes and can auto-advance
confirm when a confirmation gate is satisfied and a branch is selected
Stop when the run state becomes completed or blocked.
Default Wait Protocol
After assign_role_task, persist the run as waiting and stop active status polling.
The normal next signal is the worker's proactive agent-team reply-main "<message>".
Do not treat agent-team worker status as the default driver for wait_for_completion.
Use agent-team worker status only for assign failure diagnosis, timeout or no-reply investigation, or when the user explicitly asks for a status snapshot.
Worker Preparation

Before the first role-backed node executes:

Confirm every referenced role exists locally or can be installed.
If a role is missing and must be created, follow the role-creator contract instead of authoring role files manually.
Confirm whether to reuse an existing worker or create a new worker for each role alias.
Open worker sessions before assignment so replies can flow back to the controller.

agent-team commands are the bridge layer:

agent-team worker create <role-name>
agent-team worker open <worker-id>
agent-team worker assign <worker-id> "<task>"
agent-team worker status   # exception-only inspection, not routine polling
agent-team reply <worker-id> "<answer>"
agent-team worker merge <worker-id>

Confirmation And Branching
Treat requires_confirmation: true as a hard pause.
Do not auto-select a branch when worker feedback is ambiguous.
Prefer workflow-defined branch labels such as test_first, dev_first, passed, and failed.
Re-run a completed node only when the controller explicitly asks for a retry.

Use agent-team workflow state confirm to resolve confirmation nodes deterministically.

References
Read references/schema.md when you need the workflow and run-state schema.
Read references/execution.md when you need the node-type execution contract and controller behavior.
Commands
agent-team workflow create: generate a starter workflow template from a supported preset.
agent-team workflow validate: fail-fast validation for workflow structure and node references.
agent-team workflow state init|show|start|wait|block|complete|confirm: initialize, inspect, and update run-state files during execution.
Weekly Installs
10
Repository
jsonlee12138/agent-team
GitHub Stars
24
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass