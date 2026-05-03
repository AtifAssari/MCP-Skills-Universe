---
rating: ⭐⭐⭐
title: anygen
url: https://skills.sh/anygenio/anygen-suite-skill/anygen
---

# anygen

skills/anygenio/anygen-suite-skill/anygen
anygen
Installation
$ npx skills add https://github.com/anygenio/anygen-suite-skill --skill anygen
SKILL.md
AnyGen — Content Creation Suite

This skill uses the AnyGen CLI to generate content (slides, docs, diagrams, websites, images, research, and more) server-side at www.anygen.io.

Authentication
# Web login (opens browser, auto-configures key)
anygen auth login --no-wait

# Direct API key
anygen auth login --api-key sk-xxx

# Or set env var
export ANYGEN_API_KEY=sk-xxx


When any command fails with an auth error, run anygen auth login --no-wait and ask the user to complete browser authorization. Retry after login succeeds.

How to use

Follow the anygen-workflow-generate skill. Use anygen task operations to discover the correct operation type for the user's request.

If the anygen-workflow-generate skill is not available, install it first:

anygen skill install --platform <openclaw|claude-code> -y

Weekly Installs
52
Repository
anygenio/anygen…te-skill
GitHub Stars
12
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail