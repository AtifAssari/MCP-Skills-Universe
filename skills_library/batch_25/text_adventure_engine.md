---
title: text-adventure-engine
url: https://skills.sh/insight68/skills/text-adventure-engine
---

# text-adventure-engine

skills/insight68/skills/text-adventure-engine
text-adventure-engine
Installation
$ npx skills add https://github.com/insight68/skills --skill text-adventure-engine
SKILL.md
The Enchanted Journey 🏰✨

A magical text adventure game where your choices matter. Explore ancient forests, meet mysterious creatures, uncover hidden truths, and discover which ending awaits you.

Quick Start
Play the Game
# Method 1: Direct run (easiest)
python3 scripts/play.py

# Method 2: From skill directory
cd text-adventure-engine
python3 scripts/play.py


That's it! The game will start immediately. No setup required.

Game Controls
Command	Action
1, 2, 3...	Select a choice
S	Save your game
L	Load a saved game
H	Show help
Q	Quit game
About The Game

The Enchanted Journey is an interactive fantasy adventure where you play as a traveler who arrives at a mysterious forest. Your choices will:

Shape your character's moral alignment
Unlock hidden paths and secrets
Determine which of 6 endings you receive
Affect the lives of those you meet
Key Stats
❤️ Health - Your physical condition
💖 Morality - Your moral compass (determines your ending!)
🧠 Knowledge - Wisdom gained through exploration
💰 Gold - Currency for special choices
🎒 Inventory - Items you collect
🏆 Achievements - Special accomplishments
The Six Endings

Your morality and choices determine which ending you get:

Ending	Morality	Requirements
👑 The Guardian	High (80+)	Accept responsibility
🌗 The Age of Balance	High	Meet Shadow King, choose unity
🏠 The Return	Any	Refuse the Crown (humility path)
∞ Eternal Wanderer	Any	Choose to merge with Crown
💔 Failed Hero	Low	Selfish choices throughout
🌑 Shadow's Servant	Very Low	Consistently evil choices
Gameplay Tips
For the Best Experience
Read carefully - Details matter in this world
Explore everything - Knowledge unlocks new paths
Think before choosing - Actions have consequences
Help others - High morality leads to better endings
Save often - Before major decisions
Secret Paths to Discover
🦊 The Fox Ally - Help Felix for guidance throughout your journey
🧙‍♀️ The Witch's Deal - Visit the cottage for powerful (but costly) assistance
👤 The Star Watcher - Hidden path that reveals the truth about the Crown
🌑 The Shadow King - Can be met... or defeated... or joined
Achievement Guide
Achievement	How to Unlock
🔍 Curious Mind	Reach 50 knowledge
📚 Scholar	Reach 100 knowledge
🧠 Sage	Reach 200 knowledge
⭐ Master of Knowledge	Reach 500 knowledge
🦊 Fox Friend	Help Felix
🔮 Touched Destiny	Touch the crystal in ruins
🌟 True Balance	Achieve the co-ruler ending
∞ Eternal Wanderer	Choose to merge with Crown
Moral Choices Guide
The Power of Morality

Your morality stat is the most important factor in the game. It affects:

Which endings are available
How characters react to you
Secret paths that unlock
The ultimate fate of the kingdom
Examples of Moral Choices

Good Morality Choices (+10 to +20):

Help those in need
Show mercy to enemies
Choose diplomacy over violence
Keep your promises
Sacrifice for others

Evil Morality Choices (-10 to -20):

Harm innocents
Betray allies
Choose selfish gain
Ignore suffering
Break promises

Neutral Choices:

Focus on practical concerns
Avoid involvement
Choose inaction
Save System

Your progress is automatically saved to the saves/ folder.

Save Slots:

autosave - Default quick save
Custom names - Create named saves for different story branches

Pro Tip: Save before major story decisions to explore different outcomes!

Character Companions

Throughout your journey, you may meet allies who join you:

Companion	How to Recruit	Benefits
🦊 Felix	Talk to him at the forest entrance	Safe paths, shortcuts, lore
👤 Orion	Find the hidden trail with Felix	Reveals the Crown's true purpose
🧙‍♀️ Zora	Visit the witch's cottage	Potions, knowledge, or warnings
💚 Elara	Rescue her on the mountain path	Healing, companionship
Walkthrough Hints
Stuck? Here are some hints (spoilers minimal):

Beginning:

Talk to the fox! He's a valuable guide.
The ruins contain valuable knowledge.
The witch's cottage offers help... at a price.

Middle:

Explore all three mountain paths for different experiences.
The Shadow General can be defeated in multiple ways.
Knowledge unlocks special dialogue options.

End Game:

Your morality determines which endings are available.
Meeting the Shadow King reveals the truth.
The "best" ending requires high morality AND making the right final choice.
For Creators

Want to create your own text adventure game? This game includes a full game engine that's easy to modify.

Key Files:

scripts/engine.py - The game engine
scripts/example_game.json - The game script (easily editable!)
scripts/play.py - The game player

To Create Your Own Game:

Copy example_game.json as a template
Edit scenes, choices, and endings
Run python3 scripts/play.py to test

The JSON format is straightforward - no programming needed!

Game Info
Title: The Enchanted Journey
Genre: Text Adventure / Interactive Fiction
Playtime: 30-60 minutes per playthrough
Replayability: High (6 endings, secret paths)
Difficulty: Easy to learn, choices matter
Troubleshooting

Game won't start?

Make sure Python 3 is installed: python3 --version
Check you're in the correct directory

Lost your save?

Saves are in the saves/ folder
Each save is a JSON file you can back up

Want to restart?

Delete saves in saves/ folder
Or just load autosave and make different choices

Enjoy your adventure! 🗝️✨

Version: 2.0 | Created with love for interactive fiction fans everywhere

Weekly Installs
18
Repository
insight68/skills
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass