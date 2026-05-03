---
rating: ⭐⭐
title: probe-sdk
url: https://skills.sh/anthropics/knowledge-work-plugins/probe-sdk
---

# probe-sdk

skills/anthropics/knowledge-work-plugins/probe-sdk
probe-sdk
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill probe-sdk
SKILL.md
Zoom Probe SDK

Background reference for preflight diagnostics on user devices and networks before meeting or session workflows.

Official docs:

https://developers.zoom.us/docs/probe-sdk/
https://marketplacefront.zoom.us/sdk/probe/index.html

Reference sample:

https://github.com/zoom/probesdk-web
Routing Guardrail
Use Probe SDK when the user needs client-side diagnostics and readiness scoring (device/network/browser capability), not meeting/session join.
If user needs embedded meeting flows, route to ../meeting-sdk/SKILL.md.
If user needs custom real-time session UX, route to ../video-sdk/SKILL.md.
If user needs backend orchestration of events/APIs, chain with ../rivet-sdk/SKILL.md, ../oauth/SKILL.md, and ../rest-api/SKILL.md.
Quick Links

Start here:

probe-sdk.md
concepts/architecture-and-lifecycle.md
scenarios/high-level-scenarios.md
examples/diagnostic-page-pattern.md
examples/comprehensive-network-pattern.md
references/probe-reference-map.md
references/environment-variables.md
references/versioning-and-compatibility.md
references/samples-validation.md
references/source-map.md
troubleshooting/common-issues.md
RUNBOOK.md
Common Lifecycle Pattern
Initialize Prober / Reporter.
Request media permissions and enumerate devices.
Run targeted diagnostics (diagnoseAudio, diagnoseVideo).
Run comprehensive network diagnostic (startToDiagnose) and stream stats to UI.
Produce final report and apply readiness gates.
Stop/cleanup (stopToDiagnose, stopToDiagnoseVideo, releaseMediaStream, cleanup).
High-Level Scenarios
Pre-join diagnostics page before Meeting SDK join action.
Support workflow that captures structured report for customer troubleshooting.
Device certification flow for kiosk or controlled endpoint environments.
Browser capability gating for advanced media features.

See scenarios/high-level-scenarios.md for details.

Chaining
Meeting pre-join gate: ../meeting-sdk/web/SKILL.md
Video session readiness gate: ../video-sdk/web/SKILL.md
Telemetry/report ingestion backend: ../rivet-sdk/SKILL.md + ../rest-api/SKILL.md
Environment Variables
See references/environment-variables.md for optional .env keys and how to source values.
Operations
RUNBOOK.md - 5-minute preflight and debugging checklist.
Weekly Installs
297
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn