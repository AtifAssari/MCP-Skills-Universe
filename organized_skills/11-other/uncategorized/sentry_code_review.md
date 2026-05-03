---
rating: ⭐⭐⭐
title: sentry-code-review
url: https://skills.sh/getsentry/sentry-for-ai/sentry-code-review
---

# sentry-code-review

skills/getsentry/sentry-for-ai/sentry-code-review
sentry-code-review
Installation
$ npx skills add https://github.com/getsentry/sentry-for-ai --skill sentry-code-review
SKILL.md

All Skills > Workflow > Code Review

Sentry Code Review

You are a specialized skill for analyzing and resolving issues identified by Sentry in GitHub Pull Request review comments.

Sentry PR Review Comment Format

Sentry posts line-specific review comments on code changes in PRs. Each comment includes:

Comment Metadata (from API)
author: The bot username (e.g., "sentry[bot]")
file: The specific file being commented on (e.g., "src/sentry/seer/explorer/tools.py")
line: The line number in the code (can be null for file-level comments)
body: The full comment content (markdown with HTML details tags)
Body Structure

The body field contains markdown with collapsible sections:

Header:

**Bug:** [Issue description]
<sub>Severity: CRITICAL | Confidence: 1.00</sub>


Analysis Section (in <details> tag):

<details>
<summary>🔍 <b>Detailed Analysis</b></summary>
Explains the technical problem and consequences
</details>


Fix Section (in <details> tag):

<details>
<summary>💡 <b>Suggested Fix</b></summary>
Proposes a concrete solution
</details>


AI Agent Prompt (in <details> tag):

<details>
<summary>🤖 <b>Prompt for AI Agent</b></summary>
Specific instructions for reviewing and fixing the issue
Includes: Location (file#line), Potential issue description
</details>

Example Issues

TypeError from None values

Functions returning None when list expected
Missing null checks before iterating

Validation Issues

Too permissive input validation
Allowing invalid data to pass through

Error Handling Gaps

Errors logged but not re-thrown
Silent failures in critical paths
Your Workflow
1. Fetch PR Comments

When given a PR number or URL:

# Get PR review comments (line-by-line code comments) using GitHub API
gh api repos/{owner}/{repo}/pulls/<PR_NUMBER>/comments --jq '.[] | select(.user.login | startswith("sentry")) | {author: .user.login, file: .path, line: .line, body: .body}'


Or fetch from the PR URL directly using WebFetch.

2. Parse Sentry Comments
ONLY process comments from Sentry (username starts with "sentry", e.g., "sentry[bot]")
IGNORE comments from "cursor[bot]" or other bots
Extract from each comment:
file: The file path being commented on
line: The specific line number (if available)
body: Parse the markdown/HTML body to extract:
Bug description (from header line starting with "Bug:")
Severity level (from <sub>Severity: X tag)
Confidence score (from Confidence: X.XX in sub tag)
Detailed analysis (text inside <summary>🔍 <b>Detailed Analysis</b></summary> details block)
Suggested fix (text inside <summary>💡 <b>Suggested Fix</b></summary> details block)
AI Agent prompt (text inside <summary>🤖 <b>Prompt for AI Agent</b></summary> details block)
3. Analyze Each Issue

For each Sentry comment:

Note the file and line from the comment metadata - this tells you exactly where to look
Read the specific file mentioned in the comment
Navigate to the line number to see the problematic code
Read the "🤖 Prompt for AI Agent" section for specific context about the issue
Verify if the issue is still present in the current code
Understand the root cause from the Detailed Analysis
Evaluate the Suggested Fix
4. Implement Fixes

For each verified issue:

Read the affected file(s)
Implement the suggested fix or your own solution
Ensure the fix addresses the root cause
Consider edge cases and side effects
Use Edit tool to make precise changes
5. Provide Summary

After analyzing and fixing issues, provide a report:

## Sentry Code Review Summary

**PR:** #[number] - [title]
**Sentry Comments Found:** [count]

### Issues Resolved

#### 1. [Issue Title] - [SEVERITY]
- **Confidence:** [score]
- **Location:** [file:line]
- **Problem:** [brief description]
- **Fix Applied:** [what you did]
- **Status:** Resolved

#### 2. [Issue Title] - [SEVERITY]
- **Confidence:** [score]
- **Location:** [file:line]
- **Problem:** [brief description]
- **Fix Applied:** [what you did]
- **Status:** Resolved

### Issues Requiring Manual Review

#### 1. [Issue Title] - [SEVERITY]
- **Reason:** [why manual review is needed]
- **Recommendation:** [suggested approach]

### Summary
- **Total Issues:** [count]
- **Resolved:** [count]
- **Manual Review Required:** [count]

Important Guidelines
Only Sentry: Focus on comments from Sentry (username starts with "sentry")
Verify First: Always confirm the issue exists before attempting fixes
Read Before Edit: Always use Read tool before using Edit tool
Precision: Make targeted fixes that address the root cause
Safety: If unsure about a fix, ask the user for guidance using AskUserQuestion
Testing: Remind the user to run tests after fixes are applied
Common Sentry Bot Issue Categories
Build Configuration Issues
Missing files in build output
Incorrect tsconfig settings
Missing file copy steps in build scripts
Error Handling Issues
Errors caught but not re-thrown
Silent failures in critical paths
Missing error boundaries
Runtime Configuration Issues
Missing environment variables
Incorrect path resolutions
Missing required dependencies
Type Safety Issues
Missing null checks
Type assertions that could fail
Missing input validation
Weekly Installs
892
Repository
getsentry/sentry-for-ai
GitHub Stars
160
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn