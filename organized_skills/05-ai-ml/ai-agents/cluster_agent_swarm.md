---
rating: ⭐⭐⭐
title: cluster-agent-swarm
url: https://skills.sh/kcns008/cluster-agent-swarm-skills/cluster-agent-swarm
---

# cluster-agent-swarm

skills/kcns008/cluster-agent-swarm-skills/cluster-agent-swarm
cluster-agent-swarm
Installation
$ npx skills add https://github.com/kcns008/cluster-agent-swarm-skills --skill cluster-agent-swarm
SKILL.md
Cluster Agent Swarm — Complete Platform Operations
Runtime Requirements

This skill package provides Kubernetes/OpenShift cluster management capabilities. Credentials are modular - only configure what you need for your specific use case.

Always Required
Requirement	Description	Environment Variable
Kubeconfig	Valid kubeconfig with cluster access	KUBECONFIG or ~/.kube/config
kubectl	Kubernetes CLI	Must be in PATH
Conditional - Enable Only As Needed
Platform	Enable If...	Credentials
AWS/EKS/ROSA	Managing AWS-hosted Kubernetes	AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
Azure/ARO	Managing Azure-hosted Kubernetes	AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID
GCP/GKE	Managing GCP-hosted Kubernetes	GOOGLE_APPLICATION_CREDENTIALS
ArgoCD	Using GitOps agent	ARGOCD_AUTH_TOKEN, ARGOCD_SERVER
Vault	Using secrets management	VAULT_TOKEN
GitHub	Pushing to git repositories	GITHUB_TOKEN
Session Setup

Before using the agents, you MUST set up a session context:

# Set up session context for your environment
bash skills/orchestrator/scripts/setup-session.sh <environment> [context-name]

# Environments: dev, qa, staging, prod
# Note: prod requires human approval for all modifications

Security Considerations
Agents operate with least privilege by default
All credential access is logged
Production modifications require human approval
Secrets are never logged or stored in code
Security Assessment - Read Before Installing
Source Verification
This skill pulls code from a third-party GitHub repository
Verify the source URL before installing: https://github.com/kcns008/cluster-agent-swarm-skills
Pin to a specific version - never use main branch in production:
git clone https://github.com/kcns008/cluster-agent-swarm-skills.git
cd cluster-agent-swarm-skills
git fetch --tags
git checkout v1.0.0  # Use verified release tag or commit hash

Third-Party Script Execution Warning
This is a scripted skill - it will write executable bash scripts to disk
Scripts perform cluster operations including: deployments, scaling, scanning, configuration
Some scripts can be destructive - review before running:
Scripts with -delete, -cleanup in name may remove resources
Scripts with -promote, -deploy modify cluster state
Always test in non-production first
Install Mechanism
Installing via npx skills add downloads and executes code from GitHub
The skill cannot verify integrity of external scripts
Audit all scripts locally before running in production
Consider maintaining a verified, offline copy of trusted scripts
ALWAYS PIN TO VERIFIED COMMIT HASH for production - NEVER use floating URLs like tree/main or untagged branches
Use manual git clone with verified checkout for highest security
Persistence & Blast Radius
Agents maintain persistent state across sessions via:
WORKING.md - session progress tracking
LOGS.md - action audit trail
MEMORY.md - long-term learnings
Agents are configured to commit changes to these files as part of normal operation
This persistence increases blast radius if misused - limit repository write access if concerned
Human Approval Enforcement
The skill documentation claims human approval required for production changes
This is a procedural control, NOT a technical enforcement
Your platform MUST enforce an approval gate before allowing production operations
Do not rely on agent self-restriction for production safety
Principle of Least Privilege - Required
DO NOT provide owner/root-level cloud credentials
Create dedicated, minimal-permission service accounts for:
Kubernetes namespace-level access (not cluster-admin)
AWS IAM roles with limited EKS permissions
Azure service principals with limited subscription access
GCP service accounts with limited project permissions
Never provide production credentials until you have audited the code in non-production
Sandbox Before Production
Run this skill in an isolated/non-production environment first
Manually step through scripts to understand their behavior
Pay special attention to:
*-cleanup.sh scripts - may delete resources
*-promote.sh scripts - may promote artifacts
*-delete.sh scripts - explicitly destructive
Verify no unexpected network calls to external endpoints
Supply Chain Tools
Scripts may download binaries (syft, cosign, trivy, etc.)
Only allow downloads from trusted release sources (official GitHub releases, package managers)
Consider curating offline toolchains if your environment requires it
Additional Documentation
OPERATIONAL_RISKS.md - Complete documentation of operational risks, inconsistencies, and mitigations
SECURITY.md - Security policy, external dependencies, and verification requirements

This is the complete cluster-agent-swarm skill package. When you add this skill, you get access to ALL 7 specialized agents working together as a coordinated swarm.

Installation
Security Warning - Read Before Installing

⚠️ CRITICAL SECURITY WARNING

The installation commands below use GitHub URLs that fetch and execute code on your system. This is a supply chain risk - you must verify the repository and commit before use.

For production deployments:

ALWAYS pin to a specific, verified commit hash
Review the commit: git show <commit-hash>
Verify GPG signatures if available: git verify-commit <commit-hash>
Use the manual clone method below for highest security

NEVER use floating URLs (tree/main, main branch) in production.

Install All Skills (Development Only)

⚠️ NOT FOR PRODUCTION: Uses floating URL without commit pinning.

npx skills add https://github.com/kcns008/cluster-agent-swarm-skills

Install All Skills (Production - Pinned)

✅ RECOMMENDED: Pins to verified commit hash.

npx skills add https://github.com/kcns008/cluster-agent-swarm-skills/tree/91c362dba2911f7523f179e7dcc374cf4335814e


Verification steps:

# Verify the commit before installing
git clone https://github.com/kcns008/cluster-agent-swarm-skills
cd cluster-agent-swarm-skills
git checkout 91c362dba2911f7523f179e7dcc374cf4335814e
git show --stat  # Review what changed
# Then install using the pinned URL above

Install Individual Skills

⚠️ ALWAYS PIN TO VERIFIED COMMIT - Do not use tree/main in production.

# Orchestrator - Jarvis (task routing, coordination)
npx skills add https://github.com/kcns008/cluster-agent-swarm-skills/tree/91c362dba2911f7523f179e7dcc374cf4335814e/skills/orchestrator

# Cluster Ops - Atlas (cluster lifecycle, nodes, upgrades)
npx skills add https://github.com/kcns008/cluster-agent-swarm-skills/tree/91c362dba2911f7523f179e7dcc374cf4335814e/skills/cluster-ops

# GitOps - Flow (ArgoCD, Helm, Kustomize)
npx skills add https://github.com/kcns008/cluster-agent-swarm-skills/tree/91c362dba2911f7523f179e7dcc374cf4335814e/skills/gitops

# Security - Shield (RBAC, policies, CVEs)
npx skills add https://github.com/kcns008/cluster-agent-swarm-skills/tree/91c362dba2911f7523f179e7dcc374cf4335814e/skills/security

# Observability - Pulse (metrics, alerts, incidents)
npx skills add https://github.com/kcns008/cluster-agent-swarm-skills/tree/91c362dba2911f7523f179e7dcc374cf4335814e/skills/observability

# Artifacts - Cache (registries, SBOM, promotions)
npx skills add https://github.com/kcns008/cluster-agent-swarm-skills/tree/91c362dba2911f7523f179e7dcc374cf4335814e/skills/artifacts

# Developer Experience - Desk (namespaces, onboarding)
npx skills add https://github.com/kcns008/cluster-agent-swarm-skills/tree/91c362dba2911f7523f179e7dcc374cf4335814e/skills/developer-experience

Manual Installation (Highest Security)

✅ MOST SECURE: No remote code execution, full audit trail.

# Clone and verify
git clone https://github.com/kcns008/cluster-agent-swarm-skills
cd cluster-agent-swarm-skills

# Checkout verified commit
git checkout 91c362dba2911f7523f179e7dcc374cf4335814e

# Verify (optional, if GPG signed)
git verify-commit 91c362dba2911f7523f179e7dcc374cf4335814e

# Review scripts BEFORE copying
# ls skills/*/scripts/
# cat skills/*/scripts/*.sh

# Copy manually reviewed scripts
cp -r skills/orchestrator ~/.claude/skills/
cp -r skills/cluster-ops ~/.claude/skills/
# ... add other skills as needed

The Swarm — Agent Roster
Agent	Code Name	Session Key	Domain
Orchestrator	Jarvis	agent:platform:orchestrator	Task routing, coordination, standups
Cluster Ops	Atlas	agent:platform:cluster-ops	Cluster lifecycle, nodes, upgrades
GitOps	Flow	agent:platform:gitops	ArgoCD, Helm, Kustomize, deploys
Security	Shield	agent:platform:security	RBAC, policies, secrets, scanning
Observability	Pulse	agent:platform:observability	Metrics, logs, alerts, incidents
Artifacts	Cache	agent:platform:artifacts	Registries, SBOM, promotion, CVEs
Developer Experience	Desk	agent:platform:developer-experience	Namespaces, onboarding, support
Agent Capabilities Summary
What Agents CAN Do
Read cluster state (kubectl get, kubectl describe, oc get)
Deploy via GitOps (argocd app sync, Flux reconciliation)
Create documentation and reports
Investigate and triage incidents
Provision standard resources (namespaces, quotas, RBAC)
Run health checks and audits
Scan images and generate SBOMs
Query metrics and logs
Execute pre-approved runbooks
What Agents CANNOT Do (Human-in-the-Loop Required)
Delete production resources (kubectl delete in prod)
Modify cluster-wide policies (NetworkPolicy, OPA, Kyverno cluster policies)
Make direct changes to secrets without rotation workflow
Modify network routes or service mesh configuration
Scale beyond defined resource limits
Perform irreversible cluster upgrades
Approve production deployments (can prepare, human approves)
Change RBAC at cluster-admin level
Communication Patterns
@Mentions

Agents communicate via @mentions in shared task comments:

@Shield Please review the RBAC for payment-service v3.2 before I sync.
@Pulse Is the CPU spike related to the deployment or external traffic?
@Atlas The staging cluster needs 2 more worker nodes.

Thread Subscriptions
Commenting on a task → auto-subscribe
Being @mentioned → auto-subscribe
Being assigned → auto-subscribe
Once subscribed → receive ALL future comments on heartbeat
Escalation Path
Agent detects issue
Agent attempts resolution within guardrails
If blocked → @mention another agent or escalate to human
P1 incidents → all relevant agents auto-notified
Heartbeat Schedule

Agents wake on staggered 5-minute intervals:

*/5  * * * *  Atlas   (Cluster Ops - needs fast response for incidents)
*/5  * * * *  Pulse   (Observability - needs fast response for alerts)
*/5  * * * *  Shield  (Security - fast response for CVEs and threats)
*/10 * * * *  Flow    (GitOps - deployments can wait a few minutes)
*/10 * * * *  Cache   (Artifacts - promotions are scheduled)
*/15 * * * *  Desk    (DevEx - developer requests aren't usually urgent)
*/15 * * * *  Orchestrator (Coordination - overview and standups)

Key Principles
Roles over genericism — Each agent has a defined SOUL with exactly who they are
Files over mental notes — Only files persist between sessions
Staggered schedules — Don't wake all agents at once
Shared context — One source of truth for tasks and communication
Heartbeat, not always-on — Balance responsiveness with cost
Human-in-the-loop — Critical actions require approval
Guardrails over freedom — Define what agents can and cannot do
Audit everything — Every action logged to activity feed
Reliability first — System stability always wins over new features
Security by default — Deny access, approve by exception
Detailed Agent Capabilities
Orchestrator (Jarvis)
Task routing: determining which agent should handle which request
Workflow orchestration: coordinating multi-agent operations
Daily standups: compiling swarm-wide status reports
Priority management: determining urgency and sequencing of work
Cross-agent communication: facilitating collaboration
Accountability: tracking what was promised vs what was delivered
Cluster Ops (Atlas)
OpenShift/Kubernetes cluster operations (upgrades, scaling, patching)
Node pool management and autoscaling
Resource quota management and capacity planning
Network troubleshooting (OVN-Kubernetes, Cilium, Calico)
Storage class management and PVC/CSI issues
etcd backup, restore, and health monitoring
Multi-platform expertise (OCP, EKS, AKS, GKE, ROSA, ARO)
GitOps (Flow)
ArgoCD application management (sync, rollback, sync waves, hooks)
Helm chart development, debugging, and templating
Kustomize overlays and patch generation
ApplicationSet templates for multi-cluster deployments
Deployment strategy management (canary, blue-green, rolling)
Git repository management and branching strategies
Drift detection and remediation
Secrets management integration (Vault, Sealed Secrets, External Secrets)
Security (Shield)
RBAC audit and management
NetworkPolicy review and enforcement
Security policy validation (OPA, Kyverno)
Vulnerability scanning (image scanning, CVE triage)
Secret rotation workflows
Security incident investigation
Compliance reporting
Observability (Pulse)
Prometheus/Grafana metric queries
Log aggregation and search (Loki, Elasticsearch)
Alert triage and investigation
SLO tracking and error budget monitoring
Incident response coordination
Dashboards and visualization
Telemetry pipeline troubleshooting
Artifacts (Cache)
Container registry management
Image scanning and CVE analysis
SBOM generation and tracking
Artifact promotion workflows
Version management
Registry caching and proxying
Developer Experience (Desk)
Namespace provisioning
Resource quota and limit range management
Developer onboarding
Template generation
Developer support and troubleshooting
Documentation generation
File Structure
cluster-agent-swarm-skills/
├── SKILL.md                    # This file - combined swarm
├── AGENTS.md                   # Swarm configuration and protocols
├── skills/
│   ├── orchestrator/           # Jarvis - task routing
│   │   └── SKILL.md
│   ├── cluster-ops/            # Atlas - cluster operations
│   │   └── SKILL.md
│   ├── gitops/                 # Flow - GitOps
│   │   └── SKILL.md
│   ├── security/               # Shield - security
│   │   └── SKILL.md
│   ├── observability/          # Pulse - monitoring
│   │   └── SKILL.md
│   ├── artifacts/              # Cache - artifacts
│   │   └── SKILL.md
│   └── developer-experience/   # Desk - DevEx
│       └── SKILL.md

├── scripts/                    # Shared scripts
└── references/                 # Shared documentation

Reference Documentation

For detailed capabilities of each agent, refer to individual SKILL.md files:

skills/orchestrator/SKILL.md - Full Orchestrator documentation
skills/cluster-ops/SKILL.md - Full Cluster Ops documentation
skills/gitops/SKILL.md - Full GitOps documentation
skills/security/SKILL.md - Full Security documentation
skills/observability/SKILL.md - Full Observability documentation
skills/artifacts/SKILL.md - Full Artifacts documentation
skills/developer-experience/SKILL.md - Full Developer Experience documentation
Weekly Installs
28
Repository
kcns008/cluster…m-skills
GitHub Stars
8
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail