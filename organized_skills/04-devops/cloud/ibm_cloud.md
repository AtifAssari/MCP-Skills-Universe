---
rating: ⭐⭐⭐
title: ibm-cloud
url: https://skills.sh/dauquangthanh/hanoi-rainbow/ibm-cloud
---

# ibm-cloud

skills/dauquangthanh/hanoi-rainbow/ibm-cloud
ibm-cloud
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill ibm-cloud
SKILL.md
IBM Cloud

Systematic IBM Cloud platform guidance for enterprise cloud infrastructure, covering compute, storage, databases, networking, security, and operational best practices.

Workflow Decision Tree

Choose your path based on the task:

1. Service Category Selection

Compute & Containers → Load compute-services.md

Virtual Private Cloud (VPC) and Virtual Server Instances
IBM Kubernetes Service (IKS) and Red Hat OpenShift
Code Engine (serverless containers) and Cloud Functions

Storage → Load storage-services.md

Cloud Object Storage, Block Storage, File Storage

Databases → Load database-services.md

Db2, Cloudant, PostgreSQL, MySQL, MongoDB, Redis

Security & Access → Load iam-security.md

IAM, Resource Groups, Service IDs, Key Protect, Secrets Manager

Networking → Load networking.md

VPC Networks, Load Balancers, DNS/CDN, Direct Link
2. Architecture & Deployment Patterns

High Availability → Multi-zone deployment across 3 availability zones Microservices → IKS/OpenShift with service mesh and ingress Serverless → Code Engine applications with auto-scaling Hybrid Cloud → Direct Link or VPN for on-premises connectivity

3. Common Operations

Initial Setup → Install CLI, authenticate, configure regions and resource groups Resource Provisioning → Use CLI, Terraform, or IBM Cloud Console Security Configuration → IAM policies, encryption, network security Monitoring → Set up logging, monitoring, and cost tracking

Core Concepts
Resource Hierarchy
Account → Resource Groups → Services/Resources → Access Groups (IAM)

Regions and Multi-Zone Architecture
Primary Regions: us-south, us-east, eu-gb, eu-de, jp-tok, au-syd
Availability Zones: 3 zones per region (e.g., us-south-1, us-south-2, us-south-3)
Best Practice: Deploy across multiple zones for high availability
Service Categories
IaaS: VPC, Virtual Servers, Block/File Storage
PaaS: IKS, OpenShift, Code Engine
SaaS: Managed Databases, Watson AI, DevOps Tools
Serverless: Code Engine, Cloud Functions
Quick Start
1. Install and Configure CLI
# Install CLI (macOS/Linux)
curl -fsSL https://clis.cloud.ibm.com/install/osx | sh

# Login
ibmcloud login

# Target region and resource group
ibmcloud target -r us-south -g my-resource-group

# Install common plugins
ibmcloud plugin install container-service vpc-infrastructure

2. Basic Resource Creation Pattern
# 1. Create VPC
ibmcloud is vpc-create my-vpc

# 2. Create resources (compute, storage, network)
ibmcloud is instance-create my-vsi ...

# 3. Configure IAM
ibmcloud iam ...

# 4. Deploy application
# 5. Set up monitoring

Essential Guidance
Security Best Practices
IAM: Use Access Groups, apply least privilege, rotate API keys every 90 days
Network: Use private endpoints, configure Security Groups and ACLs
Data: Enable encryption at rest/transit, use Key Protect for key management
Compliance: Choose regions for data residency requirements
Cost Optimization
Right-size instances for workload requirements
Use reserved capacity for predictable workloads
Leverage serverless (Code Engine/Functions) for variable loads
Select appropriate storage tiers (Standard, Vault, Cold Vault)
Enable auto-scaling to match demand
Set budget alerts and monitor usage
Reference Files

Load detailed guidance based on specific needs:

compute-services.md: VPC, Virtual Servers, IKS, OpenShift, Code Engine, Cloud Functions
storage-services.md: Object Storage, Block Storage, File Storage
database-services.md: Db2, Cloudant, PostgreSQL, MySQL, MongoDB, Redis
iam-security.md: IAM, Access Groups, Service IDs, Key Protect, Secrets Manager
networking.md: VPC networking, Load Balancers, DNS/CDN, Direct Link
Support Resources
Documentation: https://cloud.ibm.com/docs
API Reference: https://cloud.ibm.com/apidocs
Terraform Provider: https://registry.terraform.io/providers/IBM-Cloud/ibm
CLI Reference: https://cloud.ibm.com/docs/cli
Weekly Installs
17
Repository
dauquangthanh/h…-rainbow
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass