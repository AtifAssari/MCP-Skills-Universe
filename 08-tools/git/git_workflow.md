---
title: git-workflow
url: https://skills.sh/youngger9765/career_ios_backend/git-workflow
---

# git-workflow

skills/youngger9765/career_ios_backend/git-workflow
git-workflow
Installation
$ npx skills add https://github.com/youngger9765/career_ios_backend --skill git-workflow
SKILL.md
Git Workflow Skill
Purpose

Enforce git best practices, pre-commit hooks, and mandatory documentation updates for the career_ios_backend project.

Automatic Activation

This skill is AUTOMATICALLY activated when user mentions:

✅ "git commit"
✅ "git push"
✅ "ready to commit/push"
✅ "提交代碼"
✅ "推送到遠端"
Git Hooks Setup
First-Time Installation
# Install pre-commit and pre-push hooks
poetry run pre-commit install
poetry run pre-commit install --hook-type pre-push

Pre-Commit Checks (Fast ~5 seconds)

When you run git commit, these checks run automatically:

✅ Branch Check - Prevents commits to main/master
✅ Ruff Linting & Formatting - Auto-fixes code style
✅ File Checks - Trailing whitespace, YAML/TOML syntax
✅ Security Checks - Prevents leaking:
API keys
Secrets
Private keys
Credentials
Pre-Push Checks (Smoke Tests ~10 seconds)

When you run git push, these tests run automatically:

✅ Critical Console API Smoke Tests
Login functionality
Client management core features
Case/Session core features
Full test suite (106+ tests) runs in CI
Commit Workflow
Step-by-Step Process
# 1. Check current branch
git branch --show-current
# ⚠️ MUST NOT be on main/master

# 2. Stage changes
git add .

# 3. Commit (triggers pre-commit hooks ~5s)
git commit -m "feat: add XXX API"
# ↓ Auto-executes:
#   ✅ Branch check
#   ✅ Ruff linting/formatting
#   ✅ Security checks
#   ✅ File checks

# 4. Push (triggers smoke tests ~10s)
git push
# ↓ Auto-executes:
#   ✅ Critical Console API smoke tests
#   ✅ Full tests run in CI (106+ tests)

Commit Message Format

Follow conventional commits:

✅ Good Examples:

feat: add user login API
fix: correct client code generation
docs: update API guide
test: add session API tests
refactor: extract session service

❌ Bad Examples:

update code (too vague)
fixes (no description)
feat: add user login API 🤖 Generated with Claude Code (no Claude signature!)
Manual Hook Execution (Optional)
# Run all pre-commit checks manually
poetry run pre-commit run --all-files

# Run pre-push smoke tests manually
poetry run pre-commit run --hook-stage push

# Run full integration test suite manually (106+ tests)
poetry run pytest tests/integration/ -v

🚨 ABSOLUTELY FORBIDDEN
NEVER Use --no-verify
# ❌ NEVER DO THIS:
git commit --no-verify
git push --no-verify

# These bypass security checks and will:
# - Allow commits to main/master
# - Skip security scans (leak secrets)
# - Skip tests (break production)
# - Violate project standards


Why it's forbidden:

Bypasses security checks → Risk of leaking credentials
Skips tests → Risk of breaking production
Violates TDD → Degrades code quality
Breaks CI/CD pipeline → Deployment failures
If Hooks Fail

DO NOT skip checks with --no-verify!

INSTEAD:

Read the error message
Fix the actual problem
Re-run the commit/push

Common failures and solutions:

# Failure: "Detected secrets in code"
Solution: Remove the secret, use environment variables

# Failure: "Ruff check failed"
Solution: Run `ruff check --fix app/` to auto-fix

# Failure: "Tests failed"
Solution: Fix the broken tests, don't skip them

# Failure: "On main branch"
Solution: Create/switch to feature branch

📚 MANDATORY Documentation Updates

CRITICAL: Before EVERY git push, you MUST update documentation.

Required Updates
# 1. Update PRD.md
- Version number (if releasing)
- New features added
- Current status

# 2. Update CHANGELOG.md
- Add changes to [Unreleased] section
- Follow Keep a Changelog format

# 3. Update CHANGELOG_zh-TW.md
- Sync with English CHANGELOG.md
- Maintain same structure

# 4. Weekly Report (if new week)
- Update progress report
- Document blockers/achievements

Enforcement
# Agent will CHECK before allowing push:
git push
  ↓
Agent checks:
  ❌ PRD.md not updated → BLOCK PUSH
  ❌ CHANGELOG.md [Unreleased] empty → BLOCK PUSH
  ❌ CHANGELOG_zh-TW.md out of sync → BLOCK PUSH
  ✅ All docs updated → ALLOW PUSH


NO EXCEPTIONS: Even small changes require documentation updates.

Branch Strategy
Current Branch Structure
main/master (protected)
  ↓
staging (main development)
  ↓
feature/xxx (your work)
  ↓
parents_rag_refine (current)

Branch Rules

NEVER commit directly to main/master

Pre-commit hook will BLOCK
Always use staging or feature branches

Create feature branches from staging

git checkout staging
git pull
git checkout -b feature/new-feature-name


Merge back to staging when complete

# After tests pass and code reviewed
git checkout staging
git merge feature/new-feature-name
git push

Common Git Operations
Starting New Work
# 1. Update staging
git checkout staging
git pull

# 2. Create feature branch
git checkout -b feature/add-client-search

# 3. Work on feature
# ... make changes ...

# 4. Commit regularly
git add .
git commit -m "feat: add client search endpoint"

# 5. Push to remote
git push -u origin feature/add-client-search

Reviewing Before Push
# Check what will be committed
git status

# Review changes
git diff

# Review staged changes
git diff --staged

# Check recent commits
git log --oneline -5

Fixing Mistakes
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) ⚠️ DESTRUCTIVE
git reset --hard HEAD~1

# Amend last commit message
git commit --amend -m "new message"

# Unstage file
git restore --staged <file>

Integration with TDD Workflow

Git workflow integrates with TDD:

TDD Cycle:
  1. RED: Write failing test
  2. GREEN: Implement minimal code
  3. REFACTOR: Improve quality
     ↓
  4. GIT COMMIT ← You are here
     - Pre-commit hooks run
     - Security checks pass
     - Code formatted
     ↓
  5. GIT PUSH
     - Smoke tests run
     - Documentation verified
     - CI/CD triggered

Quality Gates Checklist
Before Commit
 All integration tests pass locally
 Code follows project patterns
 No hardcoded credentials
 Commit message follows format
 On correct branch (not main/master)
Before Push
 Documentation updated (PRD, CHANGELOG)
 All commits have good messages
 No sensitive data in commits
 Ready for code review
 CI/CD pipeline will pass
Troubleshooting
"Hook script not found"
# Reinstall hooks
poetry run pre-commit install
poetry run pre-commit install --hook-type pre-push

"Permission denied" on hooks
# Fix permissions
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-push

"Pre-commit hook takes too long"

This is normal:

Pre-commit: ~5 seconds (formatting, security)
Pre-push: ~10 seconds (smoke tests)
Full CI: ~2 minutes (all 106+ tests)
"I need to force push"

⚠️ Be careful with force push:

# Safe force push (recommended)
git push --force-with-lease

# Unsafe force push (avoid)
git push --force  # ⚠️ Can lose others' work


Never force push to main/master - will be rejected by remote.

Success Metrics
✅ Zero commits to main/master branch
✅ 100% commits pass pre-commit hooks
✅ All pushes have updated documentation
✅ No use of --no-verify flag
✅ All commits follow message format
Related Skills
tdd-workflow - For test-first development
quality-standards - For code quality requirements
api-development - For API development patterns

Skill Version: v1.0 Last Updated: 2025-12-25 Project: career_ios_backend (Prototype Phase)

Weekly Installs
9
Repository
youngger9765/ca…_backend
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass