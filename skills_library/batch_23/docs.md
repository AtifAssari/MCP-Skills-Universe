---
title: docs
url: https://skills.sh/deepgram/skills/docs
---

# docs

skills/deepgram/skills/docs
docs
Installation
$ npx skills add https://github.com/deepgram/skills --skill docs
SKILL.md
Deepgram Documentation

Find the right docs for what you're building with Deepgram.

Ask AI

Have a question? Get answers from Deepgram's AI assistant at https://developers.deepgram.com/ask-ai.

Documentation by Topic
Speech-to-Text (STT)

Transcribe audio and video into text. Deepgram ships two actively maintained, next-gen model families — pick the one that matches your use case.

Nova (/v1/listen) — general-purpose transcription (captions, subtitles, batch files, live streams). Rich feature set including intelligence overlays (diarize, summarize, sentiment, topics, intents).
Flux (/v2/listen) — conversational-audio transcription for voice agents and interactive assistants. Built-in turn-taking (EOT events, mid-session reconfig).

Docs:

STT Getting Started (Nova)
Flux Quickstart
Nova 3 → Flux migration
Flux language prompting
Text-to-Speech (TTS)

Convert text into natural-sounding speech.

Text-to-Speech Docs
Voice Agent

Build conversational voice agents powered by Deepgram.

Voice Agent Docs
Text and Audio Intelligence

Analyze text and audio for sentiment, topics, intents, summaries, and more.

Audio Intelligence Docs
Self-Hosted Deployments

Run Deepgram on your own infrastructure.

Self-Hosted Introduction
API Reference

Full reference for all Deepgram REST and WebSocket APIs.

API Reference
SDK-Specific Skills

For language-idiomatic code patterns (imports, async idioms, error handling, type shapes), install the Deepgram SDK's own skills. Every Deepgram SDK publishes 7 product skills plus a maintainer skill:

npx skills add deepgram/deepgram-python-sdk     # Python
npx skills add deepgram/deepgram-js-sdk         # JavaScript / TypeScript
npx skills add deepgram/deepgram-java-sdk       # Java
npx skills add deepgram/deepgram-go-sdk         # Go
npx skills add deepgram/deepgram-rust-sdk       # Rust
npx skills add deepgram/deepgram-swift-sdk      # Swift
npx skills add deepgram/deepgram-kotlin-sdk     # Kotlin
npx skills add deepgram/deepgram-dotnet-sdk     # C# / .NET
npx skills add deepgram/deepgram-browser-sdk    # Browser TypeScript

Related Deepgram skills
api — consolidated REST + WebSocket API reference
recipes — minimal runnable feature snippets per language
examples — full integration examples with third-party platforms
starters — runnable starter apps (framework × feature)
setup-mcp — Deepgram MCP server installation
MCP Server

For direct documentation querying from your AI coding tool, use /deepgram:mcp to set up the Deepgram MCP server.

Weekly Installs
56
Repository
deepgram/skills
GitHub Stars
8
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass