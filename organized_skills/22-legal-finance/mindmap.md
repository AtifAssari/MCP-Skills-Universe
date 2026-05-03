---
rating: ⭐⭐⭐
title: mindmap
url: https://skills.sh/yz0812/skills/mindmap
---

# mindmap

skills/yz0812/skills/mindmap
mindmap
Installation
$ npx skills add https://github.com/yz0812/skills --skill mindmap
SKILL.md
Mindmap
Overview

Convert natural language descriptions or structured content into visual mindmaps using the MCP mindmap tool. Generated files are automatically opened in the browser and saved to the project root directory by default.

Workflow

Follow these steps when generating a mindmap:

1. Collect User Input

Gather the content or description from the user. If the input is too vague or lacks clear structure, briefly confirm the scope and hierarchy level before proceeding.

Example questions:

"What main topics should be included?"
"How many levels deep should the structure go?"
2. Structure Content as Markdown

Convert the input into clean Markdown format suitable for mindmap visualization:

Use headings (#, ##, ###) for hierarchy levels
Use lists (-, *, 1.) for sub-items
Keep structure clear and logical

Example:

# Project Architecture

## Frontend
- React Components
- State Management
- Routing

## Backend
- API Layer
- Database
- Authentication

## DevOps
- CI/CD Pipeline
- Monitoring
- Deployment

3. Generate the Mindmap

Call the mcp__mindmap__convert_markdown_to_mindmap tool with the structured Markdown content:

mcp__mindmap__convert_markdown_to_mindmap(markdown_content: <structured_markdown>)


The tool will:

Generate the mindmap HTML file
Automatically open it in the default browser
Save the file to the project root directory
4. Inform User

After generation, confirm:

The file location (project root directory by default)
The filename if relevant
That the mindmap has been opened in the browser
Tips
Hierarchy clarity: Use proper Markdown heading levels to reflect parent-child relationships
Conciseness: Keep node text brief and scannable
Logical grouping: Organize related concepts under common parent nodes
Balance: Avoid too many items at a single level; distribute across hierarchy when possible
Weekly Installs
79
Repository
yz0812/skills
GitHub Stars
7
First Seen
Feb 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass