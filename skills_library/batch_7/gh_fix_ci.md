---
title: gh-fix-ci
url: https://skills.sh/openai/skills/gh-fix-ci
---

# gh-fix-ci

skills/openai/skills/gh-fix-ci
gh-fix-ci
Installation
$ npx skills add https://github.com/openai/skills --skill gh-fix-ci
Summary

Debug and fix failing GitHub Actions checks in pull requests using gh CLI inspection and log analysis.

Inspects PR checks via GitHub CLI, fetches GitHub Actions logs, and summarizes failure context with actionable log snippets
Requires prior gh authentication with repo and workflow scopes; verifies status before proceeding
Drafts a fix plan (using create-plan skill if available, otherwise inline) and implements only after explicit user approval
Treats external CI providers (Buildkite, etc.) as out of scope; reports only their details URLs
Includes bundled Python script for automated check inspection with JSON output and configurable log line limits
SKILL.md
Gh Pr Checks Plan Fix
Overview

Use gh to locate failing PR checks, fetch GitHub Actions logs for actionable failures, summarize the failure snippet, then propose a fix plan and implement after explicit approval.

If a plan-oriented skill (for example create-plan) is available, use it; otherwise draft a concise plan inline and request approval before implementing.

Prereq: authenticate with the standard GitHub CLI once (for example, run gh auth login), then confirm with gh auth status (repo + workflow scopes are typically required).

Inputs
repo: path inside the repo (default .)
pr: PR number or URL (optional; defaults to current branch PR)
gh authentication for the repo host
Quick start
python "<path-to-skill>/scripts/inspect_pr_checks.py" --repo "." --pr "<number-or-url>"
Add --json if you want machine-friendly output for summarization.
Workflow
Verify gh authentication.
Run gh auth status in the repo.
If unauthenticated, ask the user to run gh auth login (ensuring repo + workflow scopes) before proceeding.
Resolve the PR.
Prefer the current branch PR: gh pr view --json number,url.
If the user provides a PR number or URL, use that directly.
Inspect failing checks (GitHub Actions only).
Preferred: run the bundled script (handles gh field drift and job-log fallbacks):
python "<path-to-skill>/scripts/inspect_pr_checks.py" --repo "." --pr "<number-or-url>"
Add --json for machine-friendly output.
Manual fallback:
gh pr checks <pr> --json name,state,bucket,link,startedAt,completedAt,workflow
If a field is rejected, rerun with the available fields reported by gh.
For each failing check, extract the run id from detailsUrl and run:
gh run view <run_id> --json name,workflowName,conclusion,status,url,event,headBranch,headSha
gh run view <run_id> --log
If the run log says it is still in progress, fetch job logs directly:
gh api "/repos/<owner>/<repo>/actions/jobs/<job_id>/logs" > "<path>"
Scope non-GitHub Actions checks.
If detailsUrl is not a GitHub Actions run, label it as external and only report the URL.
Do not attempt Buildkite or other providers; keep the workflow lean.
Summarize failures for the user.
Provide the failing check name, run URL (if any), and a concise log snippet.
Call out missing logs explicitly.
Create a plan.
Use the create-plan skill to draft a concise plan and request approval.
Implement after approval.
Apply the approved plan, summarize diffs/tests, and ask about opening a PR.
Recheck status.
After changes, suggest re-running the relevant tests and gh pr checks to confirm.
Bundled Resources
scripts/inspect_pr_checks.py

Fetch failing PR checks, pull GitHub Actions logs, and extract a failure snippet. Exits non-zero when failures remain so it can be used in automation.

Usage examples:

python "<path-to-skill>/scripts/inspect_pr_checks.py" --repo "." --pr "123"
python "<path-to-skill>/scripts/inspect_pr_checks.py" --repo "." --pr "https://github.com/org/repo/pull/123" --json
python "<path-to-skill>/scripts/inspect_pr_checks.py" --repo "." --max-lines 200 --context 40
Weekly Installs
1.3K
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn