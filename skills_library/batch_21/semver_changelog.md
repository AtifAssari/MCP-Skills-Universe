---
title: semver-changelog
url: https://skills.sh/prulloac/agent-skills/semver-changelog
---

# semver-changelog

skills/prulloac/agent-skills/semver-changelog
semver-changelog
Installation
$ npx skills add https://github.com/prulloac/agent-skills --skill semver-changelog
SKILL.md
Semver Changelog

This skill guides the agent through identifying released versions, analyzing git history, and documenting changes in a standard format.

Overview

A consistent changelog helps users and contributors understand what has changed between versions. This skill ensures that CHANGELOG.md follows the Keep a Changelog format and adheres to Semantic Versioning.

Workflow

Follow these steps to update or create the changelog:

1. Identify Latest Released Tag

Find the most recent git tag that follows Semantic Versioning (e.g., v1.2.3 or 1.2.3).

Use git tag -l --sort=-v:refname to list tags in version order.
Filter for tags that match the v?MAJOR.MINOR.PATCH pattern.
2. Analyze Changes

Compare the current HEAD with the identified latest tag to see what has changed.

Run git diff <latest_tag>..HEAD to see code changes.
Run git log <latest_tag>..HEAD --oneline to see commit messages.
3. Group and Categorize Changes

Group the identified changes into the following categories:

Added: New features.
Changed: Changes in existing functionality.
Deprecated: Soon-to-be removed features.
Removed: Now removed features.
Fixed: Bug fixes.
Security: Security vulnerability fixes.
4. Update CHANGELOG.md

Update the CHANGELOG.md file at the repository root.

If it doesn't exist, create it using the standard header.
Add an [Unreleased] section if it doesn't exist, or update the existing one with the new changes.
Ensure the file follows the "Keep a Changelog" structure.
Guidelines
Refer to references/semver_reference.md for detailed formatting and versioning rules.
Always check the repository root for an existing CHANGELOG.md before creating a new one.
Use the [Unreleased] section for changes that haven't been tagged yet.
Examples
Initializing a Changelog

If no changelog exists:

Create CHANGELOG.md.
Add the standard "Keep a Changelog" header.
Identify all tags and their changes to build the history, or start from the latest tag.
Validation

After updating or creating the changelog, verify the following:

File Existence: Ensure CHANGELOG.md exists at the repository root.
Format: Check that the file includes the required header and that new changes are correctly categorized under the appropriate heading (e.g., ### Added).
Links: If the file uses links at the bottom for versions, ensure they point to valid git comparison URLs (if applicable).
SemVer: Ensure the version numbers used follow the SemVer specification.
Example Output

When reporting the update to the user, you can use a format like this:

Changelog Update Summary
Category	Changes Identified
Added	- New API endpoint for users
Fixed	- Bug in authentication logic
Security	- Updated dependencies to patch CVE-2023-XXXX

Latest Version: [1.1.0] Previous Version: [1.0.0]

Weekly Installs
20
Repository
prulloac/agent-skills
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass