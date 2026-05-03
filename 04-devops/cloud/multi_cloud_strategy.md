---
rating: ⭐⭐⭐
title: multi-cloud-strategy
url: https://skills.sh/aj-geddes/useful-ai-prompts/multi-cloud-strategy
---

# multi-cloud-strategy

skills/aj-geddes/useful-ai-prompts/multi-cloud-strategy
multi-cloud-strategy
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill multi-cloud-strategy
SKILL.md
Multi-Cloud Strategy
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Multi-cloud strategies enable leveraging multiple cloud providers for flexibility, redundancy, and optimization. Avoid vendor lock-in, optimize costs by comparing cloud services, and implement hybrid deployments with seamless data synchronization.

When to Use
Reducing vendor lock-in risk
Optimizing costs across providers
Geographic distribution requirements
Compliance with regional data laws
Disaster recovery and high availability
Hybrid cloud deployments
Multi-region application deployment
Avoiding single cloud provider dependency
Quick Start

Minimal working example:

# Multi-cloud compute abstraction
from abc import ABC, abstractmethod
from enum import Enum

class CloudProvider(Enum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"

class ComputeInstance(ABC):
    """Abstract compute instance"""
    @abstractmethod
    def start(self): pass

    @abstractmethod
    def stop(self): pass

    @abstractmethod
    def get_status(self): pass

# AWS implementation
import boto3

class AWSComputeInstance(ComputeInstance):
    def __init__(self, instance_id, region='us-east-1'):
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Multi-Cloud Abstraction Layer	Multi-Cloud Abstraction Layer
Multi-Cloud Kubernetes Deployment	Multi-Cloud Kubernetes Deployment
Terraform Multi-Cloud Configuration	Terraform Multi-Cloud Configuration
Data Synchronization across Clouds	Data Synchronization across Clouds
Best Practices
✅ DO
Use cloud-agnostic APIs and frameworks
Implement abstraction layers
Monitor costs across clouds
Use Kubernetes for portability
Plan for data residency requirements
Test failover scenarios
Document cloud-specific configurations
Use infrastructure as code
❌ DON'T
Use cloud-specific services extensively
Create hard dependencies on one provider
Ignore compliance requirements
Forget about data transfer costs
Neglect network latency issues
Skip disaster recovery planning
Weekly Installs
255
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