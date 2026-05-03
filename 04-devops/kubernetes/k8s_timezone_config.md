---
rating: ⭐⭐⭐
title: k8s-timezone-config
url: https://skills.sh/julianobarbosa/claude-code-skills/k8s-timezone-config
---

# k8s-timezone-config

skills/julianobarbosa/claude-code-skills/k8s-timezone-config
k8s-timezone-config
Installation
$ npx skills add https://github.com/julianobarbosa/claude-code-skills --skill k8s-timezone-config
SKILL.md
Kubernetes Pod Timezone Configuration

Standard timezone for Hypera infrastructure: America/Sao_Paulo

Problem

Kubernetes pods run in UTC by default. Logs and application timestamps show +0000 offset instead of local Brazil time (-0300).

Solution

Add the TZ environment variable to container specifications.

Implementation Patterns
1. Helm Values (extraEnv pattern)

For Helm charts that support extraEnv:

# In values.yaml
extraEnv:
  - name: TZ
    value: America/Sao_Paulo

2. Multiple Containers

When a deployment has multiple containers (e.g., API server + frontend), add TZ to ALL containers:

apiServer:
  extraEnv:
    - name: TZ
      value: America/Sao_Paulo

frontend:
  extraEnv:
    - name: TZ
      value: America/Sao_Paulo

3. Raw Kubernetes Deployment
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
        - name: app
          env:
            - name: TZ
              value: America/Sao_Paulo

4. StatefulSet
apiVersion: apps/v1
kind: StatefulSet
spec:
  template:
    spec:
      containers:
        - name: app
          env:
            - name: TZ
              value: America/Sao_Paulo

Verification

After deployment, verify timezone is set correctly:

# Check pod logs for timestamp offset
# Before: 2026-01-13T11:37:06 +0000
# After:  2026-01-13T08:37:06 -0300

# Or exec into pod
kubectl exec -it <pod-name> -n <namespace> -- date
# Should show: Mon Jan 13 08:37:06 -03 2026

Common Applications Requiring Timezone
Application	Config Location	Notes
Dependency-Track	apiServer.extraEnv + frontend.extraEnv	Both containers need TZ
Grafana	env or extraEnvVars	Single container
Loki	extraEnv	Affects log timestamps
Prometheus	server.env	Affects alert timestamps
DefectDojo	extraEnv	Django app
PostgreSQL	primary.extraEnvVars	Database timestamps
Important Notes
Restart required: Pods must restart for TZ changes to take effect
All containers: Set TZ on ALL containers in a pod, including sidecars
Init containers: Also set TZ on init containers if they log timestamps
Cron jobs: Kubernetes CronJob schedules are always UTC - TZ only affects container-level time
Hypera GitOps Workflow
Edit values.yaml in argo-cd-helm-values/kube-addons/<service>/<cluster>/values.yaml
Add TZ environment variable to all containers
Commit and push (ArgoCD auto-syncs)
Verify pods restart with new timezone
Reference
IANA Timezone Database: America/Sao_Paulo = UTC-3 (no DST since 2019)
Linux TZ variable: Uses /usr/share/zoneinfo/America/Sao_Paulo
Weekly Installs
38
Repository
julianobarbosa/…e-skills
GitHub Stars
64
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass