---
title: terraform-azurerm-set-diff-analyzer
url: https://skills.sh/github/awesome-copilot/terraform-azurerm-set-diff-analyzer
---

# terraform-azurerm-set-diff-analyzer

skills/github/awesome-copilot/terraform-azurerm-set-diff-analyzer
terraform-azurerm-set-diff-analyzer
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill terraform-azurerm-set-diff-analyzer
Summary

Identify false-positive diffs in Terraform AzureRM plans caused by Set-type attribute ordering.

Analyzes terraform plan JSON output to distinguish spurious diffs (element reordering in Sets) from actual resource changes
Targets AzureRM resources with Set-type attributes: Application Gateway, Load Balancer, NSG, Firewall, Front Door, and others
Requires Python 3.8+ and uses only standard library; integrates into CI/CD pipelines with configurable output formats and exit codes
Helps reviewers focus on meaningful changes when terraform plan shows "all elements changed" despite minimal actual modifications
SKILL.md
Terraform AzureRM Set Diff Analyzer

A skill to identify "false-positive diffs" in Terraform plans caused by AzureRM Provider's Set-type attributes and distinguish them from actual changes.

When to Use
terraform plan shows many changes, but you only added/removed a single element
Application Gateway, Load Balancer, NSG, etc. show "all elements changed"
You want to automatically filter false-positive diffs in CI/CD
Background

Terraform's Set type compares by position rather than by key, so when adding or removing elements, all elements appear as "changed". This is a general Terraform issue, but it's particularly noticeable with AzureRM resources that heavily use Set-type attributes like Application Gateway, Load Balancer, and NSG.

These "false-positive diffs" don't actually affect the resources, but they make reviewing terraform plan output difficult.

Prerequisites
Python 3.8+

If Python is unavailable, install via your package manager (e.g., apt install python3, brew install python3) or from python.org.

Basic Usage
# 1. Generate plan JSON output
terraform plan -out=plan.tfplan
terraform show -json plan.tfplan > plan.json

# 2. Analyze
python scripts/analyze_plan.py plan.json

Troubleshooting
python: command not found: Use python3 instead, or install Python
ModuleNotFoundError: Script uses only standard library; ensure Python 3.8+
Detailed Documentation
scripts/README.md - All options, output formats, exit codes, CI/CD examples
references/azurerm_set_attributes.md - Supported resources and attributes
Weekly Installs
8.5K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass