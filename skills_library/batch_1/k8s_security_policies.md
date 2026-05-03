---
title: k8s-security-policies
url: https://skills.sh/wshobson/agents/k8s-security-policies
---

# k8s-security-policies

skills/wshobson/agents/k8s-security-policies
k8s-security-policies
Installation
$ npx skills add https://github.com/wshobson/agents --skill k8s-security-policies
Summary

Defense-in-depth Kubernetes security through network policies, pod security standards, RBAC, and admission control.

Covers three pod security levels (Privileged, Baseline, Restricted) enforced via namespace labels for graduated security posture
Provides NetworkPolicy templates for default-deny, service-to-service communication, and DNS egress patterns
Includes RBAC configuration examples for roles, cluster roles, and bindings to implement least-privilege access
Demonstrates OPA Gatekeeper constraint templates and Istio mTLS/AuthorizationPolicy for policy enforcement and service mesh security
References CIS Kubernetes Benchmark and NIST Cybersecurity Framework compliance patterns with troubleshooting commands for NetworkPolicy and RBAC validation
SKILL.md
Kubernetes Security Policies

Comprehensive guide for implementing NetworkPolicy, PodSecurityPolicy, RBAC, and Pod Security Standards in Kubernetes.

Purpose

Implement defense-in-depth security for Kubernetes clusters using network policies, pod security standards, and RBAC.

When to Use This Skill
Implement network segmentation
Configure pod security standards
Set up RBAC for least-privilege access
Create security policies for compliance
Implement admission control
Secure multi-tenant clusters
Pod Security Standards
1. Privileged (Unrestricted)
apiVersion: v1
kind: Namespace
metadata:
  name: privileged-ns
  labels:
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/warn: privileged

2. Baseline (Minimally restrictive)
apiVersion: v1
kind: Namespace
metadata:
  name: baseline-ns
  labels:
    pod-security.kubernetes.io/enforce: baseline
    pod-security.kubernetes.io/audit: baseline
    pod-security.kubernetes.io/warn: baseline

3. Restricted (Most restrictive)
apiVersion: v1
kind: Namespace
metadata:
  name: restricted-ns
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted

Network Policies
Default Deny All
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress

Allow Frontend to Backend
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080

Allow DNS
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Egress
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              name: kube-system
      ports:
        - protocol: UDP
          port: 53


Reference: See assets/network-policy-template.yaml

RBAC Configuration
Role (Namespace-scoped)
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: production
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "watch", "list"]

ClusterRole (Cluster-wide)
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get", "watch", "list"]

RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: production
subjects:
  - kind: User
    name: jane
    apiGroup: rbac.authorization.k8s.io
  - kind: ServiceAccount
    name: default
    namespace: production
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io


Reference: See references/rbac-patterns.md

Pod Security Context
Restricted Pod
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: myapp:1.0
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL

Policy Enforcement with OPA Gatekeeper
ConstraintTemplate
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequiredlabels
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredLabels
      validation:
        openAPIV3Schema:
          type: object
          properties:
            labels:
              type: array
              items:
                type: string
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequiredlabels
        violation[{"msg": msg, "details": {"missing_labels": missing}}] {
          provided := {label | input.review.object.metadata.labels[label]}
          required := {label | label := input.parameters.labels[_]}
          missing := required - provided
          count(missing) > 0
          msg := sprintf("missing required labels: %v", [missing])
        }

Constraint
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredLabels
metadata:
  name: require-app-label
spec:
  match:
    kinds:
      - apiGroups: ["apps"]
        kinds: ["Deployment"]
  parameters:
    labels: ["app", "environment"]

Service Mesh Security (Istio)
PeerAuthentication (mTLS)
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: STRICT

AuthorizationPolicy
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-frontend
  namespace: production
spec:
  selector:
    matchLabels:
      app: backend
  action: ALLOW
  rules:
    - from:
        - source:
            principals: ["cluster.local/ns/production/sa/frontend"]

Best Practices
Implement Pod Security Standards at namespace level
Use Network Policies for network segmentation
Apply least-privilege RBAC for all service accounts
Enable admission control (OPA Gatekeeper/Kyverno)
Run containers as non-root
Use read-only root filesystem
Drop all capabilities unless needed
Implement resource quotas and limit ranges
Enable audit logging for security events
Regular security scanning of images
Compliance Frameworks
CIS Kubernetes Benchmark
Use RBAC authorization
Enable audit logging
Use Pod Security Standards
Configure network policies
Implement secrets encryption at rest
Enable node authentication
NIST Cybersecurity Framework
Implement defense in depth
Use network segmentation
Configure security monitoring
Implement access controls
Enable logging and monitoring
Troubleshooting

NetworkPolicy not working:

# Check if CNI supports NetworkPolicy
kubectl get nodes -o wide
kubectl describe networkpolicy <name>


RBAC permission denied:

# Check effective permissions
kubectl auth can-i list pods --as system:serviceaccount:default:my-sa
kubectl auth can-i '*' '*' --as system:serviceaccount:default:my-sa

Related Skills
k8s-manifest-generator - For creating secure manifests
gitops-workflow - For automated policy deployment
Weekly Installs
9.1K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass