---
title: gsc-assistant
url: https://skills.sh/nicepkg/ai-workflow/gsc-assistant
---

# gsc-assistant

skills/nicepkg/ai-workflow/gsc-assistant
gsc-assistant
Installation
$ npx skills add https://github.com/nicepkg/ai-workflow --skill gsc-assistant
SKILL.md
GSC Assistant Skill
Purpose

This skill helps manage Google Search Console indexing status by maintaining two markdown tracking files:

indexed.md - All indexed pages in two tables:

"Indexed Public" - URLs confirmed in GSC export data
"Indexed With Lag" - URLs confirmed via URL Inspection (not yet in export)

to-index.md - Pages awaiting indexing:

Difference between sitemap and total indexed URLs
Prioritized by categories (configurable)
Tracks submission dates
When to Use This Skill
User asks about "indexing status" or "GSC indexing"
User wants to "compare sitemap with indexed pages"
User mentions "URL inspection" or "false positives"
User needs to "track submissions" or "indexing progress"
User asks to "move indexed pages" or "update indexing status"
User wants to "generate indexing report"
Key Concepts
GSC Data Lag

Google Search Console export data has approximately 2 weeks lag. Pages that show as indexed in URL Inspection may not appear in the export yet. These are tracked separately as "Indexed With Lag".

False Positives

When checking to-index pages via URL Inspection:

If indexed: Mark as "false positive - indexed" in Submitted column
Pre-processing moves these to indexed.md (Indexed With Lag table)
The "Detected" date is inferred from when the entry was added to to-index
Priority Categories

to-index.md organizes pages by priority:

Priority 1: High-value content series
Priority 2: Recent content (current/previous year)
Priority 3: Specific content collections
Lower priorities: Archive pages, pagination, etc.
File Schemas
indexed.md
# Indexed Pages

## Indexed Public (GSC Export)

*Last updated: YYYY-MM-DD*
*Source: gsc-export.csv*

| # | URL | Last Crawled |
|---|-----|--------------|
| 1 | https://example.com/page-1/ | 2025-12-01 |
| 2 | https://example.com/page-2/ | 2025-12-02 |

## Indexed With Lag (URL Inspection Confirmed)

*Pages confirmed indexed via URL Inspection but not yet in GSC export*

| # | URL | Detected | Confirmed |
|---|-----|----------|-----------|
| 1 | https://example.com/new-page/ | 12 Dec 2025 | 12 Dec 2025 |

to-index.md
# Pages To Index

*Generated: YYYY-MM-DD*
*Total: X pages*

## Priority 1: [Category Name]

| # | URL | Submitted |
|---|-----|-----------|
| 1 | https://example.com/important-page/ | 12 Dec |
| 2 | https://example.com/another-page/ | - |

## Priority 2: [Category Name]

| # | URL | Submitted |
|---|-----|-----------|
| 1 | https://example.com/recent-post/ | - |

Workflow
Initial Setup
Import GSC export CSV to create indexed.md (Indexed Public table)
Extract sitemap URLs
Calculate difference (sitemap - indexed = to-index)
Categorize to-index pages by priority
Generate to-index.md
Regular Updates
Pre-processing: Scan to-index.md for "false positive - indexed" entries
Move false positives to indexed.md (Indexed With Lag table)
Set "Detected" date from when entry was in to-index
Set "Confirmed" date to current date
Remove from to-index.md
Update counts and statistics
Manual Operations
Mark submissions: Update "Submitted" column with date
Check status: Use URL Inspection, mark result
Refresh data: Import new GSC export, recalculate
Configuration

Create working files in project directory:

project/
├── gsc-export.csv          # GSC indexed pages export
├── sitemap.xml             # Site sitemap (or use dist/sitemap.xml)
├── indexed.md              # Tracking file (generated)
└── to-index.md             # Tracking file (generated)

Commands
Generate Initial Files
"Generate indexing tracking files from GSC export and sitemap"

Pre-process False Positives
"Process false positives and update indexed list"

Update Submission Status
"Mark [URL] as submitted on [date]"

Refresh From New Export
"Update indexed list from new GSC export"

Generate Statistics
"Show indexing progress statistics"

Statistics Output
INDEXING STATUS SUMMARY
=======================

Indexed Public (GSC):     789 pages
Indexed With Lag:          12 pages
Total Indexed:            801 pages

Sitemap Total:          2,054 pages
To Index:               1,253 pages

Progress:                 39.0%

By Priority:
- Priority 1: 55 remaining (4 false positives moved)
- Priority 2: 7 remaining
- Priority 3: 290 remaining

Example Usage

User: "I just checked some URLs in GSC URL Inspection and marked them as false positive - indexed. Process those and update the tracking files."

Claude will:

Scan to-index.md for entries with "false positive - indexed"
Extract those URLs and their original detection dates
Add them to indexed.md Indexed With Lag table
Remove them from to-index.md
Update row numbers and counts
Report changes made
Weekly Installs
44
Repository
nicepkg/ai-workflow
GitHub Stars
176
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass