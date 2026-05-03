---
title: fix-bug
url: https://skills.sh/willbooster/agent-skills/fix-bug
---

# fix-bug

skills/willbooster/agent-skills/fix-bug
fix-bug
Installation
$ npx skills add https://github.com/willbooster/agent-skills --skill fix-bug
SKILL.md
Bug fix workflow
Understand the reported bug precisely.
Identify the expected behavior, the actual behavior, and the smallest scope that reproduces the problem.
Inspect the existing tests and locate the best place to extend them.
Prefer enhancing an existing focused test file over adding a broad new one.
Before modifying tests, gather debugging evidence that helps explain the failure mode.
Use logging, screenshots, traces, or other lightweight diagnostics that fit the stack.
Enhance the tests until they reproduce the bug.
If a relevant test already fails for the bug, keep it as the reproduction and tighten it only if needed.
Stop once the reproduction is minimal, reliable, and clearly tied to the reported bug.
Fix the implementation without weakening the new or existing assertions.
Keep the code change as small and cohesive as possible.
Run the enhanced tests and confirm they pass with the fix in place.
If the repository workflow requires broader verification, run the relevant checks after the targeted tests pass.
Summarize the root cause, the test enhancement, and the implementation fix.
Commit and push the changes, then run either the open-pr or update-pr skill.
Weekly Installs
47
Repository
willbooster/agent-skills
GitHub Stars
1
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass