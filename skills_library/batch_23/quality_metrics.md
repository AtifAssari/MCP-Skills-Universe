---
title: quality-metrics
url: https://skills.sh/proffesor-for-testing/agentic-qe/quality-metrics
---

# quality-metrics

skills/proffesor-for-testing/agentic-qe/quality-metrics
quality-metrics
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill quality-metrics
SKILL.md
Quality Metrics

<default_to_action> When measuring quality or building dashboards:

MEASURE outcomes (bug escape rate, MTTD) not activities (test count)
AVOID vanity metrics: 100% coverage means nothing if tests don't catch bugs
SET thresholds that drive behavior (quality gates block bad code)
TREND over time: Direction matters more than absolute numbers </default_to_action>
Quick Reference Card
When to Use
Building quality dashboards
Defining quality gates
Evaluating testing effectiveness
Justifying quality investments
Quality Gate Thresholds
Metric	Blocking Threshold	Warning
Test pass rate	100%	-
Critical coverage	> 80%	> 70%
Security critical	0	-
Performance p95	< 200ms	< 500ms
Flaky tests	< 2%	< 5%
Dashboard Design
// Agent generates quality dashboard
await Task("Generate Dashboard", {
  metrics: {
    delivery: ['deployment-frequency', 'lead-time', 'change-failure-rate'],
    quality: ['bug-escape-rate', 'test-effectiveness', 'defect-density'],
    stability: ['mttd', 'mttr', 'availability'],
    process: ['code-review-time', 'flaky-test-rate', 'coverage-trend']
  },
  visualization: 'grafana',
  alerts: {
    critical: { bug_escape_rate: '>20%', mttr: '>24h' },
    warning: { coverage: '<70%', flaky_rate: '>5%' }
  }
}, "qe-quality-analyzer");

Quality Gate Configuration
{
  "qualityGates": {
    "commit": {
      "coverage": { "min": 80, "blocking": true },
      "lint": { "errors": 0, "blocking": true }
    },
    "pr": {
      "tests": { "pass": "100%", "blocking": true },
      "security": { "critical": 0, "blocking": true },
      "coverage_delta": { "min": 0, "blocking": false }
    },
    "release": {
      "e2e": { "pass": "100%", "blocking": true },
      "performance_p95": { "max_ms": 200, "blocking": true },
      "bug_escape_rate": { "max": "10%", "blocking": false }
    }
  }
}

Agent-Assisted Metrics
// Calculate quality trends
await Task("Quality Trend Analysis", {
  timeframe: '90d',
  metrics: ['bug-escape-rate', 'mttd', 'test-effectiveness'],
  compare: 'previous-90d',
  predictNext: '30d'
}, "qe-quality-analyzer");

// Evaluate quality gate
await Task("Quality Gate Evaluation", {
  buildId: 'build-123',
  environment: 'staging',
  metrics: currentMetrics,
  policy: qualityPolicy
}, "qe-quality-gate");

Agent Coordination Hints
Memory Namespace
aqe/quality-metrics/
├── dashboards/*         - Dashboard configurations
├── trends/*             - Historical metric data
├── gates/*              - Gate evaluation results
└── alerts/*             - Triggered alerts

Fleet Coordination
const metricsFleet = await FleetManager.coordinate({
  strategy: 'quality-metrics',
  agents: [
    'qe-quality-analyzer',         // Trend analysis
    'qe-test-executor',            // Test metrics
    'qe-coverage-analyzer',        // Coverage data
    'qe-production-intelligence',  // Production metrics
    'qe-quality-gate'              // Gate decisions
  ],
  topology: 'mesh'
});

Related Skills
agentic-quality-engineering - Agent coordination
cicd-pipeline-qe-orchestrator - Quality gates
risk-based-testing - Risk-informed metrics
shift-right-testing - Production metrics
Remember

With Agents: Agents track metrics automatically, analyze trends, trigger alerts, and make gate decisions. Use agents to maintain continuous quality visibility.

Weekly Installs
80
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