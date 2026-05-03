---
title: github
url: https://skills.sh/johnlindquist/claude-workshop-skills/github
---

# github

skills/johnlindquist/claude-workshop-skills/github
github
Installation
$ npx skills add https://github.com/johnlindquist/claude-workshop-skills --skill github
SKILL.md
GitHub Issues Manager

Complete GitHub issue management using the gh CLI tool. This Skill provides comprehensive capabilities for creating, viewing, updating, and managing GitHub issues.

Capabilities
Create issues - Create new GitHub issues with context from conversations
List issues - View and filter issues by state, labels, assignees
View issues - Display full issue details including comments
Update issues - Modify titles, bodies, labels, and assignees
Close issues - Close issues with optional closing comments
Assign issues - Assign issues to team members
Quick Reference

For detailed instructions on each operation, see:

CREATE_ISSUE.md - Creating new issues
LIST_ISSUES.md - Listing and filtering issues
VIEW_ISSUE.md - Viewing issue details
UPDATE_ISSUE.md - Updating existing issues
CLOSE_ISSUE.md - Closing issues
ASSIGN_ISSUE.md - Assigning issues to users
Common Workflows
Bug reporting workflow
User reports a bug in conversation
Create issue with /create-issue or ask me to create one
Issue is created with context from our discussion
Assign to appropriate team member
Add labels (bug, priority, etc.)
Issue triage workflow
List open issues with filters
View specific issues for details
Update labels and assignments
Close resolved issues with status updates
Sprint planning workflow
List issues by label or milestone
Assign issues to team members
Update priorities and estimates
Track progress through status updates
Critical Instructions

REQUIRED: Before executing ANY GitHub issue operations, you MUST load the relevant reference file(s) using the Read tool. These references contain essential command patterns, parameters, and workflows that are NOT included in this overview.

When the user asks to work with GitHub issues:

Identify the operation they want to perform (create, list, view, update, close, assign)
MANDATORY: Load the relevant reference file(s) using the Read tool BEFORE executing any commands:
Creating issues → Read CREATE_ISSUE.md FIRST
Listing issues → Read LIST_ISSUES.md FIRST
Viewing issues → Read VIEW_ISSUE.md FIRST
Updating issues → Read UPDATE_ISSUE.md FIRST
Closing issues → Read CLOSE_ISSUE.md FIRST
Assigning issues → Read ASSIGN_ISSUE.md FIRST
Execute the gh CLI commands following the exact patterns from the loaded reference
Use temporary files for issue bodies to avoid markdown conflicts (as specified in references)
Confirm actions and display results

DO NOT attempt to execute GitHub issue commands without first loading and reading the relevant reference documentation.

Best Practices
Always use --body-file for issue bodies to avoid shell escaping issues
Use $$ in temp file names to avoid conflicts (expands to process ID)
Format issue bodies with proper markdown structure
Include context from conversations when creating issues
Clean up temp files after operations
Display issue URLs so users can navigate to GitHub
Examples
Create an issue from context
User: "I found a bug where login fails with special characters"
Me: *Creates issue with details from conversation*

List and filter issues
User: "Show me all open bugs assigned to alice"
Me: gh issue list --state open --label bug --assignee alice

Update an issue
User: "Add high-priority label to issue #123"
Me: gh issue edit 123 --add-label "high-priority"

Close with context
User: "Close issue #456, it was fixed in the last PR"
Me: gh issue close 456 --comment "Fixed in PR #789"

Weekly Installs
16
Repository
johnlindquist/c…p-skills
GitHub Stars
16
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn