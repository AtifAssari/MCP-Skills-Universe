---
title: devops
url: https://skills.sh/dauquangthanh/hanoi-rainbow/devops
---

# devops

skills/dauquangthanh/hanoi-rainbow/devops
devops
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill devops
SKILL.md
DevOps
Core Capabilities

Provides expert guidance covering the entire software delivery lifecycle:

CI/CD Pipeline Design - Automated build, test, and deployment workflows
Infrastructure as Code - Cloud resource provisioning with Terraform, CloudFormation, Bicep
Container Orchestration - Docker and Kubernetes deployment patterns
Deployment Strategies - Blue-green, canary, and rolling deployments
Monitoring & Observability - Metrics, logging, alerting with Prometheus, Grafana, ELK
Configuration Management - Ansible, Chef, Puppet automation
Security & Compliance - DevSecOps practices and container security
Best Practices
CI/CD
Keep pipelines fast (< 10 minutes for feedback)
Fail fast with quick tests first
Use pipeline as code (version controlled)
Implement proper secret management
Enable artifact caching and parallelize independent jobs
Infrastructure as Code
Use remote state with locking
Create reusable modules and pin versions
Always review plan before apply
Implement proper tagging strategy
Document resource dependencies
Container Orchestration
Set resource requests and limits
Implement health checks (liveness/readiness probes)
Use pod anti-affinity for high availability
Enable horizontal pod autoscaling
Implement proper logging and monitoring
Deployment
Use rolling updates with zero downtime
Implement proper health checks and rollback capabilities
Use canary/blue-green for critical applications
Test thoroughly in staging environments
Monitor post-deployment metrics
Security
Run containers as non-root with read-only root filesystems
Scan images for vulnerabilities regularly
Implement network policies and secrets management
Enable pod security standards and least privilege access
Monitoring
Collect metrics using RED/USE methods
Implement structured logging with meaningful alerts
Create actionable dashboards and monitor SLIs/SLOs
Set up distributed tracing for microservices
Detailed References

Load reference files based on specific needs:

CI/CD Pipeline Design: See cicd-pipeline-design.md for:

GitHub Actions, GitLab CI, Jenkins pipeline examples
Automated build, test, deploy workflow patterns
Pipeline optimization and caching strategies

Infrastructure as Code: See infrastructure-as-code.md for:

Terraform, CloudFormation, Bicep patterns
AWS, GCP, Azure resource provisioning
Module design and state management

Container Orchestration: See container-orchestration.md for:

Kubernetes manifests, Helm charts, Kustomize
Docker best practices and multi-stage builds
Service mesh and networking patterns

Deployment Strategies: See deployment-strategies.md for:

Blue-green deployment implementation
Canary release patterns with traffic splitting
Rolling update strategies and rollback procedures

Monitoring & Observability: See monitoring-and-observability.md for:

Prometheus, Grafana setup and configuration
ELK stack deployment and log aggregation
Alert rules, dashboards, and SLO definitions

Security Best Practices: See security-best-practices.md for:

DevSecOps pipeline integration
Container security scanning and hardening
Secret management and compliance validation

Configuration Management: See configuration-management.md for:

Ansible playbooks, Chef recipes, Puppet manifests
Server configuration automation patterns
Infrastructure drift detection

Common Commands: See common-commands.md for:

Kubernetes kubectl command reference
Docker CLI operations
Terraform and cloud provider CLI commands

Troubleshooting: See troubleshooting-guide.md for:

Common issues and resolution steps
Debugging techniques for containers and orchestration
Performance optimization strategies
Weekly Installs
12
Repository
dauquangthanh/h…-rainbow
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass