---
title: release
url: https://skills.sh/schpet/linear-cli/release
---

# release

skills/schpet/linear-cli/Release
Release
Installation
$ npx skills add https://github.com/schpet/linear-cli --skill Release
SKILL.md
Release Workflow

This skill provides a systematic workflow for creating and publishing releases for the linear-cli project. It handles changelog management, version bumping, testing, and tagging.

When to Use

Use this skill when preparing to release a new version of linear-cli. The workflow ensures all changes are documented, tests pass, and versions are properly tagged before publishing.

Prerequisites

Ensure the following tools are available:

changelog skill for changelog management
svbump for version bumping (installed)
jj for version control operations
just for running the release tasks
Release Workflow
Step 1: Review Commits Since Last Release

Determine the commits that have been made since the last release:

jj log --ignore-working-copy --git -r 'tags()..@' --no-graph


This shows all commits from the most recent tag to the current commit.

Step 2: Add Changelog Entries

For each commit identified above, evaluate whether it warrants a changelog entry. Focus on user-facing changes:

Include in changelog:

New features
Bug fixes
Breaking changes
Significant improvements
Deprecations

Exclude from changelog:

Internal refactoring without user impact
Documentation-only changes
Build/CI configuration changes
Chore commits (unless significant)

Use the changelog CLI to add entries. Use --attribute-pr with the commit SHA to automatically look up the associated PR and add attribution, excluding schpet and schpetbot:

changelog add --type <type> "<description>" --attribute-pr <commit-sha> --exclude-users schpet,schpetbot


Omit --attribute-pr for commits without an associated PR or when attribution isn't relevant.

Types match Keep a Changelog categories:

added - New features
changed - Changes in existing functionality
deprecated - Soon-to-be removed features
removed - Removed features
fixed - Bug fixes
security - Security improvements
Step 3: Verify Changelog with User

After adding all relevant changelog entries, show the unreleased section of CHANGELOG.md to the user and ask them to review it:

Read the CHANGELOG.md file
Show the [Unreleased] section
Ask: "Please review these changelog entries. Are there any changes needed before release?"
Make any requested adjustments
Step 4: Determine Semver Bump

Based on the types of changes in the changelog, determine and recommend the appropriate semantic version bump:

Major (X.0.0):

Breaking changes
Removed features
Significant API changes

Minor (0.X.0):

New features (added)
Deprecations
Backward-compatible functionality additions

Patch (0.0.X):

Bug fixes
Security fixes
Minor improvements with no new features

Present the recommendation to the user:

Based on the changelog entries, I recommend a <MAJOR/MINOR/PATCH> version bump because:
- [reason 1]
- [reason 2]

Current version: <current>
Proposed version: <proposed>

Should I proceed with this version bump?


Wait for user confirmation before proceeding.

Step 5: Run Changelog Release

Once the user confirms the version bump, run the changelog release command with the appropriate semver level:

changelog release <major|minor|patch>


This updates CHANGELOG.md, converting the Unreleased section to a versioned release.

Step 6: Execute Tag Process

After the changelog is released, execute the complete tag process from the justfile. This includes:

Run quality checks:

deno check src/main.ts
deno fmt --check
deno lint
deno task test


Update version files:

# Get the latest version from changelog
LATEST_VERSION=$(changelog version latest)

# Write version to deno.json
svbump write "$LATEST_VERSION" version deno.json

# Read version from deno.json and write to dist-workspace.toml
DENO_VERSION=$(svbump read version deno.json)
svbump write "$DENO_VERSION" package.version dist-workspace.toml


Regenerate skill documentation:

# Generate updated skill docs (includes version from deno.json)
deno task generate-skill-docs

# Update Claude Code plugin versions
FINAL_VERSION=$(svbump read version deno.json)
svbump write "$FINAL_VERSION" version .claude-plugin/plugin.json
svbump write "$FINAL_VERSION" version .claude-plugin/marketplace.json
# marketplace.json also has version inside plugins[0] — svbump can't do array paths,
# so use jq or edit it manually to match


Create commit and tag:

# Get the final version
FINAL_VERSION=$(svbump read version deno.json)

# Create commit
jj commit -m "chore: Release linear-cli version $FINAL_VERSION"

# Set main bookmark to parent commit
jj bookmark set main -r @-

# Create tag on the parent commit
jj tag set "v$FINAL_VERSION" -r @-


Push to remote:

# Push the bookmark
jj git push --bookmark main

# Push tags (using git)
git push origin --tags


Report completion:

Released v$FINAL_VERSION successfully!

Error Handling

If any step fails:

Quality checks fail: Fix the issues before continuing. Do not proceed with release if tests fail or linting errors exist.
Version bump fails: Verify the version format and files exist.
Push fails: Check authentication and remote access.

Always stop and report errors clearly. Never continue the release process if a critical step fails.

Important Notes
The justfile tag recipe handles the complete process from line 5-21
Use jj for all version control operations (per project CLAUDE.md)
Always use --ignore-working-copy for read-only jj operations
The workflow creates a commit on the parent (@-) and then creates a new working commit
Both jj git push and git push origin --tags are needed (jj for bookmark, git for tags)
Post-Release

After successful release:

Verify the tag appears on GitHub
Check that GitHub Actions release workflow triggers (if configured)
Confirm the new version is published
Reference

See justfile lines 5-21 for the complete tag recipe implementation.

Weekly Installs
1.3K
Repository
schpet/linear-cli
GitHub Stars
655
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass