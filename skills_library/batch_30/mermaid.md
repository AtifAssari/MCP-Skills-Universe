---
title: mermaid
url: https://skills.sh/wh-2099/mermaid-skill/mermaid
---

# mermaid

skills/wh-2099/mermaid-skill/mermaid
mermaid
Installation
$ npx skills add https://github.com/wh-2099/mermaid-skill --skill mermaid
SKILL.md
Mermaid Diagram Generator

Generate high-quality Mermaid diagram code based on user requirements.

Workflow
Understand Requirements: Analyze user description to determine the most suitable diagram type
Read Documentation: Read the corresponding syntax reference for the diagram type
Generate Code: Generate Mermaid code following the specification
Apply Styling: Apply appropriate themes and style configurations
Diagram Type Reference

Select the appropriate diagram type and read the corresponding documentation:

Type	Documentation	Use Cases
Flowchart	flowchart.md	Processes, decisions, steps
Sequence Diagram	sequenceDiagram.md	Interactions, messaging, API calls
Class Diagram	classDiagram.md	Class structure, inheritance, associations
State Diagram	stateDiagram.md	State machines, state transitions
ER Diagram	entityRelationshipDiagram.md	Database design, entity relationships
Gantt Chart	gantt.md	Project planning, timelines
Pie Chart	pie.md	Proportions, distributions
Mindmap	mindmap.md	Hierarchical structures, knowledge graphs
Timeline	timeline.md	Historical events, milestones
Git Graph	gitgraph.md	Branches, merges, versions
Quadrant Chart	quadrantChart.md	Four-quadrant analysis
Requirement Diagram	requirementDiagram.md	Requirements traceability
C4 Diagram	c4.md	System architecture (C4 model)
Sankey Diagram	sankey.md	Flow, conversions
XY Chart	xyChart.md	Line charts, bar charts
Block Diagram	block.md	System components, modules
Packet Diagram	packet.md	Network protocols, data structures
Kanban	kanban.md	Task management, workflows
Architecture Diagram	architecture.md	System architecture
Radar Chart	radar.md	Multi-dimensional comparison
Treemap	treemap.md	Hierarchical data visualization
User Journey	userJourney.md	User experience flows
ZenUML	zenuml.md	Sequence diagrams (code style)
Configuration & Themes
Theming - Custom colors and styles
Directives - Diagram-level configuration
Layouts - Layout direction and spacing
Configuration - Global settings
Math - LaTeX math support
Output Specification

Generated Mermaid code should:

Be wrapped in ```mermaid code blocks
Have correct syntax that renders directly
Have clear structure with proper line breaks and indentation
Use semantic node naming
Include styling when needed to improve visual appearance
Example Output
flowchart TD
    A[Start] --> B{Condition}
    B -->|Yes| C[Execute]
    B -->|No| D[End]
    C --> D


User requirements: $ARGUMENTS

Weekly Installs
34
Repository
wh-2099/mermaid-skill
GitHub Stars
34
First Seen
Feb 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass