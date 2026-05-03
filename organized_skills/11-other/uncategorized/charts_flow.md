---
rating: ⭐⭐⭐⭐⭐
title: charts-flow
url: https://skills.sh/vladm3105/aidoc-flow-framework/charts-flow
---

# charts-flow

skills/vladm3105/aidoc-flow-framework/charts-flow
charts-flow
Installation
$ npx skills add https://github.com/vladm3105/aidoc-flow-framework --skill charts-flow
SKILL.md
charts-flow
Purpose

The charts-flow skill automates creation and management of Mermaid diagrams for technical documentation. It separates diagram source files from main documents to improve rendering performance, provides automatic SVG conversion for human viewing, and maintains traceability between parent documents and diagram files.

Key Benefits:

Performance: Separate diagram files load faster in documentation viewers
Dual Format: Mermaid source for AI assistants, SVG preview for humans
Traceability: Diagrams linked to parent documents with proper ID naming
Migration: Extract existing inline diagrams to separate files
Consistency: Standardized diagram file structure and metadata
When to Use This Skill

Use charts-flow when:

Creating architecture diagrams for PRD, BRD, ADR, SYS, or other technical documents
Migrating existing inline Mermaid diagrams to separate files
Main document becomes slow to render due to complex diagrams
Diagram needs to be reused across multiple documents
Creating flowcharts, component diagrams, deployment diagrams, sequence diagrams, state machines, or class diagrams

Do NOT use charts-flow when:

Creating simple tables or text-based lists (use markdown)
Diagram is < 20 lines and main document renders fast
Creating data visualization charts (use appropriate charting libraries)
Working with non-architecture diagrams (Gantt, pie charts - outside scope)
Skill Inputs
Required Inputs
Input	Description	Example
Parent File Path	Absolute path to main document	{project_root}/docs/PRD/PRD-01_multi_agent_system_architecture.md
Diagram Description	Short name for diagram	3_tier_agent_hierarchy
Diagram Type	Architecture diagram type	flowchart, sequence, class, state, component, deployment
Optional Inputs
Input	Description	Default
Migration Mode	Extract existing diagrams from document	false (create new)
Diagram Title	Human-readable title	Derived from description
Styling Preferences	Color scheme, layout direction	Project defaults
Skill Workflow
Mode 1: Create New Diagram

Step 1: Parse Parent Document

Extract parent document ID from filename (e.g., PRD-01 from PRD-01_multi_agent_system_architecture.md)
Identify parent document type (PRD, BRD, ADR, SYS, etc.)
Determine correct diagrams/ subfolder location

Step 2: Generate Diagram File Path

Format: {parent_folder}/diagrams/{PARENT-ID}-diag_{description}.md
The diagrams/ subfolder is created in the same directory as the parent document
Examples by document type:
BRD: docs/BRD/diagrams/BRD-01-diag_workflow.md
PRD: docs/PRD/diagrams/PRD-01-diag_3_tier_agent_hierarchy.md
ADR: docs/ADR/diagrams/ADR-005-diag_cloud_deployment.md
SYS: docs/SYS/diagrams/SYS-002-diag_data_flow.md
IMPL: docs/IMPL/diagrams/IMPL-010-diag_implementation_phases.md
Create diagrams/ folder if it doesn't exist

Step 3: Create Diagram File

Use diagram file template (see Templates section below)
Include Document Control section linking to parent
Add diagram type metadata
Create Mermaid code block with syntax appropriate for diagram type

Step 4: Generate SVG

Attempt mmdc CLI conversion: mmdc -i diagram.md -o diagram.svg
Fallback: Use Mermaid Live API if CLI unavailable
Validate SVG output (check for errors, size < 1MB)

Step 5: Encode SVG as Base64

Read generated SVG file
Convert to Base64 string
Prepare data URI: data:image/svg+xml;base64,{BASE64_STRING}

Step 6: Update Parent Document

Add reference link to diagram file
Embed Base64 SVG in collapsible <details> block
Place in appropriate section of parent document

Step 7: Validate

Verify diagram file exists and is readable
Check Mermaid syntax validity
Confirm SVG renders correctly
Validate cross-references resolve
Mode 2: Migrate Existing Diagrams

Step 1: Scan Parent Document

Search for ````mermaid` code blocks
Extract each diagram with surrounding context
Preserve diagram content and styling

Step 2: Create Diagram Files

For each extracted diagram, follow Steps 1-4 from Mode 1
Auto-generate description from diagram content or context
Number multiple diagrams: _diagram_1, _diagram_2, etc.

Step 3: Replace in Parent Document

Remove original ````mermaid` blocks
Insert SVG + reference link in same location
Maintain document flow and readability

Step 4: Validate Migration

Confirm all diagrams extracted
Verify no broken references
Check visual fidelity (SVG matches original Mermaid)
Templates
Diagram File Template
# {PARENT-ID}-diag: {Diagram Title}

## Document Control

| Item | Details |
|------|---------|
| **Diagram ID** | {PARENT-ID}-diag |
| **Parent Document** | [{PARENT-ID}: {Parent Title}](../{PARENT-FILE}.md) |
| **Diagram Type** | {flowchart|sequence|class|state|component|deployment} |
| **Status** | Active |
| **Version** | 1.0.0 |
| **Created** | {YYYY-MM-DD} |
| **Last Updated** | {YYYY-MM-DD} |
| **Maintained By** | {Role} |

## Overview

{Brief description of what this diagram represents}

## {Diagram Title}

```mermaid
{Mermaid diagram code}

Diagram Description

{Detailed explanation of diagram elements, flows, and purpose}

Key Elements

{List or table of important nodes, components, actors, states, or flows}

References
Parent Document: {PARENT-ID}: {Parent Title}
Related Diagrams: {Links to related diagram files if applicable}
Related Documents: {Links to related requirements, ADRs, strategy docs}

Diagram Version: 1.0.0 Created: {YYYY-MM-DD} Maintained By: {Role}


### Parent Document Reference Template

```markdown
**Visual Diagram**: [{PARENT-ID}-diag: {Diagram Title}](diagrams/{PARENT-ID}-diag_{description}.md)

<details>
<summary>View Diagram (SVG Preview)</summary>

![{Diagram Title}](data:image/svg+xml;base64,{BASE64_SVG_STRING})

</details>

Supported Diagram Types
Flowchart / Graph
graph TB
    A[Start] --> B{Decision}
    B -->|Yes| C[Action 1]
    B -->|No| D[Action 2]


Use for: Process flows, decision trees, workflows

Sequence Diagram
sequenceDiagram
    Actor->>System: Request
    System->>Database: Query
    Database-->>System: Result
    System-->>Actor: Response


Use for: Agent interactions, API calls, message flows

Class Diagram
classDiagram
    class Agent {
        +state: State
        +execute()
        +validate()
    }
    Agent <|-- StrategyAgent


Use for: Object relationships, system components

State Diagram
stateDiagram-v2
    [*] --> SCANNING
    SCANNING --> ACTIVE
    ACTIVE --> DEFENSE
    DEFENSE --> [*]


Use for: State machines, lifecycle flows

Component Diagram (using flowchart)
graph LR
    subgraph "Level 1"
        SO[System Orchestrator]
    end
    subgraph "Level 2"
        IS[Item Selection]
    end
    SO --> IS


Use for: System architecture, component relationships

Deployment Diagram (using flowchart)
graph TB
    subgraph "Cloud Run"
        A[Agent Container]
    end
    subgraph "Cloud SQL"
        B[(Database)]
    end
    A --> B


Use for: Infrastructure architecture, deployment topology

Tool Usage
Check for Mermaid CLI
which mmdc


If not installed:

npm install -g @mermaid-js/mermaid-cli


Alternative: Use Puppeteer

npm install -g puppeteer

Generate SVG from Mermaid
mmdc -i input.md -o output.svg -b transparent


Parameters:

-i: Input file (Mermaid markdown)
-o: Output file (SVG)
-b: Background color (transparent recommended)
Convert SVG to Base64
base64 -w 0 diagram.svg


macOS:

base64 -i diagram.svg

Quality Gates (Definition of Done)
 File Created: Diagram file exists in correct diagrams/ subfolder
 Naming Convention: File name follows {PARENT-ID}-diag_{description}.md pattern
 Document Control: Metadata section present with parent link back-reference
 Mermaid Syntax: Diagram syntax validates without errors
 SVG Generated: SVG file created successfully (if using file method)
 SVG Embedded: Base64 SVG embedded in parent document
 Reference Added: Link to diagram file added in parent document
 Cross-References: All links resolve correctly (bidirectional)
 Rendering: Diagram displays correctly in GitHub, VS Code, and documentation sites
 Accessibility: Collapsible <details> block used for SVG preview
 File Size: SVG < 1MB, Base64 string < 1.5MB
Skill Constraints
What NOT to Do
Do NOT create diagrams in archived folders without explicit permission
Do NOT modify existing diagram files without checking version history
Do NOT embed large binary images (use SVG only)
Do NOT use Gantt charts, pie charts, or git graphs (outside scope - architecture diagrams only)
Do NOT create diagrams for simple lists or tables (use markdown)
Do NOT skip Document Control metadata
Do NOT use generic filenames like diagram1.md (use descriptive names)
File Organization Rules
Always create diagrams/ subfolder in same directory as parent document
Always use parent document ID as diagram file prefix
Always maintain traceability with cross-references
Always follow template structure for consistency
Error Handling
Error: mmdc command not found

Cause: Mermaid CLI not installed

Resolution:

npm install -g @mermaid-js/mermaid-cli
# OR
# Provide manual instructions to use Mermaid Live (https://mermaid.live)

Error: Invalid Mermaid syntax

Cause: Syntax error in diagram code

Resolution:

Validate syntax at https://mermaid.live
Check for missing quotes, brackets, or keywords
Review Mermaid documentation for diagram type
Error: SVG file too large (> 1MB)

Cause: Diagram too complex

Resolution:

Split into multiple diagrams
Simplify diagram (remove redundant elements)
Use subgraphs to organize complexity
Error: Cannot determine parent document ID

Cause: Filename doesn't follow standard naming (e.g., no ID prefix)

Resolution:

Prompt user to specify parent ID manually
Suggest renaming parent file to follow conventions
Error: diagrams/ folder creation failed

Cause: Permission issues or invalid path

Resolution:

Check file permissions
Verify parent directory exists
Use absolute paths
Example Usage
Example 1: Create New Flowchart Diagram for BRD

User Request:

"Create a flowchart diagram showing the user workflow for BRD-01"

Skill Actions:

Parse parent: {project_root}/docs/BRD/BRD-01_project_requirements.md
Extract ID: BRD-01
Create file: docs/BRD/diagrams/BRD-01-diag_user_workflow.md (in BRD subfolder)
Generate Mermaid flowchart with user journey steps
Convert to SVG using mmdc
Embed Base64 SVG in BRD-01
Add reference link

Result:

Diagram file created in docs/BRD/diagrams/ (document type-specific subfolder)
SVG preview visible in parent document
Cross-references working in both directions
Example 2: Migrate Existing Diagram

User Request:

"Migrate the state machine diagram from strategy_state_machine.md to a separate file"

Skill Actions:

Scan {project_root}/strategy/strategy_state_machine.md
Find ```mermaid block (state diagram)
Extract diagram code
Create {project_root}/strategy/diagrams/SSM-001-diag_state_transitions.md
Generate SVG
Replace original block with SVG + reference
Validate migration

Result:

Original Mermaid moved to separate file
SVG preview embedded in main document
Main document renders faster
Example 3: Create Sequence Diagram for ADR

User Request:

"Create a sequence diagram showing the agent communication flow for ADR-003"

Skill Actions:

Parent: docs/ADR/ADR-003_agent_communication.md
Create: docs/ADR/diagrams/ADR-003-diag_agent_communication_sequence.md (in ADR subfolder)
Generate sequence diagram: System Orchestrator → Selection Service → Strategy Agent → Risk Service
Add swimlanes for timing (A2A Protocol patterns)
Convert to SVG
Embed in ADR-003

Result:

Sequence diagram in docs/ADR/diagrams/ (document type-specific subfolder)
Message flow with <50ms SLA annotations visible
SVG preview in ADR document
Output Format
Generated Artifacts

Diagram File ({PARENT-ID}-diag_{description}.md)

Location: {parent_folder}/diagrams/
Format: Markdown with Mermaid code block
Includes: Document Control, diagram code, description, references

SVG File (optional, if using file-based approach)

Location: Same as diagram file, .svg extension
Format: Scalable Vector Graphics
Used for Base64 encoding

Updated Parent Document

Reference link added in appropriate section
SVG preview embedded in <details> block
Original content preserved
File Organization After Execution

Each document type has its own diagrams subfolder:

docs/
├── BRD/
│   ├── BRD-01_project_requirements.md         ← Updated with SVG + link
│   └── diagrams/
│       ├── BRD-01-diag_user_workflow.md       ← BRD diagrams
│       └── BRD-01-diag_business_rules.md
├── PRD/
│   ├── PRD-01_multi_agent_system.md           ← Updated with SVG + link
│   └── diagrams/
│       ├── PRD-01-diag_3_tier_hierarchy.md    ← PRD diagrams
│       └── PRD-01-diag_cloud_architecture.md
├── ADR/
│   ├── ADR-005_deployment_strategy.md          ← Updated with SVG + link
│   └── diagrams/
│       └── ADR-005-diag_deployment_flow.md     ← ADR diagrams
├── SYS/
│   ├── SYS-002_data_pipeline.md                ← Updated with SVG + link
│   └── diagrams/
│       └── SYS-002-diag_data_flow.md           ← SYS diagrams
└── IMPL/
    ├── IMPL-010_phase_1_plan.md                ← Updated with SVG + link
    └── diagrams/
        └── IMPL-010-diag_implementation.md     ← IMPL diagrams

Integration with Project Workflow
Traceability Chain
Product Strategy ({project_root}/strategy/*.md)
  ↓
Requirements (docs/reqs/*.md)
  ↓
Architecture Decisions (docs/adrs/*.md) ← diagrams support ADRs
  ↓
System Specifications (docs/sys/*.md) ← diagrams show architecture
  ↓
BDD Scenarios (docs/BDD/*.feature)
  ↓
Code Implementation


Diagrams enhance: ADRs, SYS, PRD, BRD documents with visual architecture representations

Relationship to Other Skills
doc-flow: Creates specification documents; charts-flow adds diagrams to those documents
google-adk: Defines agent framework; charts-flow visualizes agent hierarchies
project-mngt: Creates implementation plans; charts-flow shows dependency graphs
References
Internal Documentation
Claude Code Skills README
SDD Framework Guide
External Resources
Mermaid Documentation
Mermaid Live Editor
Mermaid CLI Documentation
Related Templates
BRD Template
PRD Template
ADR Template
SYS Template
IMPL Template

Skill Version: 1.0.0 Created: 2025-01-04 Last Updated: 2025-01-04 Maintained By: Development Team

Weekly Installs
64
Repository
vladm3105/aidoc…ramework
GitHub Stars
14
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass