---
rating: ⭐⭐
title: devops-iac-engineer
url: https://skills.sh/davila7/claude-code-templates/devops-iac-engineer
---

# devops-iac-engineer

skills/davila7/claude-code-templates/devops-iac-engineer
devops-iac-engineer
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill devops-iac-engineer
Summary

Cloud infrastructure design, provisioning, and operations using IaC, Kubernetes, and DevOps best practices.

Covers Terraform, Kubernetes, and multi-cloud platforms (AWS, Azure, GCP) with structured workflows for architecture design, implementation, and validation
Includes CI/CD pipeline design, GitOps patterns, and deployment strategies (blue/green, canary) with automated testing and rollback procedures
Provides observability frameworks with SLI/SLO/SLA definitions, logging, metrics, tracing, and on-call runbook guidance
Addresses common challenges: infrastructure drift detection, secrets management, cost optimization, and complex Kubernetes configurations
Emphasizes security-first practices, policy-as-code, compliance automation, and cross-team collaboration patterns
SKILL.md
DevOps IaC Engineer

This Skill helps DevOps teams design, implement, and maintain cloud infrastructure using Infrastructure as Code principles. Use this when building cloud architectures, deploying containerized applications, setting up CI/CD pipelines, or implementing observability and security practices.

Quick Navigation
Terraform & IaC: See terraform.md for Terraform best practices and patterns
Kubernetes & Containers: See kubernetes.md for container orchestration
Cloud Platforms: See cloud_platforms.md for AWS, Azure, GCP guidance
CI/CD Pipelines: See cicd.md for pipeline design and GitOps
Observability: See observability.md for monitoring and logging
Security: See security.md for DevSecOps practices
Templates & Tools: See templates.md for ready-to-use templates
Core Principles
Key DevOps Terminology (Consistent Throughout)
Infrastructure as Code (IaC): Managing infrastructure through declarative code files
GitOps: Using Git as the single source of truth for infrastructure and applications
Immutable Infrastructure: Infrastructure components that are replaced rather than modified
Service Mesh: Infrastructure layer for service-to-service communication
Observability: Ability to understand system state from external outputs (logs, metrics, traces)
SLI/SLO/SLA: Service Level Indicators/Objectives/Agreements for reliability
RTO/RPO: Recovery Time Objective/Recovery Point Objective for disaster recovery
Workflow: Infrastructure Implementation

When implementing infrastructure, follow this structured approach:

Understand Requirements

What is the business need? (new application, migration, scaling, compliance)
What are the scale requirements? (traffic, data, geographic distribution)
What are the constraints? (budget, timeline, regulatory)
What are the dependencies? (existing systems, data sources)

Design Architecture

Choose appropriate cloud platform(s) and services
Design for high availability and fault tolerance
Plan network topology and security boundaries
Identify data flows and storage requirements
Document architecture with diagrams

Select IaC Tools

Terraform for multi-cloud infrastructure provisioning
Kubernetes manifests/Helm for container orchestration
CI/CD tool selection based on team and requirements
Configuration management tools if needed

Implement Infrastructure

Create modular, reusable IaC code
Follow security best practices (see security.md)
Implement proper state management and versioning
Use consistent naming and tagging conventions
Document code and create README files

Set Up Observability

Define SLIs and SLOs for critical services
Implement logging, metrics, and tracing
Create dashboards and alerts
Set up log aggregation and analysis
Plan on-call rotation and runbooks

Implement CI/CD

Design deployment pipeline stages
Implement automated testing (unit, integration, e2e)
Set up GitOps workflows
Configure deployment strategies (blue/green, canary)
Implement rollback procedures

Test & Validate

Run infrastructure tests (security, compliance, cost)
Perform disaster recovery drills
Load testing and performance validation
Security scanning and penetration testing
Document test results and improvements

Deploy & Monitor

Execute phased rollout
Monitor metrics and logs closely
Validate against SLOs
Document runbooks and troubleshooting guides
Conduct post-deployment review
Decision Framework: Tool Selection

Multi-Cloud Requirements → Terraform or Pulumi AWS-Only → Terraform, AWS CDK, or CloudFormation Container Orchestration → Kubernetes (EKS, GKE, AKS) Simple Container Deployment → ECS, Cloud Run, or App Service Configuration Management → Ansible or cloud-native solutions GitOps Workflows → ArgoCD or Flux CI/CD Pipelines → GitHub Actions, GitLab CI, or Jenkins

Common Challenges & Solutions

Problem: Infrastructure drift between code and reality Solution: Implement automated drift detection, use terraform plan in CI/CD, enable read-only production access, maintain state file integrity

Problem: Secrets management and credential exposure Solution: Use cloud-native secret managers (AWS Secrets Manager, HashiCorp Vault), implement SOPS for encrypted secrets in Git, use IRSA/workload identity

Problem: High cloud costs and unexpected bills Solution: Implement tagging strategy, use cost allocation tags, set up budget alerts, right-size resources, use spot instances, implement auto-scaling

Problem: Complex Kubernetes configurations Solution: Use Helm charts for templating, implement Kustomize for environment-specific configs, follow GitOps patterns, use operators for complex workloads

Collaboration Tips
With Development Teams: Provide self-service platforms, document APIs, share infrastructure as reusable modules
With Security Teams: Implement policy as code, automate compliance checks, provide audit trails
With SRE Teams: Define SLIs/SLOs together, share on-call responsibilities, collaborate on incident response
With Finance Teams: Provide cost visibility, forecast expenses, implement chargeback models
Next Steps
Start with terraform.md if you're implementing infrastructure as code
Use kubernetes.md for container orchestration
Reference templates.md for ready-to-use configurations
Check observability.md to set up monitoring

Note: Always verify current infrastructure state, security requirements, and compliance needs before implementing changes. This Skill provides frameworks and best practices but should be adapted to your organization's specific requirements.

Weekly Installs
526
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass