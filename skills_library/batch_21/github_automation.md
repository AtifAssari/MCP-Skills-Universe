---
title: github-automation
url: https://skills.sh/vm0-ai/vm0-skills/github-automation
---

# github-automation

skills/vm0-ai/vm0-skills/github-automation
github-automation
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill github-automation
SKILL.md
Capabilities
Repositories: Create, clone, fork, view, and manage repos
Issues: Create, list, view, close, comment, and label issues
Pull Requests: Create, review, merge, list, and comment on PRs
Releases: Create releases and manage tags
Workflows: View and manage GitHub Actions
Gists: Create and manage gists
Search: Search repos, issues, PRs, code, and users
Authentication

Verify with:

gh auth status

Instructions
Phase 1: Understand the Request
Clarify what GitHub operation the user needs
Identify the target repository (if not specified, ask)
Confirm any destructive operations before executing
Phase 2: Execute the Operation

Use gh CLI commands. Common patterns:

Repository Operations

gh repo view <owner>/<repo>
gh repo clone <owner>/<repo>
gh repo create <name> --public/--private
gh repo list <owner>


Issue Operations

gh issue list --repo <owner>/<repo>
gh issue create --repo <owner>/<repo> --title "Title" --body "Body"
gh issue view <number> --repo <owner>/<repo>
gh issue close <number> --repo <owner>/<repo>
gh issue comment <number> --repo <owner>/<repo> --body "Comment"


Pull Request Operations

gh pr list --repo <owner>/<repo>
gh pr create --repo <owner>/<repo> --title "Title" --body "Body"
gh pr view <number> --repo <owner>/<repo>
gh pr merge <number> --repo <owner>/<repo>
gh pr review <number> --repo <owner>/<repo> --approve/--comment/--request-changes
gh pr checks <number> --repo <owner>/<repo>


Search Operations

gh search repos <query>
gh search issues <query>
gh search prs <query>
gh search code <query>


GitHub Actions

gh run list --repo <owner>/<repo>
gh run view <run-id> --repo <owner>/<repo>
gh workflow list --repo <owner>/<repo>


Releases

gh release list --repo <owner>/<repo>
gh release create <tag> --repo <owner>/<repo> --title "Title" --notes "Notes"

Guidelines
Always specify --repo <owner>/<repo> when not in a cloned repository
For destructive operations (delete, close, merge), confirm with user first
Use --json flag when you need to parse output programmatically
Handle errors gracefully and suggest fixes
When creating issues/PRs, use clear titles and descriptive bodies
Phase 3: Report Results
Summarize what was done
Provide relevant links (PR URLs, issue numbers, etc.)
Suggest next steps if applicable
Output Format

When listing items, format clearly:

#123 - Issue title (open/closed) - @author
#456 - PR title (open/merged/closed) - @author


When creating items, always report:

The created item's number/ID
Direct URL to the item
Any relevant status information
Examples

Create an issue:

gh issue create --repo <owner>/<repo> --title "Bug: Login fails" --body "Steps to reproduce..."


List open PRs awaiting review:

gh pr list --repo <owner>/<repo> --state open --search "review:required"


Get PR details as JSON:

gh pr view <number> --repo <owner>/<repo> --json title,state,reviews,checks

Weekly Installs
75
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn