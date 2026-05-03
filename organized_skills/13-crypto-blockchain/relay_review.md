---
rating: ⭐⭐⭐
title: relay-review
url: https://skills.sh/sungjunlee/dev-relay/relay-review
---

# relay-review

skills/sungjunlee/dev-relay/relay-review
relay-review
Installation
$ npx skills add https://github.com/sungjunlee/dev-relay --skill relay-review
SKILL.md
Relay Review

Independent PR review against the Done Criteria contract and scoring rubric. Use scripts/review-runner.js so round count, reviewer invocation, PR comments, and manifest transitions stay script-managed.

Context Isolation

Reviews MUST run in a fresh context — no prior planning, dispatch, or conversation history. This prevents planning bias from influencing the verdict.

Platform	Mechanism	How
Claude Code	context: fork frontmatter	Automatic — this SKILL.md's frontmatter triggers it
Codex (reviewer adapter)	--ephemeral --sandbox read-only	Automatic — invoke-reviewer-codex.js passes these flags
Claude (reviewer adapter)	--bare --no-session-persistence	Automatic — invoke-reviewer-claude.js passes these flags
Codex (manual inline review)	Start a new session	Manual — do not continue from the dispatch session
Other / Fallback	Prefix prompt	Prepend: "You are reviewing code you did NOT write. You have no context about why it was written this way."

Standard path: run review-runner.js --reviewer codex or --reviewer claude. In that path, isolation is already enforced by the adapter scripts. The manual "start a new session" rule applies only to inline reviews outside review-runner.

Setup: Establish the anchor
Get the PR diff and Done Criteria (this runs in a fresh context — fetch everything needed). Runner resolution order and issue inference details are in references/runner-notes.md.
PR_NUM=$(gh pr list --head <branch> --json number -q '.[0].number')
BRANCH=$(gh pr view $PR_NUM --json headRefName -q '.headRefName')
gh pr diff $PR_NUM > /tmp/pr-diff.txt
ISSUE_NUM=$(${CLAUDE_SKILL_DIR}/scripts/resolve-issue-number.sh "$PR_NUM" "$BRANCH")  # legacy manual helper; runner resolution is canonical
gh issue view $ISSUE_NUM  # Done Criteria / Acceptance Criteria source


Fix the anchor — these do NOT change across rounds:

Done Criteria from anchor.done_criteria_path when present, otherwise from the issue (the contract)
Rubric factors + targets from the Score Log (if relay-plan was used)
Original scope boundary ("do not change" areas)

Preferred path: let the review runner invoke an isolated reviewer directly:

RUN_ID=<run-id-from-dispatch>
node ${CLAUDE_SKILL_DIR}/scripts/review-runner.js --repo . --run-id "$RUN_ID" --pr "$PR_NUM" --reviewer codex --json


Supported built-in adapters:

--reviewer codex
--reviewer claude

Notes:

codex uses a read-only structured-output adapter and must return a full two-phase verdict.
claude --bare uses a separate token from the interactive Claude OAuth session; for --reviewer claude (direct or reviewer-swap), set ANTHROPIC_API_KEY or run claude login --api-key.
Model precedence for reviewer invocation is --reviewer-model -> manifest.model_hints.review -> reviewer default.
When the runner invokes the reviewer itself, it records a review_invoke event with the effective model value (or null when unset).
Fallback path for unsupported environments or debugging:
node ${CLAUDE_SKILL_DIR}/scripts/review-runner.js --repo . --branch "$BRANCH" --pr "$PR_NUM" --prepare-only --json


This writes round artifacts under ~/.relay/runs/<repo-slug>/<run-id>/. See references/runner-notes.md for artifact names, retained-checkout behavior, stale-SHA handling, and repeated-issue escalation.

Review Loop

Two phases, run in order. Each round re-measures against the original anchor, not the previous round's state.

Phase 1: Spec Compliance

Review the diff against Done Criteria (see references/reviewer-prompt.md or the generated review-round-N-prompt.md):

Faithfulness: Each Done Criteria item implemented? Scope respected?
Stubs/placeholders: Any return null, empty bodies, TODO in production paths?
Integration: Does it break callers/consumers of changed code?
Security: Auth/token handling, input validation, injection risks?

Rubric verification (when Score Log present):

The reviewer evaluates quality_review_status by inspection; the runner independently verifies quality_execution_status via a SHA-bound execution-evidence artifact. The reviewer cannot execute code, so quality evidence comes from two trust roots.
Re-score ALL evaluated quality factors with fresh eyes (0-10) and include numeric score / target_score; contract factors stay pass/fail and may use null numeric fields
Any required factor below target → issue
The runner computes executor/reviewer divergence and re-dispatches toward the weakest below-target quality factor before falling back to generic issue repair

Phase 1 gate: Issues found → return a structured verdict with verdict=changes_requested, then re-dispatch (see Re-dispatch below). Do NOT proceed to Phase 2 until Phase 1 passes.

Phase 2: Code Quality (only after Phase 1 PASS)
Run a code review skill on changed files — check code quality, patterns, conventions, structural issues (use the platform's best-matching skill, e.g., Claude Code: /review; if no skill is available, perform the quality review inline inside the structured reviewer round)
Run a code simplification skill on changed files — unnecessary complexity, dead code, verbose patterns (use the platform's best-matching skill, e.g., Claude Code: /simplify; if no skill is available, review for simplification inline before returning verdict=pass)
Issues found → return verdict=changes_requested, then re-dispatch and repeat from step 5 (Phase 1 — quality fixes can regress spec compliance)
Drift and stuck detection (both phases)

Before any re-dispatch, check:

Scope: Does the fix address a review issue, or is it scope creep?
Regression: Are previously passing rubric factors still passing?
Churn: Is the total diff growing without convergence?
Score trend: Is the same quality factor flat for 3 rounds? If yes, pivot implementation approach without expanding scope, or escalate.
Stuck: Same issue 3+ consecutive rounds → escalate immediately (not fixable by the executor).
Converge
Both phases pass → produce a structured verdict with:
verdict=pass
next_action=ready_to_merge
issues=[]

Safety cap: 20 rounds total. Ceiling, not target — most PRs converge in 1-3 rounds. Hitting the cap means something is structurally wrong; escalate.

Verdict + Audit Trail
If you used the fallback path, apply the structured verdict with the review runner:
node ${CLAUDE_SKILL_DIR}/scripts/review-runner.js --repo . --run-id "$RUN_ID" --pr "$PR_NUM" --review-file /tmp/review-verdict.json


The runner validates the verdict, writes the PR audit comment, updates manifest state, and records round artifacts. See references/runner-notes.md for the full audit-trail and backward-compatibility behavior.

Re-dispatch (when issues found)

Use the generated review-round-N-redispatch.md artifact as the targeted fix prompt. It already includes the issue list, scope guardrail, and original Done Criteria.

See references/evaluate-criteria.md for escalation policy (auto re-dispatch vs ask user).

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