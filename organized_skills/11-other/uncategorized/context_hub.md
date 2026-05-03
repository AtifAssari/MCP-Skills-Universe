---
rating: ⭐⭐
title: context-hub
url: https://skills.sh/luongnv89/skills/context-hub
---

# context-hub

skills/luongnv89/skills/context-hub
context-hub
Installation
$ npx skills add https://github.com/luongnv89/skills --skill context-hub
SKILL.md
Context Hub

Use chub as the default source of truth for third-party API/SDK behavior.

When to Use

Trigger this skill whenever a task involves:

Writing or reviewing code that calls an external API or SDK (OpenAI, Stripe, Anthropic, Pinecone, Twilio, etc.)
Implementing webhooks, auth flows (OAuth, API keys, JWTs), or library-specific method calls
Debugging integration errors where the root cause may be an outdated API contract
Migrating to a new version of an SDK or third-party library

Even if the user does not explicitly ask for documentation — fetch first, code second.

Repo Sync Before Edits (mandatory)

Before creating/updating/deleting files in an existing repository, sync the current branch with remote:

branch="$(git rev-parse --abbrev-ref HEAD)"
git fetch origin
git pull --rebase origin "$branch"


If the working tree is not clean, stash first, sync, then restore:

git stash push -u -m "pre-sync"
branch="$(git rev-parse --abbrev-ref HEAD)"
git fetch origin && git pull --rebase origin "$branch"
git stash pop


If origin is missing, pull is unavailable, or rebase/stash conflicts occur, stop and ask the user before continuing.

1) Ensure chub is ready

Run:

chub help
chub update


If chub is not installed and installation is allowed, run:

npm install -g @aisuite/chub


If installation is blocked, tell the user and use official docs directly.

2) Identify target docs

Run:

chub search "<library or API name>" --json


Choose the best id (<author>/<name>, for example openai/chat, stripe/api). If results are weak, retry with broader keywords.

3) Fetch language-specific docs

Run:

chub get <id> --lang py


Use the project language (py, js, ts) when variants exist. Omit --lang when only one variant is available.

Prefer focused fetches when possible:

chub get <id> --file <reference-file>


Use --full only when full package context is required.

4) Implement from fetched docs only

Write code and explanations from fetched docs. Do not guess method names, payload fields, endpoint paths, or auth headers. When uncertain, fetch again instead of inferring.

5) Capture durable learnings

If you discover a real gap (gotcha, workaround, version quirk), store it:

chub annotate <id> "<concise actionable note>"


Keep notes short, concrete, and non-duplicative.

6) Submit doc feedback only with user approval

Ask the user before sending feedback.

chub feedback <id> up
chub feedback <id> down --label outdated


Common labels: outdated, inaccurate, incomplete, wrong-examples, wrong-version, poorly-structured, accurate, well-structured, helpful, good-examples.

Quick commands
chub search "stripe"
chub get stripe/api --lang js
chub annotate stripe/api "Webhook verification requires raw body"
chub annotate --list

Expected Output

After a successful doc fetch, the skill provides:

Confirmation of which doc ID was fetched, e.g.:
Fetched: stripe/api (Python) — 42 KB, last updated 2025-03-14

Implementation — code written strictly from the fetched docs, with no guessed fields or method names
Annotation (when a new gotcha is discovered):
Annotated stripe/api: "Webhook verification requires raw request body, not parsed JSON"


If chub is unavailable and installation is blocked, the skill falls back to the official docs URL and states this explicitly.

Edge Cases
Scenario	Handling
chub not installed, installation blocked	Inform user; fetch docs directly from the official library website via /browse
chub search returns no results	Retry with broader keywords; if still empty, use official docs URL directly
Fetched docs are clearly outdated	Annotate the issue; cross-reference with official changelog before coding
Multiple language variants available	Ask the user which language to fetch if not determinable from project context
chub annotate or feedback commands fail	Log the failure; continue with implementation; do not block on annotation errors
chub update hangs or errors	Skip update, use cached docs, and note that docs may not be the latest version
Step Completion Reports

After completing each major step, output a status report in this format:

◆ [Step Name] ([step N of M] — [context])
··································································
  [Check 1]:          √ pass
  [Check 2]:          √ pass (note if relevant)
  [Check 3]:          × fail — [reason]
  [Check 4]:          √ pass
  [Criteria]:         √ N/M met
  ____________________________
  Result:             PASS | FAIL | PARTIAL


Adapt the check names to match what the step actually validates. Use √ for pass, × for fail, and — to add brief context. The "Criteria" line summarizes how many acceptance criteria were met. The "Result" line gives the overall verdict.

Skill-specific checks per phase

Phase: Tool Readiness — checks: chub availability, chub updated

Phase: Documentation Fetch — checks: Doc identification, Doc fetch success

Phase: Implementation — checks: Implementation accuracy, No guessed fields

Phase: Learning Capture — checks: Annotation saved, Note non-duplicative

Weekly Installs
19
Repository
luongnv89/skills
GitHub Stars
68
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn