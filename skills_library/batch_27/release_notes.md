---
title: release-notes
url: https://skills.sh/luongnv89/skills/release-notes
---

# release-notes

skills/luongnv89/skills/release-notes
release-notes
Installation
$ npx skills add https://github.com/luongnv89/skills --skill release-notes
SKILL.md
Release Notes Generator

Generate comprehensive release notes by analyzing git history and GitHub activity.

Workflow
1. Determine Version Range
# List recent tags
git tag --sort=-creatordate | head -10

# Find commits since last tag
git log $(git describe --tags --abbrev=0)..HEAD --oneline


Ask user for:

New version: Version number for this release (e.g., v1.2.0)
Base reference: Previous tag or commit to compare from (default: latest tag)
2. Gather Changes

Run in parallel:

# Get commits since last release
git log <base>..HEAD --pretty=format:"%h %s" --no-merges

# Get merge commits (PRs)
git log <base>..HEAD --merges --pretty=format:"%h %s"

# Get merged PRs (if GitHub repo)
gh pr list --state merged --base main --json number,title,labels,author --limit 100

# Get closed issues linked to PRs
gh issue list --state closed --json number,title,labels --limit 100

3. Categorize Changes

Group changes by type based on commit prefixes and PR labels:

Category	Commit Prefixes	PR Labels
Features	feat:, feature:	enhancement, feature
Bug Fixes	fix:, bugfix:	bug, fix
Performance	perf:	performance
Documentation	docs:	documentation
Breaking Changes	BREAKING:, !:	breaking-change
Dependencies	deps:, chore(deps):	dependencies
Other	chore:, refactor:, style:, test:	-
4. Generate Release Notes

Use this format for GitHub Releases:

## What's Changed

### Breaking Changes
- Description of breaking change (#PR)

### Features
- Add new feature X (#123) @author
- Implement Y functionality (#124) @author

### Bug Fixes
- Fix issue with Z (#125) @author

### Performance
- Improve loading speed by 50% (#126) @author

### Documentation
- Update README with new examples (#127) @author

### Other Changes
- Refactor internal APIs (#128) @author

## New Contributors
- @username made their first contribution in #123

**Full Changelog**: https://github.com/owner/repo/compare/v1.0.0...v1.1.0

5. Output

Save to RELEASE_NOTES.md in project root.

Optionally create GitHub release:

gh release create <version> --title "<version>" --notes-file RELEASE_NOTES.md

Tips
Omit empty sections
Link PR numbers: (#123) auto-links on GitHub
Credit authors: @username
Highlight breaking changes at the top
Include upgrade instructions for breaking changes
Weekly Installs
26
Repository
luongnv89/skills
GitHub Stars
68
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn