---
rating: ⭐⭐⭐
title: parallel-literature-search
url: https://skills.sh/drshailesh88/integrated_content_os/parallel-literature-search
---

# parallel-literature-search

skills/drshailesh88/integrated_content_os/parallel-literature-search
parallel-literature-search
Installation
$ npx skills add https://github.com/drshailesh88/integrated_content_os --skill parallel-literature-search
SKILL.md
Parallel Literature Search

All sources at once. This skill searches PubMed, web, and your RAG knowledge base in parallel, then synthesizes the findings into a single coherent summary with citations.

WHAT IT DOES
Source	What It Searches	Output
PubMed	Academic literature, trials, reviews	PMIDs, abstracts, citations
Perplexity	Web, recent news, guidelines	Summaries with sources
RAG (AstraDB)	Your curated knowledge base	Guideline excerpts, textbook refs
THE DIFFERENCE
Approach	Sources	Time	Depth
Sequential search	One at a time	5+ min	Deeper but slow
Parallel search	All at once	30-60 sec	Fast overview
Manual search	You do it	20+ min	Variable
TRIGGERS

Use this skill when you say:

"Search for evidence on [topic]"
"What does the literature say about [topic]?"
"Find research on [topic]"
"Quick literature review on [topic]"
"Evidence for [clinical question]"
USAGE
In Claude Code (Recommended)
"Parallel search: SGLT2 inhibitors in HFpEF"

"Find all evidence on GLP-1 and cardiovascular outcomes"

"What does literature say about statin discontinuation?"

CLI Mode
# Basic search
python scripts/parallel_search.py --query "SGLT2 inhibitors heart failure"

# Specify sources
python scripts/parallel_search.py --query "GLP-1 cardiovascular" --sources pubmed,perplexity

# Save output
python scripts/parallel_search.py --query "CAC scoring" --output ~/research/

OUTPUT FORMAT
# Literature Search: SGLT2 Inhibitors in HFpEF

**Query:** SGLT2 inhibitors heart failure preserved ejection fraction
**Searched:** 2025-01-01 09:30:45
**Sources:** PubMed, Perplexity, RAG

---

## SYNTHESIS

SGLT2 inhibitors have demonstrated significant benefit in HFpEF based on
EMPEROR-Preserved and DELIVER trials. Key findings:

1. **EMPEROR-Preserved (PMID: 34449189)**: Empagliflozin reduced composite
   endpoint of CV death/HHF by 21% (HR 0.79, 95% CI 0.69-0.90)

2. **DELIVER (PMID: 36027570)**: Dapagliflozin showed 18% reduction in
   worsening HF/CV death (HR 0.82, 95% CI 0.73-0.92)

3. Current guidelines (ACC/AHA 2022) recommend SGLT2i as Class 2a for HFpEF.

---

## PUBMED RESULTS (5 most relevant)

| # | Title | PMID | Year | Type |
|---|-------|------|------|------|
| 1 | Empagliflozin in HFpEF | 34449189 | 2021 | RCT |
| 2 | Dapagliflozin in HFpEF | 36027570 | 2022 | RCT |
| 3 | Meta-analysis SGLT2i HF | 37654321 | 2023 | MA |
| 4 | Real-world SGLT2i outcomes | 38765432 | 2024 | Obs |
| 5 | SGLT2i mechanism review | 39876543 | 2024 | Rev |

---

## WEB RESULTS (Perplexity)

- **ACC 2024 Update**: New data on SGLT2i in cardiorenal syndrome
- **ESC Guidelines 2023**: Updated recommendations for SGLT2i
- **Clinical Practice**: Real-world prescribing patterns

---

## RAG RESULTS (Your Knowledge Base)

- **Braunwald Ch. 27**: Heart failure classification and treatment
- **ACC/AHA HF Guidelines**: Class recommendations for SGLT2i
- **ESC HF Guidelines**: European perspective on SGLT2i use

---

## EVIDENCE QUALITY

| Source | Strength | Notes |
|--------|----------|-------|
| EMPEROR-Preserved | High | Large RCT, well-conducted |
| DELIVER | High | Large RCT, confirmatory |
| Meta-analyses | High | Consistent findings |
| Real-world | Moderate | Observational limitations |

---

## KEY CITATIONS

1. Anker SD, et al. N Engl J Med. 2021;385:1451-1461. (PMID: 34449189)
2. Solomon SD, et al. N Engl J Med. 2022;387:1089-1098. (PMID: 36027570)
3. Vaduganathan M, et al. Lancet. 2022;400:757-767. (Meta-analysis)

---

## GAPS & CONSIDERATIONS

- Limited data in specific HFpEF phenotypes
- Long-term safety data still accumulating
- Indian-specific data limited (consider local studies)

ARCHITECTURE
User Query
     │
     ├──────────────────┬──────────────────┐
     │                  │                  │
     ▼                  ▼                  ▼
[PubMed Agent]   [Perplexity Agent]  [RAG Agent]
     │                  │                  │
     ▼                  ▼                  ▼
  PMIDs &           Web sources       Guideline
  Abstracts         & summaries       excerpts
     │                  │                  │
     └──────────────────┴──────────────────┘
                        │
                        ▼
               [Synthesis Agent]
                        │
                        ▼
              Unified Report with
              Citations & Evidence

INTEGRATION
Works With:
quick-topic-researcher - Quick overview
deep-researcher - Comprehensive review
youtube-script-master - Evidence for scripts
cardiology-editorial - Literature for editorials
Feeds Into:
Content creation pipeline
Video script research
Editorial writing
Newsletter content
DEPENDENCIES
# Core
anthropic>=0.18.0
python-dotenv>=1.0.0
rich>=13.0.0

# Already have these via your setup
# PubMed MCP - configured in .mcp.json
# Perplexity - via OpenRouter or MCP

API KEYS NEEDED
Key	Purpose	Status
ANTHROPIC_API_KEY	Synthesis	Already have
NCBI_API_KEY	PubMed (via MCP)	Already have
PERPLEXITY_API_KEY	Web search	Already have
HOW CLAUDE SHOULD USE THIS SKILL

When user asks for literature/evidence:

Step 1: Parse the Query

Extract:

Main topic
Specific aspects (population, intervention, outcome)
Time frame (if mentioned)
Step 2: Launch Parallel Searches
# PubMed (via MCP)
pubmed_search_articles(queryTerm="SGLT2 inhibitors heart failure", maxResults=10)

# Perplexity (via MCP or API)
perplexity_ask(messages=[{"role": "user", "content": "Latest evidence on SGLT2 inhibitors in heart failure 2024"}])

# RAG (if available)
# Query AstraDB for relevant guidelines

Step 3: Synthesize Results

Combine findings from all sources into:

Key takeaways
Evidence quality assessment
Complete citation list
Gaps and considerations
Step 4: Format Output

Structured report with:

Executive synthesis
Source-by-source findings
Full citations
Actionable insights
CLINICAL QUESTION OPTIMIZATION

The skill recognizes PICO format:

Component	Example	How It's Used
Patient	"elderly patients with HFpEF"	Filters PubMed
Intervention	"SGLT2 inhibitors"	Primary search term
Comparison	"vs placebo"	Narrows to RCTs
Outcome	"mortality"	Focuses results
SAMPLE QUERIES
# Basic clinical question
"SGLT2 inhibitors in heart failure"

# PICO format
"In elderly patients with HFpEF, do SGLT2 inhibitors reduce mortality compared to placebo?"

# Specific trial
"What are the key findings from EMPEROR-Preserved?"

# Guideline-focused
"Current ACC/AHA recommendations for SGLT2i in heart failure"

# Comparative
"SGLT2i vs GLP-1 for cardiovascular outcomes in diabetes"

NOTES
Speed: Parallel search takes 30-60 seconds vs 5+ minutes sequential
Depth: Good for overview, not exhaustive systematic review
Citations: Always includes PMIDs for verification
Updates: Perplexity provides most recent web data

This skill gives you evidence from multiple sources in under a minute - perfect for content preparation and quick clinical questions.

Weekly Installs
19
Repository
drshailesh88/in…ntent_os
GitHub Stars
3
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn