---
rating: ⭐⭐⭐
title: tavily-research
url: https://skills.sh/tavily-ai/skills/tavily-research
---

# tavily-research

skills/tavily-ai/skills/tavily-research
tavily-research
Installation
$ npx skills add https://github.com/tavily-ai/skills --skill tavily-research
Summary

Comprehensive AI-powered research with multi-source synthesis and citations.

Produces structured reports grounded in web sources, taking 30-120 seconds depending on model selection (mini for targeted queries, pro for complex comparisons)
Supports multiple output formats: markdown reports, JSON with custom schemas, and configurable citation styles (numbered, MLA, APA, Chicago)
Includes async workflow for long-running research via --no-wait, status, and poll commands, plus real-time streaming with --stream
Best for deep analysis, market reports, literature reviews, and multi-angle comparisons; use tavily-search instead for quick fact-finding
SKILL.md
tavily research

AI-powered deep research that gathers sources, analyzes them, and produces a cited report. Takes 30-120 seconds.

Before running any command

If tvly is not found on PATH, install it first:

curl -fsSL https://cli.tavily.com/install.sh | bash && tvly login


Do not skip this step or fall back to other tools.

See tavily-cli for alternative install methods and auth options.

When to use
You need comprehensive, multi-source analysis
The user wants a comparison, market report, or literature review
Quick searches aren't enough — you need synthesis with citations
Step 5 in the workflow: search → extract → map → crawl → research
Quick start
# Basic research (waits for completion)
tvly research "competitive landscape of AI code assistants"

# Pro model for comprehensive analysis
tvly research "electric vehicle market analysis" --model pro

# Stream results in real-time
tvly research "AI agent frameworks comparison" --stream

# Save report to file
tvly research "fintech trends 2025" --model pro -o fintech-report.md

# JSON output for agents
tvly research "quantum computing breakthroughs" --json

Options
Option	Description
--model	mini, pro, or auto (default)
--stream	Stream results in real-time
--no-wait	Return request_id immediately (async)
--output-schema	Path to JSON schema for structured output
--citation-format	numbered, mla, apa, chicago
--poll-interval	Seconds between checks (default: 10)
--timeout	Max wait seconds (default: 600)
-o, --output	Save output to file
--json	Structured JSON output
Model selection
Model	Use for	Speed
mini	Single-topic, targeted research	~30s
pro	Comprehensive multi-angle analysis	~60-120s
auto	API chooses based on complexity	Varies

Rule of thumb: "What does X do?" → mini. "X vs Y vs Z" or "best way to..." → pro.

Async workflow

For long-running research, you can start and poll separately:

# Start without waiting
tvly research "topic" --no-wait --json    # returns request_id

# Check status
tvly research status <request_id> --json

# Wait for completion
tvly research poll <request_id> --json -o result.json

Tips
Research takes 30-120 seconds — use --stream to see progress in real-time.
Use --model pro for complex comparisons or multi-faceted topics.
Use --output-schema to get structured JSON output matching a custom schema.
For quick facts, use tvly search instead — research is for deep synthesis.
Read from stdin: echo "query" | tvly research - --json
See also
tavily-search — quick web search for simple lookups
tavily-crawl — bulk extract from a site for your own analysis
Weekly Installs
8.1K
Repository
tavily-ai/skills
GitHub Stars
259
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail