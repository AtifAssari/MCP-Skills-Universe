---
title: idea-generation
url: https://skills.sh/lingzhi227/agent-research-skills/idea-generation
---

# idea-generation

skills/lingzhi227/agent-research-skills/idea-generation
idea-generation
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill idea-generation
SKILL.md
Idea Generation

Generate and refine novel research ideas with literature-backed novelty assessment.

Input
$0 — Research area, task description, or existing codebase context
$1 — Optional: additional context (e.g., "for NeurIPS", constraints)
Scripts
Novelty check against Semantic Scholar
python ~/.claude/skills/idea-generation/scripts/novelty_check.py \
  --idea "Adaptive attention head pruning via gradient-guided importance" \
  --max-rounds 5


Performs iterative literature search to assess if an idea is novel.

References
Ideation prompts (generation, reflection, novelty): ~/.claude/skills/idea-generation/references/ideation-prompts.md
Workflow
Step 1: Generate Ideas

Given a research area and optional code/paper context:

Generate 3-5 diverse research ideas
For each idea, provide: Name, Title, Experiment plan, and ratings
Use the ideation prompt templates from references
Step 2: Iterative Refinement (up to 5 rounds per idea)

For each idea:

Critically evaluate quality, novelty, and feasibility
Refine the idea while preserving its core spirit
Stop when converged ("I am done") or max rounds reached
Step 3: Novelty Assessment

For each promising idea:

Run novelty_check.py or manually search Semantic Scholar / arXiv
Use the novelty checking prompts from references
Multi-round search: generate queries, review results, decide
Binary decision: Novel / Not Novel with justification
Step 4: Rank and Select
Score each idea on three dimensions (1-10): Interestingness, Feasibility, Novelty
Be cautious and realistic on ratings
Select the top idea(s) for development
Output Format
{
  "Name": "adaptive_attention_pruning",
  "Title": "Adaptive Attention Head Pruning via Gradient-Guided Importance Scoring",
  "Experiment": "Detailed implementation plan...",
  "Interestingness": 8,
  "Feasibility": 7,
  "Novelty": 9,
  "novel": true,
  "most_similar_papers": ["paper1", "paper2"]
}

Rules
Ideas must be feasible with available resources (no requiring new datasets or massive compute)
Do not overfit ideas to a specific dataset or model — aim for wider significance
Be a harsh critic for novelty — ensure sufficient contribution for a conference paper
Each idea should stem from a simple, elegant question or hypothesis
Always check novelty before committing to an idea
Related Skills
Upstream: literature-search, deep-research
Downstream: research-planning, experiment-design
See also: novelty-assessment
Weekly Installs
169
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