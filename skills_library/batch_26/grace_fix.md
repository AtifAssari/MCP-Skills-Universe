---
title: grace-fix
url: https://skills.sh/osovv/grace-marketplace/grace-fix
---

# grace-fix

skills/osovv/grace-marketplace/grace-fix
grace-fix
Installation
$ npx skills add https://github.com/osovv/grace-marketplace --skill grace-fix
SKILL.md

Debug an issue using GRACE semantic navigation.

Process
Step 1: Locate via Knowledge Graph

From the error/description, identify which module is likely involved:

Read docs/knowledge-graph.xml for module overview
Read docs/verification-plan.xml for relevant scenarios, test files, or log markers if available
Read docs/operational-packets.xml for the canonical FailurePacket shape if available
Follow CrossLinks to find the relevant module(s)
Read the MODULE_CONTRACT of the target module

If the optional grace CLI is available, you may use:

grace module find <query> --path <project-root> to resolve likely module IDs from stack traces, paths, verification refs, or dependency names
grace module show M-XXX --path <project-root> --with verification to pull the shared/public module and verification snapshot
grace file show <path> --path <project-root> --contracts --blocks when you already know the governed file and need its local/private navigation surface
Step 2: Navigate to Block

If the error contains a log reference like [Module][function][BLOCK_NAME]:

Search for START_BLOCK_BLOCK_NAME in the codebase — this is the exact location
Read the containing function's CONTRACT for context

If the failure came from a named verification scenario or test:

read the matching V-M-xxx entry in docs/verification-plan.xml
open the mapped test file and expected evidence for that scenario

If no log reference:

Use MODULE_MAP to find the relevant function
Read its CONTRACT
Identify the likely BLOCK by purpose
Step 3: Analyze

Read the identified block, its CONTRACT, and relevant verification entry. Determine:

What the block is supposed to do (from CONTRACT)
What evidence should prove that behavior (from tests, traces, or log markers)
What it actually does (from code)
Where the mismatch is
Step 4: Fix

Apply the fix WITHIN the semantic block boundaries. Do NOT restructure blocks unless the fix requires it.

Step 5: Update Metadata

After fixing:

Add a CHANGE_SUMMARY entry with what was fixed and why
If the fix changed the function's behavior — update its CONTRACT
If the fix changed module dependencies — update knowledge-graph.xml CrossLinks
If the fix changed tests, commands, or required markers — update docs/verification-plan.xml
Run the relevant module-local verification commands
If the failure revealed weak tests, weak logs, or poor execution-trace visibility — use $grace-verification to strengthen automated checks before considering the issue fully closed
Important
Never fix code without first reading its CONTRACT
Never change a CONTRACT without user approval
If the bug is in the architecture (wrong CONTRACT) — escalate to user, don't silently change it
Weekly Installs
26
Repository
osovv/grace-marketplace
GitHub Stars
150
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass