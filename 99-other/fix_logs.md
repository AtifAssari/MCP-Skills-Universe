---
title: fix-logs
url: https://skills.sh/duc01226/easyplatform/fix-logs
---

# fix-logs

skills/duc01226/easyplatform/fix-logs
fix-logs
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill fix-logs
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

Skill Variant: Variant of /fix — log-based troubleshooting and error analysis.

Quick Summary

Goal: Analyze application logs to diagnose and fix runtime errors or unexpected behavior.

Workflow:

Collect — Gather relevant log output (error messages, stack traces, timestamps)
Trace — Map log entries to source code locations
Fix — Apply fix based on traced execution path

Key Rules:

Debug Mindset: every claim needs file:line evidence
Focus on log patterns: stack traces, error codes, timing anomalies
Cross-reference logs with source code to find actual root cause

Root Cause Debugging — Systematic approach, never guess-and-check.

Reproduce — Confirm the issue exists with evidence (error message, stack trace, screenshot)
Isolate — Narrow to specific file/function/line using binary search + graph trace
Trace — Follow data flow from input to failure point. Read actual code, don't infer.
Hypothesize — Form theory with confidence %. State what evidence supports/contradicts it
Verify — Test hypothesis with targeted grep/read. One variable at a time.
Fix — Address root cause, not symptoms. Verify fix doesn't break callers via graph connections

NEVER: Guess without evidence. Fix symptoms instead of cause. Skip reproduction step.

IMPORTANT: Analyze the skills catalog and activate the skills that are needed for the task during the process.

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

$ARGUMENTS

⚠️ Validate Before Fix (NON-NEGOTIABLE): After root cause analysis + plan creation, MUST ATTENTION present findings + proposed fix to user via AskUserQuestion and get explicit approval BEFORE any code changes. No silent fixes.

Workflow
Check if ./logs.txt exists:
If missing, set up permanent log piping in project's script config (package.json, Makefile, pyproject.toml, etc.):
Bash/Unix: append 2>&1 | tee logs.txt
PowerShell: append *>&1 | Tee-Object logs.txt
Run the command to generate logs
Use debugger subagent to analyze ./logs.txt and find root causes:
Use Grep with head_limit: 30 to read only last 30 lines (avoid loading entire file)
If insufficient context, increase head_limit as needed
External Memory: Write log analysis to .ai/workspace/analysis/{issue-name}.analysis.md. Re-read before fixing.
Use scout subagent to analyze the codebase and find the exact location of the issues, then report back to main agent.
Use planner subagent to create an implementation plan based on the reports, then report back to main agent.
🛑 Present root cause + fix plan → AskUserQuestion → wait for user approval.
Start implementing the fix based the reports and solutions.
Use tester agent to test the fix and make sure it works, then report back to main agent.
Use code-reviewer subagent to quickly review the code changes and make sure it meets requirements, then report back to main agent.
If there are issues or failed tests, repeat from step 3.
After finishing, respond back to user with a summary of the changes and explain everything briefly, guide user to get started and suggest the next steps.
After fixing, MUST ATTENTION run /prove-fix — build code proof traces per change with confidence scores. Never skip.
Closing Reminders
MANDATORY IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
MANDATORY IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
MANDATORY IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
MANDATORY IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
MANDATORY IMPORTANT MUST ATTENTION STOP after 3 failed fix attempts — report outcomes, ask user before #4 MANDATORY IMPORTANT MUST ATTENTION READ the following files before starting:
MANDATORY IMPORTANT MUST ATTENTION search 3+ existing patterns and read code BEFORE any modification. Run graph trace when graph.db exists.
MANDATORY IMPORTANT MUST ATTENTION cite file:line evidence for every claim. Confidence >80% to act, <60% = do NOT recommend.
MANDATORY IMPORTANT MUST ATTENTION include story_points and complexity in plan frontmatter. SP > 8 = split.
Weekly Installs
34
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass