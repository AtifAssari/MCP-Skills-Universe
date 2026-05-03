---
rating: ⭐⭐
title: strategic-compact
url: https://skills.sh/affaan-m/everything-claude-code/strategic-compact
---

# strategic-compact

skills/affaan-m/everything-claude-code/strategic-compact
strategic-compact
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill strategic-compact
Summary

Strategic context compaction at logical task boundaries instead of arbitrary auto-triggers.

Suggests /compact at configurable thresholds (default: 50 tool calls) via PreToolUse hooks on Edit and Write operations
Provides a decision guide for when to compact across common phase transitions (research to planning, debugging to next feature, etc.)
Clarifies what persists through compaction (CLAUDE.md, TodoWrite, memory files, git state) versus what's lost (intermediate reasoning, file contents, conversation history)
Includes token optimization patterns for lazy-loading skills, monitoring context consumption, and detecting duplicate instructions across rules and skill files
SKILL.md
Strategic Compact Skill

Suggests manual /compact at strategic points in your workflow rather than relying on arbitrary auto-compaction.

When to Activate
Running long sessions that approach context limits (200K+ tokens)
Working on multi-phase tasks (research → plan → implement → test)
Switching between unrelated tasks within the same session
After completing a major milestone and starting new work
When responses slow down or become less coherent (context pressure)
Why Strategic Compaction?

Auto-compaction triggers at arbitrary points:

Often mid-task, losing important context
No awareness of logical task boundaries
Can interrupt complex multi-step operations

Strategic compaction at logical boundaries:

After exploration, before execution — Compact research context, keep implementation plan
After completing a milestone — Fresh start for next phase
Before major context shifts — Clear exploration context before different task
How It Works

The suggest-compact.js script runs on PreToolUse (Edit/Write) and:

Tracks tool calls — Counts tool invocations in session
Threshold detection — Suggests at configurable threshold (default: 50 calls)
Periodic reminders — Reminds every 25 calls after threshold
Hook Setup

Add to your ~/.claude/settings.json:

{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [{ "type": "command", "command": "node ~/.claude/skills/strategic-compact/suggest-compact.js" }]
      },
      {
        "matcher": "Write",
        "hooks": [{ "type": "command", "command": "node ~/.claude/skills/strategic-compact/suggest-compact.js" }]
      }
    ]
  }
}

Configuration

Environment variables:

COMPACT_THRESHOLD — Tool calls before first suggestion (default: 50)
Compaction Decision Guide

Use this table to decide when to compact:

Phase Transition	Compact?	Why
Research → Planning	Yes	Research context is bulky; plan is the distilled output
Planning → Implementation	Yes	Plan is in TodoWrite or a file; free up context for code
Implementation → Testing	Maybe	Keep if tests reference recent code; compact if switching focus
Debugging → Next feature	Yes	Debug traces pollute context for unrelated work
Mid-implementation	No	Losing variable names, file paths, and partial state is costly
After a failed approach	Yes	Clear the dead-end reasoning before trying a new approach
What Survives Compaction

Understanding what persists helps you compact with confidence:

Persists	Lost
CLAUDE.md instructions	Intermediate reasoning and analysis
TodoWrite task list	File contents you previously read
Memory files (~/.claude/memory/)	Multi-step conversation context
Git state (commits, branches)	Tool call history and counts
Files on disk	Nuanced user preferences stated verbally
Best Practices
Compact after planning — Once plan is finalized in TodoWrite, compact to start fresh
Compact after debugging — Clear error-resolution context before continuing
Don't compact mid-implementation — Preserve context for related changes
Read the suggestion — The hook tells you when, you decide if
Write before compacting — Save important context to files or memory before compacting
Use /compact with a summary — Add a custom message: /compact Focus on implementing auth middleware next
Token Optimization Patterns
Trigger-Table Lazy Loading

Instead of loading full skill content at session start, use a trigger table that maps keywords to skill paths. Skills load only when triggered, reducing baseline context by 50%+:

Trigger	Skill	Load When
"test", "tdd", "coverage"	tdd-workflow	User mentions testing
"security", "auth", "xss"	security-review	Security-related work
"deploy", "ci/cd"	deployment-patterns	Deployment context
Context Composition Awareness

Monitor what's consuming your context window:

CLAUDE.md files — Always loaded, keep lean
Loaded skills — Each skill adds 1-5K tokens
Conversation history — Grows with each exchange
Tool results — File reads, search results add bulk
Duplicate Instruction Detection

Common sources of duplicate context:

Same rules in both ~/.claude/rules/ and project .claude/rules/
Skills that repeat CLAUDE.md instructions
Multiple skills covering overlapping domains
Context Optimization Tools
token-optimizer MCP — Automated 95%+ token reduction via content deduplication
context-mode — Context virtualization (315KB to 5.4KB demonstrated)
Related
The Longform Guide — Token optimization section
Memory persistence hooks — For state that survives compaction
continuous-learning skill — Extracts patterns before session ends
Weekly Installs
3.7K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass