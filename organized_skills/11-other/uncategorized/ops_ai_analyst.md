---
rating: ⭐⭐
title: ops ai analyst
url: https://skills.sh/sixtysecondsapp/use60/ops-ai-analyst
---

# ops ai analyst

skills/sixtysecondsapp/use60/Ops AI Analyst
Ops AI Analyst
Installation
$ npx skills add https://github.com/sixtysecondsapp/use60 --skill 'Ops AI Analyst'
SKILL.md
Available Context

@_platform-references/org-variables.md

Ops AI Analyst
Goal

Enable sales reps to ask natural language questions about their Ops table data and receive AI-powered insights. Instead of manually scrolling through rows or building complex filters, reps can ask questions like "who are my highest-scoring VP-level leads?" or "show me companies in fintech with more than 100 employees" and get instant answers.

This skill bridges the gap between structured data and conversational interaction -- making ops tables feel like talking to a smart analyst who knows your prospect database inside out.

Required Capabilities
Ops Tables: Access to AI query and insights APIs
Inputs
table_id: ID of the ops table to query or analyze
query: Natural language question to ask about the data (e.g., "Which leads are VPs at companies with 50+ employees?")
Instructions
Natural Language Queries

When the user asks a question about their table data:

Identify the target table. If not specified, check if there's a table in the current conversation context.
Formulate the query from the user's question. Pass it as-is -- the AI query engine handles natural language natively.
Call execute_action("ai_query_ops_table", { table_id: "<id>", query: "<user's question>" })
Present results in a clean format:
Show the matching rows in a scannable table
Include the total count: "Found 12 leads matching your query"
Highlight the relevant columns that the query is filtering on
Suggest follow-up actions: "Want me to enrich these leads? Or narrow the search further?"
Common Query Patterns

Help the user by understanding these natural patterns:

User Says	Query Intent
"Find leads at enterprise companies"	Filter by company size
"Who has a VP or Director title?"	Filter by title/seniority
"Show leads we haven't emailed yet"	Filter by empty email status column
"Which companies are in healthcare?"	Filter by industry
"Top 10 leads by score"	Sort + limit
"Leads added this week"	Filter by date
"Companies with more than 200 employees"	Filter by size threshold
AI Insights

When the user wants broader analysis:

Call execute_action("get_ops_insights", { table_id: "<id>" })
Present the insights in a structured format covering:
Data quality: Completeness of columns, missing data patterns
Distribution: Industry breakdown, title seniority mix, company size spread
Patterns: Clusters, commonalities among high-scoring leads
Recommendations: Which segments to prioritize, gaps to fill, enrichment suggestions
Make insights actionable: each insight should connect to a next step
Combining Queries with Actions

After showing query results, proactively suggest relevant next steps:

"Want me to add these 12 leads to a separate table?"
"Should I enrich the company data for these results?"
"Want me to start a sequence for the top 5?"
Available Actions
Action	Parameters	Returns
ai_query_ops_table	{ table_id: string, query: string }	Matching rows with relevance context
get_ops_insights	{ table_id: string }	AI-generated insights about the data
Output Format
Query Results
QUERY: "VP or Director level leads at companies with 50+ employees"
FOUND: 12 leads

Name              Title              Company         Size    Score
Sarah Chen        VP Engineering     TechFlow        120     92
James Park        Director Sales     DataBridge      85      88
Maria Garcia      VP Product         CloudScale      200     85
Lisa Wong         Director Ops       FinServ Inc     150     81
...

Showing top 12 results. Want to narrow this further or take action on these leads?

Insights Response
TABLE INSIGHTS: Lead Prospects (142 rows)

DATA QUALITY
  Overall completeness: 78%
  Missing emails: 23 rows (16%)
  Missing titles: 8 rows (6%)

DISTRIBUTION
  Top industries: SaaS (34%), Fintech (22%), Healthcare (15%)
  Seniority: VP+ (28%), Director (31%), Manager (24%), IC (17%)
  Company size: 1-50 (18%), 51-200 (45%), 201-500 (27%), 500+ (10%)

PATTERNS
  High-scoring leads (80+) are concentrated in SaaS and Fintech
  VP-level contacts have 2.3x higher engagement scores
  Companies with 51-200 employees show the strongest response rates

RECOMMENDATIONS
  1. Prioritize the 18 VP+ leads in SaaS -- highest score cluster
  2. Enrich the 23 rows missing email addresses before outreach
  3. Consider adding more Healthcare leads -- strong scores but small sample

Error Handling
Ambiguous query

If the query is too vague to produce useful results: "That's a broad query -- could you be more specific? For example: 'Find leads with VP titles at fintech companies' or 'Show companies with over 100 employees.'"

No results

If the query returns zero matches: "No leads match that query. Here's what I see in the table: [brief summary of data distribution]. Want to try a different filter?"

Table too small for insights

If the table has fewer than 10 rows: "This table only has X rows -- not enough data for meaningful statistical insights. Want me to help add more leads first?"

Query on empty table

If the table has no data: "This table is empty. Let me help you populate it first -- I can import from Apollo, HubSpot, or add leads manually."

Guidelines
Pass the user's natural language query directly to the AI query engine -- don't try to pre-process it into SQL or filters
When showing query results, only display the most relevant columns (max 5-6) to keep output scannable
Always include the total count of matches, even when paginating
For insights, focus on actionable patterns, not just statistics -- "VP leads score 2x higher" is better than "average VP score is 84"
Suggest next steps after every query -- queries should lead to action, not just information
If the user asks a follow-up question, maintain the table context from the previous query
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