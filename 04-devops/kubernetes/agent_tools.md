---
title: agent-tools
url: https://skills.sh/blogic-cz/agent-tools/agent-tools
---

# agent-tools

skills/blogic-cz/agent-tools/agent-tools
agent-tools
Installation
$ npx skills add https://github.com/blogic-cz/agent-tools --skill agent-tools
SKILL.md
Agent Tools

Safe CLI wrappers for AI coding agents — GitHub, observability, databases, Kubernetes, Azure DevOps, logs, and OpenCode sessions.

Full documentation: Read the README for complete API reference, configuration, and credential setup.

How to Run (CRITICAL)

Run tools via bun <tool-name> (requires @blogic-cz/agent-tools as a dev dependency):

bun gh-tool pr status
bun observability-tool trace get <trace-id> --env local
bun k8s-tool pods --env test
bun db-tool sql --env local --sql "SELECT 1"


NEVER run raw kubectl, gh, psql, az — the credential guard will block them.

Legacy agent-tools-* binary names (e.g. bun gh-tool) still work but prefer the short form.

Tools Overview
Tool	Description	Help
gh-tool	GitHub CLI wrapper — PRs, issues, workflows, checks, reviews, merge	bun gh-tool --help
observability-tool	LGTM wrapper — Tempo traces, Loki logs, Prometheus metrics	bun observability-tool --help
db-tool	Database query tool — SQL execution, schema introspection	bun db-tool --help
k8s-tool	Kubernetes tool — kubectl with config-driven context resolution	bun k8s-tool --help
az-tool	Azure DevOps tool — pipelines, builds, repos (read-only)	bun az-tool --help
logs-tool	Application logs — read local and remote (k8s pod) logs	bun logs-tool --help
session-tool	OpenCode session browser — list, read, search session history	bun session-tool --help
Tool Priority
CLI Tools (Preferred) — More efficient, don't load context, provide full functionality
MCP Tools (Fallback) — Use when CLI alternatives don't exist

Always prefer bun gh-tool over raw gh, bun db-tool over raw psql, bun k8s-tool over raw kubectl. The wrappers add security guardrails, audit trails, and project-specific config.

Consistency: Tools provide hint, nextCommand, and retryable fields in error responses to help you recover from failures. Always check these fields when a command fails.

Quick Reference
gh-tool (GitHub)
bun gh-tool pr status                  # View PR status for current branch
bun gh-tool pr view --pr 123           # View PR details
bun gh-tool pr checks --pr 123         # Check CI status
bun gh-tool pr checks --pr 123 --watch # Watch CI until complete
bun gh-tool pr checks-failed --pr 123  # Get failed check details
bun gh-tool pr merge --pr 123 --strategy squash --delete-branch --confirm
bun gh-tool pr threads --pr 123 --unresolved-only  # Review comments
bun gh-tool pr reply --pr 123 --comment-id 456 --body "Fixed"
bun gh-tool pr resolve --thread-id 789
bun gh-tool pr create --base test --title "feat: X" --body "Description"
bun gh-tool pr review-triage --pr 123  # Combined info, threads, checks
bun gh-tool pr reply-and-resolve --pr 123 --comment-id 456 --thread-id 789 --body "Done"

bun gh-tool workflow list                              # List recent workflow runs
bun gh-tool workflow view --run 123                    # View run details with jobs/steps
bun gh-tool workflow watch --run 123                   # Block until run completes (NO sleep-polling!)
bun gh-tool workflow logs --run 123                    # Fetch logs (failed jobs by default)
bun gh-tool workflow job-logs --run 123 --job "build"  # Clean parsed logs for specific job
bun gh-tool workflow rerun --run 123                   # Rerun failed jobs
bun gh-tool workflow cancel --run 123                  # Cancel in-progress run


NEVER use sleep N && workflow list/jobs/view — use workflow watch --run N instead. The credential guard blocks sleep-polling with agent-tools commands.

bun gh-tool issue list --state open --limit 30
bun gh-tool issue view --issue 123
bun gh-tool issue close --issue 123 --reason completed --comment "Done"
bun gh-tool issue reopen --issue 123
bun gh-tool issue comment --issue 123 --body "text"
bun gh-tool issue edit --issue 123 --title "New title" --add-labels bug
bun gh-tool issue triage --issue 123 --verbosity full --format json

observability-tool (LGTM)
bun observability-tool trace get 0b7bdf0dde1c55458364ba5588a8075e --env local
bun observability-tool trace logs 0b7bdf0dde1c55458364ba5588a8075e --env local --limit 100
bun observability-tool metrics query 'up' --env local --start now-1h --end now --step 60

db-tool (Database)
bun db-tool sql --env local --sql "SELECT * FROM users LIMIT 5"
bun db-tool sql --env test --sql "SELECT count(*) FROM organizations"
bun db-tool schema --env local --mode tables          # List tables
bun db-tool schema --env local --mode columns --table users # Show table schema


Environment is any string (e.g. local, test, prod). Set defaultEnvironment in config to skip --env on every call.

k8s-tool (Kubernetes)
bun k8s-tool kubectl --env test --cmd "get pods -n test-ns"
bun k8s-tool kubectl --env prod --cmd "logs <pod> --tail=100"
bun k8s-tool kubectl --env test --cmd "describe pod <pod>"
bun k8s-tool pods --env test                     # List pods
bun k8s-tool logs --pod <pod> --env test --tail 50 # Fetch logs
bun k8s-tool describe --resource pod --name <pod> --env test
bun k8s-tool exec --pod <pod> --exec-cmd "ls -la" --env test
bun k8s-tool top --env test                      # Show resource usage

az-tool (Azure DevOps)
bun az-tool cmd --cmd "pipelines list"
bun az-tool cmd --cmd "pipelines show --id 123"
bun az-tool cmd --cmd "pipelines runs list --top 5"
bun az-tool cmd --cmd "pipelines runs show --id 456"
bun az-tool build summary --build-id 456      # Job status & duration
bun az-tool build timeline --build-id 456     # Full event timeline
bun az-tool build failed-jobs --build-id 456   # Just failures
bun az-tool build logs --build-id 456          # List available logs
bun az-tool build log-content --build-id 456 --log-id 78

logs-tool (Application Logs)
bun logs-tool list --env local          # List available log files
bun logs-tool read --env local --file app.log  # Read specific log
bun logs-tool read --env test --file app.log --tail 50

session-tool (OpenCode Sessions)
bun session-tool list                   # List recent sessions
bun session-tool read --session <session-id> # Read session messages
bun session-tool search "query"         # Search across sessions

Configuration

Config is loaded from agent-tools.json5 (or agent-tools.json) by walking up from the current working directory.

See full config reference: https://github.com/blogic-cz/agent-tools#configuration

defaultEnvironment

Set defaultEnvironment: "test" in the root of your config to skip --env test in every command. Tools will fail explicitly if they detect an implicit prod access for safety.

Credential Guard

The guard blocks agents from accessing sensitive files and leaking secrets. It's configured via the credentialGuard section in agent-tools.json5.

What it blocks:

Reads of secret files (.env, .pem, .key, .ssh/, etc.)
Writes containing detected secrets (API keys, tokens, passwords)
Dangerous shell patterns (printenv, cat .env, etc.)
Direct CLI usage (gh, kubectl, psql, az) — must use wrapper tools
Authentication

Each tool uses its own auth — no unified token store:

Tool	Auth
gh-tool	gh auth login or GITHUB_TOKEN env var
observability-tool	Grafana URL from config plus optional token from tokenEnvVar
k8s-tool	Existing kubectl context (kubeconfig)
az-tool	az login session
db-tool	Env var defined by passwordEnvVar in config
logs-tool	No auth — local files or via k8s-tool for remote access
Weekly Installs
27
Repository
blogic-cz/agent-tools
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn