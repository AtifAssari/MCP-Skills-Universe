---
title: sf-deploy
url: https://skills.sh/jaganpro/sf-skills/sf-deploy
---

# sf-deploy

skills/jaganpro/sf-skills/sf-deploy
sf-deploy
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-deploy
SKILL.md
sf-deploy: Comprehensive Salesforce DevOps Automation

Use this skill when the user needs deployment orchestration: dry-run validation, targeted or manifest-based deploys, CI/CD workflow advice, scratch-org management, failure triage, or safe rollout sequencing for Salesforce metadata.

When This Skill Owns the Task

Use sf-deploy when the work involves:

sf project deploy start, quick, report, or retrieval workflows
release sequencing across objects, permission sets, Apex, and Flows
CI/CD gates, test-level selection, or deployment reports
troubleshooting deployment failures and dependency ordering

Delegate elsewhere when the user is:

authoring Apex or LWC code → sf-apex, sf-lwc
creating metadata definitions → sf-metadata
building Flows → sf-flow
doing org data operations → sf-data
authoring Agent Script logic → sf-ai-agentscript
Critical Operating Rules
Use sf CLI v2 only.
On non-source-tracking orgs, deploy/retrieve commands require an explicit scope such as --source-dir, --metadata, or --manifest.
Prefer --dry-run first before real deploys.
For Flows, deploy safely and activate only after validation.
Keep test-data creation guidance delegated to sf-data after metadata is validated or deployed.
Default deployment order
Phase	Metadata
1	Custom objects / fields
2	Permission sets
3	Apex
4	Flows as Draft
5	Flow activation / post-verify

This ordering prevents many dependency and FLS failures.

Required Context to Gather First

Ask for or infer:

target org alias and environment type
deployment scope: source-dir, metadata list, or manifest
whether this is validate-only, deploy, quick deploy, retrieve, or CI/CD guidance
required test level and rollback expectations
whether special metadata types are involved (Flow, permission sets, agents, packages)

Preflight checks:

sf --version
sf org list
sf org display --target-org <alias> --json
test -f sfdx-project.json

Recommended Workflow
1. Preflight

Confirm auth, repo shape, package directories, and target scope.

2. Validate first
sf project deploy start --dry-run --source-dir force-app --target-org <alias> --wait 30 --json


Use manifest- or metadata-scoped validation when the change set is targeted.

3. If validation succeeds, offer the next safe workflow

After a successful validation, guide the user to the correct next action:

deploy now
assign permission sets
create test data via sf-data
run tests / smoke checks
orchestrate multiple post-deploy steps in order
4. Deploy the smallest correct scope
# source-dir deploy
sf project deploy start --source-dir force-app --target-org <alias> --wait 30 --json

# manifest deploy
sf project deploy start --manifest manifest/package.xml --target-org <alias> --test-level RunLocalTests --wait 30 --json

# manifest deploy with Spring '26 relevant-test selection
sf project deploy start --manifest manifest/package.xml --target-org <alias> --test-level RunRelevantTests --wait 30 --json

# quick deploy after successful validation
sf project deploy quick --job-id <validation-job-id> --target-org <alias> --json

5. Verify
sf project deploy report --job-id <job-id> --target-org <alias> --json


Then verify tests, Flow state, permission assignments, and smoke-test behavior.

6. Report clearly

Summarize what deployed, what failed, what was skipped, and what the next safe action is.

Output template: references/deployment-report-template.md

High-Signal Failure Patterns
Error / symptom	Likely cause	Default fix direction
FIELD_CUSTOM_VALIDATION_EXCEPTION	validation rule or bad test data	adjust data or rule timing
INVALID_CROSS_REFERENCE_KEY	missing dependency	include referenced metadata first
CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY	trigger / Flow / validation side effect	inspect automation stack and failing logic
tests fail during deploy	broken code or fragile tests	run targeted tests, fix root cause, revalidate
field/object not found in permset	wrong order	deploy objects/fields before permission sets
Flow invalid / version conflict	dependency or activation problem	deploy as Draft, verify, then activate

Full workflows: references/orchestration.md, references/trigger-deployment-safety.md

CI/CD Guidance

Default pipeline shape:

authenticate
validate repo / org state
static analysis
dry-run deploy
tests + coverage gates
deploy
verify + notify
When org policy and release risk allow it, consider --test-level RunRelevantTests for Apex-heavy deployments.
Pair this with modern Apex test annotations such as @IsTest(testFor=...) and @IsTest(isCritical=true) as documented in sf-apex.

Static analysis now uses Code Analyzer v5 (sf code-analyzer), not retired sf scanner.

Deep reference: references/deployment-workflows.md

Agentforce Deployment Note

Use this skill to orchestrate deployment/publish sequencing around agents, but use the agent-specific skills for authoring decisions:

sf-ai-agentscript for .agent authoring and validation
sf-ai-agentforce for Agent Builder / Prompt Builder / metadata config

For full agent DevOps details, including Agent: pseudo metadata, publish/activate, and sync-between-orgs, see:

references/agent-deployment-guide.md
Cross-Skill Integration
Need	Delegate to	Reason
custom object / field creation	sf-metadata	define metadata before deploy
Apex compile / review / fixes	sf-apex	code authoring and repair
Flow creation / repair	sf-flow	Flow authoring and activation guidance
test data or seed records	sf-data	describe-first data setup and cleanup
Agent Script build/publish readiness	sf-ai-agentscript	agent-specific correctness
Reference Map
Start here
references/orchestration.md
references/deployment-workflows.md
references/deployment-report-template.md
Specialized deployment safety
references/trigger-deployment-safety.md
references/agent-deployment-guide.md
references/deploy.sh
Score Guide
Score	Meaning
90+	strong deployment plan and execution guidance
75–89	good deploy guidance with minor review items
60–74	partial coverage of deployment risk
< 60	insufficient confidence; tighten plan before rollout
Completion Format
Deployment goal: <validate / deploy / retrieve / pipeline>
Target org: <alias>
Scope: <source-dir / metadata / manifest>
Result: <passed / failed / partial>
Key findings: <errors, ordering, tests, skipped items>
Next step: <safe follow-up action>

Weekly Installs
1.1K
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