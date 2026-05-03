---
rating: ⭐⭐⭐
title: c4-interactive-html
url: https://skills.sh/wghust/stark-skills/c4-interactive-html
---

# c4-interactive-html

skills/wghust/stark-skills/c4-interactive-html
c4-interactive-html
Installation
$ npx skills add https://github.com/wghust/stark-skills --skill c4-interactive-html
SKILL.md
c4-interactive-html

Language: Match the user's language (中文提问则中文回复).

When this skill applies, the agent MUST analyze the user's current workspace project (the opened repo), then generate one self-contained HTML file that implements the interactive C4 viewer described below. Do not only describe the HTML—write the file to disk.

Architectural anchors (from design)
L1: The current product/repo is the core system (highlighted, only node that drills to L2).
L2: Containers arranged in a left-to-right columnar layout inside a dashed system boundary box; only the container that has L3 content shows the drill badge.
L3: Exactly one chosen core container (e.g. main API or main web app) is expanded; others stay at L2 only.
Evidence: Prefer facts from files; in the side panel, state inference basis when uncertain (e.g. "inferred from docker-compose.yml").
Step 1 · Analyze project architecture

Read enough of the repo to justify the diagram:

Build & package

pom.xml, build.gradle, package.json, go.mod, requirements.txt, Cargo.toml, etc.

Config & ops

application.yml, docker-compose.yml, Dockerfile, .env (or .env.example)

Entry & layout

App entry points, src/ or language-idiomatic structure, notable modules

C4 elements to identify

Level	What to capture
People	End users, admins, operators, integrators—who uses or operates the system
L1 Software system	This system + external dependencies (DB, MQ, 3rd-party APIs, other microservices)
L2 Containers	Deployable/runnable units: web apps, APIs, workers, DB, cache, brokers, etc.
L3 Components	Inside one core container: controllers/services/repositories/modules—only the most important slice

Large or unclear repos: Prefer a representative L3; merge minor pieces into grouped nodes; document scope in node sub or side panel.

Step 2 · Build the interactive HTML
Overall design

Navigation UI (unchanged): The top bar (project name + clickable breadcrumb L1 / L2 / L3) and the legend row (colored category dots below the breadcrumb) are fixed navigation elements—do not alter their appearance. All visual rules in the sections below apply exclusively to the SVG canvas drawing area that occupies the rest of the page.

Theme: Light, professional—white/light gray background, clean typography.
Top bar: Project name + breadcrumb L1 / L2 / L3 (each segment clickable to go back to that level). Unchanged.
Legend row: Colored dots for node categories (People / core / external / interface / domain / infra, etc.—align with your legends data). Unchanged.
Canvas drawing area

Everything below lives inside the SVG canvas drawing zone (below the navigation chrome).

Diagram title block (top-center of canvas)

Render a centered title block at the very top of the SVG/canvas area—not as the browser <title> tag:

Bold title (large): Container View: <project-name> for L2; System Context: <project-name> for L1; Component View: <container-name> for L3.
Subtitle (small, gray): one-sentence architectural scope derived from the project README first sentence, or composed by the agent (e.g. "展示接口层、应用层、领域层、基础设施层的分层架构。"). Keep ≤ 80 characters.
Three canvases

1) L1 System Context (default)

Layout: People (left), core system (center, highlighted, clickable → L2), external systems (right).
SVG curved edges between nodes; label protocol when known (HTTP, gRPC, MQ, JDBC, etc.).
Only the core system shows a "点击下钻" (or "Drill down ↓") badge; all other nodes use opacity: 0.5 (dimmed).
Click core → switch canvas to L2.
Click dimmed node → open right panel (relationships + description); do not change level.

2) L2 Containers

System boundary box: Draw a dashed/dotted rectangle around all internal containers. At its top-center place a label <system-name> [system]. This box is only on L2—not on L1 or L3.

Left-to-right columnar layout (People outside boundary, internal layers inside):

[Outside boundary, left]       [Inside dashed boundary box]

People / External          ┌─接口层──┬──应用层──┬──领域层──┬──基础设施层─┐
trigger systems            │         │          │          │             │
(边界框外左侧)              │  nodes  │  nodes   │  nodes   │   nodes     │
                           └─────────┴──────────┴──────────┴─────────────┘

People and external trigger systems sit outside the boundary box, to its left; their edges cross the box border into the interface-layer containers.
Internal containers are arranged as vertical columns left → right: interface layer → application layer → domain layer → infrastructure layer (or detected equivalents).
Each column has a small gray column-header label at the top (e.g. 接口层, 应用层); columns are separated by a subtle visual gap.
Infrastructure layer with 6+ nodes MAY wrap into two rows instead of stretching horizontally.
Canvas min-width: 1200px; allow horizontal scrolling so the layout is never clipped on narrow screens.
SVG curved edges for calls/data flow.
Only the container that has L3 content: colored border + drill badge + cursor: pointer.
Containers without L3: dimmed (opacity: 0.5), no badge; click opens panel only.
Click drillable container → L3.

3) L3 Components

Components grouped by function; SVG edges for dependencies.
Every node click opens the side panel (no further drill level required).
Right panel
Fixed width 380px, slides in from the right.
Shows: name, level badge (L1/L2/L3), description, related relationships (list of edges touching the node).
ESC or × closes the panel.
Node styling

Each node card uses a three-part layout (matches the c4.png reference design):

┌──────────────────────────────────┐
│  REST API                        │  ← bold name  (label)
│  [Spring Boot REST]              │  ← [tech]  italic / secondary-gray
│                                  │
│  对外提供 HTTP 接口，包含 AI、     │  ← multi-line description (sub)
│  标签 6 个 Controller。          │    small font, wraps naturally
└──────────────────────────────────┘

label: bold, top of card.
tech (new, optional): rendered as [<tech>] in italic or secondary-gray on line 2. Omit the line entirely if tech is absent or empty.
sub: small multi-line description. Truncate with … if it overflows the card max height; show full text in the side panel.
Node minimum height should accommodate ~3 lines of text.

Drill / dim / select states:

Drillable: colored border/background treatment + top-right badge "点击下钻 ↓" + cursor: pointer.
Non-drillable: opacity: 0.5, no badge; click → panel only.
Selected: blue glow/shadow; incident edges emphasized; other edges and nodes fade.
Edge label convention

Render all edge protocol/call-style labels enclosed in square brackets: [HTTPS], [Java Method], [Spring Event], [Feign/HTTP], [JDBC], etc.

The renderer wraps the protocol value in brackets automatically—do not include brackets in the data field.
Position the label mid-edge, small font, with sufficient contrast (e.g. light-background pill or gray text on white).
If protocol is absent, draw the arrow but show no label.
Data shape (embed in HTML)

Use one object per level (names L1, L2, L3—be consistent in JS):

const L1 = {
  nodes: [
    {
      id: 'unique-id',
      label: '显示名称',          // bold node name
      tech: 'Spring Boot REST',   // optional — rendered as [Spring Boot REST]
      sub: '描述 / 推断依据',      // multi-line description
      c: 'color-key',
      x: 0,
      y: 0,
      w: 200,
      drill: true,
      drillTo: 'L2',
    },
  ],
  edges: [
    { f: 'from-id', t: 'to-id', c: 'color-key', protocol: 'HTTP' },
    // protocol value is auto-wrapped as [HTTP] by the renderer
  ],
  layers: [{ y: 120, label: '层名称', color: '#ccc' }],
  legends: [{ c: 'core', l: '核心系统' }],
};

c: maps to the palette / CSS class for node category.
No external JSON fetch—all data inline in the same file.
Color palette (light mode)
Background #f5f7fa, cards #ffffff, hover #f0f2f5
Core: #1168BD · Domain/data: #2b8a3e · External/AI: #6f42c1 · Interface: #d4620a · Governance: #b8860b
Fonts
Allowed external dependency: Google Fonts CDN (e.g. a Latin + CJK-friendly stack). If CDN is undesirable, use a system font stack that supports Chinese: e.g. system-ui, "PingFang SC", "Microsoft YaHei", sans-serif.
Canvas legend (bottom-right, C4 notation)

Place a compact C4 notation legend in the bottom-right corner of the canvas (inside the SVG drawing area, separate from the navigation legend row above):

Symbol	Visual	Label
Person	Person-silhouette SVG icon (circle head + body outline) or 👤 Unicode fallback	person
Software System	Plain rectangle outline	system
Container	Filled / shaded rectangle	container

Prefer inline SVG paths for cross-browser consistency; use Unicode + CSS as fallback. Ensure the legend does not overlap nodes or edges.

Layout quality
Avoid overlapping nodes; keep edge labels readable; use canvas size / coordinates so the diagram fits a typical laptop viewport with scroll as fallback.
Step 3 · Output path
Default filename: c4-<dirname>-architecture.html where <dirname> is the basename of the workspace root (e.g. workspace at /projects/my-app → c4-my-app-architecture.html). Sanitize <dirname>: replace spaces and non-alphanumeric characters with -; lowercase preferred. Save at the workspace root.
User override (same turn): if the user specifies a filename or path, honor it exactly and skip the dynamic naming rule.
Multi-root workspace: if several folders are open and the user did not specify a project, use the root that was the focus of architecture analysis, or ask which root to use before writing.
Unknown root or not writable: do not silently fall back to ~/Downloads or elsewhere. Ask the user for an explicit directory or full file path and state the reason (e.g. permission, ambiguous root).
After writing, confirm the absolute path in the assistant message.
Acceptance checklist (before finishing)
 Single file, opens in a normal browser; no npm/build step.
 Navigation UI unchanged: top bar breadcrumb and legend dot row look the same as the base skill spec.
 Canvas title block (bold title + subtitle) visible at top of drawing area.
 L2: system dashed boundary box present; People nodes outside boundary to the left; left→right column layout with column-header labels.
 Nodes show three-part layout: bold name + [tech] (if present) + multi-line description.
 Edge labels appear as [protocol] mid-edge; no label when protocol absent.
 Canvas bottom-right C4 legend symbols (person / system / container) present and not obscuring nodes.
 Breadcrumb, L1/L2/L3 drill behavior, panel, ESC close, selection highlight—all functional.
 Core system-only drill on L1; single L3 target; dimmed nodes behave as specified.
 Chinese labels render correctly (<meta charset="utf-8"> + fonts).
 Filename is c4-<dirname>-architecture.html (or user-specified); absolute path confirmed in reply.
Related doc

See USAGE.md in this folder for FAQs (path override, minimal backends, offline fonts).

Weekly Installs
12
Repository
wghust/stark-skills
GitHub Stars
4
First Seen
Apr 8, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass