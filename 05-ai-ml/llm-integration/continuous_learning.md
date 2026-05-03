---
rating: ⭐⭐
title: continuous-learning
url: https://skills.sh/affaan-m/everything-claude-code/continuous-learning
---

# continuous-learning

skills/affaan-m/everything-claude-code/continuous-learning
continuous-learning
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill continuous-learning
Summary

Automatically extract reusable patterns from Claude Code sessions and save them as learned skills.

Runs as a Stop hook at session end to evaluate transcripts, detect patterns, and save skills to ~/.claude/skills/learned/
Configurable pattern detection across five categories: error resolution, user corrections, workarounds, debugging techniques, and project-specific conventions
Customizable via config.json with minimum session length, extraction thresholds, and pattern ignore lists
Non-blocking, lightweight approach that accesses full session context without adding per-message latency
SKILL.md
Continuous Learning Skill

Automatically evaluates Claude Code sessions on end to extract reusable patterns that can be saved as learned skills.

When to Activate
Setting up automatic pattern extraction from Claude Code sessions
Configuring the Stop hook for session evaluation
Reviewing or curating learned skills in ~/.claude/skills/learned/
Adjusting extraction thresholds or pattern categories
Comparing v1 (this) vs v2 (instinct-based) approaches
Status

This v1 skill is still supported, but continuous-learning-v2 is the preferred path for new installs. Keep v1 when you explicitly want the simpler Stop-hook extraction flow or need compatibility with older learned-skill workflows.

How It Works

This skill runs as a Stop hook at the end of each session:

Session Evaluation: Checks if session has enough messages (default: 10+)
Pattern Detection: Identifies extractable patterns from the session
Skill Extraction: Saves useful patterns to ~/.claude/skills/learned/
Configuration

Edit config.json to customize:

{
  "min_session_length": 10,
  "extraction_threshold": "medium",
  "auto_approve": false,
  "learned_skills_path": "~/.claude/skills/learned/",
  "patterns_to_detect": [
    "error_resolution",
    "user_corrections",
    "workarounds",
    "debugging_techniques",
    "project_specific"
  ],
  "ignore_patterns": [
    "simple_typos",
    "one_time_fixes",
    "external_api_issues"
  ]
}

Pattern Types
Pattern	Description
error_resolution	How specific errors were resolved
user_corrections	Patterns from user corrections
workarounds	Solutions to framework/library quirks
debugging_techniques	Effective debugging approaches
project_specific	Project-specific conventions
Hook Setup

Add to your ~/.claude/settings.json:

{
  "hooks": {
    "Stop": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/skills/continuous-learning/evaluate-session.sh"
      }]
    }]
  }
}

Why Stop Hook?
Lightweight: Runs once at session end
Non-blocking: Doesn't add latency to every message
Complete context: Has access to full session transcript
Related
The Longform Guide - Section on continuous learning
/learn command - Manual pattern extraction mid-session
Comparison Notes (Research: Jan 2025)
vs Homunculus

Homunculus v2 takes a more sophisticated approach:

Feature	Our Approach	Homunculus v2
Observation	Stop hook (end of session)	PreToolUse/PostToolUse hooks (100% reliable)
Analysis	Main context	Background agent (Haiku)
Granularity	Full skills	Atomic "instincts"
Confidence	None	0.3-0.9 weighted
Evolution	Direct to skill	Instincts → cluster → skill/command/agent
Sharing	None	Export/import instincts

Key insight from homunculus:

"v1 relied on skills to observe. Skills are probabilistic—they fire ~50-80% of the time. v2 uses hooks for observation (100% reliable) and instincts as the atomic unit of learned behavior."

Potential v2 Enhancements
Instinct-based learning - Smaller, atomic behaviors with confidence scoring
Background observer - Haiku agent analyzing in parallel
Confidence decay - Instincts lose confidence if contradicted
Domain tagging - code-style, testing, git, debugging, etc.
Evolution path - Cluster related instincts into skills/commands

See: docs/continuous-learning-v2-spec.md for full spec.

Weekly Installs
3.7K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail