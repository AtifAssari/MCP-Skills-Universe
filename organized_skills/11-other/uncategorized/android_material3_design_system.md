---
rating: ⭐⭐
title: android-material3-design-system
url: https://skills.sh/krutikjain/android-agent-skills/android-material3-design-system
---

# android-material3-design-system

skills/krutikjain/android-agent-skills/android-material3-design-system
android-material3-design-system
Installation
$ npx skills add https://github.com/krutikjain/android-agent-skills --skill android-material3-design-system
SKILL.md
Android Material3 Design System
When To Use
Use this skill when the request is about: material3 theme android, design system tokens compose, android typography color system.
Primary outcome: Apply Material 3 tokens, color, type, spacing, adaptive components, and theme ownership in Android apps.
Handoff skills when the scope expands:
android-compose-foundations
android-compose-accessibility
Workflow
Identify whether the target surface is Compose, View system, or a mixed interoperability screen.
Select the lowest-friction UI pattern that satisfies responsiveness, accessibility, and performance needs.
Build the UI around stable state, explicit side effects, and reusable design tokens.
Exercise edge cases such as long text, font scaling, RTL, and narrow devices in the fixture apps.
Validate with unit, UI, and screenshot-friendly checks before handing off.
Guardrails
Optimize for stable state and predictable rendering before adding animation or abstraction.
Respect accessibility semantics, contrast, focus order, and touch target guidance by default.
Do not mix Compose and View system ownership without an explicit interoperability boundary.
Prefer measured performance work over premature micro-optimizations.
Anti-Patterns
Embedding navigation or business logic directly in leaf UI components.
Using fixed dimensions that break on localization or dynamic text.
Ignoring semantics and announcing only visual changes.
Porting XML patterns directly into Compose without adapting the mental model.
Examples
Happy path
Scenario: Apply a coherent Material 3 theme to the Compose showcase screens.
Command: cd examples/orbittasks-compose && ./gradlew :app:assembleDebug
Edge case
Scenario: Keep XML and Compose surfaces visually aligned during mixed UI migration.
Command: cd examples/orbittasks-xml && ./gradlew :app:assembleDebug
Failure recovery
Scenario: Avoid routing theme-token work into accessibility or generic Compose foundations.
Command: python3 scripts/eval_triggers.py --skill android-material3-design-system
Done Checklist
The implementation path is explicit, minimal, and tied to the right Android surface.
Relevant example commands and benchmark prompts have been exercised or updated.
Handoffs to adjacent skills are documented when the request crosses boundaries.
Official references cover the chosen pattern and the main migration or troubleshooting path.
Official References
https://developer.android.com/develop/ui/compose/designsystems/material3
https://developer.android.com/develop/ui/compose/designsystems/custom
https://developer.android.com/develop/ui/views/theming/themes
https://developer.android.com/guide/practices/ui_guidelines/material-design
Weekly Installs
18
Repository
krutikjain/andr…t-skills
GitHub Stars
5
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass