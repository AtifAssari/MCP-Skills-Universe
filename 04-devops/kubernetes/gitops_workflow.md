---
rating: ⭐⭐⭐
title: gitops-workflow
url: https://skills.sh/wshobson/agents/gitops-workflow
---

# gitops-workflow

skills/wshobson/agents/gitops-workflow
gitops-workflow
Installation
$ npx skills add https://github.com/wshobson/agents --skill gitops-workflow
Summary

Declarative, Git-based continuous delivery for Kubernetes using ArgoCD or Flux CD.

Supports both ArgoCD and Flux CD with installation, configuration, and repository structure guidance for each
Covers core GitOps patterns including App of Apps, automated sync policies with pruning and self-healing, and progressive delivery strategies (canary, blue-green)
Includes secret management approaches using External Secrets Operator and Sealed Secrets to keep credentials out of Git
Provides sync policy configuration, troubleshooting commands, and ten best practices for production GitOps workflows
SKILL.md
GitOps Workflow

Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments.

Purpose

Implement declarative, Git-based continuous delivery for Kubernetes using ArgoCD or Flux CD, following OpenGitOps principles.

When to Use This Skill
Set up GitOps for Kubernetes clusters
Automate application deployments from Git
Implement progressive delivery strategies
Manage multi-cluster deployments
Configure automated sync policies
Set up secret management in GitOps
OpenGitOps Principles
Declarative - Entire system described declaratively
Versioned and Immutable - Desired state stored in Git
Pulled Automatically - Software agents pull desired state
Continuously Reconciled - Agents reconcile actual vs desired state
ArgoCD Setup
1. Installation
# Create namespace
kubectl create namespace argocd

# Install ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Get admin password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d


Reference: See references/argocd-setup.md for detailed setup

2. Repository Structure
gitops-repo/
├── apps/
│   ├── production/
│   │   ├── app1/
│   │   │   ├── kustomization.yaml
│   │   │   └── deployment.yaml
│   │   └── app2/
│   └── staging/
├── infrastructure/
│   ├── ingress-nginx/
│   ├── cert-manager/
│   └── monitoring/
└── argocd/
    ├── applications/
    └── projects/

3. Create Application
# argocd/applications/my-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/gitops-repo
    targetRevision: main
    path: apps/production/my-app
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true

4. App of Apps Pattern
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: applications
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/gitops-repo
    targetRevision: main
    path: argocd/applications
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
  syncPolicy:
    automated: {}

Flux CD Setup
1. Installation
# Install Flux CLI
curl -s https://fluxcd.io/install.sh | sudo bash

# Bootstrap Flux
flux bootstrap github \
  --owner=org \
  --repository=gitops-repo \
  --branch=main \
  --path=clusters/production \
  --personal

2. Create GitRepository
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: my-app
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/org/my-app
  ref:
    branch: main

3. Create Kustomization
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: my-app
  namespace: flux-system
spec:
  interval: 5m
  path: ./deploy
  prune: true
  sourceRef:
    kind: GitRepository
    name: my-app

Sync Policies
Auto-Sync Configuration

ArgoCD:

syncPolicy:
  automated:
    prune: true # Delete resources not in Git
    selfHeal: true # Reconcile manual changes
    allowEmpty: false
  retry:
    limit: 5
    backoff:
      duration: 5s
      factor: 2
      maxDuration: 3m


Flux:

spec:
  interval: 1m
  prune: true
  wait: true
  timeout: 5m


Reference: See references/sync-policies.md

Progressive Delivery
Canary Deployment with ArgoCD Rollouts
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: my-app
spec:
  replicas: 5
  strategy:
    canary:
      steps:
        - setWeight: 20
        - pause: { duration: 1m }
        - setWeight: 50
        - pause: { duration: 2m }
        - setWeight: 100

Blue-Green Deployment
strategy:
  blueGreen:
    activeService: my-app
    previewService: my-app-preview
    autoPromotionEnabled: false

Secret Management
External Secrets Operator
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: SecretStore
  target:
    name: db-credentials
  data:
    - secretKey: password
      remoteRef:
        key: prod/db/password

Sealed Secrets
# Encrypt secret
kubeseal --format yaml < secret.yaml > sealed-secret.yaml

# Commit sealed-secret.yaml to Git

Best Practices
Use separate repos or branches for different environments
Implement RBAC for Git repositories
Enable notifications for sync failures
Use health checks for custom resources
Implement approval gates for production
Keep secrets out of Git (use External Secrets)
Use App of Apps pattern for organization
Tag releases for easy rollback
Monitor sync status with alerts
Test changes in staging first
Troubleshooting

Sync failures:

argocd app get my-app
argocd app sync my-app --prune


Out of sync status:

argocd app diff my-app
argocd app sync my-app --force

Related Skills
k8s-manifest-generator - For creating manifests
helm-chart-scaffolding - For packaging applications
Weekly Installs
6.0K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn