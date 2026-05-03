---
rating: ⭐⭐⭐
title: github-release
url: https://skills.sh/jezweb/claude-skills/github-release
---

# github-release

skills/jezweb/claude-skills/github-release
github-release
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill github-release
Summary

Sanitize code for secrets and artifacts, then create and publish GitHub releases with version tags.

Two-phase workflow: Phase 1 runs blocking checks (secrets scan with gitleaks, LICENSE/README validation, personal artifact removal) and stops on failures; Phase 2 creates version tags and publishes via gh CLI
Requires gh CLI authenticated, gitleaks installed, and a Git repository with a remote configured
Includes non-blocking checks for build success and dependency vulnerabilities, plus automatic sanitization commits if changes are made
Displays commit history between the last tag and HEAD before release, and reports the release URL and next steps upon completion
SKILL.md
GitHub Release

Sanitize and release projects to GitHub. Two-phase workflow: safety checks first, then tag and publish.

Prerequisites
gh CLI installed and authenticated (gh auth status)
gitleaks installed for secrets scanning (brew install gitleaks or download from GitHub)
Git repository with a remote configured
Workflow
Phase 1: Sanitize

Run these checks before any public release. Stop on blockers.

1. Scan for Secrets (BLOCKER)
gitleaks detect --no-git --source=. --verbose


If secrets found: STOP. Remove secrets, move to environment variables. Check git history with git log -S "secret_value" — if in history, use BFG Repo-Cleaner.

If gitleaks not installed, do manual checks:

# Check for .env files
find . -name ".env*" -not -path "*/node_modules/*"

# Check config files for hardcoded secrets
grep -ri "api_key\|token\|secret\|password" wrangler.toml wrangler.jsonc .dev.vars 2>/dev/null

2. Remove Personal Artifacts

Check for and remove session/planning files that shouldn't be published:

SESSION.md — session state
planning/, screenshots/ — working directories
test-*.ts, test-*.js — local test files

Either delete them or add to .gitignore.

3. Validate LICENSE
ls LICENSE LICENSE.md LICENSE.txt 2>/dev/null


If missing: create one. Check the repo visibility (gh repo view --json visibility -q '.visibility'). Use MIT for public repos. For private repos, consider a proprietary license instead.

4. Validate README

Check README exists and has basic sections:

grep -i "## Install\|## Usage\|## License" README.md


If missing sections, add them before release.

5. Check .gitignore

Verify essential patterns are present:

grep -E "node_modules|\.env|dist/|\.dev\.vars" .gitignore

6. Build Test (non-blocking)
npm run build 2>&1

7. Dependency Audit (non-blocking)
npm audit --audit-level=high

8. Create Sanitization Commit

If any changes were made during sanitization:

git add -A
git commit -m "chore: prepare for release"

Phase 2: Release
1. Determine Version

Check package.json for current version, or ask the user. Ensure version starts with v prefix.

2. Check Tag Doesn't Exist
git tag -l "v[version]"


If it exists, ask user whether to delete and recreate or use a different version.

3. Show What's Being Released
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")
if [ -z "$LAST_TAG" ]; then
  git log --oneline --no-merges HEAD | head -20
else
  git log --oneline --no-merges ${LAST_TAG}..HEAD
fi

4. Create Tag and Push
git tag -a v[version] -m "Release v[version]"
git push origin $(git branch --show-current)
git push origin --tags

5. Create GitHub Release
gh release create v[version] \
  --title "Release v[version]" \
  --notes "[auto-generated from commits]"


For pre-releases add --prerelease. For drafts add --draft.

6. Report

Show the user:

Release URL
Next steps (npm publish if applicable, announcements)
Reference Files
When	Read
Detailed safety checks	references/safety-checklist.md
Release mechanics	references/release-workflow.md
Weekly Installs
722
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass