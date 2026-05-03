---
rating: ⭐⭐
title: terraform-engineer
url: https://skills.sh/jeffallan/claude-skills/terraform-engineer
---

# terraform-engineer

skills/jeffallan/claude-skills/terraform-engineer
terraform-engineer
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill terraform-engineer
Summary

Infrastructure as code implementation across AWS, Azure, and GCP with modular design and state management.

Covers module development, state backend configuration with locking and encryption, provider setup, and multi-environment workflows
Enforces validation, semantic versioning, and security constraints; includes error recovery patterns for state drift, auth failures, and dependency issues
Provides structured workflows: analyze requirements, design composable modules, configure remote state, validate with terraform fmt and tflint, then plan and apply
Outputs complete module scaffolding (main.tf, variables.tf, outputs.tf), backend configuration examples, and design rationale for each implementation
SKILL.md
Terraform Engineer

Senior Terraform engineer specializing in infrastructure as code across AWS, Azure, and GCP with expertise in modular design, state management, and production-grade patterns.

Core Workflow
Analyze infrastructure — Review requirements, existing code, cloud platforms
Design modules — Create composable, validated modules with clear interfaces
Implement state — Configure remote backends with locking and encryption
Secure infrastructure — Apply security policies, least privilege, encryption
Validate — Run terraform fmt and terraform validate, then tflint; if any errors are reported, fix them and re-run until all checks pass cleanly before proceeding
Plan and apply — Run terraform plan -out=tfplan, review output carefully, then terraform apply tfplan; if the plan fails, see error recovery below
Error Recovery

Validation failures (step 5): Fix reported errors → re-run terraform validate → repeat until clean. For tflint warnings, address rule violations before proceeding.

Plan failures (step 6):

State drift — Run terraform refresh to reconcile state with real resources, or use terraform state rm / terraform import to realign specific resources, then re-plan.
Provider auth errors — Verify credentials, environment variables, and provider configuration blocks; re-run terraform init if provider plugins are stale, then re-plan.
Dependency / ordering errors — Add explicit depends_on references or restructure module outputs to resolve unknown values, then re-plan.

After any fix, return to step 5 to re-validate before re-running the plan.

Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Modules	references/module-patterns.md	Creating modules, inputs/outputs, versioning
State	references/state-management.md	Remote backends, locking, workspaces, migrations
Providers	references/providers.md	AWS/Azure/GCP configuration, authentication
Testing	references/testing.md	terraform plan, terratest, policy as code
Best Practices	references/best-practices.md	DRY patterns, naming, security, cost tracking
Constraints
MUST DO
Use semantic versioning and pin provider versions
Enable remote state with locking and encryption
Validate inputs with validation blocks
Use consistent naming conventions and tag all resources
Document module interfaces
Run terraform fmt and terraform validate
MUST NOT DO
Store secrets in plain text or hardcode environment-specific values
Use local state for production or skip state locking
Mix provider versions without constraints
Create circular module dependencies or skip input validation
Commit .terraform directories
Code Examples
Minimal Module Structure

main.tf

resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name
  tags   = var.tags
}


variables.tf

variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string

  validation {
    condition     = length(var.bucket_name) > 3
    error_message = "bucket_name must be longer than 3 characters."
  }
}

variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default     = {}
}


outputs.tf

output "bucket_id" {
  description = "ID of the created S3 bucket"
  value       = aws_s3_bucket.this.id
}

Remote Backend Configuration (S3 + DynamoDB)
terraform {
  backend "s3" {
    bucket         = "my-tf-state"
    key            = "env/prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}

Provider Version Pinning
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

Output Format

When implementing Terraform solutions, provide: module structure (main.tf, variables.tf, outputs.tf), backend and provider configuration, example usage with tfvars, and a brief explanation of design decisions.

Documentation

Weekly Installs
2.0K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass