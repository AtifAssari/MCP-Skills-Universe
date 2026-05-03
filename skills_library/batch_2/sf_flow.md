---
title: sf-flow
url: https://skills.sh/jaganpro/sf-skills/sf-flow
---

# sf-flow

skills/jaganpro/sf-skills/sf-flow
sf-flow
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-flow
SKILL.md
sf-flow: Salesforce Flow Creation and Validation

Use this skill when the user needs Flow design or Flow XML work: record-triggered, screen, autolaunched, scheduled, or platform-event Flows, including validation, architecture choices, and safe deployment sequencing.

When This Skill Owns the Task

Use sf-flow when the work involves:

.flow-meta.xml files
Flow Builder architecture and XML generation
record-triggered, screen, scheduled, autolaunched, or platform-event flows
Flow-specific bulk safety, fault paths, and subflow orchestration

Delegate elsewhere when the user is:

writing Apex-first automation → sf-apex
creating objects / fields first → sf-metadata
deploying metadata → sf-deploy
seeding post-deploy test data → sf-data
Required Context to Gather First

Ask for or infer:

flow type
trigger object / entry conditions
core business goal
whether this is new, refactor, or repair
target org alias if deployment or validation is needed
whether related objects / fields already exist
Recommended Workflow
1. Choose the right automation tool

Before building, confirm Flow is the right answer rather than:

formula field
validation rule
roll-up summary
Apex
2. Choose the right Flow type
Need	Default flow type
same-record update before save	before-save record-triggered
related-record work / emails / callouts	after-save record-triggered
guided UI	screen flow
reusable background logic	autolaunched / subflow
scheduled processing	scheduled flow
event-driven declarative response	platform-event flow
AI-evaluated routing (sentiment, intent, tone)	autolaunched with AI Decision element
3. Start from a template

Prefer the provided assets:

assets/record-triggered-before-save.xml
assets/record-triggered-after-save.xml
assets/screen-flow-template.xml
assets/autolaunched-flow-template.xml
assets/scheduled-flow-template.xml
assets/platform-event-flow-template.xml
assets/ai-decision-template.xml
assets/subflows/
4. Validate against Flow guardrails

Focus on:

no DML in loops
no Get Records inside loops
proper fault paths
correct trigger conditions
safe subflow composition
AI Decision elements not placed inside loops (credit cost per iteration)
AI Decision prompts include merge field references for data context
5. Hand off deployment and testing

Use:

sf-deploy for deploy / dry-run
sf-data for high-volume test data
High-Signal Rules
Flow architecture
before-save for same-record field updates
after-save for related records, emails, and callouts
do not loop over $Record
use subflows when logic becomes wide or repetitive
Bulk safety
no DML in loops
no Get Records in loops
test with 251+ records when bulk behavior matters
prefer Transform when the job is shaping data, not per-record branching
Error handling
every data-changing path should have fault handling
avoid self-referencing fault connectors
deploy Flows as Draft first when activation risk is non-trivial
Output Format

When finishing, report in this order:

Flow type and goal
Files created or updated
Architecture choices
Bulk/error-handling notes
Deploy/testing next steps

Suggested shape:

Flow: <name>
Type: <flow type>
Files: <paths>
Design: <trigger choice, subflows, key decisions>
Risks: <bulk safety, fault paths, dependencies>
Next step: <dry-run deploy, activate, or test>

Flow Testing (CLI)

Run Flow tests from the command line without VS Code:

# Run all flow tests
sf flow run test --target-org <alias> --json

# Run tests for a specific flow
sf flow run test --class-names MyFlow --target-org <alias> --json

# Get results for an asynchronous run
sf flow get test --test-run-id <id> --target-org <alias> --json


Flow tests execute in the org and can take 1-5 minutes. sf flow run test returns a test run ID for asynchronous runs; use sf flow get test to retrieve results later. Always run with --json and use background execution for longer runs.

Cross-Skill Integration
Need	Delegate to	Reason
create objects / fields first	sf-metadata	schema readiness
deploy / activate flow	sf-deploy	safe deployment sequence
create realistic bulk test data	sf-data	post-deploy verification
create Apex actions / invocables	sf-apex	imperative logic
embed LWC in a screen flow	sf-lwc	custom UI components
expose Flow to Agentforce	sf-ai-agentscript	agent action orchestration
Reference Map
Start here
references/flow-best-practices.md
references/flow-quick-reference.md
references/orchestration.md
references/testing-guide.md
Design / orchestration
references/subflow-library.md
references/governance-checklist.md
references/transform-vs-loop-guide.md
references/orchestration-guide.md
references/orchestration-parent-child.md
references/orchestration-sequential.md
references/orchestration-conditional.md
AI Decision
references/ai-decision-guide.md
Screen / integration / troubleshooting
references/form-building-guide.md
references/integration-patterns.md
references/lwc-integration-guide.md
references/agentforce-flow-integration.md
references/xml-gotchas.md
references/testing-checklist.md
references/wait-patterns.md
assets/
Score Guide
Score	Meaning
88+	production-ready Flow
75–87	good Flow with some review items
60–74	functional but needs stronger guardrails
< 60	unsafe / incomplete for deployment
Weekly Installs
1.2K
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