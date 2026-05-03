---
rating: ⭐⭐⭐
title: siebel-development
url: https://skills.sh/ujawal7/siebel_crm/siebel-development
---

# siebel-development

skills/ujawal7/siebel_crm/siebel-development
siebel-development
Installation
$ npx skills add https://github.com/ujawal7/siebel_crm --skill siebel-development
SKILL.md
Siebel Development
Development Workflow

For any Siebel requirement, follow this approach. To start, use the New Requirement Workflow.

Understand - Clarify the business requirement and identify affected objects
Design - Choose the right approach (Configuration vs Scripting vs Workflow)
Implement - Build using appropriate Siebel tools
Test - Validate in Siebel client
Document - Create implementation notes
Coding Standards

🚨 MANDATORY: Always use Oracle Courseware Style. See Coding Standards.

Decision Guide
Requirement Type	Primary Approach	Reference
Data automation on save/create	Runtime Event + Workflow	workflows.md
Field calculations/validations	BC Script or Calculated Field	scripting.md
External API calls	EAI HTTP Transport + BS	integration.md
UI behavior changes	Open UI PM/PR	open-ui.md
Scheduled/batch processing	Workflow Policy	workflows.md
Multi-step business process	Service Flow Workflow	workflows.md
🧭 Decision Principles

When answering, the agent should:

Prefer configuration over scripting
Prefer server-side logic over browser script
Avoid performance-heavy patterns by default
Clearly state trade-offs when multiple solutions exist
Highlight risks in production scenarios
🎓 Answer Style
Explain WHY before HOW
Use enterprise terminology
Assume production scale
Mention performance and maintenance impact
Avoid tutorial-style explanations unless asked
Quick Patterns
Trigger Workflow on Record Save
1. Create Workflow (Business Object = target BO)
2. Create Runtime Event: Object=BusComp, Event=WriteRecord
3. Create Action Set: Service=Workflow Process Manager, Method=RunProcess

Call REST API from Siebel
1. Create Business Service with eScript
2. Use EAI HTTP Transport: SendReceive method
3. Set: HTTPRequestURLTemplate, HTTPRequestMethod, HTTPContentType

Open UI: Conditional Display by User Profile
1. Get SessionAccessService, call GetProfileAttr
2. Check resultSet.GetProperty("Value")
3. Show/hide UI based on result


→ Full patterns: Open UI Patterns

Reference Files
Domain	Reference	When to Read
Open UI Patterns	open-ui-patterns.md	PM-PR code, Google Maps, Charts, Color-coding
Business Services	business-services.md	SessionAccessService, EAI, Helper methods
Coding Standards	coding-standards.md	Oracle courseware style rules
Workflows	workflows.md	Creating workflow processes
Integration	integration.md	REST/SOAP calls, EAI
Scripting	scripting.md	eScript, Business Services
Configuration	configuration.md	BC, Applet, Links, Picklists
Runtime Events	runtime-events.md	Triggers and action sets
Open UI Theory	open-ui.md	PM, PR, Manifest concepts
Troubleshooting	troubleshooting.md	Debugging issues
Key Siebel Objects Hierarchy
Application
└── Business Object (BO)
    └── Business Component (BC) ──► Table
        ├── Fields ──► Columns
        ├── Links ──► Parent-Child relationships
        └── Applet ──► UI display

Skill-Building Framework (Mentorship Mode)

For complex requirements, create a skill_building.md using this 8-section framework:

Requirement Breakdown - Rewrite in simple technical terms
Impact Analysis - Identify ALL impacted objects
Implementation Strategy - Step-by-step in correct sequence
Skill Upgrade - Concepts this strengthens
Edge Cases & Performance - Possible issues
Testing Strategy - Unit and negative tests
Deployment Checklist - Pre/post checks
Interview Angle - How to explain in interview
Repository Organization
Folder	Purpose
core-concepts/	Theory & fundamentals
references/	Oracle courseware patterns
rules/	Non-negotiable standards
commands/	Agent workflow entry points
templates/	Boilerplate files
Requirement Folder Structure
domain-name/
├── README.md           # Analysis, decision, interview guide
├── implementation.md   # Implementation steps & code
├── testing.md          # Verification steps
└── assets/             # Screenshots, diagrams

Best Practices Summary
Configuration over Scripting: Prefer User Properties, Calculated Fields, Workflows
Naming Convention: Use X_ prefix for custom columns
Open UI: Use Plugin Wrappers for field changes; PR for layout
Testing: Test in all supported locales
Manifest: Double-check registration—silent failures common
Code Style: Follow Oracle Courseware patterns
Weekly Installs
14
Repository
ujawal7/siebel_crm
First Seen
Feb 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn