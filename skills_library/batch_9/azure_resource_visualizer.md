---
title: azure-resource-visualizer
url: https://skills.sh/microsoft/azure-skills/azure-resource-visualizer
---

# azure-resource-visualizer

skills/microsoft/azure-skills/azure-resource-visualizer
azure-resource-visualizer
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-resource-visualizer
Summary

Transform Azure resource groups into detailed architecture diagrams showing resource relationships and configurations.

Discovers all resources within a resource group and analyzes their configurations, dependencies, and interconnections
Generates Mermaid diagrams organized by logical layers (Network, Compute, Data, Security, Monitoring) with SKU details and connection labels
Maps relationships including network connections, data flows, identity bindings, and configuration dependencies across resources
Creates comprehensive markdown documentation with resource inventory tables, architecture diagrams, and relationship explanations
SKILL.md
Azure Resource Visualizer - Architecture Diagram Generator

A user may ask for help understanding how individual resources fit together, or to create a diagram showing their relationships. Your mission is to examine Azure resource groups, understand their structure and relationships, and generate comprehensive Mermaid diagrams that clearly illustrate the architecture.

Core Responsibilities
Resource Group Discovery: List available resource groups when not specified
Deep Resource Analysis: Examine all resources, their configurations, and interdependencies
Relationship Mapping: Identify and document all connections between resources
Diagram Generation: Create detailed, accurate Mermaid diagrams
Documentation Creation: Produce clear markdown files with embedded diagrams
Workflow Process
Step 1: Resource Group Selection

If the user hasn't specified a resource group:

Use your tools to query available resource groups. If you do not have a tool for this, use az.
Present a numbered list of resource groups with their locations
Ask the user to select one by number or name
Wait for user response before proceeding

If a resource group is specified, validate it exists and proceed.

Step 2: Resource Discovery & Analysis

For bulk resource discovery across subscriptions, use Azure Resource Graph queries. See Azure Resource Graph Queries for cross-subscription inventory and relationship discovery patterns.

Once you have the resource group:

Query all resources in the resource group using Azure MCP tools or az.

Analyze each resource type and capture:

Resource name and type
SKU/tier information
Location/region
Key configuration properties
Network settings (VNets, subnets, private endpoints)
Identity and access (Managed Identity, RBAC)
Dependencies and connections

Map relationships by identifying:

Network connections: VNet peering, subnet assignments, NSG rules, private endpoints
Data flow: Apps → Databases, Functions → Storage, API Management → Backends
Identity: Managed identities connecting to resources
Configuration: App Settings pointing to Key Vaults, connection strings
Dependencies: Parent-child relationships, required resources

Important: You must only use placeholder names to represent secret values, such as keys, connection strings, Key Vault secrets, etc. Use meaningful placeholder names to represent each secret in the diagram. Never put secret values in the resource diagram.

Step 3: Diagram Construction

Create a detailed Mermaid diagram using the graph TB (top-to-bottom) or graph LR (left-to-right) format.

See example-diagram.md for a complete sample architecture diagram.

Key Diagram Requirements:

Group by layer or purpose: Network, Compute, Data, Security, Monitoring
Include details: SKUs, tiers, important settings in node labels (use <br/> for line breaks)
Label all connections: Describe what flows between resources (data, identity, network)
Use meaningful node IDs: Abbreviations that make sense (APP, FUNC, SQL, KV)
Visual hierarchy: Subgraphs for logical grouping
Connection types:
--> for data flow or dependencies
-.-> for optional/conditional connections
==> for critical/primary paths

Resource Type Examples:

App Service: Include plan tier (B1, S1, P1v2)
Functions: Include runtime (.NET, Python, Node)
Databases: Include tier (Basic, Standard, Premium)
Storage: Include redundancy (LRS, GRS, ZRS)
VNets: Include address space
Subnets: Include address range
Step 4: File Creation

Use template-architecture.md as a template and create a markdown file named [resource-group-name]-architecture.md with:

Header: Resource group name, subscription, region
Summary: Brief overview of the architecture (2-3 paragraphs)
Resource Inventory: Table listing all resources with types and key properties
Architecture Diagram: The complete Mermaid diagram
Relationship Details: Explanation of key connections and data flows
Notes: Any important observations, potential issues, or recommendations
Operating Guidelines
Quality Standards
Accuracy: Verify all resource details before including in diagram
Completeness: Don't omit resources; include everything in the resource group
Clarity: Use clear, descriptive labels and logical grouping
Detail Level: Include configuration details that matter for architecture understanding
Relationships: Show ALL significant connections, not just obvious ones
Tool Usage Patterns

Azure MCP Search:

Use intent="list resource groups" to discover resource groups
Use intent="list resources in group" with group name to get all resources
Use intent="get resource details" for individual resource analysis
Use command parameter when you need specific Azure operations

File Creation:

Always create in workspace root or a docs/ folder if it exists
Use clear, descriptive filenames: [rg-name]-architecture.md
Ensure Mermaid syntax is valid (test syntax mentally before output)

Terminal (when needed):

Use Azure CLI for complex queries not available via MCP
Example: az resource list --resource-group <name> --output json
Example: az network vnet show --resource-group <name> --name <vnet-name>
Constraints & Boundaries

Always Do:

✅ List resource groups if not specified
✅ Wait for user selection before proceeding
✅ Analyze ALL resources in the group
✅ Create detailed, accurate diagrams
✅ Include configuration details in node labels
✅ Group resources logically with subgraphs
✅ Label all connections descriptively
✅ Create a complete markdown file with diagram

Never Do:

❌ Skip resources because they seem unimportant
❌ Make assumptions about resource relationships without verification
❌ Create incomplete or placeholder diagrams
❌ Omit configuration details that affect architecture
❌ Proceed without confirming resource group selection
❌ Generate invalid Mermaid syntax
❌ Modify or delete Azure resources (read-only analysis)
Edge Cases & Error Handling
No resources found: Inform user and verify resource group name
Permission issues: Explain what's missing and suggest checking RBAC
Complex architectures (50+ resources): Consider creating multiple diagrams by layer
Cross-resource-group dependencies: Note external dependencies in diagram notes
Resources without clear relationships: Group in "Other Resources" section
Output Format Specifications
Mermaid Diagram Syntax
Use graph TB (top-to-bottom) for vertical layouts
Use graph LR (left-to-right) for horizontal layouts (better for wide architectures)
Subgraph syntax: subgraph "Descriptive Name"
Node syntax: ID["Display Name<br/>Details"]
Connection syntax: SOURCE -->|"Label"| TARGET
Markdown Structure
Use H1 for main title
Use H2 for major sections
Use H3 for subsections
Use tables for resource inventories
Use bullet lists for notes and recommendations
Use code blocks with mermaid language tag for diagrams
Success Criteria

A successful analysis includes:

✅ Valid resource group identified
✅ All resources discovered and analyzed
✅ All significant relationships mapped
✅ Detailed Mermaid diagram with proper grouping
✅ Complete markdown file created
✅ Clear, actionable documentation
✅ Valid Mermaid syntax that renders correctly
✅ Professional, architect-level output

Your goal is to provide clarity and insight into Azure architectures, making complex resource relationships easy to understand through excellent visualization.

Weekly Installs
275.7K
Repository
microsoft/azure-skills
GitHub Stars
796
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail