---
title: swiftui-performance-audit
url: https://skills.sh/dimillian/skills/swiftui-performance-audit
---

# swiftui-performance-audit

skills/dimillian/skills/swiftui-performance-audit
swiftui-performance-audit
Originally fromopenai/plugins
Installation
$ npx skills add https://github.com/dimillian/skills --skill swiftui-performance-audit
Summary

Diagnose and fix SwiftUI performance issues through code review and Instruments profiling guidance.

Classifies symptoms (slow rendering, janky scrolling, CPU spikes, memory growth, hangs, excessive view updates) and performs code-first review against common anti-patterns like invalidation storms, unstable list identity, and layout thrash.
Guides users through Instruments profiling when code review alone is inconclusive, with structured intake checklists and trace analysis.
Provides remediation patterns for state scope narrowing, identity stabilization, moving heavy work out of body, and image optimization, with before/after validation steps.
SKILL.md
SwiftUI Performance Audit
Quick start

Use this skill to diagnose SwiftUI performance issues from code first, then request profiling evidence when code review alone cannot explain the symptoms.

Workflow
Classify the symptom: slow rendering, janky scrolling, high CPU, memory growth, hangs, or excessive view updates.
If code is available, start with a code-first review using references/code-smells.md.
If code is not available, ask for the smallest useful slice: target view, data flow, reproduction steps, and deployment target.
If code review is inconclusive or runtime evidence is required, guide the user through profiling with references/profiling-intake.md.
Summarize likely causes, evidence, remediation, and validation steps using references/report-template.md.
1. Intake

Collect:

Target view or feature code.
Symptoms and exact reproduction steps.
Data flow: @State, @Binding, environment dependencies, and observable models.
Whether the issue shows up on device or simulator, and whether it was observed in Debug or Release.

Ask the user to classify the issue if possible:

CPU spike or battery drain
Janky scrolling or dropped frames
High memory or image pressure
Hangs or unresponsive interactions
Excessive or unexpectedly broad view updates

For the full profiling intake checklist, read references/profiling-intake.md.

2. Code-First Review

Focus on:

Invalidation storms from broad observation or environment reads.
Unstable identity in lists and ForEach.
Heavy derived work in body or view builders.
Layout thrash from complex hierarchies, GeometryReader, or preference chains.
Large image decode or resize work on the main thread.
Animation or transition work applied too broadly.

Use references/code-smells.md for the detailed smell catalog and fix guidance.

Provide:

Likely root causes with code references.
Suggested fixes and refactors.
If needed, a minimal repro or instrumentation suggestion.
3. Guide the User to Profile

If code review does not explain the issue, ask for runtime evidence:

A trace export or screenshots of the SwiftUI timeline and Time Profiler call tree.
Device/OS/build configuration.
The exact interaction being profiled.
Before/after metrics if the user is comparing a change.

Use references/profiling-intake.md for the exact checklist and collection steps.

4. Analyze and Diagnose
Map the evidence to the most likely category: invalidation, identity churn, layout thrash, main-thread work, image cost, or animation cost.
Prioritize problems by impact, not by how easy they are to explain.
Distinguish code-level suspicion from trace-backed evidence.
Call out when profiling is still insufficient and what additional evidence would reduce uncertainty.
5. Remediate

Apply targeted fixes:

Narrow state scope and reduce broad observation fan-out.
Stabilize identities for ForEach and lists.
Move heavy work out of body into derived state updated from inputs, model-layer precomputation, memoized helpers, or background preprocessing. Use @State only for view-owned state, not as an ad hoc cache for arbitrary computation.
Use equatable() only when equality is cheaper than recomputing the subtree and the inputs are truly value-semantic.
Downsample images before rendering.
Reduce layout complexity or use fixed sizing where possible.

Use references/code-smells.md for examples, Observation-specific fan-out guidance, and remediation patterns.

6. Verify

Ask the user to re-run the same capture and compare with baseline metrics. Summarize the delta (CPU, frame drops, memory peak) if provided.

Outputs

Provide:

A short metrics table (before/after if available).
Top issues (ordered by impact).
Proposed fixes with estimated effort.

Use references/report-template.md when formatting the final audit.

References
Profiling intake and collection checklist: references/profiling-intake.md
Common code smells and remediation patterns: references/code-smells.md
Audit output template: references/report-template.md
Add Apple documentation and WWDC resources under references/ as they are supplied by the user.
Optimizing SwiftUI performance with Instruments: references/optimizing-swiftui-performance-instruments.md
Understanding and improving SwiftUI performance: references/understanding-improving-swiftui-performance.md
Understanding hangs in your app: references/understanding-hangs-in-your-app.md
Demystify SwiftUI performance (WWDC23): references/demystify-swiftui-performance-wwdc23.md
Weekly Installs
6.8K
Repository
dimillian/skills
GitHub Stars
3.4K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass