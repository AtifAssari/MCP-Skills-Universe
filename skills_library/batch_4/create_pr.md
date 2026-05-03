---
title: create-pr
url: https://skills.sh/charon-fan/agent-playbook/create-pr
---

# create-pr

skills/charon-fan/agent-playbook/create-pr
create-pr
Installation
$ npx skills add https://github.com/charon-fan/agent-playbook --skill create-pr
SKILL.md
Create PR

A skill for creating pull requests with automatic bilingual documentation updates. This skill ensures that both English and Chinese documentation stay in sync when code changes are submitted.

When This Skill Activates

This skill activates when you:

Ask to create a pull request or PR
Say "submit my changes" or "push and create PR"
Mention "make a PR" or "open a pull request"
Want to submit code for review
PR Creation Workflow
Step 1: Analyze Changes

Examine all changes in the current branch:

git status
git diff
git log --oneline main..HEAD


Identify:

Modified files: What was changed?
New files: What was added?
Deleted files: What was removed?
Impact area: Which skills or features are affected?
Step 2: Determine Documentation Updates
Check for Skill Changes

First, detect if any skills were changed:

# Check if skills/ directory has changes
git diff --name-only main..HEAD | grep "^skills/"

Decision Matrix
Change Type	Documentation Action
New skill added	Add to skills table in both EN and CN README
Skill description changed	Update description in skills table
Skill removed	Remove from skills table
Skill hooks changed	Update Auto-Trigger column in skills table
Internal skill logic only	Skip README update
Bug fix with no user impact	Skip README update
Auto-Trigger Changes Require Update

If a skill's metadata.hooks front matter was modified, the Auto-Trigger column in the Skills Catalog must be updated:

# Check if hooks were modified
git diff main..HEAD -- skills/*/SKILL.md | grep -E "^\+.*metadata:|^\+.*hooks:|^\+.*trigger:"


If hooks changed → Update README.md and README.zh-CN.md Auto-Trigger column.

Step 3: Draft Commit Message

Use the commit-helper format:

<type>(<scope>): <subject>

<body>

<footer>


Types:

feat: New skill or feature
fix: Bug fix or correction
docs: Documentation only changes
refactor: Code refactoring
chore: Maintenance tasks
Step 4: Create the Pull Request

Run the following sequence:

# 1. Stage and commit changes
git add .
git commit -m "commit message"

# 2. Push to remote
git push -u origin <branch-name>

# 3: Create PR using gh CLI
gh pr create \
  --title "PR title" \
  --body "PR description"

Step 5: Update Documentation (If Required)

After creating the PR, update both README files:

README.md (English):

Add new skills to appropriate category table
Update project structure if needed
Keep language switch link at top

README.zh-CN.md (Chinese):

Mirror all English changes
Translate skill descriptions
Maintain same structure and formatting
Step 6: Update Changelog (Optional)

For significant changes, add to CHANGELOG.md:

## [Version] - YYYY-MM-DD

### Added
- New skill: skill-name

### Fixed
- Fixed issue in skill-name

### Changed
- Updated skill-name with new features

Documentation Update Guidelines
Skills Catalog Update Template

When adding or modifying skills, use this format for the Skills Catalog:

English (README.md):

### Category Name

| Skill | Description | Auto-Trigger |
|-------|-------------|--------------|
| **[skill-name](./skills/skill-name/)** | Brief description | Manual / Auto / Background / (keyword: "...") |


Chinese (README.zh-CN.md):

### 类别名称

| 技能 | 描述 | 自动触发 |
|------|------|----------|
| **[skill-name](./skills/skill-name/)** | 简短描述 | 手动 / 自动 / 后台 / (关键词："...") |

Auto-Trigger Column Values
Value	Meaning	Example
Manual	User must invoke	Most development skills
Auto	Triggers automatically after any skill	session-logger
Background	Runs non-blocking after related skill	self-improving-agent
After skill updates	Only triggers when skills are modified	create-pr
(keyword: "...")	Activates on specific keyword	prd-planner (keyword: "PRD")
When to Update README

Always update when:

Adding a new skill
Removing a skill
Changing skill names or descriptions
Restructuring the skills directory

Consider updating when:

Adding significant features to existing skills
Changing installation instructions
Modifying project structure

Skip updating when:

Internal code refactoring with no user impact
Minor typo fixes
Test file changes
Bilingual Update Format

When adding a new skill to the skills table:

English (README.md):

| **[skill-name](./skills/skill-name/)** | Brief skill description |


Chinese (README.zh-CN.md):

| **[skill-name](./skills/skill-name/)** | 技能简短描述 |

Language Switch Link

Both README files must have the language switch at the top:

README.md:

English | [简体中文](./README.zh-CN.md)


README.zh-CN.md:

[English](./README.md) | 简体中文

PR Description Template

When creating a PR, use this template:

## Summary

<Brief description of what this PR does>

## Changes

- [ ] New skill added
- [ ] Existing skill modified
- [ ] Documentation updated
- [ ] Tests added/updated

## Skills Affected

- `skill-name`: Description of change

## Documentation

- [x] README.md updated
- [x] README.zh-CN.md updated
- [ ] CHANGELOG.md updated (if applicable)

## Test Plan

- [ ] Skill tested in Claude Code
- [ ] Documentation links verified
- [ ] Bilingual translations checked

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Common Scenarios
Scenario 1: Adding a New Skill
# 1. Create skill files
mkdir -p skills/new-skill
touch skills/new-skill/SKILL.md
touch skills/new-skill/README.md

# 2. Create symlink
ln -s ~/path/to/agent-playbook/skills/new-skill/SKILL.md ~/.claude/skills/new-skill.md

# 3. Update README.md (add to skills table)
# 4. Update README.zh-CN.md (add to skills table with translation)

# 5. Commit and push
git add skills/new-skill/ README.md README.zh-CN.md
git commit -m "feat: add new-skill for ..."
git push -u origin feature/add-new-skill

# 6. Create PR
gh pr create --title "feat: add new-skill" --body "..."

Scenario 2: Modifying an Existing Skill
# 1. Make changes to skill
vim skills/existing-skill/SKILL.md

# 2. Check if description changed
git diff skills/existing-skill/SKILL.md

# 3. If description changed, update README files
# 4. Commit, push, create PR

Scenario 3: Bug Fix Only
# 1. Fix the bug
vim skills/some-skill/SKILL.md

# 2. Commit and push (no README update needed)
git add skills/some-skill/SKILL.md
git commit -m "fix: correct typo in some-skill"
git push

# 3. Create PR
gh pr create --title "fix: correct typo in some-skill"

Verification Checklist

Before creating the PR, verify:

 All changes are committed
 Branch is pushed to remote
 Commit messages follow Conventional Commits
 README.md is updated if needed
 README.zh-CN.md is updated if needed
 Language switch links are present in both READMEs
 New skills have symlinks created
 PR title is clear and descriptive
 PR description includes summary and changes
Quick Reference
Command	Purpose
git status	Check current state
git diff	See unstaged changes
git log main..HEAD	See branch commits
git add .	Stage all changes
git commit -m "msg"	Commit with message
git push -u origin branch	Push to remote
gh pr create	Create pull request
Tips
Commit first, PR later: Always commit changes before creating PR
Small PRs: Keep PRs focused on a single change
Clear titles: Use Conventional Commits in PR titles
Bilingual sync: Always update both README files together
Test skills: Verify skills work before submitting PR
Weekly Installs
413
Repository
charon-fan/agen…playbook
GitHub Stars
49
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass