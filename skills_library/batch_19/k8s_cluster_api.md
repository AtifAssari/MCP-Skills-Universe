---
title: k8s-cluster-api
url: https://skills.sh/itechmeat/llm-code/k8s-cluster-api
---

# k8s-cluster-api

skills/itechmeat/llm-code/k8s-cluster-api
k8s-cluster-api
Installation
$ npx skills add https://github.com/itechmeat/llm-code --skill k8s-cluster-api
SKILL.md
Kubernetes Cluster API

Kubernetes Cluster API (CAPI) is a Kubernetes sub-project focused on providing declarative APIs and tooling to simplify provisioning, upgrading, and operating multiple Kubernetes clusters.

Overview

Started by SIG Cluster Lifecycle, Cluster API uses Kubernetes-style APIs and patterns to automate cluster lifecycle management. The infrastructure (VMs, networks, load balancers, VPCs) and Kubernetes configuration are defined declaratively, enabling consistent and repeatable cluster deployments across environments.

Why Cluster API?

While kubeadm reduces installation complexity, it doesn't address day-to-day cluster management:

How to consistently provision infrastructure across providers and locations?
How to automate cluster lifecycle (upgrades, deletion)?
How to scale processes to manage any number of clusters?

Cluster API addresses these gaps with declarative, Kubernetes-style APIs that automate cluster creation, configuration, and management.

Goals
Manage lifecycle (create, scale, upgrade, destroy) of Kubernetes-conformant clusters via declarative API
Work in different environments (on-premises and cloud)
Define common operations with swappable implementations
Reuse existing ecosystem components (cluster-autoscaler, node-problem-detector)
Provide transition path for existing tools to adopt incrementally
Non-Goals
Add APIs to Kubernetes core
Manage infrastructure unrelated to Kubernetes clusters
Force all lifecycle products to use these APIs
Manage non-CAPI provisioned clusters
Manage single cluster spanning multiple providers
Configure machines after create/upgrade
Quick Navigation
Topic	Reference
Getting Started	getting-started.md
Concepts & Architecture	concepts.md
Certificates	certificates.md
Bootstrap (Kubeadm/MicroK8s)	bootstrap.md
Cluster Operations	cluster-operations.md
Experimental Features	experimental.md
clusterctl CLI	clusterctl.md
Developer Guide	developer.md
Troubleshooting	troubleshooting.md
API Reference & Providers	api-reference.md
Security & PSS	security.md
Controllers	controllers.md
Version Migrations	migrations.md
FAQ	faq.md
Best Practices	best-practices.md
When to Use
Provisioning Kubernetes clusters across multiple infrastructure providers
Managing cluster lifecycle (create, scale, upgrade, destroy)
Automating cluster operations with declarative APIs
Implementing GitOps workflows for cluster management
Building custom infrastructure providers
Core Concepts
Architecture
┌─────────────────────────────────────────┐
│         Management Cluster              │
│  ┌─────────────┐  ┌─────────────────┐   │
│  │ CAPI Core   │  │ Infrastructure  │   │
│  │ Controllers │  │ Provider        │   │
│  └─────────────┘  └─────────────────┘   │
│  ┌─────────────┐  ┌─────────────────┐   │
│  │  Bootstrap  │  │  Control Plane  │   │
│  │  Provider   │  │  Provider       │   │
│  └─────────────┘  └─────────────────┘   │
└─────────────────────┬───────────────────┘
                      │ manages
          ┌───────────┴───────────┐
          ▼                       ▼
┌─────────────────┐     ┌─────────────────┐
│ Workload        │     │ Workload        │
│ Cluster 1       │     │ Cluster N       │
└─────────────────┘     └─────────────────┘

Key Components
Component	Purpose
Management Cluster	Hosts CAPI controllers, manages workloads
Workload Cluster	User clusters managed by CAPI
Infrastructure Provider	Provisions VMs, networks, load balancers
Bootstrap Provider	Generates cloud-init/ignition configs
Control Plane Provider	Manages control plane nodes lifecycle
Core Resources
Resource	Description
Cluster	Represents a Kubernetes cluster
Machine	Represents a single node/VM
MachineSet	Manages replicas of Machines
MachineDeployment	Declarative updates for MachineSets
MachineHealthCheck	Automatic remediation of unhealthy nodes
Quick Start
# Install clusterctl
curl -L https://github.com/kubernetes-sigs/cluster-api/releases/download/v1.12.0/clusterctl-linux-amd64 -o clusterctl
chmod +x clusterctl
sudo mv clusterctl /usr/local/bin/

# Initialize management cluster
clusterctl init --infrastructure docker

# Create workload cluster
clusterctl generate cluster my-cluster --kubernetes-version v1.32.0 --control-plane-machine-count 1 --worker-machine-count 3 | kubectl apply -f -

# Get cluster kubeconfig
clusterctl get kubeconfig my-cluster > my-cluster.kubeconfig

# Delete cluster
kubectl delete cluster my-cluster

Common Workflows
Cluster Lifecycle
# Create cluster from template
clusterctl generate cluster prod-cluster \
  --infrastructure aws \
  --kubernetes-version v1.32.0 \
  --control-plane-machine-count 3 \
  --worker-machine-count 5 \
  | kubectl apply -f -

# Scale workers
kubectl scale machinedeployment prod-cluster-md-0 --replicas=10

# Upgrade Kubernetes version
kubectl patch cluster prod-cluster --type merge -p '{"spec":{"topology":{"version":"v1.33.0"}}}'

# Move cluster to new management cluster
clusterctl move --to-kubeconfig target-mgmt.kubeconfig

Health Monitoring
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineHealthCheck
metadata:
  name: my-cluster-mhc
spec:
  clusterName: my-cluster
  maxUnhealthy: 40%
  nodeStartupTimeout: 10m
  selector:
    matchLabels:
      cluster.x-k8s.io/cluster-name: my-cluster
  unhealthyConditions:
    - type: Ready
      status: "False"
      timeout: 5m
    - type: Ready
      status: Unknown
      timeout: 5m

Critical Prohibitions
Do NOT modify management cluster directly without proper backup
Do NOT delete Machine objects directly (use MachineDeployment scale)
Do NOT mix provider versions without checking compatibility
Do NOT skip cluster upgrade steps (control plane before workers)
Do NOT ignore MachineHealthCheck alerts
Scripts

Go-based tools in scripts/. Run via go run ./tool-name from the scripts directory.

Tool	Purpose
validate-manifests	Validate YAML manifests against CRD schemas
run-clusterctl-diagnose	Run clusterctl describe and save diagnostic report
migration-checker	Check v1beta1→v1beta2 migration readiness
check-cluster-health	Analyze conditions across all cluster objects
analyze-conditions	Parse and report False/Unknown conditions
scaffold-provider	Generate new provider directory structure
generate-cluster-template	Generate templates from ClusterClass
export-cluster-state	Export cluster state for backup/move
audit-security	Check PSS compliance and security posture
timeline-events	Build provisioning event timeline
compare-versions	Compare CAPI version specs and API changes
check-provider-contract	Verify provider CRD compliance with contracts
lint-cluster-templates	Lint and validate CAPI manifests
Assets

Reusable templates in assets/:

Cluster templates: cluster-minimal.yaml, cluster-production.yaml, cluster-clusterclass.yaml, clusterclass-example.yaml
Provider configs: docker-quickstart.yaml, aws-credentials.yaml, azure-credentials.yaml, provider-matrix.md
Operations: upgrade-checklist.md, migration-v1beta2.md, troubleshooting-flow.md, security-audit-report.md, dr-backup-restore.md, etcd-backup.yaml
GitOps: argocd-cluster-app.yaml, flux-kustomization.yaml, gitops-rbac.yaml
Monitoring: prometheus-alerts.yaml
Links
Documentation
GitHub
Releases
Weekly Installs
26
Repository
itechmeat/llm-code
GitHub Stars
15
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn