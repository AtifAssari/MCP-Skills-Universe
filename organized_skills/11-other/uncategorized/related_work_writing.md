---
rating: ⭐⭐
title: related-work-writing
url: https://skills.sh/lingzhi227/agent-research-skills/related-work-writing
---

# related-work-writing

skills/lingzhi227/agent-research-skills/related-work-writing
related-work-writing
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill related-work-writing
SKILL.md
Related Work Writing

Generate publication-quality Related Work sections with proper citations and thematic organization.

Input
$0 — Current paper draft or method description
$1 — Collected literature (BibTeX entries, paper summaries, or literature review notes)
References
Related work writing prompts and strategies: ~/.claude/skills/related-work-writing/references/related-work-prompts.md
Workflow
Step 1: Analyze the Paper's Contributions
Read the current paper draft (especially Methods and Introduction)
Identify the key contributions and novelty claims
List the technical components that need literature context
Step 2: Organize Literature by Theme

Group related papers into thematic clusters:

Each cluster should represent a research direction or technique
Common themes: problem formulation, methodology family, application domain, evaluation approach
Order themes from most to least relevant to your work
Step 3: Write Each Theme Paragraph

For each thematic group:

Topic sentence — Introduce the research direction
Describe key works — Summarize 2-5 representative papers
Compare and contrast — How does each approach differ from yours?
Transition — Connect to the next theme or to your contribution
Step 4: Refine
Ensure every cited paper has a clear reason for inclusion
Check that your work's novelty is clear from the comparisons
Verify all \cite{} keys exist in the .bib file
Aim for 1-2 pages (single column) or 0.5-1 page (double column)
Rules
Compare and contrast, don't just describe — "Unlike [X] which assumes..., our method..."
Organize by theme, not chronologically — Group by research direction
Cite broadly — Not just the most popular papers; include recent and diverse work
Be fair — Acknowledge strengths of prior work before stating limitations
Explain inapplicability — If a method could apply to your setting, explain why you don't compare experimentally, or add it to experiments
Use present tense for established facts — "Smith et al. propose..." or "This approach uses..."
End with positioning — The final paragraph should clearly position your work relative to all discussed prior work
Related Skills
Upstream: literature-search, literature-review, citation-management
Downstream: paper-writing-section
See also: survey-generation
Weekly Installs
136
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass