---
title: pr-reviewer
url: https://skills.sh/spillwavesolutions/pr-reviewer-skill/pr-reviewer
---

# pr-reviewer

skills/spillwavesolutions/pr-reviewer-skill/pr-reviewer
pr-reviewer
Installation
$ npx skills add https://github.com/spillwavesolutions/pr-reviewer-skill --skill pr-reviewer
SKILL.md
PR Reviewer Skill

Conduct comprehensive, professional code reviews for GitHub Pull Requests using industry-standard criteria and automated tooling.

Table of Contents
Purpose
When to Use
Review Process Workflow
Reference Documentation
Scripts Reference
Best Practices
Quick Reference Commands
Tips for Effective Reviews
Resources
Purpose

This skill performs code reviews by:

Automating data collection - Fetching all PR-related information (metadata, diff, comments, commits, issues)
Organizing review workspace - Creating structured directory with all artifacts
Applying systematic criteria - Reviewing against comprehensive quality checklist
Facilitating inline feedback - Optionally adding comments directly to PR code
Ensuring completeness - Checking functionality, security, testing, maintainability
When to Use

Activate this skill when:

A GitHub PR URL is provided with a review request
Receiving "review this PR" or "code review" requests
Checking PR quality before merging
Providing systematic feedback on proposed changes
GitHub PR review is mentioned in any context
Review Process Workflow

IMPORTANT: This skill uses a two-stage approval process. Nothing is posted to GitHub until explicit approval with /send or /send-decline.

Overview
Fetch PR data - Collect all information
Generate review files - Create detailed, human, and inline comment files
Review and edit - Examine files, make changes as needed (use /show)
Approve and post - Use /send (approve) or /send-decline (request changes)
Step 1: Fetch PR Data

Use fetch_pr_data.py to automatically collect all PR information:

python scripts/fetch_pr_data.py <pr_url> [--output-dir <dir>] [--no-clone]


Actions performed:

Parse PR URL to extract owner, repo, and PR number
Create directory structure: <output-dir>/PRs/<repo-name>/<PR-NUMBER>/
Fetch PR metadata (title, author, state, branches, labels)
Download PR diff and commit history
Retrieve all PR comments and reviews
Extract ticket references (JIRA, GitHub issues)
Optionally clone source branch and generate git diff

Example:

python scripts/fetch_pr_data.py https://github.com/facebook/react/pull/28476

# Custom output directory
python scripts/fetch_pr_data.py https://github.com/owner/repo/pull/123 --output-dir /tmp/reviews

# Skip cloning (faster, no git diff)
python scripts/fetch_pr_data.py https://github.com/owner/repo/pull/123 --no-clone


Output structure:

/tmp/PRs/<repo-name>/<PR-NUMBER>/
├── metadata.json           # PR metadata (title, author, branches)
├── diff.patch             # PR diff from gh CLI
├── git_diff.patch         # Git diff (if cloned)
├── comments.json          # Review comments on code
├── commits.json           # Commit history
├── related_issues.json    # Linked GitHub issues
├── ticket_numbers.json    # Extracted ticket references
├── SUMMARY.txt            # Human-readable summary
└── source/                # Cloned repository (if not --no-clone)

Step 2: Analyze PR Data

After fetching, analyze collected data against review criteria:

Read SUMMARY.txt - High-level overview
Review metadata.json - PR context, labels, assignees
Examine diff.patch - Code changes
Check comments.json - Existing feedback
Review commits.json - Commit quality and messages
Check related_issues.json - Linked tickets/issues
Apply review criteria - Evaluate against comprehensive checklist

Use the Read tool to examine files:

Read /tmp/PRs/<repo-name>/<PR-NUMBER>/SUMMARY.txt
Read /tmp/PRs/<repo-name>/<PR-NUMBER>/metadata.json
Read /tmp/PRs/<repo-name>/<PR-NUMBER>/diff.patch

Step 3: Generate Review Files

CRITICAL: After analysis, use generate_review_files.py to create structured review documents:

python scripts/generate_review_files.py <pr_review_dir> --findings <findings_json> [--metadata <metadata_json>]


Creates three files in pr_review_dir/pr/:

pr/review.md - Detailed internal review with emojis and line numbers
pr/human.md - Clean review for posting (no emojis, em-dashes, line numbers)
pr/inline.md - Proposed inline comments with code snippets

Also creates slash commands in .claude/commands/:

/send - Post human.md and approve PR
/send-decline - Post human.md and request changes
/show - Open review directory in VS Code

Findings JSON structure:

{
  "summary": "Overall assessment of the PR...",
  "metadata": {
    "repository": "owner/repo",
    "number": 123,
    "title": "PR title",
    "author": "username",
    "head_branch": "feature",
    "base_branch": "main"
  },
  "blockers": [
    {
      "category": "Security",
      "issue": "SQL injection vulnerability",
      "file": "src/db/queries.py",
      "line": 45,
      "details": "Using string concatenation for SQL query",
      "fix": "Use parameterized queries",
      "code_snippet": "result = db.execute('SELECT * FROM users WHERE id = ' + user_id)"
    }
  ],
  "important": [...],
  "nits": [...],
  "suggestions": ["Consider adding...", "Future enhancement..."],
  "questions": ["Is this intended to...", "Should we..."],
  "praise": ["Excellent test coverage", "Clear documentation"],
  "inline_comments": [
    {
      "file": "src/app.py",
      "line": 42,
      "comment": "Consider edge case handling for empty input",
      "code_snippet": "def process(data):\n    return data.strip()",
      "start_line": 41,
      "end_line": 43,
      "owner": "owner",
      "repo": "repo",
      "pr_number": 123
    }
  ]
}

Step 4: Review and Edit Files

Use /show to open the review directory in VS Code.

Actions available:

Read pr/review.md - Detailed analysis
Edit pr/human.md - Modify before posting
Review pr/inline.md - Check proposed comments
Adjust any content as needed

NOTHING is posted until explicit approval in Step 5.

Step 5: Approve and Post

Post the review when ready:

Option A: Approve the PR

/send

Posts pr/human.md as comment
Approves the PR
Confirms action

Option B: Request Changes

/send-decline

Posts pr/human.md as comment
Requests changes on the PR
Confirms action

Posting inline comments (optional, after /send or /send-decline): Review pr/inline.md and run the provided commands for specific code comments.

Step 6: Apply Review Criteria

Reference references/review_criteria.md for comprehensive checklist. Review against these categories:

Category	Key Questions
Functionality	Does code solve the problem? Bugs? Edge cases?
Readability	Clear code? Meaningful names? DRY?
Style	Follows linter rules? Consistent with codebase?
Performance	Efficient algorithms? Scalable?
Security	Vulnerabilities addressed? Secrets protected?
Testing	Tests exist? Cover happy paths and edge cases?
PR Quality	Focused scope? Clean commits? Clear description?

Priority markers for findings:

Blocker: Must be fixed before merge
Important: Should be addressed
Nit: Nice to have, optional
Suggestion: Consider for future
Question: Clarification needed
Praise: Good work

For detailed criteria: Read references/review_criteria.md

Reference Documentation

This skill includes comprehensive reference guides:

Reference	Purpose
references/review_criteria.md	Complete checklist covering functionality, security, testing, and more
references/gh_cli_guide.md	Quick reference for GitHub CLI commands
references/scenarios.md	Detailed workflows for common review scenarios
references/troubleshooting.md	Common issues and solutions
Scripts Reference
scripts/fetch_pr_data.py

Automated PR data fetching and organization.

python scripts/fetch_pr_data.py <pr_url> [options]

Options:
  --output-dir DIR    Base output directory (default: /tmp)
  --no-clone         Skip cloning repository

scripts/generate_review_files.py

Generate structured review files from analysis findings.

python scripts/generate_review_files.py <pr_review_dir> --findings <findings_json> [--metadata <metadata_json>]


Creates:

pr/review.md - Detailed internal review
pr/human.md - Clean review for posting
pr/inline.md - Proposed inline comments with commands
.claude/commands/send.md - Slash command to approve and post
.claude/commands/send-decline.md - Slash command to request changes
.claude/commands/show.md - Slash command to open in VS Code
REVIEW_READY.txt - Summary of next steps
scripts/add_inline_comment.py

Add inline code review comments to specific lines in PR.

python scripts/add_inline_comment.py <owner> <repo> <pr_number> <commit_id> <file_path> <line> "<comment>" [options]

Options:
  --side RIGHT|LEFT       Side of diff (default: RIGHT)
  --start-line N         Starting line for multi-line comment
  --start-side RIGHT|LEFT Starting side for multi-line comment

Best Practices
Communication
Frame feedback as suggestions, not criticism
Explain why an issue matters, not just what is wrong
Acknowledge excellent practices
Prioritize blockers first, style issues last
Review Efficiency
Use scripts to automate data fetching and comment posting
Reference review_criteria.md as checklist
Focus: Critical issues > Important > Nice-to-have
Review promptly (within 24 hours if possible)
Inline Comments
Reference exact lines and files
Provide better alternatives
Test inline comments on test PRs first
Use sparingly to avoid overwhelming
PR Size Handling
Large PRs (>400 lines): Suggest splitting
Review in logical chunks
Focus on architecture for large changes

For detailed scenarios: Read references/scenarios.md

Quick Reference Commands
# Fetch PR data
python scripts/fetch_pr_data.py https://github.com/owner/repo/pull/123

# Add inline comment
python scripts/add_inline_comment.py owner repo 123 latest "src/app.py" 42 "Comment"

# View PR in browser
gh pr view 123 --repo owner/repo --web

# Check PR status
gh pr checks 123 --repo owner/repo

# View existing comments
gh api /repos/owner/repo/pulls/123/comments --jq '.[] | {path, line, body}'

Tips for Effective Reviews
Start with context: Read PR description, linked issues, commit messages
Understand intent: Identify the problem being solved
Check tests first: Verify tests demonstrate the fix/feature
Look for patterns: Repeated issues suggest architecture problems
Consider alternatives: Evaluate simpler approaches
Think about maintenance: Assess future modification ease
Remember humans: Maintain kindness, respect, and constructive tone

For troubleshooting: Read references/troubleshooting.md

Resources
Review Criteria: references/review_criteria.md
gh CLI Guide: references/gh_cli_guide.md
Scenarios: references/scenarios.md
Troubleshooting: references/troubleshooting.md
GitHub PR Review Docs: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests
Google Engineering Practices: https://google.github.io/eng-practices/review/
OWASP Top 10: https://owasp.org/www-project-top-ten/
Weekly Installs
55
Repository
spillwavesoluti…er-skill
GitHub Stars
15
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn