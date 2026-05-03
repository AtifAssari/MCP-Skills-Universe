---
rating: ⭐⭐
title: ui-mockup
url: https://skills.sh/glittercowboy/plugin-freedom-system/ui-mockup
---

# ui-mockup

skills/glittercowboy/plugin-freedom-system/ui-mockup
ui-mockup
Installation
$ npx skills add https://github.com/glittercowboy/plugin-freedom-system --skill ui-mockup
SKILL.md

<quick_start>

Check for aesthetic library (Phase 0)
Gather requirements through tiered questions (Phases 1-3)
Dispatch ui-design-agent for mockup generation
Iterate until user approves
Generate implementation files </quick_start>

<context_detection> <standalone_mode>

No .continue-here.md file present
Generates mockups independently
Skips state updates </standalone_mode>

<workflow_mode>

File plugins/[PluginName]/.continue-here.md exists with current_stage field
Updates workflow state after each phase </workflow_mode>

Check for .continue-here.md existence to determine mode. If present, update state files. If absent, skip state updates. </context_detection>

How would you like to start the UI design?

Start from aesthetic template - Apply saved visual system
Start from scratch - Create custom design
List all aesthetics - Browse library before deciding

Choose (1-3): _

See references/aesthetic-integration.md for complete integration details.

Include in invocation prompt:

All gathered requirements (layout, controls, colors, etc.)
Quality expectation: "Design must look like commercial $50-200 audio plugin - intentional decisions, not defaults"

See references/phase-details.md for invocation summary. See references/delegation-protocols.md for complete protocol.

Files generated:

v[N]-ui.yaml (design specification)
v[N]-ui-test.html (browser-testable mockup)

What would you like to do?

Iterate - Refine design, adjust layout
Finalize - Validate alignment and complete mockup
Save as template - Add to aesthetic library for reuse
Other

Choose (1-4): _

<iteration_guidance> When collecting feedback for Option 1 (Iterate):

If user provides specific changes ("make it vertical", "add a meter", "change colors to blue"):

Pass these as explicit requirements to new ui-design-agent instance

If user provides vague improvement requests ("make it better", "improve it", "polish it"):

Prompt for specifics: "What aspect should I focus on? (layout, colors, spacing, controls)"
If user says "everything" or "overall quality": Pass instruction to refine existing elements (spacing, color harmony, control styling) rather than add new elements </iteration_guidance>

See references/decision-menus.md#phase-5-5-design-decision-menu for detailed routing.

See references/phase-b-enforcement.md for guard implementation.

<orchestration_protocol> <delegation_rules> This skill NEVER generates mockup files directly. ALL file generation delegated to subagents.

See references/delegation-protocols.md for enforcement details. </delegation_rules>

<state_management> Subagents update .continue-here.md with their phase results. Orchestrator verifies stateUpdated flag in JSON report.

After subagent returns stateUpdated: true, verify actual state contents match expected values (not just boolean flag).

Read .continue-here.md, parse YAML, check specific fields match JSON report values. If mismatch, present state recovery menu.

See references/state-tracking.md for complete state schema and verification protocol. </state_management>

<iteration_protocol> Each iteration runs in fresh agent context. User chooses "Iterate" then orchestrator collects feedback and invokes NEW ui-design-agent with incremented version. Fresh context prevents context window bloat during iterative design. </iteration_protocol>

<error_handling>

Agent failures: Present error menu (retry/manual fix/debug/cancel).
Validation failures: Agent returns validationPassed: false - present error menu.
State update failures: Agent returns stateUpdated: false - present state recovery menu (verify/manual update/continue anyway). </error_handling> </orchestration_protocol>

<versioning_strategy> Pattern: v1, v2, v3... Each version saved separately.

Purpose: Explore layouts without losing work, A/B test designs, keep history for rollback.

File naming: All 7 files prefixed with version (e.g., v2-ui.html, v2-PluginEditor.h).

Implementation: Latest version used for Stage 3 (GUI) unless user specifies different version.

See references/versioning.md for file management details. </versioning_strategy>

<success_criteria> <design_phase>

YAML spec generated matching user requirements
Browser test HTML works (interactive controls, parameter messages)
Visual quality meets commercial standard (intentional design, not defaults)
Design files committed to git
.continue-here.md updated with version (if workflow mode)
User presented with Phase 5.5 decision menu
Design approved OR user iterates with refinements </design_phase>

<implementation_phase>

All 7 files generated and saved to .ideas/mockups/
Production HTML complete (no placeholders)
C++ boilerplate matches YAML structure (correct parameter bindings)
parameter-spec.md generated and locked (v1 only)
Implementation files committed to git
.continue-here.md updated with finalization status (if workflow mode) </implementation_phase> </success_criteria>

<integration_points> <invoked_by>

/dream command - After creative brief, before implementation
plugin-workflow skill - During Stage 0 (UI design phase)
plugin-improve skill - When redesigning existing plugin UI
Natural language: "Design UI for [PluginName]", "Create mockup for compressor" </invoked_by>

<always_invokes>

ui-design-agent subagent (Phase 4-5.45) - REQUIRED for design iteration
ui-finalization-agent subagent (Phase 6-10.5) - REQUIRED for implementation files </always_invokes>

<also_invokes>

ui-template-library skill (if user saves aesthetic) </also_invokes>

<reference_documentation> Progressive disclosure - load references when reaching specific phases:

Phase 0: references/aesthetic-integration.md - Aesthetic library integration
Phase 1: references/context-extraction.md - Creative brief extraction
Phase 2-3: references/design-questions.md - Question templates and tiering
Phase 2.5: references/layout-validation.md - Dimension calculation formulas
Phase 4-5.45: references/delegation-protocols.md - Subagent invocation
Phase 5.5: references/decision-menus.md - Menu format and routing
Phase 5.6: references/state-tracking.md - Brief sync protocol
Phase 6-10: references/phase-b-enforcement.md - Phase B guard
Anti-patterns: references/common-pitfalls.md - What to avoid

Technical details:

references/html-generation.md - Production HTML rules
references/browser-testing.md - Browser test workflow
references/cmake-configuration.md - WebView build settings
references/cpp-boilerplate-generation.md - C++ template generation
references/ui-design-rules.md - Design constraints and patterns
references/versioning.md - File management </reference_documentation>

<template_assets>

assets/ui-yaml-template.yaml - YAML structure
assets/webview-boilerplate.md - C++ integration templates
assets/integration-checklist-template.md - Integration guide
assets/parameter-spec-template.md - Parameter specification format </template_assets>
Weekly Installs
23
Repository
glittercowboy/p…m-system
GitHub Stars
182
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass