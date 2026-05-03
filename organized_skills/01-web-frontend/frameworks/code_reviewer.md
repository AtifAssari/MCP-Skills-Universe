---
rating: ⭐⭐
title: code-reviewer
url: https://skills.sh/google-gemini/gemini-cli/code-reviewer
---

# code-reviewer

skills/google-gemini/gemini-cli/code-reviewer
code-reviewer
Installation
$ npx skills add https://github.com/google-gemini/gemini-cli --skill code-reviewer
Summary

Automated code review for local changes and remote pull requests with structured analysis across correctness, maintainability, and security.

Supports both local file system changes (staged and unstaged) and remote PRs (by number or URL) with automatic GitHub CLI checkout
Analyzes code across seven dimensions: correctness, maintainability, readability, efficiency, security, edge case handling, and test coverage
Runs optional preflight verification suites (e.g., npm run preflight) to catch automated failures before detailed review
Structures feedback into summary, categorized findings (critical issues, improvements, nitpicks), and clear approval or change-request recommendations
SKILL.md
Code Reviewer

This skill guides the agent in conducting professional and thorough code reviews for both local development and remote Pull Requests.

Workflow
1. Determine Review Target
Remote PR: If the user provides a PR number or URL (e.g., "Review PR #123"), target that remote PR.
Local Changes: If no specific PR is mentioned, or if the user asks to "review my changes", target the current local file system states (staged and unstaged changes).
2. Preparation
For Remote PRs:
Checkout: Use the GitHub CLI to checkout the PR.
gh pr checkout <PR_NUMBER>

Preflight: Execute the project's standard verification suite to catch automated failures early.
npm run preflight

Context: Read the PR description and any existing comments to understand the goal and history.
For Local Changes:
Identify Changes:
Check status: git status
Read diffs: git diff (working tree) and/or git diff --staged (staged).
Preflight (Optional): If the changes are substantial, ask the user if they want to run npm run preflight before reviewing.
3. In-Depth Analysis

Analyze the code changes based on the following pillars:

Correctness: Does the code achieve its stated purpose without bugs or logical errors?
Maintainability: Is the code clean, well-structured, and easy to understand and modify in the future? Consider factors like code clarity, modularity, and adherence to established design patterns.
Readability: Is the code well-commented (where necessary) and consistently formatted according to our project's coding style guidelines?
Efficiency: Are there any obvious performance bottlenecks or resource inefficiencies introduced by the changes?
Security: Are there any potential security vulnerabilities or insecure coding practices?
Edge Cases and Error Handling: Does the code appropriately handle edge cases and potential errors?
Testability: Is the new or modified code adequately covered by tests (even if preflight checks pass)? Suggest additional test cases that would improve coverage or robustness.
4. Provide Feedback
Structure
Summary: A high-level overview of the review.
Findings:
Critical: Bugs, security issues, or breaking changes.
Improvements: Suggestions for better code quality or performance.
Nitpicks: Formatting or minor style issues (optional).
Conclusion: Clear recommendation (Approved / Request Changes).
Tone
Be constructive, professional, and friendly.
Explain why a change is requested.
For approvals, acknowledge the specific value of the contribution.
5. Cleanup (Remote PRs only)
After the review, ask the user if they want to switch back to the default branch (e.g., main or master).
Weekly Installs
6.1K
Repository
google-gemini/gemini-cli
GitHub Stars
103.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn