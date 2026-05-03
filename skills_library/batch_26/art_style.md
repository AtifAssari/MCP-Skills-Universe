---
title: art-style
url: https://skills.sh/dv0x/creative-ad-agent/art-style
---

# art-style

skills/dv0x/creative-ad-agent/art-style
art-style
Installation
$ npx skills add https://github.com/dv0x/creative-ad-agent --skill art-style
SKILL.md
Art Style Skill

Routes to the appropriate art style workflow based on user keywords.

Prerequisites

Hook-bank must exist before triggering this skill. Main Agent triggers hook-methodology skill first, which creates: /storage/hooks/{brand}-{date}.md

Input/Output
Input: Reads hook-bank file for brand colors, ICP, and 6 hook concepts
Output: Writes /storage/creatives/{brand}_prompts.json

Main Agent handles image generation via MCP after this skill completes.

Style Routing
User Keywords	Workflow
"clay", "diorama", "anderson", "theatrical", "miniature", "handcrafted"	workflows/anderson-clay-diorama.md
"brutalism", "soft brutalism", "neo-brutalist", "bold borders"	workflows/soft-brutalism-clay.md
"surreal", "dreamlike", "scale", "giant"	workflows/surrealist-scale.md (future)
"minimal", "clean", "photography", "simple"	workflows/minimal-photography.md (future)
(none specified)	workflows/anderson-clay-diorama.md (default)
Style Comparison
Style	Best For	Visual Signature
Anderson Clay Diorama	Storytelling ads, emotional narratives	Wes Anderson symmetry, theatrical lighting, museum diorama feel
Soft Brutalism Clay	Bold brand statements, high-contrast ads	Neo-brutalist borders, single hero object, generous negative space
Adding New Styles
Create workflows/new-style-name.md
Include: hook-bank loading, creative process, prompt construction
Add detection keywords to routing table above
Output prompts to /storage/creatives/{brand}_prompts.json

Each workflow file must be 100% self-contained for the creative process.

Weekly Installs
14
Repository
dv0x/creative-ad-agent
GitHub Stars
93
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass