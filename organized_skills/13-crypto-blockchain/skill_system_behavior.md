---
rating: ⭐⭐
title: skill-system-behavior
url: https://skills.sh/arthur0824hao/skills/skill-system-behavior
---

# skill-system-behavior

skills/arthur0824hao/skills/skill-system-behavior
skill-system-behavior
Installation
$ npx skills add https://github.com/arthur0824hao/skills --skill skill-system-behavior
SKILL.md
Skill System Behavior — Spec Engine

Define what a skill does before writing how. This skill enforces a BDD-style workflow:

SKILL.spec.yaml  →  Acceptance Tests  →  Implementation  →  SKILL.behavior.yaml (generated)
     (WHAT)           (VERIFY)              (HOW)              (DOCUMENT)

Spec Format

Every skill's behavior is defined in SKILL.spec.yaml:

schema_version: 1
skill_name: my-skill
description: "What this skill does"

operations:
  - name: do-something
    intent: "Why this operation exists"
    inputs: [...]
    outputs: [...]
    constraints: ["Must not...", "Must always..."]
    expected_effects: [...]

acceptance_tests:
  structural:
    - id: manifest-valid
      assert: "manifest exposes all operations"
  behavioral:
    - id: happy-path
      given: "Valid input"
      when: "do-something is called"
      then: "Returns expected output"


Full schema: schema/spec-v1.yaml

For v2 behavior specs (*.behavior.yaml), you can also include an optional interaction_diagram Mermaid block to describe cross-node interactions.

interaction_diagram: |
  flowchart LR
    Script["runtime-doctor"] -->|"reads"| Config["config/memory.yaml"]

Operations
create-spec

Scaffold a new SKILL.spec.yaml from the schema template.

Read schema/spec-v1.yaml for the format
Ask user for: skill name, description, operations (name + intent + inputs/outputs)
Generate SKILL.spec.yaml in the target skill directory
Include placeholder acceptance tests (structural defaults + behavioral stubs)
validate-spec

Validate a SKILL.spec.yaml against the v1 schema.

Read the target SKILL.spec.yaml
Check required fields: schema_version, skill_name, description, operations
For each operation: verify name, intent, at least one input or output, constraints present
For acceptance_tests: verify structural tests include manifest-valid and scripts-exist
Report: PASS with summary, or FAIL with specific violations

Run via: python3 scripts/validate_spec.py <path-to-SKILL.spec.yaml>

verify-structural

Run structural acceptance tests against a built skill.

Read the skill's SKILL.spec.yaml for declared operations
Read the skill's SKILL.md for the skill-manifest block
Verify:
Every operation in spec has a matching operation in manifest
Every entrypoint script referenced in manifest exists on disk
skills-index.json includes this skill's capabilities
Report: checklist with PASS/FAIL per test
generate-contract

Generate a SKILL.behavior.yaml (Mermaid DAG) from a completed spec + implementation.

Read SKILL.spec.yaml for operations, inputs, outputs, constraints
Map operations → stages in a flowchart
Map inputs → input nodes, outputs → output nodes
Map constraints → error paths
Write SKILL.behavior.yaml with embedded Mermaid diagram

This is the last step — only run after implementation is complete and tests pass.

Coverage Gate

Scan a project tree for scripts/modules that are missing behavior specs.

Scan project_dir for scripts that match the configured patterns
Scan for *.behavior.yaml files in the same tree
Report covered/uncovered scripts using exact-name and SKILL convention matching
Emit a human-readable summary and last-line JSON report

Run via: python3 scripts/coverage_gate.py <project_dir> [--patterns ...] [--exclude ...]

Use this before declaring "behavior coverage is complete."

Workflow Integration
For skill-system-creator (updated flow)
1. Understand the skill (examples, triggers)
2. Create spec         → skill-system-behavior:create-spec
3. Validate spec       → skill-system-behavior:validate-spec
4. Write tests         → define acceptance criteria from spec
5. Initialize skill    → skill-system-creator:init
6. Implement skill     → edit SKILL.md, scripts, references
7. Verify structural   → skill-system-behavior:verify-structural
8. Generate contract   → skill-system-behavior:generate-contract
9. Package             → skill-system-creator:package

Spec as Single Source of Truth
SKILL.spec.yaml — the authoritative definition (human-written, reviewed)
SKILL.md + manifest — implementation (must conform to spec)
SKILL.behavior.yaml — generated documentation (derived from spec)
Governance Tiers

Use this 3-tier hierarchy as guidance for organizing cross-file governance docs:

Tier 1 — System Architecture
  ├── SYSTEM_ARCHITECTURE.md    (system boundaries + data flow)
  └── PIPELINE_DAG.md           (zoom-in companion, state machines)

Tier 2 — Behavior Contracts
  ├── *.behavior.yaml           (single-script: inputs/outputs/stages/error_paths)
  └── BEHAVIOR_RUNTIME.md       (strictly cross-script scenarios only)

Tier 3 — Tests
  └── test_*.py                 (each test traces to a specific behavior scenario)


For Tier 2 → Tier 3 traceability, use acceptance_tests.behavioral[].tested_by in SKILL.spec.yaml to point to validating tests.

For cross-tier references, use optional governance.tier and governance.traces_to in SKILL.spec.yaml to declare where a spec sits and what higher/lower artifacts it traces to.

Cross-File Boundary Rules
*.behavior.yaml defines single-script behavior only (inputs, outputs, stages, error paths for one script).
BEHAVIOR_RUNTIME.md is for cross-script scenarios only (2+ scripts interacting).
If a scenario involves only one script, place it in that script's .behavior.yaml, not in BEHAVIOR_RUNTIME.md.
When extending to new phases, avoid full-copy duplication; use references/overlay patterns so shared flows stay canonical.
Guidelines
Write specs in the language your team uses (English, Chinese, mixed — consistency within a spec)
Constraints are invariants: if violated, the skill has a bug
intent describes WHY, not HOW — implementation details go in SKILL.md
Acceptance tests use Given/When/Then for behavioral, assert-statements for structural
Generate contracts only after all tests pass — contracts are docs, not specs
{
  "schema_version": "2.0",
  "id": "skill-system-behavior",
  "version": "2.0.0",
  "capabilities": ["spec-create", "spec-validate", "spec-verify", "contract-generate", "coverage-gate", "skill-graph-build"],
  "effects": ["fs.read", "fs.write", "proc.exec"],
  "operations": {
    "create-spec": {
      "description": "Scaffold a new SKILL.spec.yaml from the schema template.",
      "input": {
        "skill_name": { "type": "string", "required": true, "description": "Name of the skill to spec" },
        "skill_dir": { "type": "string", "required": false, "description": "Target directory (default: skills/<skill_name>)" }
      },
      "output": {
        "description": "Path to created SKILL.spec.yaml",
        "fields": { "path": "string" }
      },
      "entrypoints": {
        "agent": "Read schema/spec-v1.yaml, then scaffold SKILL.spec.yaml in skill_dir"
      }
    },
    "validate-spec": {
      "description": "Validate a SKILL.spec.yaml against the v1 schema.",
      "input": {
        "spec_path": { "type": "string", "required": true, "description": "Path to SKILL.spec.yaml" }
      },
      "output": {
        "description": "Validation result with pass/fail and violations list",
        "fields": { "status": "string", "violations": "array" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/validate_spec.py", "{spec_path}"],
        "windows": ["python", "scripts/validate_spec.py", "{spec_path}"]
      }
    },
    "verify-structural": {
      "description": "Run structural acceptance tests against a built skill or general behavior spec.",
      "input": {
        "skill_dir": { "type": "string", "required": true, "description": "Path to skill directory or direct spec path" }
      },
      "output": {
        "description": "Test results checklist",
        "fields": { "status": "string", "results": "array" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/verify_structural.py", "{skill_dir}"],
        "windows": ["python", "scripts/verify_structural.py", "{skill_dir}"]
      }
    },
    "generate-contract": {
      "description": "Generate behavior contract Mermaid DAGs from completed skill or project specs.",
      "input": {
        "skill_dir": { "type": "string", "required": true, "description": "Path to skill directory or direct spec path" }
      },
      "output": {
        "description": "Path to generated SKILL.behavior.yaml",
        "fields": { "path": "string" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/generate_contract.py", "{skill_dir}"],
        "windows": ["python", "scripts/generate_contract.py", "{skill_dir}"]
      }
    },
    "coverage-gate": {
      "description": "Scan project for scripts/modules missing behavior specs.",
      "input": {
        "project_dir": { "type": "string", "required": true, "description": "Root directory to scan" },
        "patterns": { "type": "string", "required": false, "description": "Comma-separated glob patterns (default: **/*.py,**/*.sh)" },
        "exclude": { "type": "string", "required": false, "description": "Patterns to exclude (default: test_*,__pycache__,.*)" }
      },
      "output": {
        "description": "Coverage report with covered/uncovered lists and percentage",
        "fields": { "covered": "array", "uncovered": "array", "coverage_pct": "number" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/coverage_gate.py", "{project_dir}"],
        "windows": ["python", "scripts/coverage_gate.py", "{project_dir}"]
      }
    },
    "build-graph": {
      "description": "Build a project behavior graph from discovered spec files.",
      "input": {
        "skills_dir": { "type": "string", "required": false, "description": "Root directory to scan using config/spec_discovery.yaml patterns" },
        "output_format": { "type": "string", "required": false, "description": "mermaid, json, or sql" }
      },
      "output": {
        "description": "Graph output in the requested format",
        "fields": { "graph": "string|json" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/build_graph.py", "--skills-dir", "{skills_dir}", "--format", "{output_format}"]
      }
    },
    "refresh-projections": {
      "description": "Refresh behavior projection bundles from SKILL.spec.yaml files for behavior_* tables.",
      "input": {
        "skills_dir": { "type": "string", "required": false, "description": "Root directory to scan (default: ./skills)" },
        "output_format": { "type": "string", "required": false, "description": "json or sql" }
      },
      "output": {
        "description": "Projection bundle or SQL statements for behavior_* refresh",
        "fields": { "bundle": "json|string" }
      },
      "entrypoints": {
        "unix": ["python3", "scripts/refresh_behavior_projections.py", "--skills-dir", "{skills_dir}", "--format", "{output_format}"]
      }
    }
  },
  "stdout_contract": {
    "last_line_json": true
  }
}

Weekly Installs
51
Repository
arthur0824hao/skills
GitHub Stars
4
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass