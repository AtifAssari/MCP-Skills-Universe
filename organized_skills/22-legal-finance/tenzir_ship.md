---
rating: ⭐⭐
title: tenzir-ship
url: https://skills.sh/tenzir/skills/tenzir-ship
---

# tenzir-ship

skills/tenzir/skills/tenzir-ship
tenzir-ship
Installation
$ npx skills add https://github.com/tenzir/skills --skill tenzir-ship
SKILL.md
tenzir-ship

This skill bundles key release engineering use cases with tenzir-ship.

Available scripts
bash <skill-dir>/scripts/detect-change-scope.sh: Detects the current changelog scope. Use this before adding a changelog entry to identify whether staged, unstaged, or branch changes should drive the entry; the script prints a suggested diff command and the files in scope.
Use Cases
Initialize a changelog project

Set up a new changelog workspace before the first entry exists. Prefer the explicit init command when the task is project setup rather than entry creation.

Instructions: references/init-changelog-project.md

Add a changelog entry

Add changelog entries as part of shipping bugfixes, changes, and features during day-to-day development.

Instructions: references/add-changelog-entry.md

Create a release

We distinguish two types of releases:

Remote: triggers a CI workflow
Local: releases from a local repository

Prefer a remote release if a workflow exists, and use a local release otherwise.

Documentation

When running into errors during the release process, obtain additional help by reading the official documentation:

https://docs.tenzir.com/reference/ship-framework.md
https://docs.tenzir.com/guides/packages/maintain-a-changelog.md
Weekly Installs
44
Repository
tenzir/skills
GitHub Stars
1
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass