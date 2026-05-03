---
rating: ⭐⭐
title: daily-paper-generator
url: https://skills.sh/galaxy-dawn/claude-scholar/daily-paper-generator
---

# daily-paper-generator

skills/galaxy-dawn/claude-scholar/daily-paper-generator
daily-paper-generator
Installation
$ npx skills add https://github.com/galaxy-dawn/claude-scholar --skill daily-paper-generator
SKILL.md
Daily Paper Generator
Overview

Discover, screen, and summarize recent papers for any research topic.

Supported sources:

arXiv
bioRxiv
both (--source both)

Core workflow:

Define topic query and time window
Search papers from arXiv / bioRxiv
Select Top 10 candidates per field
Score and narrow to Top 3 per field
Choose Top 1 per field
Generate bilingual summaries
Save outputs to daily paper/
When to Use

Use this skill when:

The user asks for a daily/weekly paper digest on any topic
The user wants recent papers from arXiv and/or bioRxiv
The user needs structured bilingual notes for reading and tracking
Output Format

Each summary should contain:

Paper title
Authors and venue/source
Link(s) and date
Chinese review (~300 words)
English review (concise academic prose)
Metadata table
Appendix (optional resources)
Quick Reference
Task	Method
Search papers	Use scripts/arxiv_search.py with `--source arxiv
Topic selection	Use general-topic queries from references/keywords.md
Evaluate quality	Use references/quality-criteria.md
Write Chinese review	Use references/writing-style.md
Write English review	Follow scientific writing best practices
Workflow
Step 1: Define query

Choose a concrete topic query. Examples:

test-time adaptation for medical imaging
multimodal foundation model for healthcare
protein language model interpretability
Step 2: Search arXiv and/or bioRxiv

Use helper script:

python skills/daily-paper-generator/scripts/arxiv_search.py \
  --query "test-time adaptation for medical imaging" \
  --source both \
  --months 1 \
  --max-results 80 \
  --output /tmp/papers.json


Notes:

--source arxiv: arXiv only
--source biorxiv: bioRxiv only
--source both: merge both sources and sort by date
Step 3: Top 10 candidate selection (per field)

For each candidate paper:

Check topic relevance from title + abstract
Remove obviously off-topic papers
Keep Top 10 candidates for this field

Minimum rule:

Do not jump directly from raw search results to final paper.
Keep an explicit Top 10 list first.
Step 4: Top 3 quality shortlist (per field)

For the Top 10 pool:

Score each paper with references/quality-criteria.md
Rank by weighted score
Keep Top 3
Step 5: Final Top 1 selection (per field)

For the Top 3 shortlist:

Compare novelty + method completeness + experimental credibility
Check practical impact for the field
Select Top 1 as the final pick

Required output trace:

Top 10 candidate list
Top 3 scored shortlist (with weighted scores)
Final Top 1 and one-paragraph selection rationale
Step 6: Generate bilingual summaries

For each selected paper, generate:

中文评语：背景、挑战、贡献、方法、结果、局限
English Review: concise, factual, non-formulaic
Step 7: Save output

Recommended directory and naming:

daily paper/
  YYYY-MM-DD-HHMM-paper-1.md
  YYYY-MM-DD-HHMM-paper-2.md
  YYYY-MM-DD-HHMM-paper-3.md

Additional Resources
references/keywords.md: general-topic query templates
references/quality-criteria.md: scoring rubric
references/writing-style.md: review writing style
example/daily paper example.md: output example
scripts/arxiv_search.py: arXiv + bioRxiv search helper
Important Notes
Use explicit topic queries, avoid single-word vague queries.
Keep the time window explicit (--months N).
Distinguish source in metadata (arxiv vs biorxiv).
Use the fixed narrowing rule: Top 10 -> Top 3 -> Top 1 (per field).
If a paper lacks robust evaluation, mark confidence and limitations clearly.
Do not fabricate unavailable fields (institution/GitHub/code links).
Weekly Installs
87
Repository
galaxy-dawn/cla…-scholar
GitHub Stars
3.5K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn