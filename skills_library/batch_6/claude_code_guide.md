---
title: claude-code-guide
url: https://skills.sh/sickn33/antigravity-awesome-skills/claude-code-guide
---

# claude-code-guide

skills/sickn33/antigravity-awesome-skills/claude-code-guide
claude-code-guide
Originally fromdavila7/claude-code-templates
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill claude-code-guide
SKILL.md
Claude Code Guide
Purpose

To provide a comprehensive reference for configuring and using Claude Code (the agentic coding tool) to its full potential. This skill synthesizes best practices, configuration templates, and advanced usage patterns.

Configuration (CLAUDE.md)

When starting a new project, create a CLAUDE.md file in the root directory to guide the agent.

Template (General)
# Project Guidelines

## Commands

- Run app: `npm run dev`
- Test: `npm test`
- Build: `npm run build`

## Code Style

- Use TypeScript for all new code.
- Functional components with Hooks for React.
- Tailwind CSS for styling.
- Early returns for error handling.

## Workflow

- Read `README.md` first to understand project context.
- Before editing, read the file content.
- After editing, run tests to verify.

Advanced Features
Thinking Keywords

Use these keywords in your prompts to trigger deeper reasoning from the agent:

"Think step-by-step"
"Analyze the root cause"
"Plan before executing"
"Verify your assumptions"
Debugging

If the agent is stuck or behaving unexpectedly:

Clear Context: Start a new session or ask the agent to "forget previous instructions" if confused.
Explicit Instructions: Be extremely specific about paths, filenames, and desired outcomes.
Logs: Ask the agent to "check the logs" or "run the command with verbose output".
Best Practices
Small Contexts: Don't dump the entire codebase into the context. Use grep or find to locate relevant files first.
Iterative Development: Ask for small changes, verify, then proceed.
Feedback Loop: If the agent makes a mistake, correct it immediately and ask it to "add a lesson" to its memory (if supported) or CLAUDE.md.
Reference

Based on Claude Code Guide by zebbern.

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
255
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass