---
rating: ⭐⭐
title: xcodegen-cli
url: https://skills.sh/zyuapp/agent-skills/xcodegen-cli
---

# xcodegen-cli

skills/zyuapp/agent-skills/xcodegen-cli
xcodegen-cli
Installation
$ npx skills add https://github.com/zyuapp/agent-skills --skill xcodegen-cli
SKILL.md
XcodeGen CLI
Overview

Use this skill to drive XcodeGen workflows end-to-end: prepare or edit specs, run the right command, inspect resolved configuration, and fix generation issues quickly.

Follow This Workflow
Identify command context.
Run xcodegen ... if CLI is installed.
Run swift run xcodegen ... when working inside the XcodeGen source repository.
Resolve the spec path.
Default to project.yml in current directory.
Use --spec for custom paths or comma-separated multiple specs.
Use --project-root when include/source paths should resolve from another directory.
Inspect before changing behavior.
Run xcodegen dump --type summary for a quick structural view.
Run xcodegen dump --type yaml --file /tmp/resolved.yml to inspect merged/expanded output.
Generate or cache.
Run xcodegen generate for normal generation.
Run xcodegen generate --use-cache in repetitive local or CI workflows.
Run xcodegen cache when cache artifacts are needed without generation.
Troubleshoot with direct feedback.
Treat parser errors as spec syntax/schema issues.
Treat validation errors as semantic project-model issues.
Treat missing file errors as path, include, or working-directory issues.
Command Guidance
Use generate to produce .xcodeproj from spec files.
Use generate --only-plists when only plist output is needed.
Use dump to inspect effective configuration in yaml, json, parsed-yaml, parsed-json, summary, or swift-dump form.
Use cache to precompute/write cache files.
Add --quiet only when caller asks for reduced output.
Add --no-env to debug ${ENV_VAR} expansion issues.
Spec Editing Guidance
Keep root shape explicit: name, targets, and optional include, options, settings, schemes, packages.
Use include to split large specs and share reusable fragments.
Use :REPLACE suffix in keys when replacement is required instead of merge behavior.
Set options.minimumXcodeGenVersion when relying on newer behavior.
Prefer incremental edits and validate after each edit with dump or generate.
Validation Loop
Update spec.
Run xcodegen dump --type summary.
Run xcodegen generate --use-cache.
If generation fails, inspect resolved YAML using dump --type yaml and fix one issue at a time.
Quick Template
name: MyApp
options:
  bundleIdPrefix: com.example
targets:
  MyApp:
    type: application
    platform: iOS
    deploymentTarget: "16.0"
    sources: [MyApp]

Resources

Read references/api_reference.md for complete command flags, troubleshooting mappings, and links to the canonical docs in this repository.

Weekly Installs
16
Repository
zyuapp/agent-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass