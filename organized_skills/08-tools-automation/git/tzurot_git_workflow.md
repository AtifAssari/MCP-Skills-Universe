---
rating: ⭐⭐⭐
title: tzurot-git-workflow
url: https://skills.sh/lbds137/tzurot/tzurot-git-workflow
---

# tzurot-git-workflow

skills/lbds137/tzurot/tzurot-git-workflow
tzurot-git-workflow
Installation
$ npx skills add https://github.com/lbds137/tzurot --skill tzurot-git-workflow
SKILL.md
Git Workflow Procedures

Invoke with /tzurot-git-workflow for step-by-step git operations.

Safety rules are in .claude/rules/00-critical.md - they apply automatically.

Commit Procedure
1. Stage Changes
git status                    # Review what's changed
git add <specific-files>      # Stage specific files (preferred)
# Or: git add -p              # Interactive staging

2. Create Commit
git commit -m "$(cat <<'EOF'
feat(scope): short description

Longer explanation of what and why.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"


Types: feat, fix, docs, refactor, test, chore, perf Scopes: ai-worker, api-gateway, bot-client, common-types, ci, deps

3. Push
pnpm test && git push -u origin <branch>

PR Procedure
Create PR
# 1. Ensure on feature branch, up-to-date with develop
git checkout develop && git pull origin develop
git checkout feat/your-feature
git rebase develop

# 2. Push and create PR
git push -u origin feat/your-feature
gh pr create --base develop --title "feat: description"

After PR Merged
git checkout develop
git pull origin develop
git branch -d feat/your-feature

Rebase Procedure
git checkout develop && git pull origin develop
git checkout feat/your-feature
git rebase develop

# If conflicts:
# 1. Edit files to resolve
# 2. git add <resolved>
# 3. git rebase --continue
# Repeat until done

git push --force-with-lease origin feat/your-feature

Release Procedure
1. Version Bump
# Option A: Changesets (recommended)
pnpm changeset
pnpm changeset:version
git add . && git commit -m "chore: version packages"

# Option B: Manual
pnpm bump-version 3.0.0-beta.XX
git commit -am "chore: bump version to 3.0.0-beta.XX"

2. Write Release Notes

Write release notes following the Conventional Changelog format defined in .claude/rules/05-tooling.md.

3. Create Release PR
gh pr create --base main --head develop --title "Release v3.0.0-beta.XX: Description"

4. Merge Release PR

⚠️ NEVER use --delete-branch for release PRs. develop is a long-lived branch.

# ✅ CORRECT - Merge without deleting develop
gh pr merge <number> --rebase

# ❌ FORBIDDEN - Would delete develop!
gh pr merge <number> --rebase --delete-branch

5. After Merge to Main
git fetch --all
git checkout main && git pull origin main
git checkout develop && git pull origin develop
git rebase origin/main
git push origin develop --force-with-lease

GitHub CLI (Use ops instead of broken gh pr edit)
pnpm ops gh:pr-info 478        # Get PR info
pnpm ops gh:pr-reviews 478     # Get reviews
pnpm ops gh:pr-comments 478    # Get line comments
pnpm ops gh:pr-edit 478 --title "New title"

References
GitHub CLI: docs/reference/GITHUB_CLI_REFERENCE.md
Safety rules: .claude/rules/00-critical.md
Weekly Installs
13
Repository
lbds137/tzurot
GitHub Stars
8
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass