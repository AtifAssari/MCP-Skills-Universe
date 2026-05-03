---
title: parallel-web-extract
url: https://skills.sh/parallel-web/parallel-agent-skills/parallel-web-extract
---

# parallel-web-extract

skills/parallel-web/parallel-agent-skills/parallel-web-extract
parallel-web-extract
Installation
$ npx skills add https://github.com/parallel-web/parallel-agent-skills --skill parallel-web-extract
Summary

Extract content from multiple URLs in parallel, token-efficiently.

Handles webpages, articles, PDFs, and JavaScript-heavy sites with a single command
Runs in a forked context to minimize token overhead compared to built-in WebFetch
Supports batch extraction of multiple URLs with optional focus objectives
Requires parallel-cli installation and authentication; outputs extracted content as markdown to a local file for follow-up queries
SKILL.md
URL Extraction

Extract content from: $ARGUMENTS

Command

Choose a short, descriptive filename based on the URL or content (e.g., vespa-docs, react-hooks-api). Use lowercase with hyphens, no spaces.

parallel-cli extract "$ARGUMENTS" --json -o "/tmp/$FILENAME.md"


Options if needed:

--objective "focus area" to focus on specific content
Response format

Return content as:

Page Title

Then the extracted content verbatim, with these rules:

Keep content verbatim - do not paraphrase or summarize
Parse lists exhaustively - extract EVERY numbered/bulleted item
Strip only obvious noise: nav menus, footers, ads
Preserve all facts, names, numbers, dates, quotes

After the response, mention the output file path (/tmp/$FILENAME.md) so the user knows it's available for follow-up questions.

Setup

If parallel-cli is not found, install and authenticate:

curl -fsSL https://parallel.ai/install.sh | bash


If unable to install that way, install via pipx instead:

pipx install "parallel-web-tools[cli]"
pipx ensurepath


Then authenticate:

parallel-cli login


Or set an API key: export PARALLEL_API_KEY="your-key"

Weekly Installs
1.1K
Repository
parallel-web/pa…t-skills
GitHub Stars
46
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail