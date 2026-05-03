---
title: patent-search
url: https://skills.sh/robthepcguy/claude-patent-creator/patent-search
---

# patent-search

skills/robthepcguy/claude-patent-creator/patent-search
patent-search
Installation
$ npx skills add https://github.com/robthepcguy/claude-patent-creator --skill patent-search
SKILL.md
Patent Search Skill

Two powerful patent search methods:

BigQuery Search (Recommended) - 100M+ worldwide patents, zero local storage
PatentsView API - Detailed US patent metadata (inventors, assignees, classifications, citations)

FOR CLAUDE: All files and dependencies installed.

Go directly to Quick Test section
Script at: .claude/skills/patent-search/bigquery_search.py
Run from skill directory
Windows: Use cmd syntax (dir, set, &&)
Quick Test
# Windows
cd ".claude\skills\patent-search"
set GOOGLE_APPLICATION_CREDENTIALS=%APPDATA%\\gcloud\\application_default_credentials.json
python bigquery_search.py search "voice biometric" 5

# Linux/macOS
cd .claude/skills/patent-search
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.config/gcloud/application_default_credentials.json"
python bigquery_search.py search "voice biometric" 5


Expected: 5 patent results in ~4 seconds

Quick Start
BigQuery Search
# Keyword search (2-3 keywords for best results)
python bigquery_search.py search "voice biometric authentication" 20

# Get specific patent (hyphenated format: US-XXXXXXX-XX)
python bigquery_search.py get US-12424224-B2

# CPC classification search
python bigquery_search.py cpc G10L 15

PatentsView API
Choosing the Right Method
Use BigQuery When:
Quick keyword search needed
Worldwide patents (not just US)
Fast results (3-4 seconds)
Zero local storage
CPC classification search
Budget-conscious (free tier: 1TB/month)
Use PatentsView When:
Need detailed US patent metadata
Searching by inventor/assignee
Citation analysis required
Complex boolean queries
Exact field matching
Patent family analysis
Combined Workflow
Start with BigQuery (broad keyword search)
Identify relevant patents and CPC codes
Switch to PatentsView (detailed metadata/citations)
Export final results

Example:

# Step 1: BigQuery broad search
python bigquery_search.py search "voice biometric authentication" 20

# Step 2: Found CPC G10L17, search more
python bigquery_search.py cpc G10L17 50

# Step 3: Use PatentsView for inventor/assignee analysis

Instructions for Claude

When user requests patent searches:

Understand Goal: Technology, time period, prior art vs competitive analysis, US vs worldwide
Check Dependencies: Verify BigQuery/PatentsView setup
Choose Method: Default BigQuery for broad, PatentsView for detailed
Optimize Queries:
BigQuery: 2-3 keywords, simplify if zero results, use CPC codes
PatentsView: Verify API key, construct JSON queries, handle pagination
Present Results: Parse JSON, highlight key info, provide Google Patents URLs
Offer Next Steps: Suggest refinements, related classifications, citation analysis
Common Use Cases
Prior Art Search
BigQuery keyword search
Identify CPC codes
BigQuery CPC search
PatentsView citation analysis
Document findings
Competitive Intelligence
PatentsView search by assignee
Filter by date range
Group by CPC
Identify key inventors
Trend report
Technology Landscape
BigQuery CPC search worldwide
Analyze by country/date
Identify patent families
PatentsView US details
Summary report
Freedom to Operate
BigQuery keyword + CPC search
Filter by jurisdiction/active status
PatentsView claim analysis
Review forward citations
Risk assessment
Performance & Coverage
Method	Patents	Coverage	Speed	Cost	Storage
BigQuery	100M+	Worldwide	3-4s	Free*	0GB
PatentsView	9.2M	US only	1-3s	Free	0GB

*Free tier: 1TB queries/month

Quick Reference
BigQuery Commands
python bigquery_search.py search "query" <limit>
python bigquery_search.py get <PATENT-NUMBER>
python bigquery_search.py cpc <CODE> <limit>

Common CPC Codes
Code	Technology
G10L	Speech analysis/synthesis
G10L15	Speech recognition
G10L17	Speaker recognition/verification
G06F21	Security arrangements
G06N	Computing models
Troubleshooting

FOR CLAUDE: Only run diagnostics if Quick Test fails.

Problem	Solution
BigQuery auth fails	gcloud auth application-default login
No module google.cloud	pip install google-cloud-bigquery db-dtypes
Zero results	Simplify query (2-3 keywords max)
Patent get fails	Use hyphenated format: US-XXXXX-XX
PatentsView 403	Set API key environment variable
Rate limit (429)	Wait 60 seconds (PatentsView: 45 req/min)
Weekly Installs
25
Repository
robthepcguy/cla…-creator
GitHub Stars
97
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn