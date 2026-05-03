---
title: literature-review
url: https://skills.sh/lingzhi227/agent-research-skills/literature-review
---

# literature-review

skills/lingzhi227/agent-research-skills/literature-review
literature-review
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill literature-review
SKILL.md
Literature Review

Conduct deep literature reviews through multi-perspective dialogue and systematic search.

Input
$0 — Research topic or question
$1 — Optional: specific focus or angle
References
Multi-perspective dialogue prompts (STORM): ~/.claude/skills/literature-review/references/dialogue-prompts.md
Literature review workflow (AgentLaboratory): ~/.claude/skills/literature-review/references/review-workflow.md
Scripts (from literature-search skill)
# Search Semantic Scholar
python ~/.claude/skills/deep-research/scripts/search_semantic_scholar.py --query "topic" --max-results 20

# Search OpenAlex
python ~/.claude/skills/literature-search/scripts/search_openalex.py --query "topic" --max-results 20

# Search arXiv
python ~/.claude/skills/deep-research/scripts/search_arxiv.py --query "topic" --max-results 10

Workflow
Step 1: Generate Expert Personas (from STORM)

Given the topic, create 3-5 diverse expert personas:

Each represents a different perspective, role, or research angle
Example: "ML systems researcher focused on efficiency", "Theoretical statistician concerned with guarantees"
Use the persona generation prompts from references
Step 2: Multi-Perspective Dialogue

For each persona, simulate a multi-turn Q&A conversation:

Persona asks a question from their unique angle
Generate search queries from the question
Search literature using the search scripts
Synthesize an answer grounded in retrieved papers with inline citations
Record the dialogue turn with search results
Repeat for 3-5 turns per persona
End when persona says "Thank you so much for your help!"
Step 3: Synthesize Knowledge
Combine all persona conversations into a unified knowledge base
Remove redundancy across personas
Organize by theme/subtopic
Generate an outline based on the collected information
Step 4: Generate Literature Review
Write a structured review organized by the generated outline
Every claim must be supported by a citation
Include a summary table of key papers (method, contribution, limitations)
Output

A structured literature review with:

Outline — Hierarchical topic structure
Per-section summaries — Each grounded in retrieved papers
Paper database — Structured entries for all reviewed papers
Knowledge gaps — Identified areas needing further investigation
Rules
Every sentence in the review must be supported by gathered information
If information is not found, explicitly state the gap
Cite broadly — cover diverse approaches, not just the most popular
Include recent papers (last 2-3 years) alongside foundational work
Use inline citations: "Smith et al. [1] propose..."
Related Skills
Upstream: literature-search, deep-research
Downstream: related-work-writing, research-planning
See also: survey-generation
Weekly Installs
222
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn