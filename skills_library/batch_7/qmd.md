---
title: qmd
url: https://skills.sh/tobi/qmd/qmd
---

# qmd

skills/tobi/qmd/qmd
qmd
Installation
$ npx skills add https://github.com/tobi/qmd --skill qmd
Summary

Local markdown search engine supporting keyword, semantic, and hypothetical-document queries across indexed collections.

Three query types: lex (BM25 keyword matching), vec (semantic/natural language), and hyde (hypothetical document answers) with optional auto-expansion and intent-based disambiguation
Accessible via MCP tools (query, get, multi_get), CLI commands, and HTTP API on port 8181
Supports collection filtering, phrase matching, term exclusion, and result reranking via reciprocal rank fusion and LLM-based scoring
Requires local installation (npm install -g @tobilu/qmd) and indexed markdown collections set up via qmd collection add and qmd embed
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

QMD - Quick Markdown Search

Local search engine for markdown content.

Status

!qmd status 2>/dev/null || echo "Not installed: npm install -g @tobilu/qmd"

MCP: query
{
  "searches": [
    { "type": "lex", "query": "CAP theorem consistency" },
    { "type": "vec", "query": "tradeoff between consistency and availability" }
  ],
  "collections": ["docs"],
  "limit": 10
}

Query Types
Type	Method	Input
lex	BM25	Keywords — exact terms, names, code
vec	Vector	Question — natural language
hyde	Vector	Answer — hypothetical result (50-100 words)
Writing Good Queries

lex (keyword)

2-5 terms, no filler words
Exact phrase: "connection pool" (quoted)
Exclude terms: performance -sports (minus prefix)
Code identifiers work: handleError async

vec (semantic)

Full natural language question
Be specific: "how does the rate limiter handle burst traffic"
Include context: "in the payment service, how are refunds processed"

hyde (hypothetical document)

Write 50-100 words of what the answer looks like
Use the vocabulary you expect in the result

expand (auto-expand)

Use a single-line query (implicit) or expand: question on its own line
Lets the local LLM generate lex/vec/hyde variations
Do not mix expand: with other typed lines — it's either a standalone expand query or a full query document
Intent (Disambiguation)

When a query term is ambiguous, add intent to steer results:

{
  "searches": [
    { "type": "lex", "query": "performance" }
  ],
  "intent": "web page load times and Core Web Vitals"
}


Intent affects expansion, reranking, chunk selection, and snippet extraction. It does not search on its own — it's a steering signal that disambiguates queries like "performance" (web-perf vs team health vs fitness).

Combining Types
Goal	Approach
Know exact terms	lex only
Don't know vocabulary	Use a single-line query (implicit expand:) or vec
Best recall	lex + vec
Complex topic	lex + vec + hyde
Ambiguous query	Add intent to any combination above

First query gets 2x weight in fusion — put your best guess first.

Lex Query Syntax
Syntax	Meaning	Example
term	Prefix match	perf matches "performance"
"phrase"	Exact phrase	"rate limiter"
-term	Exclude	performance -sports

Note: -term only works in lex queries, not vec/hyde.

Collection Filtering
{ "collections": ["docs"] }              // Single
{ "collections": ["docs", "notes"] }     // Multiple (OR)


Omit to search all collections.

Other MCP Tools
Tool	Use
get	Retrieve doc by path or #docid
multi_get	Retrieve multiple by glob/list
status	Collections and health
CLI
qmd query "question"              # Auto-expand + rerank
qmd query $'lex: X\nvec: Y'       # Structured
qmd query $'expand: question'     # Explicit expand
qmd query --json --explain "q"    # Show score traces (RRF + rerank blend)
qmd search "keywords"             # BM25 only (no LLM)
qmd get "#abc123"                 # By docid
qmd multi-get "journals/2026-*.md" -l 40  # Batch pull snippets by glob
qmd multi-get notes/foo.md,notes/bar.md   # Comma-separated list, preserves order

HTTP API
curl -X POST http://localhost:8181/query \
  -H "Content-Type: application/json" \
  -d '{"searches": [{"type": "lex", "query": "test"}]}'

Setup
npm install -g @tobilu/qmd
qmd collection add ~/notes --name notes
qmd embed

Weekly Installs
1.9K
Repository
tobi/qmd
GitHub Stars
23.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass