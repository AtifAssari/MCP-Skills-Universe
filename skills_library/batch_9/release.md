---
title: release
url: https://skills.sh/s-hiraoku/synapse-a2a/release
---

# release

skills/s-hiraoku/synapse-a2a/release
release
Installation
$ npx skills add https://github.com/s-hiraoku/synapse-a2a --skill release
SKILL.md
Release Version Update

This skill updates the project version, plugin version, and changelog.

Usage
/release [version-type-or-number] [description]

Version Types
patch - Increment patch version (e.g., 0.2.12 → 0.2.13)
minor - Increment minor version (e.g., 0.2.12 → 0.3.0)
major - Increment major version (e.g., 0.2.12 → 1.0.0)
X.Y.Z - Set specific version (e.g., 1.0.0)
Version Type is Optional — Auto-detect from Conventional Commits

If the version type is omitted, auto-detect the bump level from commits since the latest tag using the standard Semantic Versioning + Conventional Commits mapping:

major — any commit contains BREAKING CHANGE: in the body or ! before the colon in the subject (e.g. feat!:, refactor(core)!:).
minor — otherwise, at least one feat: (or feat(scope):) commit.
patch — otherwise (fixes, chores, docs, etc.).

Procedure:

git describe --tags --abbrev=0 → latest tag. If this command exits non-zero because the repository has no tags yet, fall back to the full history: git log HEAD --pretty=%H%x00%s%x00%b (initial commit → HEAD) and treat every commit as "unreleased".
Otherwise git log <tag>..HEAD --pretty=%H%x00%s%x00%b → commits to classify. (NUL-separated fields keep multi-line bodies parseable.)
If the range is empty, abort with No commits since <tag>; nothing to release.
Print the detected bump type with a one-line commit count summary, then continue with the normal bump flow. Do not prompt for confirmation — this keeps non-interactive workflows like post-impl-codex unblocked.

Explicit argument always wins. If the user passes patch/minor/major/X.Y.Z, skip auto-detection entirely.

Description (Optional)

If provided, use as the changelog entry description. Otherwise, analyze recent commits to generate the changelog.

Workflow
Step 1: Read Current Version

Read pyproject.toml and extract current version:

# Look for: version = "X.Y.Z"

Step 2: Calculate New Version

Based on the version type:

patch: major.minor.patch → major.minor.(patch+1)
minor: major.minor.patch → major.(minor+1).0
major: major.minor.patch → (major+1).0.0
specific: Use the provided version directly

Validate the new version is greater than current (unless forced).

Step 3: Update pyproject.toml

Edit pyproject.toml:

version = "NEW_VERSION"

Step 3.5: Update plugin.json

Edit plugins/synapse-a2a/.claude-plugin/plugin.json:

"version": "NEW_VERSION",


Important: Keep plugin version in sync with pyproject.toml version.

Step 3.6: Update site-docs version references

Update hardcoded version strings in GitHub Pages documentation:

site-docs/getting-started/installation.md — version example in verification section:

You should see the version number (e.g., `NEW_VERSION`).


site-docs/concepts/a2a-protocol.md — Agent Card JSON example:

"version": "NEW_VERSION",


site-docs/changelog.md — add new version entry at the top of "Recent Highlights" (only if CHANGELOG.md was updated in Step 4-5).

mkdocs.yml — repo_name includes version displayed in GitHub Pages header:

repo_name: s-hiraoku/synapse-a2a vNEW_VERSION


Important: Keep site-docs version in sync with pyproject.toml version.

Step 4: Generate Changelog with git-cliff

Use git-cliff to automatically generate the changelog entry from Conventional Commits:

# Preview the generated changelog
python scripts/generate_changelog.py --unreleased --tag vNEW_VERSION --dry-run

# Write to CHANGELOG.md
python scripts/generate_changelog.py --unreleased --tag vNEW_VERSION

Step 5: Review and Adjust CHANGELOG.md

Review the generated entry and make manual adjustments if needed:

Reword entries for clarity
Add context or PR references if missing
Remove noise entries that slipped through filters
Ensure the date is correct: ## [NEW_VERSION] - YYYY-MM-DD

If no git-cliff is available, or for a manual override, write the entry directly using Keep a Changelog format (see below).

Step 6: Report Results

Display:

Old version → New version
Changelog entry preview
Files modified
Examples
Bump patch version
/release patch

Bump minor version with description
/release minor "Add new authentication system"

Bump major version
/release major

Set specific version
/release 1.0.0

Shorthand
/version patch    # Same as /release patch

File Locations
Version: pyproject.toml (line with version = "...")
Plugin Version: plugins/synapse-a2a/.claude-plugin/plugin.json (line with "version": "...")
Site Docs Version: site-docs/getting-started/installation.md, site-docs/concepts/a2a-protocol.md
Site Header Version: mkdocs.yml (repo_name field)
Changelog: CHANGELOG.md
Site Docs Changelog: site-docs/changelog.md
Changelog Format

Follow Keep a Changelog format:

## [X.Y.Z] - YYYY-MM-DD

### Added
- New features

### Changed
- Changes in existing functionality

### Fixed
- Bug fixes

### Removed
- Removed features

### Documentation
- Documentation updates

### Tests
- Test updates


Only include sections that have entries. Order sections as shown above.

Weekly Installs
64
Repository
s-hiraoku/synapse-a2a
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass