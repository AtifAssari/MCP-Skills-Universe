---
rating: ⭐⭐⭐
title: skill-comply
url: https://skills.sh/affaan-m/everything-claude-code/skill-comply
---

# skill-comply

skills/affaan-m/everything-claude-code/skill-comply
skill-comply
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill skill-comply
SKILL.md
skill-comply: Automated Compliance Measurement

Measures whether coding agents actually follow skills, rules, or agent definitions by:

Auto-generating expected behavioral sequences (specs) from any .md file
Auto-generating scenarios with decreasing prompt strictness (supportive → neutral → competing)
Running claude -p and capturing tool call traces via stream-json
Classifying tool calls against spec steps using LLM (not regex)
Checking temporal ordering deterministically
Generating self-contained reports with spec, prompts, and timelines
Supported Targets
Skills (skills/*/SKILL.md): Workflow skills like search-first, TDD guides
Rules (rules/common/*.md): Mandatory rules like testing.md, security.md, git-workflow.md
Agent definitions (agents/*.md): Whether an agent gets invoked when expected (internal workflow verification not yet supported)
When to Activate
User runs /skill-comply <path>
User asks "is this rule actually being followed?"
After adding new rules/skills, to verify agent compliance
Periodically as part of quality maintenance
Usage
# Full run
uv run python -m scripts.run ~/.claude/rules/common/testing.md

# Dry run (no cost, spec + scenarios only)
uv run python -m scripts.run --dry-run ~/.claude/skills/search-first/SKILL.md

# Custom models
uv run python -m scripts.run --gen-model haiku --model sonnet <path>

Key Concept: Prompt Independence

Measures whether a skill/rule is followed even when the prompt doesn't explicitly support it.

Report Contents

Reports are self-contained and include:

Expected behavioral sequence (auto-generated spec)
Scenario prompts (what was asked at each strictness level)
Compliance scores per scenario
Tool call timelines with LLM classification labels
Advanced (optional)

For users familiar with hooks, reports also include hook promotion recommendations for steps with low compliance. This is informational — the main value is the compliance visibility itself.

Weekly Installs
2.0K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass