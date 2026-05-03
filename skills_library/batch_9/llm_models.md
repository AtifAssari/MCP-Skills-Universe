---
title: llm-models
url: https://skills.sh/inference-sh/skills/llm-models
---

# llm-models

skills/inference-sh/skills/llm-models
llm-models
Installation
$ npx skills add https://github.com/inference-sh/skills --skill llm-models
SKILL.md
LLM Models via OpenRouter

Access 100+ language models via inference.sh CLI.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

# Call Claude Sonnet
belt app run openrouter/claude-sonnet-45 --input '{"prompt": "Explain quantum computing"}'

Available Models
Model	App ID	Best For
Claude Opus 4.5	openrouter/claude-opus-45	Complex reasoning, coding
Claude Sonnet 4.5	openrouter/claude-sonnet-45	Balanced performance
Claude Haiku 4.5	openrouter/claude-haiku-45	Fast, economical
Gemini 3 Pro	openrouter/gemini-3-pro-preview	Google's latest
Kimi K2 Thinking	openrouter/kimi-k2-thinking	Multi-step reasoning
GLM-4.6	openrouter/glm-46	Open-source, coding
Intellect 3	openrouter/intellect-3	General purpose
Any Model	openrouter/any-model	Auto-selects best option
Search LLM Apps
belt app list --search "openrouter"
belt app list --search "claude"

Examples
Claude Opus (Best Quality)
belt app run openrouter/claude-opus-45 --input '{
  "prompt": "Write a Python function to detect palindromes with comprehensive tests"
}'

Claude Sonnet (Balanced)
belt app run openrouter/claude-sonnet-45 --input '{
  "prompt": "Summarize the key concepts of machine learning"
}'

Claude Haiku (Fast & Cheap)
belt app run openrouter/claude-haiku-45 --input '{
  "prompt": "Translate this to French: Hello, how are you?"
}'

Kimi K2 (Thinking Agent)
belt app run openrouter/kimi-k2-thinking --input '{
  "prompt": "Plan a step-by-step approach to build a web scraper"
}'

Any Model (Auto-Select)
# Automatically picks the most cost-effective model
belt app run openrouter/any-model --input '{
  "prompt": "What is the capital of France?"
}'

With System Prompt
belt app sample openrouter/claude-sonnet-45 --save input.json

# Edit input.json:
# {
#   "system": "You are a helpful coding assistant",
#   "prompt": "How do I read a file in Python?"
# }

belt app run openrouter/claude-sonnet-45 --input input.json

Use Cases
Coding: Generate, review, debug code
Writing: Content, summaries, translations
Analysis: Data interpretation, research
Agents: Build AI-powered workflows
Chat: Conversational interfaces
Related Skills
# Full platform skill (all 250+ apps)
npx skills add inference-sh/skills@infsh-cli

# Web search (combine with LLMs for RAG)
npx skills add inference-sh/skills@web-search

# Image generation
npx skills add inference-sh/skills@ai-image-generation

# Video generation
npx skills add inference-sh/skills@ai-video-generation


Browse all apps: belt app list

Documentation
Agents Overview - Building AI agents
Agent SDK - Programmatic agent control
Building a Research Agent - LLM + search integration guide
Weekly Installs
300
Repository
inference-sh/skills
GitHub Stars
395
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass