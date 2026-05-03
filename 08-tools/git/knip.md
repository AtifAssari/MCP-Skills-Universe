---
title: knip
url: https://skills.sh/knoopx/pi/knip
---

# knip

skills/knoopx/pi/knip
knip
Installation
$ npx skills add https://github.com/knoopx/pi --skill knip
SKILL.md
Knip

Finds unused files, dependencies, and exports in TypeScript/JavaScript projects.

Usage
bunx knip                     # Analyze project
bunx knip --production        # Production only (no tests, devDeps)
bunx knip --strict            # Direct dependencies only
bunx knip --fix               # Auto-remove unused (use cautiously)
bunx knip --include files     # Only unused files
bunx knip --include exports   # Only unused exports
bunx knip --include dependencies  # Only unused deps

Output Formats
bunx knip --reporter compact  # Compact output
bunx knip --reporter json     # JSON for tooling
bunx knip --reporter github-actions  # CI annotations

Filtering
bunx knip --workspace packages/client  # Specific workspace
bunx knip --exclude "test/**/*"        # Exclude patterns

Debugging
bunx knip --debug                      # Debug output
bunx knip --trace-file src/utils.ts    # Trace file
bunx knip --trace-export myFunction    # Trace export

Configuration

Configure via .knip.json or knip.config.js for custom entry points and exclusions.

Related Skills
maintenance: Refactoring and technical debt management
jscpd: Find duplicate code blocks
bun: Package management for JS/TS projects
Weekly Installs
29
Repository
knoopx/pi
GitHub Stars
45
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass