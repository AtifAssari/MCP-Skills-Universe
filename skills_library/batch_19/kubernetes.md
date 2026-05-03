---
title: kubernetes
url: https://skills.sh/bobmatnyc/claude-mpm-skills/kubernetes
---

# kubernetes

skills/bobmatnyc/claude-mpm-skills/kubernetes
kubernetes
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill kubernetes
SKILL.md
Kubernetes
Quick Start (kubectl)
kubectl describe pod/<pod> -n <ns>
kubectl get events -n <ns> --sort-by=.lastTimestamp | tail -n 30
kubectl logs pod/<pod> -n <ns> --previous --tail=200

Production Minimums
Health: readinessProbe and startupProbe for safe rollouts
Resources: set requests/limits to prevent noisy-neighbor failures
Security: run as non-root and grant least privilege
Load Next (References)
references/core-objects.md — choose the right workload/controller and service type
references/rollouts-and-probes.md — probes, rollouts, graceful shutdown, rollback
references/debugging-runbook.md — common failure modes and a fast triage flow
references/security-hardening.md — pod security, RBAC, network policy, supply chain
Weekly Installs
183
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass