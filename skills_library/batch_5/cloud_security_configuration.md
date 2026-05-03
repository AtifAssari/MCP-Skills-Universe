---
title: cloud-security-configuration
url: https://skills.sh/aj-geddes/useful-ai-prompts/cloud-security-configuration
---

# cloud-security-configuration

skills/aj-geddes/useful-ai-prompts/cloud-security-configuration
cloud-security-configuration
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill cloud-security-configuration
SKILL.md
Cloud Security Configuration
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Cloud security requires comprehensive strategies spanning identity management, encryption, network controls, compliance, and threat detection. Implement defense-in-depth with multiple layers of protection and continuous monitoring.

When to Use
Protecting sensitive data in cloud
Compliance with regulations (GDPR, HIPAA, PCI-DSS)
Implementing zero-trust security
Securing multi-cloud environments
Threat detection and response
Identity and access management
Network isolation and segmentation
Encryption and key management
Quick Start

Minimal working example:

# Enable GuardDuty (threat detection)
aws guardduty create-detector \
  --enable \
  --finding-publishing-frequency FIFTEEN_MINUTES

# Enable CloudTrail (audit logging)
aws cloudtrail create-trail \
  --name organization-trail \
  --s3-bucket-name audit-bucket \
  --is-multi-region-trail

# Enable S3 bucket encryption by default
aws s3api put-bucket-encryption \
  --bucket my-bucket \
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms",
        "KMSMasterKeyID": "arn:aws:kms:region:account:key/key-id"
      },
      "BucketKeyEnabled": true
    }]
  }'

# Enable VPC Flow Logs
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
AWS Security Configuration	AWS Security Configuration
Terraform Security Configuration	Terraform Security Configuration
Azure Security Configuration	Azure Security Configuration
GCP Security Configuration	GCP Security Configuration
Best Practices
✅ DO
Implement least privilege access
Enable MFA everywhere
Use service accounts for applications
Encrypt data at rest and in transit
Enable comprehensive logging
Implement network segmentation
Use secrets management
Enable threat detection
Regular security assessments
Keep systems patched
❌ DON'T
Use root/default credentials
Store secrets in code
Over-permissive security groups
Disable encryption
Ignore logs and monitoring
Share credentials
Skip compliance requirements
Trust unverified data sources
Weekly Installs
287
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass