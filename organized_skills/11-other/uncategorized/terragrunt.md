---
rating: ⭐⭐
title: terragrunt
url: https://skills.sh/jfr992/terragrunt-skill/terragrunt
---

# terragrunt

skills/jfr992/terragrunt-skill/terragrunt
terragrunt
Installation
$ npx skills add https://github.com/jfr992/terragrunt-skill --skill terragrunt
SKILL.md
Terragrunt Infrastructure Skill
Overview

This skill provides guidance for infrastructure using Terragrunt with OpenTofu, following a three-repository pattern:

Infrastructure Catalog - Units and stacks that reference modules from separate repos
Infrastructure Live - Environment-specific deployments consuming the catalog
Module Repos - Separate repositories for each OpenTofu module (independent versioning)
Quick Navigation
Topic	Reference
Naming conventions	naming.md
Catalog structure	catalog-structure.md
Live repo structure	live-structure.md
Root/account/env configs	root-config.md
Unit dependencies	dependencies.md
Catalog scaffolding	catalog-scaffolding.md
Stack commands	stack-commands.md
Patterns & best practices	patterns.md
State management	state-management.md
Multi-account setup	multi-account.md
Performance optimization	performance.md
CI/CD pipelines	cicd-pipelines.md
Core Concepts
Values Pattern

Units receive configuration through values.xxx:

inputs = {
  name        = values.name
  environment = values.environment
  instance_class = try(values.instance_class, "db.t3.medium")  # Optional with default
}

Reference Resolution

Units resolve symbolic references like "../acm" to dependency outputs:

inputs = {
  acm_certificate_arn = try(values.acm_certificate_arn, "") == "../acm" ?
    dependency.acm.outputs.acm_certificate_arn :
    values.acm_certificate_arn
}

Module Sourcing

Units reference modules via Git URL with version from values:

terraform {
  source = "git::git@github.com:YOUR_ORG/modules/rds.git//app?ref=${values.version}"
}

Common Operations
Create New Unit
Create units/<name>/terragrunt.hcl
Reference module via Git URL with ${values.version}
Use values.xxx for inputs
Add dependencies with mock outputs
Implement reference resolution for "../unit" patterns
Create New Stack
Create stacks/<name>/terragrunt.stack.hcl
Define locals for computed values
Add unit blocks referencing catalog units
Pass values including version and dependency paths
Deploy to New Environment
Create environment directory structure
Add env.hcl with state_bucket_suffix
Run ./setup-state-backend.sh to create state resources
Add stack files referencing catalog
Best Practices
Pin module versions - Use Git tags in values.version
Pin catalog versions - Use refs in unit source URLs
Use reference resolution - "../unit" → dependency outputs
Provide mock outputs - Enable plan/validate without dependencies
Auto-detect features - length(keys(try(values.X, {}))) > 0
Override paths - try(values.X_path, "../default")
Separate state per environment - Use state_bucket_suffix
Common Pitfalls
Git refspec error - Use //path?ref=branch NOT ?ref=branch//path
Heredoc in ternary - Wrap in parentheses: condition ? (\n<<-EOF\n...\nEOF\n) : ""
Missing mock outputs - Always provide for plan/validate
Hardcoded paths - Use local paths only for testing
Version Management
Development: Branch refs (ref=feature-branch)
Testing: RC tags (ref=v1.0.0-rc1)
Production: Stable tags (ref=v1.0.0)
Weekly Installs
32
Repository
jfr992/terragrunt-skill
GitHub Stars
20
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn