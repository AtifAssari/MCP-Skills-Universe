---
rating: ⭐⭐
title: agent-capability-discovery
url: https://skills.sh/jorgealves/agent_skills/agent-capability-discovery
---

# agent-capability-discovery

skills/jorgealves/agent_skills/agent-capability-discovery
agent-capability-discovery
Installation
$ npx skills add https://github.com/jorgealves/agent_skills --skill agent-capability-discovery
SKILL.md
Agent Capability Discovery
Purpose and Intent

The agent-capability-discovery skill is the "brain" of a multi-agent system. It allows an agent to self-reflect and understand what tools and expertises are available within its environment by indexing all skill.yaml files.

When to Use
System Initialization: Run this when an agent starts up to populate its internal tool list.
Routing Decisions: Use this when a master agent receives a complex user request and needs to identify which specialized skill (e.g., hipaa-compliance-guard vs. pii-sanitizer) is best suited for the job.
Documentation Generation: Automatically keep a "Global Skills Map" up to date for human developers.
When NOT to Use
Skill Execution: This skill only discovers what is possible; it does not execute the other skills.
External Tooling: It only indexes skills defined in the local repository structure.
Input and Output Examples
Input
base_directory: "."
output_format: "markdown"

Output

A markdown table or JSON object listing all discovered skills, their descriptions, and their primary capabilities.

Error Conditions and Edge Cases
Broken YAML: If a skill.yaml is malformed, the discovery tool will skip that directory and report a warning.
Circular Dependencies: This tool does not handle execution dependencies, only discovery.
Security and Data-Handling Considerations
Metadata Only: The tool only reads the definition files; it never touches actual source code or data unless instructed by the indexed skills themselves.
Local Scope: Discovery is confined to the provided root directory to prevent directory traversal attacks.
Weekly Installs
99
Repository
jorgealves/agent_skills
GitHub Stars
1
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass