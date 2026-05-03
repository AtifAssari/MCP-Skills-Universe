---
title: groove-admin-update
url: https://skills.sh/andreadellacorte/groove/groove-admin-update
---

# groove-admin-update

skills/andreadellacorte/groove/groove-admin-update
groove-admin-update
Installation
$ npx skills add https://github.com/andreadellacorte/groove --skill groove-admin-update
SKILL.md
groove-admin-update

Maintainers (andreadellacorte/groove repo): After publishing a new GitHub Release, run this from the groove repo root so checked-in .agents/skills/groove* matches what npx skills add andreadellacorte/groove installs — see CONTRIBUTING.md (“Publish release”). Do not use manual rsync from skills/ for that.

Outcome

All pending migrations are applied to the user's local groove state in version order. .groove/index.md reflects the current installed groove version.

Acceptance Criteria
groove-version: in .groove/index.md matches version: in skills/groove/SKILL.md after update
Each pending migration was applied in order
groove-version: updated after each successful migration (partial progress is recoverable)
If already up to date, reports clearly and exits
Source-of-truth check: "up to date" is only reported when the installed skill version equals the latest GitHub release; if the add step left an older version on disk (e.g. cached or default branch), the user is warned and told how to fix it
Steps
Fetch latest release tag from https://api.github.com/repos/andreadellacorte/groove/releases/latest (tag_name, strip leading v). This is the target version. If the API call fails, skip the version check and continue without a target.
Install with retry: Run npx skills add andreadellacorte/groove --yes (no @tag — the CLI does not support tag syntax). After it completes, read version: from skills/groove/SKILL.md and compare to the target. If the installed version is still older than the target, wait 10 seconds and retry npx skills add andreadellacorte/groove --yes. Repeat up to 3 times total. If all attempts fail to install the target version, report: "Installed v but latest release is v — npx skills add may be caching an older version. Try again later." and exit.
After a successful install, re-read this SKILL.md (skills/groove-admin-update/SKILL.md) from disk before continuing — the skill refresh may have updated the update command itself, and the remainder of these steps must reflect the latest version
Read groove-version: from .groove/index.md — if key absent, assume 0.1.0 and write it
Read installed version from version: in skills/groove/SKILL.md (already confirmed to match target in step 2)
If local and installed versions match: report "groove is up to date (v)" and exit
Read skills/groove/migrations/index.md — parse the migration table
Filter rows where To > local version AND To <= installed version, in table order — the From field is informational only and does not gate execution
If no migrations found but versions differ: update groove-version: in .groove/index.md directly to the installed version and report "no state migrations needed — version bumped to v"
For each pending migration: a. Report "Applying → : " b. Read and execute the migration file c. Update groove-version: in .groove/index.md to the To version d. Report "✓ → applied"
Report summary: N migrations applied, now at v
Re-sync platform symlinks after update:
For each directory in .agents/skills/ that starts with groove:
Ensure .claude/skills/<name> is a symlink → ../../.agents/skills/<name> (create or update if stale)
Ensure .cursor/skills/<name> is a symlink → ../../.agents/skills/<name> if .cursor/skills/ exists
Remove any .claude/skills/groove-* or .cursor/skills/groove-* entries that no longer exist in .agents/skills/ (stale symlinks from removed skills)
Run: for skill in .agents/skills/groove*; do name=$(basename "$skill"); ln -sfn "../../.agents/skills/$name" ".claude/skills/$name"; done
Use ln -sfn (no-dereference) to avoid creating nested symlinks inside existing directory symlinks
Report: "✓ platform symlinks refreshed"
Constraints
Source of truth for "latest" is GitHub releases — npx skills add can cache older versions. Step 1-2 fetches the latest release tag and retries installation up to 3 times to ensure the correct version is installed.
Never skip a migration — apply every matching migration in table order even if From does not match local version exactly
Update groove-version: after each individual migration, not only at the end
If a migration fails: stop, report the failure and current version, do not continue
Do not modify skill files — npx skills update handles that; this command only migrates local state
Local state includes: .groove/index.md config keys, memory directory structure, AGENTS.md sections
Each migration file is idempotent — if re-run after partial failure, it should be safe
Weekly Installs
206
Repository
andreadellacorte/groove
GitHub Stars
5
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn