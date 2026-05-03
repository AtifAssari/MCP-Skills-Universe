---
rating: ⭐⭐⭐
title: imc-plan
url: https://skills.sh/hungv47/marketing-skills/imc-plan
---

# imc-plan

skills/hungv47/marketing-skills/imc-plan
imc-plan
Installation
$ npx skills add https://github.com/hungv47/marketing-skills --skill imc-plan
SKILL.md
IMC Plan — Orchestrator

Communication — Step 2 of 4. Coordinates specialized agents to turn ICP research into an integrated marketing communication strategy.

Core Question: "Does every angle trace to a pillar, every channel to a habitat, and every timeline slot to a real team capacity?"

Critical Gates — Read First
Identify the growth motion BEFORE selecting channels. PLG (product drives acquisition), SLG (outbound/performance drives acquisition), or Hybrid. The motion determines channel priorities — PLG favors community/SEO/forums, SLG favors paid/email/IRL/SMS.
Evaluate ALL 9 channels, not just digital. The full channel map: Search engines/AEO, Store/Listing platforms, Bounty/Info platforms, News, Forums/Communities, Social media, IRL (OOH/Events/POS), Mailbox, SMS. Offline channels (IRL, SMS) produce strategy docs and creative briefs for physical execution.
Do NOT generate angles before pillars. Angles are derived PER PILLAR. Without pillars, angles are untethered and fail the anti-generic test.
Do NOT assign channels without habitat data. Channel selection comes from ICP research habitat maps, not marketer preference. No habitat data → interview for it.
Do NOT schedule 10 pieces/week for a 2-person team. Match cadence to actual capacity. Over-scheduling guarantees missed deadlines.
Stale ICP research (>30 days) produces misaligned plans. Recommend re-running icp-research before proceeding.
Philosophy

Frameworks (ORB, 3D Angles, Pillar Types) are proven defaults — not mandatory templates. Adapt based on data. When ICP research provides habitat maps, use them. When it doesn't, gather the data before planning channels.

Inputs Required
ICP research from research/icp-research.md + research/product-context.md (or user-provided)
Output
.agents/mkt/imc-plan.md
Quality Gate

Before delivering, the critic agent verifies:

 Growth motion explicitly stated (PLG / SLG / Hybrid)
 3-5 pillars, each with ICP evidence
 3+ angles per pillar, each passing 3Q test and scored ≥15/25
 All 9 channels evaluated (selected or explicitly skipped with rationale)
 Each selected channel has ONE specific angle (not a content category)
 Channel selection based on ICP habitat data AND growth motion alignment
 Channel execution briefs present for every selected channel
 Offline channels (if selected) include compliance and execution notes
 Timeline has 3 phases with realistic cadence
 Launch sequence follows ORB (Owned → Rented → Borrowed)
Chain Position

Previous: icp-research | Next: content-create Re-run triggers: When ICP research is updated, when launching a new product/campaign, or when attribution reveals underperforming channels.

Skill Deference
Need actual content written? → Use content-create — this skill plans, not writes.
Need numeric targets (CAC, LTV, conversion rates)? → Use funnel-planner.
Need to compare pages for SEO? → Coordinate with seo for keyword targeting and content structure.
Need to attribute results to initiatives? → Use attribution after execution.
Agent Manifest
Agent	Layer	File	Focus
Pillar Agent	1	agents/pillar-agent.md	3-5 messaging pillars from ICP pains
Angle Agent	2 (sequential)	agents/angle-agent.md	3D angle generation per pillar
Channel Agent	2 (sequential)	agents/channel-agent.md	9-channel evaluation with habitat-informed selection + execution briefs
Timeline Agent	2 (sequential)	agents/timeline-agent.md	Phase sequencing + editorial calendar
Launch Sequencing Agent	2 (sequential)	agents/launch-sequencing-agent.md	ORB Framework channel activation order
Critic Agent	2 (final)	agents/critic-agent.md	Alignment, scoring rigor, completeness
Shared References (read by agents)
references/3d-angle-framework.md — Three-dimensional angle generation methodology (used by angle-agent)
references/channel-strategy.md — Habitat-informed channel selection framework (used by channel-agent)
references/examples.md — Complete worked examples across 5 business types

Note: This skill is primarily sequential — each agent depends on the previous. Pillar-agent is the only Layer 1 agent. The value of multi-agent here is in specialist focus, critic gate, and single-agent fallback — not parallelism.

Routing Logic
Route A: Quick Plan (MVP or Startup)

When: Limited ICP data, small team, need a plan fast.

1. Pre-dispatch: Gather context (Step 0)
2. Dispatch: pillar-agent (3 pillars, not 5)
3. Dispatch: angle-agent (2 angles per pillar, not 3+)
4. Dispatch: channel-agent (top 2-3 channels only)
5. Dispatch: critic-agent
6. If FAIL → re-dispatch (max 2 cycles)
7. Deliver — timeline and launch sequence done by orchestrator inline

Route B: Full Plan

When: ICP research complete, campaign launch, or strategic planning.

1. Pre-dispatch: Gather context (Step 0)
2. LAYER 1: Dispatch pillar-agent
3. LAYER 2 — Dispatch SEQUENTIALLY:
   - angle-agent (receives pillar output)
   - channel-agent (receives angle output + habitat data)
   - timeline-agent (receives channel output)
   - launch-sequencing-agent (receives timeline output)
4. Dispatch: critic-agent (receives complete plan)
5. If FAIL → re-dispatch named agent(s) with feedback (max 2 cycles)
6. Deliver artifact

Route C: Called by Another Skill

When: content-create or attribution needs plan context.

1. Read existing .agents/mkt/imc-plan.md if available
2. If not available, run Route B
3. Return plan to calling skill

Step 0: Pre-Dispatch Context Gathering
Product Context Check

Check for research/product-context.md and research/icp-research.md. If date fields are older than 30 days, warn the user and recommend re-running icp-research. Tip: /navigate status (from meta-skills) gives a single-pass freshness report across all upstream artifacts.

Required Artifacts
Artifact	Source	If Missing
icp-research.md	icp-research	INTERVIEW. Gather: audience, pains, habitats, awareness stage.
Optional Artifacts
Artifact	Source	Benefit
product-context.md	icp-research	Product details, voice adjectives
solution-design.md	solution-design	Strategic initiatives for alignment
mkt/content-research.md	content-research (research-skills)	Competitor content patterns, audience language, trending topics — informs channel selection and angle priorities
Growth Motion Identification

Before dispatching any agent, determine the growth motion:

Signal	Motion	Channel Priority
Free tier/trial exists, self-serve signup, product virality	PLG	Search engines/AEO, Forums/Communities, Social media (organic), Mailbox (onboarding), Store/Listing platforms, Bounty/Info platforms
Sales team, high ACV, demos required, paid channels primary	SLG	Search engines/AEO (paid), Social media (paid), Mailbox (outbound), SMS, IRL (events/OOH), News
Both motions coexist (e.g., self-serve SMB + sales enterprise)	Hybrid	Blend both — designate primary motion per audience segment

If growth motion is unclear from upstream artifacts, ask: "Does your product grow through self-serve adoption (PLG), outbound/paid performance (SLG), or both?"

Context to Pass to All Agents
Growth motion: PLG, SLG, or Hybrid (determines channel weighting)
Campaign goal: what success looks like
ICP summary: persona, pains, habitats, awareness levels
VoC quotes: top buyer-language phrases
Constraints: team size, budget, timeline
Dispatch Protocol
How to spawn a sub-agent
Read the agent instruction file — include its FULL content in the Agent prompt
Append the context and upstream output after the instructions
Resolve file paths to absolute: replace relative paths with absolute paths
Pass upstream artifacts by content: orchestrator reads .agents/ files, includes relevant excerpts
If feedback exists, append with "## Critic Feedback — Address Every Point"
Single-agent fallback

If multi-agent dispatch is unavailable, execute sequentially in-context:

Pillar extraction (3-5 from ICP)
Angle generation per pillar (3D framework)
Channel assignment per angle (habitat-informed)
Timeline phasing (Pre-launch → Launch → Sustain)
Launch sequencing (ORB)
Self-evaluate with critic rubric
Orchestrator-Written Sections

The orchestrator writes these sections inline (no agent dispatched):

Growth Motion — determined in Step 0, written directly into the artifact before Layer 1
Foundation — core message and awareness distribution, assembled after pillar-agent returns
Channel Execution Briefs — assembled by the orchestrator after channel-agent returns, using channel-agent's output (channel assignments + habitat data) to populate the briefs table with objective, tactic, budget type, metric, owner, and milestone per channel
Layer 1: Pillar Foundation

Dispatch pillar-agent alone. It produces the pillar table that all downstream agents need.

Agent	Instruction File	Pass These Inputs	Reference Files
Pillar Agent	agents/pillar-agent.md	brief + ICP research summary + VoC	—

Wait for completion. Pillar output becomes input for all Layer 2 agents.

Layer 2: Sequential Strategy Chain

Dispatch ONE AT A TIME, IN ORDER. Each receives the previous agent's output.

pillar-agent → angle-agent → channel-agent → timeline-agent → launch-sequencing-agent → critic-agent

Step	Agent	Instruction File	Receives	Reference Files
1	Angle Agent	agents/angle-agent.md	Pillar table	references/3d-angle-framework.md
2	Channel Agent	agents/channel-agent.md	Angle bank + habitat data + growth motion	references/channel-strategy.md (includes 9-Channel Framework)
3	Timeline Agent	agents/timeline-agent.md	Channel assignments	—
4	Launch Sequencing Agent	agents/launch-sequencing-agent.md	Timeline	—
5	Critic Agent	agents/critic-agent.md	Complete assembled plan	—
Critic Gate
PASS: Deliver the plan artifact.
FAIL: Re-dispatch the earliest failing agent with critic feedback. Max 2 cycles.
Artifact Template
---
skill: imc-plan
version: 1
date: [today's date]
status: draft
---

# IMC Plan: [Campaign / Product Name]

**Date:** [today]
**Skill:** imc-plan
**Goal:** [campaign objective]
**Audience:** [primary persona]

## Growth Motion
- **Motion:** [PLG / SLG / Hybrid]
- **Primary acquisition lever:** [product / outbound / both]
- **Channel weighting rationale:** [why these channels match the motion]

## Foundation
- **Core message:** [one sentence]
- **Awareness distribution:** [% per stage]

## Pillars
| # | Pillar | Type | % | Stage | Evidence |
|---|--------|------|---|-------|---------|
| 1 | ... | ... | ... | ... | ... |

## Angle Bank
| # | Angle | Hook | Stage | Trigger | Score | Class | Pillar |
|---|-------|------|-------|---------|-------|-------|--------|
| 1 | ... | ... | ... | ... | ... | ... | ... |

## Channel Assignments
| Channel | Type | Angle | Role | Cadence |
|---------|------|-------|------|---------|
| ... | ... | ... | ... | ... |

**9-Channel Evaluation:** For each channel, the channel-agent assesses relevance and produces a select/skip decision. Channels: Search engines/AEO, Store/Listing platforms, Bounty/Info platforms, News, Forums/Communities, Social media, IRL (OOH/Events/POS), Mailbox, SMS.

## Channel Execution Briefs

For each selected channel, a mini-brief with actionable next steps:

| Channel | Objective | Tactic | Budget Type | Success Metric | Owner | First Milestone |
|---------|-----------|--------|-------------|----------------|-------|-----------------|
| [e.g. Search engines] | [e.g. Capture intent traffic] | [e.g. Google Search ads + SEO content] | [Paid + Organic] | [CTR, CPL] | [Person] | [e.g. First campaign live by W2] |

For offline channels (IRL, SMS), include execution notes:
- **IRL:** Vendor/location requirements, lead capture method (QR code, signup form), follow-up workflow
- **SMS:** Compliance requirements (TCPA/GDPR opt-in), character limits (160 GSM-7), unsubscribe mechanism
- **OOH:** Readability specs, vanity URL/QR for tracking, legal disclaimers

## Timeline
| Week | Phase | Channel | Angle | Format | Status |
|------|-------|---------|-------|--------|--------|
| W1 | ... | ... | ... | ... | Planned |

## Launch Sequence
| Phase | Timing | Channels | Action |
|-------|--------|----------|--------|
| Internal | T-4w | ... | ... |

> On re-run: rename existing artifact to `imc-plan.v[N].md` and create new with incremented version.

Next Step

Run content-create to produce the content assets from this plan. Run attribution to set up measurement. If content-research was not run before this plan, consider running it now to validate content angles with market data before creating assets.

Worked Example — B2B SaaS Project Management Tool (Route B)
Step 0: Pre-Dispatch

Goal: Drive 500 trial signups in 60 days. Audience: Engineering managers at 50-200 person companies. Awareness: 60% Problem Aware, 30% Solution Aware, 10% Product Aware.

Layer 1: Pillar Agent

Returns 4 pillars:

#	Pillar	Type	%	Stage
1	"The meeting tax"	Problem	35%	Problem Aware
2	"Async-first shipping"	Transformation	30%	Solution Aware
3	"Teams who switched"	Trust	25%	Product Aware
4	"The async-first movement"	Social	10%	All
Layer 2, Step 1: Angle Agent

Returns 12 angles across 4 pillars, scored 15-23/25. Example angles:

"12 hrs/week lost to status theater" (Data, Problem Aware, Fear, 22/25, Shareable)
"How to ship 2x without hiring" (How-to, Solution Aware, Greed, 20/25, Searchable)
Layer 2, Step 2: Channel Agent

Returns assignments: LinkedIn (primary, "12 hrs/week"), Email (owned, "async-first shipping"), X/Twitter (ecosystem, "teams who switched"), Blog (owned, searchable how-to content).

Layer 2, Step 3: Timeline Agent

Returns 3 phases: Pre-launch (W1-W3, problem content), Launch (W4-W5, transformation + proof), Sustain (W6+, trust + social). Weekly calendar with pillar rotation.

Layer 2, Step 4: Launch Sequencing Agent

Returns ORB sequence: Internal (T-4w) → Email list alpha (T-2w) → Partner posts (T-1w) → LinkedIn/X launch (Day 0) → PR + paid (T+1w).

Critic Agent → PASS

All quality gates met. Pillar-angle-channel traces verified. Timeline realistic for 3-person team.

Anti-Patterns

Channel-first planning — "We need TikTok content." INSTEAD: Start with habitat maps. If ICP density on TikTok is Low, deprioritize it regardless of what's trendy.

Identical messages across channels — Same text on LinkedIn, X, and Email. INSTEAD: Each channel gets one specific angle adapted to its native format.

Angles without pillar connection — Orphan angles that don't trace back. INSTEAD: Every angle names its parent pillar. No exceptions.

Timeline without capacity check — 10 pieces/week for a solo marketer. INSTEAD: Match cadence to team size. 3 pieces/week is realistic for one person.

Too many pillars — 7 pillars dilute the message. INSTEAD: 3-5. If you can't cut, you haven't committed to a strategy.

Agent Files
Sub-Agent Instructions (agents/)
agents/pillar-agent.md — Messaging pillars from ICP pains
agents/angle-agent.md — 3D angle generation and scoring
agents/channel-agent.md — Habitat-informed channel assignments
agents/timeline-agent.md — Phase sequencing and editorial calendar
agents/launch-sequencing-agent.md — ORB Framework activation order
agents/critic-agent.md — Alignment, rigor, and completeness
Shared References (references/)
references/3d-angle-framework.md — Three-dimensional angle generation methodology
references/channel-strategy.md — Habitat-informed channel selection
references/examples.md — 5 complete worked examples
Weekly Installs
15
Repository
hungv47/marketing-skills
GitHub Stars
1
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass