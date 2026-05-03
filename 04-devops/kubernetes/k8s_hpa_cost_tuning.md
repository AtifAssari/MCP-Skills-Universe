---
rating: ⭐⭐⭐
title: k8s-hpa-cost-tuning
url: https://skills.sh/microlinkhq/skills/k8s-hpa-cost-tuning
---

# k8s-hpa-cost-tuning

skills/microlinkhq/skills/k8s-hpa-cost-tuning
k8s-hpa-cost-tuning
Installation
$ npx skills add https://github.com/microlinkhq/skills --skill k8s-hpa-cost-tuning
SKILL.md
Kubernetes HPA Cost & Scale-Down Tuning
Mode selection (mandatory)

Declare a mode before executing this skill. All reasoning, thresholds, and recommendations depend on this choice.

mode = audit | incident


If no mode is provided, refuse to run and request clarification.

When to use
mode = audit — Periodic cost-savings audit

Run on a schedule (weekly or bi-weekly) to:

Detect over-reservation early
Validate that scale-down and node consolidation still work
Identify safe opportunities to reduce cluster cost

This mode assumes no active incident and prioritizes stability-preserving recommendations.

mode = incident — Post-incident scaling analysis

Run after a production incident or anomaly, attaching:

Production logs
HPA events
Scaling timelines

This mode focuses on:

Explaining why scaling behaved the way it did
Distinguishing traffic-driven vs configuration-driven incidents
Preventing recurrence without overcorrecting

This skill assumes Datadog for observability and standard Kubernetes HPA + Cluster Autoscaler.

Core mental model

Kubernetes scaling is a three-layer system:

HPA decides how many pods (based on usage / requests)
Scheduler decides where pods go (based on requests + constraints)
Cluster Autoscaler decides how many nodes exist (only when nodes can empty)

Cost optimization only works if all three layers can move downward.

Key takeaway: HPA decides quantity, scheduler decides placement, autoscaler decides cost. Scale-up can be aggressive; scale-down must be possible. If replicas drop but nodes do not, the scheduler is the bottleneck.

Key Datadog metrics

The utility scripts query three metric families:

CPU used % — real utilization (kubernetes.cpu.usage.total / node.cpu_allocatable)
CPU requested % — reserved on paper (kubernetes.cpu.requests / node.cpu_allocatable)
Memory used vs requests — HPA-relevant ratio

CPU requested % must go down after scale-down for cost savings to be real. If memory usage stays above target, memory drives scale-up even when CPU is idle.

Scale-down as a first-class cost control

When scale-down is slow or blocked:

Replicas plateau
Pods remain evenly spread
Nodes never empty
Cluster Autoscaler cannot remove nodes

Result: permanent over-reservation.

Recommended HPA scale-down policy
scaleDown:
  stabilizationWindowSeconds: 60
  selectPolicy: Max
  policies:
    - type: Percent
      value: 50
      periodSeconds: 30


Effects: fast reaction once load drops, predictable replica collapse, low flapping risk.

Topology spread: critical cost lever

Topology spread must never prevent pod consolidation during scale-down.

Strict constraints block scheduler flexibility and freeze cluster size.

Anti-pattern (breaks cost optimization)
maxSkew: 1
whenUnsatisfiable: DoNotSchedule


Pods cannot collapse onto fewer nodes. Nodes never drain. Reserved CPU/memory never decreases.

Recommended default (cost-safe)
topologySpreadConstraints:
- topologyKey: kubernetes.io/hostname
  maxSkew: 2
  whenUnsatisfiable: ScheduleAnyway


Strong preference for spreading while allowing bin-packing during scale-down and enabling node removal.

Strict isolation (AZ-level only)

When hard guarantees are required:

topologySpreadConstraints:
- topologyKey: topology.kubernetes.io/zone
  maxSkew: 1
  whenUnsatisfiable: DoNotSchedule


Do not combine this with strict hostname-level spread.

Anti-affinity as a soft alternative

To avoid hot nodes without blocking scale-down:

podAntiAffinity:
  preferredDuringSchedulingIgnoredDuringExecution:
  - weight: 100
    podAffinityTerm:
      topologyKey: kubernetes.io/hostname
      labelSelector:
        matchLabels:
          app: your-app


Anti-affinity is advisory and cost-safe.

Resource requests tuning
Over-requesting CPU = slower scale-down
Over-requesting memory = unexpected scale-ups

Practical defaults:

targetCPUUtilizationPercentage: 70
targetMemoryUtilizationPercentage: 75–80

Adjust one knob at a time.

Validation loop

Run weekly (or after changes):

Check HPA current/target values
Compare CPU used % vs CPU requested %
Observe replica collapse after load drops
Verify nodes drain and disappear
Re-check latency, errors, OOMs
Quick validation commands
kubectl -n <namespace> get hpa <deployment>
kubectl -n <namespace> describe hpa <deployment>
kubectl -n <namespace> top pod --containers
kubectl top node
kubectl -n <namespace> get pods -o wide | sort -k7

Utility scripts

Both scripts require Datadog credentials:

export DD_API_KEY=...
export DD_APP_KEY=...
export DD_SITE=datadoghq.com   # optional, defaults to datadoghq.com

audit-metrics.mjs — Cost-savings discovery

Scan a cluster over a wide window (default 24 h) to find over-reservation and waste.

# Cluster-wide audit
node scripts/audit-metrics.mjs --cluster <cluster>

# With deployment deep-dive
node scripts/audit-metrics.mjs \
  --cluster <cluster> \
  --namespace <namespace> \
  --deployment <deployment>


Reports:

Cluster: CPU/memory used %, requested %, and waste % (requested minus used)
Deployment (when provided): CPU/memory usage vs requests, HPA replica range
Savings opportunities: actionable recommendations based on thresholds
incident-metrics.mjs — Post-incident analysis

Collect metrics for a narrow incident window and get a tuning recommendation.

node scripts/incident-metrics.mjs \
  --cluster <cluster> \
  --namespace <namespace> \
  --deployment <deployment> \
  --from <ISO8601> \
  --to <ISO8601>


Reports:

Cluster: CPU used % and requested % of allocatable
Deployment: CPU/memory usage vs requests, unavailable %
HPA: current / desired / max replicas
Capacity planning: required allocatable cores for 80 % and 70 % reservation ceilings
Tuning order: step-by-step recommendation (one knob at a time)
Interpretation notes
Keep limits.memory unchanged unless OOMKills or near-limit memory usage are confirmed
Use --out <path> to save full JSON for deeper analysis or diffing across runs
Run --help on either script for all options (relative windows, custom HPA name, pretty JSON)
Weekly Installs
30
Repository
microlinkhq/skills
GitHub Stars
1
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass