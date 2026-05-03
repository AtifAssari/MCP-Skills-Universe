---
rating: ⭐⭐⭐
title: git:load-issues
url: https://skills.sh/neolabhq/context-engineering-kit/git:load-issues
---

# git:load-issues

skills/neolabhq/context-engineering-kit/git:load-issues
git:load-issues
Installation
$ npx skills add https://github.com/neolabhq/context-engineering-kit --skill git:load-issues
SKILL.md

Load all open issues from the current GitHub repository and save them as markdown files in the ./specs/issues/ directory.

Follow these steps:

Use the gh CLI to list all open issues in the current repository:

Run gh issue list --limit 100 to get all open issues

For each open issue, fetch detailed information:

Run gh issue view <number> --json number,title,body,state,createdAt,updatedAt,author,labels,assignees,url
Extract all relevant metadata

Create the issues directory:

Run mkdir -p ./specs/issues to ensure the directory exists

Save each issue as a separate markdown file:

File naming pattern: <number-padded-to-3-digits>-<kebab-case-title>.md
Example: 007-make-code-review-trigger-on-sql-sh-changes.md

Use the following markdown template for each issue file:

# Issue #<number>: <title>

**Status:** <state>
**Created:** <createdAt>
**Updated:** <updatedAt>
**Author:** <author.name> (@<author.login>)
**URL:** <url>

## Description

<body>

## Labels

<labels or "None">

## Assignees

<assignees or "None">

After all issues are saved, provide a summary of:
Total number of issues loaded
List of created files with their issue numbers and titles

IMPORTANT: Execute all steps in the correct order and ensure all issue data is properly formatted in the markdown files.

Weekly Installs
397
Repository
neolabhq/contex…ring-kit
GitHub Stars
942
First Seen
Feb 23, 2026