---
title: cli-forge-publish
url: https://skills.sh/bytelandtechnology/cli-forge/cli-forge-publish
---

# cli-forge-publish

skills/bytelandtechnology/cli-forge/cli-forge-publish
cli-forge-publish
Installation
$ npx skills add https://github.com/bytelandtechnology/cli-forge --skill cli-forge-publish
SKILL.md
cli-forge Publish

Use this stage when a compliant generated CLI skill needs to adopt standard release automation, prepare a new version, or execute the paired GitHub Release + multi-package npm publication flow.

Purpose

Manage the release pipeline for a generated cli-forge skill.

This stage owns the bootstrap + production publication flow:

a required local prepublish step for the main package plus all platform packages
the paired repo-native GitHub Release plus platform-split npm publication from the later semantic-release event

One production release produces:

git tag v<version> + GitHub Release (archive + sha256 per target)
6 per-platform npm packages (<pkg>-darwin-arm64 / -darwin-x64 / -linux-arm64 / -linux-x64 / -win32-arm64 / -win32-x64) carrying the native binaries
1 main npm package (JS shim, optionalDependencies pinned to the same version)
CHANGELOG.md entry + chore(release): <version> [skip ci] commit

All npm packages publish in one semantic-release run and share the version with the git tag + GitHub Release. The total count is 1 + config.targets.length (default: 7).

Canonical References
./instructions/release/skill-release-runbook.md
./planning-brief.md
./shared-planning-brief.md
./contracts/release-receipt.yml.tpl
./templates/
Entry Gate
#	Check	Source
1	validation-report.yml exists, is fresh, and result == compliant or warning	Validate
2	Target repository path is explicitly known	Router / User
3	Requested publish mode is explicit	Router / User
4	npm package naming contract, CLI name, and scope decisions are explicit	User

Scope decisions are required inputs at this stage. Collect the main package name plus the scope policy for both the main package and the platform packages. The main package and platform packages may use different scopes, but platform names must still derive from the main package body plus -<target-suffix>.

Required Inputs
Validation outcome plus provenance snapshot (refusal to publish if non_compliant, stale, or provenance-mismatched)
Publish mode: report_only, dry_run, prepublish, or live_release
Source project path
cliName — the CLI binary name
mainPackageName — the main npm package name (with scope prefix if scoped)
mainNpmScope — null for unscoped, or the scope string for the main package
platformNpmScope — null for unscoped platform packages, or a separate scope string
sourceRepository — owner/repo on GitHub
Workflow
Read ./planning-brief.md for publish-specific planning constraints.
Accept the inbound validation-report.yml. Refuse to proceed if validation failed; do not re-run validation here.
Verify validation freshness before any publish-mode action:
compare the current .cli-forge/design-contract.yml, .cli-forge/cli-plan.yml, baseline receipt (scaffold-receipt.yml or takeover-receipt.yml), and optional extend-receipt.yml against the provenance snapshot recorded in validation-report.yml
for takeover-adopted baselines, require the report provenance to match the current adopted contract + receipt set exactly; do not rely only on the aggregate validation result
if any required baseline artifact is missing, has a different receipt, or takeover recorded contract/baseline rewrites after validation, stop and route back to Validate
Ask the user for the inputs listed above if not already collected. If the mode is report_only, skip to step 7.
If the skill project lacks the release automation assets, adopt them by copying the contents of ./templates/ to the project root while restoring the install-safe dot-* resource aliases to their real dot-prefixed target paths (dot-releaserc.json -> .releaserc.json, dot-github/ -> .github/, npm/platforms/dot-gitkeep -> .gitkeep). The adopted asset pack does NOT contain Scaffold-stage source templates (*.tpl).
Fill release/config.json and npm/main/package.json with the collected inputs. release/config.json must explicitly record mainPackageName, mainNpmScope, and platformNpmScope.
Verify the target repository has:
GitHub Actions enabled on a GitHub-hosted runner with id-token: write
npm trusted publishing configured on npmjs.com for the main package and for each of the 6 platform packages, every entry pointing at release.yml
Follow the mode path defined in ./instructions/release/skill-release-runbook.md:
report_only: audit readiness only. Read config and repository state, report blockers and next actions. Do NOT copy files, fill placeholders, or alter the repository in any way.
dry_run: run npm run release:rehearse locally. This builds every target, syncs platform packages, and runs npm publish --dry-run for each. No tag, no GitHub Release, no real npm publication.
prepublish: run npm run release:prepublish locally. This performs a real public npm bootstrap publish for every platform package and the main package using a dedicated bootstrap prerelease version. If local auth is missing, pause for interactive npm login, surface the verification URL, and continue only after the user completes browser verification.
live_release: push to main (or workflow_dispatch) so the target repository's .github/workflows/release.yml, restored from the installer-safe asset-pack resource dot-github/workflows/release.yml, drives the end-to-end run. Do not proceed to live_release until prepublish bootstrap has completed for the configured package set.
Generate .cli-forge/release-receipt.yml from the template at ./contracts/release-receipt.yml.tpl.
Outputs
A verified prepublish bootstrap for 1 main + N platform npm packages (if prepublish)
A verified GitHub Release with archives + checksums (if live_release)
1 main + N platform npm packages published at the same production version (if live_release)
Updated CHANGELOG.md and release commit on main
.cli-forge/release-receipt.yml
Exit Gate
#	Check
1	The requested mode was executed
2	For report_only: no files were written to the target repository
3	For dry_run / prepublish / live_release: asset pack adopted and filled
4	For prepublish: the bootstrap npm prerelease completed without creating a tag or GitHub Release
5	For live_release: version, tag, main package, platform packages agree
6	release-receipt.yml generated
Guardrails
All npm packages (main + platforms) MUST share the version chosen by semantic-release. The two release scripts enforce this by consuming ${nextRelease.version} from semantic-release hooks.
The bootstrap prepublish step MUST use a dedicated prerelease version such as 0.0.0-prepublish.N. It is not a production release.
Main and platform packages may differ only by scope. Do not introduce arbitrary per-platform package base names.
Do not bypass stale validation. If the codebase changed since the last validation report, route back to Validate.
For takeover-adopted repositories, freshness checks MUST verify provenance against the current contract + receipt set, not just validation-report.yml aggregate status or timestamp.
Do not hand-bump npm/main/package.json#version, hand-edit CHANGELOG.md release entries, or create tags outside semantic-release.
Interactive npm login guidance belongs only to local prepublish. Production CI publication must continue to rely on trusted publishing.
Do not leave dot-* alias names in the target repository. Those names exist only inside this skill package so .agents installers preserve the assets.
The asset pack's npm/platforms/ directory is generated at release time. Do not check generated platform package directories into source control beyond the .gitkeep placeholder.
Next Step

This is a terminal stage.

Weekly Installs
33
Repository
bytelandtechnol…li-forge
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn