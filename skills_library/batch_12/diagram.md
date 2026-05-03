---
title: diagram
url: https://skills.sh/johnlindquist/claude/diagram
---

# diagram

skills/johnlindquist/claude/diagram
diagram
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill diagram
SKILL.md
Diagram Driven Development (DDD) Skill

Maintain the ai/diagrams directory as the single source of truth for system understanding. All diagrams follow DDD principles, connecting Front-Stage (user experience) to Back-Stage (technical implementation) with clear impact annotations.

Capabilities
Create Diagrams - Generate new diagrams for features, architectures, journeys, tests, and refactorings
Update Diagrams - Synchronize existing diagrams with code changes
Audit Diagrams - Identify outdated, missing, or low-quality diagrams
Organize Diagrams - Maintain consistent structure and naming conventions
Index Management - Keep README.md index up-to-date with all diagrams
Quality Validation - Ensure all diagrams follow DDD principles
Quick Reference

For detailed instructions on each operation, see:

CREATE.md - Creating new diagrams
UPDATE.md - Updating existing diagrams
AUDIT.md - Auditing diagram quality and coverage
ORGANIZE.md - Directory structure and naming
DDD_PRINCIPLES.md - Diagram Driven Development methodology
MERMAID_GUIDE.md - Mermaid syntax patterns
Directory Structure
ai/diagrams/
├── README.md                    # Index of all diagrams
├── features/                    # Feature-specific diagrams
├── architecture/                # System architecture diagrams
├── journeys/                    # User journey diagrams
├── tests/                       # Test coverage diagrams
└── refactoring/                 # Before/After improvement diagrams

Common Workflows
Initial Setup Workflow
User starts new project or adds DDD to existing project
Create ai/diagrams/ directory structure
Generate initial system architecture diagram
Create README.md index
Document key user journeys
New Feature Workflow
User requests new feature
Create feature diagram showing user value
Connect Front-Stage (UX) to Back-Stage (implementation)
Document related files and components
Update README.md index
Code Change Workflow
Code is modified (new features, refactoring, etc.)
Identify affected diagrams
Update diagrams to reflect changes
Update "Last Updated" dates
Add change history entries
Audit Workflow
User requests diagram audit
Scan all diagrams in ai/diagrams/
Check for outdated diagrams (compare dates with git)
Identify missing diagrams (features without diagrams)
Validate DDD quality (Front-Stage/Back-Stage, impact annotations)
Report findings and recommendations
Refactoring Documentation Workflow
User plans code refactoring
Create "Before" diagram showing current state
Create "After" diagram showing improved state (highlight changes in #90EE90)
Add impact annotations explaining user benefits
Store in refactoring/ directory
Critical Instructions

REQUIRED: Before performing ANY diagram operations, you MUST load the relevant reference file(s) using the Read tool. These references contain essential DDD principles, quality standards, and operational procedures that are NOT included in this overview.

When the user asks to work with diagrams:

Identify the operation they want to perform (create, update, audit, organize)
MANDATORY: Load the relevant reference file(s) using the Read tool BEFORE executing any operations:
Creating diagrams → Read references/CREATE.md AND references/DDD_PRINCIPLES.md FIRST
Updating diagrams → Read references/UPDATE.md AND references/DDD_PRINCIPLES.md FIRST
Auditing diagrams → Read references/AUDIT.md FIRST
Organizing/restructuring → Read references/ORGANIZE.md FIRST
Understanding DDD → Read references/DDD_PRINCIPLES.md FIRST
Mermaid syntax help → Read references/MERMAID_GUIDE.md FIRST
Execute diagram operations following the exact patterns and quality standards from the loaded references
Validate quality using DDD principles checklist
Update index in README.md to reflect changes
Confirm actions and show diagram preview when possible

DO NOT attempt to create or modify diagrams without first loading and reading the relevant reference documentation, especially DDD_PRINCIPLES.md.

DDD Core Principles (Brief)

Every diagram MUST include:

✅ Front-Stage (user experience) AND Back-Stage (implementation)
✅ Impact Annotations explaining user value of technical components
✅ User Actions as entry/exit points
✅ Error Paths and recovery options
✅ Related Files documentation
❌ NO custom fill colors (except #90EE90 for Before/After changes)
❌ NO purely technical diagrams without user context
Naming Conventions
File Names
Descriptive lowercase with hyphens
Include diagram type prefix
Format: {type}-{descriptive-name}.md

Examples:

feature-user-checkout-flow.md
sequence-authentication-journey.md
arch-system-overview.md
flow-payment-processing.md
Type Prefixes
feature- - Feature-specific diagrams
sequence- - Sequence/journey diagrams
arch- - Architecture diagrams
flow- - Flow/process diagrams
test- - Test coverage diagrams
Diagram File Structure
# [Diagram Title]

**Type:** [Feature Diagram | Sequence Diagram | Architecture Diagram | etc.]
**Last Updated:** [YYYY-MM-DD]
**Related Files:**
- `path/to/implementation.ts`
- `path/to/component.tsx`

## Purpose

[1-2 sentence description of what user value this diagram illustrates]

## Diagram

\`\`\`mermaid
[Mermaid diagram code following DDD principles]
\`\`\`

## Key Insights

- [User impact point 1]
- [User impact point 2]
- [Technical enabler point 1]

## Change History

- **YYYY-MM-DD:** [Description of change]

Quality Checklist

Before storing any diagram, verify:

 Shows both Front-Stage (user experience) AND Back-Stage (implementation)
 Impact annotations explain user value
 User actions are clearly visible
 Error paths shown
 NO custom fill colors (except #90EE90 for changes)
 Related code files documented
 Last updated date is current
 Key insights explain user impact
 Mermaid syntax is valid
Best Practices
Keep diagrams synchronized - Outdated diagrams are worse than no diagrams
Follow DDD principles - Every diagram connects user value to implementation
Use subdirectories - Organize by type to prevent chaos
Maintain the index - README.md is the entry point
Document changes - Update change history when modifying
Validate quality - Run through DDD checklist before saving
Reference code files - Link diagrams to actual implementation
Show error paths - Don't just show happy paths
Use consistent naming - Predictable names enable navigation
Update after code changes - Diagrams must reflect current state
Integration with Other Skills
review - Reference diagrams during code reviews to explain impact
github - Link diagrams in issue descriptions for context
chrome-devtools - Use diagrams to plan testing flows
Examples
Create feature diagram
User: "Create a diagram for the new notification system"
Agent:
1. Reads references/CREATE.md and references/DDD_PRINCIPLES.md
2. Analyzes notification feature code
3. Creates feature-notification-system.md in features/
4. Includes user journey and technical implementation
5. Adds impact annotations
6. Updates README.md index

Update after refactoring
User: "We just refactored the auth flow, update the diagram"
Agent:
1. Reads references/UPDATE.md
2. Finds sequence-authentication-journey.md
3. Compares with new code
4. Updates diagram with changes
5. Updates "Last Updated" date
6. Adds change history entry

Audit all diagrams
User: "Audit our diagrams"
Agent:
1. Reads references/AUDIT.md and references/DDD_PRINCIPLES.md
2. Scans ai/diagrams/ directory
3. Checks each diagram against DDD checklist
4. Compares diagram dates with git history
5. Identifies missing diagrams
6. Reports findings with recommendations

Critical Rules
Diagrams MUST stay synchronized with code - Check git history vs diagram dates
Every diagram MUST follow DDD principles - No purely technical diagrams
Organization is critical - Use subdirectories consistently
Index MUST be maintained - README.md reflects all diagrams
File naming MUST be consistent - Follow type-name pattern
Quality over quantity - Better to have 5 great diagrams than 20 poor ones
User value is paramount - Every technical detail must connect to user impact
Always load references first - DDD principles are not negotiable
Workflow Integration

This skill integrates with development workflow:

Before Code Changes - Review existing diagrams to understand system
During Planning - Create proposal diagrams showing planned changes
During Implementation - Reference diagrams to maintain alignment
After Implementation - Update diagrams to reflect changes
During Review - Use diagrams to explain impact and context
During Onboarding - Diagrams serve as documentation for new team members
Weekly Installs
23
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass