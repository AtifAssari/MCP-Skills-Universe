---
title: git-workflow
url: https://skills.sh/jezweb/claude-skills/git-workflow
---

# git-workflow

skills/jezweb/claude-skills/git-workflow
git-workflow
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill git-workflow
SKILL.md
Git Workflow

Guided workflows for common git operations that benefit from structured steps.

PR Preparation

When preparing a pull request:

Gather context

git log main..HEAD --oneline — list all commits on the branch
git diff main...HEAD --stat — see all changed files
git status — check for uncommitted work

Draft PR content

Title: under 70 chars, describes the change (not the branch name)
Body: summarise the "why", list key changes, add test plan
Use the commit history to write the summary — don't rely on memory

Push and create

git push -u origin HEAD
gh pr create --title "..." --body "$(cat <<'EOF'
## Summary
- ...

## Test plan
- [ ] ...

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"


Verify — gh pr view --web to open in browser

Branch Cleanup

Clean up merged branches safely:

Switch to main and pull latest

git checkout main && git pull


List merged branches (excludes main/master/develop)

git branch --merged main | grep -vE '^\*|main|master|develop'


Delete local merged branches

git branch --merged main | grep -vE '^\*|main|master|develop' | xargs -r git branch -d


Prune remote tracking refs

git fetch --prune


List remote branches with no local tracking (optional)

git branch -r --merged origin/main | grep -vE 'main|master|develop|HEAD'

Merge Conflict Resolution

When a PR has conflicts:

Assess the conflict scope

git fetch origin
git merge origin/main --no-commit --no-ff
git diff --name-only --diff-filter=U  # List conflicted files


For each conflicted file, read the file and resolve:

Keep both changes if they're in different areas
If architecturally incompatible, prefer the main branch's approach and re-apply the PR's intent on top

If rebase is cleaner (few commits, no shared history):

git rebase origin/main
# Resolve conflicts per commit, then:
git rebase --continue


If rebase is messy (many conflicts, architectural divergence):

Abort: git rebase --abort or git merge --abort
Extract useful code: git show origin/branch:path/to/file > /tmp/extracted.txt
Apply changes manually to main
Close original PR with explanation

Verify — run tests, check the diff looks right

Monorepo Release Tags

In monorepos, scope tags to the package:

# ❌ Ambiguous in monorepos
git tag v2.1.0

# ✅ Scoped to package
git tag contextbricks-v2.1.0
git push origin contextbricks-v2.1.0


Pattern: {package-name}-v{semver}

.gitignore-First Init

When creating a new repo, always create .gitignore BEFORE the first git add:

cat > .gitignore << 'EOF'
node_modules/
.wrangler/
dist/
.dev.vars
*.log
.DS_Store
.env
.env.local
EOF

git init && git add . && git commit -m "Initial commit"


If node_modules is already tracked:

git rm -r --cached node_modules/
git commit -m "Remove node_modules from tracking"

Private Repo License Audit

Before publishing or sharing a private repo:

gh repo view --json visibility -q '.visibility'


If PRIVATE, ensure:

LICENSE contains proprietary notice (not MIT/Apache)
package.json has "license": "UNLICENSED" and "private": true
No CONTRIBUTING.md or "contributions welcome" in README
Weekly Installs
600
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass