---
rating: ⭐⭐
title: ops enrichment manager
url: https://skills.sh/sixtysecondsapp/use60/ops-enrichment-manager
---

# ops enrichment manager

skills/sixtysecondsapp/use60/Ops Enrichment Manager
Ops Enrichment Manager
Installation
$ npx skills add https://github.com/sixtysecondsapp/use60 --skill 'Ops Enrichment Manager'
SKILL.md
Available Context

@_platform-references/org-variables.md

Ops Enrichment Manager
Goal

Run AI-powered enrichment on Ops table columns and monitor enrichment job progress. Enrichment transforms empty or sparse columns into rich, AI-generated data -- company summaries, personalized intros, lead scores, industry classifications, and more.

Enrichment is the step that turns a raw list of names and emails into an actionable prospect database. Without it, reps are stuck doing manual research. With it, every row gets AI-analyzed data in minutes.

Required Capabilities
Ops Tables: Access to enrichment APIs for ops tables
Inputs
table_id: ID of the ops table containing the column to enrich
column_id: ID of the specific column to enrich
prompt: Custom AI prompt that describes what to generate (e.g., "Write a one-line personalized intro based on the lead's title and company")
Instructions
Starting Enrichment

When the user wants to enrich a column:

Identify the table and column. If the user says "enrich the company summary column", resolve the table and column IDs.
If no column is specified, ask which column to enrich. Show the table's columns and suggest candidates:
Columns of type ai_generate are natural enrichment targets
Empty or sparse columns benefit most from enrichment
If the column has a built-in enrichment type (e.g., company data lookup, email finder), no custom prompt is needed.
For AI-generated columns, check if a prompt is configured. If not, ask the user:
"What should the AI generate for this column? For example: 'Write a personalized outreach opener based on the lead's role and company.'"
Call execute_action("enrich_table_column", { table_id: "<id>", column_id: "<col_id>", prompt: "<prompt>" })
Report that enrichment has started: "Enrichment started for [Column Name] in [Table Name]. Processing X rows -- I'll check progress for you."
Checking Enrichment Status

When the user asks about enrichment progress:

Call execute_action("get_enrichment_status", { table_id: "<id>" })
Present a clear status report:
Overall progress percentage
Rows completed vs total
Estimated time remaining (if available)
Any errors or failures
If enrichment is complete, congratulate and suggest next steps: "Enrichment complete! All 142 rows now have [column name] data. Want to view the results?"
Suggesting Enrichment

When viewing a table with empty columns, proactively suggest enrichment:

"I notice the [Column Name] column is mostly empty (12% filled). Want me to run enrichment on it?"
For ai_generate columns without data, suggest a prompt based on the column name
Available Actions
Action	Parameters	Returns
enrich_table_column	{ table_id: string, column_id: string, prompt?: string }	Enrichment job with ID and status
get_enrichment_status	{ table_id: string }	Progress with completion %, row counts, errors
Output Format
Enrichment Started
ENRICHMENT STARTED
  Table: Lead Prospects
  Column: Company Summary
  Rows to process: 142
  Prompt: "Write a 2-sentence company overview based on the company name and domain"

I'll check back on progress. You can ask me "how's enrichment going?" anytime.

Enrichment Status
ENRICHMENT PROGRESS
  Table: Lead Prospects
  Column: Company Summary

  [=========>          ] 67% complete
  95 of 142 rows processed
  3 errors (missing company data)
  Est. remaining: ~2 minutes

Enrichment Complete
ENRICHMENT COMPLETE
  Table: Lead Prospects
  Column: Company Summary

  142 rows processed
  139 successful
  3 skipped (insufficient source data)

Want to view the enriched data?

Error Handling
No enrichable columns

If the table has no columns suitable for enrichment: "This table doesn't have any AI-generated or enrichable columns. Want me to add one? For example, I can add a 'Company Summary' column that AI will populate."

Enrichment already running

If enrichment is already in progress for the requested column: "Enrichment is already running on [Column Name] -- currently at X%. Want me to check back when it's done?"

Missing source data

If enrichment fails for some rows because required source columns are empty: "Enrichment completed for 95% of rows. 7 rows were skipped because they're missing [Source Column] data. Want to fill those in first?"

Prompt not provided for AI column

If the user starts enrichment on an ai_generate column without a prompt: "This is an AI-generated column -- I need to know what to generate. What should each cell contain? For example: 'A personalized outreach opening line based on the lead's role and recent company news.'"

Guidelines
Always show which table and column are being enriched -- avoid ambiguity
For large tables (500+ rows), set expectations: "This will take a few minutes for 500 rows"
Suggest checking status after starting rather than waiting: "Ask me 'how's enrichment going?' in a couple minutes"
When enrichment finishes, suggest viewing the results or running a follow-up action (like querying the enriched data)
If multiple columns need enrichment, suggest running them sequentially to avoid overwhelming the system
Always explain what the AI will generate before starting -- no surprises
Weekly Installs
–
Repository
sixtysecondsapp/use60
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass