---
rating: ⭐⭐
title: task-complete
url: https://skills.sh/xfiveco/skills/task-complete
---

# task-complete

skills/xfiveco/skills/task-complete
task-complete
Installation
$ npx skills add https://github.com/xfiveco/skills --skill task-complete
SKILL.md

First, check if the task.md file is present in the repository. If not, ask user what to do. You may proceed based on the context if requested.

Second, check if there are any uncommitted changes in the repository. If there are, offer to commit first. Do not continue with uncommitted changes. Do not commit with --no-verify flag unless user explicitly requests it.

Based on the task.md file and any information in your context prepare a title and description of the merge request/pull request.

Title should have the format ABC-123 Title and use Title Case.

Description should start with a link to task.md using git remote and a specific commit hash that contains task.md, then an empty line, then the rest of the description. Examples: task.md or task.md.

If task.md exists and is not yet committed on the branch:

Commit task.md snapshot first.
Create a second commit that removes task.md.
Use the snapshot commit hash for the description link.

Omit the task.md link only if task.md does not exist and was never part of this completed work.

Provide title in blocks like this:

... title ...

... description ...


If task.md file is present, create a commit that removes task.md file (as a separate commit after the task.md snapshot commit).

Offer user to push but do not do it without user's confirmation.

After pushing provide a link to the merge request/pull request or link to create one as markdown link. When providing a link to create a MR/PR, format it as below. Remember to escape parameters (use node).

Target branch (base) selection: pick the closest ancestor remote branch by git divergence (zero commits behind and the smallest commits ahead), falling back to the remote default branch only when no ancestor exists or asking the user when still ambiguous.

Create merge request

Create merge request

Weekly Installs
10
Repository
xfiveco/skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass