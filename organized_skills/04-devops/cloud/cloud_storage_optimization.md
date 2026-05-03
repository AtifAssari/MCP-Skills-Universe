---
rating: ⭐⭐⭐
title: cloud-storage-optimization
url: https://skills.sh/aj-geddes/useful-ai-prompts/cloud-storage-optimization
---

# cloud-storage-optimization

skills/aj-geddes/useful-ai-prompts/cloud-storage-optimization
cloud-storage-optimization
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill cloud-storage-optimization
SKILL.md
Cloud Storage Optimization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Optimize cloud storage costs and performance across multiple cloud providers using compression, intelligent tiering, data partitioning, and lifecycle management. Reduce storage costs while maintaining accessibility and compliance requirements.

When to Use
Reducing storage costs
Optimizing data access patterns
Implementing tiered storage strategies
Archiving historical data
Improving data retrieval performance
Managing compliance requirements
Organizing large datasets
Optimizing data lakes and data warehouses
Quick Start

Minimal working example:

# Enable Intelligent-Tiering
aws s3api put-bucket-intelligent-tiering-configuration \
  --bucket my-bucket \
  --id OptimizedStorage \
  --intelligent-tiering-configuration '{
    "Id": "OptimizedStorage",
    "Filter": {"Prefix": "data/"},
    "Status": "Enabled",
    "Tierings": [
      {
        "Days": 90,
        "AccessTier": "ARCHIVE_ACCESS"
      },
      {
        "Days": 180,
        "AccessTier": "DEEP_ARCHIVE_ACCESS"
      }
    ]
  }'

# Analyze storage usage
aws s3api list-bucket-metrics-configurations --bucket my-bucket

# Enable S3 Select for cost optimization
aws s3api put-bucket-metrics-configuration \
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
AWS S3 Storage Optimization	AWS S3 Storage Optimization
Data Compression and Partitioning Strategy	Data Compression and Partitioning Strategy
Terraform Multi-Cloud Storage Configuration	Terraform Multi-Cloud Storage Configuration
Data Lake Partitioning Strategy	Data Lake Partitioning Strategy
Best Practices
✅ DO
Use Parquet or ORC formats for analytics
Implement tiered storage strategy
Partition data by time and queryable dimensions
Enable versioning for critical data
Use compression (gzip, snappy, brotli)
Monitor storage costs regularly
Implement data lifecycle policies
Archive infrequently accessed data
❌ DON'T
Store uncompressed data
Keep raw logs long-term
Ignore storage optimization
Use only hot storage tier
Store duplicate data
Forget to delete old test data
Weekly Installs
265
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