---
title: kubernetes-security-policies
url: https://skills.sh/nickcrew/claude-ctx-plugin/kubernetes-security-policies
---

# kubernetes-security-policies

skills/nickcrew/claude-ctx-plugin/kubernetes-security-policies
kubernetes-security-policies
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill kubernetes-security-policies
SKILL.md
Kubernetes Security Policies

Comprehensive guidance for implementing security policies in Kubernetes clusters, covering Pod Security Standards, Network Policies, RBAC, Security Contexts, admission control, secrets management, and runtime security for production-grade hardened deployments.

When to Use This Skill
Implementing Pod Security Standards (PSS/PSA) across namespaces
Designing and enforcing Network Policies for micro-segmentation
Configuring RBAC with least-privilege access control
Setting Security Contexts for container hardening
Deploying admission controllers (OPA/Gatekeeper, Kyverno)
Managing secrets and sensitive data securely
Implementing image security and vulnerability scanning
Enforcing runtime security policies and threat detection
Meeting compliance requirements (CIS, NIST, PCI-DSS, SOC2)
Conducting security audits and hardening assessments
Core Security Concepts

Pod Security Standards (PSS): Three progressive security levels enforced via Pod Security Admission (PSA):

Privileged: Unrestricted (default)
Baseline: Prevents known privilege escalations
Restricted: Pod hardening best practices (production recommended)

Network Policies: Zero-trust micro-segmentation controlling pod-to-pod and pod-to-external traffic using label selectors and namespace isolation.

RBAC (Role-Based Access Control): Least-privilege access control using ServiceAccounts, Roles, RoleBindings for namespace-scoped permissions, and ClusterRoles for cluster-wide access.

Security Contexts: Container and pod-level security settings including user/group IDs, capabilities, seccomp profiles, and filesystem restrictions.

Admission Control: Policy enforcement at API admission time using OPA Gatekeeper (Rego) or Kyverno (YAML) to validate, mutate, or reject resources.

Secrets Management: External secret storage integration (Vault, AWS Secrets Manager, Sealed Secrets) instead of native Kubernetes secrets.

Image Security: Vulnerability scanning, signature verification, digest-based immutability, and private registry authentication.

Quick Reference
Task	Load reference
Pod Security Standards (PSS/PSA)	skills/kubernetes-security-policies/references/pod-security-standards.md
Network Policies	skills/kubernetes-security-policies/references/network-policies.md
RBAC (Roles, ServiceAccounts)	skills/kubernetes-security-policies/references/rbac.md
Security Contexts (capabilities, seccomp)	skills/kubernetes-security-policies/references/security-contexts.md
Admission Control (OPA, Kyverno)	skills/kubernetes-security-policies/references/admission-control.md
Secrets Management (Vault, ESO)	skills/kubernetes-security-policies/references/secrets-management.md
Image Security (scanning, signing)	skills/kubernetes-security-policies/references/image-security.md
Best Practices & Compliance	skills/kubernetes-security-policies/references/best-practices.md
Security Implementation Workflow
Phase 1: Baseline Assessment
Audit current security posture with kube-bench or kubescape
Identify gaps against CIS Kubernetes Benchmark
Document compliance requirements (PCI-DSS, NIST, SOC2)
Phase 2: Pod Security Standards
Enable PSA audit mode on all namespaces
Identify violations using kubectl get pods -A --show-labels
Remediate workloads to meet baseline/restricted standards
Progressively enforce: dev (warn) → staging (baseline) → prod (restricted)
Phase 3: Network Segmentation
Deploy default-deny NetworkPolicy to all namespaces
Create explicit allow rules for required traffic flows
Implement database isolation policies
Add monitoring/observability exceptions
Phase 4: Access Control (RBAC)
Audit existing RBAC with kubectl auth can-i --list
Create dedicated ServiceAccounts per application
Define least-privilege Roles with specific resource/verb restrictions
Disable automountServiceAccountToken by default
Minimize ClusterRole usage
Phase 5: Admission Control
Choose policy engine: OPA Gatekeeper (Rego) or Kyverno (YAML)
Implement validation policies: require labels, resource limits, non-root
Add mutation policies: inject security contexts, sidecar containers
Enforce image policies: disallow latest tag, require signatures
Phase 6: Secrets Management
Deploy External Secrets Operator or Vault integration
Migrate native Secrets to external secret stores
Enable encryption at rest for etcd
Implement secret rotation policies
Phase 7: Image Security
Integrate vulnerability scanning in CI/CD (Trivy, Snyk)
Implement image signing with Sigstore/Cosign
Enforce signature verification via admission control
Use immutable image digests instead of tags
Phase 8: Runtime Security
Deploy Falco for runtime threat detection
Enable Kubernetes audit logging
Configure alerts for security events
Implement intrusion detection policies
Common Mistakes

Pod Security:

Running containers as root (always set runAsNonRoot: true)
Using privileged containers (avoid unless absolutely necessary)
Writable root filesystem (set readOnlyRootFilesystem: true)
Missing resource limits (required for restricted PSS)

Network Policies:

No default-deny policy (unrestricted pod-to-pod traffic)
Overly permissive egress rules (allow all external traffic)
Forgetting DNS egress (pods can't resolve names)
Missing monitoring/observability exceptions

RBAC:

Overly broad ClusterRole permissions (violates least privilege)
Sharing ServiceAccounts across applications
Using * verbs or resources in Roles
Not auditing RBAC permissions regularly

Secrets:

Committing secrets to Git repositories
Using environment variables instead of mounted files
Relying on base64 encoding as encryption
No secret rotation policy

Admission Control:

Enforcing policies without audit phase first
Blocking kube-system namespace accidentally
No policy testing in staging environment
Missing exemptions for system components

Images:

Using latest tag (not immutable, breaks reproducibility)
No vulnerability scanning in CI/CD
Unsigned images in production
Large base images (use distroless or Alpine)
Resources
Pod Security Standards: https://kubernetes.io/docs/concepts/security/pod-security-standards/
Network Policies: https://kubernetes.io/docs/concepts/services-networking/network-policies/
RBAC: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
OPA Gatekeeper: https://open-policy-agent.github.io/gatekeeper/
Kyverno: https://kyverno.io/docs/
External Secrets Operator: https://external-secrets.io/
Falco Runtime Security: https://falco.org/docs/
CIS Benchmarks: https://www.cisecurity.org/benchmark/kubernetes
NSA/CISA Hardening Guide: https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF
Weekly Installs
58
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass