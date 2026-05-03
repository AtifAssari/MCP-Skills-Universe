---
title: android-gradle-build-logic
url: https://skills.sh/krutikjain/android-agent-skills/android-gradle-build-logic
---

# android-gradle-build-logic

skills/krutikjain/android-agent-skills/android-gradle-build-logic
android-gradle-build-logic
Installation
$ npx skills add https://github.com/krutikjain/android-agent-skills --skill android-gradle-build-logic
SKILL.md
Android Gradle Build Logic
When To Use
Use this skill when the request is about: android gradle plugin setup, fix build logic for android modules, version catalog for android repo.
Primary outcome: Shape Android build logic with Gradle, version catalogs, plugins, convention patterns, and toolchain compatibility.
Handoff skills when the scope expands:
android-modernization-upgrade
android-ci-cd-release-playstore
Workflow
Map the request to the current Android stack, module boundaries, and minimum supported API level.
Inspect the existing implementation for implicit assumptions, duplicate helpers, and outdated patterns.
Apply the smallest change that improves correctness, readability, and long-term maintainability.
Validate the result against the relevant showcase app path and repo benchmarks.
Hand off adjacent work to the next specialized skill only after the core foundation is stable.
Guardrails
Prefer official Android and Kotlin guidance over custom local conventions when they conflict.
Keep public APIs boring and explicit; avoid clever abstractions that hide Android lifecycle costs.
Do not mix architectural cleanup with product behavior changes unless the request explicitly needs both.
Document any compatibility constraints that will affect old modules or generated code.
Anti-Patterns
Sprinkling helpers across modules without a clear ownership boundary.
Introducing framework-specific code into pure domain or data layers.
Refactoring every adjacent file when only one contract needed to change.
Leaving migration notes implied instead of writing them down.
Examples
Happy path
Scenario: Run the Compose showcase build from a clean checkout with version catalogs.
Command: cd examples/orbittasks-compose && ./gradlew :app:assembleDebug
Edge case
Scenario: Validate shared repositories and plugin management in the XML fixture.
Command: cd examples/orbittasks-xml && ./gradlew :app:assembleDebug
Failure recovery
Scenario: Benchmark build-logic trigger precision against modernization and CI skills.
Command: python3 scripts/eval_triggers.py --skill android-gradle-build-logic
Done Checklist
The implementation path is explicit, minimal, and tied to the right Android surface.
Relevant example commands and benchmark prompts have been exercised or updated.
Handoffs to adjacent skills are documented when the request crosses boundaries.
Official references cover the chosen pattern and the main migration or troubleshooting path.
Official References
https://developer.android.com/build
https://developer.android.com/build/releases/gradle-plugin
https://developer.android.com/build/migrate-to-built-in-kotlin
https://docs.gradle.org/current/userguide/userguide.html
Weekly Installs
181
Repository
krutikjain/andr…t-skills
GitHub Stars
5
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass