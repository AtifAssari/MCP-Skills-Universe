---
title: gh-tool
url: https://skills.sh/blogic-cz/agent-tools/gh-tool
---

# gh-tool

skills/blogic-cz/agent-tools/gh-tool
gh-tool
Installation
$ npx skills add https://github.com/blogic-cz/agent-tools --skill gh-tool
SKILL.md
gh-tool (GitHub)

GitHub CLI wrapper — PRs, issues, workflows, checks, reviews, merge. Part of @blogic-cz/agent-tools.

How to Run

Run via bun gh-tool (requires @blogic-cz/agent-tools as a dev dependency). NEVER run bare gh — the credential guard will block it. Auth: gh auth login or GITHUB_TOKEN env var.

PR Commands
bun gh-tool pr status                  # View PR status for current branch
bun gh-tool pr view --pr 123           # View PR details
bun gh-tool pr checks --pr 123         # Check CI status
bun gh-tool pr checks --pr 123 --watch # Watch CI until complete
bun gh-tool pr checks-failed --pr 123  # Get failed check details
bun gh-tool pr close --pr 123 --comment "Closing, no longer needed" --delete-branch
bun gh-tool pr merge --pr 123 --strategy squash --delete-branch --confirm
bun gh-tool pr threads --pr 123 --unresolved-only  # Review comments
bun gh-tool pr reply --pr 123 --comment-id 456 --body "Fixed"
bun gh-tool pr resolve --thread-id 789
bun gh-tool pr create --base test --title "feat: X" --body "Description"
bun gh-tool pr review-triage --pr 123  # Combined info, threads, checks
bun gh-tool pr reply-and-resolve --pr 123 --comment-id 456 --thread-id 789 --body "Done"

Workflow Commands
bun gh-tool workflow list                              # List recent workflow runs
bun gh-tool workflow view --run 123                    # View run details with jobs/steps
bun gh-tool workflow watch --run 123                   # Block until run completes (NO sleep-polling!)
bun gh-tool workflow logs --run 123                    # Fetch logs (failed jobs by default)
bun gh-tool workflow job-logs --run 123 --job "build"  # Clean parsed logs for specific job
bun gh-tool workflow rerun --run 123                   # Rerun failed jobs
bun gh-tool workflow cancel --run 123                  # Cancel in-progress run


NEVER use sleep N && workflow list/jobs/view — use workflow watch --run N instead. The credential guard blocks sleep-polling with agent-tools commands.

Issue Commands
bun gh-tool issue list --state open --limit 30
bun gh-tool issue view --issue 123
bun gh-tool issue close --issue 123 --reason completed --comment "Done"
bun gh-tool issue reopen --issue 123
bun gh-tool issue comment --issue 123 --body "text"
bun gh-tool issue edit --issue 123 --title "New title" --add-labels bug
bun gh-tool issue triage --issue 123 --verbosity full --format json

Branch Commands
bun gh-tool branch rename --old-name feature/old --new-name feature/new          # Dry-run
bun gh-tool branch rename --old-name feature/old --new-name feature/new --confirm # Execute
bun gh-tool branch rename --old-name feature/old --new-name feature/new --repo owner/repo --confirm

Tips
Use --help on any subcommand for full options.
Error responses include hint, nextCommand, and retryable fields — always check them on failure.
Prefer CLI tool over MCP tools — more efficient, doesn't load extra context.
Weekly Installs
8
Repository
blogic-cz/agent-tools
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn