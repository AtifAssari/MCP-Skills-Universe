---
rating: ⭐⭐⭐
title: chaos-engineer
url: https://skills.sh/jeffallan/claude-skills/chaos-engineer
---

# chaos-engineer

skills/jeffallan/claude-skills/chaos-engineer
chaos-engineer
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill chaos-engineer
Summary

Designs and executes chaos experiments with safety controls, runbooks, and resilience testing frameworks.

Covers full chaos workflow: system analysis, hypothesis-driven experiment design, controlled failure injection, and learning loops with documented improvements
Provides templates and reference guides for infrastructure chaos (servers, networks, zones), Kubernetes-native experiments (Litmus, Chaos Mesh), and game day exercises
Includes concrete examples using Litmus ChaosEngine, toxiproxy for network injection, and Chaos Monkey with blast radius controls and automated rollback procedures
Enforces safety constraints: steady-state verification, sub-30-second rollback paths, single-variable isolation, and production safeguards via circuit breakers or canaries
SKILL.md
Chaos Engineer
When to Use This Skill
Designing and executing chaos experiments
Implementing failure injection frameworks (Chaos Monkey, Litmus, etc.)
Planning and conducting game day exercises
Building blast radius controls and safety mechanisms
Setting up continuous chaos testing in CI/CD
Improving system resilience based on experiment findings
Core Workflow
System Analysis - Map architecture, dependencies, critical paths, and failure modes
Experiment Design - Define hypothesis, steady state, blast radius, and safety controls
Execute Chaos - Run controlled experiments with monitoring and quick rollback
Learn & Improve - Document findings, implement fixes, enhance monitoring
Automate - Integrate chaos testing into CI/CD for continuous resilience
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Experiments	references/experiment-design.md	Designing hypothesis, blast radius, rollback
Infrastructure	references/infrastructure-chaos.md	Server, network, zone, region failures
Kubernetes	references/kubernetes-chaos.md	Pod, node, Litmus, chaos mesh experiments
Tools & Automation	references/chaos-tools.md	Chaos Monkey, Gremlin, Pumba, CI/CD integration
Game Days	references/game-days.md	Planning, executing, learning from game days
Safety Checklist

Non-obvious constraints that must be enforced on every experiment:

Steady state first — define and verify baseline metrics before injecting any failure
Blast radius cap — start with the smallest possible impact scope; expand only after validation
Automated rollback ≤ 30 seconds — abort path must be scripted and tested before the experiment begins
Single variable — change only one failure condition at a time until behaviour is well understood
No production without safety nets — customer-facing environments require circuit breakers, feature flags, or canary isolation
Close the loop — every experiment must produce a written learning summary and at least one tracked improvement
Output Templates

When implementing chaos engineering, provide:

Experiment design document (hypothesis, metrics, blast radius)
Implementation code (failure injection scripts/manifests)
Monitoring setup and alert configuration
Rollback procedures and safety controls
Learning summary and improvement recommendations
Concrete Example: Pod Failure Experiment (Litmus Chaos)

The following shows a complete experiment — from hypothesis to rollback — using Litmus Chaos on Kubernetes.

Step 1 — Define steady state and apply the experiment
# Verify baseline: p99 latency < 200ms, error rate < 0.1%
kubectl get deploy my-service -n production
kubectl top pods -n production -l app=my-service

Step 2 — Create and apply a Litmus ChaosEngine manifest
# chaos-pod-delete.yaml
apiVersion: litmuschaos.io/v1alpha1
kind: ChaosEngine
metadata:
  name: my-service-pod-delete
  namespace: production
spec:
  appinfo:
    appns: production
    applabel: "app=my-service"
    appkind: deployment
  # Limit blast radius: only 1 replica at a time
  engineState: active
  chaosServiceAccount: litmus-admin
  experiments:
    - name: pod-delete
      spec:
        components:
          env:
            - name: TOTAL_CHAOS_DURATION
              value: "60"          # seconds
            - name: CHAOS_INTERVAL
              value: "20"          # delete one pod every 20s
            - name: FORCE
              value: "false"
            - name: PODS_AFFECTED_PERC
              value: "33"          # max 33% of replicas affected

# Apply the experiment
kubectl apply -f chaos-pod-delete.yaml

# Watch experiment status
kubectl describe chaosengine my-service-pod-delete -n production
kubectl get chaosresult my-service-pod-delete-pod-delete -n production -w

Step 3 — Monitor during the experiment
# Tail application logs for errors
kubectl logs -l app=my-service -n production --since=2m -f

# Check ChaosResult verdict when complete
kubectl get chaosresult my-service-pod-delete-pod-delete \
  -n production -o jsonpath='{.status.experimentStatus.verdict}'

Step 4 — Rollback / abort if steady state is violated
# Immediately stop the experiment
kubectl patch chaosengine my-service-pod-delete \
  -n production --type merge -p '{"spec":{"engineState":"stop"}}'

# Confirm all pods are healthy
kubectl rollout status deployment/my-service -n production

Concrete Example: Network Latency with toxiproxy
# Install toxiproxy CLI
brew install toxiproxy   # macOS; use the binary release on Linux

# Start toxiproxy server (runs alongside your service)
toxiproxy-server &

# Create a proxy for your downstream dependency
toxiproxy-cli create -l 0.0.0.0:22222 -u downstream-db:5432 db-proxy

# Inject 300ms latency with 10% jitter — blast radius: this proxy only
toxiproxy-cli toxic add db-proxy -t latency -a latency=300 -a jitter=30

# Run your load test / observe metrics here ...

# Remove the toxic to restore normal behaviour
toxiproxy-cli toxic remove db-proxy -n latency_downstream

Concrete Example: Chaos Monkey (Spinnaker / standalone)
# chaos-monkey-config.yml — restrict to a single ASG
deployment:
  enabled: true
  regionIndependence: false
chaos:
  enabled: true
  meanTimeBetweenKillsInWorkDays: 2
  minTimeBetweenKillsInWorkDays: 1
  grouping: APP           # kill one instance per app, not per cluster
  exceptions:
    - account: production
      region: us-east-1
      detail: "*-canary"  # never kill canary instances

# Apply and trigger a manual kill for testing
chaos-monkey --app my-service --account staging --dry-run false


Documentation

Weekly Installs
1.5K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn