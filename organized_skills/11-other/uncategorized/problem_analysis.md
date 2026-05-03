---
rating: ⭐⭐⭐⭐⭐
title: problem-analysis
url: https://skills.sh/hungv47/strategy-skills/problem-analysis
---

# problem-analysis

skills/hungv47/strategy-skills/problem-analysis
problem-analysis
Installation
$ npx skills add https://github.com/hungv47/strategy-skills --skill problem-analysis
SKILL.md
Problem Analysis — Orchestrator

Strategy — Step 1 of 4. Defines the problem, forms testable hypotheses, and identifies root causes.

Core Question: "What's actually causing this, and what does the evidence prove?"

Critical Gates — Read First
Problem statement MUST be: "[Metric] is [current] instead of [target]." No vague problems. If the user says "things aren't going well," interview for the specific metric, current value, and target value before dispatching any agent.
Do NOT skip external factors — 30%+ of problems have external causes. The external-check-agent runs in Layer 1 alongside the tree builder. Skipping it leads to treating a symptom when the cause is environmental.
If/Then/Because format required — hypotheses without "because" are unfalsifiable. The "because" clause explains the mechanism. Without it, a rejected hypothesis teaches nothing.
Do NOT confirm hypotheses without evidence — "seems likely" is not Confirmed. Every verdict must cite a specific data point that matches or contradicts the "then" clause. Inconclusive is a valid verdict.
Inputs Required
A problem (metric decline, performance gap, strategic question)
Output
.agents/problem-analysis.md
Chain Position

Previous: none | Next: solution-design

Skill Deference
Have a METRIC that's underperforming (X is at Y, should be Z)? Use this skill.
Have a FEATURE IDEA to spec out? Use plan-interviewer (from product-skills) instead.

Re-run triggers: When the metric shifts significantly, when new data surfaces that could change verdicts, or when a solution-design initiative is killed.

Agent Manifest
#	Agent	Layer	Focus	Input	Output
1	tree-builder-agent	L1 (parallel)	MECE logic tree construction	Problem statement	Tree + MECE check
2	external-check-agent	L1 (parallel)	External cause scanning via WebSearch	Problem statement + context	External factor assessment
3	hypothesis-agent	L2 (sequential)	If/Then/Because hypothesis formation	Merged L1 output (tree + external factors)	Ranked hypotheses
4	data-mapper-agent	L2 (sequential)	Data requirement mapping	Ranked hypotheses	Data map with sources + owners
5	verdict-agent	L2 (sequential)	Evidence evaluation + root cause statement	Data map + gathered evidence	Verdicts + root cause statement
6	critic-agent	L2 (sequential)	10-point quality gate	Complete analysis	PASS or FAIL with fix routing
Routing Logic
Route A: Quick Diagnosis

When the problem is straightforward, data is readily available, and external factors are unlikely.

tree-builder-agent → hypothesis-agent → verdict-agent → critic-agent


Skip external-check-agent and data-mapper-agent. Use when:

The user already provides data alongside the problem
The problem is clearly internal (e.g., "we broke the deploy")
Time is critical and the user confirms skipping external scan
Route B: Full Analysis (Default)

For any non-trivial diagnosis. This is the default route.

Layer 1 (parallel):  tree-builder-agent + external-check-agent
         ↓ merge
Layer 2 (sequential): hypothesis-agent → data-mapper-agent → [DATA PAUSE] → verdict-agent → critic-agent

Dispatch Protocol
Pre-Dispatch: Context Gathering
Step 0: Product Context

Check for .agents/product-context.md. If missing: Strongly recommended: run icp-research (from hungv47/marketing-skills) first to create .agents/product-context.md — this skill works without it but produces significantly better analysis with it. If the user prefers not to, interview for 8 product dimensions (what, who, problem, differentiator, proof points, pricing, objections, voice) and save to .agents/product-context.md.

Step 1: Problem Interview

If the user describes a vague problem ("things aren't going well", "growth is slow"):

Ask for the specific metric and its current value
Ask for the target value and who set it
If user doesn't know the baseline, use WebSearch: "[industry] [metric] benchmark [year]" or "[business type] average [metric]"
Ask when it changed and whether there was an inflection point
Ask how big the gap is in absolute and relative terms

Metric name + current number + target number are necessary before dispatching any agent. Without all three, the logic tree has no anchor and branches become speculation.

Construct the problem statement:

[Metric] is [current number] instead of [target number]

Route Selection
If user provides data inline AND problem is clearly internal → Route A
Otherwise → Route B (default)
Single-Agent Fallback

If the full orchestration is unnecessary (trivial problem, user already has the tree and hypotheses), you may run the analysis inline without dispatching agents. Apply the same quality gate (10-point checklist) before delivering.

Layer 1 — Parallel: Tree Building + External Scan

Dispatch tree-builder-agent and external-check-agent simultaneously.

tree-builder-agent
Input: Problem statement, gap size, timeline, inflection point
References: references/watanabe-framework.md, references/logic-tree-examples.md
Expected output: Logic tree (Math/Issue/Yes-No), MECE check, branch summary
external-check-agent
Input: Problem statement, timeline, industry, product type, known competitors
References: .agents/product-context.md (if available)
Expected output: 6-factor assessment (competitor, market/seasonal, platform/algorithm, regulatory, technology, macro-economic), each with WebSearch evidence
Layer 1 Merge

After both agents return:

If external-check-agent found Confirmed or Possible external factors, add an "External Factors" branch to the tree
If all external factors were Ruled Out, note this in the analysis and proceed with the internal tree as-is
Pass the merged tree + external factor assessment to hypothesis-agent
Layer 2 — Sequential: Hypothesis → Data Map → Verdict → Critic
Step 1: hypothesis-agent
Input: Merged L1 output (tree + external factors)
References: references/hypothesis-guide.md, references/logic-tree-examples.md
Expected output: If/Then/Because hypotheses for every leaf, ranked by testability (speed x impact)
Step 2: data-mapper-agent
Input: Ranked hypotheses from hypothesis-agent
References: references/logic-tree-examples.md
Expected output: Data requirement table — deciding data point, confirming evidence, rejecting evidence, source (tool → report → metric), owner, availability
Step 3: Data Gathering Pause

This is an interactive checkpoint. Do NOT skip it.

Present the data requirements to the user:

"Share what you found for each hypothesis — data, screenshots, reports, CSVs, or describe what you saw."

If user provides data files, read and analyze them directly — do not ask the user to summarize data you can read yourself.

If user hasn't gathered data yet:

Use WebSearch for publicly available evidence: "[competitor] launch [date range]", "[industry] [metric] trend [year]", "[tool name] outage [date]"
Point them to the specific sources listed in the data map
Offer to search for any data that might be publicly available

Do not proceed to verdict-agent without evidence. Verdicts without data are speculation.

Step 4: verdict-agent
Input: Data map + gathered evidence from the user or WebSearch
Expected output: Verdict per hypothesis (Confirmed/Rejected/Inconclusive), root cause statement with gap percentages, next step routing
Step 5: critic-agent
Input: Complete merged analysis (tree + external factors + hypotheses + data map + verdicts)
Expected output: PASS or FAIL against 10-point quality gate
Critic Gate

Maximum 2 rewrite cycles. If the critic returns FAIL:

Read the critic's failure report — it names the specific gate, the fix, and the agent to re-dispatch
Re-dispatch ONLY the named agent(s) with the critic's feedback
Re-merge and send back to critic-agent
If FAIL again after 2 cycles: deliver the artifact with a "Known Issues" section listing unresolved gate failures
Inconclusive Handling

After the verdict-agent runs, check for Inconclusive verdicts:

Potential Gap Explained	Action
>50% (high-impact)	Must resolve before moving to solution-design. Specify: data needed, source, access barrier, timeline, owner.
10-50% (medium-impact)	Should resolve if data is available within 1 week. Otherwise, note as risk and proceed.
<10% (low-impact)	Skip — proceed to solution-design. Note as unexplained variance.

Designing solutions around an incomplete diagnosis is expensive. A high-impact Inconclusive hypothesis that explains 50%+ of the gap means your root cause statement is missing the biggest driver — solutions will target the wrong thing.

Artifact Template

On re-run: rename existing artifact to problem-analysis.v[N].md and create new with incremented version.

---
skill: problem-analysis
version: 1
date: {{today}}
status: draft
---

# Problem Analysis

## Phase 1: Problem Definition

### Problem Statement

[Metric] is [current] instead of [target], a gap of [X%/X units].
Started: [when]. Inflection point: [if known].

### Logic Tree

[Tree type: Math / Issue / Yes-No]

​```
[Problem statement]
├── [Branch 1]
│   ├── [Leaf 1a]
│   ├── [Leaf 1b]
│   └── [Leaf 1c]
├── [Branch 2]
│   ├── [Leaf 2a]
│   └── [Leaf 2b]
└── [Branch 3]
    ├── [Leaf 3a]
    └── [Leaf 3b]
​```

### MECE Check

- Mutually Exclusive: [confirm no overlaps]
- Collectively Exhaustive: [confirm no gaps]

### External Factor Scan

| Factor | Finding | Status |
|--------|---------|--------|
| Competitor launch | [result] | Confirmed / Ruled Out / Possible |
| Market/seasonal shift | [result] | [status] |
| Platform/algorithm change | [result] | [status] |
| Regulatory/policy change | [result] | [status] |
| Technology change | [result] | [status] |
| Macro-economic conditions | [result] | [status] |

## Phase 2: Hypotheses (Ranked by Testability)

### 1. [Short name] — Priority: HIGH
**If** [cause], **then** [observable evidence], **because** [mechanism].
- **Deciding data:** [specific data point]
- **Source:** [Tool → Report → Metric]
- **Owner:** [person/team]
- **Confirming:** [what you'd see if true]
- **Rejecting:** [what you'd see if false]
- **Potential gap explained:** ~X%

### 2. [Short name] — Priority: HIGH
[Same format]

### 3. [Short name] — Priority: MEDIUM
[Same format]

## Phase 3: Root Cause Verdict

### Verdict Table

| # | Hypothesis | Verdict | Evidence | Gap |
|---|-----------|---------|----------|-----|
| 1 | [Short name] | Confirmed / Rejected / Inconclusive | [Specific data cited] | ~X% |
| 2 | ... | ... | ... | ... |

### Root Cause Statement

**Root Cause 1 (~X% of gap):** [Cause], evidenced by [data].
[One sentence explaining the mechanism.]

**Root Cause 2 (~Y% of gap):** [Cause], evidenced by [data].
[One sentence explaining the mechanism.]

**Unexplained (~Z%):** [Description]. Next data needed: [what], from [where].

## Next Step

Run `solution-design` targeting:
1. [Root cause 1 — specific aspect to solve]
2. [Root cause 2 — specific aspect to solve]

Worked Example

User: "Our signups are declining."

Pre-Dispatch Interview
"What's the current signup rate?" → "About 200/week, down from 350/week"
"When did it start?" → "About 8 weeks ago"
"Any changes around that time?" → "We launched a new homepage and changed our ad targeting"

Problem statement: Weekly signups are 200 instead of 350, a gap of 43%.

Layer 1 — Parallel Dispatch

tree-builder-agent output:

Math Tree

Weekly signups declining (200 → 350 target)
├── Traffic volume declining (fewer people arriving)
│   ├── Paid traffic: ad targeting change reduced volume/quality
│   ├── Organic traffic: SEO impact from homepage redesign
│   └── Referral/direct: brand or word-of-mouth decline
├── Conversion rate declining (same traffic, fewer signups)
│   ├── Homepage redesign reduced clarity/trust
│   ├── Signup flow friction increased
│   └── Value proposition no longer resonates
└── Measurement change (signups happening but not counted)
    ├── Tracking code broken on new homepage
    └── Attribution model changed

MECE Check:
- Mutually Exclusive: Traffic volume vs. conversion rate vs. measurement are independent
- Collectively Exhaustive: All signup decline must come from fewer visitors, lower conversion, or miscounting


external-check-agent output:

| Factor | Finding | Status |
|--------|---------|--------|
| Competitor launch | Searched "[competitor] launch 2026 Q1" — no launches found | Ruled Out |
| Market/seasonal shift | Searched "SaaS signup trends Q1 2026" — no industry-wide decline reported | Ruled Out |
| Platform/algorithm change | Searched "Google algorithm update Feb 2026" — no major update in period | Ruled Out |
| Regulatory/policy change | No relevant changes found | Ruled Out |
| Technology change | No relevant changes found | Ruled Out |
| Macro-economic conditions | Searched "SaaS spending Q1 2026" — stable | Ruled Out |

No external factors confirmed — proceed with internal analysis.


Merge: Tree used as-is (no external branches needed).

Layer 2 — Sequential

hypothesis-agent output (3 hypotheses, ranked):

Tracking broken — Priority: HIGH. If the homepage redesign broke tracking, then GA4 shows a drop while DB signups remain stable, because the new template may not include the tracking script. ~100% if true. Test time: 1 hour.
Ad targeting reduced quality — Priority: HIGH. If the targeting change brought low-intent visitors, then paid conversion dropped while organic held steady, because broader targeting reaches people outside the ICP. ~50%. Test time: 2 hours.
Homepage reduced conversion — Priority: MEDIUM. If the new homepage is less clear, then all-source conversion dropped equally, because the design lacks social proof. ~40%. Test time: 1 day.

data-mapper-agent output:

#	Hypothesis	Deciding Data	Source	Owner
1	Tracking broken	GA4 signups vs. DB signups, 8-week comparison	GA4 Events + Production DB	Engineering
2	Ad targeting	Paid vs. organic conversion rate, before/after	GA4 → Acquisition → Traffic source → Conversion	Marketing (paid)
3	Homepage conversion	Bounce rate by source, before/after	GA4 → Pages → Homepage → Bounce rate	Product/Design
Data Gathering Pause

Orchestrator presents data requirements to user.

User returns with data:

"Checked DB vs GA4 — both show the same drop. Tracking is fine."
"Paid traffic conversion dropped from 3.5% to 1.2%. Organic is still at 4.1%."
"Homepage bounce rate increased from 35% to 52% for all traffic."
verdict-agent output:
#	Hypothesis	Verdict	Evidence	Gap
1	Tracking broken	Rejected	GA4 and DB both show 200/week. Tracking is correct.	0%
2	Ad targeting reduced quality	Confirmed	Paid conversion dropped 66% (3.5% → 1.2%). Organic stable at 4.1%.	~55%
3	Homepage reduced conversion	Confirmed	Bounce rate up 17pts across ALL sources.	~35%

Root Cause Statement:

Root Cause 1 (~55% of gap): Ad targeting change brought low-intent visitors, evidenced by paid conversion dropping 66% while organic held steady. The broader targeting reaches people outside the ICP.

Root Cause 2 (~35% of gap): Homepage redesign reduced trust/clarity, evidenced by bounce rate rising 17 points across all traffic sources. The new page likely lacks the social proof or clear value prop of the old design.

Unexplained (~10%): Minor variance, possibly seasonal. No action needed.

critic-agent output: PASS (all 10 gates satisfied)

Next step: Run solution-design targeting:

Paid targeting — restore or improve audience quality
Homepage — restore trust signals and clarify value proposition
Anti-Patterns

Too-shallow tree — Stopping at one level produces branches that are categories, not testable causes. INSTEAD: Always decompose to at least 2 levels; the leaf should be something you can look up in a specific data source.

Overlapping branches — If fixing Branch A would automatically fix Branch B, the tree is not mutually exclusive. INSTEAD: Restructure until each branch is independently testable. Use the "if I fix A, does B still exist?" check.

Restatements as causes — "Conversion is low because conversion dropped" restates the problem. INSTEAD: Every leaf must name a mechanism — what specifically changed and why.

Missing measurement branch — Most trees cover demand-side and supply-side but forget instrumentation errors. INSTEAD: Always include a "measurement/tracking" branch — it's the fastest to test and explains 100% of the gap when true.

Single tree type for everything — Math trees work for decomposable metrics; issue trees work for multi-factor problems. INSTEAD: Match tree type to problem shape. If the metric has a formula, use a math tree. If not, use an issue tree.

Unfalsifiable hypotheses — "If onboarding is bad, then users churn" cannot be tested because "bad" has no measurable threshold. INSTEAD: Every "then" clause must name a specific metric and direction. Every hypothesis must define what rejection looks like.

Testing everything at once — Running 5 tests simultaneously makes it impossible to attribute results. INSTEAD: Rank by testability and test sequentially — fast eliminations narrow the field.

Confirmation bias in evidence selection — Choosing only data sources likely to confirm the hypothesis. INSTEAD: Every hypothesis must define both confirming AND rejecting evidence before gathering data.

Premature verdicts — Declaring "Confirmed" after seeing one data point that loosely supports the hypothesis. INSTEAD: Every verdict requires evidence that specifically matches or contradicts the "then" clause. "Seems likely" is not Confirmed.

Confusing correlation with causation — "Signups dropped when we changed the homepage, so the homepage caused it." INSTEAD: Correlation identifies candidates; causation requires the mechanism ("because" clause) to hold. Check: does the because explain the data?

Skipping the "because" clause — Omitting the mechanism makes hypotheses unfalsifiable. INSTEAD: The "because" explains why the cause produces the effect — it's what you learn from when the hypothesis is wrong.

Ignoring inconclusive results — Marking ambiguous evidence as "Rejected" to simplify the analysis. INSTEAD: Inconclusive is valid. It means more data is needed. Specify what data, from where, owned by whom.

Gap percentages that don't add up — If root causes explain 140% of the gap (or only 30%), the analysis has double-counting or missing causes. INSTEAD: Percentages should roughly sum to 100%. Re-check for overlapping branches or missed causes.

References
references/watanabe-framework.md — MECE principles and tree-building
references/logic-tree-examples.md — 4 worked examples (SaaS churn, e-commerce, content ROI, B2B pipeline)
references/hypothesis-guide.md — If/Then/Because templates by problem type
Weekly Installs
10
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