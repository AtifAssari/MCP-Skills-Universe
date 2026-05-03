---
rating: ⭐⭐⭐
title: diff-preview
url: https://skills.sh/johnlindquist/claude/diff-preview
---

# diff-preview

skills/johnlindquist/claude/diff-preview
diff-preview
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill diff-preview
SKILL.md
Diff Preview & Analysis

Preview, explain, and analyze git changes with AI assistance.

Prerequisites
# Git
git --version

# Gemini for AI explanations
pip install google-generativeai
export GEMINI_API_KEY=your_api_key

CLI Reference
Basic Diff Commands
# Working directory changes
git diff

# Staged changes
git diff --staged
git diff --cached

# Specific file
git diff path/to/file.ts

# Between commits
git diff abc123 def456

# Between branches
git diff main feature-branch
git diff main...feature-branch  # Since branch diverged

# Show stat summary
git diff --stat
git diff --shortstat

# Name only
git diff --name-only
git diff --name-status  # With status (M/A/D)

Diff Output Options
# Word diff (better for prose)
git diff --word-diff

# Color words
git diff --color-words

# Ignore whitespace
git diff -w
git diff --ignore-all-space

# Context lines
git diff -U10  # 10 lines of context (default 3)

# Show function names
git diff --function-context

Commit Comparison
# Last commit
git diff HEAD~1

# Last N commits
git diff HEAD~5

# Specific commit range
git diff abc123..def456

# What changed in a specific commit
git show abc123

AI-Powered Analysis
Explain Changes
# Get diff and explain
DIFF=$(git diff --staged)
gemini -m pro -o text -e "" "Explain these code changes in plain English:

$DIFF

Summarize:
1. What was changed
2. Why it might have been changed
3. Any potential issues"

Impact Analysis
DIFF=$(git diff main...feature-branch)
gemini -m pro -o text -e "" "Analyze the impact of these changes:

$DIFF

Consider:
1. Breaking changes
2. Performance implications
3. Security considerations
4. Files/systems affected
5. Testing recommendations"

Pre-Commit Review
# Review staged changes before commit
git diff --staged | gemini -m pro -o text -e "" "Review this code diff for:
1. Bugs or issues
2. Code style problems
3. Missing error handling
4. Security concerns

Provide specific line references if issues found."

Generate Commit Message
DIFF=$(git diff --staged)
gemini -m pro -o text -e "" "Based on this diff, suggest a commit message:

$DIFF

Use conventional commit format (feat/fix/chore/etc).
First line under 50 chars, then details."

Comparison Patterns
Compare Branches
# Summary
git diff main feature-branch --stat

# Full diff
git diff main feature-branch

# Since branch point
git diff main...feature-branch

# Commits unique to feature branch
git log main..feature-branch --oneline

Find What Changed
# What files changed between commits
git diff --name-only abc123 def456

# What changed in a file
git log -p -- path/to/file.ts

# When was a line added
git blame path/to/file.ts

Merge Preview
# Preview merge conflicts
git merge --no-commit --no-ff feature-branch
git diff --staged
git merge --abort  # Clean up

Workflow Patterns
Pre-Commit Check
#!/bin/bash
# Check staged changes before commit

echo "=== Changes to commit ==="
git diff --staged --stat

echo ""
echo "=== Detailed diff ==="
git diff --staged

echo ""
read -p "Proceed with commit? (y/n) " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]; then
  git commit
fi

PR Review Prep
# Get full PR diff for review
BASE=${1:-main}
BRANCH=$(git branch --show-current)

echo "=== Files changed ==="
git diff $BASE...$BRANCH --name-status

echo ""
echo "=== Stats ==="
git diff $BASE...$BRANCH --shortstat

echo ""
echo "=== AI Summary ==="
git diff $BASE...$BRANCH | gemini -m pro -o text -e "" "Summarize this PR's changes for a code reviewer. Focus on the intent and key changes."

Track Specific Changes
# Find all changes to a function
git log -p -S "functionName" -- "*.ts"

# Find changes mentioning something
git log -p --grep="JIRA-123"

Best Practices
Review before commit - Always check git diff --staged
Use stat first - Get overview before full diff
Compare with base - Use main...branch for PR context
Ignore whitespace - Use -w for meaningful changes
Request AI review - For complex changes
Save important diffs - Redirect to file for reference
Weekly Installs
51
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass