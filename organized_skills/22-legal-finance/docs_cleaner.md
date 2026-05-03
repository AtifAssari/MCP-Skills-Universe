---
rating: ⭐⭐
title: docs-cleaner
url: https://skills.sh/daymade/claude-code-skills/docs-cleaner
---

# docs-cleaner

skills/daymade/claude-code-skills/docs-cleaner
docs-cleaner
Installation
$ npx skills add https://github.com/daymade/claude-code-skills --skill docs-cleaner
SKILL.md
Documentation Cleaner

Consolidate redundant documentation while preserving 100% of valuable content.

Core Principle

Critical evaluation before deletion. Never blindly delete. Analyze each section's unique value before proposing removal. The goal is reduction without information loss.

Workflow
Phase 1: Discovery
Identify all documentation files covering the topic
Count total lines across files
Map content overlap between documents
Phase 2: Value Analysis

For each document, create a section-by-section analysis table:

Section	Lines	Value	Reason
API Reference	25	Keep	Unique endpoint documentation
Setup Steps	40	Condense	Verbose but essential
Test Results	30	Delete	One-time record, not reference

Value categories:

Keep: Unique, essential, frequently referenced
Condense: Valuable but verbose
Delete: Duplicate, one-time, self-evident, outdated

See references/value_analysis_template.md for detailed criteria.

Phase 3: Consolidation Plan

Propose target structure:

Before: 726 lines (3 files, high redundancy)
After:  ~100 lines (1 file + reference in CLAUDE.md)
Reduction: 86%
Value preserved: 100%

Phase 4: Execution
Create consolidated document with all valuable content
Delete redundant source files
Update references (CLAUDE.md, README, imports)
Verify no broken links
Value Preservation Checklist

Before finalizing, confirm preservation of:

 Essential procedures (setup, configuration)
 Key constraints and gotchas
 Troubleshooting guides
 Technical debt / roadmap items
 External links and references
 Debug tips and code snippets
Anti-Patterns
Pattern	Problem	Solution
Blind deletion	Loses valuable information	Section-by-section analysis first
Keeping everything	No reduction achieved	Apply value criteria strictly
Multiple sources of truth	Future divergence	Single authoritative location
Orphaned references	Broken links	Update all references after consolidation
Output Artifacts

A successful cleanup produces:

Consolidated document - Single source of truth
Value analysis - Section-by-section justification
Before/after metrics - Lines reduced, value preserved
Updated references - CLAUDE.md or README with pointer to new location
Weekly Installs
287
Repository
daymade/claude-…e-skills
GitHub Stars
968
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass