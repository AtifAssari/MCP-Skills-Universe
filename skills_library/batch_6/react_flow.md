---
title: react-flow
url: https://skills.sh/framara/react-flow-skill/react-flow
---

# react-flow

skills/framara/react-flow-skill/react-flow
react-flow
Installation
$ npx skills add https://github.com/framara/react-flow-skill --skill react-flow
SKILL.md
React Flow
Overview

Use this skill to build, customize, debug, and optimize interactive node-based UIs with React Flow (@xyflow/react v12+). Covers everything from basic setup to advanced patterns like computed flows, sub-flows, and external layout integration.

Agent behavior contract (follow these rules)
Always import from @xyflow/react — never from legacy reactflow or react-flow-renderer packages.
Always import the stylesheet: import '@xyflow/react/dist/style.css' (or base.css for custom styling frameworks).
The <ReactFlow> parent container must have explicit width and height — this is the #1 cause of blank canvases.
Define nodeTypes and edgeTypes objects outside component bodies or wrap in useMemo to prevent re-renders.
Prefer custom nodes over built-in nodes — the React Flow team explicitly recommends this.
Use the nodrag class on interactive elements inside custom nodes (inputs, buttons, selects).
Use nowheel class on scrollable elements inside custom nodes to prevent zoom interference.
When hiding handles, use visibility: hidden or opacity: 0 — never display: none (breaks dimension calculation).
When using multiple handles of the same type on a node, always assign unique id props.
After programmatically adding/removing handles, call useUpdateNodeInternals to refresh the node.
Always create new objects when updating node/edge state — mutations are not detected by React Flow.
Prefer controlled flows (with onNodesChange/onEdgesChange/onConnect) for any non-trivial application.
First 60 seconds (triage template)
Clarify the goal: new flow setup, custom nodes/edges, state management, layout, performance, styling, E2E testing, advanced patterns (undo/redo, copy/paste, computed flows, collaboration), or debugging.
Collect minimal facts:
React Flow version (v12+ uses @xyflow/react)
TypeScript or JavaScript
State management approach (local state, Zustand, Redux)
Number of nodes expected (affects performance strategy)
Styling approach (CSS, Tailwind, styled-components)
Branch quickly:
migrating from legacy reactflow or react-flow-renderer -> package rename, import changes, API differences
blank canvas or missing nodes -> container dimensions or missing CSS import
edges not rendering -> missing handles, missing CSS, or display: none on handles
re-renders or sluggish performance -> nodeTypes defined inside component, missing memoization
connecting nodes not working -> missing onConnect handler or handle configuration
layout/positioning -> external layout library integration (dagre, elkjs)
type errors -> TypeScript generic patterns for Node/Edge types
Routing map (read the right reference fast)
Migrating from reactflow or react-flow-renderer to @xyflow/react v12 -> references/migration.md
Installation, setup, first flow, node/edge objects -> references/fundamentals.md
Custom node components, Handle, multiple handles, drag handles -> references/custom-nodes.md
Custom edge components, path utilities, edge labels, markers -> references/custom-edges.md
Event handlers, callbacks, connection validation, selection, keyboard -> references/interactivity.md
Controlled vs uncontrolled, Zustand integration, state update patterns -> references/state-management.md
Node/Edge types, generics, union types, type guards -> references/typescript.md
External layout libraries (dagre, elkjs, d3), sub-flows, parent-child -> references/layouting.md
Background, Controls, MiniMap, Panel, NodeToolbar, NodeResizer, hooks -> references/components-and-hooks.md
Memoization, render optimization, theming, CSS variables, Tailwind -> references/performance-and-styling.md
Common errors, debugging, edge display issues, Zustand warnings -> references/troubleshooting.md
Playwright E2E tests, flow selectors, drag/viewport/connection testing -> references/e2e-testing.md
Undo/redo, copy/paste, computed flows, dynamic handles, save/restore, collaboration -> references/advanced-patterns.md
Context menu add node, drag-and-drop sidebar, detail panel, export as image -> references/recipes.md
Common pitfalls -> next best move
Blank canvas with no errors -> parent container has no height; set explicit height: 100vh or equivalent.
nodeTypes / edgeTypes warning -> move object definition outside component body or wrap in useMemo.
Edges render but in wrong position -> handles use display: none; switch to opacity: 0.
Cannot interact with inputs inside nodes -> add className="nodrag" to interactive elements.
Nodes snap back after drag -> onNodesChange not wired up or not applying changes correctly.
Connection line appears but edge never creates -> onConnect handler missing or not calling addEdge.
Multiple handles on same side overlap -> position them with CSS (top offset) and assign unique ids.
State updates don't reflect in nodes -> creating mutations instead of new objects; spread operator required.
Zustand context warning -> two versions of @xyflow/react installed or missing <ReactFlowProvider>.
Sub-flow child nodes render behind parent -> ensure parent nodes appear before children in the nodes array.
Verification checklist
Confirm @xyflow/react/dist/style.css is imported (or base.css + custom styles).
Confirm parent container has explicit width and height.
Confirm nodeTypes / edgeTypes are stable references (defined outside component or memoized).
Confirm custom nodes use <Handle> components with proper type and position.
Confirm interactive elements inside nodes have nodrag class.
Confirm controlled flows wire up all three handlers: onNodesChange, onEdgesChange, onConnect.
Confirm state updates create new node/edge objects (no mutations).
Confirm TypeScript generics are applied to hooks and callbacks for type safety.
Confirm performance-sensitive flows memoize custom node/edge components with React.memo.
References
references/migration.md
references/fundamentals.md
references/custom-nodes.md
references/custom-edges.md
references/interactivity.md
references/state-management.md
references/typescript.md
references/layouting.md
references/components-and-hooks.md
references/performance-and-styling.md
references/troubleshooting.md
references/e2e-testing.md
references/advanced-patterns.md
references/recipes.md
Weekly Installs
250
Repository
framara/react-flow-skill
GitHub Stars
23
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn