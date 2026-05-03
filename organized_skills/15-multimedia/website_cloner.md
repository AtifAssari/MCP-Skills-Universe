---
rating: ⭐⭐⭐
title: website-cloner
url: https://skills.sh/horuz-ai/claude-plugins/website-cloner
---

# website-cloner

skills/horuz-ai/claude-plugins/website-cloner
website-cloner
Installation
$ npx skills add https://github.com/horuz-ai/claude-plugins --skill website-cloner
SKILL.md
Website Cloner Skill

Clone any website with pixel-perfect fidelity using an orchestrated multi-agent workflow.

Overview

This skill provides a complete system for cloning websites:

Slash command: /clone-website <url> orchestrates the entire workflow
4 specialized sub-agents: Each handles a specific phase
Output: Single React component using Tailwind CSS + motion
Architecture
┌─────────────────────────────────────────┐
│     ORCHESTRATOR (/clone-website)       │
│     Delegates, doesn't code             │
└─────────────────────────────────────────┘
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
┌─────────┐   ┌─────────┐   ┌─────────┐
│ screen- │   │ extrac- │   │  (can   │
│ shotter │   │  tor    │   │ parallel│
└─────────┘   └─────────┘   └─────────┘
                    │
                    ▼
            ┌─────────────┐
            │   cloner    │◄────────┐
            └─────────────┘         │
                    │               │
                    ▼               │
            ┌─────────────┐         │
            │ qa-reviewer │─────────┘
            └─────────────┘  (loop until done)

Quick Setup
1. Create Sub-Agents

Run /agents in Claude Code and create these 4 agents. For each, select "Generate with Claude" and provide the description.

Agent Name	Description Summary
website-screenshotter	Captures comprehensive screenshots (full-page, sections, components, hover states)
website-extractor	Downloads assets to public/, extracts colors, typography, spacing, animations
website-cloner	Implements React component with Tailwind + motion, auto-detects project type
website-qa-reviewer	Pixel-by-pixel comparison, classifies issues as Critical/Major/Minor

Detailed prompts for each agent: See references/subagents.md

2. Install Slash Command

Copy assets/clone-website.md to your commands folder:

# Project-level (shared via git)
cp assets/clone-website.md .claude/commands/

# Or user-level (personal)
cp assets/clone-website.md ~/.claude/commands/

3. Configure Playwright MCP

Ensure Playwright MCP is configured in ~/.claude.json or .claude/settings.json:

{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-playwright"]
    }
  }
}

Usage
/clone-website https://example.com


The orchestrator will:

Create task folder .tasks/clone-{domain}/
Invoke screenshotter → captures all visual references
Invoke extractor → downloads assets, extracts styles
Invoke cloner → implements React component
Invoke qa-reviewer → finds discrepancies
Loop steps 4-5 until PERFECT or max 5 iterations
Output Structure
your-project/
├── public/
│   ├── images/          # Downloaded images
│   ├── videos/          # Downloaded videos
│   └── icons/           # Downloaded SVGs/icons
├── app/clone/page.tsx   # React component (location varies by framework)
└── .tasks/clone-{domain}/
    ├── context.md       # Extracted styles
    ├── screenshots/     # Visual references
    └── review-notes.md  # QA findings

Tech Stack Decisions
Technology	Reason
Tailwind CSS	Arbitrary values (bg-[#hex]) enable pixel-perfect color matching
motion	Modern, lighter alternative to framer-motion (import from "motion/react")
Single component	Focus on cloning, not architecture; sections divided by comments
Auto-detect framework	Supports Next.js, TanStack Start, Vite, etc.

Detailed rationale: See references/tech-decisions.md

Workflow Details

Phase-by-phase breakdown: See references/workflow.md

Customization
Change output location

Edit the cloner agent's system prompt to specify a different output path.

Add frameworks

Update project detection logic in cloner agent for additional frameworks.

Adjust iteration limit

Modify the slash command's Phase 5 to change max iterations (default: 5).

Troubleshooting
Issue	Solution
Sub-agents not found	Verify names exactly match: website-screenshotter, website-extractor, website-cloner, website-qa-reviewer
Playwright errors	Run npm install -g @anthropic-ai/mcp-playwright
Assets not loading	Check public/ folder structure and image paths in component
Infinite loop	QA reviewer should set status; check review-notes.md for STATUS line
Weekly Installs
256
Repository
horuz-ai/claude-plugins
GitHub Stars
2
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn