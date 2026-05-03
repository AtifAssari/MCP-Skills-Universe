---
title: multi-llm-consult
url: https://skills.sh/nickcrew/claude-ctx-plugin/multi-llm-consult
---

# multi-llm-consult

skills/nickcrew/claude-ctx-plugin/multi-llm-consult
multi-llm-consult
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill multi-llm-consult
SKILL.md
Multi-LLM Consult
Overview

Use a bundled script to query external LLM providers with a sanitized prompt and return a concise comparison.

Setup
Configure API keys in the TUI: open the Command Palette (Ctrl+P) and run Configure LLM Providers.
Keys are stored in settings.json under llm_providers.
Workflow
Identify the purpose (second-opinion, plan, review, delegate).
Summarize the task and sanitize sensitive data before sending it out.
Run the consult script with the chosen provider.
Compare responses and reconcile with your own plan before acting.
Consult Script

Always run --help first:

python scripts/consult_llm.py --help


Example: second opinion

python scripts/consult_llm.py \
  --provider gemini \
  --purpose second-opinion \
  --prompt "We plan to refactor module X. What risks or gaps do you see?"


Example: delegate a review

python scripts/consult_llm.py \
  --provider qwen \
  --purpose review \
  --prompt-file /tmp/review_request.md \
  --context-file /tmp/patch.diff


Example: plan check with Codex (OpenAI)

python scripts/consult_llm.py \
  --provider codex \
  --purpose plan \
  --prompt "Draft a 5-step plan for implementing feature Y."

Output Handling
Treat responses as advisory; verify against repo constraints and current state.
Summarize the external response in 3-6 bullets before acting.
If responses conflict, call out the differences explicitly and choose a path.
References
Provider defaults and configuration: references/providers.md
Weekly Installs
42
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn