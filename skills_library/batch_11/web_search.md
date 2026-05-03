---
title: web-search
url: https://skills.sh/site/modelscope.cn/web-search
---

# web-search

skills/modelscope.cn/web-search
web-search
$ npx skills add https://modelscope.cn/skills/@inference-sh/web-search
SKILL.md
Web Search & Extraction

Search the web and extract content via inference.sh CLI.

Quick Start

Requires inference.sh CLI (infsh). Get installation instructions: npx skills add inference-sh/skills@agent-tools

infsh login

# Search the web
infsh app run tavily/search-assistant --input '{"query": "latest AI developments 2024"}'

Available Apps
Tavily
App	App ID	Description
Search Assistant	tavily/search-assistant	AI-powered search with answers
Extract	tavily/extract	Extract content from URLs
Exa
App	App ID	Description
Search	exa/search	Smart web search with AI
Answer	exa/answer	Direct factual answers
Extract	exa/extract	Extract and analyze web content
Examples
Tavily Search
infsh app run tavily/search-assistant --input '{
  "query": "What are the best practices for building AI agents?"
}'


Returns AI-generated answers with sources and images.

Tavily Extract
infsh app run tavily/extract --input '{
  "urls": ["https://example.com/article1", "https://example.com/article2"]
}'


Extracts clean text and images from multiple URLs.

Exa Search
infsh app run exa/search --input '{
  "query": "machine learning frameworks comparison"
}'


Returns highly relevant links with context.

Exa Answer
infsh app run exa/answer --input '{
  "question": "What is the population of Tokyo?"
}'


Returns direct factual answers.

Exa Extract
infsh app run exa/extract --input '{
  "url": "https://example.com/research-paper"
}'


Extracts and analyzes web page content.

Workflow: Research + LLM
# 1. Search for information
infsh app run tavily/search-assistant --input '{
  "query": "latest developments in quantum computing"
}' > search_results.json

# 2. Analyze with Claude
infsh app run openrouter/claude-sonnet-45 --input '{
  "prompt": "Based on this research, summarize the key trends: <search-results>"
}'

Workflow: Extract + Summarize
# 1. Extract content from URL
infsh app run tavily/extract --input '{
  "urls": ["https://example.com/long-article"]
}' > content.json

# 2. Summarize with LLM
infsh app run openrouter/claude-haiku-45 --input '{
  "prompt": "Summarize this article in 3 bullet points: <content>"
}'

Use Cases
Research: Gather information on any topic
RAG: Retrieval-augmented generation
Fact-checking: Verify claims with sources
Content aggregation: Collect data from multiple sources
Agents: Build research-capable AI agents
Related Skills
# Full platform skill (all 150+ apps)
npx skills add inference-sh/skills@agent-tools

# LLM models (combine with search for RAG)
npx skills add inference-sh/skills@llm-models

# Image generation
npx skills add inference-sh/skills@ai-image-generation


Browse all apps: infsh app list

Documentation
Adding Tools to Agents - Equip agents with search
Building a Research Agent - LLM + search integration guide
Tool Integration Tax - Why pre-built tools matter
Weekly Installs
266
Source
modelscope.cn/s…b-search
First Seen
Today