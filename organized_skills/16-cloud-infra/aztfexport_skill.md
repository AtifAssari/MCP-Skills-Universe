---
rating: ⭐⭐⭐
title: aztfexport-skill
url: https://skills.sh/julianobarbosa/claude-code-skills/aztfexport-skill
---

# aztfexport-skill

skills/julianobarbosa/claude-code-skills/aztfexport-skill
aztfexport-skill
Installation
$ npx skills add https://github.com/julianobarbosa/claude-code-skills --skill aztfexport-skill
SKILL.md
aztfexport — Export Azure Resources to Terraform
Overview

aztfexport is a Microsoft tool that exports existing Azure resources into Terraform HCL + state. It reverse-engineers live Azure infrastructure into Terraform configurations. Use this for Azure-only workflows or Terraform versions before 1.14's native terraform query.

When to Use
Export a single Azure resource to Terraform → aztfexport resource
Export an entire resource group → aztfexport resource-group
Export resources matching an Azure Resource Graph query → aztfexport query
Bootstrapping IaC from existing Azure infrastructure

Use terraform-search-import skill instead when: Terraform >= 1.14 with terraform query + bulk import (multi-cloud, not Azure-specific).

Prerequisites
aztfexport installed: brew install aztfexport (macOS) or see GitHub releases
Azure CLI authenticated: az login + correct subscription selected
Architecture check (critical on macOS):
file $(which aztfexport)  # Check binary arch
uname -m                  # Check system arch

If mismatch (e.g., x86_64 binary on arm64 Mac), reinstall the correct architecture version.
Workflow
Step 1: Discover the Resource ID

Use Azure CLI to find the resource ID. See references/RESOURCE-DISCOVERY.md for patterns by resource type.

Generic fallback:

az resource list --query "[?name=='RESOURCE_NAME']" -o table

Step 2: Validate aztfexport Binary
file $(which aztfexport)
uname -m
aztfexport --version


Architecture mismatch causes cryptic failures. Always verify before first use on a new machine.

Step 3: Run aztfexport

Single resource:

aztfexport resource \
  --non-interactive \
  --plain-ui \
  -o ./terraform-export \
  "/subscriptions/SUB_ID/resourceGroups/RG/providers/TYPE/NAME"


Resource group:

aztfexport resource-group \
  --non-interactive \
  --plain-ui \
  -o ./terraform-export \
  RESOURCE_GROUP_NAME


Azure Resource Graph query:

aztfexport query \
  --non-interactive \
  --plain-ui \
  -o ./terraform-export \
  "resources | where name == 'MY_RESOURCE'"

Step 4: Review Generated Files
ls ./terraform-export/
# Expect: main.tf, provider.tf, terraform.tfstate, import.tf (sometimes)

main.tf — generated HCL with res-0 style resource names
provider.tf — AzureRM provider configuration
terraform.tfstate — imported state file
Consider renaming res-0 to descriptive names (update both HCL and state)
Step 5: Verify
cd ./terraform-export
terraform init
terraform plan


A clean plan (no changes) confirms successful export. Minor diffs may appear for computed attributes — review and suppress with lifecycle { ignore_changes } if appropriate.

Critical Flags
Flag	Purpose	When Required
--non-interactive	Skip interactive prompts	Always in CI/headless/Claude
--plain-ui	Disable TUI (terminal UI)	Always pair with --non-interactive — without it, fails when no /dev/tty
-o <dir>	Output directory	Always (must be empty or non-existent)
--append	Append to existing Terraform dir	When adding to existing config (but see gotcha below)
--overwrite	Overwrite existing files	When re-exporting to same directory
--hcl-only	Generate HCL without importing state	When you only need the code
Gotchas & Troubleshooting
Problem	Cause	Solution
Binary crashes silently or exec format error	Architecture mismatch (x86 on ARM Mac)	Run file $(which aztfexport) + uname -m, reinstall correct arch
--non-interactive alone fails	No /dev/tty in headless environments	Always pair with --plain-ui
"directory is not empty" error	Output dir has files	Use -o <fresh-dir> or --overwrite
--append fails on non-empty dir without state	aztfexport expects existing Terraform state	Use -o to a fresh subdirectory instead
Can't find Azure resource ID	Resource type unknown or wrong API	Try multiple az commands — see RESOURCE-DISCOVERY.md
res-0 style names in output	Default aztfexport naming	Rename post-export in both HCL and state
terraform plan shows diffs after export	Computed/server-side attributes	Review diffs — use ignore_changes for benign ones
Example: Export an Activity Log Alert
# Step 1: Find the resource ID
az monitor activity-log alert list -g myResourceGroup \
  --query "[?name=='my-alert'].id" -o tsv

# Step 2: Export
aztfexport resource \
  --non-interactive \
  --plain-ui \
  -o ./alert-export \
  "/subscriptions/xxxx/resourceGroups/myRG/providers/Microsoft.Insights/activityLogAlerts/my-alert"

# Step 3: Verify
cd ./alert-export
terraform init
terraform plan

Weekly Installs
13
Repository
julianobarbosa/…e-skills
GitHub Stars
64
First Seen
Mar 10, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass