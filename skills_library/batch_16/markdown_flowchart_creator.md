---
title: markdown-flowchart-creator
url: https://skills.sh/josephkkmok/markdown-flowchart-creator/markdown-flowchart-creator
---

# markdown-flowchart-creator

skills/josephkkmok/markdown-flowchart-creator/markdown-flowchart-creator
markdown-flowchart-creator
Installation
$ npx skills add https://github.com/josephkkmok/markdown-flowchart-creator --skill markdown-flowchart-creator
SKILL.md
Markdown Flowchart Creator
Overview

Create comprehensive Markdown flowcharts with ASCII diagrams, detailed explanations, and real-world examples. This skill produces documentation-style flowcharts that combine visual flow diagrams with contextual information.

When to Apply

Reference this skill when:

User requests "Create a flowchart in markdown for [process]"
User asks to "Generate a flow diagram as markdown"
User wants to "Make an ASCII flowchart for [workflow]"
User needs to "Document the flow of [system/process]"
User says "Show me how [process] works in markdown"
Key Characteristics

This skill creates documentation-style flowcharts that combine:

ASCII diagrams for visual flow
Detailed explanations of each path
Real-world examples
Configuration details
Benefits and trade-offs
Maintenance commands (when applicable)
Quick Reference
Document Structure Template
# 🔒 [Process Name] Flow Diagram

[Brief description]

---

## Flow Overview

[ASCII diagram showing the main flow]

---

## 🟢 [Path 1 Name]

[Description of when this path is taken]

### Examples:
- Example 1
- Example 2

---

## 🔵 [Path 2 Name]

[Description of when this path is taken]

### Examples:
- Example 1
- Example 2

---

## ⚙️ Configuration Summary

[Relevant configuration, environment variables, etc.]

---

## 📊 Flow Examples

### Example 1: [Scenario Name]
[Step-by-step flow for this scenario]

---

## 🎯 Benefits

[Benefits of different paths/approaches]

---

## 🛠️ Maintenance Commands

[Relevant commands for managing the system]

---

## 📝 Notes

[Important notes and caveats]

ASCII Diagram Patterns
Basic Linear Flow
┌─────────────────┐
│   Start Node    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Process Step   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   End Node      │
└─────────────────┘

Decision Point (Binary)
         │
         ▼
╔════════════════╗
║   Decision?    ║
╚═══════╦════════╝
        │
    ┌───┴───┐
    │       │
  YES       NO
    │       │
    ▼       ▼
┌──────┐ ┌──────┐
│ Path │ │ Path │
│  A   │ │  B   │
└──────┘ └──────┘

Decision Point (Multi-path)
         │
         ▼
╔════════════════╗
║   Decision?    ║
╚═══════╦════════╝
        │
    ┌───┼───┐
    │   │   │
   A    B   C
    │   │   │
    ▼   ▼   ▼

Parallel Paths
        │
        ▼
┌───────────────┐
│ Starting Point│
└───────┬───────┘
        │
    ┌───┴───┐
    │       │
    ▼       ▼
┌──────┐ ┌──────┐
│Path A│ │Path B│
└───┬──┘ └──┬───┘
    │       │
    └───┬───┘
        ▼

Cycle/Loop
┌─────────────────┐
│   Start Loop    │
└────────┬────────┘
         │
         ▼
    ╔════════╗
    ║Continue║ ──NO──┐
    ╚═══╦════╝       │
        │            │
       YES           │
        │            │
        ▼            ▼
┌─────────────┐ ┌────────┐
│ Loop Action │ │  Exit  │
└──────┬──────┘ └────────┘
       │
       └──────┐
              │
              ▼
        [back to top]

Complex Multi-Stage Flow
┌─────────────────────────────────────────────────────────────┐
│                       Starting Point                         │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
                  ╔════════════════════════╗
                  ║      Decision 1?       ║
                  ╚═══════════╦════════════╝
                              │
              ┌───────────────┴───────────────┐
              │                               │
          ✅ YES                          ❌ NO
              │                               │
              ▼                               ▼
  ┌───────────────────────┐      ┌──────────────────────────┐
  │   Path A Process      │      │   Path B Process         │
  └───────────┬───────────┘      └────────────┬─────────────┘
              │                               │
              │                               ▼
              │                   ╔════════════════════════╗
              │                   ║    Sub-Decision?       ║
              │                   ╚═══════════╦════════════╝
              │                               │
              │                    ┌──────────┴──────────┐
              │                    │                     │
              │                  YES                    NO
              │                    │                     │
              ▼                    ▼                     ▼
  ┌───────────────────────┐  ┌─────────┐         ┌─────────┐
  │ ✓ Final Destination   │  │ Result1 │         │ Result2 │
  └───────────────────────┘  └────┬────┘         └────┬────┘
                                  │                    │
                                  └────────┬───────────┘
                                           ▼
                                  ┌────────────────┐
                                  │ Final Outcome  │
                                  └────────────────┘

Character Guide
Box Characters
┌─┐  └─┘  ├─┤  ┬─┴  │  ─
╔═╗  ╚═╝  ╠═╣  ╦═╩  ║  ═

Arrows
→  ←  ↑  ↓  ▲  ▼  ▶  ◀

Connectors
┌  ┐  └  ┘  ├  ┤  ┬  ┴  ┼
╔  ╗  ╚  ╝  ╠  ╣  ╦  ╩  ╬

Emojis for Sections

Use emojis to make sections visually distinct:

🔒 Security/Authentication
🟢 Success/Direct path
🔵 Alternative path
🔴 Error/Failure path
🟡 Warning/Caution
🟠 Internal/System
⚙️ Configuration
📊 Examples/Data
🎯 Benefits/Goals
🛠️ Maintenance/Tools
📝 Notes/Documentation
🔄 Retry/Loop
✅ Yes/Success
❌ No/Failure
📦 Package/Module
🌐 Network/Internet
🔗 Connection/Link
📹 Camera/Media
🚀 Performance/Speed
⚡ Fast/Quick
💰 Cost/Savings
Section Templates
Configuration Section
## ⚙️ Configuration Summary

### Environment Variables (file.yml)

\`\`\`yaml
environment:
  VAR_NAME: value
  ANOTHER_VAR: value
\`\`\`

### Component Settings

#### Component 1
- **Setting**: value
- **Function**: description
- **Config**: path/to/config

Examples Section
## 📊 Flow Examples

### Example 1: [Scenario Name]
\`\`\`
Step 1 → Action 1 → Check condition → ✅ MATCH
→ Path A → Result
\`\`\`

### Example 2: [Scenario Name]
\`\`\`
Step 1 → Action 1 → Check condition → ❌ NO MATCH
→ Path B → Fallback → Result
\`\`\`

Benefits Section
## 🎯 Benefits

### Path A Benefits
- ⚡ **Performance**: Description
- 🔧 **Simplicity**: Description
- 💰 **Cost**: Description

### Path B Benefits
- 🔒 **Security**: Description
- 🌐 **Access**: Description
- 🎭 **Privacy**: Description

Maintenance Commands
## 🛠️ Maintenance Commands

### Command Category 1
\`\`\`bash
command --with-flags
\`\`\`

### Command Category 2
\`\`\`bash
another-command --option
\`\`\`

### View Logs
\`\`\`bash
tail -f /path/to/log
\`\`\`

Content Guidelines
Start with Overview: Always begin with a high-level ASCII diagram showing the complete flow
Use Color Coding: Use emoji circles (🟢🔵🔴🟠) to categorize different paths
Provide Context: Explain WHY each path exists, not just WHAT it does
Include Examples: Show 3-5 real-world scenarios walking through the flow
Add Configuration: Include relevant config files, environment variables, or settings
List Benefits: Explain the trade-offs and benefits of different paths
Maintenance Info: Add commands for monitoring, debugging, and managing the system
Notes Section: Include important caveats, edge cases, or gotchas
File Naming

Save as: [TOPIC]-FLOW.md or [PROCESS]-DIAGRAM.md

Examples:

AUTHENTICATION-FLOW.md
DATA-PIPELINE-DIAGRAM.md
DEPLOYMENT-FLOW.md
Example Prompts

Good prompts:

"Create a markdown flowchart for our authentication process"
"Document the database migration flow in markdown"
"Show how requests are routed in our API gateway as a markdown diagram"
"Create an ASCII flowchart explaining the CI/CD pipeline"

What to deliver:

Complete markdown file with ASCII diagrams
Detailed explanations for each decision point
Real-world examples showing different paths
Configuration details relevant to the flow
Benefits and trade-offs
Maintenance commands when applicable
Tips
Keep diagrams readable: Don't make ASCII diagrams too wide (max 80-100 chars)
Use whitespace: Add blank lines between diagram sections for clarity
Label everything: Every arrow, decision, and path should be labeled
Be consistent: Use the same box style throughout the document
Add context: A diagram alone isn't enough - explain the "why" behind each step
Use code blocks: Wrap ASCII diagrams in triple backticks for proper formatting
Test rendering: Make sure the diagram looks good in both GitHub and text editors
Weekly Installs
12
Repository
josephkkmok/mar…-creator
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass