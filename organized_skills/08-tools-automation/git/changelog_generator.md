---
rating: ⭐⭐⭐
title: changelog-generator
url: https://skills.sh/composiohq/awesome-claude-skills/changelog-generator
---

# changelog-generator

skills/composiohq/awesome-claude-skills/changelog-generator
changelog-generator
Installation
$ npx skills add https://github.com/composiohq/awesome-claude-skills --skill changelog-generator
Summary

Automatically transforms git commits into polished, customer-friendly release notes.

Analyzes commit history within specified date ranges or between versions, then categorizes changes into features, improvements, bug fixes, breaking changes, and security updates
Converts technical commit messages into clear, user-facing language while filtering out internal noise like refactoring and test commits
Supports custom changelog style guidelines via CHANGELOG_STYLE.md for consistent formatting and brand voice
Generates professionally formatted markdown output ready for GitHub releases, app store submissions, email updates, and public changelog pages
SKILL.md
Changelog Generator

This skill transforms technical git commits into polished, user-friendly changelogs that your customers and users will actually understand and appreciate.

When to Use This Skill
Preparing release notes for a new version
Creating weekly or monthly product update summaries
Documenting changes for customers
Writing changelog entries for app store submissions
Generating update notifications
Creating internal release documentation
Maintaining a public changelog/product updates page
What This Skill Does
Scans Git History: Analyzes commits from a specific time period or between versions
Categorizes Changes: Groups commits into logical categories (features, improvements, bug fixes, breaking changes, security)
Translates Technical → User-Friendly: Converts developer commits into customer language
Formats Professionally: Creates clean, structured changelog entries
Filters Noise: Excludes internal commits (refactoring, tests, etc.)
Follows Best Practices: Applies changelog guidelines and your brand voice
How to Use
Basic Usage

From your project repository:

Create a changelog from commits since last release

Generate changelog for all commits from the past week

Create release notes for version 2.5.0

With Specific Date Range
Create a changelog for all commits between March 1 and March 15

With Custom Guidelines
Create a changelog for commits since v2.4.0, using my changelog 
guidelines from CHANGELOG_STYLE.md

Example

User: "Create a changelog for commits from the past 7 days"

Output:

# Updates - Week of March 10, 2024

## ✨ New Features

- **Team Workspaces**: Create separate workspaces for different 
  projects. Invite team members and keep everything organized.

- **Keyboard Shortcuts**: Press ? to see all available shortcuts. 
  Navigate faster without touching your mouse.

## 🔧 Improvements

- **Faster Sync**: Files now sync 2x faster across devices
- **Better Search**: Search now includes file contents, not just titles

## 🐛 Fixes

- Fixed issue where large images wouldn't upload
- Resolved timezone confusion in scheduled posts
- Corrected notification badge count


Inspired by: Manik Aggarwal's use case from Lenny's Newsletter

Tips
Run from your git repository root
Specify date ranges for focused changelogs
Use your CHANGELOG_STYLE.md for consistent formatting
Review and adjust the generated changelog before publishing
Save output directly to CHANGELOG.md
Related Use Cases
Creating GitHub release notes
Writing app store update descriptions
Generating email updates for users
Creating social media announcement posts
Weekly Installs
3.4K
Repository
composiohq/awes…e-skills
GitHub Stars
57.5K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass