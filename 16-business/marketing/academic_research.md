---
title: academic-research
url: https://skills.sh/chrislemke/stoffy/academic-research
---

# academic-research

skills/chrislemke/stoffy/academic-research
academic-research
Installation
$ npx skills add https://github.com/chrislemke/stoffy --skill academic-research
SKILL.md
Academic Research Skill

Conduct comprehensive academic research mimicking Claude.ai's Research feature, specialized for philosophy, neuroscience, cognitive science, and theoretical CS.

Research Workflow
1. Scope the Query

Before searching, clarify:

Domain: Philosophy / Neuroscience / Cognitive Science / Theoretical CS
Depth: Quick (3-5 sources) | Standard (10-15) | Deep (20+)
Focus: Empirical findings / Theoretical frameworks / Historical development / Current debates

If unclear, ask one clarifying question before proceeding.

2. Search Strategy

Use web search with academic-focused queries. Search in waves:

Wave 1 - Core sources:

"[topic]" site:semanticscholar.org
"[topic]" site:arxiv.org
"[topic]" site:philpapers.org (for philosophy)
"[topic]" site:ncbi.nlm.nih.gov (for neuroscience)

Wave 2 - Expand with:

"[topic]" review paper OR survey
"[topic]" [key author name]
"[topic]" [specific journal from references/domains.md]

Wave 3 - Follow citations:

Search for highly-cited papers found in Wave 1-2
Look for "cited by" to find recent work building on seminal papers
3. Source Evaluation

For each source, extract and assess:

Relevance (0-10): How directly does it address the query?
Authority: Peer-reviewed? Citation count? Author credentials?
Recency: Prioritize last 5 years unless historical context needed
Type: Empirical study / Review / Theoretical / Commentary

Flag preprints (arXiv, bioRxiv) as non-peer-reviewed.

4. Triangulation

Cross-reference findings to identify:

Consensus: Claims supported by multiple independent sources
Debates: Conflicting findings or interpretations
Gaps: Underexplored questions
Key figures: Most-cited authors and seminal works
5. Synthesis Output

Structure the report as:

# Research Report: [Topic]

## Summary
[2-3 paragraph executive summary]

## Key Findings
1. [Finding with citation]
2. [Finding with citation]
...

## Theoretical Landscape
[Major positions, schools of thought, competing frameworks]

## Open Questions
[Active debates, unresolved issues, research gaps]

## Recommended Reading
- [Paper 1] - [1-sentence annotation]
- [Paper 2] - [1-sentence annotation]
...

## References
[Full citations, preferably with DOIs/URLs]

Domain-Specific Guidance

See references/domains.md for:

Key journals and venues per domain
Important authors and research groups
Domain-specific terminology
Relevant arXiv categories
Citation Format

Default: APA 7th edition. Include:

DOI when available (as URL: https://doi.org/...)
arXiv ID for preprints: arXiv:XXXX.XXXXX
Direct URL to paper when no DOI
Quality Standards
Never cite a paper without verifying it exists via search
Distinguish peer-reviewed from preprints
Note when findings are contested or preliminary
Include publication year for temporal context
Prefer primary sources over secondary summaries
Subagent Mode

When invoked programmatically, return structured data:

{
  "query": "original research question",
  "domain": "identified domain",
  "sources_found": 15,
  "key_findings": ["finding 1", "finding 2"],
  "consensus_level": "high|moderate|low|contested",
  "top_papers": [
    {"title": "...", "authors": "...", "year": 2023, "url": "..."}
  ],
  "research_gaps": ["gap 1", "gap 2"]
}

Weekly Installs
10
Repository
chrislemke/stoffy
GitHub Stars
1
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn