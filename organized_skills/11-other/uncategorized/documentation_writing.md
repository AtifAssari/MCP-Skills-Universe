---
rating: ⭐⭐⭐⭐⭐
title: documentation-writing
url: https://skills.sh/rysweet/amplihack/documentation-writing
---

# documentation-writing

skills/rysweet/amplihack/documentation-writing
documentation-writing
Installation
$ npx skills add https://github.com/rysweet/amplihack --skill documentation-writing
SKILL.md
Documentation Writing Skill
Purpose

Creates high-quality, discoverable documentation following the Eight Rules and Diataxis framework. Ensures all docs are properly located, linked, and contain real runnable examples.

When I Activate

I load automatically when you mention:

"write documentation" or "create docs"
"document this feature/module/API"
"create a README" or "write a tutorial"
"explain how this works"
Any request to create markdown documentation
Core Rules (MANDATORY)
The Eight Rules
Location: All docs in docs/ directory
Linking: Every doc linked from at least one other doc
Simplicity: Plain language, remove unnecessary words
Real Examples: Runnable code, not "foo/bar" placeholders
Diataxis: One doc type per file (tutorial/howto/reference/explanation)
Scanability: Descriptive headings, table of contents for long docs
Local Links: Relative paths, context with links
Currency: Delete outdated docs, include update metadata
What Stays OUT of Docs

Never put in docs/:

Status reports or progress updates
Test results or benchmarks
Meeting notes or decisions
Plans with dates
Point-in-time snapshots

Where temporal info belongs:

Test results → CI logs, GitHub Actions
Status updates → GitHub Issues
Progress → Pull Request descriptions
Decisions → Commit messages
Quick Start
Creating a New Document
# [Feature Name]

Brief one-sentence description of what this is.

## Quick Start

Minimal steps to get started (3-5 steps max).

## Contents

- [Configuration](#configuration)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)

## Configuration

Step-by-step setup with real examples.

## Usage

Common use cases with runnable code.

## Troubleshooting

Common problems and solutions.

Document Types (Diataxis)
Type	Purpose	Location	User Question
Tutorial	Learning	docs/tutorials/	"Teach me how"
How-To	Doing	docs/howto/	"Help me do X"
Reference	Information	docs/reference/	"What are the options?"
Explanation	Understanding	docs/concepts/	"Why is it this way?"
Workflow
Step 1: Determine Document Type

Ask: What is the reader trying to accomplish?

Learning something new → Tutorial
Solving a specific problem → How-To
Looking up details → Reference
Understanding concepts → Explanation
Step 2: Choose Location
docs/
├── tutorials/     # Learning-oriented
├── howto/         # Task-oriented
├── reference/     # Information-oriented
├── concepts/      # Understanding-oriented
└── index.md       # Links to all docs

Step 3: Write with Examples

Every concept needs a runnable example:

# Example: Analyze file complexity
from amplihack import analyze

result = analyze("src/main.py")
print(f"Complexity: {result.score}")
# Output: Complexity: 12.5

Step 4: Link from Index

Add entry to docs/index.md:

- [New Feature Guide](./howto/new-feature.md) - How to configure X

Step 5: Validate

Checklist before completion:

 File in docs/ directory
 Linked from index or parent doc
 No temporal information
 All examples tested
 Follows one Diataxis type
Navigation Guide
When to Read Supporting Files

reference.md - Read when you need:

Complete frontmatter specification
Detailed Diataxis type definitions
Markdown style conventions
Documentation review checklist

examples.md - Read when you need:

Full document templates for each type
Real-world documentation examples
Before/after improvement examples
Complex documentation patterns
Anti-Patterns to Avoid
Anti-Pattern	Why It's Bad	Better Approach
"Click here" links	No context	"See auth config"
foo/bar examples	Not realistic	Use real project code
Wall of text	Hard to scan	Use headings and bullets
Orphan docs	Never found	Link from index
Status in docs	Gets stale	Use Issues/PRs
Retcon Documentation Exception

When writing documentation BEFORE implementation (document-driven development):

# [PLANNED - Implementation Pending]

This document describes the intended behavior of Feature X.

## Planned Interface

```python
# [PLANNED] - This API will be implemented
def future_function(input: str) -> Result:
    """Process input and return result."""
    pass
```


Once implemented, remove the [PLANNED] markers and update with real examples.


---

**Full reference**: See [reference.md](./reference.md) for complete specification.
**Templates**: See [examples.md](./examples.md) for copy-paste templates.

Weekly Installs
263
Repository
rysweet/amplihack
GitHub Stars
55
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass