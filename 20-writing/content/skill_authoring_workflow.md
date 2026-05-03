---
rating: ⭐⭐⭐
title: skill-authoring-workflow
url: https://skills.sh/deanpeters/product-manager-skills/skill-authoring-workflow
---

# skill-authoring-workflow

skills/deanpeters/product-manager-skills/skill-authoring-workflow
skill-authoring-workflow
Installation
$ npx skills add https://github.com/deanpeters/product-manager-skills --skill skill-authoring-workflow
Summary

Transform rough notes and workshop content into validated, repo-compliant PM skills.

Guides you through six phases: preflight search, draft generation, tightening, strict validation, repo integration, and optional packaging
Enforces a strict definition of done including frontmatter validity, metadata limits (name ≤64 chars, description ≤200 chars), and section compliance
Provides three creation paths: guided wizard for ideas, content-first generator for existing source material, and manual edit plus validation for updates
Includes built-in scripts for duplicate detection, structural testing, metadata checking, and trigger validation before commit
SKILL.md
Purpose

Create or update PM skills without chaos. This workflow turns rough notes, workshop content, or half-baked prompt dumps into compliant skills/<skill-name>/SKILL.md assets that actually pass validation and belong in this repo.

Use it when you want to ship a new skill without "looks good to me" roulette.

Key Concepts
Dogfood First

Use repo-native tools and standards before inventing a custom process:

scripts/find-a-skill.sh
scripts/add-a-skill.sh
scripts/build-a-skill.sh
scripts/test-a-skill.sh
scripts/check-skill-metadata.py
Pick the Right Creation Path
Guided wizard (build-a-skill.sh): Best when you have an idea but not final prose.
Content-first generator (add-a-skill.sh): Best when you already have source content.
Manual edit + validate: Best for tightening an existing skill.
Definition of Done (No Exceptions)

A skill is done only when:

Frontmatter is valid (name, description, intent, type)
Section order is compliant
Metadata limits are respected (name <= 64 chars, description <= 200 chars)
Description says both what the skill does and when to use it
Intent carries the fuller repo-facing summary without replacing the trigger-oriented description
Cross-references resolve
README catalog counts and tables are updated (if adding/removing skills)
Facilitation Source of Truth

When running this workflow as a guided conversation, use workshop-facilitation as the interaction protocol.

It defines:

session heads-up + entry mode (Guided, Context dump, Best guess)
one-question turns with plain-language prompts
progress labels (for example, Context Qx/8 and Scoring Qx/5)
interruption handling and pause/resume behavior
numbered recommendations at decision points
quick-select numbered response options for regular questions (include Other (specify) when useful)

This file defines the workflow sequence and domain-specific outputs. If there is a conflict, follow this file's workflow logic.

Application
Phase 1: Preflight (Avoid Duplicate Work)
Search for overlapping skills:
./scripts/find-a-skill.sh --keyword "<topic>"

Decide type:
Component: one artifact/template
Interactive: 3-5 adaptive questions + numbered options
Workflow: multi-phase orchestration
Phase 2: Generate Draft

If you have source material:

./scripts/add-a-skill.sh research/your-framework.md


If you want guided prompts:

./scripts/build-a-skill.sh

Phase 3: Tighten the Skill

Manually review for:

Clear "when to use" guidance
One concrete example
One explicit anti-pattern
No filler or vague consultant-speak
Phase 4: Validate Hard

Run strict checks before thinking about commit:

./scripts/test-a-skill.sh --skill <skill-name> --smoke
python3 scripts/check-skill-metadata.py skills/<skill-name>/SKILL.md
python3 scripts/check-skill-triggers.py skills/<skill-name>/SKILL.md --show-cases

Phase 5: Integrate with Repo Docs

If this is a new skill:

Add it to the correct README category table
Update skill totals and category counts
Verify link paths resolve
Phase 6: Optional Packaging

If targeting Claude custom skill upload:

./scripts/zip-a-skill.sh --skill <skill-name>
# or zip one category:
./scripts/zip-a-skill.sh --type component --output dist/skill-zips
# or use a curated starter preset:
./scripts/zip-a-skill.sh --preset core-pm --output dist/skill-zips

Examples
Example: Turn Workshop Notes into a Skill

Input: research/pricing-workshop-notes.md
Goal: new interactive advisor

./scripts/add-a-skill.sh research/pricing-workshop-notes.md
./scripts/test-a-skill.sh --skill <new-skill-name> --smoke
python3 scripts/check-skill-metadata.py skills/<new-skill-name>/SKILL.md


Expected result:

New skill folder exists
Skill passes structural and metadata checks
README catalog entry added/updated
Anti-Pattern Example

"We wrote a cool skill, skipped validation, forgot README counts, and shipped anyway."

Result:

Broken references
Inconsistent catalog numbers
Confusion for contributors and users
Common Pitfalls
Shipping vibes, not standards.
Choosing workflow when the task is really a component template.
Bloated descriptions that exceed upload limits.
Descriptions that say what the skill is but not when Claude should trigger it.
Descriptions that silently hit the 200-char limit and get cut off mid-thought.
Letting intent become a substitute for a weak trigger description.
Forgetting to update README counts after adding a skill.
Treating generated output as final without review.
References
README.md
AGENTS.md
CLAUDE.md
docs/Building PM Skills.md
docs/Add-a-Skill Utility Guide.md
Anthropic's Complete Guide to Building Skills for Claude
scripts/add-a-skill.sh
scripts/build-a-skill.sh
scripts/find-a-skill.sh
scripts/test-a-skill.sh
scripts/check-skill-metadata.py
scripts/check-skill-triggers.py
scripts/zip-a-skill.sh
Weekly Installs
780
Repository
deanpeters/prod…r-skills
GitHub Stars
3.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass