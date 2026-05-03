---
rating: ⭐⭐⭐
title: token-optimizer
url: https://skills.sh/mjohngreene/tokenoptimizer/token-optimizer
---

# token-optimizer

skills/mjohngreene/tokenoptimizer/token-optimizer
token-optimizer
Installation
$ npx skills add https://github.com/mjohngreene/tokenoptimizer --skill token-optimizer
SKILL.md
TokenOptimizer
When to Use
You have a coding task and want to send it to an LLM API with less context (fewer tokens, lower cost).
You want automatic fallback from a cheap provider to a more capable one when credits run out.
You want local LLM preprocessing to score relevance and compress context before it hits a paid API.
You need to stay within a token budget while keeping the most important context.
Quick Start
# Optimize a prompt with default strategies
token_optimizer optimize --input "Fix the bug in auth" --context src/auth.rs

# Analyze cache potential for Anthropic
token_optimizer cache-optimize --task "Add feature" --context types.rs --static-indices "0"

# Launch interactive shell (auto-selects provider)
token_optimizer interactive

# Show current config
token_optimizer config show primary

Capabilities
Capability	Description
StripWhitespace	Remove redundant whitespace, preserving code blocks
RemoveComments	Strip //, /* */, # comments from code
TruncateContext	Boundary-aware truncation using tiktoken token counts and priority-based boundary detection (code structure > paragraph > sentence > line > word)
Abbreviate	Shorten common programming terms in task text
LlmCompress	Compress context via local Ollama LLM
RelevanceFilter	Hybrid keyword + LLM relevance scoring; works without local LLM via keyword-only mode
ExtractSignatures	Keep only function/class/struct signatures
Deduplicate	Remove exact, whitespace-normalized, and near-duplicate context items
CachePrompting	Anthropic-compatible cache breakpoints for static content
Provider Fallback	Automatic primary -> fallback -> local provider pipeline
Weekly Installs
14
Repository
mjohngreene/tok…ptimizer
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass