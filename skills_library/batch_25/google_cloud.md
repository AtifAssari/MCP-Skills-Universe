---
title: google-cloud
url: https://skills.sh/dauquangthanh/hanoi-rainbow/google-cloud
---

# google-cloud

skills/dauquangthanh/hanoi-rainbow/google-cloud
google-cloud
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill google-cloud
SKILL.md
Google Cloud Platform (GCP)
Core Capabilities

Provides expert guidance for Google Cloud Platform across all major services:

Compute Services - Compute Engine (VMs), Cloud Run, Cloud Functions, App Engine
Container & Kubernetes - Google Kubernetes Engine (GKE), Artifact Registry, Cloud Build
Storage Services - Cloud Storage (buckets), Persistent Disk, Filestore
Database Services - Cloud SQL, Cloud Spanner, Firestore, Bigtable, Memorystore
Data & Analytics - BigQuery, Dataflow, Dataproc, Pub/Sub, Composer
Networking - VPC, Cloud Load Balancing, Cloud CDN, Cloud Armor, Cloud Interconnect
Security & IAM - Identity and Access Management, Secret Manager, Cloud KMS, Security Command Center
Infrastructure as Code - Terraform Google provider, Deployment Manager, Config Connector
Key Principles
General Best Practices
Follow least privilege - Use IAM roles with minimal required permissions
Enable monitoring - Configure Cloud Monitoring and Logging for all services
Use managed services - Prefer GKE Autopilot, Cloud SQL, Cloud Run over self-managed
Implement IaC - Use Terraform or Deployment Manager for reproducible infrastructure
Tag resources - Apply labels for cost allocation and organization
Design for HA - Use regional resources and multi-zone deployments
Secure by default - Enable encryption, use private IPs, configure VPC Service Controls
Optimize costs - Use committed use discounts, autoscaling, and appropriate resource sizing
Architecture Patterns
Multi-tier applications: VPC + Cloud Load Balancer + GKE/Cloud Run + Cloud SQL
Data pipelines: Pub/Sub → Dataflow → BigQuery with Cloud Storage staging
Serverless APIs: Cloud Run + Cloud SQL + Secret Manager + Cloud Armor
Hybrid connectivity: VPN or Cloud Interconnect + Shared VPC + Private Google Access
When to Use What
Compute Engine: Full VM control, Windows workloads, lift-and-shift migrations
GKE: Containerized applications, microservices, Kubernetes workloads
Cloud Run: Stateless HTTP services, event-driven processing, auto-scaling needs
Cloud Functions: Event handlers, webhooks, simple integrations
Cloud SQL: Relational databases with minimal management
Cloud Spanner: Global distributed SQL, strong consistency across regions
BigQuery: Data warehouse, analytics, large-scale SQL queries
Firestore: Document database, real-time sync, mobile/web apps
Detailed References

Load reference files based on specific needs:

Compute Services: See compute-services.md for:

Compute Engine machine types and selection guide
Managed instance groups and autoscaling
Custom images and startup scripts
Preemptible VMs and spot instances

Container Orchestration: See container-orchestration.md for:

GKE cluster setup and configuration
Autopilot vs Standard mode comparison
Node pool management and scaling
Workload identity and service accounts
GKE Ingress and Gateway API

Storage Solutions: See storage-solutions.md for:

Cloud Storage bucket configuration
Storage class selection and lifecycle policies
Persistent disk types and performance
Filestore for shared file systems

Database Services: See database-services.md for:

Cloud SQL instance configuration
Cloud Spanner for global databases
Firestore data modeling
Bigtable for large-scale NoSQL
Memorystore for Redis/Memcached

Data & Analytics: See data-analytics.md for:

BigQuery table design and optimization
Dataflow streaming and batch pipelines
Pub/Sub messaging patterns
Cloud Composer (Airflow) workflows
Data governance and security

Networking Architecture: See networking-architecture.md for:

VPC design patterns and subnet planning
Cloud Load Balancing configuration
Cloud CDN and Cloud Armor setup
VPN and Cloud Interconnect
Shared VPC and peering

Serverless Computing: See serverless-computing.md for:

Cloud Functions deployment and triggers
Cloud Run service configuration
App Engine standard and flexible
Event-driven architectures
Cold start optimization

Security & IAM: See security-iam.md for:

IAM roles and service accounts
Organization policies and constraints
VPC Service Controls
Secret Manager integration
Cloud KMS encryption
Security Command Center alerts

Infrastructure as Code: See infrastructure-as-code.md for:

Terraform Google provider patterns
Deployment Manager templates
Config Connector for GKE
CI/CD with Cloud Build
State management best practices

Migration to GCP: See migration-to-gcp.md for:

Migration planning and assessment
Migrate for Compute Engine (Velostrata)
Database migration service
Storage transfer service
Cutover strategies and validation

Monitoring & Logging: See monitoring-logging.md for:

Cloud Monitoring setup and metrics
Cloud Logging configuration
Log-based alerts and metrics
Cloud Trace for distributed tracing
Cloud Profiler for performance
Dashboards and SLO monitoring

CI/CD Pipeline: See cicd-pipeline.md for:

Cloud Build configuration
Artifact Registry for containers
Deployment to GKE, Cloud Run, App Engine
Binary Authorization for security
Integration with GitHub, GitLab

Cost Management: See cost-management.md for:

Billing reports and cost allocation
Budget alerts and quotas
Committed use discounts planning
Resource optimization strategies
Cost anomaly detection

Multi-Region Architecture: See multi-region-architecture.md for:

Global load balancing patterns
Multi-region database replication
Cross-region data transfer
Disaster recovery strategies
Regional failover setup

Hybrid & Multi-Cloud: See hybrid-multi-cloud.md for:

Anthos for hybrid Kubernetes
Cloud Interconnect and VPN
Multi-cloud networking patterns
Workload migration strategies
Identity federation

GCP CLI & Tools: See gcp-cli-tools.md for:

gcloud CLI installation and configuration
Common gcloud commands
Cloud Shell usage
gsutil for Cloud Storage
bq for BigQuery operations
kubectl for GKE management
Weekly Installs
34
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