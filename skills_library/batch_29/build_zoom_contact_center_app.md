---
title: build-zoom-contact-center-app
url: https://skills.sh/anthropics/knowledge-work-plugins/build-zoom-contact-center-app
---

# build-zoom-contact-center-app

skills/anthropics/knowledge-work-plugins/build-zoom-contact-center-app
build-zoom-contact-center-app
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill build-zoom-contact-center-app
SKILL.md
/build-zoom-contact-center-app

Background reference for Zoom Contact Center integrations across app, web, and native mobile surfaces.

Implementation guidance for Zoom Contact Center across:

Contact Center apps in the Zoom client (Zoom Apps SDK path)
Web channel embeds (chat/video/campaign)
Native mobile SDKs (Android/iOS)

Official docs:

https://developers.zoom.us/docs/contact-center/
https://developers.zoom.us/docs/contact-center/web/sdk-reference/
https://marketplacefront.zoom.us/sdk/contact/android/index.html
https://marketplacefront.zoom.us/sdk/contact/ios/index.html
Routing Guardrail
If the user is building an app inside the Zoom Contact Center desktop client, stay on the Zoom Apps SDK path and use this skill plus zoom-apps-sdk.
If the user is embedding chat/video widgets on a website, route to web/SKILL.md.
If the user is integrating native Android or iOS SDK binaries, route to android/SKILL.md or ios/SKILL.md.
If the user needs Contact Center call-control or queue APIs, chain with ../rest-api/SKILL.md.
Quick Links

Start here:

concepts/architecture-and-lifecycle.md
scenarios/high-level-scenarios.md
references/forum-top-questions.md
references/versioning-and-compatibility.md
references/samples-validation.md
references/environment-variables.md
troubleshooting/common-drift-and-breaks.md
RUNBOOK.md

Platform skills:

android/SKILL.md
ios/SKILL.md
web/SKILL.md
Documentation Structure
contact-center/
├── SKILL.md
├── RUNBOOK.md
├── concepts/
│   └── architecture-and-lifecycle.md
├── scenarios/
│   └── high-level-scenarios.md
├── references/
│   ├── versioning-and-compatibility.md
│   ├── samples-validation.md
│   └── environment-variables.md
├── troubleshooting/
│   └── common-drift-and-breaks.md
├── android/
│   ├── SKILL.md
│   ├── concepts/sdk-lifecycle.md
│   ├── examples/service-patterns.md
│   ├── references/android-reference-map.md
│   └── troubleshooting/common-issues.md
├── ios/
│   ├── SKILL.md
│   ├── concepts/sdk-lifecycle.md
│   ├── examples/service-patterns.md
│   ├── references/ios-reference-map.md
│   └── troubleshooting/common-issues.md
└── web/
    ├── SKILL.md
    ├── concepts/lifecycle-and-events.md
    ├── examples/app-context-and-state.md
    ├── references/web-reference-map.md
    └── troubleshooting/common-issues.md

Common Lifecycle Pattern
Initialize platform context early.
Build a channel item (entryId for chat/video/ZVA, apiKey for scheduled callback and campaign flows).
Get service/client instance.
Register listeners/delegates before user interaction.
Start flow (fetchUI, startVideo, or web SDK open/show path).
Handle engagement state changes (start, hold, resume, end) and context switching.
End flow and release resources (endChat/endVideo, logout/logoff, uninitialize/release).
High-Level Scenarios
Agent side-panel app that stores notes per engagementId and survives context switching.
Browser chat/video campaigns launched from web tags.
Native mobile customer app for chat/video/scheduled callback.
Campaign-driven channel selection (chat, ZVA, video, scheduled callback).
Rejoin flow for dropped video engagements on mobile.
Smart Embed CRM softphone with postMessage event contracts.

See scenarios/high-level-scenarios.md for details.

Chaining
Auth and in-client app identity: ../zoom-apps-sdk/SKILL.md and ../oauth/SKILL.md
Contact Center REST workflows: ../rest-api/SKILL.md
Cobrowse on web voice/chat channels: ../cobrowse-sdk/SKILL.md
Environment Variables
See references/environment-variables.md for standardized .env keys and where to find each value.
Weekly Installs
295
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass