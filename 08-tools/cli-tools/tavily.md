---
title: tavily
url: https://skills.sh/lag0/tavily-cli/tavily
---

# tavily

skills/lag0/tavily-cli/tavily
tavily
Installation
$ npx skills add https://github.com/lag0/tavily-cli --skill tavily
SKILL.md
Tavily CLI

Search, extract, map, crawl, and research from the terminal with Tavily.

Run tavily --help or tavily <command> --help for full option details.

Prerequisites

Must be installed and authenticated.

Check:

tavily status


If not authenticated:

tavily login


If not installed/configured, follow rules/install.md. For output handling and untrusted content guidelines, follow rules/security.md.

Workflow

Use this escalation pattern:

Search - no exact URL yet, need discovery.
Extract - already have URL(s), need content.
Map - need URL discovery within one site before extracting.
Crawl - need bulk content from a site section.
Research - need synthesized output and citations from Tavily research API.
Research Status - track/poll an existing research request.
Need	Command	When
Discover sources on a topic	search	No trusted URL yet
Get page content from URL(s)	extract	URL(s) already known
Discover pages inside a domain	map	Need URL inventory/filtering
Bulk extract many pages	crawl	Need multi-page dataset
Run guided long-form research	research	Need synthesis, not raw pages
Poll existing research job	research-status	Have request-id already

What this CLI does not provide today:

No dedicated browser automation command.
No dedicated download command.
No dedicated agent command (use research instead).
Output and Organization

Unless user requests inline output, write to .tavily/:

mkdir -p .tavily
tavily search "latest AI agent frameworks" --json -o .tavily/search-agent-frameworks.json
tavily extract "https://docs.tavily.com" -o .tavily/docs-tavily.md


Keep .tavily/ in .gitignore.

Always quote URLs because ? and & are shell-sensitive:

tavily extract "https://example.com/docs?page=2&lang=en" -o .tavily/page2.md


Read large outputs incrementally:

wc -l .tavily/result.json
head -n 60 .tavily/result.json
rg -n "keyword|error|failed" .tavily/result.json


Suggested naming:

.tavily/search-{topic}.json
.tavily/map-{site}.json
.tavily/crawl-{site}.json
.tavily/extract-{site}-{slug}.md
.tavily/research-{topic}.json

Commands
search

Discover results for a query. Useful first step before extraction/crawl.

# Basic JSON search output
tavily search "best vector databases 2026" --json --pretty -o .tavily/search-vector-db.json

# News-focused search in recent time window
tavily search "AI regulation US" --topic news --time-range month --max-results 8 --json -o .tavily/search-ai-regulation.json

# Domain-constrained search with answer/raw content
tavily search "authentication pattern" \
  --include-domains "docs.tavily.com,developer.mozilla.org" \
  --include-answer \
  --include-raw-content \
  --json -o .tavily/search-auth.json


Key options: --max-results, --search-depth, --topic, --time-range, --start-date, --end-date, --include-domains, --exclude-domains, --country, --include-raw-content, --include-images, --include-answer, -o, --json, --pretty.

extract

Extract content from one or many known URLs.

# Single URL
tavily extract "https://docs.tavily.com" --format markdown -o .tavily/extract-docs.md

# Multiple URLs in one call
tavily extract "https://docs.tavily.com" "https://docs.tavily.com/api-reference" \
  --extract-depth advanced \
  --include-images \
  --json -o .tavily/extract-docs-multi.json

# Add relevance query and chunk control
tavily extract "https://example.com/long-page" \
  --query "pricing limits and rate limits" \
  --chunks-per-source 5 \
  --timeout 30 \
  --json -o .tavily/extract-pricing.json


Key options: -u, --url, positional [urls...], --extract-depth, --format, --include-images, --timeout, --query, --chunks-per-source, -o, --json, --pretty.

map

Discover URLs on a site before extraction/crawl.

# Full map with limits
tavily map "https://docs.tavily.com" --max-depth 2 --limit 200 --json -o .tavily/map-docs.json

# Filter by paths/domains
tavily map "https://example.com" \
  --select-paths "/docs,/api" \
  --exclude-paths "/blog,/changelog" \
  --json -o .tavily/map-filtered.json


Key options: --max-depth, --max-breadth, --limit, --select-paths, --select-domains, --exclude-paths, --exclude-domains, --allow-external, --instructions, --timeout, -o, --json, --pretty.

crawl

Bulk extract many pages from a site section.

# Crawl docs section only
tavily crawl "https://docs.tavily.com" \
  --select-paths "/docs,/api-reference" \
  --max-depth 2 \
  --limit 80 \
  --json -o .tavily/crawl-docs.json

# Crawl with advanced extract options
tavily crawl "https://example.com" \
  --extract-depth advanced \
  --include-images \
  --chunks-per-source 4 \
  --timeout 45 \
  --json -o .tavily/crawl-example.json


Key options: --max-depth, --max-breadth, --limit, --extract-depth, --select-paths, --exclude-paths, --allow-external, --include-images, --instructions, --format, --timeout, --chunks-per-source, -o, --json, --pretty.

research

Start Tavily research generation.

# Basic research request
tavily research "Compare RAG chunking strategies for legal documents" \
  --model pro \
  --json -o .tavily/research-rag.json

# Stream output while running
tavily research "Summarize latest agent memory patterns" \
  --stream \
  -o .tavily/research-agent-memory.txt

# Structured output schema
tavily research "List top observability tools" \
  --output-schema '{"type":"object","properties":{"tools":{"type":"array","items":{"type":"string"}}}}' \
  --json -o .tavily/research-tools-structured.json


Key options: --model, --citation-format, --timeout, --stream, --output-schema, -o, --json, --pretty.

research-status

Poll an existing research request by id.

tavily research-status "req_123456789" --json --pretty -o .tavily/research-status.json


Key options: -o, --json, --pretty.

auth and setup commands
# Authenticate interactively (never pass secrets as CLI args)
tavily login

# Check auth/version status
tavily status

# Remove saved credentials
tavily logout

# Pull key into local .env
tavily env --file .env --overwrite

# Install integrations independently
tavily setup skills
tavily setup mcp

Working with Results

Use jq, rg, and targeted reads for analysis:

# Search: list title + URL
jq -r '.results[] | "\(.title)\t\(.url)"' .tavily/search-agent-frameworks.json

# Map: list URLs
jq -r '.results[]' .tavily/map-docs.json

# Crawl: collect crawled URLs
jq -r '.results[]?.url // empty' .tavily/crawl-docs.json

# Extract: show failures only
jq -r '.failedResults[]? | "\(.url)\t\(.error)"' .tavily/extract-docs-multi.json

# Research: inspect status and request id
jq -r '.requestId, .status' .tavily/research-rag.json

Parallelization

Prefer these patterns:

Use one extract call with multiple URLs when task scope is one batch.
Use shell parallelism only for independent targets and moderate concurrency.
# Built-in multi URL batch in one request
tavily extract "https://site-a.com" "https://site-b.com" "https://site-c.com" \
  --json -o .tavily/extract-batch.json

# Independent parallel jobs (throttle conservatively)
tavily crawl "https://docs.site-a.com" --limit 40 --json -o .tavily/crawl-a.json &
tavily crawl "https://docs.site-b.com" --limit 40 --json -o .tavily/crawl-b.json &
wait


Do not launch large parallel bursts blindly. Respect API quota/rate limits and monitor failures before scaling up.

Bulk Workflows (Tavily Equivalent)

There is no dedicated download command. Use map/crawl/extract pipelines:

# 1) Map docs URLs
tavily map "https://docs.example.com" --select-paths "/docs" --json -o .tavily/map-docs.json

# 2) Extract mapped URLs in controlled batches
jq -r '.results[]' .tavily/map-docs.json | head -n 30 > .tavily/map-docs-30.txt
while IFS= read -r url; do
  slug="$(echo "$url" | sed 's#^https://##; s#^http://##; s#[^a-zA-Z0-9._-]#-#g')"
  tavily extract "$url" --json -o ".tavily/extract-${slug}.json"
done < .tavily/map-docs-30.txt


Alternative bulk path:

tavily crawl "https://docs.example.com" --select-paths "/docs" --max-depth 2 --limit 100 --json -o .tavily/crawl-docs.json

Failure Handling
If command fails with auth error: run tavily status, then tavily login.
If URL extraction fails: inspect .failedResults from JSON output and retry only failed URLs.
If output is too large: reduce --limit / depth and split into multiple focused runs.
If parsing JSON outputs: ensure --json was used or output file uses .json extension.
Weekly Installs
20
Repository
lag0/tavily-cli
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail