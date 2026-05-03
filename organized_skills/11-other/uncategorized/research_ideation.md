---
rating: ⭐⭐⭐
title: research-ideation
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/research-ideation
---

# research-ideation

skills/pedrohcgs/claude-code-my-workflow/research-ideation
research-ideation
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill research-ideation
SKILL.md
Research Ideation

Generate structured research questions, testable hypotheses, and empirical strategies from a topic, phenomenon, or dataset.

Input: $ARGUMENTS — a topic (e.g., "minimum wage effects on employment"), a phenomenon (e.g., "why do firms cluster geographically?"), or a dataset description (e.g., "panel of US counties with pollution and health outcomes, 2000-2020").

Steps

Understand the input. Read $ARGUMENTS and any referenced files. Check master_supporting_docs/ for related papers. Check .claude/rules/ for domain conventions.

Generate 3-5 research questions ordered from descriptive to causal:

Descriptive: What are the patterns? (e.g., "How has X evolved over time?")
Correlational: What factors are associated? (e.g., "Is X correlated with Y after controlling for Z?")
Causal: What is the effect? (e.g., "What is the causal effect of X on Y?")
Mechanism: Why does the effect exist? (e.g., "Through what channel does X affect Y?")
Policy: What are the implications? (e.g., "Would policy X improve outcome Y?")

Tag each RQ with a likely paper type (drawn from methods-referee.md):

reduced-form (DiD, IV, RD, event study, synthetic control)
structural (estimation of a fully-specified model)
theory+empirics (formal model + empirical test of its predictions)
descriptive (measurement, data construction, pattern documentation)
formal-theory (pure theory, no empirical test in this paper)
survey-experiment (vignette, conjoint, list-experiment)
unsure (when multiple types are plausible — the user can pick later via /interview-me)

Use .claude/references/discipline-cards.md to bias the distribution by field (econ vs poli-sci default frequencies differ — e.g., poli-sci skews more toward survey-experiment and formal-theory than econ does).

For each research question, develop:

Hypothesis: A testable prediction with expected sign/magnitude
Identification strategy: How to establish causality (DiD, IV, RDD, synthetic control, etc.)
Data requirements: What data would be needed? Is it available?
Key assumptions: What must hold for the strategy to be valid?
Potential pitfalls: Common threats to identification
Related literature: 2-3 papers using similar approaches

Rank the questions by feasibility and contribution.

Save the output to quality_reports/research_ideation_[sanitized_topic].md

Output Format
# Research Ideation: [Topic]

**Date:** [YYYY-MM-DD]
**Input:** [Original input]

## Overview

[1-2 paragraphs situating the topic and why it matters]

## Research Questions

### RQ1: [Question] (Feasibility: High/Medium/Low)

**Type:** Descriptive / Correlational / Causal / Mechanism / Policy
**Paper type:** reduced-form / structural / theory+empirics / descriptive / formal-theory / survey-experiment / unsure

**Hypothesis:** [Testable prediction]

**Identification Strategy:**
- **Method:** [e.g., Difference-in-Differences]
- **Treatment:** [What varies and when]
- **Control group:** [Comparison units]
- **Key assumption:** [e.g., Parallel trends]

**Data Requirements:**
- [Dataset 1 — what it provides]
- [Dataset 2 — what it provides]

**Potential Pitfalls:**
1. [Threat 1 and possible mitigation]
2. [Threat 2 and possible mitigation]

**Related Work:** [Author (Year)], [Author (Year)]

---

[Repeat for RQ2-RQ5]

## Ranking

| RQ | Feasibility | Contribution | Priority |
|----|-------------|-------------|----------|
| 1  | High        | Medium      | ...      |
| 2  | Medium      | High        | ...      |

## Suggested Next Steps

1. [Most promising direction and immediate action]
2. [Data to obtain]
3. [Literature to review deeper]

Post-Flight Verification (mandatory, CoVe)

Before returning the ideation report, run the Post-Flight Verification protocol from .claude/rules/post-flight-verification.md. Research ideation is hallucination-prone in three specific ways:

Negative-literature claims — "no prior work studies X" is frequently wrong.
Dataset structure claims — "The CPS contains field educ_attain" can be confidently wrong about variable names, coverage years, or restricted-access status.
Estimator feasibility claims — "this works with panel fixed effects" can misstate an identification assumption.
Steps
Extract claims from the draft ideation report: each negative-literature claim, each named dataset with attributed fields, each claimed identification strategy + required data structure.
Generate verification questions per claim. Example: "Has Card & Krueger, Autor, or anyone in the last 10 years studied X? Search Google Scholar + NBER working papers." / "Does IPUMS-CPS include the educ_attain variable 1990–2024?"
Spawn claim-verifier via Task with subagent_type=claim-verifier and context=fork. Hand it claims + questions + source pointers (WebSearch allowed, NBER/SSRN URLs preferred, dataset codebooks preferred). Do NOT include the draft.
Reconcile: PASS → attach green block; PARTIAL → mark uncertain RQs with flags; FAIL → rewrite the affected RQ/hypothesis/strategy.
Skip conditions
--no-verify flag
User explicitly says "I'll verify the literature myself"
Principles
Be creative but grounded. Push beyond obvious questions, but every suggestion must be empirically feasible.
Think like a referee. For each causal question, immediately identify the identification challenge.
Consider data availability. A brilliant question with no available data is not actionable.
Suggest specific datasets where possible (FRED, Census, PSID, administrative data, etc.).
Weekly Installs
16
Repository
pedrohcgs/claud…workflow
GitHub Stars
1.0K
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn