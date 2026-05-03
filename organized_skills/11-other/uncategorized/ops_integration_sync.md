---
rating: ⭐⭐
title: ops integration sync
url: https://skills.sh/sixtysecondsapp/use60/ops-integration-sync
---

# ops integration sync

skills/sixtysecondsapp/use60/Ops Integration Sync
Ops Integration Sync
Installation
$ npx skills add https://github.com/sixtysecondsapp/use60 --skill 'Ops Integration Sync'
SKILL.md
Available Context

@_platform-references/org-variables.md

Ops Integration Sync
Goal

Sync ops table data with external CRM and outreach platforms. This skill bridges the gap between the user's enriched ops tables and their go-to-market tools, enabling bidirectional data flow with HubSpot, one-way push to Attio, and campaign-ready lead push to Instantly.

Prerequisites

Before any sync can execute, the organization must have integration credentials configured:

HubSpot: Requires hubspot credential in integration_credentials table with a valid API key
Attio: Requires attio credential in integration_credentials table with a valid API key
Instantly: Requires instantly credential in integration_credentials table with a valid API key

If credentials are missing, inform the user: "Your [integration] credentials aren't configured yet. Ask your admin to set them up in Settings > Integrations."

Available Actions
1. sync_ops_hubspot -- HubSpot Sync (Bidirectional)

Syncs table data with HubSpot contacts. Supports both push and pull directions.

Parameters:

table_id (required): The ops table to sync
direction (required): push or pull
push: Sends table rows to HubSpot as contacts. Creates new contacts or updates existing ones matched by email.
pull: Imports HubSpot contacts into the ops table. Creates new rows or updates existing ones matched by email.
field_mapping (optional): Custom mapping between table columns and HubSpot properties. If omitted, uses default mapping (email, first_name, last_name, company, job_title, phone).

When to use push vs pull:

Pull first when the user wants to enrich existing HubSpot contacts -- pull them into an ops table, run enrichments, then push back.
Push when the user has built a prospecting list in ops tables and wants to add them to HubSpot for CRM tracking.
Bidirectional workflow: pull -> enrich -> push (see seq-ops-hubspot-enrich-sync sequence).

Example conversation:

User: "Sync my prospecting table with HubSpot"
Assistant: "Which direction? I can:
  - **Push** -- send your table contacts to HubSpot
  - **Pull** -- import your HubSpot contacts into this table
  Which would you like?"

2. sync_ops_attio -- Attio Sync (Push Only)

Pushes table data to Attio as company or person records.

Parameters:

table_id (required): The ops table to sync

Notes:

Attio sync is currently push-only (table -> Attio)
Records are matched by email (people) or domain (companies)
New records are created if no match is found
3. push_ops_to_instantly -- Instantly Campaign Push

Pushes table leads to Instantly for outreach campaigns. Can add to an existing campaign or create a new one.

Parameters:

table_id (required): The ops table containing leads
campaign_id (optional): Add leads to an existing Instantly campaign
campaign_config (optional): Configuration for creating a new campaign:
name: Campaign name
schedule: Send schedule (days, time windows, timezone)
sequences: Email sequence steps

Important notes:

Table must have an email column -- leads without valid emails will be skipped
When creating a new campaign, campaign_schedule with a schedules array is mandatory
Timezone must use the Instantly-supported enum (e.g., America/Chicago, not America/New_York)
Default timezone: America/Chicago
Leads are deduplicated by email within the campaign

Example conversation:

User: "Send these leads to Instantly"
Assistant: "I'll push your 47 leads to Instantly. Would you like to:
  - Add them to an **existing campaign**? (I'll need the campaign ID)
  - Create a **new campaign**? (I'll set up a default schedule)
  Which do you prefer?"

Sync Flow
Validate credentials -- Check that the organization has valid credentials for the target integration
Validate table -- Confirm the table exists and has the required columns (e.g., email for Instantly)
Confirm with user -- Show record count and sync direction before executing
Execute sync -- Run the sync action and report results
Report outcome -- Show records synced, records skipped, and any errors
Error Handling
Missing credentials

Do not attempt the sync. Tell the user exactly which credential is missing and where to configure it.

Missing required columns

If pushing to Instantly and no email column exists, inform the user: "Your table needs an email column to push to Instantly. Would you like me to add one?"

Partial sync failures

Report the count of successful and failed records. Common failure reasons:

Invalid email format
Duplicate records in target system
Rate limiting from the integration API
Rate limits

HubSpot and Instantly have rate limits. For large tables (500+ rows), the sync may take longer. Inform the user of expected duration.

Guidelines
Always confirm the sync direction and target before executing
Show a preview of what will be synced (record count, key fields)
For HubSpot pull, warn that existing table data in matching columns will be overwritten
For Instantly push, verify the table has usable email addresses before pushing
After sync, suggest next steps (e.g., "Your contacts are in HubSpot. Want me to create a follow-up task list?")
Weekly Installs
–
Repository
sixtysecondsapp/use60
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn