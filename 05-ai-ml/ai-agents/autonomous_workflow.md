---
title: autonomous-workflow
url: https://skills.sh/mthines/gw-tools/autonomous-workflow
---

# autonomous-workflow

skills/mthines/gw-tools/autonomous-workflow
autonomous-workflow
Installation
$ npx skills add https://github.com/mthines/gw-tools --skill autonomous-workflow
SKILL.md
Autonomous Workflow

Execute complete feature development cycles autonomously — from task intake through tested PR delivery — using isolated Git worktrees.

CRITICAL: Before Starting ANY Work

You MUST complete these steps IN ORDER before writing any code:

Step 1: Detect Workflow Mode (MANDATORY)

Analyze the task scope to determine the workflow mode:

Mode	Criteria	Artifacts Required
Full	4+ files OR complex/architectural	YES - MANDATORY
Lite	1-3 files AND simple/straightforward	No

When in doubt, choose Full Mode.

Step 2: Plan Artifact Content (Full Mode ONLY)

For Full Mode, you will need these artifacts. Do NOT create the files yet — they must be created inside the worktree after Phase 2, not on the main branch.

File	Purpose	Created
plan.md	Implementation strategy, decisions, requirements, progress log	After Phase 2
walkthrough.md	Final summary for PR delivery	Phase 6

plan.md is the single source of truth. It must be comprehensive enough that a new Claude session can execute from it alone without the original conversation.

DO NOT create artifact files on the main branch.

Step 3: Announce Mode Selection

State your mode selection explicitly:

"This is a Full Mode task (affects 5+ files). Creating .gw/{branch-name}/ artifacts after worktree setup."

or

"This is a Lite Mode task (2 files, simple fix). Proceeding without artifacts."

Prerequisites: gw CLI Installation

Before Phase 2 (Worktree Setup), verify the gw CLI is installed:

which gw

If gw is NOT installed

STOP and prompt the user to install gw. The workflow cannot proceed without it.

Installation options (present to user):

# Via npm (recommended)
npm install -g @gw-tools/gw

# Via Homebrew (macOS)
brew install mthines/gw-tools/gw

# Via pnpm
pnpm add -g @gw-tools/gw


After installation, set up shell integration:

# For zsh (add to ~/.zshrc)
echo 'eval "$(gw install-shell)"' >> ~/.zshrc
source ~/.zshrc

# For bash (add to ~/.bashrc)
echo 'eval "$(gw install-shell)"' >> ~/.bashrc
source ~/.bashrc


Verify installation:

gw --version
gw --help


Then initialize gw in the repository (if not already done):

gw init
gw init --auto-copy-files .env,secrets/ --post-checkout "npm install"


Once gw is installed and configured, resume the workflow from Phase 2.

Rules
Rule	Description
overview	HIGH - Workflow phases, when to use, expected outcomes
smart-worktree-detection	CRITICAL - Fuzzy match task to current worktree before creating new
phase-0-validation	CRITICAL - MANDATORY - Validate requirements before any work
phase-1-planning	HIGH - Deep codebase analysis and implementation planning
phase-2-worktree	CRITICAL - MANDATORY - Create isolated worktree with gw add
phase-3-implementation	HIGH - Incremental implementation with verification after each change
phase-4-testing	CRITICAL - Fast iteration loop until tests pass (Ralph Wiggum pattern)
phase-5-documentation	MEDIUM - Update README, CHANGELOG, API docs
phase-6-pr-creation	HIGH - Create draft PR, deliver results
phase-7-cleanup	LOW - Optional worktree removal after merge
decision-framework	HIGH - Branch naming, test strategy, iteration decisions
error-recovery	HIGH - Recovery procedures for common errors
safety-guardrails	CRITICAL - Validation checkpoints, resource limits, rollback
parallel-coordination	HIGH - Multi-agent coordination, handoff protocol
artifacts-overview	HIGH - Two-artifact pattern (Plan, Walkthrough), file locations
walkthrough-generation	MEDIUM - Final summary generation at Phase 6
Templates
Template	Purpose
plan.template.md	Implementation plan with progress log
walkthrough.template.md	Final summary for PR delivery
agent.template.md	Agent file (copy to ~/.claude/agents/)
routing-rule.template.md	Auto-trigger rule (copy to .claude/rules/)
Auto-Trigger Setup (Recommended)

Install the agent and routing rule so Claude auto-triggers on phrases like "independently", "in isolation".

Option A: Global (personal use — works in all projects)

mkdir -p ~/.claude/agents && \
  ln -sf ~/.claude/skills/autonomous-workflow/templates/agent.template.md \
     ~/.claude/agents/autonomous-workflow.md


Then add the routing rule per-project:

mkdir -p .claude/rules && \
  ln -sf ~/.claude/skills/autonomous-workflow/templates/routing-rule.template.md \
     .claude/rules/autonomous-workflow-routing.md


Option B: Project-level (team use — committable to git, customizable)

mkdir -p .claude/agents .claude/rules && \
  ln -sf ~/.claude/skills/autonomous-workflow/templates/agent.template.md \
     .claude/agents/autonomous-workflow.md && \
  ln -sf ~/.claude/skills/autonomous-workflow/templates/routing-rule.template.md \
     .claude/rules/autonomous-workflow-routing.md


To customize the agent for a specific project, copy instead of symlink and edit directly. See routing-rule.template.md and agent.template.md for details.

Quick Reference
Full Mode (4+ files, complex changes)
Phase	Command/Action
0. Validation	Ask clarifying questions, get user confirmation, detect mode
1. Planning	Analyze codebase, prepare plan content in conversation (verbose, all detail)
2. Worktree	gw add feat/feature-name, then CREATE & POPULATE .gw/{branch}/plan.md
3. Implementation	Code in worktree, verify after editing, update Progress Log at milestones
4. Testing	npm test, iterate until passing, log results in Progress Log
5. Documentation	Update README, CHANGELOG
6. PR Creation	CREATE walkthrough.md, gh pr create --draft, SHOW walkthrough to user
7. Cleanup	gw remove feat/feature-name (after merge)
Lite Mode (1-3 files, simple changes)
Phase	Command/Action
0. Validation	Quick clarification if needed
1. Planning	Brief mental plan (no artifact files)
2. Worktree	gw add fix/bug-name
3. Implementation	Code directly, commit when done
4. Testing	npm test, fix any failures
5. PR Creation	gh pr create --draft
Key Principles
Detect workflow mode FIRST: Determine Full vs Lite before any other action.
plan.md is the single source of truth: Must be comprehensive enough for a new session to execute alone.
Always validate first (Phase 0): Never skip directly to implementation.
Always create worktree (Phase 2): Isolation is mandatory.
Verify after editing: Run fast checks after each change, full suite before PR.
Iterate until correct: No artificial iteration limits (Ralph Wiggum pattern).
CREATE walkthrough.md AND SHOW IT at Phase 6: MANDATORY for Full Mode.
Stop and ask when blocked: Don't guess on ambiguity.
Artifact System

The workflow produces two artifacts in .gw/{branch-name}/:

Artifact	File	Created	Purpose
Plan	plan.md	Phase 2 (end)	Implementation strategy, decisions, progress log
Walkthrough	walkthrough.md	Phase 6	Final summary for PR delivery

Files are gitignored and grouped by branch for easy browsing.

All timestamps in artifact frontmatter MUST use full ISO 8601 with time: YYYY-MM-DDTHH:MM:SSZ (e.g. 2026-03-07T14:30:00Z).

Workflow Flow
Phase 0: Validation <- MANDATORY
    | (user confirms)
Phase 1: Planning (prepare content IN CONVERSATION, no files yet)
    | (plan validated)
Phase 2: Worktree Setup <- MANDATORY
    | Full Mode: CREATE & POPULATE plan.md INSIDE worktree
    | (worktree created, plan.md populated)
Phase 3: Implementation
    | Verify after editing. Update Progress Log at milestones.
    | (code complete)
Phase 4: Testing <- iterate until passing
    | (all tests pass)
Phase 5: Documentation
    | (docs complete)
Phase 6: PR Creation
    | Full Mode: CREATE walkthrough.md + SHOW to user
    | (draft PR delivered)
Phase 7: Cleanup (optional)

Smart Worktree Detection

Before creating a new worktree, the workflow checks if the current context matches the task:

Scenario	Action
On main/master	Always create new worktree
Worktree name matches task keywords	Prompt user to continue or create new
No keyword match	Create new worktree
Fast Iteration Loop (Phase 4)

Based on the Ralph Wiggum pattern:

while not all_tests_pass:
    1. Run tests
    2. If pass: done
    3. If fail: analyze -> fix -> commit -> continue
    4. Safety: warn at 10 iterations, stop at 20

Troubleshooting Quick Reference
Issue	Check	Recovery
Wrong worktree	gw list, pwd	gw cd <correct-branch>
gw command not found	which gw	npm install -g @gw-tools/gw
Secrets missing	cat .gw/config.json	gw sync <branch> .env
Tests keep failing	plan.md Progress Log	Focus on ONE failure, escalate at 7+
Agent hallucinated cmd	Error message	See error-recovery
plan.md empty	cat .gw/{branch}/plan.md	STOP, populate plan.md before proceeding
walkthrough.md missing	ls .gw/{branch}/	Create before announcing completion
Related Skills
git-worktree-workflows - Worktree fundamentals
gw-config-management - Configure auto-copy and hooks
References

Detailed examples and scenarios (loaded on-demand):

Complete Workflow Example
Error Recovery Scenarios
Iterative Refinement Example
Research Sources
Google Antigravity Artifacts - Artifact pattern
Ralph Wiggum AI Coding Loops - Iteration pattern
Addy Osmani's LLM Workflow - Fast feedback loops
Claude Code Worktree Support - Best practices
Weekly Installs
34
Repository
mthines/gw-tools
GitHub Stars
7
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass