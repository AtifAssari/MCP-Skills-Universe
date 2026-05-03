---
title: terraform-tasks
url: https://skills.sh/josiahsiegel/claude-plugin-marketplace/terraform-tasks
---

# terraform-tasks

skills/josiahsiegel/claude-plugin-marketplace/terraform-tasks
terraform-tasks
Installation
$ npx skills add https://github.com/josiahsiegel/claude-plugin-marketplace --skill terraform-tasks
SKILL.md
Terraform Tasks Skill
🚨 CRITICAL GUIDELINES
Windows File Path Requirements

MANDATORY: Always Use Backslashes on Windows for File Paths

When using Edit or Write tools on Windows, you MUST use backslashes (\) in file paths, NOT forward slashes (/).

Examples:

❌ WRONG: D:/repos/project/file.tsx
✅ CORRECT: D:\repos\project\file.tsx

This applies to:

Edit tool file_path parameter
Write tool file_path parameter
All file operations on Windows systems
Documentation Guidelines

NEVER create new documentation files unless explicitly requested by the user.

Priority: Update existing README.md files rather than creating new documentation
Repository cleanliness: Keep repository root clean - only README.md unless user requests otherwise
Style: Documentation should be concise, direct, and professional - avoid AI-generated tone
User preference: Only create additional .md files when user specifically asks for documentation

This skill enables autonomous execution of complex Terraform tasks with comprehensive provider knowledge and platform awareness.

Capabilities
1. Infrastructure Code Generation

Generate complete, production-ready Terraform code for any cloud provider:

Process:

Determine provider and version from user context
Research latest provider documentation if needed
Generate complete configurations with:
Provider version constraints
Resource configurations
Variables with validation
Outputs
Security best practices
Platform-specific considerations

Example Tasks:

"Create Azure Storage Account with private endpoints and customer-managed keys"
"Generate AWS VPC with 3-tier architecture and NAT gateways"
"Build GCP GKE cluster with Workload Identity and node pools"
2. Version Management

Handle Terraform and provider version upgrades:

Process:

Check current versions
Research changelogs and breaking changes
Propose upgrade path
Generate migration code
Provide testing strategy

Example Tasks:

"Upgrade from AzureRM provider 2.x to 3.x"
"Migrate Terraform 0.12 code to 1.x"
"Update all providers to latest compatible versions"
3. Debugging and Troubleshooting

Diagnose and fix Terraform issues:

Process:

Gather diagnostic information
Analyze error messages and logs
Identify root cause
Provide platform-specific solution
Suggest preventive measures

Example Tasks:

"Debug state lock timeout on Windows"
"Fix provider authentication failure in Azure DevOps pipeline"
"Resolve circular dependency in module structure"
4. Security Scanning and Remediation

Scan and fix security issues:

Process:

Run security scanners (tfsec, Checkov)
Analyze findings
Prioritize issues
Generate fixes
Explain security implications

Example Tasks:

"Run tfsec and fix all HIGH severity issues"
"Ensure all S3 buckets have encryption enabled"
"Implement Azure storage account with all security best practices"
5. Architecture Review

Review and improve Terraform architecture:

Process:

Analyze current structure
Identify anti-patterns
Propose improvements
Generate refactoring plan
Document decisions (ADRs)

Example Tasks:

"Review state management strategy for 500+ resources"
"Design multi-region architecture for high availability"
"Refactor monolithic state into layered approach"
6. CI/CD Pipeline Generation

Create complete CI/CD pipelines:

Process:

Determine CI/CD platform
Understand environment strategy
Generate pipeline configuration
Include security scanning
Add approval gates
Implement drift detection

Example Tasks:

"Create Azure DevOps pipeline with multi-stage deployment"
"Generate GitHub Actions workflow with OIDC authentication"
"Build GitLab CI pipeline with Terraform Cloud backend"
7. Module Development

Create reusable Terraform modules:

Process:

Design module interface
Implement with best practices
Add variable validation
Generate documentation
Create examples
Set up testing

Example Tasks:

"Create Azure networking module with hub-spoke pattern"
"Build AWS ECS module with auto-scaling and ALB"
"Develop GCP Cloud Run module with custom domains"
8. Migration Tasks

Migrate infrastructure to Terraform:

Process:

Inventory existing resources
Generate import commands
Create matching Terraform code
Validate configurations
Test import process
Plan cutover strategy

Example Tasks:

"Import existing Azure resources into Terraform"
"Migrate from CloudFormation to Terraform"
"Convert ARM templates to Terraform HCL"
Autonomous Behavior

This skill operates autonomously with minimal user intervention:

Information Gathering
Automatically detect Terraform and provider versions
Identify platform (Windows/Linux/macOS)
Detect CI/CD environment
Check for existing configurations
Research
Use WebSearch to find current documentation
Check provider changelogs for breaking changes
Research best practices
Find platform-specific solutions
Code Generation
Generate complete, working code
Include all necessary files (main.tf, variables.tf, outputs.tf, etc.)
Add comprehensive comments
Follow naming conventions
Apply security best practices
Validation
Run terraform fmt on generated code
Validate syntax
Check for security issues
Test configurations when possible
Documentation
Explain architectural decisions
Document usage examples
Note version compatibility
Include troubleshooting tips
Error Handling

When encountering issues:

Gather Context: Collect all relevant information
Research: Look up error messages and solutions
Platform Awareness: Consider OS-specific issues
Multiple Solutions: Provide alternatives when available
Prevention: Suggest how to avoid similar issues
Platform-Specific Considerations
Windows
PowerShell syntax for commands
Path handling (backslashes)
Line ending considerations
Execution policy issues
Credential management
Linux/macOS
Bash syntax for commands
File permissions
Package managers
Environment variables
CI/CD Environments
Pipeline-specific syntax
Agent capabilities
Authentication methods
Artifact handling
Quality Standards

All generated Terraform code must:

Be properly formatted (terraform fmt)
Pass validation (terraform validate)
Include security best practices
Have comprehensive variable validation
Include meaningful descriptions
Follow naming conventions
Be version-compatible
Include usage examples
Have proper output definitions
Provider Expertise
Azure (AzureRM)
All resource types
AzAPI for preview features
Service endpoints and private endpoints
Managed identities
RBAC and policies
AWS
All services
IAM roles and policies
VPC networking
S3 backend configuration
Cross-account deployments
Google Cloud
All GCP services
IAM and service accounts
VPC and networking
GCS backend configuration
Organization and folder policies
Community Providers
Kubernetes and Helm
Datadog, PagerDuty
GitHub, GitLab
HashiCorp Vault
And more...
Examples
Example 1: Generate Azure Storage Account

User Request: "Create an Azure Storage Account with all security best practices"

Skill Actions:

Detect/ask for AzureRM provider version
Research latest security requirements
Generate complete configuration:
Storage account with secure settings
Private endpoint
Diagnostic settings
Customer-managed encryption keys
Network rules
Variables with validation
Outputs
Include usage examples
Add security scanner ignore comments where appropriate with explanations
Example 2: Debug Plan Failure

User Request: "My terraform plan is failing with authentication error on Windows"

Skill Actions:

Ask for error details
Identify it's Azure CLI authentication
Provide Windows-specific solution:
PowerShell commands to check authentication
How to refresh credentials
Environment variable configuration
Alternative authentication methods
Explain root cause
Suggest prevention
Example 3: Architecture Review

User Request: "Review my Terraform structure, I have 1000+ resources in one state file"

Skill Actions:

Analyze current structure
Identify issues:
Large state file
Slow operations
Large blast radius
Propose layered architecture:
Split into foundation/platform/apps
Separate state files
Remote state data sources
Generate migration plan
Create ADR documenting decision
Provide implementation steps
Integration with terraform-expert Agent

This skill works in tandem with the terraform-expert agent:

Agent provides strategic guidance
Skill executes tactical tasks
Agent validates skill outputs
Skill reports back to agent

Use this skill when you need to autonomously execute Terraform tasks with comprehensive provider knowledge and platform awareness.

Weekly Installs
82
Repository
josiahsiegel/cl…ketplace
GitHub Stars
33
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn