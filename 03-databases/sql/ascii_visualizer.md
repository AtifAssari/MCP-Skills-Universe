---
title: ascii-visualizer
url: https://skills.sh/yonatangross/orchestkit/ascii-visualizer
---

# ascii-visualizer

skills/yonatangross/orchestkit/ascii-visualizer
ascii-visualizer
Installation
$ npx skills add https://github.com/yonatangross/orchestkit --skill ascii-visualizer
SKILL.md
ASCII Visualizer

Consistent, readable ASCII diagrams for architecture, workflows, file trees, and data visualizations. All output renders correctly in monospace terminals without external tools.

Core principle: Encode information into structure, not decoration. Every diagram element should communicate something meaningful.

Box-Drawing Character Reference
Standard:  ┌─┐ │ └─┘  ├─┤ ┬ ┴ ┼
Heavy:     ┏━┓ ┃ ┗━┛  ┣━┫ ┳ ┻ ╋
Double:    ╔═╗ ║ ╚═╝  ╠═╣ ╦ ╩ ╬
Rounded:   ╭─╮ │ ╰─╯
Arrows:    → ← ↑ ↓ ─> <─ ──> <──
Blocks:    █ ▓ ░ ▏▎▍▌▋▊▉
Checks:    ✓ ✗ ● ○ ◆ ◇ ★ ☆

Weight Conventions
Weight	Characters	Use For
Standard ─│	Normal boxes and connectors	Most diagrams
Heavy ━┃	Emphasis, borders, headers	Key components, outer frames
Double ═║	Separation, titles	Section dividers, title boxes
Diagram Patterns
Architecture Diagrams
┌──────────────┐      ┌──────────────┐
│   Frontend   │─────>│   Backend    │
│   React 19   │      │   FastAPI    │
└──────────────┘      └───────┬──────┘
                              │
                              v
                      ┌──────────────┐
                      │  PostgreSQL  │
                      └──────────────┘

File Trees with Annotations
src/
├── api/
│   ├── routes.py          [M] +45 -12    !! high-traffic path
│   └── schemas.py         [M] +20 -5
├── services/
│   └── billing.py         [A] +180       ** new file
└── tests/
    └── test_billing.py    [A] +120       ** new file

Legend: [A]dd [M]odify [D]elete  !! Risk  ** New

Progress Bars
[████████░░] 80% Complete
+ Design    (2 days)
+ Backend   (5 days)
~ Frontend  (3 days)
- Testing   (pending)

Swimlane / Timeline Diagrams
Backend  ===[Schema]======[API]===========================[Deploy]====>
                |            |                                ^
                |            +------blocks------+             |
                |                               |             |
Frontend ------[Wait]--------[Components]=======[Integration]=+

=== Active work   --- Blocked/waiting   | Dependency

Blast Radius (Concentric Rings)
            Ring 3: Tests (8 files)
       +-------------------------------+
       |    Ring 2: Transitive (5)      |
       |   +------------------------+   |
       |   |  Ring 1: Direct (3)     |   |
       |   |   +--------------+      |   |
       |   |   | CHANGED FILE |      |   |
       |   |   +--------------+      |   |
       |   +------------------------+   |
       +-------------------------------+

Comparison Tables
BEFORE                          AFTER
┌────────────┐                  ┌────────────┐
│  Monolith  │                  │  Service A │──┐
│  (all-in-1)│                  └────────────┘  │  ┌──────────┐
└────────────┘                  ┌────────────┐  ├─>│  Shared  │
                                │  Service B │──┘  │  Queue   │
                                └────────────┘     └──────────┘

Reversibility Timeline
Phase 1  [================]  FULLY REVERSIBLE    (add column)
Phase 2  [================]  FULLY REVERSIBLE    (new endpoint)
Phase 3  [============....]  PARTIALLY           (backfill)
              --- POINT OF NO RETURN ---
Phase 4  [........????????]  IRREVERSIBLE        (drop column)

Key Rules
Rule	Description
Font	Always monospace — box-drawing requires fixed-width
Weight	Standard for normal, Heavy for emphasis, Double for titles
Arrows	─>, ──>, or │ with v/^ for direction
Alignment	Right-pad labels to match column widths
Annotations	!! for risk, ** for new, [A/M/D] for change type
Width	Keep under 80 chars for terminal compatibility
Nesting	Max 3 levels of box nesting before readability degrades
When to Use Each Pattern
Pattern	Use Case
Layered boxes	System architecture, deployment topology
Concentric rings	Blast radius, impact analysis
Timeline bars	Reversibility, migration phases
Swimlanes	Execution order, parallel work streams
Annotated trees	File change manifests, directory structures
Comparison tables	Cross-layer consistency, before/after
Progress bars	Status tracking, completion metrics
Related Skills
brainstorm — Design exploration where diagrams communicate ideas
architecture-patterns — System architecture that benefits from ASCII diagrams
code-review-playbook — Review comments with inline diagrams
Weekly Installs
161
Repository
yonatangross/orchestkit
GitHub Stars
162
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass