---
title: academic-research
url: https://skills.sh/ljt-520/openclaw-backup/academic-research
---

# academic-research

skills/ljt-520/openclaw-backup/academic-research
academic-research
Installation
$ npx skills add https://github.com/ljt-520/openclaw-backup --skill academic-research
SKILL.md
Academic Research

Search 250M+ academic works via OpenAlex. No API key required.

Built by Topanga — AI Research Consultant

Quick Start
Search papers by topic
python3 scripts/scholar-search.py search "transformer architectures" --limit 10

Search by author
python3 scripts/scholar-search.py author "Yann LeCun" --limit 5

Look up by DOI
python3 scripts/scholar-search.py doi "10.1038/s41586-021-03819-2"

Get citation chain (papers that cite a work)
python3 scripts/scholar-search.py citations "10.1038/s41586-021-03819-2" --direction both

Deep read (fetch abstract + full text when available)
python3 scripts/scholar-search.py deep "10.1038/s-03819-2"


###41586-021 JSON output for programmatic use

python3 scripts/scholar-search.py search "CRISPR" --json

Literature Review Workflow

Automated multi-step literature review:

python3 scripts/literature-review.py "algorithmic literacy in education" --papers 30 --output review.md


This will:

Search for papers across multiple query variations
Deduplicate and rank by relevance + citations
Identify thematic clusters
Generate a structured synthesis in markdown

Options:

--papers N — Target number of papers (default: 20)
--output FILE — Write review to file (default: stdout)
--years 2020-2025 — Restrict publication year range
--json — Output structured JSON instead of markdown
Output Format

All search commands return structured data per paper:

Title and publication year
Authors (up to 5)
Abstract (when available)
Citation count
DOI
Open access URL (when available)
Source journal/venue
Tips
OpenAlex sorts by relevance by default; use --sort citations for most-cited
Combine search + deep for quick triage: search first, deep-read promising hits
The literature review script caches results in /tmp/litreview_cache/ to avoid re-fetching
For full-text PDFs, pipe DOIs to your PDF extraction tool
Weekly Installs
9
Repository
ljt-520/openclaw-backup
GitHub Stars
1
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn