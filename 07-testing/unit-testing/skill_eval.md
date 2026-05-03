---
title: skill-eval
url: https://skills.sh/jiayi-ye02/skills-evaluation/skill-eval
---

# skill-eval

skills/jiayi-ye02/skills-evaluation/skill-eval
skill-eval
Installation
$ npx skills add https://github.com/jiayi-ye02/skills-evaluation --skill skill-eval
SKILL.md
Skill Eval

Use this skill only for the evaluator flow.

This skill does not define test truth. The eval repo defines the targets, suites, cases, assertions, statuses, and report contract.

This skill is a dynamic black-box evaluator. Do not replace execution with a static read-through when a fresh-agent run is possible.

File Responsibilities

Use the docs in this order and keep their roles separate:

agentic-evals/AGENT.md: canonical repo contract for any evaluator agent. Read this first for run outputs, statuses, assertion semantics, isolation rules, and report shape.
agentic-evals/docs/session-evidence.md: required local evidence contract for locating child sessions and extracting evidence from sessions/*.jsonl.
agentic-evals/targets/<target_id>/target.yaml: target-specific contract, including entry skill, roots, default suites, and allowed statuses.
agentic-evals/targets/<target_id>/suites/*.yaml: selected runnable suite definitions.
agentic-evals/targets/<target_id>/cases/*.yaml: per-case prompts, setup, and assertions.
skill-eval/SKILL.md: how this evaluator skill acquires the repo, creates isolated workspaces, spawns fresh agents, locates child sessions, validates isolation, and writes the repo-defined artifacts.

Do not duplicate repo contract rules from AGENT.md unless this skill needs an extra operational constraint.

Required Inputs
optional path to the test repo
target_id, or permission to use the repo default
selected suite names, case ids, or permission to use the defaults
path or revision of the target skill if the user provided one

If the user does not provide a test repo path, the evaluator must first look for a local agentic-evals folder in the current workspace and clone the default repo only if that folder is missing.

Default test repo:

folder name: agentic-evals
clone URL: https://github.com/Jiayi-Ye02/agentic-evals.git
Non-Negotiables
Before any test evaluation, check whether a local agentic-evals folder already exists.
If the test repo folder does not exist, clone https://github.com/Jiayi-Ye02/agentic-evals.git before doing anything else.
Read agentic-evals/AGENT.md before running any case.
Resolve target_id before selecting cases. Use the user-provided target_id when available. Otherwise, use the repo default target.
Read agentic-evals/targets/<target_id>/target.yaml before selecting cases.
Read the selected suite files and case files before executing cases.
Create one brand-new isolated workspace for every case attempt under a temp parent directory. Never execute a case in the user's main workspace.
Execute each case by running a fresh Codex sub-agent on the case prompt with spawn_agent and fork_context: false.
Do not use codex exec, terminal wrappers, or any other fallback executor for case execution.
If spawn_agent is unavailable or agent creation fails, stop the evaluation immediately and report the failure reason instead of continuing.
After each successful spawn_agent, immediately report the sub-agent nickname in the main thread so the user can find and open it in the Codex app. If no nickname is available, report the agent id.
Send the case input.user_prompt to the fresh agent verbatim. Do not paraphrase the user request.
Do not leak the case title, assertions, expected route, intended answer, or your prior judgment into the fresh-agent prompt.
The fresh sub-agent is the execution subject, not the judge. Do not ask it to grade the case, interpret the assertions, or decide pass or fail.
Do not ask the fresh sub-agent to self-report TRACE_FILES_READ, TRACE_COMMANDS_EXECUTED, or any other evaluator-facing execution log.
Judge from accepted child session evidence, not from fresh-agent self-reporting.
Do not invent pass or fail rules outside the repo.
Do not mark pass from a generic self-report alone.
Do not mark pass from a static source review alone when a fresh-agent run was available.
Treat any attempt that observably reads or executes outside its case workspace as invalid evidence. Do not judge the case from that attempt.
If a case cannot be judged reliably, mark it blocked.
On clone failure, report the error and stop. Do not silently continue without the test repo.
Workflow
Step 1: Acquire the test repo

Resolve the test repo path in this order:

If the user provided a repo path, use it.
Otherwise, look for a local folder named agentic-evals in the current workspace.
If that folder does not exist, run:
git clone --depth 1 https://github.com/Jiayi-Ye02/agentic-evals.git


Do not continue until the repo is present locally or the clone has failed.

Step 2: Load the repo contract

Read:

agentic-evals/AGENT.md
agentic-evals/docs/session-evidence.md
agentic-evals/targets/<target_id>/target.yaml
each selected suite file
each case file referenced by those suites, or the selected case file

AGENT.md defines the repo contract. This skill executes that contract.

Step 3: Create the run directory

Create the run directory and files exactly as required by agentic-evals/AGENT.md.

At minimum, the run must contain:

runs/<run_id>/
├── manifest.json
├── case-artifacts/
├── transcript.md
├── case-results/
└── report.md


When writing manifest.json, include any environment notes this skill discovers while setting up isolated workspaces or locating accepted child sessions.

Step 4: Create a fresh case workspace for every attempt

Before executing a case, create a temp parent directory and then create a brand-new workspace for that case attempt.

Use the helper script:

bash skill-eval/scripts/create_case_workspace.sh "<source_workspace>" "<case_workspace_root>" "<case_id>" --target "<target_id>"


The script returns the absolute path to the new attempt workspace. <source_workspace> must be the shared workspace root that contains sibling agentic-evals/ and .agents/ directories.

By default it should copy only the target skill materials needed for execution:

the target entry_skill
the target roots
any explicit extra relative paths passed as additional arguments when a case needs local fixtures

The case workspace must not include repo evaluation materials such as targets/, docs/, runs/, or the evaluator skill itself unless a case explicitly requires them.

Rules:

Run this once before the first attempt of every case.
Run it again before every retry of the same case. Retries must not reuse the prior attempt workspace.
Apply case setup only inside the returned workspace.
Treat the returned workspace as a minimal target-skill sandbox, not a full clone of the eval repo.
Resolve repo-defined files from <source_workspace>/agentic-evals/ and target skill files from <source_workspace>/.agents/.
Record the parent temp directory as case_workspace_root in manifest.json.
Record the exact attempt workspace used for judgment as workspace_root in case-results/<case_id>.json.
Step 5: Execute each case dynamically

For every case:

Create a fresh isolated workspace for that case attempt under case_workspace_root.
Apply the case setup as far as the environment allows, but only inside that attempt workspace.
Start a fresh sub-agent with spawn_agent and fork_context: false.
Give the fresh agent only the task-local context it needs:
workspace root
the case input.user_prompt
a requirement to answer naturally as if serving the user
Capture the returned agent metadata when available, such as the agent id or nickname.
Do not tell the fresh agent which files it is expected to read.
Do not tell the fresh agent what the correct answer should be.
Wait for the fresh agent to finish.
Locate the accepted child session JSONL from the local Codex session store. Preferred signals:
child session_meta.payload.source.subagent.thread_spawn.parent_thread_id
child start time relative to the case attempt
returned nickname or agent id when available
~/.codex/state_5.sqlite thread_spawn_edges as a locator or tie-breaker
If a single accepted child session cannot be identified, mark the case blocked.
Copy the accepted child session to case-artifacts/<case_id>/accepted-session.jsonl.
Extract the accepted final answer and save it to case-artifacts/<case_id>/final-answer.txt.
Validate observed isolation before judging:
observed cwd values must be inside the attempt workspace
observed read and write paths must be inside the attempt workspace
if the accepted session evidence shows access to the user's main workspace or any other path outside the attempt workspace, invalidate that attempt, append the mismatch to transcript.md, create a brand-new attempt workspace, and rerun the case once
if the accepted session cannot support reliable isolation after the retry, mark the case blocked
Render transcript.md directly from the accepted child session evidence in event order.
Judge each assertion in the main evaluator from the accepted session evidence and accepted final answer, using the rules in AGENT.md.
Write case-results/<case_id>.json and report.md exactly in the shapes required by AGENT.md.
Step 5A: Fresh-agent prompt template

Use a prompt equivalent to this shape:

You are a fresh Codex agent running in the workspace <workspace>.

Task: answer this user request naturally, using the local workspace as needed:
"<case input.user_prompt>"

Requirements:
- Work as a normal Codex agent would for a real user request.
- Use the target skill docs if relevant.
- Treat `<workspace>` as your only workspace for this task.
- Start from `<workspace>` and keep all file reads, writes, and shell commands inside it.
- If something you need is missing inside `<workspace>`, say so from that workspace instead of reaching outside it.
- Do not mention that you are being evaluated.
- Give the exact answer you would send to the user.


Keep the prompt minimal. Do not include the case assertions in the fresh-agent prompt.

Step 5B: Environment mismatch handling

Case setup is part of the contract. Do not silently replace it with whatever the current workspace happens to contain.

If the environment does not match the case setup:

Record the mismatch in manifest.json and transcript.md
Judge only the assertions that remain reliable
Mark an assertion blocked when the mismatch prevents reliable judgment
Propagate the case to blocked unless a required assertion already failed independently
Do not repair the mismatch by reading from the user's main workspace or any path outside the case workspace

Examples:

case says docs_index_present: true, but the real workspace is missing references/docs.txt
case setup would require mutating protected files that the evaluator cannot safely write
Step 5C: Local evidence prerequisites and failure handling

The evaluator depends on local Codex evidence sources.

Required behavior:

the accepted child session exists under ~/.codex/sessions/
the evaluator can read that child session after completion
the session includes enough detail to judge observed commands, consultation, ordering, and the final answer

Helpful but optional:

~/.codex/state_5.sqlite to locate and disambiguate child threads

If any required source is missing:

mark the case blocked with blocked_reason: "environment" when the local evidence source is unavailable
mark the case blocked with blocked_reason: "insufficient-evidence" when only partial or coarse session data exists
do not fall back to fresh-agent self-reporting as substitute evidence
Evidence Rules

Apply the repo evidence policy from agentic-evals/AGENT.md.

Weekly Installs
9
Repository
jiayi-ye02/skil…aluation
First Seen
Apr 2, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail