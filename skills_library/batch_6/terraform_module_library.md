---
title: terraform-module-library
url: https://skills.sh/wshobson/agents/terraform-module-library
---

# terraform-module-library

skills/wshobson/agents/terraform-module-library
terraform-module-library
Installation
$ npx skills add https://github.com/wshobson/agents --skill terraform-module-library
Summary

Reusable Terraform modules for AWS, Azure, GCP, and OCI infrastructure with standardized patterns and best practices.

Provides pre-built module templates across four cloud providers covering core services like VPC/VNet, Kubernetes clusters, databases, and object storage
Enforces consistent module structure with input variables, outputs, documentation, examples, and Terratest-based testing
Includes validation blocks, conditional resources via count/for_each, and tagging strategies for production-ready infrastructure
Supports module composition for multi-resource deployments and semantic versioning for dependency management
SKILL.md
Terraform Module Library

Production-ready Terraform module patterns for AWS, Azure, GCP, and OCI infrastructure.

Purpose

Create reusable, well-tested Terraform modules for common cloud infrastructure patterns across multiple cloud providers.

When to Use
Build reusable infrastructure components
Standardize cloud resource provisioning
Implement infrastructure as code best practices
Create multi-cloud compatible modules
Establish organizational Terraform standards
Module Structure
terraform-modules/
├── aws/
│   ├── vpc/
│   ├── eks/
│   ├── rds/
│   └── s3/
├── azure/
│   ├── vnet/
│   ├── aks/
│   └── storage/
├── gcp/
│   ├── vpc/
│   ├── gke/
│   └── cloud-sql/
└── oci/
    ├── vcn/
    ├── oke/
    └── object-storage/

Standard Module Pattern
module-name/
├── main.tf          # Main resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider versions
├── README.md        # Documentation
├── examples/        # Usage examples
│   └── complete/
│       ├── main.tf
│       └── variables.tf
└── tests/           # Terratest files
    └── module_test.go

AWS VPC Module Example

main.tf:

resource "aws_vpc" "main" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = var.enable_dns_support

  tags = merge(
    {
      Name = var.name
    },
    var.tags
  )
}

resource "aws_subnet" "private" {
  count             = length(var.private_subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]

  tags = merge(
    {
      Name = "${var.name}-private-${count.index + 1}"
      Tier = "private"
    },
    var.tags
  )
}

resource "aws_internet_gateway" "main" {
  count  = var.create_internet_gateway ? 1 : 0
  vpc_id = aws_vpc.main.id

  tags = merge(
    {
      Name = "${var.name}-igw"
    },
    var.tags
  )
}


variables.tf:

variable "name" {
  description = "Name of the VPC"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string
  validation {
    condition     = can(regex("^([0-9]{1,3}\\.){3}[0-9]{1,3}/[0-9]{1,2}$", var.cidr_block))
    error_message = "CIDR block must be valid IPv4 CIDR notation."
  }
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for private subnets"
  type        = list(string)
  default     = []
}

variable "enable_dns_hostnames" {
  description = "Enable DNS hostnames in VPC"
  type        = bool
  default     = true
}

variable "tags" {
  description = "Additional tags"
  type        = map(string)
  default     = {}
}


outputs.tf:

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "private_subnet_ids" {
  description = "IDs of private subnets"
  value       = aws_subnet.private[*].id
}

output "vpc_cidr_block" {
  description = "CIDR block of VPC"
  value       = aws_vpc.main.cidr_block
}

Best Practices
Use semantic versioning for modules
Document all variables with descriptions
Provide examples in examples/ directory
Use validation blocks for input validation
Output important attributes for module composition
Pin provider versions in versions.tf
Use locals for computed values
Implement conditional resources with count/for_each
Test modules with Terratest
Tag all resources consistently

Reference: See references/aws-modules.md and references/oci-modules.md

Module Composition
module "vpc" {
  source = "../../modules/aws/vpc"

  name               = "production"
  cidr_block         = "10.0.0.0/16"
  availability_zones = ["us-west-2a", "us-west-2b", "us-west-2c"]

  private_subnet_cidrs = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24"
  ]

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}

module "rds" {
  source = "../../modules/aws/rds"

  identifier     = "production-db"
  engine         = "postgres"
  engine_version = "15.3"
  instance_class = "db.t3.large"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnet_ids

  tags = {
    Environment = "production"
  }
}

Testing
// tests/vpc_test.go
package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestVPCModule(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../examples/complete",
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    vpcID := terraform.Output(t, terraformOptions, "vpc_id")
    assert.NotEmpty(t, vpcID)
}

Related Skills
multi-cloud-architecture - For architectural decisions
cost-optimization - For cost-effective designs
Weekly Installs
9.6K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass