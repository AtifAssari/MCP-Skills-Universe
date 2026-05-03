---
title: add-deeds
url: https://skills.sh/puzzmo-com/oss/add-deeds
---

# add-deeds

skills/puzzmo-com/oss/add-deeds
add-deeds
Installation
$ npx skills add https://github.com/puzzmo-com/oss --skill add-deeds
SKILL.md
Add Deeds

Deeds are interesting statistics about a gameplay session. They're sent on completion and used for leaderboards, achievements, and social sharing.

Steps

Identify 3-6 interesting metrics from the game. Good deeds are things like:

Number of moves made
Words found / items collected
Accuracy percentage
Streak length (consecutive correct answers)
Unique items discovered
Time per move/action

Track these metrics during gameplay. Add counters/trackers to the game state.

On completion, include deeds in the gameCompleted call via the config parameter:

sdk.gameCompleted(gameplayMetrics, {
  deeds: [
    { id: "moves", value: totalMoves },
    { id: "accuracy", value: Math.round((correctMoves / totalMoves) * 100) },
    { id: "streak", value: longestStreak },
    { id: "items-found", value: itemsFound },
  ],
})


Deed IDs should be:

Lowercase kebab-case
Short and descriptive
Stable (don't change between versions)

The SDK automatically adds points and time deeds - you don't need to add those.

Also send deeds during checkpoints if the game has intermediate milestones:

sdk.hitCheckpoint(
  "level-complete",
  {
    interruptible: true,
    complete: false,
    process: [],
  },
  {
    deeds: [{ id: "items-found", value: itemsFound }],
  },
)

Success Criteria
npm run build completes without errors
At least 3 meaningful deeds are tracked during gameplay
Deeds are sent with gameCompleted
Deed IDs are kebab-case and descriptive
Weekly Installs
9
Repository
puzzmo-com/oss
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass