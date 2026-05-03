---
rating: ⭐⭐⭐
title: autonomous-dev
url: https://skills.sh/zxkane/autonomous-dev-team/autonomous-dev
---

# autonomous-dev

skills/zxkane/autonomous-dev-team/autonomous-dev
autonomous-dev
Installation
$ npx skills add https://github.com/zxkane/autonomous-dev-team --skill autonomous-dev
SKILL.md
Contains Hooks

This skill uses Claude hooks which can execute code automatically in response to events. Review carefully before installing.

TDD Development Workflow

A complete development workflow enforcing test-driven development, git worktree isolation, code review, CI verification, and E2E testing. Works in two modes: interactive (default) for human-guided sessions, and autonomous for fully unattended GitHub issue implementation.

NON-NEGOTIABLE RULES -- Every step marked MANDATORY is required. You MUST NOT skip, defer, or ask the user whether to run these steps. Execute them automatically as part of the workflow. This includes: creating PRs, waiting for CI, running E2E tests, and addressing reviewer findings.

Mode Detection
Interactive Mode (default)

Used when a developer is present. The workflow:

Asks the user for design approval before proceeding to implementation
Presents design canvases and waits for feedback
Pauses at key decision points for user input
Reports final status and lets the user decide when to merge
Autonomous Mode

Triggered when running inside the scripts/autonomous-dev.sh wrapper. The workflow:

Makes all decisions autonomously (see "Decision Making Guidelines" below)
Posts progress comments to the GitHub issue instead of asking questions
Creates design docs but skips interactive approval
Stops after verification -- does not merge (the review agent handles that)
Marks requirement checkboxes in the issue body as work progresses
Cross-Platform Notes
Hooks Support
IDE/CLI	Hooks Support	Setup
Claude Code	Full	hooks/README.md
Kiro CLI	Full	hooks/README.md
Cursor	None	Follow steps manually
Windsurf	None	Follow steps manually
Gemini CLI	None	Follow steps manually
Tool Name Mapping

This skill uses generic language. Map to your IDE's tools:

"Execute in your terminal" = Bash tool (Claude Code), terminal (Cursor), shell (Gemini CLI), etc.
"Read the file" = Read tool, file viewer, or cat
"Create or edit the file" = Write/Edit tool, editor, or manual editing
"Use a subagent" = Task/Agent tool (Claude Code), or follow the steps manually if unsupported
"Load the skill" = Skill tool (Claude Code), or read the referenced SKILL.md directly
Workflow Enforcement (Optional Hooks)

If your IDE/CLI supports hooks (Claude Code, Kiro CLI), install them from hooks/ for hard enforcement. See hooks/README.md for setup.

Without hooks, follow each step manually -- the discipline is the same.

Development Workflow Overview

Follow this workflow for all feature development and bug fixes:

Step 1:  DESIGN CANVAS (Pencil MCP, if available)
Step 2:  CREATE GIT WORKTREE (MANDATORY)
Step 3:  WRITE TEST CASES (TDD)
Step 4:  IMPLEMENT CHANGES
Step 5:  LOCAL VERIFICATION
Step 6:  CODE SIMPLIFICATION
Step 7:  COMMIT AND CREATE PR          -- MANDATORY
Step 8:  PR REVIEW AGENT               -- MANDATORY
Step 9:  WAIT FOR ALL CI CHECKS        -- MANDATORY
Step 10: ADDRESS REVIEWER BOT FINDINGS -- MANDATORY
Step 11: ITERATE UNTIL NO FINDINGS
Step 12: E2E TESTS & READY FOR MERGE   -- MANDATORY
Step 13: CLEANUP WORKTREE

Step 1: Design Canvas

Available if your IDE has Pencil MCP. If Pencil MCP is not available, create a design document (docs/designs/<feature>.md) manually instead.

When to Create a Design Canvas
New UI components or pages
Feature implementations with user-facing changes
Architecture decisions that benefit from visualization
Complex data flows or state management
Pencil MCP Workflow
Check editor state: call get_editor_state() to see if a .pen file is open.
Open or create design file: call open_document("docs/designs/<feature>.pen") or open_document("new").
Get design guidelines (if needed): call get_guidelines(topic="landing-page|table|tailwind|code").
Get style guide for consistent design: call get_style_guide_tags() then get_style_guide(tags=[...]).
Create design elements: call batch_design(operations) to create UI mockups, component hierarchy diagrams, data flow visualizations, and architecture diagrams.
Validate design visually: call get_screenshot() to verify the design looks correct.
Document design decisions: add text annotations explaining choices, component specifications, and interaction patterns.
Design Canvas Template Structure
Feature: <Feature Name>
Date: YYYY-MM-DD
Status: Draft | In Review | Approved

- UI Mockup / Wireframe
- Component Architecture (component tree, props/state flow)
- Data Flow Diagram (API calls, state management)
- Design Notes (key decisions, accessibility, responsive behavior)

Design Approval
Interactive mode: Present the design canvas to the user, get explicit approval, document feedback, update status to "Approved."
Autonomous mode: Create the design doc and proceed immediately -- no approval gate.
Step 2: Create Git Worktree (MANDATORY)

Every change MUST be developed in an isolated git worktree. Never develop directly on the main workspace.

Enforced by block-commit-outside-worktree.sh hook (if hooks are installed). Commits outside worktrees are automatically blocked. Direct pushes to main are blocked by block-push-to-main.sh.

Why Worktrees?
Isolation: Each feature/fix gets its own directory, preventing cross-contamination
Parallel work: Multiple features can be in progress simultaneously
Clean main workspace: The main checkout stays on main, ready for quick checks
Safe rollback: Discard a worktree without affecting the main workspace
Worktree Creation Process

Execute in your terminal:

# 1. Determine branch name based on change type
#    feat/<name>, fix/<name>, refactor/<name>, etc.
BRANCH_NAME="feat/my-feature"

# 2. Create worktree with new branch from main
git worktree add .worktrees/$BRANCH_NAME -b $BRANCH_NAME

# 3. Enter the worktree
cd .worktrees/$BRANCH_NAME

# 4. Install dependencies (use your project's package manager)
npm install  # or: bun install, yarn install, pnpm install

# 5. Verify clean baseline
npm run build && npm test

Directory Convention
Item	Value
Worktree root	.worktrees/ (project-local, gitignored)
Path pattern	.worktrees/<branch-name>
Example	.worktrees/feat/user-authentication
Safety Checks

Before creating any worktree, verify .worktrees/ is in .gitignore:

git check-ignore -q .worktrees 2>/dev/null || echo "WARNING: .worktrees not in .gitignore!"

All Subsequent Steps Run INSIDE the Worktree

After creating the worktree, all development commands (test, lint, build, commit, push) are executed from within the worktree directory. The main workspace is not touched until cleanup.

Step 3: Write Test Cases (TDD)

Before writing any implementation code:

Read the design canvas and requirements
Identify all user scenarios, edge cases, and error handling paths
Create or edit the test case document: docs/test-cases/<feature>.md
List all test scenarios (happy path, edge cases, error handling)
Assign test IDs (e.g., TC-AUTH-001)
Define expected results and acceptance criteria
Create unit test skeletons
Create E2E test cases if applicable
Step 4: Implement Changes
Write code following the test cases (inside the worktree)
Write new unit tests for new functionality
Update existing tests if behavior changed
Ensure implementation covers all test scenarios
Step 5: Local Verification

Execute in your terminal:

npm run build
npm run test


Fix any failures before proceeding. Deploy and verify locally if applicable.

Step 6: Code Simplification
Use a subagent if your IDE supports them (e.g., code-simplifier:code-simplifier), otherwise review the code manually for unnecessary complexity.
Address simplification suggestions.
Mark complete (if hooks are installed):
hooks/state-manager.sh mark code-simplifier

Step 7: Commit and Create PR (MANDATORY)
Commit

Execute in your terminal:

git add <files>
git commit -m "type(scope): description"
git push -u origin <branch-name>

Create PR
gh pr create --title "type(scope): description" --body "$(cat <<'EOF'
## Summary
<1-3 bullet points describing the change>

## Design
- [ ] Design canvas created (`docs/designs/<feature>.pen`)
- [ ] Design approved

## Test Plan
- [ ] Test cases documented (`docs/test-cases/<feature>.md`)
- [ ] Build passes (`npm run build`)
- [ ] Unit tests pass (`npm run test`)
- [ ] CI checks pass
- [ ] Code simplification review passed
- [ ] PR review agent review passed
- [ ] Reviewer bot findings addressed (no new findings)
- [ ] E2E tests pass

## Checklist
- [ ] New unit tests written for new functionality
- [ ] E2E test cases updated if needed
- [ ] Documentation updated if needed
EOF
)"

Update PR Checklist

After completing each step, update the PR description:

gh pr view {pr_number} --json body --jq '.body' > /tmp/pr_body.md
# Edit the checklist (mark items as [x])
gh pr edit {pr_number} --body "$(cat /tmp/pr_body.md)"

Step 8: PR Review Agent (MANDATORY)
Use a subagent if your IDE supports them (e.g., /pr-review-toolkit:review-pr), otherwise perform a self-review against the PR diff.
Address findings by severity:
Critical/Severe: Must fix
High: Must fix
Medium: Should fix
Low: Optional
Mark complete (if hooks are installed):
hooks/state-manager.sh mark pr-review

Step 9: Wait for All CI Checks (MANDATORY -- DO NOT SKIP)

Execute in your terminal:

# Watch all checks until completion
gh pr checks {pr_number} --watch --interval 30


ALL checks must pass: Lint, Unit Tests, Build, Deploy Preview, E2E Tests.

If ANY check fails: analyze logs, fix, push, re-watch. DO NOT proceed until every check shows "pass."

Checks to Monitor
Check	Description	Action if Failed
CI / build-and-test	Build + unit tests	Fix code or update snapshots
Security Scan	SAST, npm audit	Fix security issues
Amazon Q Developer	Security review	Address findings, retrigger with /q review
Codex	AI code review	Address findings, retrigger with /codex review
Other review bots	Various checks	Address findings, retrigger per bot docs
Step 10: Address Reviewer Bot Findings (MANDATORY)

Multiple review bots can provide automated code review findings on PRs:

Bot	Trigger Command	Bot Username
Amazon Q Developer	/q review	amazon-q-developer[bot]
Codex	/codex review	codex[bot]
Other bots	See bot documentation	Varies
Handling Bot Review Findings
Review all comments -- read each finding carefully
Determine action:
Valid issue: fix the code and push
False positive: reply explaining the design decision
Reply to each thread -- use direct reply, not a general PR comment
Resolve each thread -- mark conversation as resolved
Retrigger review -- comment with the appropriate trigger (e.g., /q review, /codex review)
Retrigger Bot Reviews

IMPORTANT: Some bot reviewers (e.g., Amazon Q Developer) ignore /q review comments posted by GitHub App bot accounts. If your project uses scripts/gh-as-user.sh, you MUST use it to trigger bot reviews so the comment is attributed to a real user. Do NOT use the default gh wrapper for bot review triggers.

# Amazon Q Developer (use gh-as-user.sh to post as a real user)
bash scripts/gh-as-user.sh pr comment {pr_number} --body "/q review"

# Codex
bash scripts/gh-as-user.sh pr comment {pr_number} --body "/codex review"


If scripts/gh-as-user.sh is not available in your project, use gh pr comment directly as a fallback.

Wait 60-90 seconds for the review to complete, then check for new comments.

Step 11: Iterate Until No Findings

Repeat until review bots find no more issues:

Address findings (fix code or explain design)
Reply to each comment thread
Resolve all threads
Trigger review command (/q review, /codex review, etc.)
Wait 60-90 seconds
Check for new findings
If new findings: repeat from step 1
Only proceed when no new positive findings appear
Step 12: E2E Tests & Ready for Merge (MANDATORY -- DO NOT SKIP)
Run E2E tests against the deployed preview environment (all tests must pass; skipped agent-dependent tests are acceptable)
Mark complete (if hooks are installed):
hooks/state-manager.sh mark e2e-tests

Update PR checklist to show all items complete
STOP HERE: report status to the user (interactive mode) or post a summary comment on the issue (autonomous mode)
User or review agent decides when to merge
Step 13: Cleanup Worktree

After the PR is merged or closed, execute in your terminal:

# Return to main workspace
cd $(git rev-parse --show-toplevel)

# Remove the worktree
git worktree remove .worktrees/<branch-name>

# Prune stale worktree references
git worktree prune

References

For detailed commands and conventions, consult:

references/commit-conventions.md -- Branch naming and commit message conventions
references/review-commands.md -- Complete gh CLI and GraphQL command reference
references/review-threads.md -- Review thread management, response patterns, and quick reference commands
references/autonomous-mode.md -- Decision making, resume awareness, requirement tracking, pre-existing changes, bot review integration, and error recovery (autonomous mode only)
Weekly Installs
34
Repository
zxkane/autonomo…dev-team
GitHub Stars
15
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn