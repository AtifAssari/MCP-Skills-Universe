---
title: pr-review
url: https://skills.sh/jellydn/my-ai-tools/pr-review
---

# pr-review

skills/jellydn/my-ai-tools/pr-review
pr-review
Installation
$ npx skills add https://github.com/jellydn/my-ai-tools --skill pr-review
SKILL.md
Fix PR Review Comments

Fix PR review comments by implementing the requested changes.

Usage
/pr-review <PR_URL>      # Review PR by URL (expects full GitHub URL)
/pr-review <PR_NUMBER>   # Review PR by number (expects number, e.g., 123)
/pr-review               # Auto-detect PR from current branch

📋 Argument Handling

The command accepts the PR identifier from $ARGUMENTS:

PR URL: Full GitHub PR URL (e.g., https://github.com/owner/repo/pull/123)
PR Number: Just the PR number (e.g., 123)
No Arguments: Auto-detect the PR associated with the current Git branch

If $ARGUMENTS is provided, use it as the PR identifier. Otherwise, auto-detect the current branch's PR using:

gh pr view --json number,url -q '.number'


This extracts the PR number from the current branch's open PR for use in subsequent commands.

If no open PR is found for the current branch, show this error:

Error: No open pull request found for the current branch.

To review a specific PR:
  /pr-review <PR_URL>
  /pr-review <PR_NUMBER>

Or create a PR first:
  gh pr create

Process
Parse $ARGUMENTS to determine PR identifier (URL, number, or auto-detect)
Fetch PR details and review comments using gh CLI
Parse review comments to understand what needs to be changed
For each comment, implement the fix
Run tests to ensure nothing breaks
Commit the changes
Available Scripts
Extract PR Comments

The extract-pr-comments.js script processes GitHub PR review comments and issue comments to create actionable TODO lists.

# Usage
node $SKILL_PATH/scripts/extract-pr-comments.js <review-comments-file> <issue-comments-file> [output-file]

# Example
node $SKILL_PATH/scripts/extract-pr-comments.js \
  pr-4972-review-comments-raw.json \
  pr-4972-issue-comments-raw.json \
  pr-4972-comments.ndjson


What it does:

Filters out comments with replies (likely resolved)
Classifies comments by severity (critical, high, medium, low)
Categorizes comments (security, performance, maintainability, etc.)
Creates 3 output files:
.ndjson - Structured comment data
-todo.md - Prioritized TODO list
-summary.md - Analysis summary with emojis

Severity classification:

🔴 Critical: security, vulnerability, exploit
🟠 High: bug, error, breaking, crash, fail
🟡 Medium: performance, improvement, refactor, optimize
🟢 Low: everything else

Categories:

🔒 Security
⚡ Performance
🔧 Maintainability
♿ Accessibility
🧪 Testing
📚 Documentation
🏷️ Typing
🎨 Style
✨ Code Quality
Examples
# Fix review comments for a PR using URL
/pr-review https://github.com/owner/repo/pull/123

# Fix review comments using PR number
/pr-review 123

# Auto-detect PR from current branch
/pr-review

# After extracting comments with the script, work through the TODO list
# The TODO list is ordered by priority: Critical → High → Medium → Low

Weekly Installs
27
Repository
jellydn/my-ai-tools
GitHub Stars
71
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn