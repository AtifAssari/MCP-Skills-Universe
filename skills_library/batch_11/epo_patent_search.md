---
title: epo-patent-search
url: https://skills.sh/robthepcguy/claude-patent-creator/epo-patent-search
---

# epo-patent-search

skills/robthepcguy/claude-patent-creator/epo-patent-search
epo-patent-search
Installation
$ npx skills add https://github.com/robthepcguy/claude-patent-creator --skill epo-patent-search
SKILL.md
EPO Patent Search Skill

Search European patents using the EPO Open Patent Services (OPS) API and Google BigQuery with EP country filtering.

When to Use

Invoke this skill when users ask to:

Search for European patents
Find EP prior art for a technology
Check legal status of EP patents
Explore patent families across jurisdictions
Conduct EP freedom-to-operate analysis
Research the EP patent landscape for a technology area
Get full-text EP claims or descriptions
What This Skill Does

Provides access to European patent data through two methods:

EPO OPS API (European Patent Data):

Full-text EP patent retrieval (claims, description)
Legal status and procedural history
INPADOC patent family linking
Applicant and inventor search
EP publication types (A1, A2, A3, B1, B2)
Designated contracting states

BigQuery (Worldwide Patents, EP Filter):

Fast keyword search across 100M+ patents with country="EP"
CPC classification search for EP patents
Filing trend analysis
Cross-jurisdiction comparison
Required Setup
BigQuery (Primary)

Prerequisites:

Google Cloud Project (free to create)
BigQuery API enabled
Application Default Credentials configured

Setup:

gcloud auth application-default login
export GOOGLE_CLOUD_PROJECT=your-project-id

EPO OPS API (Optional, for full-text/legal status)

Prerequisites:

Register at https://developers.epo.org/
Create an application to get Consumer Key and Secret
Set environment variables

Setup:

export EPO_OPS_CONSUMER_KEY=your-key
export EPO_OPS_CONSUMER_SECRET=your-secret

How to Use

When this skill is invoked:

Determine search type:

Keyword search: use BigQuery with country="EP" for speed
Full-text retrieval: use EPO OPS for complete claims/description
Legal status: use EPO OPS for procedural data
Family search: use EPO OPS INPADOC family service
CPC search: use BigQuery for broad classification browsing

Execute search:

BigQuery keyword search (EP patents):

results = search_patents_bigquery(
    query="blockchain authentication",
    country="EP",
    limit=20,
    start_year=2020
)


BigQuery CPC search (EP patents):

results = search_patents_by_cpc_bigquery(
    cpc_code="H04L9/32",
    country="EP",
    limit=30
)


EPO OPS full-text retrieval:

results = search_epo_patents(
    query="EP3456789",
    search_type="full_text"
)


EPO OPS family search:

results = search_epo_patents(
    query="EP3456789",
    search_type="family"
)


Present results:

Rank by relevance
Show key metadata (title, applicant, dates, IPC/CPC)
Highlight legal status (in force, expired, opposed)
Provide links to Espacenet for full documents
Note patent family members in other jurisdictions
Search Result Format
{
    "publication_number": "EP3456789A1",
    "title": "Authentication system using distributed ledger",
    "abstract": "A system for authenticating...",
    "applicant": "Example GmbH",
    "inventors": ["Hans Mueller", "Maria Schmidt"],
    "filing_date": "2019-03-15",
    "publication_date": "2020-01-22",
    "grant_date": null,
    "ipc_codes": ["H04L9/32", "G06F21/31"],
    "cpc_codes": ["H04L9/32", "G06F21/31"],
    "designated_states": ["DE", "FR", "GB", "NL", "IT"],
    "priority_claims": ["US16/234567 (2018-12-28)"],
    "family_id": "67890123",
    "legal_status": "Examination in progress",
    "publication_type": "A1"
}

EP Publication Types
Code	Type	Description
A1	Application + search	Published EP application with search report
A2	Application only	Published without search report
A3	Search report	Search report published separately
B1	Granted patent	Patent specification as granted
B2	Amended patent	Amended specification after opposition
B3	Limited patent	Patent after limitation proceedings
Cross-Jurisdiction Linking

Use family_id to find related patents across jurisdictions:

EP3456789A1 (European application)
├── US10123456B2 (US counterpart)
├── CN112345678A (Chinese counterpart)
├── JP2020-123456A (Japanese counterpart)
└── WO2019/123456A1 (PCT application)


This is essential for:

Prior art analysis (one patent may be available in multiple languages)
Freedom-to-operate (check where patent is in force)
Competitive intelligence (track filing strategy)
Presentation Format

Present search results as:

EP PATENT SEARCH RESULTS
=========================

Query: "blockchain authentication"
Source: BigQuery (EP filter) + EPO OPS
Found: 89 EP patents
Date Range: 2020-2025

[1] EP3456789B1 - Authentication system using distributed ledger
    Applicant: Example GmbH (DE)
    Filed: 2019-03-15 | Granted: 2022-08-10
    IPC: H04L9/32, G06F21/31
    Status: Patent in force (validated in DE, FR, GB)
    Family: US10123456B2, CN112345678B, WO2019/123456A1
    Espacenet: https://worldwide.espacenet.com/patent/search?q=EP3456789

[2] EP3567890A1 - Blockchain-based identity verification method
    Applicant: Tech Corp (US)
    Filed: 2020-01-10 | Published: 2021-06-16
    IPC: H04L9/00, G06Q20/38
    Status: Examination in progress
    Family: US20210203456A1, WO2020/234567A1

---

Top CPC Codes in Results:
- H04L9/32 (15 patents): Authentication/verification
- G06F21/31 (12 patents): User authentication
- H04L9/00 (8 patents): Cryptographic mechanisms

Common Use Cases
EP Prior Art Search
BigQuery keyword search (country="EP")
Identify relevant CPC codes
BigQuery CPC search (country="EP")
EPO OPS full-text for top results
Document findings with citations
Patent Family Analysis
Find EP patent via BigQuery or EPO OPS
Get family_id
Search for family members worldwide
Map filing strategy across jurisdictions
Check legal status in each country
EP Freedom-to-Operate
Search EP patents in relevant technology
Filter for granted patents (B1/B2)
Check legal status (in force vs expired)
Identify validated countries
Assess infringement risk
EP Opposition Research
Find granted EP patents (B1)
Check if within 9-month opposition window
Search for prior art predating priority date
Analyze claims scope
Assess opposition grounds (Art. 100 EPC)
Performance & Coverage
Method	Patents	Coverage	Speed	Cost
BigQuery (EP)	~5M EP	EP applications + grants	3-4s	Free*
EPO OPS	All EP	Full text + legal status	1-3s	Free**

*BigQuery free tier: 1TB queries/month (~20,000 searches) **EPO OPS: Fair use (2.5GB data traffic per week)

Tools Available
Bash: To run search scripts
Read: To load saved search results
Write: To save patent search results
Weekly Installs
19
Repository
robthepcguy/cla…-creator
GitHub Stars
97
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass