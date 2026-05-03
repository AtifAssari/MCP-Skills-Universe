---
rating: ⭐⭐⭐
title: terraform-infrastructure
url: https://skills.sh/aj-geddes/useful-ai-prompts/terraform-infrastructure
---

# terraform-infrastructure

skills/aj-geddes/useful-ai-prompts/terraform-infrastructure
terraform-infrastructure
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill terraform-infrastructure
SKILL.md
Terraform Infrastructure
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build scalable infrastructure as code with Terraform, managing AWS, Azure, GCP, and on-premise resources through declarative configuration, remote state, and automated provisioning.

When to Use
Cloud infrastructure provisioning
Multi-environment management (dev, staging, prod)
Infrastructure versioning and code review
Cost tracking and resource optimization
Disaster recovery and environment replication
Automated infrastructure testing
Cross-region deployments
Quick Start

Minimal working example:

# terraform/main.tf
terraform {
  required_version = ">= 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # Remote state configuration
  backend "s3" {
    bucket         = "terraform-state-prod"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
AWS Infrastructure Module	AWS Infrastructure Module
Variables and Outputs	Variables and Outputs
Terraform Deployment Script	Terraform Deployment Script
Best Practices
✅ DO
Use remote state (S3, Terraform Cloud)
Implement state locking (DynamoDB)
Organize code into modules
Use workspaces for environments
Apply tags consistently
Use variables for flexibility
Implement code review before apply
Keep sensitive data in separate variable files
❌ DON'T
Store state files locally in git
Use hardcoded values
Mix environments in single state
Skip terraform plan review
Use root module for everything
Store secrets in code
Disable state locking
Weekly Installs
372
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