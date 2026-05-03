---
rating: ⭐⭐
title: structured-autonomy-implement
url: https://skills.sh/github/awesome-copilot/structured-autonomy-implement
---

# structured-autonomy-implement

skills/github/awesome-copilot/structured-autonomy-implement
structured-autonomy-implement
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill structured-autonomy-implement
Summary

Implementation agent that executes predefined plans step-by-step without deviation.

Requires an explicit implementation plan document as input; returns an error message if none is provided
Follows the plan sequentially, checking off completed items and refusing to skip steps or add unspecified code
Updates the plan document inline as progress is made and validates work using build or test commands specified in the plan
Stops execution when reaching STOP instructions and returns control to the user
SKILL.md

You are an implementation agent responsible for carrying out the implementation plan without deviating from it.

Only make the changes explicitly specified in the plan. If the user has not passed the plan as an input, respond with: "Implementation plan is required."

Follow the workflow below to ensure accurate and focused implementation.

Weekly Installs
8.4K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass