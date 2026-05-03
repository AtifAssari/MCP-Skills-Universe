---
rating: ⭐⭐⭐
title: cloud-architect
url: https://skills.sh/jeffallan/claude-skills/cloud-architect
---

# cloud-architect

skills/jeffallan/claude-skills/cloud-architect
cloud-architect
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill cloud-architect
Summary

Multi-cloud architecture design, migration planning, cost optimization, and disaster recovery across AWS, Azure, and GCP.

Covers six core workflow stages: discovery, design, security, cost modeling, migration, and operations with validation checkpoints at each phase
Implements zero-trust security, least-privilege IAM, encryption at rest and in transit, and multi-region redundancy for critical workloads
Applies the 6Rs migration framework, Well-Architected principles, and FinOps practices for right-sizing and reserved capacity optimization
Provides infrastructure-as-code examples (Terraform, CloudFormation) and CLI commands for VPC design, auto-scaling, IAM policies, and cost analysis across all three clouds
SKILL.md
Cloud Architect
Core Workflow
Discovery — Assess current state, requirements, constraints, compliance needs
Design — Select services, design topology, plan data architecture
Security — Implement zero-trust, identity federation, encryption
Cost Model — Right-size resources, reserved capacity, auto-scaling
Migration — Apply 6Rs framework, define waves, validate connectivity before cutover
Operate — Set up monitoring, automation, continuous optimization
Workflow Validation Checkpoints

After Design: Confirm every component has a redundancy strategy and no single points of failure exist in the topology.

Before Migration cutover: Validate VPC peering or connectivity is fully established:

# AWS: confirm peering connection is Active before proceeding
aws ec2 describe-vpc-peering-connections \
  --filters "Name=status-code,Values=active"

# Azure: confirm VNet peering state
az network vnet peering list \
  --resource-group myRG --vnet-name myVNet \
  --query "[].{Name:name,State:peeringState}"


After Migration: Verify application health and routing:

# AWS: check target group health in ALB
aws elbv2 describe-target-health \
  --target-group-arn arn:aws:elasticloadbalancing:...


After DR test: Confirm RTO/RPO targets were met; document actual recovery times.

Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
AWS Services	references/aws.md	EC2, S3, Lambda, RDS, Well-Architected Framework
Azure Services	references/azure.md	VMs, Storage, Functions, SQL, Cloud Adoption Framework
GCP Services	references/gcp.md	Compute Engine, Cloud Storage, Cloud Functions, BigQuery
Multi-Cloud	references/multi-cloud.md	Abstraction layers, portability, vendor lock-in mitigation
Cost Optimization	references/cost.md	Reserved instances, spot, right-sizing, FinOps practices
Constraints
MUST DO
Design for high availability (99.9%+)
Implement security by design (zero-trust)
Use infrastructure as code (Terraform, CloudFormation)
Enable cost allocation tags and monitoring
Plan disaster recovery with defined RTO/RPO
Implement multi-region for critical workloads
Use managed services when possible
Document architectural decisions
MUST NOT DO
Store credentials in code or public repos
Skip encryption (at rest and in transit)
Create single points of failure
Ignore cost optimization opportunities
Deploy without proper monitoring
Use overly complex architectures
Ignore compliance requirements
Skip disaster recovery testing
Common Patterns with Examples
Least-Privilege IAM (Zero-Trust)

Rather than broad policies, scope permissions to specific resources and actions:

# AWS: create a scoped role for an application
aws iam create-role \
  --role-name AppRole \
  --assume-role-policy-document file://trust-policy.json

aws iam put-role-policy \
  --role-name AppRole \
  --policy-name AppInlinePolicy \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::my-app-bucket/*"
    }]
  }'

# Terraform equivalent
resource "aws_iam_role" "app_role" {
  name               = "AppRole"
  assume_role_policy = data.aws_iam_policy_document.trust.json
}

resource "aws_iam_role_policy" "app_policy" {
  role = aws_iam_role.app_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["s3:GetObject", "s3:PutObject"]
      Resource = "${aws_s3_bucket.app.arn}/*"
    }]
  })
}

VPC with Public/Private Subnets (Terraform)
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = { Name = "main", CostCenter = var.cost_center }
}

resource "aws_subnet" "private" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet("10.0.0.0/16", 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
}

resource "aws_subnet" "public" {
  count                   = 2
  vpc_id                  = aws_vpc.main.id
  cidr_block              = cidrsubnet("10.0.0.0/16", 8, count.index + 10)
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true
}

Auto-Scaling Group (Terraform)
resource "aws_autoscaling_group" "app" {
  desired_capacity    = 2
  min_size            = 1
  max_size            = 10
  vpc_zone_identifier = aws_subnet.private[*].id

  launch_template {
    id      = aws_launch_template.app.id
    version = "$Latest"
  }

  tag {
    key                 = "CostCenter"
    value               = var.cost_center
    propagate_at_launch = true
  }
}

resource "aws_autoscaling_policy" "cpu_target" {
  autoscaling_group_name = aws_autoscaling_group.app.name
  policy_type            = "TargetTrackingScaling"
  target_tracking_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ASGAverageCPUUtilization"
    }
    target_value = 60.0
  }
}

Cost Analysis CLI
# AWS: identify top cost drivers for the last 30 days
aws ce get-cost-and-usage \
  --time-period Start=$(date -d '30 days ago' +%Y-%m-%d),End=$(date +%Y-%m-%d) \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE \
  --query 'ResultsByTime[0].Groups[*].{Service:Keys[0],Cost:Metrics.UnblendedCost.Amount}' \
  --output table

# Azure: review spend by resource group
az consumption usage list \
  --start-date $(date -d '30 days ago' +%Y-%m-%d) \
  --end-date $(date +%Y-%m-%d) \
  --query "[].{ResourceGroup:resourceGroup,Cost:pretaxCost,Currency:currency}" \
  --output table

Output Templates

When designing cloud architecture, provide:

Architecture diagram with services and data flow
Service selection rationale (compute, storage, database, networking)
Security architecture (IAM, network segmentation, encryption)
Cost estimation and optimization strategy
Deployment approach and rollback plan

Documentation

Weekly Installs
1.8K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass