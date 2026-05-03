---
title: auto-skill-generator
url: https://skills.sh/benchflow-ai/skillsbench/auto-skill-generator
---

# auto-skill-generator

skills/benchflow-ai/skillsbench/auto-skill-generator
auto-skill-generator
Installation
$ npx skills add https://github.com/benchflow-ai/skillsbench --skill auto-skill-generator
SKILL.md
Auto Skill Generator

Generate skills by researching and crawling authoritative documentation.

Tool: fetch_docs.py
# Search - returns all URLs with snippets
python scripts/fetch_docs.py search "Modal GPU Python documentation"

# Crawl - with domain/path filtering to stay focused
python scripts/fetch_docs.py crawl \
  --url https://modal.com/docs/guide/gpu \
  --no-external \
  --select-paths "/docs/.*" \
  --instructions "Focus on GPU setup and code examples" \
  --limit 30

Workflow
1. Search for Documentation
python scripts/fetch_docs.py search "{topic} documentation"


Returns JSON with all URLs, titles, scores, and content snippets.

2. Select Best URL

Review search results and select based on:

Official docs: *.com/docs/, docs.*.com, *.readthedocs.io
Content relevance: Check snippets for API docs, code examples
Avoid: Blog posts, changelogs, marketing, glossaries
3. Crawl with Filtering
python scripts/fetch_docs.py crawl \
  --url {selected_url} \
  --no-external \
  --select-paths "/docs/.*" "/guide/.*" \
  --instructions "Focus on API methods and code examples"


Core Parameters:

Parameter	Description
--url	Required. URL to crawl
--instructions	Natural language guidance for crawler
--limit	Total pages (default: 50)
--max-depth	Link depth (default: 2)

Domain/Path Filtering (Critical):

Parameter	Description
--no-external	Block external domains
--select-paths	Regex patterns to include (e.g., /docs/.*)
--exclude-paths	Regex patterns to exclude (e.g., /blog/.*)
--select-domains	Regex for allowed domains
--exclude-domains	Regex for blocked domains

Quality Options:

Parameter	Description
--extract-depth	basic (1 credit/5 URLs) or advanced (2 credits/5 URLs)
--format	markdown or text
--timeout	Seconds (10-150, default: 150)
4. Generate Skill File

From crawled content, create:

---
name: {topic-slug}ß
description: >
  {What the skill does}. Use when: {specific triggers}.
---

# {Topic Name}

## Quick Start
## Core API
## Common Patterns

Output
Location: ~/.claude/skills/{topic-slug}/SKILL.md
Extract ALL code blocks from crawled content
Keep SKILL.md under 500 lines; split to references/ if longer
Weekly Installs
29
Repository
benchflow-ai/skillsbench
GitHub Stars
1.1K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn