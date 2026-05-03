---
title: starters
url: https://skills.sh/deepgram/skills/starters
---

# starters

skills/deepgram/skills/starters
starters
Installation
$ npx skills add https://github.com/deepgram/skills --skill starters
SKILL.md
Deepgram Starter Apps

Clone a working demo and start building. Every starter is a minimal, runnable app you can extend.

1. Pick Your Feature

What do you want to build?

Transcribe a file → transcription — send audio/video, get text back (REST, Nova)
Transcribe a live stream → live-transcription — real-time speech-to-text (WebSocket, Nova)
Generate speech → text-to-speech — send text, get audio back (REST)
Stream speech → live-text-to-speech — real-time text-to-audio (WebSocket)
Analyze text or audio → text-intelligence — sentiment, topics, intents, summaries (REST)
Build a voice agent → voice-agent — conversational AI agent (WebSocket, agent.deepgram.com)
Conversational STT with turn detection → flux — Deepgram Flux for voice agents and interactive assistants (WebSocket, /v2/listen)

Nova vs Flux for speech-to-text: use transcription or live-transcription (Nova, /v1/listen) for general-purpose transcription, captions, and batch workloads. Use flux (Flux, /v2/listen) when you need built-in turn detection for conversational audio. See the api skill for a full comparison.

2. Pick Your Stack
Language	Frameworks
JavaScript	node
TypeScript	bun, deno
Python	fastapi, flask, django
Go	go
Java	java
C#	csharp
Rust	rust
Ruby	ruby
PHP	php
C++	cpp
3. Clone and Run

Every starter lives at https://github.com/deepgram-starters/{framework}-{feature}:

git clone https://github.com/deepgram-starters/{framework}-{feature}.git
cd {framework}-{feature}


Set your API key and follow the README:

export DEEPGRAM_API_KEY=your_key_here


Get an API key at https://console.deepgram.com.

Examples

"I want to build a voice agent in Python" → git clone https://github.com/deepgram-starters/fastapi-voice-agent.git

"I need live transcription in my Node app" → git clone https://github.com/deepgram-starters/node-live-transcription.git

"I want to add text-to-speech to my Go service" → git clone https://github.com/deepgram-starters/go-text-to-speech.git

"I want to analyze audio for sentiment in C#" → git clone https://github.com/deepgram-starters/csharp-text-intelligence.git

All Starters
	transcription	live-transcription	text-to-speech	live-text-to-speech	text-intelligence	voice-agent	flux
node	repo	repo	repo	repo	repo	repo	repo
bun	repo	repo	repo	repo	repo	repo	repo
deno	repo	repo	repo	repo	repo	repo	repo
fastapi	repo	repo	repo	repo	repo	repo	repo
flask	repo	repo	repo	repo	repo	repo	repo
django	repo	repo	repo	repo	repo	repo	repo
go	repo	repo	repo	repo	repo	repo	repo
java	repo	repo	repo	repo	repo	repo	repo
csharp	repo	repo	repo	repo	repo	repo	repo
rust	repo	repo	repo	repo	repo	repo	repo
ruby	repo	repo	repo	repo	repo	repo	repo
php	repo	repo	repo	repo	repo	repo	repo
cpp	repo	repo	repo	repo	repo	repo	repo
Need something more specific?
Focused feature snippets (one feature, one language, < 50 lines) → recipes skill → https://github.com/deepgram/recipes
Third-party integrations (Twilio, LiveKit, LangChain, Vercel AI SDK, Discord, etc.) → examples skill → https://github.com/deepgram/examples
SDK-specific code skills (idiomatic imports, async patterns, gotchas) → npx skills add deepgram/deepgram-{lang}-sdk — see the api skill for the full list of 9 SDKs.
Related Deepgram skills
api — consolidated REST + WebSocket API reference
recipes — minimal runnable feature snippets per language
examples — full integration examples with third-party platforms
docs — documentation finder
setup-mcp — Deepgram MCP server installation
Weekly Installs
46
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