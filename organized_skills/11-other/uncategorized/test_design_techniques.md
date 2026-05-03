---
rating: ⭐⭐
title: test-design-techniques
url: https://skills.sh/proffesor-for-testing/agentic-qe/test-design-techniques
---

# test-design-techniques

skills/proffesor-for-testing/agentic-qe/test-design-techniques
test-design-techniques
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill test-design-techniques
SKILL.md
Test Design Techniques

<default_to_action> When designing test cases, select technique by input type:

Numeric ranges → BVA + EP
Multiple conditions → Decision Tables
Workflows → State Transition
Many parameter combinations → Pairwise Testing </default_to_action>
Quick Reference Card
When to Use
Designing new test suites
Optimizing existing tests
Complex business rules
Reducing test redundancy
Agent-Driven Test Design
// Auto-generate BVA tests
await Task("Generate BVA Tests", {
  field: 'age',
  dataType: 'integer',
  constraints: { min: 18, max: 120 }
}, "qe-test-generator");
// Returns: 6 boundary test cases

// Auto-generate pairwise tests
await Task("Generate Pairwise Tests", {
  parameters: {
    browser: ['Chrome', 'Firefox', 'Safari'],
    os: ['Windows', 'Mac', 'Linux'],
    screen: ['Desktop', 'Tablet', 'Mobile']
  }
}, "qe-test-generator");
// Returns: 9-12 tests (vs 27 full combination)

Agent Coordination Hints
Memory Namespace
aqe/test-design/
├── bva-analysis/*       - Boundary value tests
├── partitions/*         - Equivalence partitions
├── decision-tables/*    - Decision table tests
└── pairwise/*           - Combinatorial reduction

Fleet Coordination
const designFleet = await FleetManager.coordinate({
  strategy: 'systematic-test-design',
  agents: [
    'qe-test-generator',    // Apply design techniques
    'qe-coverage-analyzer', // Analyze coverage
    'qe-quality-analyzer'   // Assess test quality
  ],
  topology: 'sequential'
});

Related Skills
agentic-quality-engineering - Agent-driven testing
risk-based-testing - Prioritize by risk
mutation-testing - Validate test effectiveness
Remember

With Agents: qe-test-generator applies these techniques automatically, generating optimal test suites with maximum coverage and minimum redundancy. Agents identify boundaries, partitions, and combinations from code analysis.

Weekly Installs
98
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass