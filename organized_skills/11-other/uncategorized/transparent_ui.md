---
rating: ⭐⭐
title: transparent-ui
url: https://skills.sh/petekp/claude-code-setup/transparent-ui
---

# transparent-ui

skills/petekp/claude-code-setup/transparent-ui
transparent-ui
Installation
$ npx skills add https://github.com/petekp/claude-code-setup --skill transparent-ui
SKILL.md
Transparent UI

Build temporary debugging interfaces that make invisible system behavior visible. These are development-only routes/pages that reveal internal state, transitions, and data flow through interactive visualization.

Core Principles

Make the invisible visible. Show state that normally exists only in memory. Reveal transitions that happen too fast to observe. Surface the "why" behind system behavior.

Temporary by design. These are debugging tools, not production features. Keep changes isolated for easy removal. Use dev-only routes and environment checks.

Use existing components. Build with the project's component library and design system. The visualization should feel native to the codebase, not like a foreign debugging tool.

Match instrumentation to context. Sometimes minimal logging is enough; sometimes a full observable wrapper is needed. Choose the lightest approach that captures the necessary information.

Workflow
Step 1: Identify What to Make Transparent

Analyze the system and identify:

State: What values change over time? What's the shape of the data?
Transitions: What events trigger state changes? What's the sequence?
Relationships: How do components/modules communicate? What depends on what?
Hidden logic: What conditions, thresholds, or rules govern behavior?

Ask the user clarifying questions if the system boundary is unclear.

Step 2: Choose Visualization Approach

Select based on the system's nature. See references/patterns.md for domain-specific guidance.

System Type	Primary Visualization	Key Elements
State machines	Node-edge graph	States as nodes, transitions as edges, current state highlighted
Data flow	Directed graph or Sankey	Sources, transformations, sinks with data flowing between
Event systems	Timeline or sequence diagram	Events on time axis, handlers, propagation paths
Algorithms	Step-by-step animation	Data structure state at each step, highlighting active elements
Render/update cycles	Tree with diff overlay	Component tree, what re-rendered, why
Animations	Timeline scrubber	Keyframes, easing curves, current progress
CSS/Layout	Box model overlay	Computed values, constraint sources
Step 3: Design Interactivity Level

Layer interactivity based on debugging needs:

Level 1 - Observation: Real-time display of current state and recent changes. Always include this.

Level 2 - Inspection: Click/hover to see details. Expand nodes, view full payloads, trace data origins.

Level 3 - Manipulation: Trigger events, modify state, inject test data. Useful for reproducing edge cases.

Level 4 - Time travel: Record history, scrub through past states, replay sequences. Essential for race conditions and timing bugs.

Start with Level 1-2. Add 3-4 when the user needs them.

Step 4: Instrument the System

Choose instrumentation strategy based on invasiveness tolerance:

Minimal (prefer when possible):

Add event emitters at key points
Wrap state setters to broadcast changes
Use existing debug/logging hooks if available

Wrapper/Proxy approach:

Create observable wrappers around the system
Intercept calls without modifying core code
Useful for third-party code or when core modifications are undesirable

Implementation patterns:

// Event emitter pattern - add to existing code
const debugEmitter = new EventEmitter();
function transition(from: State, to: State, event: string) {
  debugEmitter.emit('transition', { from, to, event, timestamp: Date.now() });
  // ... existing logic
}

// Proxy pattern - wrap without modifying
function createObservableStore<T>(store: T): T & { subscribe: (fn: Listener) => void } {
  const listeners: Listener[] = [];
  return new Proxy(store, {
    set(target, prop, value) {
      const oldValue = target[prop];
      target[prop] = value;
      listeners.forEach(fn => fn({ prop, oldValue, newValue: value }));
      return true;
    }
  });
}

Step 5: Build the Debug Route

Create a development-only route that:

Guards against production: Check process.env.NODE_ENV === 'development'
Connects to instrumentation: Subscribe to events/state changes
Renders visualization: Use the project's components where possible
Provides controls: Play/pause, speed, filters, time scrubbing as needed

Route structure (Next.js example):

app/
  __dev/
    transparent/
      [system]/
        page.tsx    # Dynamic route for different systems


Or simpler:

app/
  __dev/
    state-machine/
      page.tsx


Recommended libraries (install only if not already in project):

react-flow or reactflow: Node-edge graphs for state machines, data flow
framer-motion: Smooth transitions in visualization itself
Existing charting library: If project already has one, use it
Step 6: Document Removal Path

At the top of every file created, add:

/**
 * TRANSPARENT-UI DEBUG TOOL
 *
 * Temporary debugging visualization. Remove when no longer needed:
 * 1. Delete this file: app/__dev/[name]/page.tsx
 * 2. Delete instrumentation: src/lib/[system]-debug.ts
 * 3. Remove debug hooks from: src/lib/[system].ts (lines XX-YY)
 *
 * Created for: [description of what this helps debug]
 */

Cleanup

When the user asks to remove the transparent UI or is done debugging:

Delete debug route: Remove the __dev/ page(s)
Remove instrumentation: Delete event emitters, proxies, debug hooks
Uninstall unused deps: If visualization libraries were added solely for this
Verify no remnants: Search for debugEmitter, TRANSPARENT-UI, or similar markers

Provide a summary of removed files and modified lines.

Domain-Specific Patterns

For detailed visualization patterns, layouts, and code examples organized by system type, see references/patterns.md.

Weekly Installs
18
Repository
petekp/claude-code-setup
GitHub Stars
35
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass