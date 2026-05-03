---
rating: ⭐⭐
title: figma-reader
url: https://skills.sh/delexw/claude-code-misc/figma-reader
---

# figma-reader

skills/delexw/claude-code-misc/figma-reader
figma-reader
Installation
$ npx skills add https://github.com/delexw/claude-code-misc --skill figma-reader
SKILL.md
Figma Reader

Read Figma design context via the Figma MCP server.

Inputs

Raw arguments: $ARGUMENTS

Infer from the arguments:

DESIGN_INPUT: Figma link, design prompt copied from Figma, or attached UI design image (optional)
OUT_DIR: output directory, or .implement-assets/figma if not provided

Use OUT_DIR for all output paths below.

Execution
Pre-flight check: Use ToolSearch to detect if Figma MCP tools are available — follow references/rules.md
If MCP is not available, use AskUserQuestion to guide setup or allow skip
Resolve design input:
If DESIGN_INPUT contains a valid Figma link or prompt → use it directly
If DESIGN_INPUT is an attached UI image → show it for context, then use AskUserQuestion to ask the user to select the relevant component in Figma (see references/rules.md Design Input)
If DESIGN_INPUT is empty or not provided → use AskUserQuestion to ask user (see references/rules.md Design Input)
Read design: Use the Figma MCP tools to read the design from the Figma link resolved in step 3
Format the output per references/output-format.md
Save output: Run mkdir -p OUT_DIR via Bash, then save the full formatted output to OUT_DIR/blueprint.md using the Write tool
Weekly Installs
62
Repository
delexw/claude-code-misc
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn