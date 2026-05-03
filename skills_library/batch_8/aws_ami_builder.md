---
title: aws-ami-builder
url: https://skills.sh/hashicorp/agent-skills/aws-ami-builder
---

# aws-ami-builder

skills/hashicorp/agent-skills/aws-ami-builder
aws-ami-builder
Installation
$ npx skills add https://github.com/hashicorp/agent-skills --skill aws-ami-builder
Summary

Build custom Amazon Machine Images with Packer's amazon-ebs builder.

Automates AMI creation from source AMIs using HCL templates with provisioners for customization (shell scripts, file uploads, configuration management)
Supports multi-region AMI distribution via ami_regions and flexible source AMI filtering by name, owner, and virtualization type
Authenticates via environment variables, AWS credentials file, or IAM instance profiles; includes validation and build commands for template management
Common use cases include OS patching, software pre-installation, and hardened base image creation; builds typically take 10–30 minutes and incur AWS costs for compute and storage
SKILL.md
AWS AMI Builder

Build Amazon Machine Images (AMIs) using Packer's amazon-ebs builder.

Reference: Amazon EBS Builder

Note: Building AMIs incurs AWS costs (EC2 instances, EBS storage, data transfer). Builds typically take 10-30 minutes depending on provisioning complexity.

Basic AMI Template
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = "~> 1.3"
    }
  }
}

variable "region" {
  type    = string
  default = "us-west-2"
}

locals {
  timestamp = regex_replace(timestamp(), "[- TZ:]", "")
}

source "amazon-ebs" "ubuntu" {
  region        = var.region
  instance_type = "t3.micro"

  source_ami_filter {
    filters = {
      name                = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
      root-device-type    = "ebs"
      virtualization-type = "hvm"
    }
    most_recent = true
    owners      = ["099720109477"] # Canonical
  }

  ssh_username = "ubuntu"
  ami_name     = "my-app-${local.timestamp}"

  tags = {
    Name      = "my-app"
    BuildDate = local.timestamp
  }
}

build {
  sources = ["source.amazon-ebs.ubuntu"]

  provisioner "shell" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get upgrade -y",
    ]
  }
}

Common Source AMI Filters
Ubuntu 22.04 LTS
source_ami_filter {
  filters = {
    name                = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
    root-device-type    = "ebs"
    virtualization-type = "hvm"
  }
  most_recent = true
  owners      = ["099720109477"] # Canonical
}

Amazon Linux 2023
source_ami_filter {
  filters = {
    name                = "al2023-ami-*-x86_64"
    root-device-type    = "ebs"
    virtualization-type = "hvm"
  }
  most_recent = true
  owners      = ["amazon"]
}

Multi-Region AMI
source "amazon-ebs" "ubuntu" {
  region        = "us-west-2"
  instance_type = "t3.micro"

  source_ami_filter {
    filters = {
      name = "ubuntu/images/*ubuntu-jammy-22.04-amd64-server-*"
    }
    most_recent = true
    owners      = ["099720109477"]
  }

  ssh_username = "ubuntu"
  ami_name     = "my-app-${local.timestamp}"

  # Copy to additional regions
  ami_regions = ["us-east-1", "us-east-2", "eu-west-1"]
}

Authentication

Packer uses AWS credential resolution:

Environment variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
AWS credentials file: ~/.aws/credentials
IAM instance profile (when running on EC2)
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_REGION="us-west-2"

packer build .

Build Commands
# Initialize plugins
packer init .

# Validate template
packer validate .

# Build AMI
packer build .

# Build with variables
packer build -var "region=us-east-1" .

Common Issues

SSH Timeout

Ensure security group allows SSH (port 22)
Verify subnet has internet access

AMI Already Exists

AMI names must be unique
Use timestamp in name: my-app-${local.timestamp}

Volume Size Too Small

Check source AMI's volume size
Set launch_block_device_mappings.volume_size accordingly
References
Amazon EBS Builder
AWS AMI Documentation
Weekly Installs
775
Repository
hashicorp/agent-skills
GitHub Stars
595
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass