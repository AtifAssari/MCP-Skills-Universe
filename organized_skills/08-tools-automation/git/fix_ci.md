---
rating: ⭐⭐
title: fix-ci
url: https://skills.sh/duc01226/easyplatform/fix-ci
---

# fix-ci

skills/duc01226/easyplatform/fix-ci
fix-ci
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill fix-ci
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

Skill Variant: Variant of /fix — specialized for CI/GitHub Actions log analysis.

Quick Summary

Goal: Analyze GitHub Actions CI logs to identify and fix build/test failures in the pipeline.

Workflow:

Fetch — Download CI logs from GitHub Actions
Analyze — Identify root cause from log output (build errors, test failures, env issues)
Fix — Apply targeted fix based on traced root cause

Key Rules:

Infrastructure Context: Read docs/project-config.json → infrastructure.cicd.tool to identify CI platform (e.g., "azure-devops", "github-actions", "gitlab-ci"). Target the correct pipeline config files for that platform.
Debug Mindset: every claim needs file:line evidence
Focus on CI-specific issues (env vars, Docker, dependencies, build order)
Verify fix doesn't break local development

Root Cause Debugging — Systematic approach, never guess-and-check.

Reproduce — Confirm the issue exists with evidence (error message, stack trace, screenshot)
Isolate — Narrow to specific file/function/line using binary search + graph trace
Trace — Follow data flow from input to failure point. Read actual code, don't infer.
Hypothesize — Form theory with confidence %. State what evidence supports/contradicts it
Verify — Test hypothesis with targeted grep/read. One variable at a time.
Fix — Address root cause, not symptoms. Verify fix doesn't break callers via graph connections

NEVER: Guess without evidence. Fix symptoms instead of cause. Skip reproduction step.

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

Github Actions URL

$ARGUMENTS

⚠️ Validate Before Fix (NON-NEGOTIABLE): After CI log analysis + root cause identification, MUST ATTENTION present findings + proposed fix to user via AskUserQuestion and get explicit approval BEFORE any code changes. No silent fixes.

Workflow
Use debugger subagent to read the github actions logs with gh command, analyze and find the root cause of the issues and report back to main agent. 1.5. Write analysis findings to .ai/workspace/analysis/{ci-issue}.analysis.md. Re-read before implementing fix.
🛑 Present root cause + proposed fix → AskUserQuestion → wait for user approval.
Start implementing the fix based the reports and solutions.
Use tester agent to test the fix and make sure it works, then report back to main agent.
If there are issues or failed tests, repeat from step 2.
After finishing, respond back to user with a summary of the changes and explain everything briefly, guide user to get started and suggest the next steps.
Notes

If gh command is not available, instruct the user to install and authorize GitHub CLI first.

After fixing, MUST ATTENTION run /prove-fix — build code proof traces per change with confidence scores. Never skip.

Closing Reminders
IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
IMPORTANT MUST ATTENTION STOP after 3 failed fix attempts — report outcomes, ask user before #4 MANDATORY IMPORTANT MUST ATTENTION READ the following files before starting:
IMPORTANT MUST ATTENTION search 3+ existing patterns and read code BEFORE any modification. Run graph trace when graph.db exists.
IMPORTANT MUST ATTENTION cite file:line evidence for every claim. Confidence >80% to act, <60% = do NOT recommend.
IMPORTANT MUST ATTENTION include story_points and complexity in plan frontmatter. SP > 8 = split.
Weekly Installs
36
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn