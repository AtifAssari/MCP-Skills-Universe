---
rating: ⭐⭐
title: deepxiv
url: https://skills.sh/wanshuiyin/auto-claude-code-research-in-sleep/deepxiv
---

# deepxiv

skills/wanshuiyin/auto-claude-code-research-in-sleep/deepxiv
deepxiv
Installation
$ npx skills add https://github.com/wanshuiyin/auto-claude-code-research-in-sleep --skill deepxiv
SKILL.md
DeepXiv Paper Search & Progressive Reading

Search topic or paper ID: $ARGUMENTS

Role & Positioning

DeepXiv is the progressive-reading literature source:

Skill	Best for
/arxiv	Direct preprint search and PDF download
/semantic-scholar	Published venue metadata, citation counts, DOI links
/deepxiv	Layered reading: search → brief → head → section, plus trending and web search

Use DeepXiv when you want to avoid loading full papers too early.

Constants
FETCH_SCRIPT — tools/deepxiv_fetch.py relative to the current project. If unavailable, fall back to the raw deepxiv CLI.
MAX_RESULTS = 10 — Default number of results to return.

Overrides (append to arguments):

/deepxiv "agent memory" - max: 5 — top 5 results
/deepxiv "2409.05591" - brief — quick paper summary
/deepxiv "2409.05591" - head — metadata + section overview
/deepxiv "2409.05591" - section: Introduction — read one section only
/deepxiv "trending" - days: 14 - max: 10 — trending papers
/deepxiv "karpathy" - web — DeepXiv web search
/deepxiv "258001" - sc — Semantic Scholar metadata by ID
Setup

DeepXiv is optional. If the CLI is not installed, tell the user:

pip install deepxiv-sdk


On first use, deepxiv auto-registers a free token and stores it in ~/.env.

Workflow
Step 1: Parse Arguments

Parse $ARGUMENTS for:

Query or ID: a paper topic, arXiv ID, or Semantic Scholar ID
- max: N: override MAX_RESULTS
- brief: fetch paper brief
- head: fetch metadata and section map
- section: NAME: fetch one named section
- trending or query trending: fetch trending papers
- days: 7|14|30: trending time window
- web: run DeepXiv web search
- sc: fetch Semantic Scholar metadata by ID

If the main argument looks like an arXiv ID and no explicit mode is given, default to - brief.

Step 2: Locate the Adapter

Prefer the ARIS adapter:

python3 tools/deepxiv_fetch.py --help


If tools/deepxiv_fetch.py is not available, fall back to raw deepxiv commands.

Step 3: Execute the Minimal Command

Search papers

python3 tools/deepxiv_fetch.py search "QUERY" --max MAX_RESULTS


Fallback:

deepxiv search "QUERY" --limit MAX_RESULTS --format json


Brief summary

python3 tools/deepxiv_fetch.py paper-brief ARXIV_ID


Fallback:

deepxiv paper ARXIV_ID --brief --format json


Section map

python3 tools/deepxiv_fetch.py paper-head ARXIV_ID


Fallback:

deepxiv paper ARXIV_ID --head --format json


Specific section

python3 tools/deepxiv_fetch.py paper-section ARXIV_ID "SECTION_NAME"


Fallback:

deepxiv paper ARXIV_ID --section "SECTION_NAME" --format json


Trending

python3 tools/deepxiv_fetch.py trending --days 7 --max MAX_RESULTS


Fallback:

deepxiv trending --days 7 --limit MAX_RESULTS --output json


Web search

python3 tools/deepxiv_fetch.py wsearch "QUERY"


Fallback:

deepxiv wsearch "QUERY" --output json


Semantic Scholar metadata

python3 tools/deepxiv_fetch.py sc "SEMANTIC_SCHOLAR_ID"


Fallback:

deepxiv sc "SEMANTIC_SCHOLAR_ID" --output json

Step 4: Present Results

When searching, present a compact table:

| # | ID | Title | Year | Citations | Notes |
|---|----|-------|------|-----------|-------|


When reading a paper, show:

title
arXiv ID
authors
venue/date if available
TLDR or abstract summary
suggested next step: brief → head → section
Step 5: Escalate Depth Only When Needed

Use this progression:

search
paper-brief
paper-head
paper-section
full paper only if necessary

Do not jump to full-paper reads when a brief or one section answers the question.

Step 6: Update Research Wiki (if active)

Required when research-wiki/ exists in the project; skip silently otherwise. Ingest papers that were meaningfully read (brief / head / section / full) during this invocation — mere search hits without a depth read do not need ingestion:

if [ -d research-wiki/ ]:
    for each arxiv_id the user asked this skill to read in depth:
        python3 tools/research_wiki.py ingest_paper research-wiki/ \
            --arxiv-id "<arxiv_id>"


The helper handles metadata / slug / dedup / page / index / log in one call — do not handwrite papers/<slug>.md. See shared-references/integration-contract.md. Backfill missed ingests with python3 tools/research_wiki.py sync research-wiki/ --arxiv-ids <id1>,<id2>,....

Key Rules
Prefer the adapter script over raw deepxiv commands when available.
DeepXiv is optional. If unavailable, give the install command and suggest /arxiv or /research-lit "topic" - sources: web.
Use section-level reads to save tokens.
Treat DeepXiv as complementary to /arxiv and /semantic-scholar, not a replacement.
If the result overlaps with a published venue paper from Semantic Scholar, keep the richer venue metadata in the final summary.
Weekly Installs
41
Repository
wanshuiyin/auto…in-sleep
GitHub Stars
7.9K
First Seen
4 days ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass