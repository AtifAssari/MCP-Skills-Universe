---
rating: ⭐⭐
title: new-terraform-provider
url: https://skills.sh/hashicorp/agent-skills/new-terraform-provider
---

# new-terraform-provider

skills/hashicorp/agent-skills/new-terraform-provider
new-terraform-provider
Installation
$ npx skills add https://github.com/hashicorp/agent-skills --skill new-terraform-provider
Summary

Scaffold a new Terraform provider using the Plugin Framework.

Generates a new Go module workspace with the standard "terraform-provider-" naming convention and initializes required dependencies
Provides a template main.go file following HashiCorp's Plugin Framework patterns, with TODO markers for customization
Validates the setup by running build and test commands to ensure the provider compiles and passes initial checks
Handles workspace management by confirming intent before creating a new provider directory if already in an existing Terraform provider workspace
SKILL.md

To scaffold a new Terraform provider with Plugin Framework:

If I am already in a Terraform provider workspace, then confirm that I want to create a new workspace. If I do not want to create a new workspace, then skip all remaining steps.
Create a new workspace root directory. The root directory name should be prefixed with "terraform-provider-". Perform all subsequent steps in this new workspace.
Initialize a new Go module..
Run go get -u github.com/hashicorp/terraform-plugin-framework@latest.
Write a main.go file that follows the example.
Remove TODO comments from main.go
Run go mod tidy
Run go build -o /dev/null
Run go test ./...
Weekly Installs
1.2K
Repository
hashicorp/agent-skills
GitHub Stars
595
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass