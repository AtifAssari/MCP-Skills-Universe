---
rating: ⭐⭐
title: ai ark reverse lookup
url: https://skills.sh/sixtysecondsapp/use60/ai-ark-reverse-lookup
---

# ai ark reverse lookup

skills/sixtysecondsapp/use60/AI Ark Reverse Lookup
AI Ark Reverse Lookup
Installation
$ npx skills add https://github.com/sixtysecondsapp/use60 --skill 'AI Ark Reverse Lookup'
SKILL.md
Available Context

@_platform-references/org-variables.md

AI Ark Reverse Lookup
Goal

Enrich a known contact or batch of contacts with current profile data from AI Ark.

Required Capabilities
AI Ark API: Reverse people lookup via ai-ark-enrich edge function
Inputs

Provide at least one identifier:

email: Contact email address
linkedin_url: LinkedIn profile URL
full_name + company_name: Name and company combo
table_id: For batch mode across a table
Execution
Single Contact
Call ai-ark-enrich with action: 'reverse_lookup' and identifier
Return enriched profile data
Batch Mode
Call ai-ark-enrich with action: 'bulk_enrich' and table_id
Processes all rows, matching by email > LinkedIn > name+company
Caches full response in source_data.ai_ark (enrich-once pattern)
Credit Cost

Each reverse lookup call consumes credits. Bulk enrichment processes contacts individually (4 concurrent, rate-limited). Warn users about credit cost before batch operations.

Output Contract

Return enriched fields:

current_title, company, seniority
linkedin_url, location, photo_url
Note: Email and phone are NOT returned by reverse lookup — use the mobile-phone-finder endpoint for phone numbers
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