---
title: aws-s3-management
url: https://skills.sh/aj-geddes/useful-ai-prompts/aws-s3-management
---

# aws-s3-management

skills/aj-geddes/useful-ai-prompts/aws-s3-management
aws-s3-management
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill aws-s3-management
SKILL.md
AWS S3 Management
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Amazon S3 provides secure, durable, and highly scalable object storage. Manage buckets with encryption, versioning, access controls, lifecycle policies, and cross-region replication for reliable data storage and retrieval.

When to Use
Static website hosting
Data backup and archival
Media library and CDN origin
Data lake and analytics
Log storage and analysis
Application asset storage
Disaster recovery
Data sharing and collaboration
Quick Start

Minimal working example:

# Create bucket
aws s3api create-bucket \
  --bucket my-app-bucket-$(date +%s) \
  --region us-east-1

# Enable versioning
aws s3api put-bucket-versioning \
  --bucket my-app-bucket \
  --versioning-configuration Status=Enabled

# Block public access
aws s3api put-public-access-block \
  --bucket my-app-bucket \
  --public-access-block-configuration \
    BlockPublicAcls=true,IgnorePublicAcls=true,\
    BlockPublicPolicy=true,RestrictPublicBuckets=true

# Enable encryption
aws s3api put-bucket-encryption \
  --bucket my-app-bucket \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
S3 Bucket Creation and Configuration with AWS CLI	S3 Bucket Creation and Configuration with AWS CLI
S3 Lifecycle Policy Configuration	S3 Lifecycle Policy Configuration
Terraform S3 Configuration	Terraform S3 Configuration
S3 Access with Presigned URLs	S3 Access with Presigned URLs
Best Practices
✅ DO
Enable versioning for important data
Use server-side encryption
Block public access by default
Implement lifecycle policies
Enable logging and monitoring
Use bucket policies for access control
Enable MFA delete for critical buckets
Use IAM roles instead of access keys
Implement cross-region replication
❌ DON'T
Make buckets publicly accessible
Store sensitive credentials
Ignore CloudTrail logging
Use overly permissive policies
Forget to set lifecycle rules
Ignore encryption requirements
Weekly Installs
363
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass