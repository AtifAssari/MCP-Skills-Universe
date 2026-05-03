---
title: k8s-security
url: https://skills.sh/eyadsibai/ltk/k8s-security
---

# k8s-security

skills/eyadsibai/ltk/k8s-security
k8s-security
Installation
$ npx skills add https://github.com/eyadsibai/ltk --skill k8s-security
SKILL.md
Kubernetes Security Policies

Implement defense-in-depth security for Kubernetes clusters.

Pod Security Standards
Restricted (Most Secure)
apiVersion: v1
kind: Namespace
metadata:
  name: restricted-ns
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted

Secure Pod Configuration
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

Network Policies
Default Deny All
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
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
spec:
  podSelector:
    matchLabels:
      app: backend
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080

Allow DNS Egress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns
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

RBAC Configuration
Role (Namespace-scoped)
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]

RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
subjects:
- kind: ServiceAccount
  name: my-app
  namespace: production
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io

OPA Gatekeeper Policies
Required Labels Constraint
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequiredlabels
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredLabels
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequiredlabels
        violation[{"msg": msg}] {
          provided := {label | input.review.object.metadata.labels[label]}
          required := {label | label := input.parameters.labels[_]}
          missing := required - provided
          count(missing) > 0
          msg := sprintf("missing labels: %v", [missing])
        }

Service Mesh Security (Istio)
Strict mTLS
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
spec:
  mtls:
    mode: STRICT

Best Practices
Pod Security Standards at namespace level
Network Policies for segmentation
Least-privilege RBAC for all service accounts
Run containers as non-root
Read-only root filesystem
Drop all capabilities unless needed
Enable audit logging
Regular image scanning
Troubleshooting
# Check RBAC permissions
kubectl auth can-i list pods --as system:serviceaccount:default:my-sa

# Debug NetworkPolicy
kubectl describe networkpolicy <name>
kubectl get networkpolicy -A

Weekly Installs
42
Repository
eyadsibai/ltk
GitHub Stars
4
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass