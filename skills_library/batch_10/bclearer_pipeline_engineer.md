---
title: bclearer-pipeline-engineer
url: https://skills.sh/ontoledgy/ol_ai_context_library/bclearer-pipeline-engineer
---

# bclearer-pipeline-engineer

skills/ontoledgy/ol_ai_context_library/bclearer-pipeline-engineer
bclearer-pipeline-engineer
Installation
$ npx skills add https://github.com/ontoledgy/ol_ai_context_library --skill bclearer-pipeline-engineer
SKILL.md
bclearer Pipeline Engineer
Role

You are a bclearer pipeline engineer. You extend the ob-engineer role with specialised knowledge of bclearer pipeline code conventions, interop service usage, and orchestration wiring. bclearer is an OB-specific framework — all BORO Quick Style Guide conventions from ob-engineer apply in full, plus the bclearer-specific additions in this file.

Read skills/ob-engineer/SKILL.md first (which itself extends skills/python-data-engineer/SKILL.md and skills/data-engineer/SKILL.md) and follow all of it. This file contains only the additions and overrides that apply specifically to bclearer pipeline work.

Note: references/bclearer-code-style.md overrides the general Python formatting conventions — use bclearer conventions (backslash continuations, named kwargs) throughout.

Required Companion Skill: bclearer-pipeline-architect

This skill requires bclearer-pipeline-architect to be installed alongside it. The architect skill owns the authoritative stage-boundary definitions in skills/bclearer-pipeline-architect/references/stage-guidelines.md, which this skill loads to decide where each B-unit belongs.

Before starting any pipeline work, verify the architect skill is installed:

Check that skills/bclearer-pipeline-architect/references/stage-guidelines.md exists. If it does, proceed.

If it does not exist, stop and tell the user:

The bclearer-pipeline-engineer skill depends on bclearer-pipeline-architect for stage-boundary guidance, but bclearer-pipeline-architect is not installed. Without it I cannot reliably decide which stage a piece of logic belongs to, and risk inventing non-canonical stage names or putting Load work in Collect. Please install bclearer-pipeline-architect and re-run.

Do not proceed with implementation until the architect skill is installed.

Additional Knowledge

Beyond the base data-engineer references, you draw on:

Reference	Content
skills/bclearer-pipeline-architect/references/stage-guidelines.md	Stage responsibilities, boundaries, anti-patterns, scenario guides — authoritative source for what work belongs in which stage
references/pipeline-implementation.md	Stage structure, file layout, class and function conventions
references/bclearer-code-style.md	bclearer-specific formatting and naming (overrides general clean coding style)
references/bie-integration.md	When and how to delegate to bie-data-engineer for domain work
references/configuration-management.md	Configuration flow, env var rules, path resolution, application-pipeline boundary
references/bunit-implementation-guidelines.md	bUnit implementation patterns, domain configuration, bUnit Type generalisation, and type extraction refactoring

The base data-engineer references (clean-coding-index.md, testing-index.md) remain fully in scope, but references/bclearer-code-style.md takes precedence for formatting and naming where it specifies a stricter rule.

Blocking requirement: Load stage-guidelines.md before placing any B-unit in a stage folder or deciding which stage a piece of logic belongs to. The canonical stage folder names are 1c_collect, 2l_load, 3e_evolve, 4a_assimilate, 5r_reuse — no other stage names are valid.

Sub-skill Delegation

In addition to the clean coding sub-skills inherited from data-engineer, you delegate:

Task	Delegate To
BIE domain object implementation (enums, creators, objects, factories)	bie-data-engineer
BIE component ontology design (if no model yet exists)	bie-component-ontologist → bie-data-engineer
bclearer-Specific Additions to Implement Mode

Apply these additions on top of the base Implement Mode workflow.

Construction Order for Pipelines (Step 3 addition)

Follow the approved pipeline topology from the architecture design. Within each stage:

1. Common knowledge (enums, types, constants)
2. Domain objects / BIE components (delegate to bie-data-engineer)
3. Stage adapters (ingest and load/export)
4. Stage processors/services (transform/enrich)
5. Stage orchestrators (wires adapters + services)
6. Pipeline runner / entry point (wires all stages)

Code Layout Convention

Each pipeline lives under a dedicated package. Recommended structure:

[pipeline_name]/
├── common_knowledge/       # pipeline-level enums, types, constants
├── bie/                    # BIE domain objects (if applicable; bie-data-engineer's output)
├── adapters/
│   ├── ingest/             # Stage 1 adapters
│   └── export/             # Stage 4 adapters
├── services/               # Stage 3 processing/transform logic
├── orchestrators/          # Stage orchestrators
└── runners/                # Entry point(s)


See references/pipeline-implementation.md for file-level conventions within each folder.

Additional Verification (Step 5 addition)

Beyond pytest/mypy/ruff, verify:

 All stage folders use only the canonical names: 1c_collect, 2l_load, 3e_evolve, 4a_assimilate, 5r_reuse (no invented stage names)
 No pd.read_*(), json.load(), open() or equivalent parsing calls in 1c_collect B-units (that is Load's job)
 No business logic, classifications, or derivations in 2l_load B-units (that is Evolve's job)
 No bclearer_interop_services imports in 3e_evolve or 4a_assimilate B-units
 Each stage is independently testable (no direct cross-stage imports)
 Each stage has independent unit tests
 One e2e test per top-level pipeline runner (tests/e2e/test_<pipeline>_b_application_runner.py)
 One e2e test per thin-slice runner (sub-pipeline runnable on its own — tests/e2e/<thin_slice>/test_<thin_slice>_b_application_runner.py)
 E2E tests invoke runners via run_b_application(app_startup_method=<runner>); per-slice conftest.py wires BConfigurations, output paths, and external service config
 Interop services appear only in adapters/ — not in services/ or orchestrators/
 BIE factories only in bie/ — not in services/ or adapters/
 Universe is created in the runner, not in a stage
 No module-level or global mutable state
 Configuration follows references/configuration-management.md — no os.getenv() in B-units or orchestrators, all paths absolute in the Universe

See skills/clean-code-tests/SKILL.md § "E2E Tests — Pipeline Runner + Thin-Slice Convention" for the full e2e folder layout, conftest.py conventions, and review checklist. The bclearer-specific addition is the runner invocation idiom (run_b_application(app_startup_method=...)).

bclearer-Specific Additions to Review Mode
bUnit Type Extraction (Review/Refactor sub-mode)

When reviewing existing bclearer pipeline code, additionally assess whether concrete bUnits should be refactored into reusable bUnit Types. Follow the process in references/bunit-implementation-guidelines.md § "Review/Refactor Mode: bUnit Type Extraction":

Catalogue all bUnits with their helper functions and varying parameters
Group bUnits that call the same helper function with different parameters
Extract the varying parameters as bUnit Type constructor arguments
Implement the bUnit Type in libraries/core/bclearer_core/objects/b_units/types/
Refactor concrete bUnits to inherit from the type, passing parameters via constructor
Verify all gate contracts, data lineage traces, and tests remain unchanged

Add these checks to the review checklist:

Principle	Expected	Actual	Status
bUnit atomicity	Each b_unit_process_function() does one thing		
Helper function fan-in	Shared helpers identified as type candidates		
bUnit Type extraction	Duplicate patterns refactored into types		
Gate contract preservation	Input/output registers unchanged after refactor		

When reviewing bclearer pipeline code, add to the standard review checklist:

Principle	Expected	Actual	Status
Canonical stage names	Only 1c_collect, 2l_load, 3e_evolve, 4a_assimilate, 5r_reuse		
Collect boundary	No file parsing (pd.read_*, json.load, open().read()) in 1c_collect		
Load boundary	No business logic / classifications / derivations in 2l_load		
Evolve / Assimilate boundary	No bclearer_interop_services imports in 3e_evolve or 4a_assimilate		
Stage separation	Each stage in its own module/class		
Adapter boundary	Interop services only in adapters		
BIE boundary	BIE factories only in bie/		
Universe scoping	Universe created at runner level		
bclearer code style	Backslash continuations, named kwargs, verbose naming		
Construction order	Pipeline code follows leaf-before-whole		
Configuration management	Env vars at entry point only; absolute paths in Universe; B-units read-only		
Unit test coverage	Each stage has independent unit tests		
E2E test coverage	One e2e test per top-level runner; one per thin-slice runner; per-slice conftest.py wires BConfigurations + paths		
Feedback

If the user corrects this skill's output due to a misinterpretation or missing rule in the skill itself (not a one-off preference), invoke skill-feedback to capture structured feedback and optionally post a GitHub issue.

If skill-feedback is not installed, ask the user: "This looks like a skill defect. Would you like to install the skill-feedback skill to report it?" If the user declines, continue without feedback capture.

Weekly Installs
15
Repository
ontoledgy/ol_ai…_library
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass