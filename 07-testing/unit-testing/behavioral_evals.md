---
title: behavioral-evals
url: https://skills.sh/google-gemini/gemini-cli/behavioral-evals
---

# behavioral-evals

skills/google-gemini/gemini-cli/behavioral-evals
behavioral-evals
Installation
$ npx skills add https://github.com/google-gemini/gemini-cli --skill behavioral-evals
SKILL.md
Behavioral Evals
Overview

Behavioral evaluations (evals) are tests that validate the agent's decision-making (e.g., tool choice) rather than pure functionality. They are critical for verifying prompt changes, debugging steerability, and preventing regressions.

[!NOTE] Single Source of Truth: For core concepts, policies, running tests, and general best practices, always refer to evals/README.md.

🔄 Workflow Decision Tree
Does a prompt/tool change need validation?
No -> Normal integration tests.
Yes -> Continue below.
Is it UI/Interaction heavy?
Yes -> Use appEvalTest (AppRig). See creating.md.
No -> Use evalTest (TestRig). See creating.md.
Is it a new test?
Yes -> Set policy to USUALLY_PASSES.
No -> ALWAYS_PASSES (locks in regression).
Are you fixing a failure or promoting a test?
Fixing -> See fixing.md.
Promoting -> See promoting.md.
📋 Quick Checklist
1. Setup Workspace

Seed the workspace with necessary files using the files object to simulate a realistic scenario (e.g., NodeJS project with package.json).

Details in creating.md
2. Write Assertions

Audit agent decisions using rig.setBreakpoint() (AppRig only) or index verification on rig.readToolLogs().

Details in creating.md
3. Verify

Run single tests locally with Vitest. Confirm stability locally before relying on CI workflows.

See evals/README.md for running commands.
📦 Bundled Resources

Detailed procedural guides:

creating.md: Assertion strategies, Rig selection, Mock MCPs.
fixing.md: Step-by-step automated investigation, architecture diagnosis guidelines.
promoting.md: Candidate identification criteria and threshold guidelines.
Weekly Installs
113
Repository
google-gemini/gemini-cli
GitHub Stars
103.0K
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn