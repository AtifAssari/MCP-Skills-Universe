---
title: coderabbit-review
url: https://skills.sh/showcase-gig-platform/scg-ai-playbook/coderabbit-review
---

# coderabbit-review

skills/showcase-gig-platform/scg-ai-playbook/coderabbit-review
coderabbit-review
Installation
$ npx skills add https://github.com/showcase-gig-platform/scg-ai-playbook --skill coderabbit-review
SKILL.md
Coderabbit Review
Workflow
After implementing code changes, request a review from CodeRabbit
Analyze the review results and understand the feedback
Fix the identified issues
Re-run the review if necessary to confirm fixes
Command Reference
--prompt-only: Show only AI agent prompts (implies --plain)
--plain: Output in plain text format with human-friendly formatting
--type <type>: Review type: all, committed, uncommitted (default: "all")
--base <branch>: Base branch for comparison
--base-commit <commit>: Base commit on current branch for comparison
--cwd <path>: Working directory path (default: current directory)
Command Selection

Review all changes (default):

coderabbit review --prompt-only


Review uncommitted changes only:

coderabbit review --prompt-only --type uncommitted


Review committed changes only:

coderabbit review --prompt-only --type committed


Compare against base branch:

coderabbit review --prompt-only --base <branch>

Handling Review Feedback

When review feedback is received, address issues in the following priority order:

Security issues - Fix immediately
Bugs/regressions - High priority fixes
Missing tests - Add required test coverage
Code quality - Implement refactoring and improvements
Style/conventions - Align with project standards
Verification

After addressing the feedback, re-run coderabbit review --prompt-only to confirm that the issues have been resolved.

Weekly Installs
11
Repository
showcase-gig-pl…playbook
GitHub Stars
3
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass