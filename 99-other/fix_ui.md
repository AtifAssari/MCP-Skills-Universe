---
title: fix-ui
url: https://skills.sh/duc01226/easyplatform/fix-ui
---

# fix-ui

skills/duc01226/easyplatform/fix-ui
fix-ui
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill fix-ui
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

Skill Variant: Variant of /fix — UI/UX visual issue diagnosis and fix.

Quick Summary

Goal: Diagnose and fix UI/UX issues including layout, styling, responsiveness, and visual bugs.

Workflow:

Identify — Locate the component/template causing the visual issue
Diagnose — Trace CSS/HTML/component logic to find root cause
Fix — Apply targeted fix (SCSS, template, component logic)
Verify — Check responsive behavior and cross-browser rendering

Key Rules:

Debug Mindset: every claim needs file:line evidence
Always use BEM classes on template elements
Check responsive breakpoints when fixing layout issues

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

Required Skills (Priority Order)
visual-component-finder - If screenshot/image provided, use to identify the component FIRST
ui-ux-pro-max - Design intelligence database
web-design-guidelines - Design principles
frontend-design - Implementation patterns

⚠️ Validate Before Fix (NON-NEGOTIABLE): After identifying UI root cause, MUST ATTENTION present findings + proposed fix to user via AskUserQuestion and get explicit approval BEFORE any code changes. No silent fixes.

Use ui-ux-designer subagent to read and analyze ./docs/design-guidelines.md then fix the following issues: $ARGUMENTS

Workflow

FIRST (after identifying component via visual-component-finder if screenshot provided): Run ui-ux-pro-max searches to understand context and common issues:

python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "<product-type>" --domain product
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "<style-keywords>" --domain style
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "accessibility" --domain ux
python3 $HOME/.claude/skills/ui-ux-pro-max/scripts/search.py "z-index animation" --domain ux


If the user provides a screenshots or videos, use ai-multimodal skill to describe as detailed as possible the issue, make sure developers can predict the root causes easily based on the description.

Use ui-ux-designer subagent to implement the fix step by step.
Use screenshot capture tools along with ai-multimodal skill to take screenshots of the implemented fix (at the exact parent container, don't take screenshot of the whole page) and use the appropriate Gemini analysis skills (ai-multimodal, video-analysis, or document-extraction) to analyze those outputs so the result matches the design guideline and addresses all issues.
If the issues are not addressed, repeat the process until all issues are addressed.
Use chrome-devtools skill to analyze the implemented fix and make sure it matches the design guideline.
Use tester agent to test the fix and compile the code to make sure it works, then report back to main agent.
If there are issues or failed tests, ask main agent to fix all of them and repeat the process until all tests pass.
Project Management & Documentation: If user approves the changes: Use project-manager and docs-manager subagents in parallel to update the project progress and documentation:
Use project-manager subagent to update the project progress and task status in the given plan file.
Use docs-manager subagent to update the docs in ./docs directory if needed.
Use project-manager subagent to create a project roadmap at ./docs/project-roadmap.md file.
IMPORTANT: Sacrifice grammar for the sake of concision when writing outputs. If user rejects the changes: Ask user to explain the issues and ask main agent to fix all of them and repeat the process.
Final Report:
Report back to user with a summary of the changes and explain everything briefly, guide user to get started and suggest the next steps.
Ask the user if they want to commit and push to git repository, if yes, use git-manager subagent to commit and push to git repository.
IMPORTANT: Sacrifice grammar for the sake of concision when writing reports.
IMPORTANT: In reports, list any unresolved questions at the end, if any.

REMEMBER:

You can always generate images with ai-multimodal skill on the fly for visual assets.

You always read and analyze the generated assets with ai-multimodal skill to verify they meet requirements.

For image editing (removing background, adjusting, cropping), use media-processing skill as needed.

IMPORTANT: Analyze the skills catalog and activate the skills that are needed for the task during the process.

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
36
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass