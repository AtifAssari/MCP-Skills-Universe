---
rating: ⭐⭐⭐
title: paper-finder
url: https://skills.sh/bchao1/paper-finder/paper-finder
---

# paper-finder

skills/bchao1/paper-finder/paper-finder
paper-finder
Installation
$ npx skills add https://github.com/bchao1/paper-finder --skill paper-finder
SKILL.md
Paper Finder

Research paper discovery and organization agent. Find relevant ML/AI/CV/NLP papers, organize them into a persistent knowledge base, and connect them across topics.

Directory Structure

Each search/topic gets its own folder. The folder name should be a short, descriptive kebab-case name for the search topic (e.g., mixed-resolution-diffusion/, video-generation-efficiency/). The user may also specify a custom folder name. Create on first use:

<topic-name>/
  memory-bank.md        # Master list of all discovered papers
  mind-graph.md         # Topic-paper connection graph
  summaries/            # Per-paper .md files (via research-paper-analyst skill)
  references.bib        # Combined BibTeX for all papers
  pdfs/                 # Downloaded PDFs (only when user asks)
  discussions/          # Paper comparison logs


If the user references an existing folder (e.g., @mixed-resolution-diffusion/), operate within that folder. If starting a new search without a specified folder, derive a descriptive name from the search query.

Searching for Papers
Web search is mandatory

Use WebSearch and WebFetch for every search. Training knowledge alone misses recent papers (2024-2025+). If web tools are denied, retry once, then tell the user you need web access and explain what you'd search for.

Search strategy

Run 2-3 parallel searches per query:

Semantic Scholar API via WebFetch: https://api.semanticscholar.org/graph/v1/paper/search?query=<query>&limit=20&fields=title,authors,year,venue,abstract,externalIds,citationCount,url
WebSearch with queries like <topic> paper <venue> <year> — good for Google Scholar results
Venue-specific when relevant: <topic> CVPR 2025, <topic> site:openreview.net
Follow citations on Semantic Scholar for highly relevant papers

Relevant venues by field: CV (CVPR, ECCV, ICCV, WACV), ML (NeurIPS, ICML, ICLR, COLM, AAAI), NLP (ACL, EMNLP, NAACL), Graphics (SIGGRAPH, SIGGRAPH Asia, 3DV), Robotics (CoRL, RSS, ICRA), Medical (MICCAI), Preprints (arXiv cs.CV/CL/LG/AI).

Multi-angle search (mandatory)

A single concept can be described using very different vocabulary depending on the angle. After the initial direct-concept searches, you MUST run at least one additional search round covering these three angles. Skipping these is the #1 cause of missed papers.

Cross-domain synonyms: The same idea often has established names in adjacent fields. Before searching, brainstorm 2-3 alternative terms from related domains (graphics, neuroscience, signal processing, HCI, information theory, etc.). For example, "mixed-resolution spatial tokens" in ML maps to "foveated rendering" in graphics, "saliency-driven attention" in neuroscience, or "non-uniform sampling" in signal processing. Search using these alternative vocabularies.

Enabling mechanisms / building blocks: Search for the specific technical components needed to implement the concept — not just the concept itself. Every novel representation requires changes to attention, positional encodings, loss functions, normalization, etc. For example, mixed-resolution tokens require modified RoPE/positional embeddings, cross-resolution attention alignment, and boundary handling. Search for these mechanism-level terms (e.g., "positional encoding mixed resolution," "RoPE phase alignment multi-scale").

Motivating applications / problem framing: Papers solving the same technical problem may frame it as a different goal. Search from the perspective of why someone would build this (efficiency, speed, perceptual quality, hardware constraints). For example, "spatial acceleration diffusion" and "latent upsampling" lead to mixed-resolution tokens as a solution, but would never surface from searches for "mixed-resolution tokens" directly.

After initial results come in, also follow the citation graph: fetch the related-work section of 1-2 top-relevance papers and scan for references you haven't found yet.

Understand the concept precisely

Before searching, understand the exact technical distinction the user cares about. If they describe a specific mechanism (e.g., "tokens of different spatial sizes within a single image"), search for that literal property — don't broaden to superficially similar but technically different work (e.g., cascaded pipelines, super-resolution).

Filtering
Prioritize algorithmic contributions over architecture/engineering/systems papers
Prioritize recent work (2024-2025+) — skip well-known basics (DiT, VQGAN, etc.) unless directly relevant
Note citation counts when available
Tier results by relevance to the user's specific concept
Memory Bank (memory-bank.md)

Master record of all discovered papers. Append new entries, never overwrite. Read existing file before searching to avoid duplicates.

# Paper Memory Bank
Last updated: YYYY-MM-DD

### [short-id] Paper Title
- **Authors**: Author list
- **Venue**: Conference/Journal, Year
- **URL**: Link to paper
- **Citations**: N (if known)
- **Status**: discovered | summarized | analyzed
- **Topics**: topic1, topic2
- **Abstract**: 1-2 sentence description
- **Notes**: Relevance observations
---

Mind Graph (mind-graph.md)

Topic-centric hierarchy — NOT pairwise paper comparisons. Each topic has 1-3 umbrella/landmark papers plus other relevant work.

# Mind Graph
Last updated: YYYY-MM-DD

### Topic Name
- **Description**: One-line description
- **Related topics**: [other topic], [other topic]
- **Key papers**:
  - [short-id] Paper Title (Venue Year) — why it's key for this topic
- **Other relevant papers**:
  - [short-id] Paper Title — one-line note

BibTeX (references.bib)

Write a single combined references.bib file with all papers. Use @inproceedings for conferences, @article for journals, @misc for arXiv preprints. Citation key = short-id.

Paper Summaries and Comparisons
Summaries: Invoke research-paper-analyst skill. Save to summaries/<short-id>.md. Only when user explicitly asks — don't auto-summarize.
Comparisons: Read existing summaries first (create if missing via research-paper-analyst), save discussion to discussions/<descriptive-name>.md.
References to known papers: Search summaries and memory bank first. Only re-read the original paper if the user explicitly asks.
PDF Management

Do NOT download PDFs unless the user explicitly asks. When asked:

Read references.bib to extract the arXiv eprint ID or URL for each paper. This is the canonical source — do NOT read memory-bank.md or other files just to find download URLs.
Construct the PDF URL from the arXiv ID: https://arxiv.org/pdf/<eprint-id>
Download via curl/WebFetch and save to pdfs/<short-id>.pdf
Only fall back to memory-bank.md or web search if a paper has no entry in references.bib.
Interaction Flow
Search: Run parallel web searches, present ranked list (title, venue, year, citations, one-line description)
Record: Add papers to memory-bank.md, update mind-graph.md, write references.bib
Ask: Whether user wants deeper analysis of any specific papers
Weekly Installs
17
Repository
bchao1/paper-finder
GitHub Stars
207
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn