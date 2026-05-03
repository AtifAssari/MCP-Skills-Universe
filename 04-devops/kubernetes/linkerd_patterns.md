---
rating: ⭐⭐⭐
title: linkerd-patterns
url: https://skills.sh/wshobson/agents/linkerd-patterns
---

# linkerd-patterns

skills/wshobson/agents/linkerd-patterns
linkerd-patterns
Installation
$ npx skills add https://github.com/wshobson/agents --skill linkerd-patterns
Summary

Lightweight service mesh patterns for Kubernetes with automatic mTLS and zero-trust networking.

Covers installation, namespace injection, and core resources including ServiceProfile for per-route metrics, TrafficSplit for canary deployments, and Server/ServerAuthorization policies for access control
Includes templates for mesh setup, traffic splitting, retry configuration with budgets, multi-cluster linking, and HTTPRoute-based advanced routing
Provides monitoring and debugging commands for live traffic inspection, proxy status checks, and cross-cluster connectivity verification
Emphasizes automatic mTLS, sensible defaults, and per-route observability without requiring complex configuration
SKILL.md
Linkerd Patterns

Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes.

When to Use This Skill
Setting up a lightweight service mesh
Implementing automatic mTLS
Configuring traffic splits for canary deployments
Setting up service profiles for per-route metrics
Implementing retries and timeouts
Multi-cluster service mesh
Core Concepts
1. Linkerd Architecture
┌─────────────────────────────────────────────┐
│                Control Plane                 │
│  ┌─────────┐ ┌──────────┐ ┌──────────────┐ │
│  │ destiny │ │ identity │ │ proxy-inject │ │
│  └─────────┘ └──────────┘ └──────────────┘ │
└─────────────────────────────────────────────┘
                      │
┌─────────────────────────────────────────────┐
│                 Data Plane                   │
│  ┌─────┐    ┌─────┐    ┌─────┐             │
│  │proxy│────│proxy│────│proxy│             │
│  └─────┘    └─────┘    └─────┘             │
│     │           │           │               │
│  ┌──┴──┐    ┌──┴──┐    ┌──┴──┐            │
│  │ app │    │ app │    │ app │            │
│  └─────┘    └─────┘    └─────┘            │
└─────────────────────────────────────────────┘

2. Key Resources
Resource	Purpose
ServiceProfile	Per-route metrics, retries, timeouts
TrafficSplit	Canary deployments, A/B testing
Server	Define server-side policies
ServerAuthorization	Access control policies
Templates
Template 1: Mesh Installation
# Install CLI
curl --proto '=https' --tlsv1.2 -sSfL https://run.linkerd.io/install | sh

# Validate cluster
linkerd check --pre

# Install CRDs
linkerd install --crds | kubectl apply -f -

# Install control plane
linkerd install | kubectl apply -f -

# Verify installation
linkerd check

# Install viz extension (optional)
linkerd viz install | kubectl apply -f -

Template 2: Inject Namespace
# Automatic injection for namespace
apiVersion: v1
kind: Namespace
metadata:
  name: my-app
  annotations:
    linkerd.io/inject: enabled
---
# Or inject specific deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  annotations:
    linkerd.io/inject: enabled
spec:
  template:
    metadata:
      annotations:
        linkerd.io/inject: enabled

Template 3: Service Profile with Retries
apiVersion: linkerd.io/v1alpha2
kind: ServiceProfile
metadata:
  name: my-service.my-namespace.svc.cluster.local
  namespace: my-namespace
spec:
  routes:
    - name: GET /api/users
      condition:
        method: GET
        pathRegex: /api/users
      responseClasses:
        - condition:
            status:
              min: 500
              max: 599
          isFailure: true
      isRetryable: true
    - name: POST /api/users
      condition:
        method: POST
        pathRegex: /api/users
      # POST not retryable by default
      isRetryable: false
    - name: GET /api/users/{id}
      condition:
        method: GET
        pathRegex: /api/users/[^/]+
      timeout: 5s
      isRetryable: true
  retryBudget:
    retryRatio: 0.2
    minRetriesPerSecond: 10
    ttl: 10s

Template 4: Traffic Split (Canary)
apiVersion: split.smi-spec.io/v1alpha1
kind: TrafficSplit
metadata:
  name: my-service-canary
  namespace: my-namespace
spec:
  service: my-service
  backends:
    - service: my-service-stable
      weight: 900m # 90%
    - service: my-service-canary
      weight: 100m # 10%

Template 5: Server Authorization Policy
# Define the server
apiVersion: policy.linkerd.io/v1beta1
kind: Server
metadata:
  name: my-service-http
  namespace: my-namespace
spec:
  podSelector:
    matchLabels:
      app: my-service
  port: http
  proxyProtocol: HTTP/1
---
# Allow traffic from specific clients
apiVersion: policy.linkerd.io/v1beta1
kind: ServerAuthorization
metadata:
  name: allow-frontend
  namespace: my-namespace
spec:
  server:
    name: my-service-http
  client:
    meshTLS:
      serviceAccounts:
        - name: frontend
          namespace: my-namespace
---
# Allow unauthenticated traffic (e.g., from ingress)
apiVersion: policy.linkerd.io/v1beta1
kind: ServerAuthorization
metadata:
  name: allow-ingress
  namespace: my-namespace
spec:
  server:
    name: my-service-http
  client:
    unauthenticated: true
    networks:
      - cidr: 10.0.0.0/8

Template 6: HTTPRoute for Advanced Routing
apiVersion: policy.linkerd.io/v1beta2
kind: HTTPRoute
metadata:
  name: my-route
  namespace: my-namespace
spec:
  parentRefs:
    - name: my-service
      kind: Service
      group: core
      port: 8080
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/v2
        - headers:
            - name: x-api-version
              value: v2
      backendRefs:
        - name: my-service-v2
          port: 8080
    - matches:
        - path:
            type: PathPrefix
            value: /api
      backendRefs:
        - name: my-service-v1
          port: 8080

Template 7: Multi-cluster Setup
# On each cluster, install with cluster credentials
linkerd multicluster install | kubectl apply -f -

# Link clusters
linkerd multicluster link --cluster-name west \
  --api-server-address https://west.example.com:6443 \
  | kubectl apply -f -

# Export a service to other clusters
kubectl label svc/my-service mirror.linkerd.io/exported=true

# Verify cross-cluster connectivity
linkerd multicluster check
linkerd multicluster gateways

Monitoring Commands
# Live traffic view
linkerd viz top deploy/my-app

# Per-route metrics
linkerd viz routes deploy/my-app

# Check proxy status
linkerd viz stat deploy -n my-namespace

# View service dependencies
linkerd viz edges deploy -n my-namespace

# Dashboard
linkerd viz dashboard

Debugging
# Check injection status
linkerd check --proxy -n my-namespace

# View proxy logs
kubectl logs deploy/my-app -c linkerd-proxy

# Debug identity/TLS
linkerd identity -n my-namespace

# Tap traffic (live)
linkerd viz tap deploy/my-app --to deploy/my-backend

Best Practices
Do's
Enable mTLS everywhere - It's automatic with Linkerd
Use ServiceProfiles - Get per-route metrics and retries
Set retry budgets - Prevent retry storms
Monitor golden metrics - Success rate, latency, throughput
Don'ts
Don't skip check - Always run linkerd check after changes
Don't over-configure - Linkerd defaults are sensible
Don't ignore ServiceProfiles - They unlock advanced features
Don't forget timeouts - Set appropriate values per route
Weekly Installs
5.3K
Repository
wshobson/agents
GitHub Stars
34.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn