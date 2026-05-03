---
rating: ⭐⭐⭐
title: docs-seeker
url: https://skills.sh/arielperez82/agents-and-skills/docs-seeker
---

# docs-seeker

skills/arielperez82/agents-and-skills/docs-seeker
docs-seeker
Installation
$ npx skills add https://github.com/arielperez82/agents-and-skills --skill docs-seeker
SKILL.md
Documentation Discovery via Scripts
Overview

Script-first documentation discovery using llms.txt standard.

Execute scripts to handle entire workflow - no manual URL construction needed.

Primary Workflow

ALWAYS execute scripts in this order:

# 1. DETECT query type (topic-specific vs general)
node scripts/detect-topic.js "<user query>"

# 2. FETCH documentation using script output
node scripts/fetch-docs.js "<user query>"

# 3. ANALYZE results (if multiple URLs returned)
cat llms.txt | node scripts/analyze-llms-txt.js -


Scripts handle URL construction, fallback chains, and error handling automatically.

Scripts

detect-topic.js - Classify query type

Identifies topic-specific vs general queries
Extracts library name + topic keyword
Returns JSON: {topic, library, isTopicSpecific}
Zero-token execution

fetch-docs.js - Retrieve documentation

Constructs context7.com URLs automatically
Handles fallback: topic → general → error
Outputs llms.txt content or error message
Zero-token execution

analyze-llms-txt.js - Process llms.txt

Categorizes URLs (critical/important/supplementary)
Recommends agent distribution (1 agent, 3 agents, 7 agents, phased)
Returns JSON with strategy
Zero-token execution
Workflow References

Topic-Specific Search - Fastest path (10-15s)

General Library Search - Comprehensive coverage (30-60s)

Repository Analysis - Fallback strategy

References

context7-patterns.md - URL patterns, known repositories

errors.md - Error handling, fallback strategies

advanced.md - Edge cases, versioning, multi-language

Execution Principles
Scripts first - Execute scripts instead of manual URL construction
Zero-token overhead - Scripts run without context loading
Automatic fallback - Scripts handle topic → general → error chains
Progressive disclosure - Load workflows/references only when needed
Agent distribution - Scripts recommend parallel agent strategy
Quick Start

Topic query: "How do I use date picker in shadcn?"

node scripts/detect-topic.js "<query>"  # → {topic, library, isTopicSpecific}
node scripts/fetch-docs.js "<query>"    # → 2-3 URLs
# Read URLs with WebFetch


General query: "Documentation for Next.js"

node scripts/detect-topic.js "<query>"         # → {isTopicSpecific: false}
node scripts/fetch-docs.js "<query>"           # → 8+ URLs
cat llms.txt | node scripts/analyze-llms-txt.js -  # → {totalUrls, distribution}
# Deploy agents per recommendation

Environment

Scripts load .env: process.env > .claude/skills/docs-seeker/.env > .claude/skills/.env > .claude/.env

See .env.example for configuration options.

Weekly Installs
14
Repository
arielperez82/ag…d-skills
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn