---
rating: ⭐⭐⭐⭐⭐
title: readme-expert
url: https://skills.sh/rfxlamia/claude-skillkit/readme-expert
---

# readme-expert

skills/rfxlamia/claude-skillkit/readme-expert
readme-expert
Installation
$ npx skills add https://github.com/rfxlamia/claude-skillkit --skill readme-expert
SKILL.md
KEY FEATURES:
Codebase scanning for accurate facts
5-layer anti-hallucination validation
Script execution testing
Citation tracking for all claims
Template-based structure selection
DIFFERENTIATOR: Every claim verified against actual codebase. No assumptions, no hallucinations. Script execution testing ensures examples work.
README Expert

Create comprehensive README.md files grounded in codebase reality.

Overview

README Expert uses validation-first methodology to generate accurate, comprehensive README files by:

Scanning actual codebase - Extract facts from real files (no assumptions)
Verifying every claim - 5-layer validation ensures accuracy
Testing all scripts - Execute commands/examples to ensure they work
Tracking citations - Every statement traceable to source files
Quality standards - Follows standard-readme and Google style guides

Anti-Hallucination Core: Research shows AI README hallucinations occur in 3-27% of outputs. This skill reduces that to near-zero through systematic verification.

Workflow Decision Tree

Choose workflow based on task:

┌─────────────────────────────────────┐
│   What is your README task?         │
└───────────┬─────────────────────────┘
            │
    ┌───────┴───────┐
    │               │
    ▼               ▼
┌─────────┐   ┌──────────┐
│ CREATE  │   │ VALIDATE │
│   NEW   │   │ EXISTING │
└────┬────┘   └────┬─────┘
     │             │
     ▼             ▼
  Section 1     Section 2
  (Full Flow)  (Validation Only)


Decision Criteria:

Scenario	Route	Sections Used
No README exists	CREATE NEW	1 (Full Workflow)
README exists but incomplete	CREATE NEW	1 (Full Workflow)
README exists, check accuracy	VALIDATE	2 (Validation Only)
Update sections of README	CREATE NEW	1 (Partial execution)
Verify scripts still work	VALIDATE	2 (Focus Layer 3)
Section 1: Full README Creation Workflow

Use when: Creating new README or major overhaul.

Time: 3-5 minutes with automation Output: Complete, validated README.md Quality Target: 95%+ accuracy, 0 hallucinations

Phase 1: Codebase Scanning (2 min)

Goal: Extract accurate project facts from actual files.

Load Knowledge: knowledge/foundation/codebase-scanner.md

Steps:

Detect Project Type

# Find config files
Glob: pattern="{package.json,pyproject.toml,Cargo.toml,go.mod}"
# Read detected file
Read: file_path="<detected_config>"


Extract Metadata

Project name, version, description (exact quotes)
Dependencies (actual, not assumed)
Entry points / CLI commands
Author, license, repo URL

Scan Structure

# Find source directories
Glob: pattern="src/**/*.{py,js,ts,go,rs}"
Glob: pattern="lib/**/*.{py,js,ts}"
# Find tests
Glob: pattern="{tests,test,__tests__}/**/*"
# Find docs
Glob: pattern="docs/**/*.md"


Discover Features

# Find public API
Grep: pattern="^(export|class|def)\s+\w+" output_mode="content"
# Find CLI commands
Grep: pattern="(scripts|entry_points|bin)" path="<config_file>"
# Find environment variables
Grep: pattern="(process\.env|os\.environ|os\.Getenv)"


Output: Verified project facts with source citations.

Anti-Hallucination Check: Every fact must have source file reference.

Phase 2: Template Selection (30 sec)

Goal: Choose appropriate README structure.

Load Knowledge: knowledge/application/template-library.md

Templates by Project Type:

Project Type	Template	Key Sections
Library/Package	standard-readme	Title, Install, Usage, API, License
CLI Tool	CLI-focused	Title, Install, Commands, Examples, Config
Web App	App-focused	Title, Features, Deploy, Config, Develop
Framework	Framework	Title, Quick Start, Concepts, API, Extend
API Service	API-focused	Title, Endpoints, Auth, Examples, Deploy

Selection Criteria:

Check package.json "bin" field → CLI template
Check pyproject.toml [project.scripts] → CLI template
Check "dependencies" with "express|fastify|flask" → API template
Check "src/components" or "react|vue|svelte" → Web App template
Default: Library template

Output: Selected template structure.

Phase 3: README Generation (1 min)

Goal: Write README sections with verified content.

Standard Structure:

Title & Badges

# {project_name}

> {description from package metadata - EXACT quote}

![CI Status](badge_url) ![Version](badge_url) ![License](badge_url)


Verification:

Name from package.json:name
Description from package.json:description (exact)
Badge URLs verified against .github/workflows/ files

Installation

## Installation

```bash
npm install {exact_package_name}


**Verification:**
- Package name from metadata (exact)
- Installation command matches package manager detected
- Prerequisites from "engines" field



Usage Examples

## Usage

```javascript
import { functionName } from 'package-name'

// Example verified from examples/ directory or tests/
const result = functionName(input)


**Verification:**
- Imports verified: Grep for actual exports
- Function signatures extracted from actual code
- Examples copied from examples/ or tests/ directories



API Documentation

## API

### `functionName(param: Type): ReturnType`

Description verified from code comments/docstrings.


Verification:

Function signatures extracted with Grep
Parameters from actual function definitions
Descriptions from docstrings (if present)

Configuration

## Configuration

Required environment variables:
- `VAR_NAME` - Description from .env.example


Verification:

Variables found in code with Grep
Descriptions from .env.example (if exists)

Testing

## Testing

```bash
npm test


**Verification:**
- Test command from package.json scripts.test
- Test framework detected from dependencies



Contributing, License, Contact

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## License

{license from package.json} - See [LICENSE](./LICENSE)


Verification:

CONTRIBUTING.md existence checked
LICENSE file existence checked
License type from package metadata

Output: Complete README draft with inline citations.

Phase 4: Validation (1-2 min)

Goal: Verify all claims are accurate.

Load Knowledge: knowledge/foundation/validation-checklist.md

Execute 5-Layer Validation:

Layer 1: File Existence

# Verify all referenced files
Read: file_path="<each_referenced_file>"
# Pass: File exists ✅
# Fail: Remove reference from README ❌


Layer 2: Content Accuracy

Compare README claims against actual file contents
Verify function signatures match actual code
Check version numbers match package.json exactly
Confirm descriptions are exact quotes (not paraphrased)

Layer 3: Execution Validity Load Knowledge: knowledge/application/script-executor.md

# Test installation command (if safe)
# Test CLI commands with --help flag
# Extract code examples to temp files and execute


Layer 4: Link Integrity

# Internal links
Read: file_path="<each_linked_file>"

# External URLs (sample check)
WebFetch: url="<external_url>" prompt="Check accessibility"

# Anchor links
Grep: pattern="^#+\s+{anchor_text}" path="README.md"


Layer 5: Citation Traceability

Every claim has source file:line reference (internal tracking)
Confidence scores: 100% (direct quote), 90% (extracted), 70%+ required
Remove any claim with confidence <70%

Output: Validation report with pass/fail for each layer.

Phase 5: Quality Assessment (30 sec)

Goal: Ensure README meets quality standards.

Load Knowledge: knowledge/application/quality-standards.md

Quality Checklist:

 Completeness: All required sections present
 Accuracy: All claims verified (95%+ confidence)
 Clarity: Readable, concise, well-structured
 Functional: All commands/examples tested
 Standard Compliance: Follows standard-readme spec
 Links: All links valid and working
 Length: Not too short (<50 lines) or too long (>500 lines)
 TOC: Table of contents if >100 lines
 Badges: Relevant and accurate
 License: Clearly stated

Scoring Rubric:

9-10/10: Excellent - All criteria met
7-8/10: Good - Minor improvements needed
5-6/10: Fair - Several issues to fix
<5/10: Poor - Major revision required

Target: ≥8/10 for publication

Output: Quality score and improvement recommendations.

Phase 6: Final Output

Deliverables:

README.md - Complete, validated file
Validation Report - Results from 5-layer validation
Citation Map (optional) - Source tracking for audit
Quality Score - Final assessment

Final Checks Before Delivery:

No TODOs or placeholder text
No broken links
No unverified claims
All code examples tested (where possible)
No marketing fluff without evidence
Section 2: Validation-Only Workflow

Use when: README exists, need to verify accuracy.

Time: 2-3 minutes Output: Validation report with pass/fail status

Quick Validation Process

Load Knowledge: knowledge/foundation/validation-checklist.md

Execute 5-Layer Validation:

Layer 1: File Existence (verify all referenced files)
Layer 2: Content Accuracy (check claims match reality)
Layer 3: Execution Validity (test commands/scripts)
Layer 4: Link Integrity (validate all URLs/links)
Layer 5: Citation Traceability (audit claim sources)

Generate Report:

README Validation Report
========================
Layer 1: ✅ PASS / ❌ FAIL (details)
Layer 2: ✅ PASS / ⚠️ WARNING (details)
Layer 3: ✅ PASS / ❌ FAIL (details)
Layer 4: ✅ PASS / ❌ FAIL (details)
Layer 5: ✅ PASS / ⚠️ WARNING (details)

OVERALL: ✅ READY / ⚠️ NEEDS FIXES / ❌ MAJOR ISSUES
Hallucination Risk: LOW/MEDIUM/HIGH
Confidence: XX%


Provide Fix Recommendations:

List specific issues found
Suggest corrections with source file references
Prioritize critical fixes (broken links, false claims)
Anti-Hallucination Principles

Core Rules (Always Follow):

✅ DO: Verify every file reference with Read/Glob

✅ DO: Extract exact quotes from source files

✅ DO: Test commands before documenting them

✅ DO: Link claims to source files (internal tracking)

✅ DO: Acknowledge uncertainty when confidence <90%

❌ DON'T: Assume standard structure without checking

❌ DON'T: Invent features not found in code

❌ DON'T: Copy examples from other projects

❌ DON'T: Paraphrase or "improve" actual descriptions

❌ DON'T: Include marketing claims without evidence

Hallucination Detection Patterns:

Red Flag	Example	Fix
Invented features	"Supports automatic retry" (no retry code)	Remove or find evidence
Fake examples	api.configure({theme:'dark'}) (method doesn't exist)	Use actual API
Missing files	"See docs/guide.md" (file doesn't exist)	Remove reference or create file
Wrong versions	"Requires Node 14+" (actually requires 18+)	Use exact version from metadata
Unsupported claims	"The fastest solution"	Remove or cite benchmarks
Knowledge Base Reference

All detailed guides are in knowledge/ directory.

Quick Access:

Scanning techniques: knowledge/foundation/codebase-scanner.md
Validation checklist: knowledge/foundation/validation-checklist.md
Script testing: knowledge/application/script-executor.md
Templates: knowledge/application/template-library.md
Quality standards: knowledge/application/quality-standards.md

Navigation: See knowledge/INDEX.md for complete map.

Best Practices
Start with scanning - Gather facts before writing
Use templates - Don't reinvent structure
Quote exactly - Never paraphrase metadata
Test everything - Execute commands where safe
Validate thoroughly - All 5 layers, no shortcuts
Acknowledge gaps - Mark uncertain info clearly
Keep it concise - Link to detailed docs instead of duplicating
Update regularly - Validate README on major code changes
Common Use Cases
Use Case 1: New Project README
User: "Create a README for my new npm package"
→ Section 1 (Full Workflow)
→ Scan package.json → Select template → Generate → Validate → Deliver

Use Case 2: Validate Accuracy
User: "Check if my README is still accurate"
→ Section 2 (Validation Only)
→ Run 5-layer validation → Report issues → Suggest fixes

Use Case 3: Update After Refactor
User: "Update README after refactoring API"
→ Section 1 (Focus on API section)
→ Scan new API → Update API section → Validate → Deliver

Use Case 4: Test Examples
User: "Make sure all code examples in README work"
→ Section 2 Layer 3 (Execution Validity)
→ Extract examples → Execute → Report failures → Fix

Technical Notes

Token Efficiency:

P0 knowledge files: ~530 tokens
P1 knowledge files: ~830 tokens
Total knowledge: ~1,360 tokens (well under 5k limit)
On-demand loading: Load only sections needed

Confidence Scoring:

100%: Direct file quote
90%: Extracted from code analysis
80%: Inferred from multiple sources
70%: Based on conventions
<70%: Reject (too risky)

Script Execution Safety:

Always ask permission before executing destructive commands
Safe: --help, --version, --list
Risky: install, build, deploy
Dangerous: rm, drop, delete
Version

Current Version: 1.0 Last Updated: 2025-11-13 Status: Production Ready

Changelog:

v1.0: Initial release with validation-first approach
Added script execution testing
5-layer anti-hallucination validation
Citation tracking system
Weekly Installs
14
Repository
rfxlamia/claude-skillkit
GitHub Stars
95
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn