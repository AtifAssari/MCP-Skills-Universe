---
title: qa-testing-mobile
url: https://skills.sh/vasilyu1983/ai-agents-public/qa-testing-mobile
---

# qa-testing-mobile

skills/vasilyu1983/ai-agents-public/qa-testing-mobile
qa-testing-mobile
Installation
$ npx skills add https://github.com/vasilyu1983/ai-agents-public --skill qa-testing-mobile
SKILL.md
QA Mobile Testing

Design and execute reliable, cost-aware mobile testing across iOS and Android (native + cross-platform).

Quick Start
Fill assets/mobile-test-plan.md to define risk, layers, and gates.
Fill assets/device-matrix.md from analytics to pick Tier 1/2/3 coverage.
Use references/framework-comparison.md to choose automation frameworks.
Use references/flake-management.md to set a flake budget, reruns, and quarantine rules.
Scope
Define mobile test strategy across iOS and Android.
Plan device matrix, OS coverage, and risk tiers.
Choose automation frameworks and CI + device lab setup.
Address performance, network/offline, backgrounding, and permissions.
Define pre-release gates, staged rollout, and store readiness checks.
When NOT to Use
Platform-specific iOS test command details -> qa-testing-ios
Platform-specific Android test command details -> qa-testing-android
Inputs
Platforms, supported OS versions, and device targets.
App type (native, cross-platform, hybrid/webview).
Critical user flows and risk areas.
Distribution channels and release cadence.
Existing test tooling, CI, and device lab access (Firebase Test Lab, BrowserStack, AWS Device Farm).
Observability and rollout controls (Crashlytics/Sentry, performance/RUM, feature flags, staged rollout).
Test data strategy (seed/reset, test accounts, environment parity).
Workflow
Define quality risks and SLIs (crash-free, ANR, startup time, key flow success).
Build a device matrix from analytics; keep PR gates emulator/simulator-first.
Choose frameworks (default: XCUITest + Espresso/Compose; add cross-platform only when it reduces total cost).
Build test layers: unit, integration/contract, UI smoke, targeted E2E on real devices.
Add mobile-specific coverage: permissions, background/foreground, deep links, offline/poor network.
Add performance checks (startup, scrolling/jank, memory) and accessibility checks.
Set flake budget, rerun limits, quarantine policy, and failure triage (artifacts + reproducibility).
Define release gates + store readiness; ship via staged rollout with monitoring + rollback.
Outputs
Mobile test strategy and device matrix.
Automation plan and framework selection.
Test case inventory with priorities.
Release readiness checklist.
CI pipeline and reporting plan.
Quality Checks
Keep UI tests focused on critical flows; keep suites small and fast.
Separate device specific bugs from logic regressions.
Track flake rate per test/device; quarantine and fix top offenders.
Verify permissions, notifications, and background behavior.
Prefer stable selectors (accessibility IDs/test tags), not localized text.
Templates
assets/device-matrix.md for OS and device coverage.
assets/mobile-test-plan.md for test scope and automation.
assets/release-readiness-checklist.md for release gates.
Resources
references/framework-comparison.md for choosing between XCUITest, Espresso/Compose, Appium, Detox, Maestro, and Flutter testing.
references/flake-management.md for flake control guidance.
references/device-farm-strategies.md for cloud device farm selection and cost optimization.
references/mobile-performance-testing.md for startup, jank, memory, and battery testing.
references/cross-platform-test-patterns.md for React Native, Flutter, and KMP testing patterns.
data/sources.json for curated documentation and device lab links.
Related Skills
Use qa-testing-ios for iOS specific depth (XCTest, Swift Testing, simctl).
Use qa-testing-android for Android specific depth (Espresso, Compose Testing, UIAutomator).
Use qa-testing-playwright for web and webview testing.
Use software-mobile for mobile architecture guidance.
Fact-Checking
Use web search/web fetch to verify current external facts, versions, pricing, deadlines, regulations, or platform behavior before final answers.
Prefer primary sources; report source links and dates for volatile information.
If web access is unavailable, state the limitation and mark guidance as unverified.
Weekly Installs
170
Repository
vasilyu1983/ai-…s-public
GitHub Stars
59
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass