---
rating: ⭐⭐⭐
title: address-github-issue
url: https://skills.sh/morphet81/cheat-sheets/address-github-issue
---

# address-github-issue

skills/morphet81/cheat-sheets/address-github-issue
address-github-issue
Installation
$ npx skills add https://github.com/morphet81/cheat-sheets --skill address-github-issue
SKILL.md

Retrieve a GitHub issue and coordinate a team to address it.

Usage:

/address-github-issue 42 — Address issue #42 in the current repo
/address-github-issue owner/repo#42 — Address issue #42 in a specific repo
/address-github-issue https://github.com/owner/repo/issues/42 — Address issue by URL

Instructions:

Validate the gh CLI is available:

Run gh --version to confirm it is installed
If not found, stop and display:
❌ GitHub CLI (`gh`) is not installed.
Install it with: brew install gh
Then authenticate with: gh auth login

Run gh auth status to confirm authentication
If not authenticated, stop and display:
❌ GitHub CLI is not authenticated.
Run: gh auth login


Parse the issue reference from $ARGUMENTS:

If $ARGUMENTS is empty, use AskUserQuestion to ask for the issue reference and STOP until provided.
Accepted formats:
A bare number (e.g., 42) → use the current repo
owner/repo#42 → explicit repo and number
A full GitHub URL (e.g., https://github.com/owner/repo/issues/42) → parse repo and number from it
For bare numbers, determine the current repo with gh repo view --json nameWithOwner -q .nameWithOwner. If this fails (not in a GitHub repo), stop:
❌ Could not determine the GitHub repository.
Run this skill from inside a GitHub repo, or provide a full issue reference (e.g., owner/repo#42).


Fetch the issue:

Run:
gh issue view <number> --repo <owner/repo> --json number,title,body,labels,assignees,milestone,state,comments,url

If the issue is not found or access is denied, stop with the error message from gh.
Parse the JSON output to extract:
title, body, labels, state, url
comments array (each has author.login and body)

Analyze the issue:

Read the title, body, and all comments thoroughly.
Identify the issue type:
Bug — something is broken; labels like bug, defect, regression
Feature — new capability; labels like enhancement, feature request
Chore / Maintenance — tech debt, refactor, CI, docs; labels like chore, docs, refactor
Question / Investigation — needs research before coding
Identify the scope and complexity:
Simple (1 developer) — isolated fix or small addition, touches ≤2 files, no API or schema changes
Medium (2 developers) — moderate feature or bug with multiple moving parts; may touch frontend and backend separately
Complex (3 developers) — large feature, architectural change, cross-cutting concern, or multiple independent workstreams
Note any ambiguities or missing information that the PM should clarify in requirements.

Determine team composition:

Always spawn exactly 1 PM.
Spawn 1, 2, or 3 developers based on the complexity assessment above.
No designers or testers are spawned by this skill (developers are expected to include tests in their implementation).

Create the team:

Use TeamCreate with a short kebab-case name derived from the issue title or number (e.g., issue-42, fix-login-crash, add-dark-mode).
Use TaskCreate to create one task per role before spawning agents:
PM task: "Write requirements and acceptance criteria for issue #"
One developer task per developer: "Implement for issue #"

Spawn the PM (subagent_type: general-purpose):

Provide:
The full issue content (title, body, all comments, URL)
The issue type and complexity assessment
The team name
The PM's job:
Read the issue thoroughly, including all comments
Write detailed requirements and acceptance criteria to address the issue, resolving any ambiguities using the comments and their knowledge of the codebase
Structure the requirements as:
## Issue #<number>: <title>
**Type:** <Bug / Feature / Chore> | **URL:** <url>

## Context
<Brief summary of the issue and why it matters>

## Requirements
<Numbered list of concrete, testable requirements>

## Acceptance Criteria
<Checklist of conditions that must be true when the issue is resolved>

## Developer Workstreams
<If multiple developers: describe each workstream clearly with its scope and any shared interfaces or contracts they need to agree on>

## Out of Scope
<Anything explicitly excluded from this issue>

Check for a project lore file (LORE.md, docs/lore.md, .agent/lore.md, or similar) and update it with any relevant context this issue introduces
Mark their task as completed via TaskUpdate
Message the team lead when done

Wait for the PM to finish and retrieve the requirements from the completed task or PM message.

Spawn developers (subagent_type: general-purpose) in parallel, one per workstream:

Provide each developer with:
The original issue content (title, body, comments, URL)
The PM's requirements document
Their specific workstream scope (if multiple developers)
The issue type for context (bug fix → write a regression test; feature → write unit/integration tests; etc.)
Each developer's job:
Explore the relevant parts of the codebase
Implement the changes required by their workstream
Write tests covering their changes (unit tests at minimum; integration tests if applicable)
Mark their task as completed via TaskUpdate
Message the team lead when done

Wait for all developers to finish.

Verify no conflicts:

If multiple developers were spawned, check whether any two agents modified the same files
If conflicts exist, resolve them by reading both sets of changes and merging intelligently
Run a quick sanity check: ensure the codebase compiles and lints cleanly after all changes are applied (use the project's existing lint/build scripts if available)

Present a final summary to the user:

## Issue #<number> Addressed

**Issue:** <title>
**URL:** <url>

### What was done
- <Bullet summary of changes made>

### Tests added
- <List of test files added or updated>

### Developers
- <Developer 1>: <what they implemented>
- <Developer 2>: <what they implemented> (if applicable)

### Recommended next steps
- Review the changes with `/review-changes`
- Create a PR with `/create-pr`
- Link the PR to the issue on GitHub: `gh issue develop <number> --repo <owner/repo>`


Shut down the team gracefully:

Send a shutdown_request to each teammate via SendMessage
Once all have confirmed, call TeamDelete
Weekly Installs
65
Repository
morphet81/cheat-sheets
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn