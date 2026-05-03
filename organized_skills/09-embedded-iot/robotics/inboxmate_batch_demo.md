---
rating: ⭐⭐
title: inboxmate-batch-demo
url: https://skills.sh/psquared-development/psquared-skills/inboxmate-batch-demo
---

# inboxmate-batch-demo

skills/psquared-development/psquared-skills/inboxmate-batch-demo
inboxmate-batch-demo
Installation
$ npx skills add https://github.com/psquared-development/psquared-skills --skill inboxmate-batch-demo
SKILL.md
InboxMate Batch Demo Pipeline
Prerequisites — Environment Variables

All required tokens are in the .env file in the current working directory (the agenthub repo root). Read it at startup to get:

PSQUARED_CRM_TOKEN — Bearer token for Twenty CRM GraphQL API
NUXT_MCP_DEMO_TOKEN — Bearer token for the InboxMate MCP server
OPENBRAND_API_KEY — API key for OpenBrand brand color/logo extraction

Do this first: Read .env from the current directory and extract these values. If any are missing, stop and ask the user.

Before starting, ask the user for the offer deadline:

When should the demo offers expire?
This sets the countdown timer on all demo pages in this batch.
Examples: "in 14 days", "2026-04-01", "end of month"


Wait for the answer. Convert to an ISO 8601 date. Pass this deadline to every demo created in the batch — do NOT ask again per company.

Announce:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
InboxMate Batch Demo Pipeline
Offer deadline: [date]
Reading .env for CRM and MCP tokens...
Querying CRM for unprocessed prospects...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1 — Get Prospects from CRM

Read PSQUARED_CRM_TOKEN from .env and use it to query the Twenty CRM (GraphQL at https://crm.psquared.dev/graphql) for companies that do NOT yet have an opportunity. Use this approach:

Fetch all companies (up to 100)
Fetch all opportunities (up to 200)
Filter out companies that already have ANY opportunity (regardless of stage)

The remaining companies are unprocessed prospects.

Announce: Found [N] unprocessed prospects.

If there's a specific company or list the user wants to process, use that instead.

Step 2 — Validate Each Prospect's Website

For each prospect, before running the demo pipeline:

2a — Check if the website is reachable

Use WebFetch on the company's domain (from CRM domainName.primaryLinkUrl).

Skip the prospect if ANY of these are true:

Domain returns HTTP error (4xx, 5xx) or times out
Domain redirects to a parked/expired domain page
Domain shows a "coming soon" or "under construction" placeholder
Website has no meaningful content (just a logo and "contact us")
Website is clearly outdated — copyright year 2+ years old, broken images, obviously abandoned
Website is a social media profile only (LinkedIn, Facebook) — not a real business site
2b — Mark skipped prospects in CRM

Do NOT ask the user what to do. Auto-skip and mark in CRM immediately.

First, check if the Company object has a field like idealCustomerProfile (ICP) or a rating/status field you can use. Run this introspection query once at the start:

query { __type(name: "Company") { fields { name type { name kind ofType { name } } } } }


If there's a usable boolean/enum field (e.g. idealCustomerProfile): set it to false or the "not a fit" value to mark the company directly.

Regardless, also create a DISQUALIFIED opportunity so the company is excluded from future batch runs:

mutation CreateOpportunity($data: OpportunityCreateInput!) {
  createOpportunity(data: $data) { id name stage }
}


Variables:

{
  "data": {
    "name": "[Company] — Website not suitable",
    "stage": "DISQUALIFIED",
    "companyId": "[companyId]"
  }
}


Announce for each skip: SKIP: [Company] — [reason] Never pause to ask. Just mark and move to the next prospect.

2c — Collect valid prospects

Prospects with a working, current website proceed to Step 3.

Announce: [N] prospects ready for demo creation, [M] skipped.

Step 3 — Create Demos for Valid Prospects

For each valid prospect, invoke the /inboxmate-demo skill (or follow the inboxmate-demo SKILL.md pipeline).

Process one prospect at a time — do not parallelize MCP calls.

After each demo is created:

The inboxmate-demo pipeline creates an opportunity in CRM at SCREENING / PENDING_REVIEW with the demo URL — verify it was created
Announce the result

Announce after each:

DONE: [Company] — [playgroundUrl]

Step 4 — Summary

After all prospects are processed:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BATCH COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Demos created: [N]
  - [Company 1] → [url]
  - [Company 2] → [url]

Skipped (website issues): [M]
  - [Company A] — [reason]
  - [Company B] — [reason]

Already processed (had opportunity): [K]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Skip Criteria Quick Reference
Signal	Action
HTTP error / timeout	SKIP — "unreachable"
Parked / expired domain	SKIP — "parked domain"
"Coming soon" / "Under construction"	SKIP — "placeholder page"
No real content (just logo + contact form)	SKIP — "no meaningful content"
Copyright year 2+ years behind current	SKIP — "outdated (copyright YYYY)"
Broken images, dead links, 90s design	SKIP — "outdated/abandoned"
Social media profile only	SKIP — "no website (social only)"
No domain in CRM	SKIP — "no domain on file"
Working site with real content	PROCEED with demo
Weekly Installs
24
Repository
psquared-develo…d-skills
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail