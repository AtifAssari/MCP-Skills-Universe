---
title: foundation-models
url: https://skills.sh/johnrogers/claude-swift-engineering/foundation-models
---

# foundation-models

skills/johnrogers/claude-swift-engineering/foundation-models
foundation-models
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill foundation-models
SKILL.md
Foundation Models

Apple's on-device AI framework providing access to a 3B parameter language model for summarization, extraction, classification, and content generation. Runs entirely on-device with no network required.

Overview

Foundation Models enable intelligent text processing directly on device without server round-trips, user data sharing, or network dependencies. The core principle: leverage on-device AI for specific, contained tasks (not for general knowledge).

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Getting Started	Setting up LanguageModelSession, checking availability, basic prompts
Structured Output	Using @Generable for type-safe responses, @Guide constraints
Tool Calling	Integrating external data (weather, contacts, MapKit) via Tool protocol
Streaming	AsyncSequence for progressive UI updates, PartiallyGenerated types
Troubleshooting	Context overflow, guardrails, errors, anti-patterns
Core Workflow
Check availability with SystemLanguageModel.default.availability
Create LanguageModelSession with optional instructions
Choose output type: plain String or @Generable struct
Use streaming for long generations (>1 second)
Handle errors: context overflow, guardrails, unsupported language
Model Capabilities
Use Case	Foundation Models?	Alternative
Summarization	Yes	-
Extraction (key info)	Yes	-
Classification	Yes	-
Content tagging	Yes (built-in adapter)	-
World knowledge	No	ChatGPT, Claude, Gemini
Complex reasoning	No	Server LLMs
Platform Requirements
iOS 26+, macOS 26+, iPadOS 26+, visionOS 26+
Apple Intelligence-enabled device (iPhone 15 Pro+, M1+ iPad/Mac)
User opted into Apple Intelligence
Common Mistakes

Using Foundation Models for world knowledge — The 3B model is trained for on-device tasks only. It won't know current events, specific facts, or "who is X". Use ChatGPT/Claude for that. Keep prompts to: summarizing user's own content, extracting info, classifying text.

Blocking the main thread — LanguageModelSession calls must run on a background thread or async context. Blocking the main thread locks UI. Always use Task { } or background queue.

Ignoring context overflow — The model has finite context. If the user pastes a 50KB document, it will fail silently or truncate. Check input length and trim/truncate proactively.

Forgetting to check availability — Not all devices support Foundation Models. Check SystemLanguageModel.default.availability before using. Graceful degradation is required.

Ignoring guardrails — The model won't answer harmful queries. Instead of fighting it, design prompts that respect safety guidelines. Rephrasing requests usually works.

Weekly Installs
98
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass