---
rating: ⭐⭐
title: setup-augmentations
url: https://skills.sh/puzzmo-com/oss/setup-augmentations
---

# setup-augmentations

skills/puzzmo-com/oss/setup-augmentations
setup-augmentations
Installation
$ npx skills add https://github.com/puzzmo-com/oss --skill setup-augmentations
SKILL.md
Setup Augmentations

Create an augmentations.json file that configures leaderboards and other meta-game features using the deeds defined in the previous step.

Steps

Create augmentations.json in the project root:

{
  "_v": 1,
  "augmentations": {
    "leaderboards": [
      {
        "displayName": "Fastest Time",
        "stableID": "game-GAMESLUG:time",
        "order": "Lower=better",
        "deedID": "time",
        "formatString": "[time]"
      },
      {
        "displayName": "High Score",
        "stableID": "game-GAMESLUG:points",
        "order": "Higher=better",
        "deedID": "points",
        "formatString": "%@"
      }
    ]
  }
}


Replace GAMESLUG with the actual game slug (the directory name, lowercased).

Add leaderboards for each meaningful deed. The stableID format MUST be game-[gameslug]:[deed-id].

Choose appropriate formatString values:

"[time]" - Converts seconds to MM:SS format
"%@" - Shows the number with locale formatting
"%@ moves" - Appends a unit
"%@%" - Shows as percentage

Set order appropriately:

"Lower=better" for time, moves, errors
"Higher=better" for score, accuracy, streaks
Success Criteria
augmentations.json exists and is valid JSON
At least 2 leaderboards are configured
All stableID values follow the game-slug:deed-id format
formatString values are appropriate for each metric
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