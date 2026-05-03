---
rating: ⭐⭐
title: model-healthcheck
url: https://skills.sh/xmanrui/model-healthcheck/model-healthcheck
---

# model-healthcheck

skills/xmanrui/model-healthcheck/model-healthcheck
model-healthcheck
Installation
$ npx skills add https://github.com/xmanrui/model-healthcheck --skill model-healthcheck
SKILL.md
Model Healthcheck Skill

When the user requests a model test, follow these steps:

Steps

Get all model list Use gateway config.get to read the current config and extract all provider/model combinations from models.providers.

Test all models concurrently For each model, use sessions_spawn to run a test:

task: "Reply with exactly: model ok. Only reply these two words."
model: the corresponding provider/model-id
runTimeoutSeconds: 30
cleanup: "delete"

Fire all tests concurrently (multiple sessions_spawn calls at once), do not test sequentially.

Collect results and summarize Wait for all tests to complete, then summarize as a list:

provider/model-id — ✅ OK / ❌ Failed (Xs) — error message if any

Fields:

Status: normal reply = ✅, timeout or error = ❌
Duration: time from spawn to result
Error: if failed, show the specific error (API error, timeout, auth failure, etc.)

Output results Send the summary to the user, with a final tally:

Total models tested: X
Passed: X
Failed: X (list failed model names and reasons)
Notes
Skip the model currently in use (no need to test yourself)
If the user specifies a particular model, only test that one
Feishu/WhatsApp and similar platforms don't support markdown tables — use list format instead
Weekly Installs
8
Repository
xmanrui/model-h…lthcheck
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass