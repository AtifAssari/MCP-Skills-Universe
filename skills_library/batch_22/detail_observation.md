---
title: detail-observation
url: https://skills.sh/dragoon0x/taste-skills/detail-observation
---

# detail-observation

skills/dragoon0x/taste-skills/detail-observation
detail-observation
Installation
$ npx skills add https://github.com/dragoon0x/taste-skills --skill detail-observation
SKILL.md
Detail Observation

Catalog the micro-decisions nobody else notices.

How to use
/detail-observation Apply detail-level analysis constraints to this conversation.
Constraints
What to Catalog
MUST count the actual number of type sizes in use (not what the system says, what's on screen)
MUST identify the spacing scale (is it 4/8/16/24/32 or random values?)
MUST note border radius consistency (same across buttons, cards, inputs, or varying?)
MUST check weight usage (how many font weights, and is each one serving a clear purpose?)
SHOULD identify the color count and role of each color (primary, neutral, accent, semantic)
SHOULD check hover, focus, active, disabled, loading, empty, error, and success states
Precision Over Opinion
MUST use specific values: "16px margin" not "generous spacing"
MUST note inconsistencies with evidence: "buttons use 4px radius, cards use 8px, inputs use 6px"
NEVER say "it feels inconsistent" without pointing to the specific inconsistency
SHOULD compare observed values against the design system if one exists
Anti-Patterns
Stopping at the surface level ("the typography looks good")
Treating every inconsistency as an error (some breaks are intentional)
Spending time on details that don't affect the user experience
Weekly Installs
13
Repository
dragoon0x/taste-skills
GitHub Stars
1
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass