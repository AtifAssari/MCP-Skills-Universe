---
rating: ⭐⭐⭐
title: relay
url: https://skills.sh/sungjunlee/dev-relay/relay
---

# relay

skills/sungjunlee/dev-relay/relay
relay
Installation
$ npx skills add https://github.com/sungjunlee/dev-relay --skill relay
SKILL.md
Dev Relay

Execute the plan → dispatch → review cycle. Stop at ready_to_merge unless the user explicitly asks to merge. Follow ALL steps below in order.

Role Defaults
Role	Default	Override
Orchestrator	unknown until explicitly stamped	RELAY_ORCHESTRATOR env
Executor	Codex	--executor flag
Reviewer	unknown until explicitly stamped	--reviewer flag, RELAY_REVIEWER env

Standard Codex path: stamp RELAY_ORCHESTRATOR=codex and run review through review-runner --reviewer codex. Assigned manifest roles stay immutable; the acting reviewer for a round is recorded separately under review.last_reviewer and the review_apply event.

Step 0: Re-Anchor

Always run before every task — standalone or batch. Ensures current state, not stale context.

git fetch origin — check for divergence from remote
If sprint file exists: re-read it. Check Running Context for new entries from previous tasks. Note completed/in-flight task status changes.
If previous task added Running Context that affects this task, adjust your approach before proceeding.

No sprint file? Just do the git fetch. Takes <5 seconds; never skip this step.

Step 1: Route and Read Context

Gather task details and sprint context:

Task evidence (try in order, use first that succeeds):
Local task file: backlog/tasks/{PREFIX}-{N} - {Title}.md
GitHub: gh issue view <N>
User-provided description (from argument or conversation)
Sprint context (optional): If backlog/sprints/ has an active sprint file, read Running Context and batch info. If no sprint file, proceed without — sprint tracking is skipped.
Fast path vs intake path:
Bypass intake only when the input is already one relay-ready task, has a stable review anchor, and needs no clarification or decomposition.
Otherwise run relay-intake first, persist a request artifact, and use the generated relay-ready/<leaf-id>.md as the downstream source of truth.

If no issue number, use a descriptive branch name (e.g., feat/<slug>) and skip issue-close in Step 6.

Intake path

If intake is required, persist a single-leaf contract first:

${CLAUDE_SKILL_DIR}/../relay-intake/scripts/persist-request.js --repo . --contract-file /tmp/relay-intake-contract.json --json


Carry these artifacts forward:

handoff brief: ~/.relay/requests/<repo-slug>/<request-id>/relay-ready/<leaf-id>.md
frozen Done Criteria: ~/.relay/requests/<repo-slug>/<request-id>/done-criteria/<leaf-id>.md
linkage: request_id, leaf_id
Step 1.5: Check for in-flight work

Check if this issue already has a PR in progress:

PR_NUM=$(gh pr list --head issue-<N> --json number -q '.[0].number')

PR exists and open → skip Steps 2-3, go directly to Step 4 (review)
PR exists and merged → update sprint file to [x] (if exists), done
PR not found → continue to Step 2
Step 2: Plan

Always build a rubric. Follow relay-plan's planning process (read task → recover Done Criteria → build rubric → generate prompt). Do NOT dispatch from relay-plan — Step 3 below handles dispatch. See relay-plan SKILL.md for rubric depth by task size (S/M/L/XL).

Write the dispatch prompt to a temp file (e.g., /tmp/dispatch-<N>.md). If intake ran, the relay-ready handoff brief becomes the task source of truth for planning. Write the rubric YAML to a temp file (e.g., /tmp/rubric-<N>.yaml).

Step 3: Dispatch (relay-dispatch)
${CLAUDE_SKILL_DIR}/../relay-dispatch/scripts/dispatch.js . \
  -b issue-<N> --prompt-file /tmp/dispatch-<N>.md --rubric-file /tmp/rubric-<N>.yaml --timeout 3600
# If intake ran, append: --request-id <id> --leaf-id <id> --done-criteria-file <done-criteria-path>


While dispatch runs in the background, optionally monitor progress:

git -C <worktree> log --oneline        # new commits
wc -l <stdoutLog>                       # output growth


Wait for completion. Check result:

status: "completed" and runState: "review_pending" → proceed to Step 4
status: "completed-with-warning" and runState: "review_pending" → executor timed out but made progress; check worktree, proceed to Step 4
status: "failed" and runState: "escalated" → inspect the dispatch error / manifest, fix and re-dispatch

Capture the run metadata from dispatch output:

runId
manifestPath
runState

Get PR number:

PR_NUM=$(gh pr list --head issue-<N> --json number -q '.[0].number')


The manifest is written under ~/.relay/runs/<repo-slug>/. This is the shared state surface for later review/merge lifecycle work. Intake linkage is recorded there, but the run lifecycle remains execution-only.

Current scope: dispatch writes the manifest. Review and merge still follow their existing PR-comment and gate-check flow.

If sprint file exists, mark Plan item as in-flight: [~] #42 OAuth2 flow → PR #89 (reviewing)

Step 4: Review (relay-review)

MANDATORY. Do NOT skip this step.

Verify PR exists: gh pr list --head issue-<N>

Invoke relay-review in an isolated context (no planning bias). It runs two phases (Spec Compliance → Code Quality), re-dispatches on issues, and updates manifest state. See relay-review SKILL.md for the Phase 1/2 procedure, Context Isolation per platform, and runner details.

The rubric from relay-plan anchors each iteration — prevents context drift across rounds. Safety cap: 20 rounds (most PRs converge in 1-3).

Do NOT review inline — relay-review must run in an isolated context to prevent planning bias.

Step 5: Ready to Merge

If relay-review returns LGTM, the review runner should already have recorded the run as ready_to_merge. Do not mark the sprint task complete yet. Only run relay-merge when the user explicitly wants to land the PR.

Create follow-up issues if discovered during review.

Batch Mode

When multiple independent tasks are ready, dispatch in parallel instead of running sequential relay cycles. See references/batch-mode.md for the full flow (plan all → dispatch all → review as completed → merge one-by-one), merge-conflict recovery, and the "when in doubt, run sequentially" principle.

Summary Checklist

After completing the relay cycle, verify:

 Done Criteria fully implemented (relay-review confirmed)
 PR has <!-- relay-review --> LGTM comment (or <!-- relay-review-skip --> with reason)
 PR marked ready_to_merge, or merged and closed if relay-merge was explicitly requested
 Sprint file updated — if exists (Plan [x], Progress entry with review round count)
 Follow-up issues created (if applicable)
Weekly Installs
13
Repository
sungjunlee/dev-relay
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn