---
rating: ⭐⭐
title: sf-soql
url: https://skills.sh/jaganpro/sf-skills/sf-soql
---

# sf-soql

skills/jaganpro/sf-skills/sf-soql
sf-soql
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-soql
SKILL.md
sf-soql: Salesforce SOQL Query Expert

Use this skill when the user needs SOQL/SOSL authoring or optimization: natural-language-to-query generation, relationship queries, aggregates, query-plan analysis, and performance/safety improvements for Salesforce queries.

When This Skill Owns the Task

Use sf-soql when the work involves:

.soql files
query generation from natural language
relationship queries and aggregate queries
query optimization and selectivity analysis
SOQL/SOSL syntax and governor-aware design

Delegate elsewhere when the user is:

performing bulk data operations → sf-data
embedding query logic inside broader Apex implementation → sf-apex
debugging via logs rather than query shape → sf-debug
Required Context to Gather First

Ask for or infer:

target object(s)
fields needed
filter criteria
sort / limit requirements
whether the query is for display, automation, reporting-like analysis, or Apex usage
whether performance / selectivity is already a concern
Recommended Workflow
1. Generate the simplest correct query

Prefer:

only needed fields
clear WHERE criteria
reasonable LIMIT when appropriate
relationship depth only as deep as necessary
2. Choose the right query shape
Need	Default pattern
parent data from child	child-to-parent traversal
child rows from parent	subquery
counts / rollups	aggregate query
records with / without related rows	semi-join / anti-join
text search across objects	SOSL
3. Optimize for selectivity and safety

Check:

indexed / selective filters
no unnecessary fields
no avoidable wildcard or scan-heavy patterns
security enforcement expectations
4. Validate execution path if needed

If the user wants runtime verification, hand off execution to:

sf-data
High-Signal Rules
never use SELECT * style thinking; query only required fields
do not query inside loops in Apex contexts
prefer filtering in SOQL rather than post-filtering in Apex
use aggregates for counts and grouped summaries instead of loading unnecessary records
evaluate wildcard usage carefully; leading wildcards often defeat indexes
account for security mode / field access requirements when queries move into Apex
Output Format

When finishing, report in this order:

Query purpose
Final SOQL/SOSL
Why this shape was chosen
Optimization or security notes
Execution suggestion if needed

Suggested shape:

Query goal: <summary>
Query: <soql or sosl>
Design: <relationship / aggregate / filter choices>
Notes: <selectivity, limits, security, governor awareness>
Next step: <run in sf-data or embed in Apex>

Cross-Skill Integration
Need	Delegate to	Reason
run the query against an org	sf-data	execution and export
embed the query in services/selectors	sf-apex	implementation context
analyze slow-query symptoms from logs	sf-debug	runtime evidence
wire query-backed UI	sf-lwc	frontend integration
Reference Map
Start here
references/soql-syntax-reference.md
references/query-optimization.md
references/cli-commands.md
Specialized guidance
references/soql-reference.md
references/anti-patterns.md
references/selector-patterns.md
references/field-coverage-rules.md
assets/
Score Guide
Score	Meaning
90+	production-optimized query
80–89	good query with minor improvements possible
70–79	functional but performance concerns remain
< 70	needs revision before production use
Weekly Installs
1.1K
Repository
jaganpro/sf-skills
GitHub Stars
404
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass