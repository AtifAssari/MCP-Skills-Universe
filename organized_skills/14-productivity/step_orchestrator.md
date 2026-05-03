---
rating: ⭐⭐⭐
title: step-orchestrator
url: https://skills.sh/charys117/skills/step-orchestrator
---

# step-orchestrator

skills/charys117/skills/step-orchestrator
step-orchestrator
Installation
$ npx skills add https://github.com/charys117/skills --skill step-orchestrator
SKILL.md
Step Orchestrator

Run the main agent as coordinator. It owns plan state, Markdown plan writeback, commits, and hard-blocker decisions. Subagents own only the single round they are spawned for.

Require these inputs
Require a repo-local Markdown plan file path such as docs/plan.md or plans/migration.md.
Require explicit step IDs or ranges such as 3-5,7.
Require the target workspace or repository. Treat the current workspace as the default only when the user does not name another one.
Accept tests, constraints, branch preferences, and acceptance criteria as optional additions.
Treat an explicit request to use this skill, delegate, use subagents, or run worker/reviewer agents as permission to spawn subagents. If that permission is absent, ask before spawning.
Load references only when needed
Read references/adapter-contract.md before mutating the Markdown plan file.
Read references/harness-minimum.md when creating or refreshing the repo project status or memory doc.
Do not use Notion, external databases, or other external plan stores for this skill. The plan state lives in the repo Markdown file.
Stop and report a blocker if the current context cannot safely inspect and update the named Markdown plan file.
Set up coordinator state
Inspect the Markdown plan format before mutating anything.
Resolve the requested range against a sortable numeric or order column in the plan file.
Normalize duplicates and process steps in ascending order.
Snapshot repository state before the first step and before each commit.
Build a visible execution ledger with step ID, title, status, current round, worker handoff, reviewer verdict, tests, commit, and blockers.
Define the step's acceptance criteria from the Markdown row, any step detail section, user prompt, tests, and repository instructions before spawning worker1.
Do not spawn a worker until the prompt can be built from explicit step-local inputs.
Capture the coordinator's current model and reasoning effort. Spawn every worker, reviewer, and sidecar subagent with the same model and same reasoning effort when the runtime exposes those settings; do not downgrade, upgrade, or auto-select different subagent settings.
Prepare the repo memory harness
Treat repo-maintained Markdown memory as the subagent harness. Do not use the coordinator's hidden conversation context as memory.
Before spawning the first worker, locate the harness docs the subagents must read:
applicable AGENTS.md files, including the repo root file and any nested files that govern paths in the active step
the Markdown plan file, including the active step row, step detail section, and ## Step Execution Log
a project status or memory doc such as .agents/docs/project-status.md, PROJECT_STATUS.md, STATUS.md, or another clearly named repo Markdown status file
relevant architecture, test, migration, decision, release, issue, or troubleshooting records already maintained in the repo
If a required harness doc is missing or stale enough that a subagent would lack necessary context, create or update the smallest useful Markdown doc before spawning. Prefer existing repo conventions; otherwise use .agents/docs/project-status.md. Do not create a top-level docs/ directory just for the harness. Use references/harness-minimum.md for the minimum structure.
Before relying on the selected project status or memory doc, verify it is not ignored by git and can be committed with the repo, whether it already existed, was created, or was updated. If .agents/docs/project-status.md is ignored, use another existing trackable repo memory location or stop with a blocker.
Keep harness docs concise and factual: current goal, active steps, important constraints, relevant decisions, known risks, test commands, recent commits, and links to deeper records.
Add or update a short ## Harness or equivalent reference section in the plan file when the required docs are not already obvious from the plan.
Pass harness doc paths to subagents and instruct them to read those files. Do not paste large doc contents into the prompt unless a short excerpt is necessary to avoid ambiguity.
Run the coordinator loop
Handle one step at a time. Do not overlap steps.
For each step:
Mark the step In Progress in the Markdown plan file.
Spawn fresh worker worker1 dedicated only to that step. Use a worker-style subagent when available. Set its model and reasoning effort to match the coordinator. Do not attach or reuse a worker thread from any earlier step. If the runtime exposes fork_context, set fork_context=false. Instruct it not to commit, tag, or update the Markdown plan file.
Wait for worker1 to finish and return a complete handoff for that step before doing any implementation work on the same step yourself. If the handoff is incomplete, ask worker1 to clarify or finish it.
Mark the step In Review in the Markdown plan file.
Spawn fresh reviewer reviewer1 dedicated only to that step. Use a read-only reviewer or explorer-style subagent when available. Set its model and reasoning effort to match the coordinator. Do not attach or reuse a reviewer thread from any earlier step. If the runtime exposes fork_context, set fork_context=false. Keep reviewer read-only.
Wait for reviewer1 to return a final review result before doing any review work on the same step yourself.
If reviewer1 rejects the work, append reviewer1 review history to the Markdown plan file, set the step back to In Progress, and spawn worker worker2 with the review notes.
Continue worker<n> -> reviewer<n> rounds until the reviewer approves or a hard blocker prevents safe progress.
After approval, inspect repository status and the approved diff. Run any missing or stale required verification.
Mark the step Done in the Markdown plan file and write back the approval summary plus the planned commit subject step {id}: {step_title}. Do not require or write a commit SHA.
Stage only the approved step's changes plus the coordinator's Markdown plan and harness writebacks, then commit step {id}: {step_title}.
Retire the step's subagents before continuing. Do not carry any worker or reviewer thread across the step boundary.
Continue to the next requested step only after the current step is approved, committed, and written back.
Keep side effects centralized
Let worker agents patch code and run the tests needed for that step.
Let reviewer agents inspect and report findings, but never patch code.
Let only the coordinator commit, update the Markdown plan file, and decide whether a blocker is hard.
While a worker or reviewer round is active, let the coordinator orchestrate and wait. Do not let it silently absorb the same round just because the subagent is slow.
Avoid parallel write-heavy work. Only use extra sidecar subagents for read-only exploration or verification when their output can be summarized back into the active step.
Wait deliberately for spawned agents
Treat each spawned worker<n> or reviewer<n> as the owner of that round until it finishes, reports a blocker, or is explicitly replaced.
Use long waits and sparse polling. A single timeout or slow response is not permission for the coordinator to take over the round.
If a subagent is slow, ask for a status update or continue waiting. Prefer patience over duplicate work.
If a subagent stalls across multiple waits, first nudge it or replace it with a fresh subagent for the same role and same step. Preserve the round history and handoff context as explicit notes, diffs, file paths, and test results rather than hidden thread state.
Let the coordinator take over a round only when subagent execution is impossible in the current session, and record that reason in the review history or blocker notes.
Never start the next step while any subagent still owns the current step.
Isolate subagents by step
Treat every step boundary as a hard context boundary. Each step gets new worker and reviewer threads even when the workspace, code area, and role stay the same.
Never attach a later step to a subagent from an earlier step. Reusing agent history across steps is a workflow bug because it leaks assumptions and review context.
Pass forward only explicit artifacts such as the Markdown plan state, written handoff notes, commits, and test results. Do not pass forward hidden thread state by reusing the same subagent.
If you need context from a prior step, summarize it in the new step prompt or writeback instead of reviving the earlier subagent.
Pass only step-local context to subagents
Never spawn a step subagent with the coordinator thread history attached. If the spawning tool supports fork_context, keep it false.
Build each subagent prompt from explicit step-local inputs only: step ID and title, the step body or acceptance criteria, harness doc paths to read, relevant file paths, required test commands, the current round's reviewer notes, and any concrete approved artifacts from earlier steps that this step depends on.
Do not dump the full coordinator conversation, unrelated repository exploration, or future-step plans into the subagent prompt.
When a later step depends on an earlier one, pass a short dependency summary or concrete artifacts such as the commit subject, changed paths, interface notes, and test results.
Treat any leakage of coordinator thread state into a subagent as a workflow failure because it lets the subagent infer or preempt work outside the active step.
Treat missing harness docs as a coordinator preparation failure, not as a reason to fork coordinator context into the subagent.
Require structured handoffs
Worker handoff must include: summary, changed paths, tests run with results, acceptance-criteria mapping, user or environment changes noticed, and blockers or risks.
Reviewer result must include: approved or rejected, findings with file and line references when possible, required changes, tests or checks considered, and residual risk.
Rejection notes must be actionable enough for the next worker round to work without hidden reviewer context.
Approval is not enough by itself if required tests were skipped, the diff includes unrelated changes, or the reviewer only inspected a subset without saying why.
Shape subagent prompts narrowly
Role: <worker|reviewer> for step <id> only.
Workspace: <path>.
Active step:
- title: <step title>
- objective: <step body or goal>
- acceptance criteria: <criteria>
Harness docs to read first:
- repo instructions: <AGENTS.md paths that apply>
- plan: <plan path and relevant step/detail/log anchors>
- project status or memory: <paths>
- relevant records: <architecture/test/decision/migration/troubleshooting docs>
Relevant artifacts:
- files or directories: <paths>
- prior approved dependency notes: <only what this step needs>
- current round review notes: <same-step notes only>
Run tests: <commands>
Rules:
- work only on this step
- do not infer or start later steps
- do not use or request hidden coordinator thread context
- read the listed harness docs before editing or reviewing
- worker: do not commit or update the Markdown plan file
- reviewer: read-only, report findings and verdict only
Return:
- worker: summary, changed paths, tests/results, acceptance mapping, risks/blockers
- reviewer: approved/rejected verdict, findings, required changes, checks considered, residual risk

Enforce the minimum contract
Require one repo-local Markdown plan file with an identifiable step table. Stop before mutation if it is missing or outside the workspace.
Require one sortable numeric or order column for range resolution. Stop before mutation if it is missing.
Infer a writable status column and map the local flow to Todo, In Progress, In Review, and Done. Stop before mutation if no writable status-like column exists.
Infer commit subject/message columns by name when present. Do not require or populate commit SHA columns. Always append detailed worker/reviewer history to the Markdown execution log so table cells stay compact.
Require enough repo Markdown harness context for subagents to work without coordinator thread history. Prepare missing project status, memory, or record docs before spawning.
Append review history by round. Do not overwrite earlier reviewer1, reviewer2, or later reviewer feedback.
Treat missing or malformed Markdown plan files, missing required schema primitives, unrecoverable test or setup failures, or conflicting user changes as hard blockers. Write the blocker back to the Markdown execution log when safe, then stop.
Use this prompt shape
Use the step-orchestrator skill with plan file <repo-relative markdown path>.
Process steps 3-5 in workspace <path>.
Run a worker/reviewer loop until each step is approved.
Run tests: <commands>.
Constraints: <constraints>.

Weekly Installs
10
Repository
charys117/skills
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass