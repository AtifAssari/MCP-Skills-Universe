---
rating: ⭐⭐
title: apify results query
url: https://skills.sh/sixtysecondsapp/use60/apify-results-query
---

# apify results query

skills/sixtysecondsapp/use60/Apify Results Query
Apify Results Query
Installation
$ npx skills add https://github.com/sixtysecondsapp/use60 --skill 'Apify Results Query'
SKILL.md
Available Context

@_platform-references/org-variables.md

Apify Results Query
Goal

Query and filter mapped results from completed Apify actor runs using natural language filters.

Required Capabilities
Apify API: Results stored in apify_results / apify_mapped_records tables, queried via apify-admin edge function
Inputs
run_id: Optional run ID (defaults to most recent completed run)
filter_description: Natural language filter criteria
columns: Optional column selection
limit: Row limit (default 50)
Execution
If no run_id provided, fetch the most recent completed run for the user's organization
Translate filter_description into SQL-compatible filters on apify_mapped_records
Call apify-admin with action: 'query_results', run ID, and filters
Present results as a table with GDPR flags highlighted
Offer follow-up actions: "export to CSV", "push to CRM", "push to Instantly"
GDPR Handling

Results may contain personal email flags (is_personal_email). When present:

Show a warning badge on flagged rows
Suggest the user review before exporting or pushing to outbound tools
Count and display total flagged records
Output Contract

Return a table with the mapped columns from the actor run, plus:

GDPR Flag column (if personal emails detected)
Total count and page info
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