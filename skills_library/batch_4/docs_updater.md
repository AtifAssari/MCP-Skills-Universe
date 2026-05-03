---
title: docs-updater
url: https://skills.sh/giuseppe-trisciuoglio/developer-kit/docs-updater
---

# docs-updater

skills/giuseppe-trisciuoglio/developer-kit/docs-updater
docs-updater
Installation
$ npx skills add https://github.com/giuseppe-trisciuoglio/developer-kit --skill docs-updater
SKILL.md
Universal Documentation Updater

Analyzes git changes since the latest release tag and updates the documentation files that should change with them.

Overview

Use git history to identify release-relevant changes, then update README.md, CHANGELOG.md, and any relevant documentation folders. Keep the workflow focused on explicit user approval, precise edits, and repository-specific documentation structure.

When to Use

Use this skill when:

Preparing release notes or an Unreleased changelog update
Syncing README.md or documentation after feature work lands
Reviewing what changed since the last release before a PR or release
Prerequisites

Before starting, verify that the following conditions are met:

# Verify we're in a git repository
git rev-parse --git-dir

# Check that git tags exist
git tag --list | head -5

# Verify documentation files exist
test -f README.md || echo "README.md not found"
test -f CHANGELOG.md || echo "CHANGELOG.md not found"


If no tags exist, inform the user that this skill requires at least one release tag to compare against.

Instructions
Phase 1: Detect Last Release Version

Goal: Identify the latest released version to compare against.

Actions:

Detect the comparison baseline and display it:
LATEST_TAG=$(git describe --tags --abbrev=0 2>/dev/null)

if [ -z "$LATEST_TAG" ]; then
    echo "No git tags found. This skill requires at least one release tag."
    echo "Please create a release tag first (e.g., git tag -a v1.0.0 -m 'Initial release')"
    exit 1
fi

CURRENT_BRANCH=$(git branch --show-current)
VERSION=$(echo "$LATEST_TAG" | sed -E 's/^[^0-9]*([0-9]+\.[0-9]+\.[0-9]+).*/\1/')

echo "Latest release tag: $LATEST_TAG"
echo "Version detected: $VERSION"
echo "Comparing: $LATEST_TAG -> $CURRENT_BRANCH"

Phase 2: Perform Git Diff Analysis

Goal: Analyze all changes between the last release and current branch.

Actions:

Get the commit range and statistics:
# Get commit count between tag and HEAD
COMMIT_COUNT=$(git rev-list --count ${LATEST_TAG}..HEAD 2>/dev/null || echo "0")
echo "Commits since $LATEST_TAG: $COMMIT_COUNT"

# Get file change statistics
git diff --stat ${LATEST_TAG}..HEAD

Extract commit messages for analysis:
# Get all commit messages in the range
COMMITS=$(git log ${LATEST_TAG}..HEAD --pretty=format:"%h|%s|%b" --reverse)

# Display commits for review
echo "$COMMITS"

Get detailed file changes:
# Get list of changed files
CHANGED_FILES=$(git diff --name-only ${LATEST_TAG}..HEAD)

# Show add/modify/delete status for quick categorization
git diff --name-status ${LATEST_TAG}..HEAD

Identify component areas based on file paths:
# Detect which components/areas changed
echo "$CHANGED_FILES" | grep -E "^plugins/" | cut -d'/' -f2 | sort -u

Phase 3: Discover Documentation Structure

Goal: Identify all relevant documentation locations in the project.

Actions:

Find standard documentation folders:
# Check for common documentation locations
DOC_FOLDERS=()

[ -d "docs" ] && DOC_FOLDERS+=("docs/")
[ -d "documentation" ] && DOC_FOLDERS+=("documentation/")
[ -d "doc" ] && DOC_FOLDERS+=("doc/")

# Find plugin-specific docs
for plugin_dir in plugins/*/; do
    if [ -d "${plugin_dir}docs" ]; then
        DOC_FOLDERS+=("${plugin_dir}docs/")
    fi
done

echo "Documentation folders found:"
printf '  - %s\n' "${DOC_FOLDERS[@]}"

Identify existing documentation files:
# Check for standard doc files
DOC_FILES=()

[ -f "README.md" ] && DOC_FILES+=("README.md")
[ -f "CHANGELOG.md" ] && DOC_FILES+=("CHANGELOG.md")
[ -f "CONTRIBUTING.md" ] && DOC_FILES+=("CONTRIBUTING.md")
[ -f "docs/GUIDE.md" ] && DOC_FILES+=("docs/GUIDE.md")

echo "Documentation files found:"
printf '  - %s\n' "${DOC_FILES[@]}"

Phase 4: Generate CHANGELOG Updates

Goal: Create categorized changelog entries following Keep a Changelog standard.

Actions:

Parse commits using conventional commit semantics and map them into Keep a Changelog sections such as Added, Changed, Fixed, Removed, and Security.

Read the existing CHANGELOG.md to understand structure, then generate new entries following Keep a Changelog format.

See references/examples.md for detailed bash commands and changelog templates.

Phase 5: Update README.md

Goal: Update the main README with relevant high-level changes.

Actions:

Read the current README.md to understand its structure
Identify sections needing updates (features list, skills/agents, setup instructions, version references)
Apply updates using Edit tool: preserve structure, maintain tone, update version numbers
Phase 6: Update Documentation Folders

Goal: Propagate changes to relevant documentation in docs/ folders.

Actions:

For each documentation folder found, check for files referencing changed code
Map changed files to their documentation
Generate updates: add new feature docs, update API references, fix outdated examples

See references/examples.md for detailed discovery patterns and update strategies.

Phase 7: Present Changes for Review

Goal: Show the user what will be updated before applying changes.

Actions:

Present a summary of proposed changes:
## Proposed Documentation Updates

### Version Information
- Previous release: $LATEST_TAG
- Current branch: $CURRENT_BRANCH
- Commits analyzed: $COMMIT_COUNT

### Files to Update
- [ ] CHANGELOG.md - Add new version section with categorized changes
- [ ] README.md - Update [specific sections]
- [ ] docs/[specific files] - Update documentation

### Summary of Changes
**Added**: N new features
**Changed**: N modifications
**Fixed**: N bug fixes
**Breaking**: N breaking changes

Ask the user for confirmation via AskUserQuestion:
Confirm which files to update
Ask if any changes should be modified
Get approval to proceed
Phase 8: Apply Documentation Updates

Goal: Write the approved updates, then verify they landed correctly.

Actions:

Update CHANGELOG.md:
# Read current changelog
CURRENT_CHANGELOG=$(cat CHANGELOG.md)

# Prepend new section
cat > CHANGELOG.md << 'EOF'
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
[New content goes here]

[Rest of existing changelog]
EOF

Update README.md using Edit tool:
Make targeted edits to specific sections
Preserve overall structure
Update version numbers if applicable
Update documentation files:
# For each documentation file that needs updates
# Use Edit tool to make precise changes

Validate the applied changes:
# Confirm key files still exist after editing
test -f CHANGELOG.md && echo "CHANGELOG.md present"
test -f README.md && echo "README.md present"

# Review the scope of markdown changes
git diff --stat -- '*.md'

# Spot-check the actual content written
git diff -- '*.md' | sed -n '1,240p'

If the repository already defines documentation or markdown validation commands, run them before finishing.
Examples
Example 1: Update After Feature Development

User request: "Update docs for the new features I just added"

Output:

Latest tag: v2.4.1 → Current branch: develop
5 commits analyzed
CHANGELOG entry generated for new Spring Boot Actuator skill
README.md skills list updated
Example 2: Prepare Release Documentation

User request: "Prepare documentation for v2.5.0 release"

Output:

47 commits analyzed since v2.4.1
15 features, 8 fixes, 3 breaking changes detected
Complete CHANGELOG.md [2.5.0] section generated
README.md and plugin docs updated
Example 3: Incremental Sync

User request: "Sync docs, I've made some changes"

Output:

2 commits analyzed
Focused CHANGELOG update for github-issue-workflow skill changes
No README or plugin doc updates needed

See references/examples.md for detailed session transcripts and troubleshooting.

Best Practices
Preview before writing, verify after writing: Show the plan first, then confirm the final diff after edits
Follow Keep a Changelog: Maintain consistent changelog formatting
Categorize properly: Use correct categories (Added, Changed, Fixed, etc.)
Be specific: Include plugin/component names in changelog entries
Preserve structure: Maintain existing documentation structure and style
Reference commits: Include commit hashes for traceability when helpful
Handle breaking changes: Clearly highlight breaking changes with migration notes
Update version refs: Keep version numbers consistent across documentation
Constraints and Warnings
Requires git tags: This skill only works if the repository has at least one release tag
Read-only analysis: The skill analyzes changes but asks before writing
Manual review required: Generated changelog entries should be reviewed for accuracy
Conventional commits: Works best with projects using conventional commit format
Does not create tags: This skill updates docs but does not create release tags
No auto-commit: Documentation changes are prepared but not committed automatically
Project-specific patterns: Some projects may have custom changelog formats to respect
File paths: All file paths use forward slashes (Unix style) for cross-platform compatibility
Weekly Installs
463
Repository
giuseppe-trisci…oper-kit
GitHub Stars
233
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass