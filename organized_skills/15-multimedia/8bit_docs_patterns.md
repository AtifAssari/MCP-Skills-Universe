---
rating: ⭐⭐
title: 8bit-docs-patterns
url: https://skills.sh/theorcdev/8bitcn-ui/8bit-docs-patterns
---

# 8bit-docs-patterns

skills/theorcdev/8bitcn-ui/8bit-docs-patterns
8bit-docs-patterns
Installation
$ npx skills add https://github.com/theorcdev/8bitcn-ui --skill 8bit-docs-patterns
SKILL.md
8-bit Documentation Patterns

Create documentation that emphasizes the gaming and retro aspects of 8-bit components.

Gaming Terminology

Use gaming-specific language in descriptions and examples:

---
title: Quest Log
description: Displays an 8-bit mission and task tracking system.
---

Realistic Game Data

Use meaningful, game-related data in examples:

<QuestLog
  quests={[
    {
      id: "quest-1",
      title: "Defeat the Goblin King",
      description: "The Goblin King has been terrorizing the village for weeks.",
      status: "active",
      shortDescription: "Defeat the Goblin King in the Dark Forest.",
    },
    {
      id: "quest-2",
      title: "Collect Dragon Scales",
      description: "The local blacksmith needs dragon scales to forge armor.",
      status: "completed",
      shortDescription: "Collect 10 dragon scales.",
    },
  ]}
/>

Health Bar Examples

Use realistic health values and context:

<HealthBar value={75} />

<div className="flex justify-between text-sm mb-2 retro">
  <span>Health</span>
  <span>75%</span>
</div>
<HealthBar value={75} />

<p className="text-sm text-muted-foreground mb-2">
  Default health bar
</p>
<HealthBar value={75} />

<p className="text-sm text-muted-foreground mb-2">
  Critical health (25%)
</p>
<HealthBar value={25} variant="retro" />

Pixel Font Usage

Apply .retro class for pixel font styling:

<div className="flex justify-between text-sm mb-2 retro">
  <span>Health</span>
  <span>75/100</span>
</div>

Wrapper Pattern in Examples

Remember 8-bit components wrap shadcn/ui:

// Import the 8-bit component
import { Button } from "@/components/ui/8bit/button";

// Not the base shadcn component
import { Button } from "@/components/ui/button"; // Wrong!

retro.css Awareness

All 8-bit components require retro.css:

// This import is required in the component source
import "@/components/ui/8bit/styles/retro.css";

// Documentation shows usage with 8-bit components
<Button className="retro">START GAME</Button>

Multiple Variants

Show default vs retro variants:

<ComponentPreview title="8-bit Health Bar component" name="health-bar">
  <div className="md:min-w-[300px] min-w-[200px] flex flex-col gap-8">
    <div>
      <p className="text-sm text-muted-foreground mb-2">
        Default health bar
      </p>
      <HealthBar value={75} />
    </div>
    <div>
      <p className="text-sm text-muted-foreground mb-2">
        Retro health bar
      </p>
      <HealthBar value={45} variant="retro" />
    </div>
  </div>
</ComponentPreview>

Gaming Block Documentation

For blocks (multiple components):

---
title: Quest Log
description: Displays an 8-bit mission and task tracking system.
---

<ComponentPreview title="8-bit Quest Log block" name="quest-log">
  <QuestLog
    quests={[
      {
        id: "quest-1",
        title: "Defeat the Goblin King",
        status: "active",
      },
    ]}
  />
</ComponentPreview>

Key Principles
Gaming context - Use game-related terminology
Realistic data - Show actual game scenarios
Retro styling - Use .retro class for pixel fonts
Wrapper awareness - Import from @/components/ui/8bit/
Variant showcase - Demonstrate multiple variants
Block complexity - Handle multi-component documentation
8-bit specific - Emphasize unique 8-bit features
Reference Examples
content/docs/blocks/gaming/quest-log.mdx - Quest tracking pattern
content/docs/components/health-bar.mdx - Health bar variants
content/docs/blocks/gaming/leaderboard.mdx - Gaming list pattern
Weekly Installs
26
Repository
theorcdev/8bitcn-ui
GitHub Stars
1.8K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass