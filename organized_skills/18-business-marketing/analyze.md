---
rating: ⭐⭐⭐
title: analyze
url: https://skills.sh/bntvllnt/agent-skills/analyze
---

# analyze

skills/bntvllnt/agent-skills/analyze
analyze
Installation
$ npx skills add https://github.com/bntvllnt/agent-skills --skill analyze
SKILL.md
Universal Analyzer

A standalone skill for multi-perspective analysis of any topic, file, idea, or decision.

Use when:

Need to extract KEY POINTS from anything
Want multi-perspective gap/risk analysis (4-10 experts)
Need improvement opportunities with actionable plans
Want quick summary OR deep analysis mode
Need first-principles brief that challenges assumptions

Triggers: "analyze", "key points", "what's important", "improve this", "review", "examine", "assess", "analysis", "deep analysis", "run deep analysis", "brief", "challenge assumptions", "first principles"

Agent Capabilities
Capability	Used For	Required	Fallback
File read	Load target files/folders	Yes	—
Sub-agent dispatch	Parallel perspective analysis	Recommended	Sequential in main thread
Codebase intelligence (npx codebase-intelligence)	Structural analysis for TS/TSX software domain	No	Pure reasoning from file contents

This skill remains fully functional without CLI tools. Codebase intelligence is an optional enhancement for the software domain only.

Table of Contents
Quick Start
Analysis Modes
Execution Flow
Output Formats
Perspectives Library
Thinking Framework
First-Principles Analysis
Examples
Quick Start
# Quick analysis (fast key points)
analyze quick "our pricing strategy"
analyze brief src/api/auth.ts

# Standard analysis (default)
analyze "SaaS product for developers"
analyze "should I accept this job offer"
analyze package.json

# Deep analysis (comprehensive)
analyze deep "company rebrand strategy"
analyze thorough "migration to microservices"

Analysis Modes
Mode	Triggers	Agents	Duration	Output
Quick	"quick", "fast", "brief", "summary"	0-1	30-60s	Key Points + Actions
Standard	(default)	4-6	2-4min	Multi-Perspective + Roadmap
Deep	"deep", "thorough", "comprehensive"	6-10	5-8min	Full Synthesis + Detailed Plan
Execution Flow
Phase 0: Detection
Mode: Detect from keywords (quick/standard/deep)
Domain: Auto-detect from content/keywords
Target: Load file/folder content if path provided
TypeScript detection: If target is a code path and tsconfig.json exists:
Detection gate: tsconfig.json exists + npx codebase-intelligence --help succeeds
For full CLI reference, fetch https://raw.githubusercontent.com/bntvllnt/codebase-intelligence/main/llms.txt
If available: gather structural data in Phase 1
If unavailable: proceed with pure file-reading context gathering
Phase 1: Context Gathering
File/folder path → Read files
Software domain + TypeScript + CI available → Augment file reading with:
npx codebase-intelligence overview --json <path> → project structure snapshot
npx codebase-intelligence modules --json <path> → module boundaries and cross-deps
npx codebase-intelligence groups --json <path> → directory-level aggregates Include as structured context alongside file contents. If CI unavailable: read files only.
Topic/idea → Use provided context
Unfamiliar domain → Optional web search
Phase 2: Analysis
Quick Mode

Direct analysis by primary agent, no sub-agents

Standard Mode
Select 4-6 perspectives based on domain
Launch all perspectives in parallel (single message block)
Each agent answers 7 core questions
Deep Mode
Select 6-10 perspectives based on domain
Launch all perspectives in parallel (single message block)
Each agent answers 12 questions (7 core + 5 deep)
Software Domain Enhancement (TypeScript + CI available)

Include pre-computed structural data in software domain agent prompts:

npx codebase-intelligence hotspots --json --metric complexity --limit 20 → complexity/churn hotspots
npx codebase-intelligence forces --json → cohesion/coupling tensions per module
npx codebase-intelligence dead-exports --json --limit 20 → unused export analysis
npx codebase-intelligence clusters --json → dependency community clusters

Agents receive this as structured context alongside the target content. Supplements their analysis — does not replace independent reasoning. If CI unavailable: agents analyze from file contents only.

Phase 3: Synthesis

After ALL agents complete:

Aggregate Failure Hypotheses → prioritize Critical→High→Med→Low
Extract TOP 10 key points → rank by consensus
Identify gaps → Critical/High/Medium/Low
Generate actionable roadmap with dependencies
Output Formats
Quick Mode
# Quick Analysis: [Target]

**Mode**: Quick | **Domain**: [Domain] | **Date**: [Date]

## The Essence
[1-2 sentences: What this ACTUALLY is at its core, stripped of complexity]

## Verified Facts
- [Fact 1] — evidence: `path/file:line` or [source]
- [Fact 2] — evidence: ...
- [Fact 3] — evidence: ...

## Key Points (Top 5-10)
1. **[Most Important]**: [Explanation]
2. **[Second]**: [Explanation]
...

## Assumptions to Challenge

| Assumption | Evidence For | Evidence Against | Verdict |
|------------|-------------|------------------|---------|
| [Assumed thing] | [If any] | [If any] | Validate/Keep/Discard |

## What You Haven't Considered

1. **[Critical Item]**: [Why this matters, what to do about it]
2. **[Hidden Risk/Opportunity]**: [Explanation]
3. **[Simpler Alternative?]**: [If exists, describe it]

## The Real Question
[Reframe what the user should actually be asking about this]

## Quick Actions (Top 3-5)
- [ ] [Action 1] - [Why/Impact]
- [ ] [Action 2] - [Why/Impact]
- [ ] [Action 3] - [Why/Impact]

## Critical Risk to Watch
[The one thing that could derail this]

Standard Mode
# Analysis: [Target]

**Mode**: Standard | **Domain**: [Domain] | **Perspectives**: [Count]
**Date**: [Date] | **Hypotheses**: [Count] total

## The Essence
[1-2 sentences: What this ACTUALLY is at its core, stripped of complexity]

## Executive Summary
[2-3 sentences capturing most critical findings]

## First-Principles Analysis

### Verified Facts
- [Fact 1] — evidence: `path/file:line` or [source] — confidence: High/Medium/Low
- [Fact 2] — evidence: ... — confidence: ...

### Assumptions to Challenge

| Assumption | Evidence For | Evidence Against | Verdict |
|------------|-------------|------------------|---------|
| [Assumed thing] | [If any] | [If any] | Validate/Keep/Discard |

### What You Haven't Considered

1. **[Critical Item]**: [Why this matters, what to do about it]
2. **[Hidden Risk/Opportunity]**: [Explanation]
3. **[Simpler Alternative?]**: [If exists, describe it]
4. **[Downstream Impact]**: [What this affects that wasn't mentioned]

### The Real Question
[Reframe what the user should actually be asking about this]

## Failure Hypotheses (Aggregated)

| ID | Type | IF (Trigger) | THEN (Failure) | BECAUSE | Sev | Mitigation |
|----|------|--------------|----------------|---------|-----|------------|
| S001 | Security | ... | ... | ... | Crit | ... |
| M001 | Misuse | ... | ... | ... | High | ... |

### Critical Mitigations Required
- [ ] {mitigation} ← Addresses: S001, M001

## Key Points (Ranked by Importance)

### Consensus Points (Flagged by 3+ perspectives)
1. **[Point]** - [Why important] (Flagged by: [Perspectives])

### Important Points
2. **[Point]** - [Explanation]

### Divergent Views
- **[Topic]**: [Perspective A] sees X, [Perspective B] sees Y
  - *Implication*: [What this tension means]

## Gap Analysis

### Critical Gaps (Action Required)
| Gap | Flagged By | Impact | Suggested Action |
|-----|------------|--------|------------------|
| ... | ... | High | ... |

### High Priority Gaps
[Grouped by theme]

## Improvement Opportunities

### Top 5 Improvements
1. **[Improvement]**: [Details] - Expected Impact: [High/Medium/Low]

## Action Plan & Roadmap

### Immediate Actions (This Week)
| Action | Owner | Dependencies | Success Criteria |
|--------|-------|--------------|------------------|
| ... | [TBD] | None | ... |

### Short-term (1-2 Weeks)
| Action | Dependencies | Resources Needed | Outcome |
|--------|--------------|------------------|---------|
| ... | Immediate #1 | ... | ... |

## Cross-cutting Concerns
[Issues flagged by 3+ perspectives]

Deep Mode

Deep mode extends Standard format with:

Additional 5 questions per agent (12 total)
Medium-term (1 Month) and Long-term (3+ Months) roadmap sections
Dependency map visualization
Risk mitigation table
More detailed failure hypotheses
Perspectives Library
Domain Detection

Analyze content/keywords to auto-detect domain:

Domain	Trigger Keywords	Example Targets
business	startup, business, market, revenue	"coffee subscription", business-plan.md
product	product, feature, user, MVP	"habit tracking app", roadmap.md
software	API, code, function, class, tech	src/auth, package.json
process	workflow, process, SOP, operations	"hiring workflow", "incident response"
document	doc, article, proposal, report	"resume", proposal.docx
research	research, study, hypothesis, data	"hypothesis: remote work"
creative	design, art, brand, visual	"rebrand", logo-designs/
personal	decision, "should I", career, life	"moving to Austin", "career change"
legal	contract, legal, policy, terms	"employment contract"
financial	budget, investment, cost, ROI	"Q4 budget", "pricing strategy"
marketing	campaign, marketing, sales, brand	"email campaign", "launch strategy"
event	event, conference, launch	"product launch", "conference plan"
education	course, curriculum, teaching	"bootcamp curriculum"
general	(fallback when no domain matches)	Any general topic
Perspective Roles by Domain
Business Domain
Startup Founder - Viability, growth, scalability
Investor - ROI, risk, market size
CFO - Unit economics, burn rate, margins
Customer - Value proposition, willingness to pay
Competitor - Differentiation, competitive moats
Market Analyst - TAM, trends, timing
Product Domain
Product Manager - User needs, roadmap, prioritization
Designer (UX) - Usability, user flows, accessibility
Customer - Actual use cases, pain points
QA Engineer - Edge cases, error states
Data Analyst - Metrics, success criteria
Support Lead - Maintenance burden, user confusion
Software Domain
Security Engineer - Vulnerabilities, attack vectors
DevOps - Deployment, monitoring, reliability
Architect - Design patterns, scalability, debt
QA Engineer - Test coverage, edge cases
Performance Engineer - Bottlenecks, resource usage
Tech Lead - Maintainability, team velocity
Process Domain
Operator - Daily execution, friction points
Manager - Efficiency, bottlenecks, metrics
Employee - Experience, clarity, pain points
Auditor - Compliance, documentation, risks
Improvement Specialist - Waste, optimization
Personal Domain
Future You (1 year) - Long-term impact
Future You (5 years) - Career trajectory
Skeptic - Risks, downsides, failure modes
Supporter - Strengths, opportunities
Financial Advisor - Money implications
Life Coach - Values alignment, fulfillment
General Domain (Fallback)
Analyst - Facts, data, patterns
Critic - Weaknesses, risks, gaps
Advocate - Strengths, opportunities
Pragmatist - Feasibility, resources, timeline
Strategist - Long-term implications, alternatives
Devil's Advocate - Unconsidered downsides
Per-Agent Prompt Template

Standard Mode (7 questions):

You are a [Role]. Analyze:
TARGET: [content]

Answer these 7 questions:
1. KEY POINTS: 3-5 most important elements?
2. CORE INSIGHT: Single most critical thing?
3. GAPS: What's missing or incomplete?
4. RISKS: What could go wrong?
5. ASSUMPTIONS: What needs validation?
6. IMPROVEMENTS: Top 3 ways to improve?
7. BLIND SPOTS: What isn't being considered?

FAILURE HYPOTHESES: For each risk/gap:
| ID | IF (Trigger) | THEN (Failure) | BECAUSE | Severity | Mitigation |

Include MISUSE + ADVERSARIAL hypotheses.
Rate findings: Critical/High/Medium/Low


Deep Mode (12 questions = 7 core + 5 additional):

DEPENDENCIES: What does success depend on?
ALTERNATIVES: What other approaches should be considered?
TIMELINE RISKS: What could cause delays or failure?
RESOURCE GAPS: What's missing to execute well?
SUCCESS METRICS: How would you measure success?
Thinking Framework
The UltraThink Loop
THINK → CHECKLIST → PLAN → EXECUTE → VALIDATE → LEARN

Phase 0: THINK

Select thinking model based on task type:

Model	When to Use	Pattern
CoT (Chain of Thought)	Linear, sequential tasks	Step-by-step reasoning
ToT (Tree of Thought)	Multiple valid paths, decisions	Evaluate branches, pick best
Reflexion	Learning from failure, retry logic	Analyze error → adjust → retry
Decomposition	Complex tasks, parallel work	Break into sub-problems

For Analysis: Use ToT (multi-perspective evaluation) for Standard/Deep, CoT for Quick

Phase 1: CHECKLIST
 Mode detected (quick/standard/deep) [blocking]
 Domain identified [blocking]
 Target content accessible [blocking]
 Perspectives selected [blocking]
 Agents dispatched in parallel [blocking]
 All agents completed [blocking]
 Synthesis complete [advisory]
Phase 2: PLAN

For Standard/Deep:

1. Detect mode from keywords
2. Detect domain from content
3. Select N perspectives (4-6 for standard, 6-10 for deep)
4. Launch all agents in ONE message block
5. Wait for completion
6. Synthesize findings
7. Generate output

Phase 3: EXECUTE

Execute plan with progress tracking. On failure → trigger Reflexion (max 2 retries)

Phase 4: VALIDATE
All agents returned findings? ✓
Cross-cutting concerns identified? ✓
Actionable roadmap generated? ✓
Phase 5: LEARN

Capture patterns for continuous improvement

Self-Correction Guide
Issue	Check	Fix	Escalate If
Shallow analysis	Domain auto-detected?	Add specific perspectives	Still shallow after 2 retries
Mode mismatch	User keywords?	Ask for clarification	Agent count doesn't match
Weak synthesis	All agents complete?	Re-run failed agents	<3 perspectives useful
Wrong domain	Keywords ambiguous?	Ask user explicitly	Multiple domains equally valid

Max iterations: 2 | Escalation: Ask user to specify domain/perspectives

First-Principles Analysis

Philosophy: Don't just summarize—decompose to fundamentals, surface what's actually true vs assumed, and raise what the user hasn't considered. User must always get data to make their own decisions.

A. Verified Facts (Separate from Assumptions)
Only report what can be VERIFIED with evidence
Include source: path/file:line or [URL]
Mark confidence: High (verified) / Medium (inferred) / Low (stated but unverified)
B. First-Principles Decomposition

Apply these questions to EVERYTHING found:

1. Question Assumptions
What's being assumed that hasn't been validated?
Is this constraint real or inherited from old decisions?
What would change if [assumption] were false?
2. Decompose to Fundamentals
What MUST be true for this to work?
What are the actual dependencies (not just stated ones)?
What's the irreducible core?
3. Systems Thinking
What else does this affect? (upstream/downstream)
What's the blast radius if this fails?
What's competing for the same resources?
4. Root Cause vs Symptom
Is the current state addressing root cause or masking symptoms?
Why does this exist in its current form?
What problem was this originally solving?
C. Assumptions to Challenge (MANDATORY)

Every analysis MUST include this table:

Assumption	Evidence For	Evidence Against	Verdict
[Assumed thing]	[If any]	[If any]	Validate/Keep/Discard
D. What You Haven't Considered (MANDATORY 2-4 items)

Surface items the user likely hasn't thought about:

Category	What to Look For
Unvalidated Assumptions	Things treated as true without evidence
Hidden Dependencies	Non-obvious things this relies on
Downstream Impacts	What breaks if this changes
Simpler Alternatives	Is there a 10x simpler approach?
Edge Cases	What inputs/states break this?
Technical Debt	Shortcuts that will cost later
Missing Pieces	What's conspicuously absent?
E. The Real Question

Reframe what the user should actually be asking. Often the stated question isn't the right question.

Examples
Example 1: Quick Mode
Input: analyze quick "our pricing strategy"

Output:
# Quick Analysis: Pricing Strategy

**Mode**: Quick | **Domain**: Business | **Date**: 2026-01-28

## The Essence
A business decision about how to extract value from customers, constrained by market dynamics and competitive positioning.

## Verified Facts
- (Would include actual facts from provided content)

## Key Points
1. **Pricing = value capture, not cost recovery**: Price based on customer willingness to pay, not internal costs
2. **Anchor matters**: First price seen shapes all subsequent evaluations
...

## Assumptions to Challenge
| Assumption | Evidence For | Evidence Against | Verdict |
|------------|-------------|------------------|---------|
| "Customers will pay more if we add features" | Common belief | Often false - bloat reduces WTP | Validate with tests |

## What You Haven't Considered
1. **Price as a signal**: Low price may signal low quality, harming conversion
2. **Competitive response**: Price changes trigger competitor reactions
3. **Simplicity premium**: Simpler pricing often outperforms complex tiers

## The Real Question
Not "what price should we charge" but "what's the maximum value customers perceive, and how do we capture 30-50% of it?"

## Quick Actions
- [ ] Survey 20 target customers on WTP before changing price
- [ ] A/B test 2-3 price points on landing page
- [ ] Model competitor response scenarios

## Critical Risk to Watch
Pricing too low initially makes raising prices later extremely difficult (customer backlash + anchoring effect)

Example 2: Standard Mode
Input: analyze "SaaS product for developers"

Flow:
1. Detect mode: standard (no quick/deep keywords)
2. Detect domain: product + software
3. Select 6 perspectives:
   - Product Manager
   - Developer (user persona)
   - Security Engineer
   - DevOps
   - Support Lead
   - Investor
4. Launch all 6 agents in parallel
5. Synthesize findings into standard format
6. Generate actionable roadmap

Output: [Standard format with all sections filled]

Example 3: Deep Mode
Input: analyze deep "migration to microservices"

Flow:
1. Detect mode: deep
2. Detect domain: software
3. Select 10 perspectives:
   - Architect
   - DevOps
   - Security Engineer
   - Database Engineer
   - Frontend Developer
   - QA Engineer
   - Performance Engineer
   - SRE
   - Tech Lead
   - CTO
4. Launch all 10 agents in parallel
5. Each answers 12 questions (7 core + 5 deep)
6. Synthesize into deep format with dependency map
7. Generate comprehensive roadmap (immediate/short/medium/long)

Output: [Deep format with extended sections]

Common Failure Patterns
Failure	Root Cause	Reflexion Response
Wrong domain detected	Ambiguous keywords	Ask user explicitly or use General domain
Too few perspectives	Quick mode used for complex topic	Escalate to Standard mode
Weak synthesis	Agent outputs inconsistent	Re-run with explicit constraints
Missing blind spots	Obvious perspectives chosen	Add Devil's Advocate perspective
Roadmap not actionable	Actions too vague	Break each action into atomic: owner, deadline, metric
Analysis takes >2min	Too many agents (Deep mode overkill)	Switch to Standard mode
Integration Notes

This skill is standalone and includes all necessary frameworks:

UltraThink cognitive framework (embedded)
First-principles analysis (embedded)
Perspectives library (embedded)
Output formats (embedded)

No external dependencies required.

Optional enhancement: For software domain analysis of TypeScript codebases, codebase-intelligence CLI (npx codebase-intelligence --json) provides structural data — hotspots, coupling, dead exports, module boundaries, blast radius. Detection: tsconfig.json must exist. For full CLI reference, fetch https://raw.githubusercontent.com/bntvllnt/codebase-intelligence/main/llms-full.txt. The skill works identically without it — data is supplementary context for perspective agents.

License

MIT License - Free to use, modify, and distribute.

Version

v1.0.0 - 2026-01-28 - Initial public release by bntvllnt

Weekly Installs
52
Repository
bntvllnt/agent-skills
GitHub Stars
14
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass