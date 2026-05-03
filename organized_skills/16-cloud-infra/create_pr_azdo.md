---
rating: ⭐⭐⭐
title: create-pr-azdo
url: https://skills.sh/oocx/tfplan2md/create-pr-azdo
---

# create-pr-azdo

skills/oocx/tfplan2md/create-pr-azdo
create-pr-azdo
Installation
$ npx skills add https://github.com/oocx/tfplan2md --skill create-pr-azdo
SKILL.md
Create PR (Azure DevOps)
Purpose

Create an Azure DevOps pull request in a consistent way, while still encoding the repository’s preference for a linear history.

This skill prefers using the repo wrapper script scripts/pr-azdo.sh to minimize Maintainer approval interruptions (single terminal invocation).

Notes on Merge Policy

CONTRIBUTING.md specifies Rebase and merge as the required merge strategy for this repo.

Azure DevOps UI/merge options differ by project settings. When merging an Azure DevOps PR, choose the most “rebase/linear-history” option available (often called Rebase and fast-forward) when available; otherwise, ask the Maintainer what to use.

Hard Rules
Must
Work on a non-main branch.
Ensure the working tree is clean before creating a PR.
Push the branch before creating the PR.
Keep PR title and description conventional and review-friendly.
Before creating the PR, post the exact Title and Description in chat.
Use the standard description template (Problem / Change / Verification).
Must Not
Merge using a strategy that introduces merge commits unless the Maintainer explicitly requests it.
Actions
0. Title + Description (Required)

Before running any PR creation command, provide in chat:

PR title (exact)
PR description (exact), using this template:
## Problem
<why is this change needed?>

## Change
<what changed?>

## Verification
<how was it validated?>

Recommended: One-Command Wrapper
scripts/pr-azdo.sh create --title "<type(scope): summary>" --description "<why + what + testing notes>"


Abandon a test PR (cleanup):

scripts/pr-azdo.sh abandon --id <pr-id>

1. Pre-flight Checks
git branch --show-current
scripts/git-status.sh --short

2. Push the Branch
git push -u origin HEAD

3. Create the PR

This is a minimal example; set --organization/--project appropriately for the target repo.

az repos pr create \
  --title "<type(scope): summary>" \
  --description "<why + what + testing notes>" \
  --source-branch "$(git branch --show-current)" \
  --target-branch main

4. Merging
If you need to merge the PR, confirm the exact merge option with the Maintainer first.
Prefer a rebase/linear-history option when available.
Weekly Installs
17
Repository
oocx/tfplan2md
GitHub Stars
163
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass