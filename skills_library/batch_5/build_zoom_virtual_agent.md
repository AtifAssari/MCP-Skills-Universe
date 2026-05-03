---
title: build-zoom-virtual-agent
url: https://skills.sh/anthropics/knowledge-work-plugins/build-zoom-virtual-agent
---

# build-zoom-virtual-agent

skills/anthropics/knowledge-work-plugins/build-zoom-virtual-agent
build-zoom-virtual-agent
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill build-zoom-virtual-agent
SKILL.md
/build-zoom-virtual-agent

Background reference for Zoom Virtual Agent across:

Web campaign/chat embeds.
Android WebView wrappers.
iOS WKWebView wrappers.
Knowledge-base sync and custom API ingestion.

Official docs:

https://developers.zoom.us/docs/virtual-agent/
https://developers.zoom.us/docs/virtual-agent/web/
https://developers.zoom.us/docs/virtual-agent/android/
https://developers.zoom.us/docs/virtual-agent/ios/
Routing Guardrail
If the user is implementing Contact Center app surfaces inside Zoom client, chain with ../contact-center/SKILL.md.
If the user needs backend knowledge-base CRUD or automation scripts, chain with ../rest-api/SKILL.md and ../oauth/SKILL.md.
If the user asks only for website bot embed and campaign controls, stay on web/SKILL.md.
If the user asks for mobile native wrappers around web chat, route to android/SKILL.md or ios/SKILL.md.
Quick Links
concepts/architecture-and-lifecycle.md
scenarios/high-level-scenarios.md
references/versioning-and-drift.md
references/samples-validation.md
references/environment-variables.md
troubleshooting/common-drift-and-breaks.md
RUNBOOK.md

Platform skills:

web/SKILL.md
android/SKILL.md
ios/SKILL.md
Common Lifecycle Pattern
Configure campaign or entry ID in Virtual Agent admin.
Initialize SDK in web or WebView container.
Wait for readiness (zoomCampaignSdk:ready or waitForReady()) before calling APIs.
Register bridge handlers (exitHandler, commonHandler, support_handoff) when native orchestration is needed.
Handle conversation lifecycle (engagement_started, engagement_ended) and UI state.
End chat (endChat) and clean up listeners.
High-Level Scenarios
Website campaign launcher with contextual customer attributes.
Mobile app WebView chat with native close/handoff bridge.
External URL handling via system browser vs in-app browser policy.
Knowledge-base sync from external systems using custom API connector.
Cross-team support flow that escalates from bot to live support with handoff payload.
Chaining
Contact Center app/web/mobile patterns: ../contact-center/SKILL.md
OAuth app setup and tokens: ../oauth/SKILL.md
API workflows for KB automation: ../rest-api/SKILL.md
Event-driven backend follow-up: ../webhooks/SKILL.md
Operations
RUNBOOK.md - 5-minute preflight and debugging checklist.
Weekly Installs
290
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn