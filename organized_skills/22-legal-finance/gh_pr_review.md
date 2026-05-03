---
rating: ⭐⭐⭐⭐⭐
title: gh-pr-review
url: https://skills.sh/squirrel289/pax/gh-pr-review
---

# gh-pr-review

skills/squirrel289/pax/gh-pr-review
gh-pr-review
Installation
$ npx skills add https://github.com/squirrel289/pax --skill gh-pr-review
SKILL.md
gh-pr-review

A skill for comprehensive GitHub pull request interaction using the GitHub CLI and API.

Interface, Workflows, and Best Practices

This skill implements the shared, versioned interface and workflows defined in ../PR_MANAGEMENT_INTERFACE.md.

All parameters, output formats, error handling, and best practices are defined in the shared interface.
This file documents only CLI-specific usage, requirements, and backend notes.
When to Use

Use this skill when you need to interact with GitHub pull requests via the command line, especially in environments where the GitHub CLI (gh) is available and API-based skills are not suitable. It is ideal for:

Automated PR review workflows
LLM-based code review agents
PR processing and merge automation
Resolving review feedback programmatically
Prerequisites

GitHub CLI (gh) must be installed and authenticated:

gh auth login


Optional: Install the gh-pr-review extension for enhanced review features:

gh extension install agynio/gh-pr-review

CLI Usage Examples

The following examples show how to invoke the shared interface using the GitHub CLI and the gh-pr-review extension. See ../PR_MANAGEMENT_INTERFACE.md for parameter details and expected outputs.

View Pull Request Details
gh pr view <number> --json title,state,author,mergeable,statusCheckRollup

View All Reviews and Threads
gh pr-review review view -R owner/repo --pr <number>
# Filters:
#   --unresolved
#   --reviewer <login>
#   --states APPROVED,CHANGES_REQUESTED,COMMENTED
#   --not_outdated

Reply to Review Threads
gh pr-review comments reply <pr-number> -R owner/repo \
  --thread-id <PRRT_...> \
  --body "Your reply message"

Resolve Review Threads
gh pr-review threads resolve -R owner/repo <pr-number> \
  --thread-id <PRRT_...>


List unresolved threads:

gh pr-review threads list -R owner/repo <pr-number> --unresolved

Check Merge Readiness
gh pr view <number> --json mergeable,mergeStateStatus,statusCheckRollup

Merge Pull Request
gh pr merge <number> --merge|--squash|--rebase [--auto] [--delete-branch]

Output Format

All GitHub CLI commands return structured JSON for programmatic use. See ../PR_MANAGEMENT_INTERFACE.md for field definitions and output structure.

Common Workflows

See ../PR_MANAGEMENT_INTERFACE.md for canonical workflows, error handling, and best practices. All workflows are supported via the CLI commands above.

Best Practices

Refer to ../PR_MANAGEMENT_INTERFACE.md for best practices. When using the CLI, always specify -R owner/repo for clarity, parse JSON output, and handle errors as described in the shared interface.

Error Handling

See ../PR_MANAGEMENT_INTERFACE.md for error handling strategies and common issues. CLI-specific errors (e.g., not authenticated) should be handled as per GitHub CLI documentation.

Integration with Other Skills

This skill is fully composable with other PAX skills, including parallel and sequential execution, yolo/collaborative interaction, and dedicated PR processing/merge/comment resolution skills. See ../PR_MANAGEMENT_INTERFACE.md for integration patterns.

Quick Reference
FETCH PR:

```bash
gh pr view <number> --json <fields>
```

LIST COMMENTS:

```bash
gh pr-review review view -R owner/repo --pr <number> [--unresolved]
```

REPLY TO COMMENT:

```bash
gh pr-review comments reply <number> -R owner/repo \
 --thread-id <id> --body "message"
```

RESOLVE THREAD:

```bash
gh pr-review threads resolve -R owner/repo <number> \
 --thread-id <id>
```

CHECK MERGEABLE:

```bash
gh pr view <number> --json mergeable,mergeStateStatus,statusCheckRollup
```

MERGE PR:

```bash
gh pr merge <number> --squash --delete-branch
```

LIST UNRESOLVED:

```bash
gh pr-review threads list -R owner/repo <number> --unresolved
```

Weekly Installs
10
Repository
squirrel289/pax
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn