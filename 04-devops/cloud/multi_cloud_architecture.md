---
title: multi-cloud-architecture
url: https://skills.sh/wshobson/agents/multi-cloud-architecture
---

# multi-cloud-architecture

skills/wshobson/agents/multi-cloud-architecture
multi-cloud-architecture
Installation
$ npx skills add https://github.com/wshobson/agents --skill multi-cloud-architecture
Summary

Decision framework and service comparison patterns for architecting across AWS, Azure, GCP, and OCI.

Includes detailed service mapping tables across compute, storage, and database categories to identify equivalent offerings and best-of-breed selections
Four core multi-cloud patterns: single provider with disaster recovery, best-of-breed service selection, geographic distribution, and cloud-agnostic abstraction layers
Cloud-agnostic alternatives using Kubernetes, PostgreSQL, Apache Kafka, Redis, and open source tools to reduce vendor lock-in
Cost comparison and optimization strategies covering reserved capacity, spot instances, right-sizing, and lifecycle policies across all four providers
Phased migration strategy from assessment through optimization with best practices for infrastructure as code, monitoring, and disaster recovery testing
SKILL.md
Multi-Cloud Architecture

Decision framework and patterns for architecting applications across AWS, Azure, GCP, and OCI.

Purpose

Design cloud-agnostic architectures and make informed decisions about service selection across cloud providers.

When to Use
Design multi-cloud strategies
Migrate between cloud providers
Select cloud services for specific workloads
Implement cloud-agnostic architectures
Optimize costs across providers
Cloud Service Comparison
Compute Services
AWS	Azure	GCP	OCI	Use Case
EC2	Virtual Machines	Compute Engine	Compute	IaaS VMs
ECS	Container Instances	Cloud Run	Container Instances	Containers
EKS	AKS	GKE	OKE	Kubernetes
Lambda	Functions	Cloud Functions	Functions	Serverless
Fargate	Container Apps	Cloud Run	Container Instances	Managed containers
Storage Services
AWS	Azure	GCP	OCI	Use Case
S3	Blob Storage	Cloud Storage	Object Storage	Object storage
EBS	Managed Disks	Persistent Disk	Block Volumes	Block storage
EFS	Azure Files	Filestore	File Storage	File storage
Glacier	Archive Storage	Archive Storage	Archive Storage	Cold storage
Database Services
AWS	Azure	GCP	OCI	Use Case
RDS	SQL Database	Cloud SQL	MySQL HeatWave	Managed SQL
DynamoDB	Cosmos DB	Firestore	NoSQL Database	NoSQL
Aurora	PostgreSQL/MySQL	Cloud Spanner	Autonomous Database	Distributed SQL
ElastiCache	Cache for Redis	Memorystore	OCI Cache	Caching

Reference: See references/service-comparison.md for complete comparison

Multi-Cloud Patterns
Pattern 1: Single Provider with DR
Primary workload in one cloud
Disaster recovery in another
Database replication across clouds
Automated failover
Pattern 2: Best-of-Breed
Use best service from each provider
AI/ML on GCP
Enterprise apps on Azure
Regulated data platforms on OCI
General compute on AWS
Pattern 3: Geographic Distribution
Serve users from nearest cloud region
Data sovereignty compliance
Global load balancing
Regional failover
Pattern 4: Cloud-Agnostic Abstraction
Kubernetes for compute
PostgreSQL for database
S3-compatible storage (MinIO)
Open source tools
Cloud-Agnostic Architecture
Use Cloud-Native Alternatives
Compute: Kubernetes (EKS/AKS/GKE/OKE)
Database: PostgreSQL/MySQL (RDS/SQL Database/Cloud SQL/MySQL HeatWave)
Message Queue: Apache Kafka or managed streaming (MSK/Event Hubs/Confluent/OCI Streaming)
Cache: Redis (ElastiCache/Azure Cache/Memorystore/OCI Cache)
Object Storage: S3-compatible API
Monitoring: Prometheus/Grafana
Service Mesh: Istio/Linkerd
Abstraction Layers
Application Layer
    ↓
Infrastructure Abstraction (Terraform)
    ↓
Cloud Provider APIs
    ↓
AWS / Azure / GCP / OCI

Cost Comparison
Compute Pricing Factors
AWS: On-demand, Reserved, Spot, Savings Plans
Azure: Pay-as-you-go, Reserved, Spot
GCP: On-demand, Committed use, Preemptible
OCI: Pay-as-you-go, annual commitments, burstable/flexible shapes, preemptible instances
Cost Optimization Strategies
Use reserved/committed capacity (30-70% savings)
Leverage spot/preemptible instances
Right-size resources
Use serverless for variable workloads
Optimize data transfer costs
Implement lifecycle policies
Use cost allocation tags
Monitor with cloud cost tools

Reference: See references/multi-cloud-patterns.md

Migration Strategy
Phase 1: Assessment
Inventory current infrastructure
Identify dependencies
Assess cloud compatibility
Estimate costs
Phase 2: Pilot
Select pilot workload
Implement in target cloud
Test thoroughly
Document learnings
Phase 3: Migration
Migrate workloads incrementally
Maintain dual-run period
Monitor performance
Validate functionality
Phase 4: Optimization
Right-size resources
Implement cloud-native services
Optimize costs
Enhance security
Best Practices
Use infrastructure as code (Terraform/OpenTofu)
Implement CI/CD pipelines for deployments
Design for failure across clouds
Use managed services when possible
Implement comprehensive monitoring
Automate cost optimization
Follow security best practices
Document cloud-specific configurations
Test disaster recovery procedures
Train teams on multiple clouds
Related Skills
terraform-module-library - For IaC implementation
cost-optimization - For cost management
hybrid-cloud-networking - For connectivity
Weekly Installs
5.6K
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