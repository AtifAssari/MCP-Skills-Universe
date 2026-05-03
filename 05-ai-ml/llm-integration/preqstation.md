---
title: preqstation
url: https://skills.sh/sonim1/preqstation-skill/preqstation
---

# preqstation

skills/sonim1/preqstation-skill/preqstation
preqstation
Installation
$ npx skills add https://github.com/sonim1/preqstation-skill --skill preqstation
SKILL.md

This is the agent-side lifecycle skill. The OpenClaw launcher skill is separate and should be named preqstation-dispatch.

Environment

Recommended MCP mode:

Register the remote MCP endpoint from the PREQSTATION projects-manager service:
Claude Code: claude mcp add -s user --transport http preqstation https://<your-domain>/mcp
Codex: codex mcp add preqstation --url https://<your-domain>/mcp
Gemini CLI: gemini mcp add --scope user --transport http preqstation https://<your-domain>/mcp
OAuth starts when the client first makes a real request to /mcp
Codex often triggers login during add because it probes the server immediately
Gemini CLI may also prompt for auth during MCP registration or first real tool call. If gemini mcp list still shows preqstation as Disconnected, open an interactive Gemini session and run /mcp auth preqstation.
Claude Code usually stores the config first and may show Needs authentication until first use or claude mcp get preqstation
Prefer one user-scoped Claude Code PREQ registration so you do not accumulate duplicate project-local entries
Verify MCP registration with claude mcp list, codex mcp list, or gemini mcp list
Complete the browser login flow when prompted by the client

Optional shell helper mode:

PREQSTATION_API_URL: PREQSTATION API base URL (example: https://mypreqstation.vercel.app)
PREQSTATION_TOKEN: PREQSTATION Bearer token (generated in PREQSTATION /api-keys)
PREQSTATION_ENGINE (optional): fallback engine (claude-code | codex | gemini-cli) when client auto-detection is unavailable
Agent Identity & Engine Mapping

Each agent must identify itself and use the corresponding engine value in all task operations (list, create, plan, start, update status, complete, review, block):

If you are...	Use engine=
Claude (Anthropic)	claude-code
GPT / Codex (OpenAI)	codex
Gemini (Google)	gemini-cli

Always include your engine value when listing, creating, planning, starting, completing, reviewing, or blocking tasks.

Gemini CLI workers can run interactively with gemini or headless with gemini -p "<prompt>". If your installed Gemini environment does not expose remote HTTP MCP, use the shell helper fallback instead of this MCP path.

MCP Plugin Mode (Recommended)

If MCP is available, prefer the remote /mcp endpoint exposed by the PREQSTATION service. All mutation tools accept an optional engine parameter and always send an engine value using this order:

explicit tool arg
existing task engine (when available)
MCP initialize.clientInfo.name auto-detection
PREQSTATION_ENGINE
codex fallback
Tool	engine usage
preq_list_projects	Read-only, no engine needed (list PREQ projects for setup and local repo mapping)
preq_list_tasks	Read-only, no engine needed
preq_get_task	Read-only, no engine needed
preq_get_project_settings	Read-only, no engine needed (fetch project deploy settings by key)
preq_list_task_comments	Read-only; for comment objectives, fetch task comments as conversation history/reference around the target comment
preq_get_task_comment	Read-only; fetch the exact comment being handled before replying or changing comment state
preq_update_qa_run	Read-only from task lifecycle perspective; updates branch-level QA run status/report without task transitions
preq_plan_task	Assign engine, send lifecycle action plan, backend moves inbox task to todo and clears run_state
preq_create_task	Assign engine to new inbox task
preq_start_task	Record engine claiming the task; backend marks run_state=working
preq_update_task_note	Record engine while replacing the task note markdown without changing workflow status
preq_update_task_status	Record engine while updating workflow status-only endpoint (/api/tasks/:id/status)
preq_update_task_comment_state	Record engine while marking a task comment working, done, or failed without changing task workflow status
preq_reply_task_comment	Record engine while replying to a task comment; backend creates work logs for comment replies/failures automatically
preq_list_dispatch_requests	Read-only; inspect explicit dispatch requests used by launcher runtimes for ask parity and project-level insight
preq_update_dispatch_request	Launcher runtime only; mark an explicit dispatch request as dispatched or failed after launch succeeds or fails
preq_complete_task	Record engine in work log result, send lifecycle action complete; backend moves → ready and clears run_state
preq_review_task	Record engine running verification, send lifecycle action review; backend moves → done and clears run_state
preq_block_task	Record engine reporting the block, send lifecycle action block; backend moves → hold and clears run_state
preq_delete_task	Permanently delete a task by ticket number or UUID

This gives deterministic task-id based execution and result upload.

Execution Flow (Mandatory)

You must follow this execution flow exactly. Do not skip, reorder, combine, or substitute lifecycle actions. PREQ launcher-driven runs are non-interactive by default. You may use process skills such as brainstorming or writing-plans only as internal guidance while continuing the PREQ lifecycle in the same run. Do not stop to ask the user for approval, clarifications, or design feedback mid-run unless PREQ tools are unavailable or the prompt/worktree/task state is invalid. Project deploy settings are explicit operator authorization for this PREQ run. When deploy_strategy requires commit, push, or PR work, perform those git/GitHub actions without asking for separate approval.

Load -> Initialize -> Execute -> Finalize

Load: Load the .preqstation-prompt.txt in this worktree/branch

Initialize:

When Task ID is present, MUST call preq_get_task once at the start to fetch task details, acceptance criteria, workflow status, run_state, and the initial engine.
If preq_get_task returns latest_preq_result, read it before substantive work and treat it as previous execution context, especially for resumed or previously blocked tasks.
When Task ID is present and the task is active, MUST call preq_start_task, except for comment objectives where task claiming is explicitly forbidden.
When Task ID is absent for project-level objectives such as insight, skip task lifecycle reads/writes and treat the prompt metadata plus project key as the source of truth.
In debug mode, create or refresh preqstation-progress.md after preq_get_task and update it after each major checkpoint.
Resolve the task-facing content language once near the start of the run by inspecting the current task note and any temporary trailing Ask: helper block first, then acceptance criteria, and only using the task title as a weak tie-breaker.
Use the dominant language of that note-centric task content for PREQ-facing written updates such as plan markdown, rewritten task notes, completion summaries and notes, review notes, block reasons, QA reports, and newly created task content.
Use project agent_instructions only as a final tie-breaker when the task note, Ask: block, and acceptance criteria are still mixed or ambiguous. The current task content takes precedence.
If no dominant language is clear, default PREQ-facing written updates to English.
Execute the user objective user objective is in the .preqstation-prompt.txt
If user objective start with plan:
Start to plan using the local code.
Planning means plan generation only. You may inspect local code, but you must not implement product changes, run deploy steps, or run tests, build, lint, or other verification commands.
Before blocking for missing code, inspect the primary checkout as well as the current worktree. If the worktree is in a bootstrap repo state, such as only .gitignore being tracked, but the primary checkout contains the real app files, treat that as repo recovery rather than a missing project.
During bootstrap repo recovery, ensure origin exists and matches the PREQ repo URL. If origin is missing and the repo URL is known, add it with git remote add origin <repo_url>.
Commit the baseline project files on main, push origin/main, recreate or refresh the worktree, and continue planning after the code becomes inspectable.
Block the run only when the primary checkout is the wrong repo, the repo URL is unavailable or mismatched, or the bootstrap recovery push to origin/main fails.
Call preq_plan_task with plan markdown and implementation checklist.
Process skills are allowed only as internal guidance. This run must stay non-interactive and end at preq_plan_task.
Else If user objective start with ask:
Rewrite or update the existing task note. Keep the workflow status unchanged.
Treat the current task note plus any temporary trailing Ask: helper block as the source material for the rewrite.
If the ask clearly requests a prototype or reviewable artifact, local artifact generation is allowed.
Artifact publishing is best-effort, but it is mandatory to attempt when a safe artifact provider is already available. Use the provider already authenticated in the current agent session; Fast.io is one supported provider, not the only valid target.
If the current agent already has an authenticated Fast.io MCP session or another authenticated provider, treat that provider as already available and attempt publication without waiting for extra provider instructions.
Durable artifact links must use a private-or-skip policy. Authenticated workspace targets, member-restricted shares, and registered-account shares count as acceptable private access. Skip non-expiring anyone with the link URLs or other public-link-only modes.
If the provider can create temporary external share or quickshare links, create 7-day expiring reviewer links for the published artifacts. Mark them with access=quickshare or the provider's equivalent and include expires=...; do not create non-expiring public links.
If the local artifact is an HTML prototype or HTML mockup, generate at least one screenshot PNG for review, then attempt to publish both the HTML source and screenshot artifact when an authenticated provider is available.
Record published links under an Artifacts: markdown block using lines like - [image] Desktop screenshot | provider=fastio | access=quickshare | expires=2026-04-18T00:00:00Z | url=... and - [document] HTML prototype | provider=fastio | access=private-workspace | url=....
For prototype or reviewable artifact asks, record the artifact publishing result or skip reason in the note. If publishing is skipped, include the local artifact path and a concise reason such as provider unavailable, unauthenticated, or no safe target.
Treat localhost and 127.0.0.1 URLs as local-only diagnostics. Do not present them as the only review link; either publish a private artifact URL or explicitly mark the artifact as local-only with the skip reason.
Persist the rewritten markdown with preq_update_task_note, including any published artifact URLs or artifact publishing skip note.
Clear execution state by calling preq_update_task_status with the current workflow status from preq_get_task.
The final saved note must not include the temporary Ask: helper block.
Else If user objective start with comment:
Handle the referenced task comment only; preserve the task workflow status for the entire run.
Treat comments as a conversational request channel, not as implementation source of truth. A comment affects future implementation only if this comment objective explicitly promotes it into the task note/spec with preq_update_task_note.
MUST call preq_get_task, preq_get_task_comment, and preq_list_task_comments at the start to fetch task details, the current note, workflow status, existing run state, the exact comment being handled, and the surrounding task-scoped comment conversation.
Treat the referenced comment_id as the primary request for this run. Other user, agent, and system comments are conversation history/reference only, including prior AI replies; use them to understand flow and avoid contradictory or context-blind responses.
Do not treat non-target comments as independent actionable requirements. They affect future implementation only after the current target comment explicitly or unambiguously asks you to promote the conversational decision into the task note/spec with preq_update_task_note.
MUST NOT call preq_start_task; comments use comment state rather than task run_state claiming.
Mark the original comment working with preq_update_task_comment_state before substantive work.
Inspect the current task note, target comment, and comment history before deciding how to respond.
Optionally call preq_update_task_note only when the comment explicitly requests a note, plan, or specification change. This is the only “promote comment to notes” path: convert the requested change into canonical note/spec language, then mention that the note was updated in the reply. Do not rewrite the note for a normal answer, acknowledgement, or implementation-review comment.
Reply with preq_reply_task_comment and set noteUpdated accurately to indicate whether preq_update_task_note was used.
Mark the original comment done with preq_update_task_comment_state after the reply succeeds.
Never call preq_complete_task, preq_review_task, preq_plan_task, or preq_block_task for a comment objective.
Do not create a separate work log for comment handling. The backend creates work logs automatically for comment replies and failure updates.
On failure, preserve task workflow status, reply with the failure details using preq_reply_task_comment if possible, then mark the original comment failed with preq_update_task_comment_state. If replying is impossible, still mark the comment failed with the most concrete failure reason available.
Else If user objective start with insight:
Task ID may be absent for this branch. Do not invent one and do not call task lifecycle mutations when no task exists.
Inspect the local project from the current worktree and use the provided Insight Prompt only as task-generation guidance.
Call preq_list_tasks with the current projectKey and detail=full before creating anything so you can avoid duplicates in inbox, todo, hold, and ready.
Create multiple Inbox tasks with preq_create_task.
Title each created task with a short shared topical prefix derived from the user intent or current work area.
Keep description detailed, but keep acceptanceCriteria to checklist-only verification items.
Do not mutate existing tasks and do not produce a long-form implementation plan instead of task creation.
Else If user objective start with qa:
Task ID may be absent for this branch. Do not invent one and do not call task lifecycle mutations when no task exists.
Resolve qa_run_id from .preqstation-prompt.txt and use preq_update_qa_run to mark the run running as soon as the local target URL is known.
Resolve qa_task_keys from .preqstation-prompt.txt when present. If listed, call preq_get_task for each task key before browser testing and treat those tasks' titles, descriptions, and acceptance criteria as the QA scope.
If the current agent has access to the dogfood skill, use it as the default QA workflow for browser testing and report generation.
Start the current project from the current worktree/branch, determine the local target URL, and run browser QA against that URL.
Limit QA to the scoped Ready tasks and the minimal navigation or sanity checks needed to reach and verify them. Do not expand into unrelated full-app exploratory QA. Report unrelated findings only when they block scoped verification or prevent the app from starting.
QA reports may include optional artifact references for screenshots, videos, and documents. Use the same private-or-skip policy when a safe provider is available.
If QA artifact publishing is skipped after generating local artifacts, record the artifact publishing result or skip reason in the final QA report.
When QA finishes, call preq_update_qa_run again with final status (passed or failed), target_url, markdown report, and summary counts.
Do not call preq_complete_task, preq_review_task, or preq_block_task unless this run is also handling a real PREQ task.
Else If user objective start with implement or resume:
Implement code changes and run task-level tests.
Use task notes, acceptance criteria, and explicit PREQ result context as the implementation source of truth. Do not fetch or interpret task comments as hidden requirements or conversation context; comments affect implementation only after a prior comment objective updated the canonical task note/spec.
If latest_preq_result is present, use it to understand the latest blocked reason, prior summary, and most recent PREQ execution context before making changes.
Resolve deploy strategy via the Deployment Strategy Contract.
Perform the required git/deploy steps for direct_commit, feature_branch, or none. Follow the Deployment Strategy Contract section.
Do not stop for user approval or separate conversational design/spec loops mid-run.
Else If user objective start with review:
Run verification (tests, build, lint).
Review against task notes and acceptance criteria, not raw task comments. Do not fetch or interpret task comments as conversational context during review; comments matter to review only after a prior comment objective promoted them into the note/spec.
Call preq_review_task with review notes.
Do not request additional user approval or switch into a separate conversational workflow mid-run.

On any failure in an active task branch, call preq_block_task with the blocking reason and stop. This does not apply to comment objectives; use the comment failure lifecycle instead. On any failure in a QA branch, update the QA run to failed with a concise markdown report and stop.

Finalize: On success for implementation/review branches, call preq_complete_task with summary, branch, and pr_url when applicable. On success for ask branches, do not call preq_complete_task; the successful note rewrite ends after preq_update_task_note plus preq_update_task_status using the unchanged workflow status. On success for comment branches, do not call task completion, review, plan, or block tools; the successful comment response ends after preq_reply_task_comment plus marking the original comment done. On success for insight branches, stop after the Inbox tasks are created; do not call preq_complete_task or mutate existing task workflow state.
Deployment Strategy Contract (required)

Before any git action, resolve deployment strategy through MCP:

Call preq_get_task <task_id>.
Read task.deploy_strategy from the response.
If missing, call preq_get_project_settings <project_key> and resolve from:
settings.deploy_strategy
settings.deploy_default_branch
settings.deploy_auto_pr
settings.deploy_commit_on_review
settings.deploy_squash_merge

Expected values from PREQSTATION backend:

strategy: direct_commit | feature_branch | none
default_branch: string (usually main)
auto_pr: boolean (feature_branch only)
commit_on_review: boolean
squash_merge: boolean (direct_commit only)

Default when absent/invalid:

strategy=none
default_branch=main
auto_pr=false
commit_on_review=true
squash_merge=true

Behavior by strategy:

none: do not run git commit/push/PR. Only code changes + task update result.

direct_commit and feature_branch are authorized git-operation modes. Do not block solely because general coding-agent defaults discourage autonomous commits, pushes, or PRs; the PREQ project deploy strategy is the approval source for this run.

Git-facing artifacts must default to English even when PREQ-facing task updates use another language. This includes commit messages, PR titles, PR bodies, branch names, and other repository-facing metadata.

direct_commit: merge worktree commits into default_branch and push. No PR. After completing work in the worktree:

# In primary checkout: update and merge
git -C <project_cwd> checkout <default_branch>
git -C <project_cwd> pull origin <default_branch>

# squash_merge=true (default): single commit
git -C <project_cwd> merge --squash <worktree_branch>
git -C <project_cwd> commit -m "<task_id>: <summary>"

# squash_merge=false: regular merge
git -C <project_cwd> merge <worktree_branch>

# Push to remote
git -C <project_cwd> push origin <default_branch>


feature_branch: push worktree branch to remote. Create PR only when auto_pr=true (requires GitHub access on the agent such as gh auth or GitHub MCP).

git -C <project_cwd> push origin <worktree_branch>
# if auto_pr=true: create PR via GitHub MCP or gh CLI and capture the PR URL


PR creation rule for feature_branch + auto_pr:

Default to a non-draft PR.
Do not create a draft PR unless the user explicitly asked for a draft PR, or the task is intentionally being handed off in an incomplete/blocked state.
If the available GitHub tool or CLI flow creates a draft PR by default, immediately convert it to "ready for review" before calling preq_complete_task.
Always capture the final non-draft PR URL that will actually be reviewed.

Rule for commit_on_review:

if true and strategy is direct_commit or feature_branch, do not move task to ready until remote push is verified.
if false, ready transition is allowed without mandatory remote push.

Required completion rule for feature_branch + auto_pr + commit_on_review:

Treat both the pushed branch name and the PR URL as required before preq_complete_task.
Preferred order:
push worktree_branch
create a non-draft PR
if a draft PR was created implicitly, convert it to ready for review
capture the PR URL
call preq_complete_task with both branchName and prUrl
If GitHub access is unavailable, branch push fails, PR creation fails, or the PR URL cannot be captured, call preq_block_task with the exact missing prerequisite and the next operator action.
Good block reasons are concrete, for example:
Auto PR required before ready, but gh is not authenticated on the coding agent. Run gh auth login or configure GitHub MCP, then resume.
Auto PR required before ready, but gh pr create failed after pushing task/proj-123/example. Fix the GitHub error and resume.
Auto PR required before ready, but the PR is still a draft. Mark it ready for review, capture the final PR URL, then resume.
Shell Helper Mode (Optional)

If MCP is unavailable, source scripts/preqstation-api.sh and use the shell helpers documented in docs/shell-helper-mode.md. Keep SKILL.md focused on lifecycle rules; use the helper reference doc for function signatures and jq/curl notes.

Debug Progress Mode (Optional)

Use this only when the caller explicitly asks for debug mode or requests progress visibility.

File path: <worktree>/preqstation-progress.md
Purpose: local human-readable progress artifact for the current run
Scope: current run only; refresh it at run start instead of appending infinite history
Safety: do not use it as lifecycle source of truth, and do not commit or push it unless the user explicitly asks

Write down the current execution flow steps

For example:

# PREQ Progress

- Task: PROJ-123
- Objective: implement
- Status: todo
- Run State: working
- Current Step: running task-level tests
- Last Updated: 2026-03-13T14:30:00Z

## Timeline

- 2026-03-13T14:10:00Z fetched task details using `preq_get_task`
- 2026-03-13T14:11:00Z called preq_start_task using `preq_start_task`
- 2026-03-13T14:18:00Z finished local code inspection
- 2026-03-13T14:30:00Z running task-level tests
  ...

Weekly Installs
64
Repository
sonim1/preqstation-skill
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn