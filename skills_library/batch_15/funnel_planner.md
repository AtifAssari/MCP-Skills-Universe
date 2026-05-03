---
title: funnel-planner
url: https://skills.sh/hungv47/strategy-skills/funnel-planner
---

# funnel-planner

skills/hungv47/strategy-skills/funnel-planner
funnel-planner
Installation
$ npx skills add https://github.com/hungv47/strategy-skills --skill funnel-planner
SKILL.md
Funnel Planner — Orchestrator

Strategy — Step 3 of 4. Sets data-driven targets for each prioritized initiative.

Core Question: "Do the numbers actually work?"

Critical Gates — Read First
Every target MUST have a numeric baseline — zero "TBD" values. Targets without baselines are arbitrary guesses. If the user lacks data, use industry benchmarks with confidence flagging.
Every target MUST cite justification — no naked numbers. "Achieve 5% conversion" needs: baseline (current 3.2%), improvement factor (20% lift), reasoning (no optimization done yet, fixing known broken page).
70% test is mandatory — partial achievement must still be valuable. If hitting 70% of a target is meaningless, the target is wrong. Apply context rules for metric type (higher-is-better, lower-is-better, binary).
LTV:CAC ≥ 3:1 required for acquisition targets — or explicitly flagged. Setting aggressive acquisition targets when unit economics are unhealthy means you lose money faster.
Growth motion MUST be explicitly identified — PLG, SLG, or Hybrid. The funnel model selection depends on the growth motion. PLG → PLG Funnel or AARRR. SLG → SLG Funnel or TOFU-MOFU-BOFU. Hybrid → both with clear primary/supplementary designation.
Three-outcome validation required — every funnel must account for Business (revenue), Brand (awareness), and Community (engagement). Business must be Covered. Brand and Community may be N/A with justification. Gaps without justification are flagged.
Philosophy

Improvement factors and benchmarks here are evidence-backed starting points. Actual achievable improvement depends on baseline, team capability, and market context. Use the defaults as sanity checks, not ceilings or floors.

Inputs Required
Prioritized initiatives from .agents/solution-design.md (preferred)
OR: A business with metrics that need targets
Output
.agents/targets.md
Chain Position

Previous: solution-design | Next: experiment

Re-run triggers: When baselines shift >20% from target table values, after experiments conclude with new data, or quarterly.

Agent Manifest
#	Agent	Layer	Focus	Input	Output
1	model-selection-agent	L1 (parallel)	Funnel model selection, stage mapping	Business profile + initiatives	Selected model + stage definitions
2	baseline-collector-agent	L1 (parallel)	Baseline metrics collection	Initiatives + metrics data	Baselines, benchmarks, unit economics
3	target-setter-agent	L2 (sequential)	Numeric target setting with justification	Merged L1 output	Target table with improvement factors
4	sanity-check-agent	L2 (sequential)	Anti-pattern detection	Target table	Anti-pattern scan with fixes
5	stress-test-agent	L2 (sequential)	4-stress-test validation	Checked targets	Stress test results
6	critic-agent	L2 (sequential)	4-point quality gate	Complete analysis	PASS or FAIL with fix routing
Routing Logic
Route A: Full Analysis (Default)

For any target-setting exercise with multiple initiatives.

Layer 1 (parallel):  model-selection-agent + baseline-collector-agent
         ↓ merge
Layer 2 (sequential): target-setter-agent → sanity-check-agent → stress-test-agent → critic-agent

Route B: Quick Targets

When the funnel model is already established and baselines are known.

target-setter-agent → sanity-check-agent → critic-agent


Skip model-selection-agent, baseline-collector-agent, and stress-test-agent. Use when:

User already has a funnel model and baselines
Updating existing targets with new data
Single initiative needs a quick target
Dispatch Protocol
Pre-Dispatch: Context Gathering
Step 0: Product Context

Check for .agents/product-context.md. If missing: Strongly recommended: run icp-research (from hungv47/marketing-skills) first to create .agents/product-context.md — this skill works without it but produces significantly better analysis with it. If the user prefers not to, ask the user 8 product questions (what, who, problem, differentiator, proof points, pricing, objections, voice) and save to .agents/product-context.md.

If upstream artifacts' date fields are older than 30 days, recommend re-running upstream skills before proceeding — stale baselines produce unreliable targets. Tip: /navigate status (from meta-skills) gives a single-pass freshness report across all upstream artifacts.

Required Artifacts
Artifact	Source	If Missing
solution-design.md	solution-design	INTERVIEW. Ask what initiatives to set targets for.
Optional Artifacts
Artifact	Source	Benefit
product-context.md	icp-research (from hungv47/marketing-skills)	Business model context for benchmark selection
Growth Motion Identification

Before selecting a funnel model, determine the growth motion:

PLG — Product drives acquisition. Users find, try, and buy through self-serve. Indicators: free tier exists, low-touch onboarding, product virality.
SLG — Outbound and paid performance drive acquisition. Indicators: sales team, high ACV, demo-required, paid channels are primary.
Hybrid — Both motions coexist (e.g., self-serve for SMB + sales-assisted for enterprise). Designate which is primary for target-setting.
Initiative Review

Read .agents/solution-design.md if it exists — set a target for each "Proceed" initiative. If it doesn't exist, interview for:

What business type? (SaaS, e-commerce, B2B services, etc.)
What stage? (Pre-launch, early traction, growth, mature)
What is the growth motion? (PLG, SLG, or Hybrid — see above)
What metrics need targets?
What channels are active or planned? (Reference the 9-channel map: Search engines/GEO, Store/Listing platforms, Bounty/Info platforms, News, Forums/Communities, Social media, IRL, Mailbox, SMS)
Route Selection
Default → Route A (Full Analysis)
If user provides baselines + funnel model → Route B
Single-Agent Fallback

If the full orchestration is unnecessary (single metric, user has baseline and benchmark), you may run the target-setting inline without dispatching agents. Apply the same quality gate (4-point checklist) before delivering.

Layer 1 — Parallel: Model Selection + Baseline Collection

Dispatch model-selection-agent and baseline-collector-agent simultaneously.

model-selection-agent
Input: Business profile (type, stage, sales cycle, revenue model, growth motion), initiatives from solution-design.md
References: references/funnel-models.md (includes PLG Funnel, SLG Funnel, AARRR, AIDA, TOFU-MOFU-BOFU)
Expected output: Growth motion classification (PLG/SLG/Hybrid), selected funnel model, stage definitions, initiative-to-stage mapping, channel-to-stage mapping for active channels
baseline-collector-agent
Input: Initiatives with their target metrics, user-provided data
References: references/benchmarks.md, references/unit-economics.md
Expected output: Baselines with sources and confidence, benchmark context, unit economics snapshot
Layer 1 Merge

After both agents return:

Combine model selection (stages + mapping) with baselines (numbers + benchmarks)
Verify every initiative has both a funnel stage mapping AND a numeric baseline
If any initiative is missing a baseline, send feedback to baseline-collector-agent
Pass merged output to target-setter-agent
Layer 2 — Sequential: Set → Check → Stress → Critic
Step 1: target-setter-agent
Input: Merged L1 output (model + baselines)
References: references/benchmarks.md, references/unit-economics.md
Expected output: Target table with improvement factors and justifications, LTV:CAC check, pricing health signals
Step 2: sanity-check-agent
Input: Target-setter-agent output
References: references/anti-patterns.md
Expected output: Anti-pattern scan — 6 checks with pass/fail per target

If sanity-check-agent finds Blocking failures:

Re-dispatch target-setter-agent with the specific fixes
Re-run sanity-check-agent on the updated targets
Maximum 1 fix cycle before proceeding
Step 3: stress-test-agent
Input: Sanity-checked targets
References: references/stress-tests.md
Expected output: 4 stress tests per target with pass/fail and recommendations
Step 4: critic-agent
Input: Complete merged analysis
Expected output: PASS or FAIL against 4-point quality gate
Critic Gate

Maximum 2 rewrite cycles. If the critic returns FAIL:

Read the critic's failure report — it names the specific gate, the fix, and the agent to re-dispatch
Re-dispatch ONLY the named agent(s) with the critic's feedback
Re-merge and send back to critic-agent
If FAIL again after 2 cycles: deliver the artifact with a "Known Issues" section listing unresolved gate failures
Artifact Template

On re-run: rename existing artifact to targets.v[N].md and create new with incremented version.

---
skill: funnel-planner
version: 1
date: {{today}}
status: draft
---

# Targets

**Growth Motion:** [PLG / SLG / Hybrid]
**Funnel Model:** [PLG Funnel / SLG Funnel / AARRR / AIDA / TOFU-MOFU-BOFU]
**Primary Model:** [if Hybrid — which model is primary for target-setting]

## Funnel Stages

Stage definitions from the selected model, with initiative-to-stage mapping.

| Stage | Definition | Key Metric | Mapped Initiatives |
|-------|------------|------------|-------------------|
| [e.g. Visitor] | [How users enter this stage] | [e.g. Unique visitors] | [Which initiatives target this stage] |

## Target Table

| Initiative | Metric | Baseline | Benchmark (Good) | Target | Variance vs. Benchmark | Justification | Owner |
|-----------|--------|----------|-------------------|--------|----------------------|---------------|-------|
| [Name] | [Metric] | [Current] | [Industry ref] | [Goal] | [+X% above benchmark or within range] | [Why achievable — cite evidence] | [Person] |

If Variance > 50% above good-tier benchmark, flag: "This target requires significantly above-average performance. Justification: [why your situation is different]."

## Channel → Funnel Stage Map

Which channels from the 9-channel map drive which funnel stages. Include only channels active in your strategy — use `references/funnel-models.md` for typical stage assignments by growth motion. If a channel is used differently than the default tactic (e.g., paid Reddit ads vs. organic forum engagement), create separate rows.

| Channel | Primary Stage | Secondary Stage | Key Metric | Budget Type |
|---------|--------------|-----------------|------------|-------------|
| [e.g. Search engines] | [e.g. Impression → Click] | [e.g. Lead] | [e.g. CTR, CPL] | [Paid / Organic / Both] |

**9-Channel Reference:** Search engines/GEO, Store/Listing platforms, Bounty/Info platforms, News, Forums/Communities, Social media, IRL (OOH/Events/POS), Mailbox (email), SMS.

## Three-Outcome Validation

Both PLG and SLG motions feed three outcomes: Business, Brand, Community. This section checks coverage — gaps are flagged but not blocking.

| Outcome | Metric(s) | Current | Target | Status |
|---------|-----------|---------|--------|--------|
| **Business** | [Revenue, conversion, unit economics] | [value] | [value] | [Covered / Gap] |
| **Brand** | [Branded search volume, social mentions, NPS, share of voice] | [value] | [value] | [Covered / Gap / N/A] |
| **Community** | [Active members, engagement rate, UGC volume, forum activity] | [value] | [value] | [Covered / Gap / N/A] |

**Status definitions:**
- **Covered** — metrics exist with baselines and targets
- **Gap** — outcome is relevant but no metrics defined. Recommend adding before proceeding to experiment.
- **N/A** — outcome is legitimately out of scope for this business. Justify: e.g., "B2B enterprise with no user community — Community is N/A. Brand is tracked via branded search only."

Business must always be Covered. Brand and Community may be N/A with justification — this is not a failure.

## Validation

### Anti-Patterns: [None detected / List any found + fixes]
### 70% Test: [Pass/fail per target]
### LTV:CAC Check: [Ratio] — [Healthy / Flag]

## Baseline Handoff to Experiment

Every target in this table becomes a baseline for `experiment`. When running `experiment`, the baseline MUST match the number in this table — if it doesn't, update this table first. Stale baselines produce incorrect sample size calculations and misleading lift targets.

## Next Step

Run `experiment` to design minimum viable tests before full rollout. Pass this artifact as required input — experiment should read baselines from this table, not re-interview for them.

Worked Example

Initiatives from solution-design: Restore Paid Targeting (Proceed), Restore Social Proof (Proceed).

Layer 1: Parallel Dispatch

model-selection-agent: Selects AARRR (SaaS with retention-dependent economics). Maps Paid Targeting → Acquisition stage, Social Proof → Activation stage.

baseline-collector-agent: Collects baselines — paid conversion 1.2% (user data, High confidence), bounce rate 52% (user data, High confidence), weekly signups 200 (user data, High). Benchmarks: B2B SaaS paid conversion good = 3-5%, bounce rate good = 30-40%. LTV:CAC = 15:1 (healthy).

Layer 2: Sequential

target-setter-agent: Sets targets — paid conversion 3.0% (was 3.5% before change, 30% lift = conservative recovery), bounce 40% (old page was 35%, major fix scenario), overall signups 300 (combined effect).

sanity-check-agent: All pass. No vanity metrics, no sandbagging, owners assigned.

stress-test-agent: Revenue test PASS (both connect to signups → revenue). 70% test PASS (2.5% and 43% still meaningful recovery). Ownership test PASS. Measurement test PASS (weekly check via analytics).

critic-agent: PASS — all 4 gates satisfied.

Final Artifact
# Targets

**Funnel Model:** AARRR

## Target Table

| Initiative | Metric | Baseline | Benchmark | Target | Justification | Owner |
|-----------|--------|----------|-----------|--------|---------------|-------|
| Restore Paid Targeting | Paid visitor signup rate | 1.2% | 3-5% (B2B SaaS median) | 3.0% | Was 3.5% before targeting change; conservative recovery with lookalike | Sarah |
| Restore Social Proof | Homepage bounce rate | 52% | 30-40% (B2B SaaS) | 40% | Old homepage was 35%; restoring trust signals should recover most of gap | James |
| Overall | Weekly signups | 200 | — | 300 | Combined effect: paid fix (150 → 225 from paid) + bounce fix (all sources) | Sarah (owner) |

## Validation

### Anti-Patterns: None detected. All targets have baselines, single owners, revenue connection.
### 70% Test: Hitting 70% (2.5% paid rate, 43% bounce, 270 signups) still represents meaningful recovery from 200.
### LTV:CAC Check: Current CAC $120, LTV $1,800 → 15:1 ratio. Healthy even if CAC rises 50%.

## Next Step

Run `experiment` to design A/B test for paid targeting and before-after for social proof restoration.

Anti-Patterns

Targets without baselines — "Achieve 5% conversion" without knowing current conversion makes the target unverifiable. INSTEAD: Collect baseline first. Use benchmarks with low confidence if user data is unavailable. Zero "TBD" values.

Aspirational math — Target significantly above good-tier benchmark without written justification. INSTEAD: Flag any target >1.5x above good-tier benchmark. Require explicit reasoning for why this situation enables outperformance.

Vanity metrics — Targeting Instagram followers or page views when they don't connect to revenue. INSTEAD: For every metric, ask "If this 5x'd tomorrow, would revenue change?" If not, find the revenue-connected metric.

Sandbagging — Setting targets that will happen without effort. INSTEAD: Add 30-50% stretch above organic trajectory.

Orphan targets — Owner is "the team" or a department. INSTEAD: One named person per target.

Input traps — Measuring activities ("publish 4 posts") instead of outcomes ("organic signups from content"). INSTEAD: Measure the output the activity should produce.

Ignoring unit economics — Setting aggressive acquisition targets when LTV:CAC is unhealthy. INSTEAD: Check LTV:CAC first. If <3:1, fix economics before scaling acquisition.

References
Reference	Use For
funnel-models.md	Stage definitions, model selection
benchmarks.md	Industry benchmarks by stage
anti-patterns.md	Target-setting pitfalls
stress-tests.md	Target validation questions
unit-economics.md	LTV:CAC, payback formulas
Weekly Installs
11
Repository
hungv47/strategy-skills
GitHub Stars
1
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn