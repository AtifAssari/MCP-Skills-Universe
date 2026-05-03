---
title: fix-fast
url: https://skills.sh/duc01226/easyplatform/fix-fast
---

# fix-fast

skills/duc01226/easyplatform/fix-fast
fix-fast
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill fix-fast
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Understand Code First — HARD-GATE: Do NOT write, plan, or fix until you READ existing code.

Search 3+ similar patterns (grep/glob) — cite file:line evidence
Read existing files in target area — understand structure, base classes, conventions
Run python .claude/scripts/code_graph trace <file> --direction both --json when .code-graph/graph.db exists
Map dependencies via connections or callers_of — know what depends on your target
Write investigation to .ai/workspace/analysis/ for non-trivial tasks (3+ files)
Re-read analysis file before implementing — never work from memory alone
NEVER invent new patterns when existing ones work — match exactly or document deviation

BLOCKED until: - [ ] Read target files - [ ] Grep 3+ patterns - [ ] Graph trace (if graph.db exists) - [ ] Assumptions verified with evidence

Evidence-Based Reasoning — Speculation is FORBIDDEN. Every claim needs proof.

Cite file:line, grep results, or framework docs for EVERY claim
Declare confidence: >80% act freely, 60-80% verify first, <60% DO NOT recommend
Cross-service validation required for architectural changes
"I don't have enough evidence" is valid and expected output

BLOCKED until: - [ ] Evidence file path (file:line) - [ ] Grep search performed - [ ] 3+ similar patterns found - [ ] Confidence level stated

Forbidden without proof: "obviously", "I think", "should be", "probably", "this is because" If incomplete → output: "Insufficient evidence. Verified: [...]. Not verified: [...]."

docs/project-reference/domain-entities-reference.md — Domain entity catalog, relationships, cross-service sync (read when task involves business entities/models) (content auto-injected by hook — check for [Injected: ...] header before reading)

Estimation — Modified Fibonacci: 1(trivial) → 2(small) → 3(medium) → 5(large) → 8(very large) → 13(epic, SHOULD split) → 21(MUST ATTENTION split). Output story_points and complexity in plan frontmatter. Complexity auto-derived: 1-2=Low, 3-5=Medium, 8=High, 13+=Critical.

Fix-Layer Accountability — NEVER fix at the crash site. Trace the full flow, fix at the owning layer.

AI default behavior: see error at Place A → fix Place A. This is WRONG. The crash site is a SYMPTOM, not the cause.

MANDATORY before ANY fix:

Trace full data flow — Map the complete path from data origin to crash site across ALL layers (storage → backend → API → frontend → UI). Identify where the bad state ENTERS, not where it CRASHES.
Identify the invariant owner — Which layer's contract guarantees this value is valid? That layer is responsible. Fix at the LOWEST layer that owns the invariant — not the highest layer that consumes it.
One fix, maximum protection — Ask: "If I fix here, does it protect ALL downstream consumers with ONE change?" If fix requires touching 3+ files with defensive checks, you are at the wrong layer — go lower.
Verify no bypass paths — Confirm all data flows through the fix point. Check for: direct construction skipping factories, clone/spread without re-validation, raw data not wrapped in domain models, mutations outside the model layer.

BLOCKED until: - [ ] Full data flow traced (origin → crash) - [ ] Invariant owner identified with file:line evidence - [ ] All access sites audited (grep count) - [ ] Fix layer justified (lowest layer that protects most consumers)

Anti-patterns (REJECT these):

"Fix it where it crashes" — Crash site ≠ cause site. Trace upstream.
"Add defensive checks at every consumer" — Scattered defense = wrong layer. One authoritative fix > many scattered guards.
"Both fix is safer" — Pick ONE authoritative layer. Redundant checks across layers send mixed signals about who owns the invariant.

Skill Variant: Variant of /fix — quick fixes with minimal investigation.

Quick Summary

Goal: Rapidly fix small, well-understood issues with minimal investigation overhead.

Workflow:

Identify — Quick root cause analysis from error message
Fix — Apply targeted fix directly
Verify — Run affected tests to confirm

Key Rules:

Debug Mindset: every claim needs file:line evidence
Use for simple, isolated bugs only — escalate to /fix-hard for complex issues
Minimize investigation time; if root cause isn't clear within minutes, escalate

Root Cause Debugging — Systematic approach, never guess-and-check.

Reproduce — Confirm the issue exists with evidence (error message, stack trace, screenshot)
Isolate — Narrow to specific file/function/line using binary search + graph trace
Trace — Follow data flow from input to failure point. Read actual code, don't infer.
Hypothesize — Form theory with confidence %. State what evidence supports/contradicts it
Verify — Test hypothesis with targeted grep/read. One variable at a time.
Fix — Address root cause, not symptoms. Verify fix doesn't break callers via graph connections

NEVER: Guess without evidence. Fix symptoms instead of cause. Skip reproduction step.

Analyze the skills catalog and activate the skills that are needed for the task during the process.

Debug Mindset (NON-NEGOTIABLE)

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

Do NOT assume the first hypothesis is correct — verify with actual code traces
Every root cause claim must include file:line evidence
If you cannot prove a root cause with a code trace, state "hypothesis, not confirmed"
Question assumptions: "Is this really the cause?" → trace the actual execution path
Challenge completeness: "Are there other contributing factors?" → check related code paths
No "should fix it" without proof — verify the fix addresses the traced root cause
⚠️ MANDATORY: Confidence & Evidence Gate

MANDATORY IMPORTANT MUST ATTENTION declare Confidence: X% with evidence list + file:line proof for EVERY claim. 95%+ recommend freely | 80-94% with caveats | 60-79% list unknowns | <60% STOP — gather more evidence.

Mission

Think hard to analyze and fix these issues: $ARGUMENTS

⚠️ Validate Before Fix (NON-NEGOTIABLE): After root cause analysis, MUST ATTENTION present findings + proposed fix to user via AskUserQuestion and get explicit approval BEFORE any code changes. No silent fixes.

Workflow
If the user provides a screenshots or videos, use ai-multimodal skill to describe as detailed as possible the issue, make sure developers can predict the root causes easily based on the description.
Use debugger subagent to find the root cause of the issues and report back to main agent. 2.5. Write root cause analysis to .ai/workspace/analysis/{issue-name}.analysis.md. Re-read before implementing fix.
Activate debug-investigate skills and problem-solving skills to tackle the issues.
🛑 Present root cause + proposed fix → AskUserQuestion → wait for user approval.
Start implementing the fix based the reports and solutions.
Use tester agent to test the fix and make sure it works, then report back to main agent.
If there are issues or failed tests, repeat from step 2.
After finishing, respond back to user with a summary of the changes and explain everything briefly, guide user to get started and suggest the next steps.
After fixing, MUST ATTENTION run /prove-fix — build code proof traces per change with confidence scores. Never skip.
Next Steps (Standalone: MUST ATTENTION ask user via AskUserQuestion. Skip if inside workflow.)

MANDATORY IMPORTANT MUST ATTENTION — NO EXCEPTIONS: If this skill was called outside a workflow, you MUST ATTENTION use AskUserQuestion to present these options. Do NOT skip because the task seems "simple" or "obvious" — the user decides:

"Proceed with full workflow (Recommended)" — I'll detect the best workflow to continue from here (fix applied). This ensures prove-fix, review, testing, and docs steps aren't skipped.
"/prove-fix" — Prove fix correctness with code traces
"/test" — Run tests to verify fix
"Skip, continue manually" — user decides

If already inside a workflow, skip — the workflow handles sequencing.

Closing Reminders
IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
IMPORTANT MUST ATTENTION STOP after 3 failed fix attempts — report outcomes, ask user before #4 MANDATORY IMPORTANT MUST ATTENTION READ the following files before starting:
IMPORTANT MUST ATTENTION search 3+ existing patterns and read code BEFORE any modification. Run graph trace when graph.db exists.
IMPORTANT MUST ATTENTION cite file:line evidence for every claim. Confidence >80% to act, <60% = do NOT recommend.
IMPORTANT MUST ATTENTION include story_points and complexity in plan frontmatter. SP > 8 = split.
IMPORTANT MUST ATTENTION trace full data flow and fix at the owning layer, not the crash site. Audit all access sites before adding ?..
Weekly Installs
35
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass