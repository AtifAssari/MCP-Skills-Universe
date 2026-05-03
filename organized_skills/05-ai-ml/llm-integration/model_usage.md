---
rating: ⭐⭐
title: model-usage
url: https://skills.sh/steipete/clawdis/model-usage
---

# model-usage

skills/steipete/clawdis/model-usage
model-usage
Installation
$ npx skills add https://github.com/steipete/clawdis --skill model-usage
Summary

Per-model cost summaries from CodexBar CLI logs for Codex or Claude providers.

Supports two summary modes: "current" (most recent daily model with highest cost) and "all" (full model breakdown across all logged days)
Accepts input via live CodexBar CLI invocation, JSON file, or stdin; outputs as plain text or formatted JSON
Requires CodexBar CLI installed locally (macOS only via Homebrew; Linux support pending)
Falls back to last entry in modelsUsed when model breakdowns are unavailable; override with --model flag for specific model queries
SKILL.md
Model usage
Overview

Get per-model usage cost from CodexBar's local cost logs. Supports "current model" (most recent daily entry) or "all models" summaries for Codex or Claude.

TODO: add Linux CLI support guidance once CodexBar CLI install path is documented for Linux.

Quick start
Fetch cost JSON via CodexBar CLI or pass a JSON file.
Use the bundled script to summarize by model.
python {baseDir}/scripts/model_usage.py --provider codex --mode current
python {baseDir}/scripts/model_usage.py --provider codex --mode all
python {baseDir}/scripts/model_usage.py --provider claude --mode all --format json --pretty

Current model logic
Uses the most recent daily row with modelBreakdowns.
Picks the model with the highest cost in that row.
Falls back to the last entry in modelsUsed when breakdowns are missing.
Override with --model <name> when you need a specific model.
Inputs
Default: runs codexbar cost --format json --provider <codex|claude>.
File or stdin:
codexbar cost --provider codex --format json > /tmp/cost.json
python {baseDir}/scripts/model_usage.py --input /tmp/cost.json --mode all
cat /tmp/cost.json | python {baseDir}/scripts/model_usage.py --input - --mode current

Output
Text (default) or JSON (--format json --pretty).
Values are cost-only per model; tokens are not split by model in CodexBar output.
References
Read references/codexbar-cli.md for CLI flags and cost JSON fields.
Weekly Installs
1.1K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass