---
title: summarize
url: https://skills.sh/steipete/clawdis/summarize
---

# summarize

skills/steipete/clawdis/summarize
summarize
Installation
$ npx skills add https://github.com/steipete/clawdis --skill summarize
Summary

Extract summaries and transcripts from URLs, videos, and local files via CLI.

Supports URLs, YouTube links, PDFs, and local files with configurable summary length (short to xxl) and output format (text or JSON)
Works with OpenAI, Anthropic, xAI, and Google Gemini models; defaults to Gemini 3 Flash if no model specified
Includes best-effort YouTube transcript extraction and Firecrawl/Apify fallbacks for blocked or hard-to-parse content
Single command interface with optional config file for persistent model and API key settings
SKILL.md
Summarize

Fast CLI to summarize URLs, local files, and YouTube links.

When to use (trigger phrases)

Use this skill immediately when the user asks any of:

“use summarize.sh”
“what’s this link/video about?”
“summarize this URL/article”
“transcribe this YouTube/video” (best-effort transcript extraction; no yt-dlp needed)
Quick start
summarize "https://example.com" --model google/gemini-3-flash-preview
summarize "/path/to/file.pdf" --model google/gemini-3-flash-preview
summarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto

YouTube: summary vs transcript

Best-effort transcript (URLs only):

summarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto --extract-only


If the user asked for a transcript but it’s huge, return a tight summary first, then ask which section/time range to expand.

Model + keys

Set the API key for your chosen provider:

OpenAI: OPENAI_API_KEY
Anthropic: ANTHROPIC_API_KEY
xAI: XAI_API_KEY
Google: GEMINI_API_KEY (aliases: GOOGLE_GENERATIVE_AI_API_KEY, GOOGLE_API_KEY)

Default model is google/gemini-3-flash-preview if none is set.

Useful flags
--length short|medium|long|xl|xxl|<chars>
--max-output-tokens <count>
--extract-only (URLs only)
--json (machine readable)
--firecrawl auto|off|always (fallback extraction)
--youtube auto (Apify fallback if APIFY_API_TOKEN set)
Config

Optional config file: ~/.summarize/config.json

{ "model": "openai/gpt-5.2" }


Optional services:

FIRECRAWL_API_KEY for blocked sites
APIFY_API_TOKEN for YouTube fallback
Weekly Installs
13.5K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn