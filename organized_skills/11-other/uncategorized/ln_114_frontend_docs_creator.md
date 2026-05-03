---
rating: ⭐⭐
title: ln-114-frontend-docs-creator
url: https://skills.sh/levnikolaevich/claude-code-skills/ln-114-frontend-docs-creator
---

# ln-114-frontend-docs-creator

skills/levnikolaevich/claude-code-skills/ln-114-frontend-docs-creator
ln-114-frontend-docs-creator
Installation
$ npx skills add https://github.com/levnikolaevich/claude-code-skills --skill ln-114-frontend-docs-creator
SKILL.md

Paths: File paths (shared/, references/, ../ln-*) are relative to skills repo root. If not found at CWD, locate this SKILL.md directory and go up one level for repo root. If shared/ is missing, fetch files via WebFetch from https://raw.githubusercontent.com/levnikolaevich/claude-code-skills/master/skills/{path}.

Frontend Documentation Creator

Type: L3 Worker

L3 Worker that creates design_guidelines.md. CONDITIONAL - only invoked when project has frontend.

Purpose & Scope
Creates design_guidelines.md (if hasFrontend)
Receives Context Store from ln-110-project-docs-coordinator
WCAG 2.1 Level AA accessibility compliance
Design system documentation
Downstream consumers: design_guidelines.md is loaded by ln-401 (Frontend Guard) and ln-402 (Frontend Review Checks) for runtime design validation against implementation
Never gathers context itself; uses coordinator input
Invocation (who/when)
ln-110-project-docs-coordinator: CONDITIONALLY invoked when:
hasFrontend=true (react, vue, angular, svelte detected)
Never called directly by users
Inputs

From coordinator:

contextStore: Context Store with frontend-specific data
DESIGN_SYSTEM (Material-UI, Ant Design, custom)
COLOR_PALETTE (primary, secondary, accent)
TYPOGRAPHY (font families, sizes, weights)
COMPONENT_LIBRARY (detected components)
targetDir: Project root directory
flags: { hasFrontend }

MANDATORY READ: Load shared/references/docs_quality_contract.md, shared/references/docs_quality_rules.json, and shared/references/markdown_read_protocol.md.

Documents Created (1, conditional)
File	Condition	Questions	Auto-Discovery
docs/project/design_guidelines.md	hasFrontend	Q43-Q45	Low
Workflow
Phase 1: Check Conditions
Parse flags from coordinator
If !hasFrontend: return early with empty result
Phase 2: Create Document
Check if file exists (idempotent)
If exists: skip with log
If not exists:
Copy template
Replace placeholders with Context Store values
Preserve the shared opening contract and standard top sections from the template
Populate design system section
Never leave template markers in published frontend docs
If data is missing: omit the claim or use a concise neutral fallback, but do NOT emit [TBD: ...]
Phase 3: Self-Validate
Check SCOPE tag and metadata markers
Check required top sections (Quick Navigation, Agent Entry, Maintenance)
Validate sections:
Design System (component library)
Typography (font families, sizes)
Colors (hex codes, semantic colors)
Check WCAG 2.1 references
Check docs-quality contract compliance (no forbidden placeholders, no leaked template metadata, valid doc kind/role)
Phase 4: Return Status
{
  "created_files": ["docs/project/design_guidelines.md"],
  "skipped_files": [],
  "quality_inputs": {
    "doc_paths": ["docs/project/design_guidelines.md"],
    "owners": {
      "docs/project/design_guidelines.md": "ln-114-frontend-docs-creator"
    }
  },
  "validation_status": "passed"
}

Critical Notes
Core Rules
Conditional: Skip entirely if no frontend detected
WCAG compliance: Document must reference accessibility standards
Design tokens: Extract from CSS variables, tailwind config, or theme files
Idempotent: Never overwrite existing files
Publishable output: No [TBD: ...], TODO, or leaked template metadata in frontend docs
NO_CODE_EXAMPLES Rule (MANDATORY)

Design guidelines document visual standards, NOT code:

FORBIDDEN: CSS code blocks, component implementations
ALLOWED: Tables (colors, typography), design tokens, Figma links
INSTEAD OF CODE: "See Component Library" or "See src/components/Button.tsx"
Stack Adaptation Rule (MANDATORY)
Link to correct component library docs (MUI for React, Vuetify for Vue)
Reference framework-specific patterns (React hooks, Vue composition API)
Never mix stack references (no React examples in Vue project)
Format Priority (MANDATORY)

Tables (colors, typography, spacing) > Lists (component inventory) > Text

Runtime Summary Artifact

MANDATORY READ: Load shared/references/docs_generation_summary_contract.md

Accept optional summaryArtifactPath.

Summary kind:

docs-generation

Required payload semantics:

worker = "ln-114"
status
created_files
skipped_files
quality_inputs
validation_status
warnings

Write the summary to the provided artifact path or return the same envelope in structured output.

Definition of Done
 Condition checked (hasFrontend)
 Document created if applicable
 Design system, typography, colors documented
 WCAG references included
 Actuality verified: all document facts match current code (paths, functions, APIs, configs exist and are accurate)
 Status returned
Reference Files
Templates: references/templates/design_guidelines_template.md
Questions: references/questions_frontend.md (Q43-Q45)

Version: 1.1.0 Last Updated: 2025-01-12

Weekly Installs
278
Repository
levnikolaevich/…e-skills
GitHub Stars
445
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn