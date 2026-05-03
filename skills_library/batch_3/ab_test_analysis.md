---
title: ab-test-analysis
url: https://skills.sh/phuryn/pm-skills/ab-test-analysis
---

# ab-test-analysis

skills/phuryn/pm-skills/ab-test-analysis
ab-test-analysis
Installation
$ npx skills add https://github.com/phuryn/pm-skills --skill ab-test-analysis
SKILL.md
A/B Test Analysis

Evaluate A/B test results with statistical rigor and translate findings into clear product decisions.

Context

You are analyzing A/B test results for $ARGUMENTS.

If the user provides data files (CSV, Excel, or analytics exports), read and analyze them directly. Generate Python scripts for statistical calculations when needed.

Instructions

Understand the experiment:

What was the hypothesis?
What was changed (the variant)?
What is the primary metric? Any guardrail metrics?
How long did the test run?
What is the traffic split?

Validate the test setup:

Sample size: Is the sample large enough for the expected effect size?
Use the formula: n = (Z²α/2 × 2 × p × (1-p)) / MDE²
Flag if the test is underpowered (<80% power)
Duration: Did the test run for at least 1-2 full business cycles?
Randomization: Any evidence of sample ratio mismatch (SRM)?
Novelty/primacy effects: Was there enough time to wash out initial behavior changes?

Calculate statistical significance:

Conversion rate for control and variant
Relative lift: (variant - control) / control × 100
p-value: Using a two-tailed z-test or chi-squared test
Confidence interval: 95% CI for the difference
Statistical significance: Is p < 0.05?
Practical significance: Is the lift meaningful for the business?

If the user provides raw data, generate and run a Python script to calculate these.

Check guardrail metrics:

Did any guardrail metrics (revenue, engagement, page load time) degrade?
A winning primary metric with degraded guardrails may not be a true win

Interpret results:

Outcome	Recommendation
Significant positive lift, no guardrail issues	Ship it — roll out to 100%
Significant positive lift, guardrail concerns	Investigate — understand trade-offs before shipping
Not significant, positive trend	Extend the test — need more data or larger effect
Not significant, flat	Stop the test — no meaningful difference detected
Significant negative lift	Don't ship — revert to control, analyze why

Provide the analysis summary:

## A/B Test Results: [Test Name]

**Hypothesis**: [What we expected]
**Duration**: [X days] | **Sample**: [N control / M variant]

| Metric | Control | Variant | Lift | p-value | Significant? |
|---|---|---|---|---|---|
| [Primary] | X% | Y% | +Z% | 0.0X | Yes/No |
| [Guardrail] | ... | ... | ... | ... | ... |

**Recommendation**: [Ship / Extend / Stop / Investigate]
**Reasoning**: [Why]
**Next steps**: [What to do]


Think step by step. Save as markdown. Generate Python scripts for calculations if raw data is provided.

Further Reading
A/B Testing 101 + Examples
Testing Product Ideas: The Ultimate Validation Experiments Library
Are You Tracking the Right Metrics?
Weekly Installs
566
Repository
phuryn/pm-skills
GitHub Stars
10.8K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass