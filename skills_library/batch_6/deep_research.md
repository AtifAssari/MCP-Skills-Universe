---
title: deep-research
url: https://skills.sh/199-biotechnologies/claude-deep-research-skill/deep-research
---

# deep-research

skills/199-biotechnologies/claude-deep-research-skill/deep-research
deep-research
Installation
$ npx skills add https://github.com/199-biotechnologies/claude-deep-research-skill --skill deep-research
Summary

Multi-source research synthesis with citation tracking, source verification, and structured reporting across 8-phase methodology.

Executes parallel searches and spawns concurrent agents to gather 10+ sources quickly, with credibility scoring and triangulation across sources
Generates comprehensive markdown reports with full bibliographies, executive summaries, and detailed findings—each claim immediately cited [N]
Produces three output formats automatically: markdown (source), McKinsey-style HTML (opened in browser), and professional PDF
Includes anti-hallucination protocols, citation verification scripts, and validation gates to catch fabricated sources and missing bibliography entries
Supports four research modes (quick/standard/deep/ultradeep) with auto-continuation for reports exceeding 18,000 words, enabling unlimited report length
SKILL.md
Deep Research
Core Purpose

Deliver citation-tracked research reports through a structured pipeline with evidence persistence, source identity management, claim-level verification, and progressive context management.

Autonomy Principle: Operate independently. Infer assumptions from context. Only stop for critical errors or incomprehensible queries. Surface high-materiality assumptions explicitly in the Introduction and Methodology rather than silently defaulting.

Decision Tree
Request Analysis
+-- Simple lookup? --> STOP: Use WebSearch
+-- Debugging? --> STOP: Use standard tools
+-- Complex analysis needed? --> CONTINUE

Mode Selection
+-- Initial exploration --> quick (3 phases, 2-5 min)
+-- Standard research --> standard (6 phases, 5-10 min) [DEFAULT]
+-- Critical decision --> deep (8 phases, 10-20 min)
+-- Comprehensive review --> ultradeep (8+ phases, 20-45 min)


Default assumptions: Technical query = technical audience. Comparison = balanced perspective. Trend = recent 1-2 years.

Workflow Overview
Phase	Name	Quick	Std	Deep	Ultra
1	SCOPE	Y	Y	Y	Y
2	PLAN	-	Y	Y	Y
3	RETRIEVE	Y	Y	Y	Y
4	TRIANGULATE	-	Y	Y	Y
4.5	OUTLINE REFINEMENT	-	Y	Y	Y
5	SYNTHESIZE	-	Y	Y	Y
6	CRITIQUE	-	-	Y	Y
7	REFINE	-	-	Y	Y
8	PACKAGE	Y	Y	Y	Y

Note: Phases 3-5 operate as an evidence loop per section (retrieve → evidence store → refine outline → draft → verify claims → delta-retrieve if needed), not as strict sequential gates.

Execution

On invocation, load relevant reference files:

Phase 1-7: Load methodology.md for detailed phase instructions
Phase 8 (Report): Load report-assembly.md for progressive generation
HTML/PDF output: Load html-generation.md
Quality checks: Load quality-gates.md
Long reports (>18K words): Load continuation.md

Templates:

Report structure: report_template.md
HTML styling: mckinsey_report_template.html

Scripts:

python scripts/validate_report.py --report [path]
python scripts/verify_citations.py --report [path]
python scripts/md_to_html.py [markdown_path]
Output Contract

Required sections:

Executive Summary (200-400 words)
Introduction (scope, methodology, assumptions)
Main Analysis (4-8 findings, 600-2,000 words each, cited)
Synthesis & Insights (patterns, implications)
Limitations & Caveats
Recommendations
Bibliography (COMPLETE - every citation, no placeholders)
Methodology Appendix

Output files (all to ~/Documents/[Topic]_Research_[YYYYMMDD]/):

Markdown (primary source of truth)
sources.jsonl — stable source registry with canonical IDs
evidence.jsonl — append-only evidence store with quotes and locators
claims.jsonl — atomic claim ledger with support status
run_manifest.json — query, mode, assumptions, provider config
HTML (McKinsey style, auto-opened)
PDF (professional print, auto-opened)

Quality standards:

10+ sources, 3+ per major claim (cluster-independent, not just count)
All factual claims cited immediately [N] with evidence backing in evidence.jsonl
Claim-support verification mandatory: no unsupported factual claims pass delivery
No placeholders, no fabricated citations
Prose-first (>=80%), bullets sparingly
When to Use / NOT Use

Use: Comprehensive analysis, technology comparisons, state-of-the-art reviews, multi-perspective investigation, market analysis.

Do NOT use: Simple lookups, debugging, 1-2 search answers, quick time-sensitive queries.

Weekly Installs
6.0K
Repository
199-biotechnolo…ch-skill
GitHub Stars
596
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn