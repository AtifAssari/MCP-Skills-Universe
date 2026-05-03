---
title: github-cli
url: https://skills.sh/hairyf/skills/github-cli
---

# github-cli

skills/hairyf/skills/github-cli
github-cli
Installation
$ npx skills add https://github.com/hairyf/skills --skill github-cli
SKILL.md
GitHub CLI (gh)

Use this skill when working with GitHub from the command line: repos, issues, PRs, Actions, projects, releases, gists, codespaces, search, secrets, and API. Content is based on gh 2.85.0 (January 2026).

Core References
Topic	Description	Reference
CLI Structure	Full command tree for discovery	core-cli-structure
Install & Verify	Install on macOS, Linux, Windows; verify	core-install
Auth & Config	Login, token, config, env vars, browse, global flags, JSON/template output	core-auth-config
Repos, Issues, PRs	Create/list/view/edit repo, issue, PR; merge, review, checkout	core-repo-issues-prs
Repo Extras	Autolinks, deploy keys, gitignore/license, rename, archive	core-repo-extras
Issue & PR Advanced	Status, pin, lock, transfer, delete, review types, merge options	core-issue-pr-advanced
Features
Actions & Secrets
Topic	Description	Reference
Runs, Workflows, Cache	List/watch/rerun/delete runs, run workflows, manage caches	features-actions-secrets
Secrets & Variables	Repository, environment, org secrets/variables	features-actions-secrets
Projects, Releases & More
Topic	Description	Reference
Projects	Fields, items, link/unlink, copy, mark-template	features-projects-releases-gists
Releases	Create, upload, download, verify, verify-asset	features-projects-releases-gists
Gists & Codespaces	Gist rename/multi-file; codespace cp, jupyter, logs, ports	features-projects-releases-gists
Orgs	List, view, JSON output	features-projects-releases-gists
Preview & Agent Tasks	gh preview, gh agent-task	features-preview-agent-task
Search, API, Misc	Search, labels, SSH/GPG keys, gh api, aliases, extensions, rulesets, attestation	features-search-api-misc
Best Practices
Topic	Description	Reference
Environment Setup	Shell completion, aliases, git credential helper	best-practices-workflows
Workflows & Practices	Automation tips, bulk ops, repo setup, CI/CD, fork sync, help	best-practices-workflows
Quick Tips
Use GH_TOKEN and GH_REPO for non-interactive use.
Prefer --json + --jq for scripting.
Use gh repo set-default owner/repo to avoid repeating --repo.
Weekly Installs
76
Repository
hairyf/skills
GitHub Stars
15
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn