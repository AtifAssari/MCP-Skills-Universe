---
title: reporting-pipelines
url: https://skills.sh/bobmatnyc/claude-mpm-skills/reporting-pipelines
---

# reporting-pipelines

skills/bobmatnyc/claude-mpm-skills/reporting-pipelines
reporting-pipelines
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill reporting-pipelines
SKILL.md
Reporting Pipelines
Overview

Your reporting pattern is consistent across repos: run a CLI or script that emits structured data, then export CSV/JSON/markdown reports with timestamped filenames into reports/ or tests/results/.

GitFlow Analytics Pattern
# Basic run
gitflow-analytics -c config.yaml --weeks 8 --output ./reports

# Explicit analyze + CSV
gitflow-analytics analyze -c config.yaml --weeks 12 --output ./reports --generate-csv


Outputs include CSV + markdown narrative reports with date suffixes.

EDGAR CSV Export Pattern

edgar/scripts/create_csv_reports.py reads a JSON results file and emits:

executive_compensation_<timestamp>.csv
top_25_executives_<timestamp>.csv
company_summary_<timestamp>.csv

This script uses pandas for sorting and percentile calculations.

Standard Pipeline Steps
Collect base data (CLI or JSON artifacts)
Normalize into rows/records
Export CSV/JSON/markdown with timestamp suffixes
Summarize key metrics in stdout
Store outputs in reports/ or tests/results/
Naming Conventions
Use YYYYMMDD or YYYYMMDD_HHMMSS suffixes
Keep one output directory per repo (reports/ or tests/results/)
Prefer explicit prefixes (e.g., narrative_report_, comprehensive_export_)
Troubleshooting
Missing output: ensure output directory exists and is writable.
Large CSVs: filter or aggregate before export; keep summary CSVs for quick review.
Related Skills
universal/data/sec-edgar-pipeline
toolchains/universal/infrastructure/github-actions
Weekly Installs
170
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass