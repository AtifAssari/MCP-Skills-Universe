---
title: release-notes
url: https://skills.sh/jmerta/codex-skills/release-notes
---

# release-notes

skills/jmerta/codex-skills/release-notes
release-notes
Installation
$ npx skills add https://github.com/jmerta/codex-skills --skill release-notes
SKILL.md
Release notes
Goal

Produce accurate, scannable release notes (Markdown) for a specific release range.

Inputs to ask for (if missing)
Release version + date (or "unreleased").
Range to summarize: from_ref..to_ref (tags/SHAs/branches). If unknown, ask: "last release tag?" and "target branch/tag?"
Target audience: end users, developers, internal ops, or all.
What to include/exclude: internal refactors, dependency bumps, infra-only changes.
Workflow (checklist)
Determine the release range
Prefer tags: pick the previous tag and the new tag/HEAD.
If no tags: use the last release branch point or a date-based window.
Commands to gather candidates:
git tag --sort=-creatordate | Select-Object -First 20
git log --first-parent --oneline <from_ref>..<to_ref>
If GitHub CLI is available: list merged PRs for the range and use titles for grouping.
Collect and categorize changes
Start from merge commits (first-parent) to avoid noise.
Categorize into: Highlights, Breaking changes, Features, Fixes, Performance, Security, Deprecations, Docs, Dependencies, Infra/ops.
Flag anything requiring action: config changes, env vars, DB migrations, API contract changes.
Identify breaking changes and upgrade steps
Look for: renamed/removed endpoints, changed request/response fields, changed config keys, Java/Kotlin/Node version bumps, DB schema changes.
Add explicit "Upgrade" and "Rollback" notes when impact is non-trivial.
Write release notes using the template
Use short bullets, active voice, and user-facing wording.
Prefer "what changed" + "why it matters" over implementation details.
Include PR/issue references only if they are stable in your repo hosting.
Use references/release-notes-template.md to keep structure consistent.
Sanity check for omissions and accuracy
Diff the range: git diff --stat <from_ref>..<to_ref>
Scan for config/migrations: rg -n \"ENV|config|migration|Flyway|Liquibase\" -S
Ensure breaking changes are called out and have upgrade steps.
Deliverable

Provide:

Release notes Markdown (ready to paste into a GitHub Release / changelog).
A short "Risk/notes" section listing any required migrations, config changes, or rollback concerns.
Weekly Installs
29
Repository
jmerta/codex-skills
GitHub Stars
126
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass