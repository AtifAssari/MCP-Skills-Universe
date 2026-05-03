---
rating: ⭐⭐⭐
title: browser-automation-parity
url: https://skills.sh/terryjyu/browser-automation-parity-skill/browser-automation-parity
---

# browser-automation-parity

skills/terryjyu/browser-automation-parity-skill/browser-automation-parity
browser-automation-parity
Installation
$ npx skills add https://github.com/terryjyu/browser-automation-parity-skill --skill browser-automation-parity
SKILL.md
Browser Automation Parity

Eliminate the gap between Browser Subagent mode (interactive, DOM-level reasoning) and Run mode (headless Python + Playwright) in Google Antigravity.

The core problem: automation that "passes" with subagent guidance silently fails or diverges when replayed as plain Python. This skill makes run mode observable, self-checking, and debuggable at step granularity.

When to Use
Automation passes under Browser Subagent but fails (or silently diverges) in Python replay
A missed click, paste, or navigation causes wrong results with unclear root cause
You need CI-grade reproducibility with rich diagnostics
Building any Playwright automation that should be production-grade
Key Principles
1. Every action is a checked contract

A browser action is not "done" until its postcondition is verified. Structure every meaningful interaction as:

precondition → action → postcondition


Postcondition examples: URL changed to expected route, target element became visible, success toast appeared, network request returned expected status, DOM attribute matches expected value.

Never assume a click landed. Always verify the expected state change occurred.

2. Step-level observability is mandatory

For every meaningful step, capture: step name, selector(s) used, timestamps and duration, URL before and after, screenshot on failure (optionally before/after on success), and relevant console logs or network activity.

Emit all step events to a structured JSONL log so failures can be diagnosed without re-running.

3. Playwright tracing for failure forensics

Enable Playwright's Trace Viewer artifacts on failure. Traces include action timeline, DOM snapshots, screencast frames, and network logs — everything needed to diagnose "it worked interactively but not headless."

Use retain-on-failure tracing so passing runs stay lightweight while failures get full diagnostics.

4. Browser Subagent is the debugger, not the executor

The goal is for Python scripts to be the executor. When something fails, the subagent's role is to examine the trace artifacts, screenshots, and step logs, then prescribe fixes to the Python code — not to re-run the workflow interactively.

Implementation

Read the reference files for detailed implementation guidance:

references/step-contract.md — The step context manager, precondition/postcondition API, and retry logic. Read this first.
references/tracing-setup.md — Playwright tracing configuration, artifact retention, and Trace Viewer integration.
references/diagnostics.md — Step log format, failure reports, and how to hand off artifacts to the Browser Subagent for debugging.
scripts/step_contract.py — Ready-to-use step contract module. Copy into your project.
scripts/example_workflow.py — Example automation using the step contract pattern.
Quick Start
Copy scripts/step_contract.py into your project
Wrap each meaningful browser action in a step() context manager
Add postcondition checks after each action
Enable tracing with retain-on-failure mode
Run your automation — on failure, examine artifacts/steps.jsonl and any .zip traces
from step_contract import step, check, TracingConfig

async def my_workflow(page, artifacts_dir="./artifacts"):
    async with step("login", page, artifacts_dir) as s:
        await page.fill("#email", "user@example.com")
        await page.fill("#password", "secret")
        await page.click("button[type=submit]")
        await check(s, lambda: "dashboard" in page.url, "should navigate to dashboard")

    async with step("create_item", page, artifacts_dir) as s:
        await page.click("[data-testid=new-item]")
        await check(s, lambda: page.locator(".item-form").is_visible(),
                    "item form should appear")

Workflow: Diagnosing a Run Mode Failure
Run the automation — it fails or produces wrong results
Examine steps.jsonl — find the first step with "status": "fail" or unexpected postcondition failure
Open the failure screenshot — see what the page actually looked like
Open the Playwright trace (if enabled) — npx playwright show-trace trace.zip
Hand artifacts to Browser Subagent — ask it to examine the trace/screenshots and suggest code fixes
Apply fixes to the Python script — not to a subagent session
Re-run — verify the fix in headless mode

This keeps the subagent as a diagnostic tool rather than a crutch.

Weekly Installs
10
Repository
terryjyu/browse…ty-skill
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn