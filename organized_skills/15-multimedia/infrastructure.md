---
rating: ⭐⭐⭐
title: infrastructure
url: https://skills.sh/nguyenhuuca/assessment/infrastructure
---

# infrastructure

skills/nguyenhuuca/assessment/infrastructure
infrastructure
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill infrastructure
SKILL.md
Infrastructure as Code
Principles
Everything in Code: No manual changes
Version Controlled: All changes tracked
Idempotent: Safe to run multiple times
Tested: Validate before apply
Terraform Basics
Project Structure
infrastructure/
├── main.tf           # Main configuration
├── variables.tf      # Input variables
├── outputs.tf        # Output values
├── providers.tf      # Provider config
├── terraform.tfvars  # Variable values
└── modules/
    └── vpc/          # Reusable modules

Example: AWS VPC
# providers.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# main.tf
resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr

  tags = {
    Name        = "${var.project}-vpc"
    Environment = var.environment
  }
}

# variables.tf
variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

Workflows
# Initialize
terraform init

# Plan changes
terraform plan -out=tfplan

# Apply changes
terraform apply tfplan

# Destroy resources
terraform destroy

Best Practices
Use Remote State: Store state in S3/GCS
Lock State: Prevent concurrent modifications
Use Modules: Reusable infrastructure components
Environment Separation: Separate state per environment
Secret Management: Never store secrets in code
State Management
terraform {
  backend "s3" {
    bucket         = "terraform-state-bucket"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}

ECS/Fargate
# Task Definition
resource "aws_ecs_task_definition" "app" {
  family                   = "${var.project}-task"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = 256
  memory                   = 512
  execution_role_arn       = aws_iam_role.ecs_execution.arn

  container_definitions = jsonencode([{
    name  = "app"
    image = "${aws_ecr_repository.app.repository_url}:latest"
    portMappings = [{
      containerPort = 8080
      protocol      = "tcp"
    }]
    logConfiguration = {
      logDriver = "awslogs"
      options = {
        awslogs-group         = aws_cloudwatch_log_group.app.name
        awslogs-region        = var.aws_region
        awslogs-stream-prefix = "app"
      }
    }
  }])
}

# ECS Service
resource "aws_ecs_service" "app" {
  name            = "${var.project}-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = var.app_count
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = aws_subnet.private[*].id
    security_groups = [aws_security_group.app.id]
  }
}

S3 Buckets
resource "aws_s3_bucket" "assets" {
  bucket = "${var.project}-assets-${var.environment}"
}

resource "aws_s3_bucket_versioning" "assets" {
  bucket = aws_s3_bucket.assets.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "assets" {
  bucket = aws_s3_bucket.assets.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

Weekly Installs
11
Repository
nguyenhuuca/assessment
GitHub Stars
24
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass