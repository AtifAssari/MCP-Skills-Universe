---
title: sf-vlocity-build-deploy
url: https://skills.sh/jaganpro/sf-skills/sf-vlocity-build-deploy
---

# sf-vlocity-build-deploy

skills/jaganpro/sf-skills/sf-vlocity-build-deploy
sf-vlocity-build-deploy
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-vlocity-build-deploy
SKILL.md
sf-vlocity-build-deploy: Vlocity Build DataPack Deployment

Use this skill when the user needs Vlocity DataPack deployment orchestration: export/deploy workflow, manifest-driven deploys, failure triage, and CI/CD sequencing for OmniStudio/Industries DataPacks.

When This Skill Owns the Task

Use sf-vlocity-build-deploy when work involves:

vlocity packDeploy, packRetry, packContinue, packExport, packGetDiffs, validateLocalData
DataPack job-file design (projectPath, expansionPath, manifest, queries)
org-to-org DataPack migration and retry loops
troubleshooting DataPack dependency, matching-key, and GlobalKey issues

Delegate elsewhere when the user is:

deploying standard metadata with sf project deploy -> sf-deploy
building OmniScripts, FlexCards, IPs, or Data Mappers -> sf-industry-commoncore-*
designing Product2 EPC bundles -> sf-industry-cme-epc-model
writing Apex/LWC code -> sf-apex, sf-lwc
Critical Operating Rules
Use Vlocity Build (vlocity) commands for DataPacks, not sf project deploy.
Prefer Salesforce CLI auth integration (-sfdx.username <alias>) over username/password files when available.
Always run a pre-deploy quality gate before full deploy:
validateLocalData
optional packGetDiffs
then packDeploy
Use packRetry repeatedly when error counts are dropping; stop when retries no longer improve results.
Keep matching-key strategy and GlobalKey integrity consistent across source and target orgs.
Required Context to Gather First

Ask for or infer:

source org and target org aliases
job file path and DataPack project path
deployment scope (full project, manifest subset, or specific -key)
whether this is export, deploy, retry, continue, or diff-only
namespace model (%vlocity_namespace%, vlocity_cmt, or core)
known constraints (new sandbox bootstrap, trigger behavior, matching key customizations)

Preflight checks:

vlocity help
sf org list
sf org display --target-org <alias> --json
test -f <job-file>.yaml

Recommended Workflow
1. Ensure tool readiness
npm install --global vlocity
vlocity help

2. Validate project data locally
vlocity -sfdx.username <source-alias> -job <job-file>.yaml validateLocalData


Use --fixLocalGlobalKeys only when explicitly requested and after explaining impact.

3. Export from source (when needed)
vlocity -sfdx.username <source-alias> -job <job-file>.yaml packExport
vlocity -sfdx.username <source-alias> -job <job-file>.yaml packRetry

4. Deploy to target
vlocity -sfdx.username <target-alias> -job <job-file>.yaml packDeploy
vlocity -sfdx.username <target-alias> -job <job-file>.yaml packRetry

5. Continue interrupted jobs
vlocity -sfdx.username <target-alias> -job <job-file>.yaml packContinue

6. Verify post-deploy parity
vlocity -sfdx.username <target-alias> -job <job-file>.yaml packGetDiffs


Job-file starter: references/job-file-template.md

High-Signal Failure Patterns
Error / symptom	Likely cause	Default fix direction
No match found for ...	missing dependency in target org	include missing DataPack key and redeploy
Duplicate Results found for ... GlobalKey	duplicate records in target	clean duplicates and re-run deploy
Multiple Imported Records ... same Salesforce Record	source duplicate matching-key records	remove duplicates in source and re-export
No Configuration Found	outdated DataPack settings	run packUpdateSettings or enable autoUpdateSettings
Some records were not processed	settings mismatch / partial dependency state	refresh settings both orgs, then retry
SASS / template compile failures	missing referenced UI template assets	export/deploy referenced template dependencies first

Detailed matrix: references/troubleshooting-matrix.md

CI/CD Guidance

Default pipeline shape:

authenticate orgs (sf org login ...)
validate local DataPack integrity (validateLocalData)
export changed scope (packExport or manifest-driven export)
deploy (packDeploy)
retry loop (packRetry) until stable
compare (packGetDiffs) and publish deployment report

For incremental deploy optimization, use job-file options such as:

gitCheck: true
gitCheckKey: <folder>
manifest for deterministic scope control
Cross-Skill Integration
Need	Delegate to	Reason
metadata deploy outside DataPacks	sf-deploy	Metadata API workflows
OmniStudio component authoring	sf-industry-commoncore-*	build artifacts before deploy
EPC product and offer payload authoring	sf-industry-cme-epc-model	Product2/DataPack model quality
Apex trigger/log error diagnosis	sf-debug, sf-apex	automation-side root-cause fixes
Reference Map
Start here
references/job-file-template.md
references/troubleshooting-matrix.md
examples/business-internet-plus-bundle/TRANSCRIPT.md
examples/business-internet-plus-bundle-deploy/TRANSCRIPT.md
External reference
Vlocity Build GitHub
Completion Format
DataPack goal: <export / deploy / retry / diff / ci-cd>
Source org: <alias or N/A>
Target org: <alias or N/A>
Scope: <job file + manifest/key/full>
Result: <passed / failed / partial>
Key findings: <errors, dependencies, retries, diffs>
Next step: <safe follow-up action>

Weekly Installs
566
Repository
jaganpro/sf-skills
GitHub Stars
404
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass