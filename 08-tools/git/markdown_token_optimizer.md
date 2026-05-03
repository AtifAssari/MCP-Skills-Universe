---
rating: ⭐⭐
title: markdown-token-optimizer
url: https://skills.sh/microsoft/github-copilot-for-azure/markdown-token-optimizer
---

# markdown-token-optimizer

skills/microsoft/github-copilot-for-azure/markdown-token-optimizer
markdown-token-optimizer
Installation
$ npx skills add https://github.com/microsoft/github-copilot-for-azure --skill markdown-token-optimizer
Summary

Analyzes markdown files and suggests token-reduction optimizations while preserving clarity.

Counts tokens using a 4-character-per-token approximation and identifies token-wasting patterns including emojis, verbosity, duplication, and oversized code blocks
Generates a detailed suggestions table showing issue location, description, recommended fix, and estimated token savings
Targets SKILL.md files for under 500 tokens and reference files for under 1000 tokens
Provides recommendations only without auto-modifying files, ensuring developers retain full control over changes
SKILL.md
Markdown Token Optimizer

This skill analyzes markdown files and suggests optimizations to reduce token consumption while maintaining clarity.

When to Use
Optimize markdown files for token efficiency
Reduce SKILL.md file size or check for bloat
Make documentation more concise for AI consumption
Workflow
Count - Calculate tokens (~4 chars = 1 token), report totals
Scan - Find patterns: emojis, verbosity, duplication, large blocks
Suggest - Table with location, issue, fix, savings estimate
Summary - Current/potential/savings with top recommendations

See ANTI-PATTERNS.md for detection patterns and OPTIMIZATION-PATTERNS.md for techniques.

Rules
Suggest only (no auto-modification)
Preserve clarity in all optimizations
SKILL.md target: <500 tokens, references: <1000 tokens
References
OPTIMIZATION-PATTERNS.md - Optimization techniques
ANTI-PATTERNS.md - Token-wasting patterns
Weekly Installs
1.2K
Repository
microsoft/githu…or-azure
GitHub Stars
202
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass