---
rating: ⭐⭐
title: gemini-computer-use
url: https://skills.sh/am-will/codex-skills/gemini-computer-use
---

# gemini-computer-use

skills/am-will/codex-skills/gemini-computer-use
gemini-computer-use
Installation
$ npx skills add https://github.com/am-will/codex-skills --skill gemini-computer-use
Summary

Gemini 2.5 Computer Use browser automation with Playwright-based agent loops and safety confirmations.

Implements a screenshot-to-action cycle: capture screen, send to Gemini, parse function calls, execute in Playwright, return results until task completion or turn limit
Supports multiple browser options: bundled Chromium (default), Chrome/Edge channels via COMPUTER_USE_BROWSER_CHANNEL, or custom executables like Brave
Includes safety confirmation workflow that prompts users before executing risky UI actions flagged by the model
Provides action exclusion via --exclude flag and recommends sandboxed profiles or containers for safe operation
SKILL.md
Gemini Computer Use
Quick start

Source the env file and set your API key:

cp env.example env.sh
$EDITOR env.sh
source env.sh


Create a virtual environment and install dependencies:

python -m venv .venv
source .venv/bin/activate
pip install google-genai playwright
playwright install chromium


Run the agent script with a prompt:

python scripts/computer_use_agent.py \
  --prompt "Find the latest blog post title on example.com" \
  --start-url "https://example.com" \
  --turn-limit 6

Browser selection
Default: Playwright's bundled Chromium (no env vars required).
Choose a channel (Chrome/Edge) with COMPUTER_USE_BROWSER_CHANNEL.
Use a custom Chromium-based executable (e.g., Brave) with COMPUTER_USE_BROWSER_EXECUTABLE.

If both are set, COMPUTER_USE_BROWSER_EXECUTABLE takes precedence.

Core workflow (agent loop)
Capture a screenshot and send the user goal + screenshot to the model.
Parse function_call actions in the response.
Execute each action in Playwright.
If a safety_decision is require_confirmation, prompt the user before executing.
Send function_response objects containing the latest URL + screenshot.
Repeat until the model returns only text (no actions) or you hit the turn limit.
Operational guidance
Run in a sandboxed browser profile or container.
Use --exclude to block risky actions you do not want the model to take.
Keep the viewport at 1440x900 unless you have a reason to change it.
Resources
Script: scripts/computer_use_agent.py
Reference notes: references/google-computer-use.md
Env template: env.example
Weekly Installs
1.2K
Repository
am-will/codex-skills
GitHub Stars
907
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail