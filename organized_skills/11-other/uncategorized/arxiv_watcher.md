---
rating: ⭐⭐⭐
title: arxiv-watcher
url: https://skills.sh/site/skills.volces.com/arxiv-watcher
---

# arxiv-watcher

skills/skills.volces.com/arxiv-watcher
arxiv-watcher
$ npx skills add https://skills.volces.com/skills/clawhub/rubenfb23@arxiv-watcher
SKILL.md
ArXiv Watcher

This skill interacts with the ArXiv API to find and summarize the latest research papers.

Capabilities
Search: Find papers by keyword, author, or category.
Summarize: Fetch the abstract and provide a concise summary.
Save to Memory: Automatically record summarized papers to memory/RESEARCH_LOG.md for long-term tracking.
Deep Dive: Use web_fetch on the PDF link to extract more details if requested.
Workflow
Use scripts/search_arxiv.sh "<query>" to get the XML results.
Parse the XML (look for <entry>, <title>, <summary>, and <link title="pdf">).
Present the findings to the user.
MANDATORY: Append the title, authors, date, and summary of any paper discussed to memory/RESEARCH_LOG.md. Use the format:
### [YYYY-MM-DD] TITLE_OF_PAPER
- **Authors**: Author List
- **Link**: ArXiv Link
- **Summary**: Brief summary of the paper and its relevance.

Examples
"Busca los últimos papers sobre LLM reasoning en ArXiv."
"Dime de qué trata el paper con ID 2512.08769."
"Hazme un resumen de las novedades de hoy en ArXiv sobre agentes."
Resources
scripts/search_arxiv.sh: Direct API access script.
Weekly Installs
17
Source
skills.volces.c…-watcher
First Seen
Mar 24, 2026