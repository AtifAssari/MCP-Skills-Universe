---
title: gemini-cli
url: https://skills.sh/samhvw8/dot-claude/gemini-cli
---

# gemini-cli

skills/samhvw8/dot-claude/gemini-cli
gemini-cli
Installation
$ npx skills add https://github.com/samhvw8/dot-claude --skill gemini-cli
SKILL.md
Gemini CLI Integration Skill

This skill enables Claude Code to effectively orchestrate Gemini CLI (v0.16.0+) with Gemini 3 Pro for code generation, review, analysis, and specialized tasks.

When to Use This Skill
Ideal Use Cases

Second Opinion / Cross-Validation

Code review after writing code (different AI perspective)
Security audit with alternative analysis
Finding bugs Claude might have missed

Google Search Grounding

Questions requiring current internet information
Latest library versions, API changes, documentation updates
Current events or recent releases

Codebase Architecture Analysis

Use Gemini's codebase_investigator tool
Understanding unfamiliar codebases
Mapping cross-file dependencies

Parallel Processing

Offload tasks while continuing other work
Run multiple code generations simultaneously
Background documentation generation

Specialized Generation

Test suite generation
JSDoc/documentation generation
Code translation between languages
When NOT to Use
Simple, quick tasks (overhead not worth it)
Tasks requiring immediate response (rate limits cause delays)
When context is already loaded and understood
Interactive refinement requiring conversation
Core Instructions
1. Verify Installation
command -v gemini || which gemini

2. Basic Command Pattern
gemini "[prompt]" --yolo -o text 2>&1


Key flags:

--yolo or -y: Auto-approve all tool calls
-o text: Human-readable output
-o json: Structured output with stats
-m gemini-2.5-flash: Use faster model for simple tasks
3. Critical Behavioral Notes

YOLO Mode Behavior: Auto-approves tool calls but does NOT prevent planning prompts. Gemini may still present plans and ask "Does this plan look good?" Use forceful language:

"Apply now"
"Start immediately"
"Do this without asking for confirmation"

Rate Limits: Free tier has 60 requests/min, 1000/day. CLI auto-retries with backoff. Expect messages like "quota will reset after Xs".

4. Output Processing

For JSON output (-o json), parse:

{
  "response": "actual content",
  "stats": {
    "models": { "tokens": {...} },
    "tools": { "byName": {...} }
  }
}

Quick Reference Commands
Code Generation
gemini "Create [description] with [features]. Output complete file content." --yolo -o text

Code Review
gemini "Review [file] for: 1) features, 2) bugs/security issues, 3) improvements" -o text

Bug Fixing
gemini "Fix these bugs in [file]: [list]. Apply fixes now." --yolo -o text

Test Generation
gemini "Generate [Jest/pytest] tests for [file]. Focus on [areas]." --yolo -o text

Documentation
gemini "Generate JSDoc for all functions in [file]. Output as markdown." --yolo -o text

Architecture Analysis
gemini "Use codebase_investigator to analyze this project" -o text

Web Research
gemini "What are the latest [topic]? Use Google Search." -o text

Faster Model (Simple Tasks)
gemini "[prompt]" -m gemini-2.5-flash -o text

Error Handling
Rate Limit Exceeded
CLI auto-retries with backoff
Use -m gemini-2.5-flash for lower priority tasks
Run in background for long operations
Command Failures
Check JSON output for detailed error stats
Verify Gemini is authenticated: gemini --version
Check ~/.gemini/settings.json for config issues
Validation After Generation

Always verify Gemini's output:

Check for security vulnerabilities (XSS, injection)
Test functionality matches requirements
Review code style consistency
Verify dependencies are appropriate
Integration Workflow
Standard Generate-Review-Fix Cycle
# 1. Generate
gemini "Create [code]" --yolo -o text

# 2. Review (Gemini reviews its own work)
gemini "Review [file] for bugs and security issues" -o text

# 3. Fix identified issues
gemini "Fix [issues] in [file]. Apply now." --yolo -o text

Background Execution

For long tasks, run in background and monitor:

gemini "[long task]" --yolo -o text 2>&1 &
# Monitor with BashOutput tool

Gemini's Unique Capabilities

These tools are available only through Gemini:

google_web_search - Real-time internet search via Google
codebase_investigator - Deep architectural analysis
save_memory - Cross-session persistent memory
Configuration
Project Context (Optional)

Create .gemini/GEMINI.md in project root for persistent context that Gemini will automatically read.

Session Management

List sessions: gemini --list-sessions Resume session: echo "follow-up" | gemini -r [index] -o text

See Also
reference.md - Complete command and flag reference
templates.md - Prompt templates for common operations
patterns.md - Advanced integration patterns
tools.md - Gemini's built-in tools documentation
Weekly Installs
44
Repository
samhvw8/dot-claude
GitHub Stars
10
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn