---
rating: ⭐⭐⭐
title: experiment
url: https://skills.sh/hungv47/strategy-skills/experiment
---

# experiment

skills/hungv47/strategy-skills/experiment
experiment
Installation
$ npx skills add https://github.com/hungv47/strategy-skills --skill experiment
SKILL.md
Experiment Design — Orchestrator

Strategy — Step 4 of 4. Designs minimum viable tests with clear success/iterate/kill rules.

Core Question: "What's the cheapest way to learn if this works?"

Critical Gates — Read First
Executable in ≤2 weeks. If the experiment takes longer than 2 weeks, it's not a minimum viable test. Simplify the design or switch test type.
Success threshold MUST be a specific number. "Significant improvement" or "we'll know it when we see it" are not thresholds. "≥2.5% signup rate" is a threshold. Define before launching.
Sample size MUST be checked. If insufficient for A/B, adjust: bigger swing, lower confidence, Before-After, or Pilot. Never rationalize "let's just go with what feels right."
Guardrail metrics are mandatory. A test can "succeed" on the primary metric while degrading support tickets, error rates, or refund rates. Define at least 2 guardrail metrics with specific thresholds.
Philosophy

Experimental rigor matters — but the level should match the stakes. Sample size tables assume 95% confidence / 80% power, appropriate for high-stakes decisions. For lower-stakes tests (social creative, email subjects), 90% confidence may suffice. Define acceptable risk upfront.

Inputs Required
An initiative with hypothesis and target metric (from .agents/solution-design.md + .agents/targets.md)
Baselines from .agents/targets.md (required for sample size calculation and lift targets)
OR: User describes what they want to test
Output
.agents/experiment-[name].md
Chain Position

Previous: funnel-planner | Next: implement winning variant, or re-diagnose with problem-analysis if inconclusive

Re-run triggers: When prior experiment results become stale (>60 days), when testing a new initiative from solution-design, or when baselines in targets.md are updated.

Agent Manifest
#	Agent	Layer	Focus	Input	Output
1	test-design-agent	L1 (parallel)	Test type selection, experiment structure	Initiative + baselines	Test design with hypothesis and variants
2	metrics-agent	L1 (parallel)	Decision rules, success/iterate/kill thresholds	Initiative + baselines + targets	Decision thresholds + guardrail definitions
3	sample-size-agent	L2 (sequential)	Sample size calculation, sufficiency check	Merged L1 output	Sample calculation + adjustments
4	guardrail-agent	L2 (sequential)	Breach protocols, rollback plan	Sample-size output + metrics	Breach scenario matrix + monitoring plan
5	critic-agent	L2 (sequential)	5-point quality gate	Complete analysis	PASS or FAIL with fix routing
Routing Logic
Route A: Full Experiment Design (Default)

For any initiative that needs a properly designed test.

Layer 1 (parallel):  test-design-agent + metrics-agent
         ↓ merge
Layer 2 (sequential): sample-size-agent → guardrail-agent → critic-agent

Route B: Quick Experiment

When the test type is obvious and the user just needs decision rules and sample validation.

test-design-agent → sample-size-agent → critic-agent


Skip metrics-agent (user provides thresholds) and guardrail-agent (low-stakes test). Use when:

Test type is already decided (e.g., "run an A/B test on this headline")
User provides their own success/kill thresholds
Low-stakes test where guardrail complexity isn't warranted (e.g., email subject line test)
Dispatch Protocol
Pre-Dispatch: Context Gathering
Step 0: Product Context

Check for .agents/product-context.md. If missing: Strongly recommended: run icp-research (from hungv47/marketing-skills) first to create .agents/product-context.md — this skill works without it but produces significantly better analysis with it. If the user prefers not to, ask the user 8 product questions (what, who, problem, differentiator, proof points, pricing, objections, voice) and save to .agents/product-context.md.

If upstream artifacts' date fields are older than 30 days, recommend re-running upstream skills before proceeding — stale baselines invalidate sample size calculations.

Required Artifacts
Artifact	Source	If Missing
solution-design.md	solution-design	INTERVIEW. Ask what to test.
targets.md	funnel-planner	INTERVIEW. Ask for baseline metrics. Baselines are required — without them, sample size and lift calculations are meaningless.
Optional Artifacts
Artifact	Source	Benefit
product-context.md	icp-research (from hungv47/marketing-skills)	Test design context
Initiative & Target Review

Read .agents/solution-design.md and .agents/targets.md if they exist. If not, interview for:

"What are you trying to test? What's your hypothesis?"
"What metric are you measuring? What's the current baseline?"
"What would success look like? What would make you stop?"

A hypothesis, a target metric, and a baseline number are the minimum required inputs — without them, success criteria become subjective.

Route Selection
Default → Route A (Full Experiment Design)
If user provides thresholds + test type AND it's low-stakes → Route B
Single-Agent Fallback

If the full orchestration is unnecessary (simple test, user has design and thresholds already), you may run the experiment design inline without dispatching agents. Apply the same quality gate (5-point checklist) before delivering.

Layer 1 — Parallel: Test Design + Metrics

Dispatch test-design-agent and metrics-agent simultaneously.

test-design-agent
Input: Initiative details, baselines from targets.md, traffic data
References: references/experiment-templates.md
Expected output: Test type selection (with reasoning against all 4 types), hypothesis, variant definition, duration, budget
metrics-agent
Input: Initiative details, baselines, target values from targets.md
References: references/common-mistakes.md
Expected output: Decision rules (success/iterate/kill with specific numbers), guardrail metrics with thresholds
Layer 1 Merge

After both agents return:

Combine test design (type, variants, duration) with metrics (thresholds, guardrails)
Verify hypothesis in test design matches the metrics baseline and target
If misalignment, reconcile before passing downstream
Pass merged output to sample-size-agent
Layer 2 — Sequential: Sample Size → Guardrails → Critic
Step 1: sample-size-agent
Input: Merged L1 output (test design + metrics)
References: references/sample-size-guide.md
Expected output: Sample size calculation, sufficiency verdict, adjustments if insufficient

If INSUFFICIENT:

sample-size-agent recommends adjustments (bigger swing, lower confidence, different test type)
If test type change is recommended, re-dispatch test-design-agent with the new type
Re-merge before proceeding
Step 2: guardrail-agent
Input: Sample-size-agent output + merged L1 (metrics with guardrail definitions)
References: references/common-mistakes.md
Expected output: Breach scenario matrix, guardrail-specific protocols, monitoring schedule, rollback plan
Step 3: critic-agent
Input: Complete merged analysis
Expected output: PASS or FAIL against 5-point quality gate
Critic Gate

Maximum 2 rewrite cycles. If the critic returns FAIL:

Read the critic's failure report — it names the specific gate, the fix, and the agent to re-dispatch
Re-dispatch ONLY the named agent(s) with the critic's feedback
Re-merge and send back to critic-agent
If FAIL again after 2 cycles: deliver the artifact with a "Known Issues" section listing unresolved gate failures
Loop-Back Protocol

When an experiment concludes, follow the appropriate path:

Kill Decision
Append learnings to the experiment file under ## Post-Mortem
Check: Is the root cause (.agents/problem-analysis.md) still valid?
Yes → Route to solution design: Run solution-design with constraint: "[Failed approach] did not work because [reason]. Generate alternatives that avoid this failure mode."
No → Route to problem analysis: Problem may have shifted. Re-diagnose using problem-analysis.
Update .agents/solution-design.md — move killed initiative to "Kill" status with reason.
Iterate Decision
Change exactly ONE variable from the original test
Maximum 2 iterations allowed before triggering Kill protocol
Document iteration rationale in experiment file under ## Iterations
Scale Decision
Document final results in experiment file under ## Results
Move to full execution — no further testing needed for this initiative
Map the scaled initiative to KPIs and track attribution
Artifact Template

On re-run: rename existing artifact to experiment-[name].v[N].md and create new with incremented version.

---
skill: experiment
version: 1
date: {{today}}
status: draft
---

# Experiment: [Name]

**Initiative:** [from prioritized list]

## Design

| Field | Value |
|-------|-------|
| Hypothesis | If [action], then [metric] changes from [baseline] to [target], because [reason] |
| Test Type | A/B / Before-After / Cohort / Pilot |
| Duration | [≤2 weeks] |
| Budget | [$X or $0] |
| Primary Metric | [metric name] |
| Baseline | [current value] |
| Guardrail Metrics | [metrics that must NOT degrade — e.g., support tickets, error rate, refund rate] |
| Guardrail Thresholds | [acceptable range for each guardrail — e.g., support tickets ≤ current +10%] |

## Decision Rules

| Outcome | Threshold | Action |
|---------|-----------|--------|
| Success | [metric] ≥ [X] | [Scale how] |
| Iterate | [metric] between [X-Y] | Change: [one specific variable]. Rerun: [duration]. |
| Kill | [metric] < [X] after [duration] | Archive. Next: [what to try instead] |

## Guardrail Breach Protocol

| Situation | Decision | Action |
|-----------|----------|--------|
| Primary succeeds, guardrails hold | Success | Scale as planned |
| Primary succeeds, guardrail breached slightly | Conditional Success | Reduce scope, rerun |
| Primary succeeds, guardrail breached severely | Iterate | Fix implementation, retest |
| Primary succeeds, breach inherent | Kill | Not worth guardrail cost |

## Sample Size Check

- Daily traffic: [N]
- Test duration: [days]
- Visitors per variant: [N x days / 2]
- Required for [X%] lift at baseline [Y%]: [from table]
- **Sufficient?** Yes / No → [if no, adjusted approach]

## Results

[Filled in after experiment concludes]
- **Outcome:** Success / Iterate / Kill
- **Primary metric result:** [actual value]
- **Duration:** [actual days run]
- **Key finding:** [one sentence — what did we learn?]

## Post-Mortem

[Filled in for Kill decisions]
- **What we tested:** [summary]
- **Why it failed:** [root cause of failure]
- **What we learned:** [insight for future initiatives]
- **Next action:** Run `solution-design` for alternatives / Run `problem-analysis` to re-diagnose

## Next Step

[When to check results. What to do with each outcome.]

Worked Example 1: A/B Test

Initiative: Restore + Refine Paid Targeting. Baseline: 1.2% paid signup rate. Target: 3.0%.

Layer 1: Parallel Dispatch

test-design-agent: Selects A/B test (can split paid budget 50/50, enough volume). Hypothesis: "If we use a 1% converters lookalike audience, then paid signup rate increases from 1.2% to ≥3%, because the lookalike matches our ICP better than current broad targeting." Duration: 10 days. Budget: $500 (redirected existing spend).

metrics-agent: Success ≥2.5%, Iterate 1.5-2.5%, Kill <1.5% after 10 days. Guardrails: CPA (must not exceed $80), landing page error rate (must stay <1%).

Layer 2: Sequential

sample-size-agent: Daily paid traffic ~300. 10 days = 3,000 total → 1,500 per variant. Need ~1,300 for 50% lift at 1.2% baseline. SUFFICIENT.

guardrail-agent: Breach matrix defined. CPA slight breach = ≤$95, severe = >$95. Early termination if CPA >$120 for 3 consecutive days. Rollback: revert to original targeting in Meta.

critic-agent: PASS — all 5 gates satisfied.

Worked Example 2: Before-After

Initiative: Restore Homepage Social Proof. Baseline: 52% bounce. Target: ≤42%.

Layer 1: Parallel

test-design-agent: Before-After (change affects all visitors, can't split). Duration: 7 days. Budget: $0.

metrics-agent: Success ≤42%, Iterate 42-48%, Kill >48% after 7 days. Guardrails: signup rate (must not drop >5%), page load time (must stay <3s).

Layer 2: Sequential

sample-size-agent: 800 daily visitors x 7 = 5,600. Ample for 10-point bounce rate change. SUFFICIENT.

guardrail-agent: Breach protocols. Signup drop >5% = pause and investigate. Load time >3s = optimize assets before continuing.

critic-agent: PASS.

Anti-Patterns

Testing the wrong level — Most teams test CTA button colors when they should test entirely different angles. INSTEAD: Start at the top of the creative testing hierarchy: Concept/angle → Hook/headline → Visual style → Body copy → CTA.

Testing multiple variables — Changing the hook, CTA, and format simultaneously makes results uninterpretable. INSTEAD: Change exactly ONE element per variant. The learning is more valuable than the lift.

Insufficient sample rationalization — "We don't have enough traffic for statistical significance, so let's just go with what feels right." INSTEAD: Adjust the test — aim for bigger change (50%+ lift), use Before-After, or run a Pilot. Don't abandon rigor.

Novelty effect as success — New things get clicks initially. A variant that "wins" in 3 days may lose after 2 weeks. INSTEAD: Run tests long enough for novelty to normalize (minimum 7 days).

Metrics without baselines — "Let's test if this improves conversions" without knowing the current rate. INSTEAD: Every experiment requires a numeric baseline. Without one, you can't calculate lift, sample size, or significance.

Testing without guardrails — A test can "succeed" on the primary metric while degrading other metrics. INSTEAD: Define at least 2 guardrail metrics with specific thresholds before launching.

Survivorship bias in iteration — Iterating only on winners while ignoring what failures teach. INSTEAD: Kill decisions feed learnings back to solution-design. The failure mechanism often reveals a better approach.

References
references/experiment-templates.md — Templates for landing page, email, ad creative, feature flag tests
references/sample-size-guide.md — Full sample size tables and common mistakes
references/common-mistakes.md — Experiment mistakes by phase (pre-launch, during, post-test) with detection signals and fixes
Weekly Installs
9
Repository
hungv47/strategy-skills
GitHub Stars
1
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass