---
rating: ⭐⭐
title: codex-claude-loop
url: https://skills.sh/bear2u/my-skills/codex-claude-loop
---

# codex-claude-loop

skills/bear2u/my-skills/codex-claude-loop
codex-claude-loop
Installation
$ npx skills add https://github.com/bear2u/my-skills --skill codex-claude-loop
SKILL.md
Codex-Claude Engineering Loop Skill
Core Workflow Philosophy

This skill implements a balanced engineering loop:

Claude Code: Architecture, planning, and execution
Codex: Validation and code review
Continuous Review: Each AI reviews the other's work
Context Handoff: Always continue with whoever last cleaned up
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
   - Security concerns" | codex exec -m  --config model_reasoning_effort="" --sandbox read-only

Capture Codex's feedback
Phase 3: Feedback Loop

If Codex finds issues:

Summarize Codex's concerns to the user
Refine the plan based on feedback
Ask user (via AskUserQuestion): "Should I revise the plan and re-validate, or proceed with fixes?"
Repeat Phase 2 if needed
Phase 4: Execution

Once the plan is validated:

Claude implements the code using available tools (Edit, Write, Read, etc.)
Break down implementation into manageable steps
Execute each step carefully with proper error handling
Document what was implemented
Phase 5: Cross-Review After Changes

After every change:

Send Claude's implementation to Codex for review:
Bug detection
Performance issues
Best practices validation
Security vulnerabilities
Claude analyzes Codex's feedback and decides:
Apply fixes immediately if issues are critical
Discuss with user if architectural changes needed
Document decisions made
Phase 6: Iterative Improvement
After Codex review, Claude applies necessary fixes
For significant changes, send back to Codex for re-validation
Continue the loop until code quality standards are met
Use codex exec resume --last to continue validation sessions:
   echo "Review the updated implementation" | codex exec resume --last


Note: Resume inherits all settings (model, reasoning, sandbox) from original session

Recovery When Issues Are Found

When Codex identifies problems:

Claude analyzes the root cause
Implements fixes using available tools
Sends updated code back to Codex for verification
Repeats until validation passes

When implementation errors occur:

Claude reviews the error/issue
Adjusts implementation strategy
Re-validates with Codex before proceeding
Best Practices
Always validate plans before execution
Never skip cross-review after changes
Maintain clear handoff between AIs
Document who did what for context
Use resume to preserve session state
Command Reference
Phase	Command Pattern	Purpose
Validate plan	echo "plan" | codex exec --sandbox read-only	Check logic before coding
Implement	Claude uses Edit/Write/Read tools	Claude implements the validated plan
Review code	echo "review changes" | codex exec --sandbox read-only	Codex validates Claude's implementation
Continue review	echo "next step" | codex exec resume --last	Continue validation session
Apply fixes	Claude uses Edit/Write tools	Claude fixes issues found by Codex
Re-validate	echo "verify fixes" | codex exec resume --last	Codex re-checks after fixes
Error Handling
Stop on non-zero exit codes from Codex
Summarize Codex feedback and ask for direction via AskUserQuestion
Before implementing changes, confirm approach with user if:
Significant architectural changes needed
Multiple files will be affected
Breaking changes are required
When Codex warnings appear, Claude evaluates severity and decides next steps
The Perfect Loop
Plan (Claude) → Validate Plan (Codex) → Feedback →
Implement (Claude) → Review Code (Codex) →
Fix Issues (Claude) → Re-validate (Codex) → Repeat until perfect


This creates a self-correcting, high-quality engineering system where:

Claude handles all code implementation and modifications
Codex provides validation, review, and quality assurance
Weekly Installs
30
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