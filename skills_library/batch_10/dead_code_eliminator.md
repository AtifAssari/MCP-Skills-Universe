---
title: dead-code-eliminator
url: https://skills.sh/abpai/skills/dead-code-eliminator
---

# dead-code-eliminator

skills/abpai/skills/dead-code-eliminator
dead-code-eliminator
Installation
$ npx skills add https://github.com/abpai/skills --skill dead-code-eliminator
SKILL.md
Dead Code Eliminator

Use this skill when the user wants a dead-code audit, not a broad refactor. The default outcome is a reachability report and a removal order, with code changes only after the audit is clear.

Main Workflow
Find the project entry points: executables, CLI bins, routes, jobs, exports, package indexes, and framework lifecycle hooks.
Trace the live set from those roots through imports, calls, instantiations, and other statically provable edges.
Mark anything unresolved, conditional, or externally consumable instead of guessing reachability.
Separate test-only reachability from production reachability.
Report dead code candidates, confidence level, and any correctness or soundness concerns in the live code.
If the user asks for removal, delete in dependency-safe order after the audit is complete.
Safety Rules
Do not guess through reflection, eval, string dispatch, or other dynamic lookup paths.
Treat feature-flagged or environment-conditional code as conditionally reachable and name the condition.
Treat symbols that may be consumed outside the repository as unused export (external consumers possible), not as dead code.
Do not collapse low-confidence items into the dead list without calling out the uncertainty.
Stop and ask for a narrower scope if the codebase is too large to trace confidently.
Output Rules
Always start with the live-entry-point and reachability picture before listing dead code.
Keep the main report focused on the audit result, not on style commentary.
Use references/report-shape.md for the exact report sections, item formatting, and removal-order template.
Include correctness and algorithmic-soundness suggestions only for live code.
Decision Heuristics
Prefer conservative reachability over false positives.
Prefer a smaller proven live set over speculative reachability.
Prefer explicit confidence labels over silent omissions.
Prefer audit-first output over code edits unless the user explicitly asks to remove code.
Update Check

On first use in a session, silently check for a newer version:

Fetch https://raw.githubusercontent.com/abpai/skills/main/versions.json.
Compare the version for dead-code-eliminator against this file's metadata.version.
If the remote version is newer, pause before the main task and ask:

dead-code-eliminator update available (local {X.Y} → remote {A.B}). Would you like me to update it for you first? I can run npx skills update dead-code-eliminator for you.

If the user says yes, run the update before continuing.
If the user says no, continue with the current local version.
If the fetch fails or web access is unavailable, skip silently.
Weekly Installs
23
Repository
abpai/skills
First Seen
Feb 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn