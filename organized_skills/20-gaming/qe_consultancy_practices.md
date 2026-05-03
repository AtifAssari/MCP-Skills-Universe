---
rating: ⭐⭐
title: qe-consultancy-practices
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-consultancy-practices
---

# qe-consultancy-practices

skills/proffesor-for-testing/agentic-qe/qe-consultancy-practices
qe-consultancy-practices
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-consultancy-practices
SKILL.md
Consultancy Practices

<default_to_action> When consulting on quality:

LISTEN FIRST: Understand their context before prescribing solutions
DISCOVER: What's the pain? What have they tried? What are constraints?
PRIORITIZE: Impact/effort matrix - high impact, low effort first
TRANSFER KNOWLEDGE: Leave them better, not dependent on you
MEASURE: Define success metrics upfront, track weekly

Engagement Types:

Assessment (1-4 weeks): Discover, analyze, recommend
Transformation (3-12 months): Implement new practices
Advisory (ongoing): Strategic guidance, course-correct
Crisis (1-4 weeks): Fix critical issues blocking production

Key Questions:

"Walk me through your last deployment"
"Tell me about a recent bug that escaped to production"
"If you could fix one thing, what would it be?" </default_to_action>
Quick Reference Card
The Consulting Process
Phase	Duration	Goal	Deliverable
Discovery	Week 1-2	Understand context	Interview notes, observations
Analysis	Week 2-3	Identify root causes	Impact/effort matrix
Recommendations	Week 3-4	Present findings	Report with roadmap
Implementation	Month 2-6+	Execute changes	Working system, trained team
Transition	Final month	Ensure self-sufficiency	Handover docs
Impact/Effort Matrix
Priority	What	Action
High Impact, Low Effort	Quick wins	Do first
High Impact, High Effort	Major initiatives	Plan carefully
Low Impact, Low Effort	Nice-to-haves	If time permits
Low Impact, High Effort	Distractions	Skip
Common Patterns
"We Need Test Automation"

What they say: "We need test automation" What they mean: "Manual testing is too slow/expensive"

Discovery: How long is regression? What's deployment frequency?

Typical Finding: They need faster feedback, not "automation"

Recommendation:

Unit tests for new code (TDD)
Smoke tests for critical paths
Keep exploratory for discovery
Build automation incrementally
"Fix Our Quality Problem"

What they say: "We have too many bugs" What they mean: "Something is broken but we don't know what"

Discovery: Where found? What types? When introduced?

Typical Finding: No test strategy, testing too late, poor feedback loops

Recommendation:

Shift testing left
Improve coverage on critical paths
Speed up CI/CD feedback
Better requirements/acceptance criteria
"We Want to Scale Quality"

What they say: "Growing fast, quality can't keep up" What they mean: "Can't hire enough QA fast enough"

Discovery: Current QA:Dev ratio? Where's QA spending time?

Typical Finding: QA is bottleneck - manual regression, gatekeeping

Recommendation:

Make QA strategic, not tactical
Developers own test automation
QA focuses on exploratory, risk analysis
Use agentic approaches for scale
Anti-Patterns
Anti-Pattern	Problem	Better
Cookie-Cutter	Same solution everywhere	Context-specific recommendations
Tool Pusher	Recommend expensive tools	Tools that solve actual problems
Process Nazi	Impose rigid process	Lightweight, fits their culture
Permanent Fixture	Never leave, create dependency	Work toward them not needing you
Blame Game	Point fingers at people	Fix systems, not blame people
Difficult Situations

"We already tried that" → "Tell me what you tried and what didn't work" (learn from their experience)

"Our context is special" → "Help me understand what makes yours special" (they might be right, or making excuses)

"We don't have budget/time" → "What's the cost of not fixing this? Let's start small" (show ROI)

"That won't work here" → "What specific constraints? Let's adapt" (find what WILL work)

Agent Integration
// Automated codebase assessment
const assessment = await Task("Assess Codebase", {
  scope: 'client-project/',
  depth: 'comprehensive',
  reportFormat: 'executive-summary'
}, "qe-quality-analyzer");

// Returns: { qualityScore, testCoverage, technicalDebt, recommendations }

// ROI analysis for quality initiatives
const roi = await Task("Calculate ROI", {
  currentState: { defectEscapeRate: 0.15, mttr: 48 },
  proposedImprovements: ['test-automation', 'ci-cd-pipeline'],
  timeframe: '6-months'
}, "qe-quality-analyzer");

// Returns: { estimatedCost, estimatedSavings, paybackPeriod }

Agent Coordination Hints
Memory Namespace
aqe/consultancy/
├── assessments/*      - Client assessments
├── recommendations/*  - Prioritized recommendations
├── roi-analysis/*     - ROI calculations
└── progress/*         - Implementation tracking

Fleet Coordination
const consultingFleet = await FleetManager.coordinate({
  strategy: 'client-engagement',
  agents: [
    'qe-quality-analyzer',          // Assess current state
    'qe-regression-risk-analyzer',  // Risk assessment
    'qe-quality-gate',              // Define quality gates
    'qe-deployment-readiness'       // Deployment maturity
  ],
  topology: 'hierarchical'
});

Related Skills
quality-metrics - Metrics for client reporting
risk-based-testing - Client risk assessment
holistic-testing-pact - Comprehensive strategy
Remember

Good consulting is about empowering teams, not creating dependency. Your success is measured by them not needing you anymore - while still wanting to work with you again.

Best compliment: "We've got this now, but when we tackle X next year, we're calling you."

Be honest. Be helpful. Be context-driven. Leave them better.

Weekly Installs
47
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass