---
title: paw-ps-research-to-brief
url: https://skills.sh/pawbytes/skill-suites/paw-ps-research-to-brief
---

# paw-ps-research-to-brief

skills/pawbytes/skill-suites/paw-ps-research-to-brief
paw-ps-research-to-brief
Installation
$ npx skills add https://github.com/pawbytes/skill-suites --skill paw-ps-research-to-brief
SKILL.md
Research to Brief
Overview

A deterministic workflow that converts validated research outputs into a clean, structured product brief. This pipeline ensures no evidence or uncertainty is lost during synthesis.

Args: Accepts --headless / -H for non-interactive execution.

Output: Product brief document with preserved signals (evidence and uncertainties).

Pipeline
Stage 1: Gather Inputs

Load ./references/01-gather-inputs.md

Collect all relevant research files from the product workspace:

Discovery outputs (product-context.md)
Market intelligence (market-intelligence.md)
Audience intelligence (audience-intelligence.md)

Progression: Proceed when at least one input source is located.

Stage 2: Validate Completeness

Load ./references/02-validate-completeness.md

Assess whether inputs meet minimum thresholds for brief synthesis. Identify gaps and either proceed with available data or flag for additional research.

Progression: Proceed when minimum input requirements are met OR explicit decision to proceed with gaps documented.

Stage 3: Synthesize Brief

Load ./references/03-synthesize-brief.md

Create the structured product brief by consolidating validated inputs into a single document. Apply consistent formatting and ensure traceability to source materials.

Progression: Proceed when brief structure is complete with all required sections populated.

Stage 4: Preserve Signals

Load ./references/04-preserve-signals.md

Document key evidence sources and unresolved uncertainties. Create signal preservation notes that trace decisions back to research findings.

Progression: Complete when all signals are documented and appended to the brief or decision log.

On Activation
Determine the product workspace root: {project-root}/.pawbytes/prodig-suites/
Identify active product context from .pawbytes/prodig-suites/active-product.md if it exists
If no active product is set and not in headless mode, prompt user to specify product slug
Begin pipeline at Stage 1
Input Sources
Source	File Path	Required
Discovery	.pawbytes/prodig-suites/products/{product-slug}/product-context.md	Preferred
Market Research	.pawbytes/prodig-suites/products/{product-slug}/market-intelligence.md	Preferred
Audience Research	.pawbytes/prodig-suites/products/{product-slug}/audience-intelligence.md	Preferred

Minimum Requirement: At least one of the three input sources must be available.

Output Structure
.pawbytes/prodig-suites/products/{product-slug}/
├── product-brief.md              # Main brief document
├── signal-notes.md               # Evidence and uncertainty log
└── product-decisions.md          # Appended brief metadata (if exists)

Output Contract

Every execution delivers:

Action type: Brief synthesis from research inputs
Files saved:
product-brief.md — Structured product brief
signal-notes.md — Evidence and uncertainty preservation
Recommendations: Next steps (e.g., validate with stakeholders, initiate design phase)
File saved to: .pawbytes/prodig-suites/products/{product-slug}/
Headless Mode

When invoked with --headless or -H:

Attempt to read active product from .pawbytes/prodig-suites/active-product.md
If not found, scan for most recently modified product workspace
Execute all stages without prompts
Document any gaps or assumptions in signal notes
Exit with status code 0 on success, 1 if minimum inputs not met
Quality Gates
Stage	Gate Condition
Gather Inputs	At least 1 input file located
Validate Completeness	Minimum input threshold met OR documented decision to proceed
Synthesize Brief	All required brief sections populated
Preserve Signals	All evidence and uncertainties documented
Weekly Installs
19
Repository
pawbytes/skill-suites
GitHub Stars
25
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass