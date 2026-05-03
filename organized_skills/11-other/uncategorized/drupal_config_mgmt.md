---
rating: ⭐⭐⭐
title: drupal-config-mgmt
url: https://skills.sh/grasmash/drupal-claude-skills/drupal-config-mgmt
---

# drupal-config-mgmt

skills/grasmash/drupal-claude-skills/drupal-config-mgmt
drupal-config-mgmt
Installation
$ npx skills add https://github.com/grasmash/drupal-claude-skills --skill drupal-config-mgmt
SKILL.md
Drupal Configuration Management

Comprehensive guide for Drupal configuration management including imports, exports, config splits, and environment syncing.

Problem: Avoid Accidental Config Imports

CRITICAL: Remote drush commands may default to --yes depending on your hosting setup. This means commands like config:import or cim can AUTO-CONFIRM and import configuration even when you only want to inspect differences.

Dangerous vs Safe Patterns

❌ DANGEROUS - May auto-import without confirmation:

ssh user@remote.server "cd /path/to/drupal && drush cim --diff"  # DON'T DO THIS!


✅ SAFE - Shows diff without importing:

ssh user@remote.server "cd /path/to/drupal && drush cim --no --diff"


✅ SAFEST - Read-only commands:

ssh user@remote.server "cd /path/to/drupal && drush config:get config.name"
ssh user@remote.server "cd /path/to/drupal && drush config:status"

Table of Contents
Preferred Prod Config Merge Workflow
Configuration Import & Export Basics
Config Splits Overview
Complete vs Partial Splits
Config Split Commands
Safe Inspection Workflow
Syncing Config from Upstream Environments
Preferred Prod Config Merge Workflow

Purpose: Safely merge production config changes while preserving local feature work.

The Process

Step 1: Commit local changes first

git add config/default/your-new-field.yml docroot/modules/custom/your_module/your_module.module
git commit -m "feat: add new feature"


Step 2: Pull production database

ddev pull --environment=live
# Or your preferred method for pulling a remote database


Step 3: Export config from prod DB

ddev drush config:export -y


Step 4: Review git diff on config directory

git diff --stat config/           # Summary of changes
git status --short config/        # See added/modified/deleted


Step 5: Identify files to revert vs keep

Look for these patterns:

D (Deleted) - Your new feature files deleted by prod export → REVERT
M (Modified) - UUID changes from prod → KEEP
M (Modified) - Actual prod config changes → KEEP
M (Modified) - Local changes overwritten → REVERT (case by case)

Step 6: Restore your local feature files

# Restore deleted files (your new feature config)
git checkout HEAD -- config/default/field.storage.node.your_new_field.yml
git checkout HEAD -- config/default/field.field.node.bundle.your_new_field.yml

# Or restore specific modified files
git checkout HEAD -- config/default/some.config.yml


Step 7: Verify and commit prod config

git status --short config/        # Verify your files are restored
git diff config/                  # Review remaining prod changes
git add config/
git commit -m "chore: sync config from production"

Quick Reference Table
git status	Meaning	Action
D config/default/field.*.your_feature.yml	Your new feature deleted	git checkout HEAD -- <file>
M config/default/*.yml (UUID only)	Prod UUID sync	Keep (stage for commit)
M config/default/views.view.*.yml	View changed in prod	Keep (review first)
M config/default/system.*.yml	System config from prod	Keep (review first)
Example Session
# After pulling prod DB and exporting config
$ git status --short config/
 M config/default/core.entity_view_display.node.article.teaser.yml
 M config/default/field.storage.node.field_featured_image.yml
 D config/default/field.field.node.article.field_summary.yml
 D config/default/field.storage.node.field_summary.yml
 M config/default/views.view.content.yml

# The D files are our new feature - restore them
$ git checkout HEAD -- config/default/field.field.node.article.field_summary.yml \
                       config/default/field.storage.node.field_summary.yml

# Verify
$ git status --short config/
 M config/default/core.entity_view_display.node.article.teaser.yml
 M config/default/field.storage.node.field_featured_image.yml
 M config/default/views.view.content.yml

# Our feature files are no longer in the diff - commit prod changes
$ git add config/ && git commit -m "chore: sync config from production"

Configuration Import & Export Basics
Exporting Configuration

Export ALL configuration (from active config to YAML files):

# Local
ddev drush config:export
ddev drush cex

# Remote
ssh user@remote.server "cd /path/to/drupal && drush config:export"


Export a SINGLE config object:

# Get config and save to file
ddev drush config:get config.name --format=yaml > config/default/config.name.yml

# Example: Export a specific view
ddev drush config:get views.view.content --format=yaml > config/default/views.view.content.yml

Importing Configuration

Import ALL configuration (from YAML files to active config):

# Local
ddev drush config:import
ddev drush cim

# Remote (DANGEROUS - may auto-confirm!)
ssh user@remote.server "cd /path/to/drupal && drush config:import --no"  # Use --no to preview only


Import a SINGLE config object:

# Delete from active config first, then import
ddev drush config:delete config.name
ddev drush config:import --partial --source=config/default

# Or use config:set for specific values
ddev drush config:set config.name key.subkey value


Best Practice: Always preview changes first:

ddev drush config:import --no --diff  # Show what would change
ddev drush cim --no --diff            # Alias

Config Splits Overview

Config splits allow you to have environment-specific configuration that doesn't get deployed to all environments.

Common Use Cases
Local development: Enable devel, kint, stage_file_proxy
Staging/Test: Enable similar modules but different API keys
Production: Disable development modules, enable caching
How Splits Work
Base config (config/default/) - Shared across all environments
Split config (config/{split-name}/) - Environment-specific overrides
Split definition (config/default/config_split.config_split.{name}.yml) - Defines which config goes in split

When a split is active, its config takes precedence over base config.

Split Activation

Splits are activated based on conditions in their config:

Status: status: true in split config
Environment variable: Can use conditions based on env vars
Manual activation: Via admin UI or drush
Complete vs Partial Splits

CRITICAL: Understanding the difference between Complete and Partial splits is essential.

Complete Splits (Recommended for most cases)

How it works:

Config in the split is ONLY active when split is enabled
When split is disabled, config is completely removed from active config
Think: "This config exists ONLY in this environment"

Use cases:

Development modules (devel, kint, webprofiler)
Environment-specific modules (stage_file_proxy for local)
Testing modules (simpletest, phpunit)

Example: Local split with devel module

# config/default/config_split.config_split.local.yml
status: true
module:
  devel: 0
  kint: 0
complete_list:
  - 'core.extension'


When split is active: devel and kint are enabled When split is inactive: devel and kint are completely removed

Reference: See admin form at /admin/config/development/configuration/config-split/{split-name}:

"Complete Split: Remove the selected configuration entirely when the split is inactive. When this split is inactive, the configuration listed here will be removed from the system completely."

Partial Splits (Conditional Overrides)

How it works:

Base config exists in config/default/
Split contains overrides in config/{split-name}/
When split is active, overrides are merged with base config
When split is inactive, base config is used
Think: "This config exists everywhere, but with different values per environment"

Use cases:

API keys that differ per environment
Email settings (different SMTP per environment)
Cache settings (aggressive in prod, disabled in local)
Search server URLs (local Solr vs remote search server)

Example: Different search servers per environment

Base config (config/default/search_api.server.main.yml):

backend_config:
  connector: solr_cloud
  # Production settings


Local override (config/local/config_split.patch.search_api.server.main.yml):

backend_config:
  connector: solr
  connector_config:
    host: solr
    # Local Solr settings


When local split is active: Uses local Solr When local split is inactive: Uses production search server

Reference: See admin form at /admin/config/development/configuration/config-split/{split-name}:

"Partial Split (Conditional Override): Keep the selected configuration, but override it when the split is active. The configuration will exist in the sync directory, but the version from this split will be used instead when the split is active."

Choosing Complete vs Partial

Use Complete when:

✅ Config should NOT exist in other environments (modules, views, blocks)
✅ It's an on/off decision (enable/disable)
✅ Different environments need different features

Use Partial when:

✅ Config exists everywhere but with different VALUES
✅ Same feature, different settings (API URLs, credentials)
✅ You need the base config to be importable without the split active
Config Split Commands
CRITICAL: Active vs Exported Configuration

⚠️ IMPORTANT: When updating config split definitions, changes must be in ACTIVE configuration (database), not just exported files!

Workflow:

Edit config/default/config_split.config_split.{name}.yml
Import to make active: ddev drush config:import --partial OR use PHP (see below)
Export: ddev drush cex

Quick method - Set active config via PHP:

ddev drush php:eval "\$config = \Drupal::configFactory()->getEditable('config_split.config_split.local'); \$config->set('partial_list', ['config.name']); \$config->save();"


See examples.md for detailed workflow.

Export Config with Splits

Export ALL config including active splits:

ddev drush config:export


This exports:

Base config to config/default/
Active split config to config/{split-name}/

Export a specific split:

ddev drush config-split:export {split-name}
ddev drush csex {split-name}

Import Config with Splits

Import ALL config including active splits:

ddev drush config:import
ddev drush cim


This imports:

Base config from config/default/
Active split config from config/{split-name}/

Import a specific split:

ddev drush config-split:import {split-name}
ddev drush csim {split-name}


Import only base config (ignore splits):

ddev drush config:import --skip-modules=config_split

Activate/Deactivate Splits

Activate a split:

ddev drush config-split:activate {split-name}


Deactivate a split:

ddev drush config-split:deactivate {split-name}

Check Split Status

List all splits and their status:

ddev drush config-split:status
ddev drush css


Example output:

Split       Active  Configuration directory
local       Yes     ../config/local
dev         No      ../config/dev
test        No      ../config/test

Safe Inspection Workflow

Use config:get and config:status for read-only inspection, or use --no flag with cim/cex to prevent auto-confirmation.

Get Config Values
# Get full config object
ssh user@remote.server "cd /path/to/drupal && drush config:get config.name"

# Get as YAML
ssh user@remote.server "cd /path/to/drupal && drush config:get config.name --format=yaml"

# Extract specific values
ssh user@remote.server "cd /path/to/drupal && drush config:get config.name 2>&1 | grep 'setting_name'"

Compare Local vs Remote
# View diffs without importing (SAFE with --no)
ssh user@remote.server "cd /path/to/drupal && drush cim --no --diff"

# Get remote and compare manually
ssh user@remote.server "cd /path/to/drupal && drush config:get config.name --format=yaml" > /tmp/remote.yml
diff -u config/default/config.name.yml /tmp/remote.yml


CRITICAL: Always use --no flag with remote drush! Without it, commands may auto-confirm.

Apply Changes

Preferred: Edit config files directly, then commit:

# Use Edit tool on config/default/config.name.yml
git diff config/default/config.name.yml
git add config/default/config.name.yml
git commit -m "Update config from {env}"

Syncing Config from Upstream Environments
Quick Methods

Single config object:

ssh user@remote.server "cd /path/to/drupal && drush config:get config.name --format=yaml" > config/default/config.name.yml
git add config/default/config.name.yml && git commit -m "Update from {env}"
ddev drush config:import --partial


Full config sync via rsync/scp:

ssh user@remote.server "cd /path/to/drupal && drush cex"
rsync -avz user@remote.server:/path/to/drupal/config/default/ /tmp/remote/
diff -r config/default /tmp/remote  # Review
cp /tmp/remote/*.yml config/default/
git add config/default/ && git commit -m "Sync from {env}"
ddev drush cim


Via database pull (DDEV):

ddev pull --environment={env}  # Warning: Overwrites local DB!
ddev drush cex
git diff config/ && git add config/ && git commit -m "Config from {env}"


See examples.md for detailed workflows.

Best practices: Review diffs, commit separately, test locally, document source, avoid syncing environment-specific config.

Deep Dive References

For comprehensive technical documentation, see:

config-split-deep-dive.md - Complete technical reference on Config Split 2.0, patch files, export/import process, and dependency handling
examples.md - Practical examples and workflows
Config Status Check

Check what config would be imported (read-only):

# Local environment
ddev drush config:status

# Remote environment
ssh user@remote.server "cd /path/to/drupal && drush config:status"

Best Practices
Always inspect before importing - Use config:get and --no --diff flags
Manual edits preferred - Edit config files directly for precision
One config type per commit - Separate concerns for clean history
Clear commit messages - Reference source environment
Clean up temp files - Remove temporary YAML files
Verify before committing - Always review git diff output
Test locally first - Import and test before deploying
Use config splits - Keep environment-specific config separate
Troubleshooting
Config files deleted from working directory

If files are marked as deleted in git status:

git checkout HEAD -- config/default/*.yml


This can happen if a drush command runs unexpectedly.

Split not activating

Check split status:

ddev drush config-split:status


Manually activate:

ddev drush config-split:activate {split-name}
ddev drush cex  # Export to save activation state

Config deleted from config/default on export

COMMON ISSUE: Config (like search_api.server.main) gets removed from config/default/ when you run drush cex.

Root cause (99% of cases): Config is in complete_list instead of partial_list!

Complete split = Config is REMOVED from config/default/ and moved to split directory entirely Partial split = Config STAYS in config/default/, only differences are patched

Diagnosis:

# Check if config is in complete_list (will be deleted from config/default)
grep -A10 "complete_list:" config/default/config_split.config_split.local.yml

# Check if config is in partial_list (will stay in config/default)
grep -A10 "partial_list:" config/default/config_split.config_split.local.yml


Solution: Move from complete_list to partial_list

# Edit the split definition
# Move: search_api.server.main
# FROM: complete_list
# TO: partial_list

ddev drush cex  # Re-export
# Check that config/default/search_api.server.main.yml exists
# Check that config/local/config_split.patch.search_api.server.main.yml exists


See config-split-deep-dive.md for complete technical explanation.

Config won't import

Common issues:

Dependencies missing: Install required modules first
UUID mismatch: Use --partial flag
Locked config: Some config (like system.site) has immutable values
# Skip specific config during import
ddev drush config:import --skip-config=system.site

Related Commands

Read-only: config:get, config:status Exports: config:export (alias: cex) Imports: config:import (alias: cim) - Use with --no --diff to preview Splits: config-split:status, csex, csim, config-split:activate

Weekly Installs
56
Repository
grasmash/drupal…e-skills
GitHub Stars
61
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass