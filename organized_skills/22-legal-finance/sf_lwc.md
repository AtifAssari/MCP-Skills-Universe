---
rating: ⭐⭐⭐
title: sf-lwc
url: https://skills.sh/jaganpro/sf-skills/sf-lwc
---

# sf-lwc

skills/jaganpro/sf-skills/sf-lwc
sf-lwc
Installation
$ npx skills add https://github.com/jaganpro/sf-skills --skill sf-lwc
SKILL.md
sf-lwc: Lightning Web Components Development

Use this skill when the user needs Lightning Web Components: LWC bundles, wire patterns, Apex/GraphQL integration, SLDS 2 styling, accessibility, performance work, or Jest unit tests.

When This Skill Owns the Task

Use sf-lwc when the work involves:

lwc/**/*.js, .html, .css, .js-meta.xml
component scaffolding and bundle design
wire service, Apex integration, GraphQL integration
SLDS 2, dark mode, and accessibility work
Jest unit tests for LWC

Delegate elsewhere when the user is:

writing Apex controllers or business logic first → sf-apex
building Flow XML rather than an LWC screen component → sf-flow
deploying metadata → sf-deploy
Required Context to Gather First

Ask for or infer:

component purpose and target surface
data source: LDS, Apex, GraphQL, LMS, or external system via Apex
whether the user needs tests
whether the component must run in Flow, App Builder, Experience Cloud, or dashboard contexts
accessibility and styling expectations
Recommended Workflow
1. Choose the right architecture

Use the PICKLES mindset:

prototype
integrate the right data source
compose component boundaries
define interaction model
use platform libraries
optimize execution
enforce security
2. Choose the right data access pattern
Need	Default pattern
single-record UI	LDS / getRecord
simple CRUD form	base record form components
complex server query	Apex @AuraEnabled(cacheable=true)
related graph data	GraphQL wire adapter
cross-DOM communication	Lightning Message Service
3. Start from an asset when useful

Use provided assets for:

basic component bundles
datatables
modal patterns
Flow screen components
GraphQL components
LMS message channels
Jest tests
TypeScript-enabled components
4. Validate for frontend quality

Check:

accessibility
SLDS 2 / dark mode compliance
event contracts
performance / rerender safety
Jest coverage when required
5. Hand off supporting backend or deploy work

Use:

sf-apex for controllers / services
sf-deploy for deployment
sf-testing only for Apex-side test loops, not Jest
High-Signal Rules
prefer platform base components over reinventing controls
use @wire for reactive read-only use cases; imperative calls for explicit actions and DML paths
do not introduce inaccessible custom UI
avoid hardcoded colors; use SLDS 2-compatible styling hooks / variables
avoid rerender loops in renderedCallback()
keep component communication patterns explicit and minimal
Output Format

When finishing, report in this order:

Component(s) created or updated
Data access pattern chosen
Files changed
Accessibility / styling / testing notes
Next implementation or deploy step

Suggested shape:

LWC work: <summary>
Pattern: <wire / apex / graphql / lms / flow-screen>
Files: <paths>
Quality: <a11y, SLDS2, dark mode, Jest>
Next step: <deploy, add controller, or run tests>

Local Development Server

Preview LWC components locally with hot reload — no deployment needed:

# Preview LWC components in isolation
sf lightning dev component --target-org <alias>

# Preview a Lightning Experience app locally
sf lightning dev app --target-org <alias>

# Preview an Experience Cloud site locally
sf lightning dev site --target-org <alias>


In current SF CLI releases, these Local Dev commands are installed just-in-time the first time you run them. They are long-running processes that open a browser with live preview. Changes to .js, .html, and .css files auto-reload instantly. Requires an active org connection for data and Apex callouts.

Cross-Skill Integration
Need	Delegate to	Reason
Apex controller or service	sf-apex	backend logic
embed in Flow screens	sf-flow	declarative orchestration
deploy component bundle	sf-deploy	org rollout
create metadata like message channels	sf-metadata	supporting metadata
Reference Map
Start here
references/component-patterns.md
references/slds-design-guide.md
references/lwc-best-practices.md
references/scoring-and-testing.md
references/jest-testing.md
Accessibility / performance / state
references/accessibility-guide.md
references/performance-guide.md
references/state-management.md
references/template-anti-patterns.md
Integration / advanced features
references/lms-guide.md
references/flow-integration-guide.md
references/advanced-features.md
references/async-notification-patterns.md
references/triangle-pattern.md
assets/
Score Guide
Score	Meaning
150+	production-ready LWC bundle
125–149	strong component with minor polish left
100–124	functional but review recommended
< 100	needs significant improvement
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