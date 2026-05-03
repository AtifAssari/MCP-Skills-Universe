---
rating: ⭐⭐
title: paw-tools-release
url: https://skills.sh/pawbytes/skill-suites/paw-tools-release
---

# paw-tools-release

skills/pawbytes/skill-suites/paw-tools-release
paw-tools-release
Installation
$ npx skills add https://github.com/pawbytes/skill-suites --skill paw-tools-release
SKILL.md
Release Automation
Overview

This skill automates the complete release workflow: version bumping, changelog generation, git tagging, and GitHub release creation. Act as a release engineer who ensures clean, traceable releases with informative changelogs.

Args: Accepts --headless / -H for non-interactive execution, --version <semver> to specify version explicitly, --branch <name> to set allowed release branch.

Your output: A complete release with updated version files, appended changelog, git tag, and draft GitHub release.

On Activation

Load available config from {project-root}/.pawbytes/config/config.yaml and {project-root}/.pawbytes/config/config.user.yaml if present. If config is missing, continue with sensible defaults.

Extract relevant config keys:

release_default_branch (default: main)
communication_language (default: English)

Detect --headless / -H flag. If present, set {headless_mode}=true for all stages and complete the release without user interaction.

Prerequisites

Before starting, verify:

Git repository — Must be in a git repository with at least one commit
GitHub CLI — gh must be installed and authenticated for GitHub releases
Clean working tree — Abort if uncommitted changes exist (warn in headless, prompt in interactive)

If any prerequisite fails, explain what's needed and offer to help resolve.

Workflow

Load and execute stages sequentially:

Validate → ./references/01-validate.md
Version → ./references/02-version.md
Changelog → ./references/03-changelog.md
Release → ./references/04-release.md

Each stage specifies its progression condition. If a stage fails, stop and inform the user.

Key Decisions

These guide the executing agent's judgment:

Version bump logic — If user doesn't specify version, infer from conventional commits: breaking: → major, feat: → minor, fix:/others → patch. When in doubt, ask (or patch in headless).
Branch enforcement — If configured, only allow releases from that branch. In interactive mode, let user override.
First release handling — If no previous tags exist, include all commits since repository start.
Pre-release versions — Support --pre-release beta/rc/alpha flag for pre-release versions.
Output Artifacts
Artifact	Location
Updated version files	Project root (package.json, Cargo.toml, etc.)
Changelog entry	{project-root}/CHANGELOG.md
Git tag	Pushed to origin
GitHub release	Draft, ready to publish
Release report	{project-root}/.pawbytes/tools-output/releases/
Scripts
./scripts/detect_version_files.py — Finds and parses version files across project types
./scripts/parse_commits.py — Parses conventional commits for changelog grouping

Run <script> --help for usage details.

Weekly Installs
20
Repository
pawbytes/skill-suites
GitHub Stars
25
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn