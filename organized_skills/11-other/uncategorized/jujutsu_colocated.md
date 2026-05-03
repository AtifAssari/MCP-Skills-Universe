---
rating: ⭐⭐⭐
title: jujutsu-colocated
url: https://skills.sh/khoahyh/skills/jujutsu-colocated
---

# jujutsu-colocated

skills/khoahyh/skills/jujutsu-colocated
jujutsu-colocated
Installation
$ npx skills add https://github.com/khoahyh/skills --skill jujutsu-colocated
SKILL.md
Jujutsu Colocated Workflow

Use this skill to execute jj-first workflows safely in repositories where git and jj coexist.

Detect VCS First

Run this before any VCS command:

if jj root &>/dev/null; then echo "jj"
elif git rev-parse --show-toplevel &>/dev/null; then echo "git"
else echo "none"
fi


Interpretation:

jj: continue with this skill (also covers colocated repos).
git: stop and report that this is a Git-only repository. Ask the user to colocate before continuing with this skill (for example, run jj git init --git-repo . from the repo root, then verify with jj git colocation status).
none: stop and report no repository detected.

Default to jj help <command> for command syntax to keep context lean. Use Context7 selectively for nuanced or best-practice questions (for example colocation caveats, safety guidance, and version-migration differences).

In colocated repositories, prefer read-only git commands and use jj for mutating operations.

Follow Non-Negotiable Safety Rules
Treat working copy @ as a real commit, not a staging area.
Use one workspace per agent for parallel work; never share a workspace path across active agents.
Refer to work using change IDs when coordinating; commit IDs can change after rewrites.
Use jj op log as the recovery source of truth.
Treat bookmarks as publication pointers, not a current-branch model.
Never run destructive history/state operations without explicit written approval in-thread.
Never edit .env or environment variable files.
Never revert or delete other agents' work without coordination.
Workspace and Worktree Naming Convention

Use one canonical token for JJ workspace names and Git worktree directory names:

<repo>-<agent>-<task>


Rules:

repo: short repository slug (for example billing-api).
agent: stable agent identifier (for example hephaestus, reviewer-2).
task: short kebab-case task slug (for example token-refresh).
Keep names lowercase and ASCII; avoid spaces and punctuation beyond -.
If the same agent repeats the same task, append a short disambiguator (for example -v2, -2, -20260210).

Example:

billing-api-hephaestus-token-refresh


Cross-tool policy:

JJ: pass --name <repo>-<agent>-<task> explicitly so workspace identity does not depend on path basename inference.
Git worktree: pass -b <branch> explicitly; do not rely on git worktree add <path> default branch-from-path behavior.
Recommended Git branch shape for agent worktrees: wip/<agent>/<task>.

Forbidden without explicit written approval:

jj op restore ...
jj op abandon ...
jj util gc
jj bookmark set --allow-backwards ...
jj abandon <shared-change>
jj bookmark delete <shared-bookmark>
destructive Git fallbacks (git reset --hard, git checkout --, broad git restore, rollback rm)
Use Conventional Commit Descriptions

In jj, the -m value is the change description (commit message equivalent). Require Conventional Commit format:

<type>(<scope>): <description>


Allowed types:

feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert

Examples:

feat(auth): add token refresh flow
fix(sync): avoid duplicate bookmark tracking
chore(integration): merge parallel agent changes
Core Workflow
Sync first:
jj git fetch --remote origin

Create a dedicated workspace for this agent from mainline, with the first scoped change already described:
jj workspace add --name <repo>-<agent>-<task> --revision main@origin \
  -m "<type(scope): description>" ../<repo>-<agent>-<task>
cd ../<repo>-<agent>-<task>
jj workspace list

Create additional scoped changes in that workspace only when needed:
jj new -m "<type(scope): description>"

Keep one logical concern per change:
jj split -i
jj squash --into <target-change>

Inspect and pick publish targets (plain English):
jj status
jj diff
jj log -r "main@origin..@" --reversed --no-graph \
  -T 'change_id.short() ++ " | " ++ description.first_line() ++ "\n"'

Publish selected change(s) explicitly (single PR or stack):
# Single PR in this workspace
jj bookmark set pr/<agent>/<task> -r <change-id>
jj git push --bookmark pr/<agent>/<task> --remote origin

# Stacked PRs in this workspace
jj bookmark set pr/<agent>/<task>/01 -r <change-id-1>
jj bookmark set pr/<agent>/<task>/02 -r <change-id-2>
jj git push --bookmark pr/<agent>/<task>/01 --bookmark pr/<agent>/<task>/02 --remote origin


CI guardrails:

Push only selected bookmarks. Never use broad push patterns for publish.
Reuse stable bookmark names with jj bookmark set to avoid creating extra CI-triggering branches.
Resolve conflicts intentionally (never by deleting peers' edits):
jj resolve --list
jj resolve

Retire temporary workspaces after integration:
jj workspace list
jj workspace forget <workspace-name>

Recovery Ladder
Use jj undo for immediate local mistakes.
Use jj op log and inspect prior states.
Use operation-level restore only with explicit approval.
References
Colocated playbooks: references/colocated-workflows.md
Git-to-JJ mental model: references/git-to-jj-map.md
Safety and recovery rules: references/safety-and-recovery.md
Parallel multi-agent contract: references/parallel-agent-contract.md
Weekly Installs
13
Repository
khoahyh/skills
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn