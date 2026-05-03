---
title: ant-design-knowledge-base
url: https://skills.sh/lyq-lin/ycode.cli/ant-design-knowledge-base
---

# ant-design-knowledge-base

skills/lyq-lin/ycode.cli/ant-design-knowledge-base
ant-design-knowledge-base
Installation
$ npx skills add https://github.com/lyq-lin/ycode.cli --skill ant-design-knowledge-base
SKILL.md
Ant Design Knowledge Base
Overview

This skill provides access to local Ant Design documentation and semantic descriptions sourced from the official Ant Design website. The knowledge base includes:

Component Documentation: Links to all Ant Design component documentation pages
Design Resources: Links to design specifications, values, patterns, and guidelines
Semantic Descriptions: Detailed semantic descriptions of each component's CSS class structure (root, icon, title, etc.)
Knowledge Base Files

The following files are available in the knowledge-base/ directory:

llms.txt: Contains documentation links and component overview
llms-full.txt: Contains detailed semantic descriptions of all Ant Design components
How to Use This Knowledge Base
Finding Information

When asked about Ant Design components, documentation, or semantics:

Search for component names: Use Grep to find relevant lines in the knowledge base files:

Grep("Button", "knowledge-base/llms.txt")
Grep("button", "knowledge-base/llms-full.txt")


Read specific sections: Use Read to view the full content or specific lines:

Read("knowledge-base/llms-full.txt", offset=40, limit=50)  # Example for button component


Browse all components: Use Glob to list available files:

Glob("knowledge-base/*.txt")

File Structure Details
llms.txt contains:
Introduction to Ant Design
Semantic descriptions link
Documentation links (Resources, Visualization, Design Values, etc.)
Component links (Affix through Watermark)
llms-full.txt contains:
Semantic descriptions for 64 Ant Design components
For each component: root element and sub-element descriptions with CSS styling purposes
Common Queries
Component Questions

When asked about a specific component (e.g., "Button", "Table", "Form"):

Search for the component in both files:
Grep("button", "knowledge-base/llms.txt", -i)
Grep("### button", "knowledge-base/llms-full.txt", -i)

Read the semantic description section for that component
Provide the component's purpose, semantic elements, and documentation link
Documentation Questions

When asked about design principles, values, or guidelines:

Search for relevant terms in llms.txt:
Grep("Design Values", "knowledge-base/llms.txt")
Grep("Visualization", "knowledge-base/llms.txt")

Provide the documentation links and summaries
Semantic Description Questions

When asked about component structure or CSS classes:

Find the component in llms-full.txt:
Grep("### button", "knowledge-base/llms-full.txt", -A 20)

Extract and explain the semantic elements (root, icon, title, etc.)
Describe the styling purposes of each element
Examples
Example 1: Button Component Query

User: "What are the semantic elements of the Ant Design Button component?"

Approach:

Search for button in semantic descriptions:
Grep("### button", "knowledge-base/llms-full.txt", -A 10)

Read the button section:
Read("knowledge-base/llms-full.txt", offset=42, limit=8)

Present the root, content, and icon elements with their styling purposes.
Example 2: Component Documentation Query

User: "Where can I find documentation for Ant Design Table component?"

Approach:

Search for Table in component links:
Grep("Table", "knowledge-base/llms.txt")

Provide the documentation URL and related resources.
Example 3: Design Principles Query

User: "What are the Ant Design design values?"

Approach:

Search for Design Values link:
Grep("Design Values", "knowledge-base/llms.txt")

Provide the link and summary from the knowledge base.
Notes
The knowledge base is in Chinese for semantic descriptions, but component names are in English.
Some documentation links may require internet access to view full content.
The semantic descriptions are focused on CSS class structure and styling purposes.
Skill Activation

This skill will automatically activate when questions include terms like:

"Ant Design"
"antd"
"React UI components"
"component semantics"
"design system"
Specific component names (Button, Table, Form, etc.)

When activated, Claude has permission to use Read, Grep, and Glob tools to access the knowledge base files in the knowledge-base/ directory.

Weekly Installs
13
Repository
lyq-lin/ycode.cli
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass