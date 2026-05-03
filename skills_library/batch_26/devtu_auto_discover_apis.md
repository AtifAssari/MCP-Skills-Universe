---
title: devtu-auto-discover-apis
url: https://skills.sh/mims-harvard/tooluniverse/devtu-auto-discover-apis
---

# devtu-auto-discover-apis

skills/mims-harvard/tooluniverse/devtu-auto-discover-apis
devtu-auto-discover-apis
Installation
$ npx skills add https://github.com/mims-harvard/tooluniverse --skill devtu-auto-discover-apis
SKILL.md
Automated Life Science API Discovery & Tool Creation

Discover, create, validate, and integrate life science APIs into ToolUniverse.

Four-Phase Workflow
Gap Analysis → API Discovery → Tool Creation → Validation → Integration
     ↓              ↓               ↓              ↓            ↓
  Coverage      Web Search      devtu-create   devtu-fix    Git PR


Human approval gates after: discovery, creation, validation, and before PR.

Phase 1: Discovery & Gap Analysis
1.1 Analyze Current Coverage

Load ToolUniverse, categorize tools by domain (genomics, proteomics, drug discovery, clinical, omics, imaging, literature, pathways, systems biology). Count per category.

1.2 Identify Gap Domains
Critical Gap: <5 tools in category
Moderate Gap: 5-15 tools, missing key subcategories
Emerging Gap: New technologies not represented

Common gaps: single-cell genomics, metabolomics, patient registries, microbial genomics, multi-omics integration, synthetic biology, toxicology.

1.3 Web Search for APIs

For each gap domain, run multiple queries:

"[domain] API REST JSON" — direct API search
"[domain] public database" — database discovery
"[domain] API 2025 OR 2026" — recent releases
"[domain] database" site:nar.oxfordjournals.org — NAR Database Issue

Extract: base URL, endpoints, auth method, parameter schemas, rate limits.

1.4 Score and Prioritize
Criterion	Max Points
Documentation Quality	20
API Stability	15
Authentication Simplicity	15
Coverage	15
Maintenance	10
Community	10
License	10
Rate Limits	5

High priority (>=70), Medium (50-69), Low (<50).

1.5 Generate Discovery Report

Coverage analysis, prioritized candidates with scores, implementation roadmap.

Phase 2: Tool Creation

For each API, use Skill(skill="devtu-create-tool") or follow these patterns.

Architecture Decision
Multiple endpoints → multi-operation tool (single class, multiple JSON wrappers)
Single endpoint → single-operation acceptable
Key Steps
Design tool class following template — see references/tool-templates.md
Create JSON config with oneOf return_schema
Find real test examples (use List endpoint → extract IDs → verify)
Register in default_config.py
Critical Requirements
return_schema MUST have oneOf (success + error schemas)
test_examples MUST use real IDs (NO placeholders)
Tool name <= 55 characters
NEVER raise exceptions in run() — return error dict
Set timeout on all HTTP requests (30s)
Phase 3: Validation

Full guide: references/validation-guide.md

Quick Validation Checklist
Schema: oneOf structure, data wrapper, error field
Placeholders: No TEST/DUMMY/PLACEHOLDER in test_examples
Loading: 3-step check (class registered, config registered, wrappers generated)
Integration tests: python scripts/test_new_tools.py [api_name] -v → 100% pass

Fix failures with Skill(skill="devtu-fix-tool").

Phase 4: Integration

Use Skill(skill="devtu-github") or:

Create branch: feature/add-[api-name]-tools
Stage tool files + default_config.py
Commit with descriptive message
Push and create PR with validation results
Processing Patterns
Pattern	When to Use
Batch (multiple APIs → single PR)	Same domain, similar structure
Iterative (one API at a time)	Complex auth, novel patterns
Discovery-only (report, no tools)	Planning roadmap
Validation-only (audit existing)	PR review, quality check
References
Tool templates (Python class + JSON config): references/tool-templates.md
Validation & integration guide: references/validation-guide.md
Weekly Installs
208
Repository
mims-harvard/to…universe
GitHub Stars
1.3K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn