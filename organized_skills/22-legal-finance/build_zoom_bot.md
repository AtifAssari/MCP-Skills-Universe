---
rating: ⭐⭐
title: build-zoom-bot
url: https://skills.sh/anthropics/knowledge-work-plugins/build-zoom-bot
---

# build-zoom-bot

skills/anthropics/knowledge-work-plugins/build-zoom-bot
build-zoom-bot
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill build-zoom-bot
SKILL.md
/build-zoom-bot

Use this skill for automation that joins meetings, captures media, or reacts to live session data.

Covers
Bot architecture
Meeting join strategy
Real-time media and transcript handling
Backend orchestration
Storage, post-processing, and event flow design
Workflow
Clarify whether the bot needs to join, observe, transcribe, summarize, or act.
Route to Meeting SDK and RTMS as the core implementation path.
Add REST API for meeting/resource management and Webhooks for asynchronous events when needed.
Call out environment and lifecycle constraints early.
Primary References
meeting-sdk
rtms
scribe
rest-api
webhooks
Common Mistakes
Treating batch transcription and live media as the same workflow
Designing the bot before defining join authority and auth model
Forgetting post-meeting storage and retry behavior
Weekly Installs
291
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass