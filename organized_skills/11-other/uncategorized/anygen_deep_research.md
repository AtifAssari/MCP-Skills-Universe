---
rating: ⭐⭐⭐
title: anygen-deep-research
url: https://skills.sh/anygenio/anygen-skills/anygen-deep-research
---

# anygen-deep-research

skills/anygenio/anygen-skills/anygen-deep-research
anygen-deep-research
Installation
$ npx skills add https://github.com/anygenio/anygen-skills --skill anygen-deep-research
SKILL.md
AI Deep Research — AnyGen

This skill uses the AnyGen CLI to generate in-depth research and analysis reports server-side at www.anygen.io.

Authentication
# Web login (opens browser, auto-configures key)
anygen auth login --no-wait

# Direct API key
anygen auth login --api-key sk-xxx

# Or set env var
export ANYGEN_API_KEY=sk-xxx


When any command fails with an auth error, run anygen auth login --no-wait and ask the user to complete browser authorization. Retry after login succeeds.

How to use

Follow the anygen-workflow-generate skill with operation type deep_research.

If the anygen-workflow-generate skill is not available, install it first:

anygen skill install --platform <openclaw|claude-code> -y

Weekly Installs
51
Repository
anygenio/anygen-skills
GitHub Stars
60
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn