---
title: alibaba-cloud
url: https://skills.sh/dauquangthanh/hanoi-rainbow/alibaba-cloud
---

# alibaba-cloud

skills/dauquangthanh/hanoi-rainbow/alibaba-cloud
alibaba-cloud
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill alibaba-cloud
SKILL.md
Alibaba Cloud
Core Capabilities

Provides expert guidance across Alibaba Cloud ecosystem:

Compute Services - ECS instances, Auto Scaling, Container Service (ACK), Function Compute
Storage & Database - OSS object storage, ApsaraDB (RDS, Redis, MongoDB), NAS, Block Storage
Networking - VPC, SLB (Server Load Balancer), VPN Gateway, CEN, NAT Gateway
Security & Identity - RAM (Resource Access Management), Security Center, WAF, Anti-DDoS
Application Services - API Gateway, Message Service (MNS/MQ), DirectMail, SMS
DevOps & Monitoring - CloudMonitor, Log Service, ARMS, Container Registry
CDN & Edge - Alibaba Cloud CDN, DCDN, Global Accelerator
Data & Analytics - DataWorks, MaxCompute, AnalyticDB, E-MapReduce
Best Practices
Architecture
Deploy across multiple zones for high availability
Use SLB for load balancing with health checks
Implement Auto Scaling for dynamic capacity
Configure CloudMonitor with actionable alerts
Security
Enable RAM with least privilege access control
Use Security Groups and Network ACLs for filtering
Enable encryption at rest and in transit
Implement WAF and Anti-DDoS for protection
Enable ActionTrail for audit logging
Cost Optimization
Use Reserved Instances for predictable workloads (up to 70% savings)
Leverage Preemptible Instances for batch jobs
Configure Auto Scaling to match demand
Use OSS lifecycle policies for cold data
Monitor with Cost Management dashboards
Performance
Choose appropriate instance families and sizes
Implement Redis/Memcache for caching
Use CDN for static content delivery
Configure read replicas for databases
Enable ESSD disks for high IOPS workloads
Infrastructure as Code
Terraform for Alibaba Cloud
terraform {
  required_providers {
    alicloud = {
      source  = "aliyun/alicloud"
      version = "~> 1.200"
    }
  }
}

provider "alicloud" {
  region = "cn-hangzhou"
}

# VPC with multi-zone deployment
resource "alicloud_vpc" "main" {
  vpc_name   = "production-vpc"
  cidr_block = "10.0.0.0/16"
}

resource "alicloud_vswitch" "app" {
  vpc_id     = alicloud_vpc.main.id
  cidr_block = "10.0.1.0/24"
  zone_id    = "cn-hangzhou-h"
}

resource "alicloud_security_group" "app" {
  vpc_id = alicloud_vpc.main.id
  name   = "application-sg"
}

resource "alicloud_instance" "app" {
  instance_name              = "app-server"
  instance_type              = "ecs.g6.large"
  image_id                   = "ubuntu_20_04_x64"
  vswitch_id                 = alicloud_vswitch.app.id
  security_groups            = [alicloud_security_group.app.id]
  internet_max_bandwidth_out = 10
}

ROS (Resource Orchestration Service)
ROSTemplateFormatVersion: '2015-09-01'
Description: High availability web application
Parameters:
  InstanceType:
    Type: String
    Default: ecs.g6.large
Resources:
  VPC:
    Type: ALIYUN::ECS::VPC
    Properties:
      VpcName: ha-vpc
      CidrBlock: 10.0.0.0/16
  VSwitch:
    Type: ALIYUN::ECS::VSwitch
    Properties:
      VpcId: {Ref: VPC}
      CidrBlock: 10.0.1.0/24
      ZoneId: cn-hangzhou-h
  SLB:
    Type: ALIYUN::SLB::LoadBalancer
    Properties:
      LoadBalancerName: web-lb
      AddressType: internet
      VpcId: {Ref: VPC}
      VSwitchId: {Ref: VSwitch}

China-Specific Considerations
ICP Filing
Required for websites hosted in mainland China
Obtain before pointing domain to Alibaba Cloud
Allow 20-30 business days for approval
Different requirements for personal vs corporate
Data Residency & Compliance
Data localization laws require China region storage
Use: cn-hangzhou, cn-shanghai, cn-beijing, cn-shenzhen
Understand Cybersecurity Law and Data Security Law
Cross-border transfer requires security assessment
Network & Performance
Great Wall Firewall impacts international connectivity
Use China CDN for domestic users
Use Global Accelerator for cross-border access
Test from within China for accurate results
Migration to Alibaba Cloud
Assessment
Inventory infrastructure, applications, and dependencies
Analyze regulatory requirements (ICP, data residency)
Map services to Alibaba Cloud equivalents
Estimate costs with pricing calculator
Plan connectivity (VPN Gateway, Express Connect)
Strategies
Rehost - Lift and shift with minimal changes
Replatform - Optimize with managed services (RDS, OSS, Redis)
Refactor - Rebuild with cloud-native services (Function Compute, ACK)
Hybrid - Partial migration with on-premises connectivity
Execution
Set up account and configure RAM
Establish network connectivity
Create VPC, VSwitches, security groups
Migrate data to OSS/RDS
Deploy applications to ECS/ACK
Configure SLB and DNS
Set up CloudMonitor and Log Service
Test and execute cutover

See cloud-migration.md for detailed procedures

Reference Files

Load detailed documentation when needed:

Compute Services: See compute-services.md for ECS instance families, specifications, custom images, Auto Scaling configuration, and optimization techniques

Storage Solutions: See storage-solutions.md for OSS bucket policies, encryption, lifecycle rules, NAS setup, and storage optimization strategies

Database Services: See database-services.md for ApsaraDB RDS, PolarDB, Redis, MongoDB configuration, tuning, backup, and high availability setup

Infrastructure as Code: See infrastructure-as-code.md for Terraform modules, ROS templates, multi-environment patterns, and deployment automation

Cloud Migration: See cloud-migration.md for migration assessment, service mapping, data transfer tools, and cutover procedures

Weekly Installs
28
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