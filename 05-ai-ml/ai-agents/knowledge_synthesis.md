---
title: knowledge-synthesis
url: https://skills.sh/nickcrew/claude-ctx-plugin/knowledge-synthesis
---

# knowledge-synthesis

skills/nickcrew/claude-ctx-plugin/knowledge-synthesis
knowledge-synthesis
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill knowledge-synthesis
SKILL.md
Knowledge Synthesis

Extract, organize, and distribute insights across multi-agent systems. Turns raw interaction data, logs, and outcomes into actionable knowledge through pattern recognition, best practice codification, and structured retrieval.

When to Use This Skill
Synthesizing findings from multiple agents or research sessions
Building or updating a shared knowledge base
Identifying recurring success or failure patterns in workflows
Codifying best practices from empirical evidence
Structuring data for optimal retrieval (RAG optimization)
Cross-domain knowledge transfer between projects or teams
Quick Reference
Resource	Purpose	Load when
references/synthesis-workflow.md	Pattern recognition, RAG optimization, citation methods, knowledge graphs	Starting a synthesis cycle
Workflow
Phase 1: Discovery     → Mine interactions, logs, and outcomes for patterns
Phase 2: Codification  → Document best practices, build knowledge graph
Phase 3: Dissemination → Surface insights to relevant agents/teams
Phase 4: Feedback      → Capture adoption feedback, refine the knowledge base

Phase 1: Knowledge Discovery

Map the landscape before extracting insights:

Scope sources -- identify which interactions, logs, artifacts, and outcomes to mine
Classify signals -- tag each finding by value (high/medium/low), novelty, and confidence
Identify patterns -- look for recurring success patterns, failure modes, and decision trees
Document contradictions -- note where sources disagree or outcomes diverge
Discovery Checklist
 All relevant interaction logs identified
 Outcomes mapped to the workflows that produced them
 Recurring patterns tagged with confidence levels
 Contradictions and edge cases flagged
Phase 2: Codification

Transform raw patterns into structured, retrievable knowledge:

Write Knowledge Nuggets -- concise, actionable summaries with context and evidence
Build decision trees -- for common choice points, document the decision logic
Create playbooks -- step-by-step guides for patterns that recur frequently
Update indices -- structure data for retrieval (embeddings, tags, graph links)
Knowledge Nugget Template
## [Pattern Name]

**Context**: When does this pattern apply?
**Evidence**: What interactions/outcomes support it? [cite sources]
**Action**: What should agents do when they encounter this situation?
**Confidence**: High | Medium | Low
**Tags**: [domain], [workflow-type], [agent-role]

Phase 3: Dissemination

Surface the right insights to the right consumers:

Route knowledge nuggets to agents whose workflows they affect
Integrate high-confidence patterns into skill references and playbooks
Flag low-confidence patterns for further validation
Update retrieval indices so future queries find new knowledge
Phase 4: Feedback Loop

Close the loop to keep the knowledge base accurate:

Monitor adoption -- are agents applying the patterns?
Capture corrections -- when a pattern proves wrong, update or retract it
Track retrieval quality -- are the right nuggets surfacing for the right queries?
Refine confidence scores based on real-world outcomes
Grounded Responses and Citations

When answering questions based on the knowledge base, provide grounded responses:

Use numbered citation markers (e.g., [1], [2]) inline
Append a References section listing the source and relevant snippet
Cite the specific session, log, or artifact that provided evidence

Example:

The retry logic reduces failures by 40% in high-latency environments [1].

References: [1] "Session 2025-03-12" -- "After adding exponential backoff, error rate dropped from 12% to 7%"

Anti-Patterns
Do not synthesize from a single data point -- require multiple corroborating sources
Do not codify patterns without confidence ratings
Do not overwrite existing knowledge without citing the new evidence
Do not skip the feedback loop -- unvalidated knowledge degrades over time
Weekly Installs
35
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass