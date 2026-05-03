---
rating: ⭐⭐⭐
title: cmux-markdown
url: https://skills.sh/manaflow-ai/cmux/cmux-markdown
---

# cmux-markdown

skills/manaflow-ai/cmux/cmux-markdown
cmux-markdown
Installation
$ npx skills add https://github.com/manaflow-ai/cmux --skill cmux-markdown
SKILL.md
Markdown Viewer with cmux

Use this skill to display markdown files in a dedicated panel with rich formatting and live file watching.

Core Workflow
Write your plan or notes to a .md file.
Open it in a markdown panel.
The panel auto-updates when the file changes on disk.
# Open a markdown file as a split panel next to the current terminal
cmux markdown open plan.md

# Absolute path
cmux markdown open /path/to/PLAN.md

# Target a specific workspace
cmux markdown open design.md --workspace workspace:2

When to Use
Displaying an agent plan or task list alongside the terminal
Showing documentation, changelogs, or READMEs while working
Reviewing notes that update in real-time (e.g., a plan file being written by another process)
Live File Watching

The panel automatically re-renders when the file changes on disk. This works with:

Direct writes (echo "..." >> plan.md)
Editor saves (vim, nano, VS Code)
Atomic file replacement (write to temp, rename over original)
Agent-generated plan files that are updated progressively

If the file is deleted, the panel shows a "file unavailable" state. During atomic replace, the panel attempts automatic reconnection within its short retry window. If the file returns later, close and reopen the panel.

Agent Integration
Opening a plan file

Write your plan to a file, then open it:

cat > plan.md << 'EOF'
# Task Plan

## Steps
1. Analyze the codebase
2. Implement the feature
3. Write tests
4. Verify the build
EOF

cmux markdown open plan.md

Updating a plan in real-time

The panel live-reloads, so simply overwrite the file as work progresses:

# The markdown panel updates automatically when the file changes
echo "## Step 1: Complete" >> plan.md

Recommended AGENTS.md instruction

Add this to your project's AGENTS.md to instruct coding agents to use the markdown viewer:

## Plan Display

When creating a plan or task list, write it to a `.md` file and open it in cmux:

    cmux markdown open plan.md

The panel renders markdown with rich formatting and auto-updates when the file changes.

Routing
# Open in the caller's workspace (default -- uses CMUX_WORKSPACE_ID)
cmux markdown open plan.md

# Open in a specific workspace
cmux markdown open plan.md --workspace workspace:2

# Open splitting from a specific surface
cmux markdown open plan.md --surface surface:5

# Open in a specific window
cmux markdown open plan.md --window window:1

Deep-Dive References
Reference	When to Use
references/commands.md	Full command syntax and options
references/live-reload.md	File watching behavior, atomic writes, edge cases
Rendering Support

The markdown panel renders:

Headings (h1-h6) with dividers on h1/h2
Fenced code blocks with monospaced font
Inline code with highlighted background
Tables with alternating row colors
Ordered and unordered lists (nested)
Blockquotes with left border
Bold, italic, strikethrough
Links (clickable)
Horizontal rules
Images (inline)

Supports both light and dark mode.

Weekly Installs
671
Repository
manaflow-ai/cmux
GitHub Stars
16.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass