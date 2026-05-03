---
title: spec-template
url: https://skills.sh/b1tank/skills/spec-template
---

# spec-template

skills/b1tank/skills/spec-template
spec-template
Installation
$ npx skills add https://github.com/b1tank/skills --skill spec-template
SKILL.md
Product Spec Template

A structured 9-section template for defining software product specifications.

When to Use
Starting a new project from a one-liner idea
Converting rough notes into a formal specification
Reviewing spec completeness before implementation
Ensuring consistent spec format across projects
The 9 Sections
Section Structure

Every spec.md should include these sections:

## 🎯 [Product Name]

### 🧠 One-Line Definition

> **[Concise description: what it is, key differentiator, core value prop]**

### Top Principles
- [Guiding principle 1]
- [Guiding principle 2]
- [Guiding principle 3]

### 1. [Core Capability Area]
| Category | Feature |
|----------|---------|
| ... | ... |

### 2. [Controls / Interactions]
| Feature | Support |
|---------|---------|
| ... | ... |

### 3. [Technical / Output Format]
| Feature | Support |
|---------|---------|
| ... | ... |

### 4. [Secondary Feature Area]
| Feature | Support |
|---------|---------|
| ... | ... |

### 5. [Tertiary Feature Area]
| Feature | Support |
|---------|---------|
| ... | ... |

### 6. [Optional Feature Area]
| Feature | Support |
|---------|---------|
| ... | ... |

### 7. UI / UX Principles
| Principle | Description |
|-----------|-------------|
| ... | ... |

### 8. Platform / Scope
| Platform | Priority |
|----------|----------|
| ... | ... |

### 9. Explicit Non-Goals
| Feature | Status |
|---------|--------|
| [Feature X] | ❌ |
| [Feature Y] | ❌ |

Section Guidelines
One-Line Definition
Must be a single sentence
Include: what it is, how it differs, core value
Example: "A lightweight screen recorder that matches GNOME Screencast's minimal UX, adds audio capture, and supports basic post-capture annotation."
Top Principles
3-5 guiding principles
Drive prioritization decisions
Examples: "Quickly deliverable MVP", "Cross-platform support", "Minimal UI"
Feature Sections (1-6)
Use tables for consistency
Mark support: ✅ (yes), ❌ (no), Optional, Basic
Group related features
Section names vary by product type
UI/UX Principles
Reference existing UX patterns when applicable
Define the "feel" of the product
Include mode-based behavior if relevant
Platform Scope
List all target platforms
Mark priority: Primary, Supported, Future
Be explicit about what's NOT supported initially
Non-Goals
Critical section—prevents scope creep
List features explicitly excluded
Mark all with ❌
Include common requests that won't be built
Output Quality Checklist
 One-liner is truly one sentence
 Principles are actionable, not vague
 Feature tables use consistent format
 Non-goals section is substantive (5+ items)
 No ambiguous "maybe" features—decide yes/no
 Platform priorities are clear
Weekly Installs
9
Repository
b1tank/skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass