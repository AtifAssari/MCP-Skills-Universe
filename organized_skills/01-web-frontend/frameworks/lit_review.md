---
rating: ⭐⭐⭐⭐⭐
title: lit-review
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/lit-review
---

# lit-review

skills/pedrohcgs/claude-code-my-workflow/lit-review
lit-review
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill lit-review
SKILL.md
Literature Review

Conduct a structured literature search and synthesis on the given topic.

Input: $ARGUMENTS — a topic, paper title, research question, or phenomenon to investigate.

Steps

Parse the topic from $ARGUMENTS. If a specific paper is named, use it as the anchor.

Search for related work using available tools:

Check master_supporting_docs/supporting_papers/ for uploaded papers
Use WebSearch to find recent publications (if available)
Use WebFetch to access working paper repositories (if available)
Read any existing .bib file for papers already in the project

Organize findings into these categories:

Theoretical contributions — models, frameworks, mechanisms
Empirical findings — key results, effect sizes, data sources
Methodological innovations — new estimators, identification strategies, inference methods
Open debates — unresolved disagreements in the literature

Identify gaps and opportunities:

What questions remain unanswered?
What data or methods could address them?
Where do findings conflict?

Extract citations in BibTeX format for all papers discussed.

Save the report to quality_reports/lit_review_[sanitized_topic].md

Output Format
# Literature Review: [Topic]

**Date:** [YYYY-MM-DD]
**Query:** [Original query from user]

## Summary

[2-3 paragraph overview of the state of the literature]

## Key Papers

### [Author (Year)] — [Short Title]
- **Main contribution:** [1-2 sentences]
- **Method:** [Identification strategy / data]
- **Key finding:** [Result with effect size if available]
- **Relevance:** [Why it matters for our research]

[Repeat for 5-15 papers, ordered by relevance]

## Thematic Organization

### Theoretical Contributions
[Grouped discussion]

### Empirical Findings
[Grouped discussion with comparison across studies]

### Methodological Innovations
[Methods relevant to the topic]

## Gaps and Opportunities

1. [Gap 1 — what's missing and why it matters]
2. [Gap 2]
3. [Gap 3]

## Suggested Next Steps

- [Concrete actions: papers to read, data to obtain, methods to consider]

## BibTeX Entries

```bibtex
@article{...}


---

## Post-Flight Verification (mandatory, CoVe)

Before returning the draft literature review to the user, run the Post-Flight Verification protocol from [`.claude/rules/post-flight-verification.md`](../../rules/post-flight-verification.md). Literature reviews are **very high** hallucination risk because WebSearch can return plausible-sounding fabricated citations. CoVe catches this architecturally.

### Steps

1. **Extract claims** from the draft. Each cited paper, each paraphrased finding ("Smith 2019 shows X"), each negative-literature assertion ("no prior work studies Y") is a claim.
2. **Generate verification questions** per claim. Specific ones: "Does Smith (2019, *JEL*) Section 3 actually report the finding that X implies Y? Is the venue correct?"
3. **Spawn `claim-verifier`** via `Task` with `subagent_type=claim-verifier` and `context=fork`. Pass: the claims table, the verification questions, the source-material pointers (paper URLs, DOIs, `master_supporting_docs/` paths). **Do NOT pass the draft text itself** — the fresh-context independence is what makes CoVe work.
4. **Reconcile:** if the verifier reports PASS, attach a green Post-Flight block to the output. If PARTIAL, mark the unverifiable claims with uncertainty flags in the BibTeX block. If FAIL, **remove or rewrite the contradicted citations** using the verifier's evidence before returning.

### Skip conditions

- `--no-verify` flag — user opts out for speed.
- User hands you ≤3 papers they already have read and confirmed; CoVe is overhead for content they've personally verified.

### Output contract

Append a Post-Flight block to the report (collapsed by default). See rule doc for the format.

---

## Important

- **Be honest about uncertainty.** If you cannot verify a citation, say so.
- **Prioritize recent work** (last 5-10 years) unless seminal papers are older.
- **Note working papers vs published papers** — working papers may change.
- **Do NOT fabricate citations.** If you're unsure about a paper's details, flag it for the user to verify. Post-Flight Verification catches most fabrications automatically; this rule is the backup.

Weekly Installs
18
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