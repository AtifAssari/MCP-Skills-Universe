---
rating: ⭐⭐⭐
title: memory-palace
url: https://skills.sh/simhacker/moollm/memory-palace
---

# memory-palace

skills/simhacker/moollm/memory-palace
memory-palace
Installation
$ npx skills add https://github.com/simhacker/moollm --skill memory-palace
SKILL.md
🏛️ Memory Palace Skill

"The filesystem is the mind. Directories are rooms. Files are objects."

The ancient method of loci, adapted for LLMs navigating filesystems.

The Technique

Place knowledge in locations. Navigate to remember.

Each room contains:

Objects (files) — artifacts to examine
Exits (links) — doors to other rooms
Atmosphere — the room's essence
This IS the Room Skill

Memory Palace and Room are deeply connected:

Memory Palace	Room Skill
Location	Directory
Object	File
Traversal	Enter/Exit
Placement	Create file
Recall	Navigate to

Memory Palace = Room + spatial mnemonic intent

Palace Structure
palace/
├── ENTRY.md          # Front door (README)
├── MAP.yml           # Navigation overview
│
├── concepts/         # Wing: Ideas
│   ├── ROOM.md
│   ├── yaml-jazz/
│   └── play-learn-lift/
│
├── characters/       # Wing: Personas
│   ├── ROOM.md
│   ├── gardener/
│   └── archivist/
│
└── skills/           # Wing: Capabilities
    ├── ROOM.md
    └── ...

Placing Knowledge

To remember something:

Choose a room — where does this belong?
Create a file — the object to place
Link it — connect to related objects
Walk there — navigate to reinforce
# palace/concepts/yaml-jazz/ROOM.yml
room:
  name: "YAML Jazz Chamber"
  contains:
    - "jazz-principles.md"    # Core ideas
    - "examples/"             # Sub-room of examples
  exits:
    parent: "../"
    related: "../play-learn-lift/"
  atmosphere: "improvisational, semantic"

Core Files
ENTRY.md

The front door to your palace:

# Palace Name

## Welcome
What this palace contains and why.

## Quick Navigation
- [Room A](room-a/ROOM.md) - Description
- [Room B](room-b/ROOM.md) - Description

## Recent Activity
- Added X to Room A
- Created new Room C

MAP.yml

Navigation structure:

palace:
  name: "Research Palace"
  created: "2025-12-30"
  
rooms:
  - name: "foundations"
    path: "foundations/"
    description: "Core concepts"
    connects_to: ["applications", "history"]
    
  - name: "applications"
    path: "applications/"
    description: "Practical uses"
    connects_to: ["foundations", "examples"]

landmarks:
  - name: "The Big Question"
    location: "foundations/core-question.md"
    importance: "Start here"

ROOM.md (in each room)
# Room Name

## What's Here
Description of this room's contents.

## Artifacts
- [artifact-1.md](artifact-1.md) - Description

## Doors
- ← Back to [Entry](../ENTRY.md)
- → Forward to [Next Room](../next-room/ROOM.md)

## Notes
Observations, questions, TODOs for this room.

Navigation Commands
Intent	Action
"Enter the palace"	Read ENTRY.md
"Look around"	ls current directory
"Go to room X"	cd to room, read ROOM.md
"Examine artifact"	Read the file
"Leave a note"	Create/update .meta.yml
"Create new room"	mkdir + create ROOM.md
"Check the map"	Read MAP.yml
"Where am I?"	Note current path
Lifecycle
Create
mkdir palace root
create ENTRY.md
create MAP.yml
create initial rooms
Expand
create new room directory
add ROOM.md
update MAP.yml
link from related rooms
Maintain
update MAP.yml periodically
add cross-references
archive stale rooms
create summaries
Archive
move to attic/
note in MAP.yml
update links
Tips
Start small — Begin with 3-5 rooms, expand as needed
Name meaningfully — Directory names are addresses
Link generously — Cross-references aid recall
Leave breadcrumbs — Update .meta.yml as you explore
Maintain the map — MAP.yml is your table of contents
Archive, don't delete — Move stale rooms to attic/
Integration
Skill	Relationship
room	Memory Palace IS Room + spatial mnemonic intent
adventure	Adventure IS Room + narrative quest framing
card	Objects placed in rooms can be cards
soul-chat	Palace rooms can speak, guide visitors
summarize	Compress palace knowledge for context
Weekly Installs
27
Repository
simhacker/moollm
GitHub Stars
38
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass