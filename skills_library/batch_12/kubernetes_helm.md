---
title: kubernetes-helm
url: https://skills.sh/blogic-cz/blogic-marketplace/kubernetes-helm
---

# kubernetes-helm

skills/blogic-cz/blogic-marketplace/kubernetes-helm
kubernetes-helm
Installation
$ npx skills add https://github.com/blogic-cz/blogic-marketplace --skill kubernetes-helm
SKILL.md
Kubernetes & Helm Workflow

Apply consistent Helm patterns for test and production Kubernetes environments.

Use this skill when
Update Helm values files
Add or change environment variables
Configure resources, probes, ingress, security, jobs, or cronjobs
Work with Kubernetes secrets, namespaces, pods, and environment URLs
Follow this workflow
Locate the target chart in kubernetes/helm/ and edit both values.test.yaml and values.prod.yaml unless the change is environment-specific.
Add non-sensitive variables under extraEnvVars with direct value; keep entries alphabetically sorted.
Add sensitive variables with valueFrom.secretKeyRef; never inline secrets in values files.
Define hook/job secrets through the chart values key hooks.secretName (in values.*.yaml), then consume it in hook templates (for example migration/sync jobs).
If the repository uses local env files, mirror new variables in .env.example and .env with safe placeholder defaults.
Check chart-specific secret naming and namespace conventions before deploying.
Use k8s-tool for runtime checks only after prerequisites are met: k8s-tool is a project wrapper around kubectl with environment shortcuts, and requires an installed CLI plus valid kubeconfig/cluster access.
Reference material

Read concrete snippets and YAML examples in:

references/chart-structure.md
references/helm-examples.md
Key Rules
Keep extraEnvVars alphabetically sorted
Never commit secrets - use K8s secrets with secretKeyRef
Test values are conservative - lower resources than prod
Use appropriate probe paths - /api/alive for liveness, /api/health for readiness
CronJobs need concurrencyPolicy: Forbid to prevent overlapping
Weekly Installs
63
Repository
blogic-cz/blogi…ketplace
GitHub Stars
3
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass