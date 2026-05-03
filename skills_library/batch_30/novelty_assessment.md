---
title: novelty-assessment
url: https://skills.sh/lingzhi227/agent-research-skills/novelty-assessment
---

# novelty-assessment

skills/lingzhi227/agent-research-skills/novelty-assessment
novelty-assessment
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill novelty-assessment
SKILL.md
Novelty Assessment

Rigorously assess whether a research idea is novel through systematic literature search.

Input
$0 — Research idea description, title, or JSON file
Scripts
Automated novelty check
python ~/.claude/skills/idea-generation/scripts/novelty_check.py \
  --idea "Your research idea description" \
  --max-rounds 10 --output novelty_report.json

Literature search
python ~/.claude/skills/deep-research/scripts/search_semantic_scholar.py \
  --query "relevant search query" --max-results 10

References
Assessment prompts and criteria: ~/.claude/skills/novelty-assessment/references/assessment-prompts.md
Workflow
Step 1: Understand the Idea
Identify the core contribution
List the key technical components
Determine the research area and subfield
Step 2: Multi-Round Literature Search (up to 10 rounds)

For each round:

Generate a targeted search query
Search Semantic Scholar / arXiv / OpenAlex
Review top-10 results with abstracts
Assess overlap with the idea
Decide: need more searching, or ready to decide
Step 3: Make Decision
Novel: After sufficient searching, no paper significantly overlaps
Not Novel: Found a paper that significantly overlaps
Step 4: Position the Idea

If novel, identify:

Most similar existing papers (for Related Work)
How the idea differs from each
The specific gap this idea fills
Harsh Critic Persona
Be a harsh critic for novelty. Ensure there is a sufficient contribution
for a new conference or workshop paper. A trivial extension of existing
work is NOT novel. The idea must offer a meaningfully different approach,
formulation, or insight.

Output Format
{
  "decision": "novel" | "not_novel",
  "confidence": "high" | "medium" | "low",
  "justification": "After searching X rounds...",
  "most_similar_papers": [
    {"title": "...", "year": 2024, "overlap": "..."}
  ],
  "differentiation": "Our idea differs because..."
}

Rules
Minimum 3 search rounds before declaring novel
Try to recall exact paper names for targeted queries
A paper idea is NOT novel if it's a trivial extension
Consider both methodology novelty AND application novelty
Check for concurrent/recent arXiv submissions
Related Skills
Upstream: literature-search, deep-research
Downstream: idea-generation, research-planning
See also: related-work-writing
Weekly Installs
156
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