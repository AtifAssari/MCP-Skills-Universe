---
title: mermaid
url: https://skills.sh/markdown-viewer/skills/mermaid
---

# mermaid

skills/markdown-viewer/skills/mermaid
mermaid
Installation
$ npx skills add https://github.com/markdown-viewer/skills --skill mermaid
SKILL.md
Mermaid Diagram Visualizer

Quick Start: Identify diagram type (flowchart/sequence/state/class/ER/gantt/mindmap) → Define nodes with shapes → Connect with arrows → Wrap in ```mermaid fence. Default: top-to-bottom (TD), use flowchart over graph, Unicode supported.

Critical Syntax Rules
Rule 1: List Syntax Conflicts
❌ [1. Item]     → "Unsupported markdown: list"
✅ [1.Item]      → Remove space after period
✅ [① Item]      → Use circled numbers ①②③④⑤⑥⑦⑧⑨⑩
✅ [(1) Item]    → Use parentheses

Rule 2: Subgraph Naming
❌ subgraph AI Agent Core    → Space without quotes
✅ subgraph agent["AI Agent Core"]  → ID with display name
✅ subgraph agent            → Simple ID only

Rule 3: Node References in Subgraphs
❌ Title --> AI Agent Core   → Reference display name
✅ Title --> agent           → Reference subgraph ID

Rule 4: Special Characters in Node Text
✅ ["Text with spaces"]       → Quotes for spaces
✅ Use #quot; instead of "    → Avoid quotation marks
✅ Use #lpar;#rpar; for ()    → Avoid parentheses

Rule 5: Use flowchart over graph
❌ graph TD      → Outdated
✅ flowchart TD  → Supports subgraph directions, more features

Common Pitfalls
Issue	Solution
Diagram won't render	Check unmatched brackets, quotes
List syntax error	[1.Item] not [1. Item]
Subgraph reference fails	Use ID not display name
Too crowded	Split into multiple diagrams
Crossing connections	Use different layout direction or invisible edges ~~~
Output Format
```mermaid
[diagram code]
```

Related Files

For diagram-specific syntax and advanced features, refer to references below:

syntax.md — Detailed syntax for all 14+ diagram types: flowchart shapes, sequence actors, class relationships, state transitions, ER cardinality, Gantt tasks, and more
Weekly Installs
542
Repository
markdown-viewer/skills
GitHub Stars
2.4K
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass