---
rating: ⭐⭐⭐
title: docs-seeker
url: https://skills.sh/duc01226/easyplatform/docs-seeker
---

# docs-seeker

skills/duc01226/easyplatform/docs-seeker
docs-seeker
Installation
$ npx skills add https://github.com/duc01226/easyplatform --skill docs-seeker
SKILL.md

[IMPORTANT] Use TaskCreate to break ALL work into small tasks BEFORE starting — including tasks for each file read. This prevents context loss from long files. For simple tasks, AI MUST ATTENTION ask user whether to skip.

Quick Summary

Goal: Search and fetch technical documentation using executable scripts with llms.txt standard (context7.com).

Workflow:

Detect — Run scripts/detect-topic.js to classify query type (topic-specific vs general)
Fetch — Run scripts/fetch-docs.js to retrieve documentation with automatic fallback
Analyze — Run scripts/analyze-llms-txt.js to categorize URLs and recommend agent distribution

Key Rules:

Always execute scripts in order: detect -> fetch -> analyze
Scripts handle URL construction and fallback chains automatically; no manual URL building
Zero-token overhead: scripts run without context loading

Be skeptical. Apply critical thinking, sequential thinking. Every claim needs traced proof, confidence percentages (Idea should be more than 80%).

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

Closing Reminders
IMPORTANT MUST ATTENTION break work into small todo tasks using TaskCreate BEFORE starting
IMPORTANT MUST ATTENTION search codebase for 3+ similar patterns before creating new code
IMPORTANT MUST ATTENTION cite file:line evidence for every claim (confidence >80% to act)
IMPORTANT MUST ATTENTION add a final review todo task to verify work quality
Weekly Installs
45
Repository
duc01226/easyplatform
GitHub Stars
6
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn