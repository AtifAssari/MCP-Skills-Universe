---
rating: ⭐⭐
title: releasenotes
url: https://skills.sh/exceptionless/exceptionless/releasenotes
---

# releasenotes

skills/exceptionless/exceptionless/releasenotes
releasenotes
Installation
$ npx skills add https://github.com/exceptionless/exceptionless --skill releasenotes
SKILL.md

Generate a changelog for all changes from the most recent release until now.

Steps
Find the most recent release tag using git tag --sort=-creatordate
Get commits and merged PRs since that tag
Look at previous releases in this repo to match their format and style
Categorize changes into sections: Breaking Changes, Added, Changed, Fixed, Notes
Focus on user-facing changes (features, important bug fixes, breaking changes)
Include PR links and contributor attribution
Output

Present the changelog in a markdown code block, ready to copy-paste into a GitHub release.

Weekly Installs
56
Repository
exceptionless/e…tionless
GitHub Stars
2.5K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass