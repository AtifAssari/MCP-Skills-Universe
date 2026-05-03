---
title: context-map
url: https://skills.sh/github/awesome-copilot/context-map
---

# context-map

skills/github/awesome-copilot/context-map
context-map
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill context-map
Summary

Analyze codebases and map task-relevant files before implementing changes.

Automatically searches for related files, dependencies, tests, and similar code patterns to establish full context
Generates structured markdown output with files to modify, dependency relationships, test coverage, and reference patterns
Includes risk assessment checklist for breaking changes, migrations, and configuration updates
Designed as a pre-implementation step to prevent missed dependencies and unintended side effects
SKILL.md
Context Map

Before implementing any changes, analyze the codebase and create a context map.

Task

{{task_description}}

Instructions
Search the codebase for files related to this task
Identify direct dependencies (imports/exports)
Find related tests
Look for similar patterns in existing code
Output Format
## Context Map

### Files to Modify
| File | Purpose | Changes Needed |
|------|---------|----------------|
| path/to/file | description | what changes |

### Dependencies (may need updates)
| File | Relationship |
|------|--------------|
| path/to/dep | imports X from modified file |

### Test Files
| Test | Coverage |
|------|----------|
| path/to/test | tests affected functionality |

### Reference Patterns
| File | Pattern |
|------|---------|
| path/to/similar | example to follow |

### Risk Assessment
- [ ] Breaking changes to public API
- [ ] Database migrations needed
- [ ] Configuration changes required


Do not proceed with implementation until this map is reviewed.

Weekly Installs
8.8K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass