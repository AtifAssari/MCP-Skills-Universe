---
title: sparql-university
url: https://skills.sh/letta-ai/skills/sparql-university
---

# sparql-university

skills/letta-ai/skills/sparql-university
sparql-university
Installation
$ npx skills add https://github.com/letta-ai/skills --skill sparql-university
SKILL.md
SPARQL University Query Tasks
Overview

This skill provides guidance for writing SPARQL queries against RDF/Turtle datasets, with emphasis on ensuring complete data analysis, proper query construction, and thorough verification.

Workflow
Step 1: Complete Data Acquisition

Before writing any query, ensure complete visibility of the source data.

Critical actions:

Read the entire Turtle (.ttl) or RDF file without truncation
If data appears truncated, request additional content or use pagination
Count distinct entities to verify data completeness
Document all entity types, predicates, and relationships observed

Verification checkpoint: Confirm the number of distinct entities matches expectations before proceeding.

Step 2: Schema Understanding

Map out the data structure before query construction.

Key elements to identify:

All entity types (classes) in the dataset
All predicates/properties used
Relationships between entities (e.g., professor → department → students)
Data types for literals (strings, dates, integers)
Naming conventions and value formats

Common patterns in academic data:

Roles/titles often use specific prefixes (e.g., "Professor of", "Associate Professor")
Dates may require comparison logic for "current" status
Geographic codes may use ISO standards (country codes)
Enrollment may span multiple departments
Step 3: Criteria Decomposition

Break down filtering requirements into discrete, testable conditions.

For each criterion:

Identify the exact predicate path to the relevant data
Determine the comparison type (equality, prefix match, membership, numeric)
Consider edge cases in the criterion interpretation
Test each criterion independently before combining

Example decomposition:

"Full professors" → Filter where role starts with specific prefix
"Working in EU countries" → Filter country codes against EU membership list
"Departments with >10 students" → Count students per department, apply threshold
Step 4: Query Construction

Build the query incrementally with validation at each stage.

Construction sequence:

Start with the most restrictive filter to reduce result set
Add one filter at a time, verifying intermediate results
Include all necessary SELECT variables
Add aggregation (GROUP BY, GROUP_CONCAT) last

Syntax validation:

Verify all prefixes are declared
Ensure FILTER expressions are properly closed
Check string comparisons use correct functions (STRSTARTS, CONTAINS, regex)
Confirm numeric comparisons handle data types correctly

Output format considerations:

Determine if results need aggregation (e.g., concatenating multiple values)
Specify sort order and separators for concatenated values
Distinguish between filtering criteria and output requirements (e.g., filter by EU countries but output ALL countries)
Step 5: Verification Strategy

Test the query against known expectations.

Verification methods:

Run the query and examine raw output
Manually trace through data for at least 2-3 entities to verify correctness
Check for both inclusion (expected entities present) AND exclusion (unexpected entities absent)
Verify aggregated values by manual count

Cross-reference checklist:

Do the returned entities match manual analysis?
Are all expected entities present in results?
Are any unexpected entities incorrectly included?
Do aggregated counts/values match manual verification?
Common Pitfalls
Incomplete Data Reading
Problem: Working with truncated data leads to missing entities
Prevention: Always confirm complete file content; re-read if truncated
Query Truncation
Problem: Long queries may be incompletely written
Prevention: After writing, read back the query file to verify completeness
Criterion Misinterpretation
Problem: Confusing filter criteria with output requirements
Prevention: Distinguish between "filter BY X" vs "output X" - these may differ
Date/Time Edge Cases
Problem: Incorrect handling of boundary dates
Prevention: Clarify whether comparisons are inclusive or exclusive; test boundaries
Aggregation Errors
Problem: Missing GROUP BY clauses or incorrect GROUP_CONCAT usage
Prevention: Verify aggregation syntax matches the query structure
EU Country List
Problem: Incomplete or outdated list of EU member country codes
Prevention: Use comprehensive list: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, GR, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
Cross-Entity Relationships
Problem: Miscounting entities across relationships (e.g., students in departments)
Prevention: Trace the full predicate path; verify join conditions
Testing Protocol
Syntax check: Ensure query parses without errors
Subset test: Run on a known subset of data with expected results
Full test: Run on complete dataset
Manual verification: Trace 2-3 results through source data
Boundary test: Check edge cases in filters (dates, counts, string matches)
Iteration Approach

If initial results do not match expectations:

Isolate which filter condition is causing discrepancies
Test each filter independently
Examine entities that should appear but don't (false negatives)
Examine entities that shouldn't appear but do (false positives)
Adjust filter logic based on findings
Re-verify after each adjustment
Weekly Installs
42
Repository
letta-ai/skills
GitHub Stars
93
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass