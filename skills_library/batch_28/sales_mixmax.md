---
title: sales-mixmax
url: https://skills.sh/sales-skills/sales/sales-mixmax
---

# sales-mixmax

skills/sales-skills/sales/sales-mixmax
sales-mixmax
Installation
$ npx skills add https://github.com/sales-skills/sales --skill sales-mixmax
SKILL.md
Mixmax Platform Help

Help the user with Mixmax platform questions — from sequences and email tracking through one-click meetings, rules engine, dialer, AI Compose, Salesforce/HubSpot integration, polls, and reporting.

Step 1 — Gather context

If references/learnings.md exists, read it first for accumulated knowledge.

Ask the user:

What area of Mixmax do you need help with?

A) Sequences — multi-channel outreach campaigns (email, phone, LinkedIn, tasks)
B) Email Tracking — open, click, download, and RSVP tracking
C) Meeting Scheduling — one-click meetings, round-robin, inbound lead routing
D) Rules Engine — IF/THEN automations, Salesforce triggers, webhooks
E) Templates & Snippets — reusable email content with personalization
F) Dialer — in-Gmail calling with CRM and Gong logging
G) AI Features — AI Compose, Smart Send, AI sequence builder
H) Polls & Surveys — embedded one-click response polls in emails
I) Salesforce Integration — inbox sidebar, auto-create records, dynamic fields, advanced rules
J) HubSpot Integration — activity sync, list import, sidebar
K) Reporting — opens, clicks, bounces, replies, downloads, RSVPs
L) Admin — branding, team settings, compliance
M) API — programmatic access to sequences, messages, rules, contacts
N) Something else — describe it

What's your role?

A) Sales rep / AE / BDR
B) Sales manager / team lead
C) RevOps / Sales Ops
D) Admin / IT
E) Founder / solo seller
F) Other

What are you trying to accomplish? (describe your specific goal or question)

If the user's request already provides most of this context, skip directly to the relevant step. Lead with your best-effort answer using reasonable assumptions (stated explicitly), then ask only the most critical 1-2 clarifying questions at the end — don't gate your response behind gathering complete context.

Note: If the user needs a specialized skill, route them there with a brief explanation of why that skill is a better fit.

Step 2 — Route or answer directly

If the request maps to a specialized skill, route:

Outbound cadence strategy / sequence design → /sales-cadence
Cross-platform email deliverability → /sales-deliverability
Meeting scheduling strategy → /sales-meeting-scheduler
Email tracking strategy → /sales-email-tracking
Connecting Mixmax to other tools via Zapier → /sales-integration

Otherwise, answer directly from platform knowledge using the reference below.

Step 3 — Mixmax platform reference

Read references/platform-guide.md for detailed module documentation, pricing, integrations, and data model.

You no longer need the platform guide details — focus on the user's specific situation.

Step 4 — Actionable guidance

Based on the user's specific question:

Step-by-step instructions — numbered steps to accomplish their goal in Mixmax
Configuration recommendations — specific settings to change, with navigation paths (typically via the Mixmax sidebar in Gmail or Mixmax dashboard)
Common pitfalls — what can go wrong and how to avoid it
Verification — how to confirm the change worked as expected
Plan check — flag any features that require a specific plan tier before recommending them
Gotchas

Best-effort from research — review these, especially items about plan-gated features and integration gotchas that may be outdated.

Mixmax is Gmail-only — there is no Outlook support. Mixmax works exclusively as a Gmail/Google Workspace extension. Don't recommend Mixmax to users on Outlook or Microsoft 365. If they need Outlook support, suggest alternatives like Salesloft, Yesware, or Mailshake.

Salesforce advanced rules require Growth+CRM plan (~$89/user/mo). Basic Salesforce sidebar and activity logging are on the Growth plan, but rules triggered by Salesforce objects (opportunities, accounts, custom objects) require Growth+CRM. Always ask about the user's plan before suggesting SF-triggered automations.

The Contacts API is deprecated. Don't recommend building integrations against the /contacts endpoints. Use Salesforce or HubSpot as the contact source of truth instead. The contacts endpoints may be removed in a future API version.

API rate limits are undocumented. Mixmax does not publish official rate limits. The API is described as "optimized for lightweight, real-time interactions" — it is NOT suitable for bulk exports or high-volume sync. Recommend building with conservative backoff and small batch sizes.

One-click meetings require the recipient's email client to render rich HTML. If the recipient uses a plain-text email client or has images disabled, one-click meeting proposals won't render correctly. They'll fall back to a scheduling link, but the one-click experience is lost.

Self-improving: If you discover something not covered here, append it to references/learnings.md with today's date.

Step 5 — Related skills
/sales-cadence — Design outbound cadence strategy (platform-agnostic, works with Mixmax sequences)
/sales-deliverability — Cross-platform email deliverability — SPF/DKIM/DMARC, warmup, inbox placement
/sales-meeting-scheduler — Meeting scheduling strategy and best practices (platform-agnostic)
/sales-email-tracking — Email tracking strategy and best practices (platform-agnostic)
/sales-integration — Connect Mixmax to other tools via Zapier, webhooks, or native integrations
/sales-do — Not sure which skill to use? The router matches any sales objective to the right skill. Install: npx skills add sales-skills/sales --skill sales-do
Examples
Example 1: Multi-channel sequence setup

User says: "How do I set up a multi-channel sequence in Mixmax with email, phone, and LinkedIn?" Skill does:

Explains Mixmax sequences as multi-channel campaigns with email, phone, LinkedIn Sales Navigator, and task steps
Walks through creating a sequence: name, stages, channel per stage, timing between stages
Explains how to add LinkedIn Sales Navigator steps (InMail and connection requests) as automated sequence stages
Notes that LinkedIn Sales Navigator license is required separately Result: User has a multi-channel sequence with email, phone, and LinkedIn steps configured
Example 2: Salesforce integration with advanced rules

User says: "I want to automatically add prospects to a Mixmax sequence when an opportunity moves to a specific stage in Salesforce" Skill does:

States upfront that Salesforce object-triggered rules require Growth+CRM plan (~$89/user/mo)
Walks through creating an advanced rule: trigger on Salesforce Opportunity stage change → action: add related contact to sequence
Explains how to configure the rule trigger (Salesforce object, field, condition) and action (target sequence, recipient mapping)
Suggests testing with a single opportunity before applying broadly Result: User has an advanced rule that auto-enrolls prospects into sequences based on Salesforce deal stage changes
Example 3: API-driven recipient management

User says: "I want to use the Mixmax API to programmatically add recipients to a sequence" Skill does:

Points to references/mixmax-api-reference.md for full API documentation
Explains API key authentication via the X-API-Token header
Walks through the workflow: GET /sequences to find the sequence ID → POST /sequences/:id/recipients to add recipients
Warns about undocumented rate limits and recommends conservative batching Result: User understands the API workflow for adding recipients and the precautions needed
Troubleshooting
Email tracking not showing opens

Symptom: Emails show as sent but no open notifications appear Cause: Recipient's email client blocks tracking pixels (Apple Mail Privacy Protection, corporate proxies), or tracking is not enabled for the message Solution: Verify tracking is enabled in the Mixmax compose window before sending (tracking toggle should be on). Note that Apple Mail (iOS 15+) pre-loads images, which may inflate or block accurate tracking. For critical prospects, rely on click tracking (include a link) and reply tracking instead of open tracking. See /sales-email-tracking for a full tracking strategy.

Salesforce rules not triggering

Symptom: Advanced rules configured to trigger on Salesforce object changes are not firing Cause: Not on Growth+CRM plan, Salesforce connection expired or disconnected, rule conditions too narrow, or Salesforce sync delay Solution: Confirm you are on the Growth+CRM plan (~$89/user/mo) — advanced Salesforce rules are not available on lower plans. Re-authorize the Salesforce connection in Mixmax settings. Check the rule conditions — test with a broad condition first, then narrow down. Allow up to a few minutes for Salesforce sync delays.

Sequence emails landing in spam

Symptom: Recipients report sequence emails going to spam or not arriving Cause: Domain not authenticated, sending too many emails too fast, or email content triggering spam filters Solution: Verify custom sending domain with SPF/DKIM/DMARC authentication. Start with low volume and ramp up gradually. Avoid spam trigger words in subject lines and body. Use Smart Send to optimize send times. Check sender reputation at mail-tester.com. See /sales-deliverability for a comprehensive deliverability strategy.

Weekly Installs
49
Repository
sales-skills/sales
GitHub Stars
14
First Seen
Mar 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass