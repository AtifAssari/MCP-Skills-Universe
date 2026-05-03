---
rating: ⭐⭐
title: opentelemetry-sdk-versions
url: https://skills.sh/niwoerner/opentelemetry-agent-skills/opentelemetry-sdk-versions
---

# opentelemetry-sdk-versions

skills/niwoerner/opentelemetry-agent-skills/opentelemetry-sdk-versions
opentelemetry-sdk-versions
Installation
$ npx skills add https://github.com/niwoerner/opentelemetry-agent-skills --skill opentelemetry-sdk-versions
SKILL.md
OpenTelemetry SDK Versions

Use this skill when you need the latest released OpenTelemetry SDK or package version for a language.

If the broader task is manual instrumentation design or review, pair this with opentelemetry-manual-instrumentation. If the task involves SDK initialization or configuration, pair this with opentelemetry-sdk-setup.

Workflow
Open references/generated/otel-version-index.md.
identify the row for the project language and package
use the bundled table as the default source of truth for supported languages in this repository
Choose the version deliberately.
prefer the latest released version when it is compatible with the project
if the latest release is not compatible, choose the latest compatible version and state the compatibility reason explicitly
reuse that decision for the rest of the task unless the language, package, or constraints change
Resolve companion packages from the release source.
the index covers one primary SDK package per language
if the task requires additional packages from the same ecosystem (exporters, instrumentations, resource detectors), look up their versions from the release source — do not infer or reuse the primary package version
sub-packages within the same project often share a version line but not always; confirm each package individually
Use the linked follow-up sources when needed.
use the Release Source column to confirm the package or repo
use the Setup Docs column for SDK setup guidance
use the Examples column for implementation references when examples are available
Handle gaps explicitly.
if the requested language or package is not in the bundled index, say that the index does not cover that exact package
then fall back to the official release source and official docs for that package
do not assume an unreleased, prerelease, or incompatible version is acceptable without saying so
Weekly Installs
8
Repository
niwoerner/opent…t-skills
GitHub Stars
7
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn