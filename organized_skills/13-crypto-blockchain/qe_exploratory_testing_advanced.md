---
rating: ⭐⭐⭐
title: qe-exploratory-testing-advanced
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-exploratory-testing-advanced
---

# qe-exploratory-testing-advanced

skills/proffesor-for-testing/agentic-qe/qe-exploratory-testing-advanced
qe-exploratory-testing-advanced
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-exploratory-testing-advanced
SKILL.md
Advanced Exploratory Testing

<default_to_action> When exploring software or investigating quality risks:

CREATE charter with mission, scope, and time-box (45-90 min)
APPLY heuristics: SFDIPOT (quality criteria), FEW HICCUPPS (consistency oracles)
EXPLORE systematically using test tours (Business District, Bad Neighborhood, Historical)
DOCUMENT findings in real-time with notes, screenshots, evidence
DEBRIEF: What learned? What's next? Share via agent memory

Quick Heuristic Selection:

What to test → SFDIPOT (Structure, Function, Data, Interfaces, Platform, Operations, Time)
Recognize problems → FEW HICCUPPS (Familiar, Explainable, World, History, Image, Comparable, Claims, Users, Product, Purpose, Standards)
Navigate app → Test Tours (12 types for different exploration strategies)

Critical Success Factors:

Exploration is skilled, structured thinking - not random clicking
Document discoveries, not pre-planned test cases
Pair testing reveals more than solo exploration </default_to_action>
Quick Reference Card
When to Use
Investigating new or changed features
Finding bugs automation misses
Learning unfamiliar systems
Risk discovery before test planning
Session Structure (SBTM)
Phase	Duration	Activity
Charter	5 min	Define mission, scope, focus
Explore	45-75 min	Systematic investigation
Note	Continuous	Document findings real-time
Debrief	10-15 min	Summarize, prioritize, share
SFDIPOT Heuristic (What to Test)
Letter	Focus	Example Questions
Structure	Is it properly composed?	Code structure, UI layout, data schema
Function	Does it do what it should?	Core features work correctly
Data	Handles data correctly?	CRUD, validation, persistence
Interfaces	Interacts well?	APIs, UI, integrations
Platform	Works in environment?	Browsers, OS, devices
Operations	Can be used/managed?	Install, config, monitor
Time	Handles timing?	Concurrency, timeouts, scheduling
FEW HICCUPPS Oracle (Recognize Problems)
Consistency With	Check
Familiar problems	Does this look like a known bug pattern?
Explainable	Can behavior be explained rationally?
World	Matches real-world expectations?
History	Consistent with prior versions?
Image	Matches brand/product image?
Comparable	Similar to competing products?
Claims	Matches specs/docs/marketing?
Users	Meets user expectations?
Purpose	Fulfills intended purpose?
Statements	Matches what devs said?
Test Tours (12 Types)
Tour	Strategy
Business District	Critical business flows
Historical	Where bugs clustered before
Bad Neighborhood	Known problem areas
Money	Revenue-impacting features
Landmark	Navigate by key features
Intellectual	Complex, thinking-intensive features
FedEx	Follow data through system
Garbage Collector	Cleanup and edge cases
Museum	Help docs and examples
Rained-Out	What happens when things fail?
Couch Potato	Minimal effort paths
Obsessive-Compulsive	Repetitive actions
Session Note Template
**Charter:** Explore [area] to discover [what] focusing on [heuristic]
**Time-box:** 60 min | **Tester:** [name] | **Date:** [date]

## Session Notes
- [timestamp] Observation/finding
- [timestamp] Bug: [description] - [severity]
- [timestamp] Question: [unclear behavior]

## Findings Summary
- Bugs: X (Critical: Y, Major: Z)
- Questions: X
- Ideas: X

## Coverage
- Areas explored: [list]
- Heuristics used: [SFDIPOT areas]
- % Time on: Bug investigation 30%, Exploration 50%, Setup 20%

## Next Steps
- [ ] Deep dive on [area]
- [ ] Follow up on question about [topic]

Agent-Assisted Exploration
// Collaborative exploration session
await Task("Exploratory Session", {
  charter: 'Explore checkout flow for payment edge cases',
  duration: '60min',
  heuristics: ['SFDIPOT', 'FEW_HICCUPPS'],
  tour: 'money',
  collaboration: 'human-navigator-agent-driver'
}, "qe-flaky-test-hunter");

// Agent generates test variations while human observes
await Task("Edge Case Generation", {
  area: 'payment-form',
  variations: ['boundary-values', 'invalid-inputs', 'concurrent-submits']
}, "qe-test-generator");

// Visual exploration
await Task("Visual Exploration", {
  tour: 'landmark',
  focus: 'responsive-breakpoints',
  compare: 'baseline-screenshots'
}, "qe-visual-tester");

Agent Coordination Hints
Memory Namespace
aqe/exploratory/
├── sessions/*           - Session notes and findings
├── charters/*           - Reusable charter templates
├── bug-clusters/*       - Historical bug patterns
└── heuristic-results/*  - What heuristics revealed

Fleet Coordination
const exploratoryFleet = await FleetManager.coordinate({
  strategy: 'exploratory-testing',
  agents: [
    'qe-flaky-test-hunter',   // Pattern recognition
    'qe-visual-tester',       // Visual anomalies
    'qe-quality-analyzer'     // Risk assessment
  ],
  topology: 'mesh'
});

Pairing Patterns
Pattern	Human Role	Agent Role
Driver-Navigator	Navigate strategy	Execute variations
Strong-Style	Dictate actions	Record findings
Ping-Pong	Observe one area	Explore another
Related Skills
context-driven-testing - RST foundations
risk-based-testing - Focus exploration on risk
agentic-quality-engineering - Agent coordination
Remember

Exploratory testing = simultaneous learning, test design, and test execution.

Not random clicking. Structured, skilled investigation guided by heuristics and oracles. Document discoveries in real-time. Pair testing amplifies findings.

With Agents: Agents generate variations, recognize patterns, and maintain session notes while humans apply judgment and intuition. Combine agent thoroughness with human insight.

Weekly Installs
42
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