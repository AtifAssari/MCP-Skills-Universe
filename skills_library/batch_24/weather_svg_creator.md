---
title: weather-svg-creator
url: https://skills.sh/shanraisshan/claude-code-best-practice/weather-svg-creator
---

# weather-svg-creator

skills/shanraisshan/claude-code-best-practice/weather-svg-creator
weather-svg-creator
Installation
$ npx skills add https://github.com/shanraisshan/claude-code-best-practice --skill weather-svg-creator
SKILL.md
Weather SVG Creator Skill

Creates a visual SVG weather card for Dubai, UAE and writes the output files.

Task

You will receive a temperature value and unit (Celsius or Fahrenheit) from the calling context. Create an SVG weather card and write both the SVG and a markdown summary.

Instructions
Create SVG — Use the SVG template from reference.md, replacing placeholders with actual values
Write SVG file — Read then write to orchestration-workflow/weather.svg
Write summary — Read then write to orchestration-workflow/output.md using the markdown template from reference.md
Rules
Use the exact temperature value and unit provided — do not re-fetch or modify
The SVG must be self-contained and valid
Both output files go in the orchestration-workflow/ directory
Additional resources
For SVG template, output template, and design specs, see reference.md
For example input/output pairs, see examples.md
Weekly Installs
64
Repository
shanraisshan/cl…practice
GitHub Stars
50.1K
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass