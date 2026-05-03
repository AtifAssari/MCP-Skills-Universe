---
title: sharex workflow and versioning
url: https://skills.sh/sharex/xerahs/sharex-workflow-and-versioning
---

# sharex workflow and versioning

skills/sharex/xerahs/ShareX Workflow and Versioning
ShareX Workflow and Versioning
Installation
$ npx skills add https://github.com/sharex/xerahs --skill 'ShareX Workflow and Versioning'
SKILL.md
Scope

This file is the single source of truth for Git and versioning rules that involve:

Commit and push workflow
Commit message format
Version bump behavior
Directory.Build.props updates

This supersedes the retired docs/development/RELEASE_PROCESS.md.

Version Source Of Truth
Treat the root Directory.Build.props file as the working XerahS app version source of truth.
Before any versioned XerahS commit, compare the root version with the highest existing XerahS git tag.
If the root version is not strictly greater than the latest tag, bump the root version first so the branch carries the next unreleased version.
Never set version numbers in individual .csproj files.
When bumping version, update every tracked Directory.Build.props in the repository that intentionally carries the XerahS app version so values match.
Derived release metadata files, such as build/windows/chocolatey/xerahs.nuspec, must be synchronized from the root version during release automation.
Tagged releases also generate and smoke-test the Chocolatey .nupkg, so release metadata under build/windows/chocolatey/ must stay automation-friendly.
Version Bump Policy
Bug fix: increment patch only (0.0.z rule: keep major/minor, increase z).
New feature: increment minor and reset patch.
Breaking change: increment major and reset minor/patch.
Required Pre-Commit Checks

Before committing and pushing:

git pull --recurse-submodules
git submodule update --init --recursive
dotnet build src/desktop/XerahS.sln


Only continue when build succeeds with 0 errors.

Commit And Push Procedure
Stage changes:
git add .

Commit using:
git commit -m "[vX.Y.Z] [Type] concise description"

Push:
git push

Commit Message Rules
Prefix XerahS app commits with the root Directory.Build.props <Version> as [vX.Y.Z], but only after verifying that version is strictly greater than the highest existing XerahS git tag.
Never use a version prefix that is lower than or equal to the latest tag. If the latest tag is already at or above the root version, bump Directory.Build.props first and then commit with that bumped version.
Include a type token such as [Fix], [Feature], [Build], [Docs], [Refactor].
Keep the description concise and specific.
Submodule-only commits in shared libraries (e.g. ShareX.ImageEditor): omit [vX.Y.Z]; use [Type] description per AGENTS.md.
Git Hook Expectations
Keep .githooks active (git config core.hooksPath .githooks).
Do not bypass hooks with --no-verify unless explicitly requested for emergency use.
If hooks fail, fix issues and recommit.
Documentation And Git
Commit Markdown documentation changes with related code/config changes.
Do not leave generated instruction docs uncommitted when they are part of the requested work.
Weekly Installs
–
Repository
sharex/xerahs
GitHub Stars
239
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass