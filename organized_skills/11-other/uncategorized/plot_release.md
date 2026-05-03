---
rating: ⭐⭐⭐
title: plot-release
url: https://skills.sh/eins78/skills/plot-release
---

# plot-release

skills/eins78/skills/plot-release
plot-release
Installation
$ npx skills add https://github.com/eins78/skills --skill plot-release
SKILL.md
Plot: Cut a Release

Create a versioned release from delivered plans. This workflow can be run manually (using git and forge CLI), by an AI agent interpreting this skill, or via a workflow script (once available).

Input: $ARGUMENTS is optional. Can be:

rc — cut a release candidate tag and generate a verification checklist
A version number (e.g., 1.2.0) or bump type (major, minor, patch) — cut the final release

Examples: /plot-release rc, /plot-release minor, /plot-release 1.2.0

Setup

Add a ## Plot Config section to the adopting project's CLAUDE.md:

## Plot Config
- **Project board:** <your-project-name> (#<number>)  <!-- optional, for `gh pr edit --add-project` -->
- **Branch prefixes:** idea/, feature/, bug/, docs/, infra/
- **Plan directory:** docs/plans/
- **Active index:** docs/plans/active/
- **Delivered index:** docs/plans/delivered/

Model Guidance
Steps	Min. Tier	Notes
1. Determine Version	Mid	Heuristic: plan types → bump suggestion
2A. RC Path	Small	Git tag, template generation
2B. Release Notes	Mid	Discovery logic, changelog collection
3. Cross-check Notes	Frontier (orchestrator) + Small (subagents)	Orchestrator compares; small subagents can gather commit messages and plan changelogs in parallel
4-6. Next Steps through Summary	Small	Template list, no-ops, formatting
1. Determine Version

Check for the latest git tag:

git tag --sort=-v:refname | head -1


If $ARGUMENTS is rc:

Determine the target version (same rules as below — check delivered plans, suggest bump type)
Check for existing RC tags for this version: git tag --list "v<version>-rc.*"
Next RC number: if no existing RCs, use rc.1; otherwise increment
Proceed to step 2A (RC path)

If $ARGUMENTS specifies a version (e.g., 1.2.0):

Use it directly (validate it's valid semver)
Proceed to step 2B (final release path)

If $ARGUMENTS specifies a bump type (major, minor, patch):

Calculate the new version from the latest tag
Proceed to step 2B (final release path)

If $ARGUMENTS is empty:

Check if there's an open RC checklist (docs/releases/v*-checklist.md) with all items checked
If yes: propose cutting the final release for that version
If no: look at delivered plans since the last release to suggest a bump type:
Any features → suggest minor
Only bug fixes → suggest patch
Breaking changes noted in changelogs → suggest major
If unable to determine bump type from plan metadata, ask the user to specify the version directly
Propose the version and confirm with the user

Smaller models: Skip the automatic bump type suggestion. Instead, list the delivered plans with their types and ask the user: "What version should this release be? (major/minor/patch or exact version)" Let the human decide.

2A. RC Path — Cut Release Candidate

Tag the RC:

git tag -a v<version>-rc.<n> -m "Release candidate v<version>-rc.<n>"
git push origin v<version>-rc.<n>


Generate verification checklist:

Collect all delivered plans since the last release (via docs/plans/delivered/ — check the Delivered date in each plan's Status section against the last release tag date). For each delivered feature or bug plan, extract the ## Changelog section and create a checklist item. If a plan has a Sprint: <name> field, include the sprint name alongside the checklist item for context. Sprint completion is informational — it does not block the release.

mkdir -p docs/releases


Write docs/releases/v<version>-checklist.md:

# Release Checklist — v<version>

RC: v<version>-rc.<n> (YYYY-MM-DD)

## Verification

- [ ] <feature/bug slug> — <changelog summary>
- [ ] <feature/bug slug> — <changelog summary>

## Automated Tests

- [ ] CI passes on RC tag

## Sign-off

- [ ] All items verified by: ___
- [ ] Final release approved by: ___

git add docs/releases/v<version>-checklist.md
git commit -m "release: v<version>-rc.<n> checklist"
git push


Summary (RC):

RC tag: v<version>-rc.<n>
Checklist: docs/releases/v<version>-checklist.md
Plans included: list of slugs
Progress: [ ] Draft > [ ] Approved > [x] Delivered > [*] Released (RC)
Suggested next actions:
Test against the checklist items
If bugs found: fix via bug/ branches, merge, then /plot-release rc for next RC
When all items pass: /plot-release to cut the final release
2B. Final Release Path — Generate Release Notes

Check for project-specific release note tooling, then either run it or fall back to manual collection.

Discover tooling — check in this order:

Changesets: Does .changeset/config.json exist? If so, the project uses @changesets/cli.
Project rules: Read CLAUDE.md and AGENTS.md for release note instructions (e.g., custom scripts, specific commands).
Custom scripts: Check package.json for release-related scripts (e.g., release, version, changelog).

If tooling is found: remind the user to run it (e.g., pnpm exec changeset version for changesets). Do not run release tooling automatically — the user controls when and how versions are bumped. Then proceed to step 3 (cross-check).

If no tooling is found: collect changelog entries from delivered plans and present them to the user:

# Get the date of the last release tag (exclude RC tags)
LAST_TAG=$(git tag --sort=-v:refname | grep -v '\-rc\.' | head -1)
if [ -n "$LAST_TAG" ]; then
  LAST_RELEASE_DATE=$(git log -1 --format=%ai "$LAST_TAG" | cut -d' ' -f1)
else
  LAST_RELEASE_DATE="1970-01-01"
fi

# Find delivered plans newer than the last release
ls docs/plans/delivered/ 2>/dev/null


For each delivered plan since the last release:

Read the ## Changelog section
Read the ## Status section for the Type (feature/bug/docs/infra)
Collect the changelog entries

Only include feature and bug plans in the release notes (docs/infra are live when merged — they don't need release).

Present the collected entries to the user and suggest they add them to CHANGELOG.md. Do not write to CHANGELOG.md directly.

3. Cross-check Release Notes

Model tiers for this step:

Frontier (e.g., Opus): Full cross-check — compare changelog entries against delivered plans and commit messages. Can delegate data gathering (reading plans, collecting commit messages) to small subagents. Flag significant gaps (missing features, phantom entries). Don't nitpick wording.
Mid (e.g., Sonnet): Compare changelog entry count against delivered plan count. Can delegate plan reading to small subagents. Flag obvious mismatches (plan with no corresponding entry, entry with no corresponding plan). Skip semantic content comparison.
Small (e.g., Haiku): Skip gap detection. Present the generated release notes and ask: "Do these release notes look complete?" Human review is the final gate.

Whether generated by tooling or manually constructed, compare the changelog against the actual work:

Collect the list of delivered plans and commit messages since the last tag
Compare against the generated changelog entries
Only flag significant gaps or errors — e.g., a delivered feature completely missing from the changelog, or a changelog entry that doesn't match any actual work
Don't nitpick wording or minor omissions — offer improvements only if there are clear, meaningful gaps
If gaps are found, show them to the user and ask whether to fix before proceeding

This cross-check is the primary value of /plot-release — verifying that release notes accurately reflect delivered work.

4. Recommended Next Steps

Present a numbered list of actions for the user to confirm:

Update CHANGELOG.md with the collected entries (if not already done by tooling)
Bump version in package.json (if applicable): pnpm version <version> --no-git-tag-version
Commit: git commit -am "release: v<version>"
Tag: git tag -a v<version> -m "Release v<version>"
Push: git push origin main && git push origin v<version>

Offer to execute these steps only if the user confirms. Do not run them automatically.

5. Clean Up RC Artifacts

If RC tags exist for this version, they remain in git history (don't delete them — they're part of the release record). The checklist file at docs/releases/v<version>-checklist.md stays committed as documentation of what was verified.

6. Summary

Print:

Version: v<version>
Plans included:
<slug> —
<slug> —
Cross-check result: complete / gaps found
RC iterations: (if any)
Progress: [ ] Draft > [ ] Approved > [ ] Delivered > [x] Released
Status: what remains to be done (version bump, tag, push, etc.)
Suggested next actions:
If version bump/tag/push still needed: follow the steps from step 4
Run /plot to verify clean state
Start next cycle: /plot-idea or /plot-sprint
Weekly Installs
17
Repository
eins78/skills
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass