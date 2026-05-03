---
rating: ⭐⭐⭐
title: aws-ec2-setup
url: https://skills.sh/aj-geddes/useful-ai-prompts/aws-ec2-setup
---

# aws-ec2-setup

skills/aj-geddes/useful-ai-prompts/aws-ec2-setup
aws-ec2-setup
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill aws-ec2-setup
SKILL.md
AWS EC2 Setup
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Amazon EC2 provides resizable compute capacity in the cloud. Launch and configure virtual servers with complete control over networking, storage, and security settings. Scale automatically based on demand.

When to Use
Web application servers
Application backends and APIs
Batch processing and compute jobs
Development and testing environments
Containerized applications (ECS)
Kubernetes clusters (EKS)
Database servers
VPN and proxy servers
Quick Start

Minimal working example:

# Create security group
aws ec2 create-security-group \
  --group-name web-server-sg \
  --description "Web server security group" \
  --vpc-id vpc-12345678

# Add ingress rules
aws ec2 authorize-security-group-ingress \
  --group-id sg-0123456789abcdef0 \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0

aws ec2 authorize-security-group-ingress \
  --group-id sg-0123456789abcdef0 \
  --protocol tcp \
  --port 443 \
  --cidr 0.0.0.0/0

aws ec2 authorize-security-group-ingress \
  --group-id sg-0123456789abcdef0 \
  --protocol tcp \
  --port 22 \
  --cidr YOUR_IP/32

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
EC2 Instance Creation with AWS CLI	EC2 Instance Creation with AWS CLI
User Data Script	User Data Script
Terraform EC2 Configuration	Terraform EC2 Configuration
Best Practices
✅ DO
Use security groups for network control
Attach IAM roles for AWS access
Enable CloudWatch monitoring
Use AMI for consistent deployments
Implement auto-scaling for variable load
Use EBS for persistent storage
Enable termination protection for production
Keep systems patched and updated
❌ DON'T
Use overly permissive security groups
Store credentials in user data
Ignore CloudWatch metrics
Use outdated AMIs
Create hardcoded configurations
Forget to monitor costs
Weekly Installs
297
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn