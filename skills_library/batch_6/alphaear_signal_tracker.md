---
title: alphaear-signal-tracker
url: https://skills.sh/rkiding/awesome-finance-skills/alphaear-signal-tracker
---

# alphaear-signal-tracker

skills/rkiding/awesome-finance-skills/alphaear-signal-tracker
alphaear-signal-tracker
Installation
$ npx skills add https://github.com/rkiding/awesome-finance-skills --skill alphaear-signal-tracker
SKILL.md
AlphaEar Signal Tracker Skill
Overview

This skill provides logic to track and update investment signals. It assesses how new market information impacts existing signals (Strengthened, Weakened, Falsified, or Unchanged).

Capabilities
1. Track Signal Evolution
1. Track Signal Evolution (Agentic Workflow)

YOU (the Agent) are the Tracker. Use the prompts in references/PROMPTS.md.

Workflow:

Research: Use FinResearcher Prompt to gather facts/price for a signal.
Analyze: Use FinAnalyst Prompt to generate the initial InvestmentSignal.
Track: For existing signals, use Signal Tracking Prompt to assess evolution (Strengthened/Weakened/Falsified) based on new info.

Tools:

Use alphaear-search and alphaear-stock skills to gather the necessary data.
Use scripts/fin_agent.py helper _sanitize_signal_output if needing to clean JSON.

Key Logic:

Input: Existing Signal State + New Information (News/Price).
Process:
Compare new info with signal thesis.
Determine impact direction (Positive/Negative/Neutral).
Update confidence and intensity.
Output: Updated Signal.

Example Usage (Conceptual):

# This skill is currently a pattern extracted from FinAgent.
# In a future refactor, it should be a standalone utility class.
# For now, refer to `scripts/fin_agent.py`'s `track_signal` method implementation.

Dependencies
agno (Agent framework)
sqlite3 (built-in)

Ensure DatabaseManager is initialized correctly.

Weekly Installs
255
Repository
rkiding/awesome…e-skills
GitHub Stars
2.0K
First Seen
Feb 9, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn