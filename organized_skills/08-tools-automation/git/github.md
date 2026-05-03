---
rating: ⭐⭐⭐
title: github
url: https://skills.sh/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations/github
---

# github

skills/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations/github
github
Installation
$ npx skills add https://github.com/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill github
SKILL.md
GitHub CLI Skill

Use the gh CLI to interact with GitHub repositories and services.

Authentication

Check auth status:

gh auth status


Login:

gh auth login


Refresh token:

gh auth refresh

Repositories

Clone repository:

gh repo clone owner/repo


Create new repo:

gh repo create my-repo --public --source=. --push


Fork repository:

gh repo fork owner/repo --clone


View repo in browser:

gh repo view --web


List your repos:

gh repo list

Issues

List issues:

gh issue list


Create issue:

gh issue create --title "Bug: Login fails" --body "Description here"


Create issue interactively:

gh issue create


View issue:

gh issue view 123


Close issue:

gh issue close 123


Reopen issue:

gh issue reopen 123


Comment on issue:

gh issue comment 123 --body "Working on this"


Assign issue:

gh issue edit 123 --add-assignee @me


Add labels:

gh issue edit 123 --add-label "bug,priority:high"

Pull Requests

List PRs:

gh pr list


Create PR:

gh pr create --title "Add feature" --body "Description"


Create PR from current branch:

gh pr create --fill


View PR:

gh pr view 45


View PR in browser:

gh pr view 45 --web


Checkout PR locally:

gh pr checkout 45


Review PR:

gh pr review 45 --approve
gh pr review 45 --request-changes --body "Please fix X"
gh pr review 45 --comment --body "Looks good but..."


Merge PR:

gh pr merge 45 --squash
gh pr merge 45 --merge
gh pr merge 45 --rebase


Close PR:

gh pr close 45


List PR checks:

gh pr checks 45


View PR diff:

gh pr diff 45

Actions (CI/CD)

List workflow runs:

gh run list


View run details:

gh run view 12345


Watch run in progress:

gh run watch 12345


View run logs:

gh run view 12345 --log


Rerun failed jobs:

gh run rerun 12345 --failed


List workflows:

gh workflow list


Run workflow manually:

gh workflow run deploy.yml


Run with inputs:

gh workflow run deploy.yml -f environment=production


Disable/enable workflow:

gh workflow disable deploy.yml
gh workflow enable deploy.yml

Releases

List releases:

gh release list


Create release:

gh release create v1.0.0 --title "Version 1.0" --notes "Release notes"


Create from tag:

gh release create v1.0.0 --generate-notes


Upload assets:

gh release upload v1.0.0 ./dist/app.zip


Download assets:

gh release download v1.0.0


Delete release:

gh release delete v1.0.0

Gists

Create gist:

gh gist create file.txt --public


Create from stdin:

echo "Hello" | gh gist create -


List gists:

gh gist list


View gist:

gh gist view GIST_ID


Edit gist:

gh gist edit GIST_ID

Search

Search repos:

gh search repos "react hooks" --limit 10


Search issues:

gh search issues "bug authentication" --repo owner/repo


Search PRs:

gh search prs "fix memory leak" --state open


Search code:

gh search code "function handleAuth" --repo owner/repo

API

Make API request:

gh api repos/owner/repo


POST request:

gh api repos/owner/repo/issues -f title="New issue" -f body="Description"


GraphQL query:

gh api graphql -f query='{ viewer { login } }'


Paginate results:

gh api repos/owner/repo/issues --paginate

Labels

List labels:

gh label list


Create label:

gh label create "priority:high" --color FF0000 --description "High priority"

Projects

List projects:

gh project list


View project:

gh project view 1

SSH Keys

List SSH keys:

gh ssh-key list


Add SSH key:

gh ssh-key add ~/.ssh/id_ed25519.pub --title "My laptop"

GPG Keys

List GPG keys:

gh gpg-key list


Add GPG key:

gh gpg-key add key.gpg

Secrets (for Actions)

List secrets:

gh secret list


Set secret:

gh secret set MY_SECRET


Set from file:

gh secret set MY_SECRET < secret.txt


Delete secret:

gh secret delete MY_SECRET

Variables (for Actions)

List variables:

gh variable list


Set variable:

gh variable set MY_VAR --body "value"

Extensions

List installed extensions:

gh extension list


Install extension:

gh extension install owner/gh-extension


Browse extensions:

gh extension browse

Aliases

Create alias:

gh alias set pv 'pr view'


List aliases:

gh alias list

Configuration

View config:

gh config list


Set default editor:

gh config set editor vim


Set default browser:

gh config set browser "open"

Common Workflows
Quick PR workflow:
# Create branch, commit, push, create PR
git checkout -b feature/my-feature
# ... make changes ...
git add . && git commit -m "Add feature"
git push -u origin feature/my-feature
gh pr create --fill

Review and merge:
gh pr checkout 45
# ... review code ...
gh pr review --approve
gh pr merge --squash --delete-branch

Check CI status:
gh pr checks
gh run watch

Weekly Installs
82
Repository
dicklesworthsto…grations
GitHub Stars
63
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn