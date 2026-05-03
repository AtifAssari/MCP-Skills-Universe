---
rating: ⭐⭐
title: github-repo
url: https://skills.sh/jdevalk/skills/github-repo
---

# github-repo

skills/jdevalk/skills/github-repo
github-repo
Installation
$ npx skills add https://github.com/jdevalk/skills --skill github-repo
SKILL.md
GitHub Repository Optimizer

This skill audits a GitHub repository against best practices and generates or improves the files that make a repo look professional, welcoming, and well-maintained. It works with live repos (via gh CLI), local git directories, or files the user provides.

Implementation recipes live in AGENTS.md — read it when you need to generate or improve specific files. This file has the workflow and audit checklist.

Workflow
Gather repo context — Determine what we're working with and collect information
Run the audit — Score every aspect of the repo's public-facing quality
Generate or improve files — Produce the files that are missing or need work. Recipes are in AGENTS.md.
Metadata and readability pass — invoke metadata-check on the repo description and README blurb; readability-check on prose-heavy files.
Verify — Confirm the outputs are correct and complete
Phase 0: Gather Context

Key information to collect: repo name, description, language/framework, README existence and quality, which community health files exist, issue/PR template status, CI/CD status, release history, branch count. Use gh CLI if authenticated, otherwise read local files.

Phase 1: Audit

Score each category out of 10. For each, give 2–4 specific findings that quote the actual state.

README Quality (x/10)

Does the README exist? Is it well-structured with: project name and clear one-liner, badge row (build/license/version), description explaining what/why/who, quick start (install + first use in 3 steps or fewer), code examples, screenshots/demos if visual, configuration docs, contributing link, license mention? Is it under 500 lines with <details> for optional content?

Repository Metadata (x/10)
Description set and useful (not blank or "My awesome project")?
Topics/tags relevant and complete?
Website URL set if applicable?
Social preview image uploaded?
"Packages", "Environments", "Deployments" sections hidden if unused?
Community Health Files (x/10)
CONTRIBUTING.md — exists? Covers dev setup, code style, testing, PR process?
SECURITY.md — exists? Directs to private reporting channel, states response time?
CODE_OF_CONDUCT.md — exists? Contributor Covenant 2.1 is the standard.
LICENSE — exists in root? Appropriate for project type?
SUPPORT.md — exists? Separates bugs from support questions?
CHANGELOG.md — follows Keep a Changelog format?

For organizations: check for a .github repository with org-wide default health files.

Issue & PR Templates (x/10)
YAML-based issue forms (.github/ISSUE_TEMPLATE/*.yml) with at least bug report and feature request? Numbered filenames for ordering?
config.yml disabling blank issues and linking external support?
PR template with description, related issues (Closes #XXX), type-of-change checkboxes, testing checklist?
CODEOWNERS file defining reviewers per directory?
CI/CD & Automation (x/10)
GitHub Actions workflows for testing, linting, building? Passing status badges in README?
Dependabot or Renovate configured?
Code quality (CodeQL, linting actions)?
Stale issue management?
Releases & Branch Hygiene (x/10)
Tagged releases with changelogs? Semantic versioning?
Stale branches cleaned up?
.gitattributes with export-ignore?
Auto-release (semantic-release or release-please)?
Phase 2: Generate or Improve Files

Based on the audit, generate the files that are missing or need improvement. Always ask before overwriting. Read AGENTS.md for detailed recipes.

File generation order by impact: README.md, LICENSE, CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md, issue templates, PR template, CHANGELOG.md, SUPPORT.md, config files (dependabot.yml, CODEOWNERS, FUNDING.yml).

AGENTS.md sections: README generation, Community health files (CONTRIBUTING, SECURITY, CODE_OF_CONDUCT), Issue templates, Organization-level setup (.github repo, org profile, private member profile, domain verification, rulesets).

Phase 2.5: Metadata and readability pass
Metadata pass — metadata-check skill. Run on the repo description (first ~100 chars show in search and profile cards) and the README's opening blurb.
Prose pass — readability-check skill. Run on every prose-heavy file — at minimum the README, plus CONTRIBUTING.md and SECURITY.md if you produced them.

Apply fixes directly. Skip for code-heavy files (issue templates, workflow YAML).

Phase 3: Verify
Verify files are in the correct locations.
Check that all internal links in the README work.
Confirm badge URLs are correctly formatted.
If gh is available, remind the user to update the repo's About section (description, topics, website URL, social preview) — these can't be set via files alone.
Summarize what was created/changed and what the user should do next.
Output format

Score table (6 categories, x/60), grouped findings quoting actual state, list of files generated/changed, and next steps for the user.

Weekly Installs
12
Repository
jdevalk/skills
GitHub Stars
48
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn