---
rating: ⭐⭐
title: build-zoom-phone-integration
url: https://skills.sh/anthropics/knowledge-work-plugins/build-zoom-phone-integration
---

# build-zoom-phone-integration

skills/anthropics/knowledge-work-plugins/build-zoom-phone-integration
build-zoom-phone-integration
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill build-zoom-phone-integration
SKILL.md
/build-zoom-phone-integration

Background reference for Zoom Phone integrations across API, webhook, Smart Embed, and URI-launch workflows.

Implementation guidance for Zoom Phone integrations across API, webhook/event, Smart Embed, and URI-launch workflows.

Official docs:

https://developers.zoom.us/docs/phone/
CRM sample reference: https://github.com/zoom/CRM-Sample
Routing Guardrail
If the user needs embedded softphone behavior in a web app, use Smart Embed (examples/smart-embed-postmessage-bridge.md).
If the user needs call records, analytics, or automation, use Phone REST API and webhooks (references/deprecations-and-migrations.md).
If the user needs click-to-dial/SMS launch from external UI, use URI schemes (zoomphonecall://, zoomphonesms://).
If the user mixes Zoom Phone and Contact Center, chain with ../contact-center/SKILL.md.
Quick Links

Start here:

concepts/architecture-and-lifecycle.md
scenarios/high-level-scenarios.md
references/deprecations-and-migrations.md
references/forum-top-questions.md
references/smart-embed-event-contract.md
references/call-handling-patterns.md
references/environment-variables.md
references/crm-sample-validation.md
troubleshooting/common-issues.md
RUNBOOK.md
examples/smart-embed-postmessage-bridge.md
examples/phone-api-service-pattern.md
references/source-map.md
Common Lifecycle Pattern
Provision account prerequisites (Zoom Phone license, admin setup, SMS readiness).
Create OAuth app and scopes in Marketplace.
Choose integration surface:
Smart Embed (iframe + postMessage)
REST + webhooks
URI launch (callto, tel, zoomphonecall, zoomphonesms)
Capture real-time events (Smart Embed events and/or webhooks).
Persist call identifiers and correlate records (call_id, call_history_uuid, call_element_id).
Apply migration-safe data mapping (v1 -> v2 -> v3) and handle renamed fields.
Harden security (origin validation, webhook signature validation, least-privilege scopes).
High-Level Scenarios
CRM softphone pane using Smart Embed + contact search/match callbacks.
Click-to-call from account/contact table via zp-make-call.
Call disposition workflow using zp-save-log-event and custom notes page.
SMS engagement workflow with zoomphonesms:// and zp-sms-log-event.
Real-time operational board driven by phone.* webhook events.
Call analytics migration from legacy call logs to call history/call elements.
Admin automation for user/auto-receptionist/call-queue call-handling settings.

See scenarios/high-level-scenarios.md for details.

Chaining
OAuth setup/token lifecycle: ../oauth/SKILL.md
Phone and account resources via REST: ../rest-api/SKILL.md
Event delivery and signature validation: ../webhooks/SKILL.md
Contact Center blended journey: ../contact-center/SKILL.md
Environment Variables
See references/environment-variables.md for standardized .env keys and where to find each value.
Weekly Installs
293
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