---
title: recall-reasoning
url: https://skills.sh/parcadei/continuous-claude-v3/recall-reasoning
---

# recall-reasoning

skills/parcadei/continuous-claude-v3/recall-reasoning
recall-reasoning
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill recall-reasoning
SKILL.md
Recall Past Work

Search through previous sessions to find relevant decisions, approaches that worked, and approaches that failed. Queries two sources:

Artifact Index - Handoffs, plans, ledgers with post-mortems (what worked/failed)
Reasoning Files - Build attempts, test failures, commit context
When to Use
Starting work similar to past sessions
"What did we do last time with X?"
Looking for patterns that worked before
Investigating why something was done a certain way
Debugging an issue encountered previously
Usage
Primary: Artifact Index (rich context)
uv run python scripts/core/artifact_query.py "<query>" [--outcome SUCCEEDED|FAILED] [--limit N]


This searches handoffs with post-mortems (what worked, what failed, key decisions).

Secondary: Reasoning Files (build attempts)
bash "$CLAUDE_PROJECT_DIR/.claude/scripts/search-reasoning.sh" "<query>"


This searches .git/claude/commits/*/reasoning.md for build failures and fixes.

Examples
# Search for authentication-related work
uv run python scripts/core/artifact_query.py "authentication OAuth JWT"

# Find only successful approaches
uv run python scripts/core/artifact_query.py "implement agent" --outcome SUCCEEDED

# Find what failed (to avoid repeating mistakes)
uv run python scripts/core/artifact_query.py "hook implementation" --outcome FAILED

# Search build/test reasoning
bash "$CLAUDE_PROJECT_DIR/.claude/scripts/search-reasoning.sh" "TypeError"

What Gets Searched

Artifact Index (handoffs, plans, ledgers):

Task summaries and status
What worked - Successful approaches
What failed - Dead ends and why
Key decisions - Choices with rationale
Goal and constraints from ledgers

Reasoning Files (.git/claude/):

Failed build attempts and error output
Successful builds after failures
Commit context and branch info
Interpreting Results

From Artifact Index:

✓ = SUCCEEDED outcome (pattern to follow)
✗ = FAILED outcome (pattern to avoid)
? = UNKNOWN outcome (not yet marked)
Post-mortem sections show distilled learnings

From Reasoning:

build_fail = approach that didn't work
build_pass = what finally succeeded
Multiple failures before success = non-trivial problem
Process
Run Artifact Index query first - richer context, post-mortems
Review relevant handoffs - check what worked/failed sections
If needed, search reasoning - for specific build errors
Apply learnings - follow successful patterns, avoid failed ones
No Results?

Artifact Index empty:

Run uv run python scripts/core/artifact_index.py --all to index existing handoffs
Create handoffs with post-mortem sections for future recall

Reasoning files empty:

Use /commit after builds to capture reasoning
Check if .git/claude/ directory exists
Weekly Installs
347
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass