---
title: workflow-patterns
url: https://skills.sh/mgd34msu/goodvibes-plugin/workflow-patterns
---

# workflow-patterns

skills/mgd34msu/goodvibes-plugin/workflow-patterns
workflow-patterns
Installation
$ npx skills add https://github.com/mgd34msu/goodvibes-plugin --skill workflow-patterns
SKILL.md
Workflow Patterns

Reusable patterns for structuring workflows in skills and agents.

Sequential with Checklist

Use when steps must be completed in order with tracking:

## Form Processing Workflow

Track progress:
- [ ] Step 1: Analyze form (run analyze_form.py)
- [ ] Step 2: Create field mapping
- [ ] Step 3: Validate (run validate.py)
- [ ] Step 4: Fill form
- [ ] Step 5: Verify output


When to use: Multi-step processes where completion tracking matters.

Conditional Routing

Use when different paths apply based on context:

## Document Workflow

1. Determine task type:
   - **Creating new?** -> Follow Creation workflow
   - **Editing existing?** -> Follow Editing workflow

## Creation workflow
[steps for new documents]

## Editing workflow
[steps for existing documents]


When to use: Tasks with distinct modes or branches.

Validation Loop

Use when iterative refinement is needed:

1. Make changes
2. Validate: `python validate.py`
3. If errors:
   - Fix issues
   - Return to step 2
4. Only proceed when validation passes


When to use: Operations requiring correctness verification.

Progressive Disclosure Patterns
Pattern 1: Quick Start + References

Front-load common usage, defer details:

## Quick start
[Most common usage - get user productive fast]

## Advanced
- **Forms**: See [FORMS.md](references/forms.md)
- **API details**: See [REFERENCE.md](references/reference.md)

Pattern 2: Domain Organization

Organize by topic when multiple domains exist:

bigquery/
  SKILL.md (overview + navigation)
  references/
    finance.md
    sales.md
    product.md

Pattern 3: Conditional Depth

Provide escape hatches for advanced needs:

## Basic usage
[Simple approach that works 80% of the time]

**For tracked changes**: See [REDLINING.md](references/redlining.md)
**For batch processing**: See [BATCH.md](references/batch.md)

Degrees of Freedom

Match instruction specificity to the situation:

Situation	Freedom Level	Example
Multiple valid approaches	High	"Analyze code structure and suggest improvements"
Preferred pattern exists	Medium	"Use this template, customize as needed"
Fragile/critical operation	Low	"Run exactly: python migrate.py --verify"
Combining Patterns

Patterns can be nested:

## Main Workflow

1. Determine mode:
   - **Quick fix?** -> Use Quick Fix workflow
   - **Full analysis?** -> Use Analysis workflow

## Quick Fix workflow
- [ ] Identify issue
- [ ] Apply fix
- [ ] Validate: `npm test`
- [ ] If fails, return to step 2

## Analysis workflow
See [DEEP_ANALYSIS.md](references/deep-analysis.md) for comprehensive steps.

Anti-Patterns
Anti-Pattern	Problem	Fix
No clear entry point	User doesn't know where to start	Add "Quick Start" section
Too many branches	Decision paralysis	Provide sensible defaults
No validation step	Errors discovered too late	Add explicit verification
References too deep	Content hard to find	Keep one level from SKILL.md
Weekly Installs
16
Repository
mgd34msu/goodvi…s-plugin
GitHub Stars
6
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass