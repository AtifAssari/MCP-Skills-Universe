---
title: tool-selection
url: https://skills.sh/nickcrew/claude-ctx-plugin/tool-selection
---

# tool-selection

skills/nickcrew/claude-ctx-plugin/tool-selection
tool-selection
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill tool-selection
SKILL.md
Tool Selection
Overview

Select the optimal MCP tool by evaluating task complexity, accuracy needs, and performance trade-offs.

When to Use
Choosing between Codanna and Morphllm
Routing tasks based on complexity
Explaining tool selection rationale

Avoid when:

The tool is explicitly specified by the user
Quick Reference
Task	Load reference
Tool selection	skills/tool-selection/references/select.md
Workflow
Parse the operation requirements.
Load the tool selection reference.
Apply the scoring and decision matrix.
Report the chosen tool and rationale.
Output
Selected tool and confidence
Rationale and trade-offs
Common Mistakes
Ignoring explicit user tool preferences
Overweighting speed vs accuracy without justification
Weekly Installs
42
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass