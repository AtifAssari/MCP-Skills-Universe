---
title: coderabbit-review
url: https://skills.sh/uwe-schwarz/skills/coderabbit-review
---

# coderabbit-review

skills/uwe-schwarz/skills/coderabbit-review
coderabbit-review
Installation
$ npx skills add https://github.com/uwe-schwarz/skills --skill coderabbit-review
SKILL.md
CodeRabbit Review

This skill provides instructions on how to use CodeRabbit CLI for code reviews, and how to handle the feedback received.

Instructions
Check authentication status with coderabbit auth status. If not logged in, prompt the user to log in using coderabbit auth login.
Determine whether to review uncommitted or committed code changes based on the git status.
Run the appropriate CodeRabbit command without sandbox:
For uncommitted changes: coderabbit --plain --type uncommitted
For committed changes: coderabbit --plain --type committed
When receiving the message "Review Completed", it indicates the review process is finished.
If there are no review comments from CodeRabbit, inform the user that no issues were found.
If there are review comments, address the issues as follows:
If the comment points out clear bugs, coding standard violations, security issues, or performance improvements, make the necessary changes immediately.
If the comment is overly strict, involves trade-offs, or requires significant architectural changes, ask the user for a decision before making any changes.
Report back to the user with a summary of the comments received from CodeRabbit and the actions taken for each comment.
Note
CodeRabbit reviews can take 5+ minutes. Please wait.
You should communicate to the user in Japanese.
Weekly Installs
9
Repository
uwe-schwarz/skills
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass