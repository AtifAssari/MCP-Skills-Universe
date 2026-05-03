---
rating: ⭐⭐
title: docs-updater
url: https://skills.sh/anton-abyzov/specweave/docs-updater
---

# docs-updater

skills/anton-abyzov/specweave/docs-updater
docs-updater
Installation
$ npx skills add https://github.com/anton-abyzov/specweave --skill docs-updater
SKILL.md
Documentation Updater

Updates product documentation (.specweave/docs/) based on implementation progress.

When to Use
Task specifies documentation updates in tasks.md
Feature implementation is complete
User says "update documentation" or "sync docs"
After closing increment to ensure docs reflect reality
What It Does
Reads task requirements - Understands what was implemented from tasks.md
Updates living docs - Modifies .specweave/docs/ files with actual implementation
Status tracking - Changes [DRAFT] � [COMPLETE] on doc sections
Bidirectional links - Maintains links between docs and increments
Format adaptation - Matches existing doc structure (features/ or modules/)
Workflow
1. Read tasks.md � Find documentation tasks
2. Read implementation � Understand what changed
3. Update docs � Add real code examples, endpoints, configs
4. Mark complete � Change [DRAFT] to [COMPLETE]
5. Verify links � Ensure increment � doc references work

Example

tasks.md says:

**Documentation Updates**:
- [ ] .specweave/docs/features/payment.md [DRAFT]
- [ ] .specweave/docs/api/payments.md [DRAFT]


docs-updater does:

Reads payment implementation code
Updates payment.md with actual code examples
Updates API docs with real endpoints discovered in code
Changes status to [COMPLETE]
Integration Points
Called by: spec-generator, task completion hooks
Updates: .specweave/docs/**/*.md
Reads: tasks.md, implementation code
Best Practices
Run after completing feature tasks, not during
Verify doc links are valid (use relative paths)
Keep examples in sync with actual code
Don't over-document - focus on what users need
Project-Specific Learnings

Before starting work, check for project-specific learnings:

# Check if skill memory exists for this skill
cat .specweave/skill-memories/docs-updater.md 2>/dev/null || echo "No project learnings yet"


Project learnings are automatically captured by the reflection system when corrections or patterns are identified during development. These learnings help you understand project-specific conventions and past decisions.

Weekly Installs
19
Repository
anton-abyzov/specweave
GitHub Stars
134
First Seen
Jan 22, 2026