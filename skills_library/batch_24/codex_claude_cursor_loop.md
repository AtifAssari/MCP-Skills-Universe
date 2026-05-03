---
title: codex-claude-cursor-loop
url: https://skills.sh/bear2u/my-skills/codex-claude-cursor-loop
---

# codex-claude-cursor-loop

skills/bear2u/my-skills/codex-claude-cursor-loop
codex-claude-cursor-loop
Installation
$ npx skills add https://github.com/bear2u/my-skills --skill codex-claude-cursor-loop
SKILL.md
Codex-Claude-Cursor Engineering Loop Skill
Core Workflow Philosophy

This skill implements a 3-way sequential validation engineering loop:

Claude Code: Architecture and planning, final review
Codex: Plan validation (logic/security), code review (bugs/performance)
Cursor Agent: Code implementation and execution
Sequential Validation: Claude plans → Codex validates → Cursor implements → Codex reviews → Claude final check → repeat
Phase 1: Planning with Claude Code
Start by creating a detailed plan for the task
Break down the implementation into clear steps
Document assumptions and potential issues
Output the plan in a structured format
Phase 2: Plan Validation with Codex
Ask user (via AskUserQuestion):
Model: gpt-5 or gpt-5-codex
Reasoning effort: low, medium, or high
Send the plan to Codex for validation:
   echo "Review this implementation plan and identify any issues:
   [Claude's plan here]

   Check for:
   - Logic errors
   - Missing edge cases
   - Architecture flaws
   - Security concerns" | codex exec -m <model> --config model_reasoning_effort="<effort>" --sandbox read-only

Capture Codex's feedback and summarize to user
Phase 3: Plan Refinement Loop

If Codex finds issues in the plan:

Summarize Codex's concerns to the user
Refine the plan based on feedback
Ask user (via AskUserQuestion): "Should I revise the plan and re-validate, or proceed with implementation?"
Repeat Phase 2 if needed until plan is solid
Phase 4: Implementation with Cursor Agent

Once the plan is validated by Codex:

Session Management

Ask user (via AskUserQuestion): "Do you want to start a new Cursor session or resume an existing one?"

New session: Start fresh
Resume session: Continue previous work

If resuming:

   # List available sessions
   cursor-agent ls

   # Let user select session ID
   # Store session ID for subsequent calls

Ask user (via AskUserQuestion): Which Cursor model to use (e.g., composer-1, claude-3.5-sonnet, gpt-4o)
Implementation
Send the validated plan to Cursor Agent:

For new session:

   cursor-agent --model "<model-name>" -p --force "Implement this plan:
   [Validated plan here]

   Please implement the code following these specifications exactly."


For resumed session:

   cursor-agent --resume="<session-id>" -p --force "Continue implementation:
   [Validated plan here]"

IMPORTANT: Store the session ID from the output for all subsequent Cursor calls
Capture what was implemented and which files were modified
Phase 5: Codex Code Review

After Cursor implements:

Send Cursor's implementation to Codex for code review:
   echo "Review this implementation for:
   - Bugs and logic errors
   - Performance issues
   - Security vulnerabilities
   - Best practices violations
   - Code quality concerns

   Files modified: [list of files]
   Implementation summary: [what Cursor did]" | codex exec --sandbox read-only

Capture Codex's code review feedback
Summarize findings to user
Phase 6: Claude's Final Review

After Codex code review:

Claude reads the implemented code using Read tool
Claude analyzes both:
Codex's review findings
The actual implementation
Claude provides final assessment:
Verify if it matches the original plan
Confirm Codex's findings are valid
Identify any additional concerns
Make final architectural decisions
Summarize overall quality and readiness
Phase 7: Iterative Improvement Loop

If issues are found (by Codex or Claude):

Claude creates a detailed fix plan based on:
Codex's code review findings
Claude's final review insights
Send the fix plan to Cursor Agent using the same session:
   # IMPORTANT: Use --resume with the stored session ID
   cursor-agent --resume="<session-id>" -p --force "Fix these issues:
   [Detailed fix plan]

   Issues from Codex: [list]
   Issues from Claude: [list]"

After Cursor fixes, repeat from Phase 5 (Codex code review)
Continue the loop until all validations pass
Note:
Use same Codex model for consistency
Always use the same Cursor session ID to maintain context
Session maintains full history of changes
Recovery When Issues Are Found
When Codex finds plan issues (Phase 2):
Claude analyzes Codex's concerns
Refines the plan addressing all issues
Re-submits to Codex for validation
Repeats until Codex approves
When Codex finds code issues (Phase 5):
Claude reviews Codex's findings
Creates detailed fix plan
Sends to Cursor for fixes
After Cursor fixes, back to Codex review
Repeats until Codex approves
When Claude finds issues (Phase 6):
Claude creates comprehensive fix plan
Sends to Cursor for implementation
After fixes, Codex reviews again
Claude does final check
Repeats until Claude approves
Best Practices
Always validate plans with Codex before implementation
Never skip Codex code review after Cursor implements
Never skip Claude's final review for architectural oversight
Maintain clear handoff between all three AIs
Document who did what for context
Use same models throughout (same Codex model, same Cursor model)
Session Management:
Always use --resume with same session ID for iterative fixes
Store session ID at the start and reuse throughout
Use cursor-agent ls to find previous sessions
Only start new session when beginning completely new feature
Command Reference
Phase	Who	Command Pattern	Purpose
1. Plan	Claude	TodoWrite, Read, analysis tools	Claude creates detailed plan
2. Validate plan	Codex	echo "plan" | codex exec -m <model> --config model_reasoning_effort="<effort>" --sandbox read-only	Codex validates logic/security
3. Refine	Claude	Analyze Codex feedback, update plan	Claude fixes plan issues
4. Session setup	Claude + User	Ask new/resume, cursor-agent ls if needed	Setup or resume Cursor session
5. Implement	Cursor	cursor-agent --model "<model>" -p --force "prompt" OR cursor-agent --resume="<id>" -p --force "prompt"	Cursor implements validated plan
6. Review code	Codex	echo "review" | codex exec --sandbox read-only	Codex reviews for bugs/performance
7. Final review	Claude	Read tool, analysis	Claude final architectural check
8. Fix plan	Claude	Create detailed fix plan	Claude plans fixes from all feedback
9. Apply fixes	Cursor	cursor-agent --resume="<id>" -p --force "fixes"	Cursor implements fixes in same session
10. Re-review	Codex + Claude	Repeat phases 6-7	Validate fixes until perfect
Error Handling
Monitor Cursor Agent output for errors
Summarize Cursor's implementation results and Claude's review
Ask for user direction via AskUserQuestion if:
Significant architectural changes needed
Multiple files will be affected
Breaking changes are required
When issues appear, Claude creates a detailed fix plan before sending to Cursor
The Perfect Loop
1. Plan (Claude)
   ↓
2. Validate Plan (Codex) → if issues → refine plan → repeat
   ↓
3. Implement (Cursor)
   ↓
4. Code Review (Codex) → captures bugs/performance issues
   ↓
5. Final Review (Claude) → architectural check
   ↓
6. Issues found? → Fix Plan (Claude) → Implement Fixes (Cursor) → back to step 4
   ↓
7. All passed? → Done! ✅


This creates a triple-validation, self-correcting, high-quality engineering system where:

Claude: All planning, architecture, and final oversight
Codex: All validation (plan logic + code quality)
Cursor Agent: All implementation and coding
Weekly Installs
20
Repository
bear2u/my-skills
GitHub Stars
840
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass