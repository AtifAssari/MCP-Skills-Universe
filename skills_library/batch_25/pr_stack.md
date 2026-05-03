---
title: pr-stack
url: https://skills.sh/ouj/skills/pr-stack
---

# pr-stack

skills/ouj/skills/pr-stack
pr-stack
Installation
$ npx skills add https://github.com/ouj/skills --skill pr-stack
SKILL.md
PR Stack

Use this skill for stacked PR workflows built on top of plain git and gh.

Mental Model

A stack has:

A trunk branch, usually the repo default branch.
Feature branches where each branch has one intended parent.
Pull requests whose base branch is that parent, not always trunk.

Track stack relationships explicitly:

Required: stack.trunk=<branch>, branch.<name>.stackParent=<parent-branch>
Strongly recommended: stack.remote=<remote>, branch.<name>.stackParentRemoteRef=<remote>/<parent-branch>

Use stack.trunk and branch.<name>.stackParent as the source of truth. Resolve PR state live through gh. Derive children by scanning branches for matching stackParent values.

Treat GitHub PR bases as derived state that must match the recorded parent chain. In a healthy stack, each branch PR targets its previous branch in the stack, except the bottom branch which targets trunk.

If required metadata is missing, infer a recommended parent from Git ancestry or existing PR bases, mark it as inferred, and ask the user to confirm before any operation that would rewrite history or change PR bases.

Rules
Resolve state first: inspect git status -sb, current branch, trunk, and a concise branch graph; confirm gh auth for PR operations; never operate on detached HEAD.
Protect history: never rewrite the default branch, never use plain --force, and check for existing PRs before creating new ones.
Handle dirty trees deliberately: if the worktree is dirty, decide whether branch switching or rebasing is safe before continuing.
Resolve conflicts automatically when the correct result is clear from local context and stack intent; otherwise stop and report the blocker.
Treat merged parents specially: retarget the child to the next surviving parent or trunk, then restack.
Repair PR base drift explicitly: during submit or retarget flows, update every existing GitHub PR base to the recorded parent branch, even if the PR already exists and even if only one branch's commits changed.
If a branch's remote PR is closed or merged, ask whether the local branch should be deleted before cleaning it up.
Recommend performing large stack work in a subagent or separate branch when practical so the active thread context stays focused.
Commands
stack track
Resolve trunk, remote, current branch, and intended parent.
Write or repair stack.trunk and branch.<name>.stackParent.
Write strongly recommended remote metadata when known.
Verify the parent chain is not self-referential or cyclic.
stack log
Read stack metadata for all local branches.
Derive parent-child relationships from stackParent.
Resolve live PR state through gh.
Present stack order, parents, and PR status.
stack create
Capture the source branch as the intended parent.
Create the child branch from that source branch.
Generate a commit message from the staged diff.
Create the commit.
Record the source branch explicitly as the new branch's parent.
stack restack
Resolve the branch graph from parent metadata.
Find descendants of the selected branch in parent-to-child order.
Rebase each child onto its recorded parent.
Resolve conflicts automatically when the correct result is clear; otherwise stop and report the blocker.
stack move
Resolve the branch's current parent and intended new parent.
Update the branch's parent metadata.
Restack that branch onto the new parent.
Restack descendants in parent-to-child order.
stack squash
Resolve the current branch's parent.
Compute the full branch diff against that parent.
Rewrite the branch into a single commit on top of the parent.
Generate the new commit message from the squashed diff.
stack submit
Resolve each branch's parent branch and existing PR state through gh.
Ask whether PR title and description should be refreshed.
Generate or refresh PR content from the branch diff against the parent branch when requested.
Push each branch.
Create missing PRs with base = parent branch.
Update every existing PR base branch to the resolved parent branch so the full stack tracks the previous branch correctly.
Refresh PR title and body when requested.
stack retarget
Resolve the selected branch set in stack order, including each recorded parent.
Compare every existing GitHub PR base branch to its resolved parent branch.
Update any mismatched PR base branch so each PR targets the previous branch in the stack.
Report which PRs changed and which were already correct.
stack sync
Fetch the remote trunk.
Rebase the bottom branch onto trunk.
Restack the branches above it in parent-to-child order.
Resolve conflicts automatically when the correct result is clear; otherwise stop and report the blocker.
Content Generation
Generate commit messages from the staged diff or squashed branch diff, not from branch names or prior commit subjects.
Generate PR title and body from the branch diff against the parent branch.
If the branch has multiple commits, summarize the branch holistically instead of mirroring the commit list.
During stack submit, create missing PRs first, then explicitly update every submitted PR base branch to the resolved parent branch.
Before updating an existing PR during stack submit, ask whether the PR title and description should be refreshed; if yes, regenerate them from the current branch diff after base branches are corrected.
Output Expectations
Report the trunk branch, current branch, resolved parent, and whether parentage was explicit or inferred.
Report which branches were restacked, squashed, moved, pushed, or submitted.
Report which PR base branches were changed, skipped as already correct, or could not be updated.
Include PR URLs when created or updated.
Call out conflicts, blocked rebases, or metadata inconsistencies explicitly.
Weekly Installs
8
Repository
ouj/skills
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn