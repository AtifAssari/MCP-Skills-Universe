---
rating: ⭐⭐
title: qe-risk-based-testing
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-risk-based-testing
---

# qe-risk-based-testing

skills/proffesor-for-testing/agentic-qe/qe-risk-based-testing
qe-risk-based-testing
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-risk-based-testing
SKILL.md
Risk-Based Testing

<default_to_action> When planning tests or allocating testing resources:

IDENTIFY risks: What can go wrong? What's the impact? What's the likelihood?
CALCULATE risk: Risk = Probability × Impact (use 1-5 scale for each)
PRIORITIZE: Critical (20+) → High (12-19) → Medium (6-11) → Low (1-5)
ALLOCATE effort: 60% critical, 25% high, 10% medium, 5% low
REASSESS continuously: New info, changes, production incidents

Quick Risk Assessment:

Probability factors: Complexity, change frequency, developer experience, technical debt
Impact factors: User count, revenue, safety, reputation, regulatory
Dynamic adjustment: Production bugs increase risk; stable code decreases

Critical Success Factors:

Test where bugs hurt most, not everywhere equally
Risk is dynamic - reassess with new information
Production data informs risk (shift-right feeds shift-left) </default_to_action>
Quick Reference Card
When to Use
Planning sprint/release test strategy
Deciding what to automate first
Allocating limited testing time
Justifying test coverage decisions
Risk Calculation
Risk Score = Probability (1-5) × Impact (1-5)

Score	Priority	Effort	Action
20-25	Critical	60%	Comprehensive testing, multiple techniques
12-19	High	25%	Thorough testing, automation priority
6-11	Medium	10%	Standard testing, basic automation
1-5	Low	5%	Smoke test, exploratory only
Probability Factors
Factor	Low (1)	Medium (3)	High (5)
Complexity	Simple CRUD	Business logic	Algorithms, integrations
Change Rate	Stable 6+ months	Monthly changes	Weekly/daily changes
Developer Experience	Senior, domain expert	Mid-level	Junior, new to codebase
Technical Debt	Clean code	Some debt	Legacy, no tests
Impact Factors
Factor	Low (1)	Medium (3)	High (5)
Users Affected	Admin only	Department	All users
Revenue	None	Indirect	Direct (checkout)
Safety	Convenience	Data loss	Physical harm
Reputation	Internal	Industry	Public scandal
Risk Assessment Workflow
Step 1: List Features/Components
Feature | Probability | Impact | Risk | Priority
--------|-------------|--------|------|----------
Checkout | 4 | 5 | 20 | Critical
User Auth | 3 | 5 | 15 | High
Admin Panel | 2 | 2 | 4 | Low
Search | 3 | 3 | 9 | Medium

Step 2: Apply Test Depth
await Task("Risk-Based Test Generation", {
  critical: {
    features: ['checkout', 'payment'],
    depth: 'comprehensive',
    techniques: ['unit', 'integration', 'e2e', 'performance', 'security']
  },
  high: {
    features: ['auth', 'user-profile'],
    depth: 'thorough',
    techniques: ['unit', 'integration', 'e2e']
  },
  medium: {
    features: ['search', 'notifications'],
    depth: 'standard',
    techniques: ['unit', 'integration']
  },
  low: {
    features: ['admin-panel', 'settings'],
    depth: 'smoke',
    techniques: ['smoke-tests']
  }
}, "qe-test-generator");

Step 3: Reassess Dynamically
// Production incident increases risk
await Task("Update Risk Score", {
  feature: 'search',
  event: 'production-incident',
  previousRisk: 9,
  newProbability: 5,  // Increased due to incident
  newRisk: 15         // Now HIGH priority
}, "qe-regression-risk-analyzer");

ML-Enhanced Risk Analysis
// Agent predicts risk using historical data
const riskAnalysis = await Task("ML Risk Analysis", {
  codeChanges: changedFiles,
  historicalBugs: bugDatabase,
  prediction: {
    model: 'gradient-boosting',
    factors: ['complexity', 'change-frequency', 'author-experience', 'file-age']
  }
}, "qe-regression-risk-analyzer");

// Output: 95% accuracy risk prediction per file

Agent Coordination Hints
Memory Namespace
aqe/risk-based/
├── risk-scores/*        - Current risk assessments
├── historical-bugs/*    - Bug patterns by area
├── production-data/*    - Incident data for risk
└── coverage-map/*       - Test depth by risk level

Fleet Coordination
const riskFleet = await FleetManager.coordinate({
  strategy: 'risk-based-testing',
  agents: [
    'qe-regression-risk-analyzer',  // Risk scoring
    'qe-test-generator',            // Risk-appropriate tests
    'qe-production-intelligence',   // Production feedback
    'qe-quality-gate'               // Risk-based gates
  ],
  topology: 'sequential'
});

Integration with CI/CD
# Risk-based test selection in pipeline
- name: Risk Analysis
  run: aqe risk-analyze --changes ${{ github.event.pull_request.files }}

- name: Run Critical Tests
  if: risk.critical > 0
  run: npm run test:critical

- name: Run High Tests
  if: risk.high > 0
  run: npm run test:high

- name: Skip Low Risk
  if: risk.low_only
  run: npm run test:smoke

Related Skills
agentic-quality-engineering - Risk-aware agents
context-driven-testing - Context affects risk
regression-testing - Risk-based regression selection
shift-right-testing - Production informs risk
Remember

Risk = Probability × Impact. Test where bugs hurt most. Critical gets 60%, low gets 5%. Risk is dynamic - reassess with new info. Production incidents raise risk scores.

With Agents: Agents calculate risk using ML on historical data, select risk-appropriate tests, and adjust scores from production feedback. Use agents to maintain dynamic risk profiles at scale.

Weekly Installs
50
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass