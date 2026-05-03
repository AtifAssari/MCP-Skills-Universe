---
title: survey-generation
url: https://skills.sh/lingzhi227/agent-research-skills/survey-generation
---

# survey-generation

skills/lingzhi227/agent-research-skills/survey-generation
survey-generation
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill survey-generation
SKILL.md
Survey Generation

Generate complete academic survey papers with structured outline, RAG-based writing, and citation validation.

Input
$0 — Survey topic or research area
Scripts
Literature search
python ~/.claude/skills/deep-research/scripts/search_semantic_scholar.py \
  --query "relevant search query" --max-results 50

References
Survey prompts (outline, writing, citation, coherence): ~/.claude/skills/survey-generation/references/survey-prompts.md
Workflow (from AutoSurvey)
Step 1: Collect Papers
Search Semantic Scholar / arXiv for papers on the topic
Collect 50-200 relevant papers with titles and abstracts
Filter by relevance and citation count
Step 2: Generate Outline (Multi-LLM Parallel)
Generate N rough outlines independently (parallel)
Merge outlines into a single comprehensive outline
Expand each section into subsections
Edit final outline to remove redundancies
Step 3: Write Subsections (RAG-Based)

For each subsection:

Retrieve relevant papers for the subsection topic
Generate content with inline citations [paper_title]
Enforce minimum word count per subsection
Only cite papers from the provided list
Step 4: Validate Citations

For each subsection:

Check that cited paper titles are correct
Verify citations support the claims made
Remove or correct unsupported citations
Use NLI (Natural Language Inference) for claim-source faithfulness
Step 5: Enhance Local Coherence

For each subsection:

Read previous and following subsections
Refine transitions and flow
Preserve core content and citations
Ensure smooth reading experience
Step 6: Convert Citations to BibTeX
Replace [paper_title] with \cite{key}
Generate BibTeX entries for all cited papers
Validate all citation keys exist in .bib file
Output Structure
survey/
├── main.tex          # Complete survey paper
├── references.bib    # All citations
├── outline.json      # Survey outline
└── sections/         # Individual section files

Rules
Only cite papers from the collected paper list — never hallucinate citations
Each subsection must meet minimum word count
No duplicate subsections across sections
Citation validation is mandatory before final output
Local coherence enhancement must preserve all citations
The survey should be comprehensive and logically organized
Related Skills
Upstream: deep-research, literature-search, literature-review
See also: related-work-writing
Weekly Installs
129
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn