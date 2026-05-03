---
title: quick-mockups
url: https://skills.sh/civitai/civitai/quick-mockups
---

# quick-mockups

skills/civitai/civitai/quick-mockups
quick-mockups
Installation
$ npx skills add https://github.com/civitai/civitai --skill quick-mockups
SKILL.md
Quick Mockups

Create multiple design mockups in parallel using the design-mockup agent.

Usage

When asked to create mockups for a feature:

Create the output directory if it doesn't exist:

docs/working/mockups/<feature-name>/


Launch 3-5 parallel mockup agents using the Task tool with subagent_type: design-mockup

Each agent creates a unique variation with different:

Layout approaches (grid, list, masonry, cards)
Information hierarchy
Visual emphasis
Interaction patterns
Directory Structure
docs/working/mockups/
├── crucible-discovery/
│   ├── v1-grid-cards.html
│   ├── v2-featured-hero.html
│   ├── v3-compact-list.html
│   └── v4-masonry.html
├── crucible-rating/
│   ├── v1-side-by-side.html
│   ├── v2-stacked.html
│   └── v3-swipe.html
└── [feature-name]/
    └── [variation].html

Prompting Agents

When launching mockup agents, provide:

Feature name - What page/component to design
Key requirements - What must be included
Variation focus - What makes this variation unique
Reference context - Link to existing similar pages if helpful

Example prompt for agent:

Create a mockup for the Crucible Discovery page.

Requirements:
- List of active crucibles as cards
- Show: name, prize pool, time remaining, entry count
- Filter/sort controls (by prize, ending soon, newest)
- "Create Crucible" button

Variation: Grid layout with large hero card for featured crucible

Output to: docs/working/mockups/crucible-discovery/v1-featured-hero.html

After Creating Mockups
List all created mockup files
Summarize each variation's approach
Ask user which direction to pursue or if they want more variations
Tips
Create variations that are meaningfully different, not just minor tweaks
Consider mobile layouts in at least one variation
Show realistic content (names, numbers, times)
Include empty states where relevant
Use the Civitai design patterns from .claude/agents/design-mockup.md
Weekly Installs
298
Repository
civitai/civitai
GitHub Stars
7.1K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass