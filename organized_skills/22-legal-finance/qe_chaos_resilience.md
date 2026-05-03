---
rating: ⭐⭐⭐
title: qe-chaos-resilience
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-chaos-resilience
---

# qe-chaos-resilience

skills/proffesor-for-testing/agentic-qe/qe-chaos-resilience
qe-chaos-resilience
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-chaos-resilience
SKILL.md
QE Chaos Resilience
Purpose

Guide the use of v3's chaos engineering capabilities including controlled fault injection, load/stress testing, resilience validation, and disaster recovery testing.

Activation
When testing system resilience
When performing chaos experiments
When load/stress testing
When validating disaster recovery
When testing circuit breakers
Quick Start
# Run chaos experiment
aqe chaos run --experiment network-latency --target api-service

# Load test
aqe chaos load --scenario peak-traffic --duration 30m

# Stress test to breaking point
aqe chaos stress --endpoint /api/users --max-users 10000

# Test circuit breaker
aqe chaos circuit-breaker --service payment-service

Agent Workflow
// Chaos experiment
Task("Run chaos experiment", `
  Execute controlled chaos on api-service:
  - Inject 500ms network latency
  - Monitor service health metrics
  - Verify circuit breaker activation
  - Measure recovery time
  - Document findings
`, "qe-chaos-engineer")

// Load testing
Task("Performance load test", `
  Run load test simulating Black Friday traffic:
  - Ramp up to 10,000 concurrent users
  - Maintain load for 30 minutes
  - Monitor response times and error rates
  - Identify bottlenecks
  - Compare against SLAs
`, "qe-load-tester")

Chaos Experiments
1. Fault Injection
await chaosEngineer.injectFault({
  target: 'api-service',
  fault: {
    type: 'latency',
    parameters: {
      delay: '500ms',
      jitter: '100ms',
      percentage: 50
    }
  },
  duration: '5m',
  monitoring: {
    metrics: ['response_time', 'error_rate', 'throughput'],
    alerts: true
  },
  rollback: {
    automatic: true,
    trigger: 'error_rate > 10%'
  }
});

2. Load Testing
await loadTester.execute({
  scenario: 'peak-traffic',
  profile: {
    rampUp: '5m',
    steadyState: '30m',
    rampDown: '5m'
  },
  users: {
    initial: 100,
    target: 5000,
    pattern: 'linear'
  },
  assertions: {
    p95_latency: '<500ms',
    error_rate: '<1%',
    throughput: '>1000rps'
  }
});

3. Stress Testing
await loadTester.stressTest({
  endpoint: '/api/checkout',
  strategy: 'step-increase',
  steps: [100, 500, 1000, 2000, 5000],
  stepDuration: '5m',
  findBreakingPoint: true,
  monitoring: {
    resourceUtilization: true,
    databaseConnections: true,
    memoryUsage: true
  }
});

4. Resilience Validation
await resilienceTester.validate({
  scenarios: [
    'database-failover',
    'cache-failure',
    'external-service-timeout',
    'pod-termination'
  ],
  expectations: {
    gracefulDegradation: true,
    automaticRecovery: true,
    dataIntegrity: true,
    recoveryTime: '<30s'
  }
});

Fault Types
Fault	Description	Use Case
Latency	Add network delay	Test timeouts
Packet Loss	Drop network packets	Test retry logic
CPU Stress	Consume CPU	Test resource limits
Memory Pressure	Consume memory	Test OOM handling
Disk Full	Fill disk space	Test disk errors
Process Kill	Terminate process	Test recovery
Chaos Report
interface ChaosReport {
  experiment: {
    name: string;
    target: string;
    fault: FaultConfig;
    duration: number;
  };
  results: {
    hypothesis: string;
    validated: boolean;
    metrics: {
      before: MetricSnapshot;
      during: MetricSnapshot;
      after: MetricSnapshot;
    };
    events: ChaosEvent[];
    recovery: {
      detected: boolean;
      time: number;
      automatic: boolean;
    };
  };
  findings: {
    severity: 'critical' | 'high' | 'medium' | 'low';
    description: string;
    recommendation: string;
  }[];
  artifacts: {
    logs: string;
    metrics: string;
    traces: string;
  };
}

Safety Controls
safety:
  blast_radius:
    max_affected_pods: 1
    max_affected_percentage: 10

  abort_conditions:
    - error_rate > 50%
    - p99_latency > 10s
    - service_unavailable

  excluded_environments:
    - production-critical

  required_approvals:
    production: 2
    staging: 0

SLA Validation
await resilienceTester.validateSLA({
  slas: {
    availability: 99.9,
    p95_latency: 500,
    error_rate: 0.1
  },
  period: '30d',
  report: {
    breaches: true,
    trends: true,
    projections: true
  }
});

Coordination

Primary Agents: qe-chaos-engineer, qe-load-tester, qe-resilience-tester Coordinator: qe-chaos-coordinator Related Skills: qe-performance, security-testing

Weekly Installs
44
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn