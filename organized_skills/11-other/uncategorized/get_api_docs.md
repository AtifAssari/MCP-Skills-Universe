---
rating: ⭐⭐
title: get-api-docs
url: https://skills.sh/andrewyng/context-hub/get-api-docs
---

# get-api-docs

skills/andrewyng/context-hub/get-api-docs
get-api-docs
Installation
$ npx skills add https://github.com/andrewyng/context-hub --skill get-api-docs
SKILL.md
Get API Docs via chub

When you need documentation for a library or API, fetch it with the chub CLI rather than guessing from training data. This gives you the current, correct API.

Step 1 - Ensure chub exists and get the latest instructions for using it

Run

chub --help


If this results in an error showing that chub does not exist, then install it first, and run it again. If the environment has node, npm, network access, and package-manager permission, install it as follows:

npm install -g @aisuite/chub

Step 2 — Find the right documents

If there is a conflict, follow the instructions from the output of chub --help since that will be the latest guidance. However, a key command for searching for the right documentation is chub search:

chub search "<keywords>" --json


Pick the best-matching id from the results (e.g. openai/chat, anthropic/sdk, stripe/api). If nothing matches, try some broader terms.

Step 3 — Fetch the docs

Again, follow the latest instructions from chub --help instead of this if there is a conflict. But a key command for fetching the relevant docs is:

chub get <id> --lang py    # or --lang js, --lang ts


Remember to include the --lang parameter.

Step 4 — Use the docs and leave feedback

Read the fetched content and use it to write accurate code or answer the question. Do not rely on memorized API shapes — use what the docs say.

Finally, after completing the task, if you discovered something not in the doc — a gotcha, workaround, version quirk, or project-specific detail — save it so future sessions start smarter:

chub annotate <id> "Webhook verification requires raw body — do not parse before verifying"


Annotations are local, persist across sessions, and appear automatically on future chub get calls. Keep notes concise and actionable. Don't repeat what's already in the doc.

Additionally, to help all developers, give feedback on the documentation using chub feedback, following the instructions in chub --help . Do not include secrets, source code, private architecture details, or other sensitive information in feedback comments.

Weekly Installs
536
Repository
andrewyng/context-hub
GitHub Stars
13.1K
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn