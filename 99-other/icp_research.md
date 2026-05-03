---
title: icp-research
url: https://skills.sh/hungv47/research-skills/icp-research
---

# icp-research

skills/hungv47/research-skills/icp-research
icp-research
Installation
$ npx skills add https://github.com/hungv47/research-skills --skill icp-research
SKILL.md
ICP Research — Orchestrator

Communication — Step 1 of 4. Foundational skill for all stacks. Coordinates specialized sub-agents to build deep audience intelligence from real research, not assumptions.

Core Question: "Who exactly are we talking to and what keeps them up at night?"

Critical Gates — Read First

Before dispatching any agent, internalize these non-negotiable constraints:

Do NOT guess personas — evidence from VoC or interview only. Every persona attribute must trace to product context, brief details, user input, or VoC quotes. Fabricated personas collapse under scrutiny and mislead 12+ downstream skills.
Do NOT skip habitat mapping — channels without habitats waste downstream effort. IMC planning depends on specific community names with density and engagement type. "They're on LinkedIn" is not actionable.
Max 2 personas — more dilutes focus for 12+ downstream skills. If research reveals 4+ segments, force-rank by revenue potential. This is a genuine constraint, not a suggestion.
Stale product context (>30 days) → recommend re-running. If research/product-context.md exists but its Date field is older than 30 days, warn the user and recommend re-running this skill. Proceed if the user confirms, but note "stale product context" in the artifact header.
Philosophy

This skill provides research structure, not a rigid formula. The minimums for channels, quotes, and platforms ensure thoroughness — they're not arbitrary thresholds. If overwhelming evidence surfaces in 2 channels, you don't need a third. If one devastating quote captures a pain perfectly, you don't need three. Let evidence dictate depth. This orchestrator dispatches specialist agents for each research concern, then a critic agent ensures every section meets the bar.

Inputs Required
Product context from research/product-context.md (or willingness to answer product questions)
Output
research/icp-research.md
research/product-context.md (foundational — written on first run, updated on re-run)
Quality Gate

Before delivering, the critic agent verifies:

 Every VoC quote includes platform name and is from a real source (not agent-generated)
 Each persona has a habitat map with specific channels with supporting evidence. Aim for 3+; if research surfaces fewer, document why.
 Each emotional driver is traced to at least 2 specific quotes
 Decision psychology section names specific cognitive biases and objections (not generic "they need trust")
 At least 15 VoC quotes across categories
 Maximum 2 personas
Chain Position

Previous: none (or any skill needing audience context) | Next: imc-plan, brand-system (from marketing-skills — uses audience data for brand strategy)

Foundational role: This skill creates research/product-context.md, used by 12+ downstream skills across all 4 stacks (comms, strategy, prod, design). Running it first provides significantly better output for all downstream skills. Re-run triggers: When pivoting audience, entering a new market, after major product changes, or quarterly for active products.

Skill Deference
Need competitive analysis or market sizing? → Use market-research
Need campaign planning from these personas? → Use imc-plan
Need brand identity using audience data? → Use brand-system
Need to diagnose a business problem, not an audience? → Use problem-analysis
Agent Manifest
Agent	Layer	File	Focus
Persona Agent	1 (parallel)	agents/persona-agent.md	Demographics, role, goals, frustrations — builds persona cards
VoC Collector Agent	1 (parallel)	agents/voc-collector-agent.md	Voice-of-customer quote collection from multiple platforms
Habitat Agent	1 (parallel)	agents/habitat-agent.md	Platform/community mapping — where the ICP lives online
Pain Analysis Agent	2 (sequential)	agents/pain-analysis-agent.md	Surface → Hidden → Emotional pain classification from VoC evidence
Decision Psychology Agent	2 (sequential)	agents/decision-psychology-agent.md	Trigger events, research behavior, cognitive biases, objections
Synthesis Agent	2 (sequential)	agents/synthesis-agent.md	Merges all fragments into coherent ICP profile
Critic Agent	2 (final)	agents/critic-agent.md	Quality gate — PASS/FAIL evaluation with rewrite routing
Shared References (read by multiple agents)
references/voice-of-customer.md — VoC collection patterns, quote categories, platform tips (used by voc-collector-agent)
references/customer-interviews.md — Win/loss interview methodology, support ticket analysis (used by voc-collector-agent)
references/habitat-mapping.md — Density definitions, engagement types, cross-persona analysis (used by habitat-agent)
references/icp-to-imc-handoff.md — How to package outputs for IMC planning (used by synthesis-agent)
Routing Logic

Classify the task, then follow the matching route.

Route A: Quick ICP

When: Brief asks for a focused ICP with minimal scope — single persona, known audience, time-constrained.

1. Pre-dispatch: Gather context (Step 0 below)
2. Scope interview (Step 1 below)
3. LAYER 1 — Dispatch IN PARALLEL:
   - persona-agent
   - voc-collector-agent
4. LAYER 2 — Dispatch SEQUENTIALLY:
   - pain-analysis-agent (receives persona + VoC output)
   - synthesis-agent (receives all upstream — skips habitat + decision psychology)
   - critic-agent
5. If critic returns FAIL → re-dispatch named agent(s) with feedback (max 2 cycles)
6. Deliver artifact


Note: Route A skips habitat-agent and decision-psychology-agent. Use when the user needs speed over depth. The artifact will have empty Habitat Map and Decision Psychology sections — note this as a limitation.

Route B: Full ICP

When: Brief asks for comprehensive ICP research — full persona profiles, habitat mapping, decision psychology.

1. Pre-dispatch: Gather context (Step 0 below)
2. Scope interview (Step 1 below)
3. LAYER 1 — Dispatch IN PARALLEL:
   - persona-agent
   - voc-collector-agent
   - habitat-agent
4. LAYER 2 — Dispatch SEQUENTIALLY:
   - pain-analysis-agent (receives persona + VoC output)
   - decision-psychology-agent (receives pain-analysis output)
   - synthesis-agent (receives ALL upstream outputs)
   - critic-agent (receives synthesis output)
5. If critic returns FAIL → re-dispatch named agent(s) with feedback (max 2 cycles)
6. Deliver final artifact

Route C: Called by Another Skill

When: Invoked by imc-plan, brand-system, content-create, or another skill that needs audience context.

1. Pre-dispatch: Read context from calling skill's artifacts
2. Check if research/icp-research.md already exists:
   - If exists and fresh (< 30 days) → return existing artifact
   - If exists but stale (> 30 days) → warn caller and recommend re-run
   - If missing → run Route B
3. Return artifact to calling skill

Step 0: Pre-Dispatch — Product Context

Check for research/product-context.md. If missing, scan first, then interview for gaps:

Auto-scan available sources: Look for README.md, marketing site copy, pricing page, product descriptions, and any existing documentation in the codebase. Extract what you can about the 8 dimensions below.
Interview only for gaps: Present what you found and ask the user to confirm, correct, or fill in missing dimensions.

This scan-then-interview approach avoids asking the user questions they've already answered elsewhere. This skill is the canonical source for product context across all skill stacks (comms, strategy, prod, design). Save to research/product-context.md:

# Product Context

**Date:** [today]

## Product
[One sentence: what you sell]

## Buyer
[Primary buyer: role, company type, situation]

## Problem
[The pain it solves — in their words, not yours]

## Differentiator
[What's different — something a competitor CANNOT claim]

## Social Proof
[Best testimonial or most repeated praise]

## Model
[Price, pricing model, free trial availability]

## Voice
[3 adjectives: e.g., "direct, technical, warm"]

## Primary CTA
[What should people do next: e.g., "Start free trial"]

## Canonical Terminology
| Term | Definition | Don't use |
|------|-----------|-----------|
| [canonical term] | [precise definition] | [synonyms to avoid] |


The Canonical Terminology section defines the shared vocabulary for the product and domain. Downstream skills (imc-plan, content-create, copywriting, humanize, lp-optimization) reference this to maintain consistent language across all artifacts. Populate during the scope interview — ask: "What do you call your users? Your pricing tiers? The main workspace?" If the user doesn't have strong preferences, propose defaults from the codebase (variable names, UI labels, docs).

All marketing skills read this file for product context.

Required Artifacts
Artifact	Source	If Missing
product-context.md	icp-research	INTERVIEW. Interview for 8 product dimensions and save to research/product-context.md.
Optional Artifacts
Artifact	Source	Benefit
problem-analysis.md	problem-analysis (from hungv47/research-skills)	Problem context sharpens audience research
Step 1: Scope Interview

Interview for:

Who are we researching? (Job role, mindset, community, or use case)
What decisions will this inform? (Messaging? Channels? Positioning? All three?)
B2C or B2B? Geography? Specific segments to focus or exclude?

Use the answers to determine the route (A, B, or C) and to populate the brief passed to all agents.

Dispatch Protocol
How to spawn a sub-agent

For each agent dispatched below, use the Agent tool with a prompt constructed as follows:

Read the agent instruction file (e.g., agents/persona-agent.md) — include its FULL content in the Agent prompt
Append the brief and context after the instructions
Resolve file paths to absolute: replace relative paths with absolute paths rooted at this skill's directory. Example: if this skill is at /path/to/icp-research/, then references/voice-of-customer.md becomes /path/to/icp-research/references/voice-of-customer.md. Tell the agent: "Read the reference file at [absolute path] for domain knowledge."
Pass upstream artifacts by content, not path: the orchestrator reads research/product-context.md FIRST, then includes relevant excerpts (product, buyer, problem, differentiator) in the context object. Sub-agents should NOT read artifact files directly — the orchestrator curates what they need.
If feedback exists (from a critic FAIL cycle), append it at the end of the prompt with the header "## Critic Feedback — Address Every Point"
Single-agent fallback

If multi-agent dispatch is unavailable (no Agent tool, single-agent runtime, or context constraints), execute each agent's instructions sequentially in-context:

Layer 1: Run each agent's domain instructions one at a time — persona, VoC collection, habitat mapping
Layer 2: Apply pain analysis to Layer 1 outputs, then decision psychology, then synthesis
Critic: Self-evaluate using the critic-agent's quality gate criteria
Produce the complete artifact as if all agents had run

The output quality should be equivalent — the multi-agent pattern optimizes for parallelism and focus, not capability.

Layer 1: Parallel Research Agents

Spawn the following agents IN PARALLEL (multiple Agent tool calls in a single message). For each agent, follow the Dispatch Protocol above.

Agent	Instruction File	Pass These Inputs	Reference Files to Resolve
Persona Agent	agents/persona-agent.md	brief + product context	—
VoC Collector Agent	agents/voc-collector-agent.md	brief + product context	references/voice-of-customer.md, references/customer-interviews.md
Habitat Agent	agents/habitat-agent.md	brief + product context	references/habitat-mapping.md

For Quick ICP (Route A): Dispatch only persona-agent and voc-collector-agent.

After Layer 1 completes, the orchestrator holds all three outputs (persona cards, VoC library, habitat map) ready to feed into Layer 2.

Layer 2: Sequential Analysis Chain

Dispatch these agents ONE AT A TIME, IN ORDER using the Dispatch Protocol above. Each receives the previous agent's output (plus relevant Layer 1 outputs) as the upstream field.

pain-analysis-agent → decision-psychology-agent → synthesis-agent → critic-agent

Step	Agent	Instruction File	Receives
1	Pain Analysis Agent	agents/pain-analysis-agent.md	persona-agent output + voc-collector-agent output
2	Decision Psychology Agent	agents/decision-psychology-agent.md	pain-analysis-agent output
3	Synthesis Agent	agents/synthesis-agent.md	ALL upstream: persona + VoC + habitat + pain + psychology
4	Critic Agent	agents/critic-agent.md	synthesis-agent output

For Quick ICP (Route A): Skip decision-psychology-agent. Pain-analysis feeds directly to synthesis, which feeds to critic.

Critic Gate

The critic agent returns one of two verdicts:

PASS

The artifact meets all quality standards. Deliver the synthesis agent's output as the final artifact to research/icp-research.md.

FAIL

The critic returns specific failures with:

Which gate failed and what's wrong
Specific fix instructions
Which agent to re-dispatch

Rewrite loop:

Read the critic's failure report
Re-dispatch ONLY the named agent(s) with the critic's feedback attached as the feedback input
If the fix affects downstream agents, re-run the chain from the fixed agent forward
Run the modified output back through the critic
Maximum 2 rewrite cycles. After 2 failures, deliver the artifact with the critic's annotations and flag to the user: "ICP scored below quality gate — manual review recommended on [specific sections]."
Artifact Template
---
skill: icp-research
version: 1
date: [today's date]
status: draft
---

# ICP Research

**Date:** [today]
**Skill:** icp-research
**Product:** [from product-context.md]

## Persona 1: [Name/Archetype]

**Demographics:** [Age, role, industry, company size]

### Pain Profile
1. **[Pain name]** — [description]
   - Trigger: [what causes acute pain]
   - Impact: [daily/financial/professional]
   - Quote: "[exact quote]" — [Platform, context]
   - Quote: "[exact quote]" — [Platform, context]

2. **[Pain name]** — [description]
   [Same format]

3. **[Pain name]** — [description]
   [Same format]

### Decision Psychology
- **Trigger:** [what event starts their search]
- **Research path:** [where they go 1st → 2nd → 3rd]
- **Key biases:** [which cognitive biases are strongest]
- **Objections:** (1) [objection] — root: [psychological reason]. (2) [objection] — root: [reason]. (3) [objection] — root: [reason].
- **Trust signals:** [what they trust]
- **Distrust triggers:** [what kills credibility]

### Habitat Map
| Platform | Community | Density | Engagement | Role |
|----------|-----------|---------|-----------|------|
| [Specific] | [Specific] | H/M/L | [Type] | [Role] |

## Persona 2: [Name/Archetype]
[Same format]

## Top 3 Emotional Drivers
1. **[Driver]** — [explanation]. Quotes: "[quote 1]" ([source]), "[quote 2]" ([source])
2. **[Driver]** — [explanation]. Quotes: ...
3. **[Driver]** — [explanation]. Quotes: ...

## Red Flags
- [Language/positioning that triggers skepticism and why]

## Next Step
Run `imc-plan` to turn these insights into a communication plan.

> On re-run: rename existing artifact to `icp-research.v[N].md` and create new with incremented version.

Worked Example — Full ICP (Route B)

Brief: "Research my ICP for a project management tool aimed at engineering teams."

Step 0: Pre-Dispatch

Product context scanned from README.md and pricing page. Saved to research/product-context.md:

Product: ProjectSync — async project visibility for engineering teams
Buyer: Engineering managers at mid-size SaaS companies
Problem: Hours lost to status updates nobody reads
Step 1: Scope Interview
"Who?" → Engineering managers at mid-size SaaS companies (50-200 engineers)
"What decisions?" → Messaging and channel strategy for launch
"B2B/B2C?" → B2B, US and EU
Route selected: B (Full ICP — comprehensive research needed for launch)
Layer 1: Parallel Dispatch

Three agents dispatched simultaneously:

Persona agent returns:

Persona 1: The Overwhelmed EM

Demographics: 30-38, Engineering Manager, B2B SaaS, 50-200 engineers Goals: (1) Ship on schedule without burning out the team. (2) Give leadership visibility without micromanaging. Frustrations: "I spend more time telling people what I did than actually doing it." "Our standups are 45 minutes of reading Jira tickets aloud." Day-in-the-life: Monday 9am — Sarah opens Slack to 47 unread messages, half status updates she needs to compile for her VP by 10am.

VoC collector agent returns:

18 quotes across 5 categories from r/ExperiencedDevs, r/engineeringmanagers, G2, Twitter, LinkedIn. Key mechanism quote: "No single tool shows me what my team actually shipped this week — I have to check Jira, GitHub, and Slack separately and piece it together."

Habitat agent returns:

Platform	Community	Density	Engagement	Role
Reddit	r/ExperiencedDevs	H	Engager	Trust
Reddit	r/engineeringmanagers	M	Lurker	Trust
LinkedIn	#engineeringmanagement feed	M	Creator	Discovery
Twitter/X	#engmanagement	L	Lurker	Discovery
Slack	Rands Leadership Slack	H	Engager	Trust
Layer 2: Sequential Dispatch

Pain analysis agent receives persona + VoC output. Returns:

1. Status Update Theater — hours lost compiling updates nobody reads
Level: Surface → Hidden (spreadsheet workarounds) → Emotional (fear of looking disorganized)
Trigger: Monday 9am — VP expects status email by 10am
Impact: 6-8 hrs/week on reporting. Career: EMs who can't show visibility get passed over.
Mechanism: No single system aggregates team activity. The EM becomes the human integration layer.

Decision psychology agent receives pain analysis output. Returns:

Trigger: Promoted to manage second team — reporting overhead doubles
Research path: 1st Reddit (r/ExperiencedDevs) → 2nd G2 comparisons → 3rd free trial
Key biases: Status-quo bias (invested in current Jira setup), loss aversion (fear of losing data in migration)
Objections: (1) "We already have Jira" — root: sunk cost + status-quo bias. (2) "My team won't adopt another tool" — root: diffusion of responsibility. (3) "How is this different from Monday.com?" — root: category fatigue.

Synthesis agent receives all upstream. Merges into complete ICP artifact matching the template. Adds:

Top 3 Emotional Drivers
Fear of being perceived as unable to scale — EMs who can't produce visibility for leadership fear being passed over for promotion or labeled as "not ready for director." Quotes: "My skip-level keeps asking me for updates I can't produce fast enough" (r/engineeringmanagers), "I got feedback that I 'lack strategic visibility' and I don't even know what that means" (r/ExperiencedDevs)
Critic Gate → PASS

All 7 gates pass. 18 quotes with attribution. Habitats are specific. Biases are named. Drivers traced to 2+ quotes each. Artifact delivered to research/icp-research.md.

Anti-Patterns

Guessing personas without evidence — Inventing "Sarah, 34, EM" because it sounds right, without VoC quotes or brief details to support it. INSTEAD: Let the persona agent build from product context and brief, and the pain analysis agent validate against VoC evidence.

Skipping habitat mapping for speed — Dropping the habitat agent because "we know they're on Reddit." INSTEAD: Use Route A (Quick ICP) which explicitly skips habitats and notes the limitation. Don't silently omit sections.

Fabricating VoC quotes — Generating plausible-sounding quotes when research tools return thin results. INSTEAD: Document data gaps honestly, flag confidence as LOW, and recommend the user provide customer quotes, support tickets, or sales call notes.

Too many personas — Including 3+ personas because research surfaced distinct segments. INSTEAD: Force-rank to 2 max by revenue potential. Document who was cut and why in the Segment Rationale.

Platform-level habitat mapping — "They're on LinkedIn" without naming the specific group, hashtag, or content type. INSTEAD: Every habitat entry must name the specific community. The habitat agent enforces this.

Recycling stale research — Reusing personas and VoC from a previous iteration without re-validation. INSTEAD: Check the artifact date. If >30 days, recommend re-running. Markets shift, competitors launch, and pain points evolve.

Ignoring the critic's FAIL — Delivering an artifact that failed quality gates because "it's close enough." INSTEAD: Re-dispatch the named agent with critic feedback. Max 2 cycles, then deliver with annotations.

Agent Files
Sub-Agent Instructions (agents/)
agents/persona-agent.md — Demographics, role, goals, frustrations — persona card builder
agents/voc-collector-agent.md — VoC quote collection from multiple platforms
agents/habitat-agent.md — Platform/community mapping with density and engagement
agents/pain-analysis-agent.md — Surface → Hidden → Emotional pain classification
agents/decision-psychology-agent.md — Triggers, biases, objections, trust/distrust signals
agents/synthesis-agent.md — Merges fragments into coherent ICP artifact
agents/critic-agent.md — Quality gate — PASS/FAIL with rewrite routing
agents/_template.md — Reusable template for creating new agent files
Shared References (references/)
references/voice-of-customer.md — VoC collection patterns, quote categories, platform tips
references/customer-interviews.md — Win/loss interview methodology, support ticket analysis
references/habitat-mapping.md — Density definitions, engagement types, cross-persona analysis
references/icp-to-imc-handoff.md — How to package outputs for IMC planning
Weekly Installs
8
Repository
hungv47/research-skills
GitHub Stars
1
First Seen
8 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn