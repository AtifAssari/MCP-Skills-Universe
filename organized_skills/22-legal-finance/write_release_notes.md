---
rating: ⭐⭐⭐
title: write-release-notes
url: https://skills.sh/tldraw/tldraw/write-release-notes
---

# write-release-notes

skills/tldraw/tldraw/write-release-notes
write-release-notes
Installation
$ npx skills add https://github.com/tldraw/tldraw --skill write-release-notes
SKILL.md
Write release notes

This skill covers how to write a complete release notes article for a published tldraw SDK release.

Location

All release files live in apps/docs/content/releases/.

File	Purpose
next.mdx	Accumulates changes for the upcoming release
vX.Y.0.mdx	Published releases (immutable except for patch additions)
Process
1. Identify the release

Get the version number and find the GitHub release:

gh release view v4.3.0


This shows the release date, tag, and any release notes from GitHub.

2. Find all PRs in the release

List PRs merged between the previous release and this one:

# Find commits between releases
git log v4.2.0..v4.3.0 --oneline --merges

# Or use gh to list PRs
gh pr list --state merged --base main --search "merged:2024-01-01..2024-02-01"

3. Fetch PR details

For each PR, get the full details:

gh pr view <PR_NUMBER> --json title,body,labels,author,baseRefName


Look for:

### Release notes section in PR body
### API changes section in PR body
Labels indicating category (api, bugfix, improvement, etc.)
Whether "breaking" appears in the PR

Important: Only include PRs whose baseRefName is main. PRs merged into feature branches (e.g. default-shape-customization) are not yet released — they will be included when the feature branch itself is merged to main.

4. Find patch releases

List any patch releases for this minor version:

gh release list | grep "v4.3"


For each patch release, find its PRs:

git log v4.3.0..v4.3.1 --oneline --merges

5. Write the article

Create apps/docs/content/releases/vX.Y.0.mdx following the style guide.

Write the frontmatter with version, dates, and keywords
Write a 1-2 sentence introduction summarizing highlights
Create featured sections for major features and breaking changes
List API changes, improvements, and bug fixes
Add patch release sections if applicable
Add GitHub release links
6. Verify

Check that:

All significant PRs are represented
PR links are correct and formatted properly
Community contributors are credited
Breaking changes are marked with 💥
Sections are in the correct order
References
Style guide: See ../shared/release-notes-guide.md for guidance on what a release notes article should contain and how to format it.
Weekly Installs
256
Repository
tldraw/tldraw
GitHub Stars
46.8K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn