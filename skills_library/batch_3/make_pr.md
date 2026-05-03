---
title: make-pr
url: https://skills.sh/remotion-dev/remotion/make-pr
---

# make-pr

skills/remotion-dev/remotion/make-pr
make-pr
Installation
$ npx skills add https://github.com/remotion-dev/remotion --skill make-pr
Summary

Automate pull request creation with formatted commits and branch management.

Ensures you're not on the main branch, creating a feature branch if needed
Runs Oxfmt code formatting across all affected packages before committing
Formats commits and PR titles using package name from package.json (e.g., "@remotion/shapes: Add heart shape")
Uses the gh CLI to open the pull request automatically after pushing changes
SKILL.md

Ensure we are not on the main branch, make a branch if necessary.
For all packages affected, run Oxfmt to format the code:

bunx oxfmt src --write


Commit the changes. The title of the PR must be according to the pr-name skill.

Push the changes to the remote branch.
Use the gh CLI to create a pull request and use the same format as above for the title.

Weekly Installs
728
Repository
remotion-dev/remotion
GitHub Stars
45.4K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass