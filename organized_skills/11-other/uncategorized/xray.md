---
rating: ⭐⭐⭐
title: xray
url: https://skills.sh/soul-brews-studio/arra-oracle-skills/xray
---

# xray

skills/soul-brews-studio/arra-oracle-skills/xray
xray
Installation
$ npx skills add https://github.com/soul-brews-studio/arra-oracle-skills --skill xray
SKILL.md
/xray - X-Ray Deep Scan

Inspect and manage Claude Code auto-memory, installed skills, and session history.

Subcommands
Target	Description
memory	(default) Scan and manage Claude Code auto-memory
skills	List installed skills with profiles and status
sessions	Show session history and retrospectives
Target: memory (default)
Memory Location
ENCODED=$(pwd | sed 's|^/|-|; s|/|-|g')
MEMORY_DIR="$HOME/.claude/projects/${ENCODED}/memory"

Usage
/xray                     # Default: scan memory — list all memories with types
/xray memory              # Same as above
/xray memory scan         # Same as above
/xray memory read <name>  # Read a specific memory file
/xray memory stats        # Show counts by type, total size, age
/xray memory types        # Group memories by type
/xray memory clean        # Find stale/outdated memories
/xray memory forget <name># Remove a memory (after confirmation)
/xray skills              # List installed Oracle skills
/xray sessions            # Show session history

Mode 1: Scan (default)

List all memory files with type, age, and description.

MEMORY_DIR="$HOME/.claude/projects/$(pwd | sed 's|^/|-|; s|/|-|g')/memory"


Read each .md file (except MEMORY.md), extract frontmatter:

For each file, display:

🧠 Memory Scanner — [project name]

  Type        Name                              Age     Description
  ─────────── ───────────────────────────────── ─────── ────────────────────────
  feedback    never_push_main_skills            2d      Always use branch + PR
  feedback    talk_to_not_oracle_thread         9d      Use /talk-to for threads
  reference   maw_cli                           9d      maw hey, peek, ls commands
  reference   pulse_cli                         9d      board, timeline, scan
  user        work_patterns                     9d      maker's schedule, peak hours

  Total: 14 memories (5 feedback, 3 reference, 1 user, 0 project)
  Index: MEMORY.md (60 lines)

How to parse

For each .md file in MEMORY_DIR (excluding MEMORY.md):

Read frontmatter between --- markers
Extract name, description, type fields
Get file age from modification time: stat -c %Y or date -r
Format age as: Xd (days), Xh (hours), Xm (minutes)

Sort by type, then by age (newest first).

Mode 2: Read
/xray memory read <name>

Find file matching <name> (partial match OK):

ls "$MEMORY_DIR"/*<name>*.md | head -1


Display full content with frontmatter highlighted.

Mode 3: Stats
/xray memory stats
🧠 Memory Stats — [project name]

  Memories:    14 files
  Index:       MEMORY.md (60 lines)
  Total size:  12.4 KB
  Oldest:      9 days (reference_maw_cli.md)
  Newest:      2 days (feedback_never_push_main.md)

  By type:
    feedback   ████████████  5  (36%)
    reference  ████████      3  (21%)
    user       ████          1  (7%)
    project    ░░░░          0  (0%)

  Top keywords: oracle, push, maw, agent, fleet

How to calculate
Count files by type (from frontmatter)
Sum file sizes
Extract keywords: split all description fields into words, count frequency, show top 5
Mode 4: Types
/xray memory types

Group and display memories by type:

🧠 Memory Types

  📝 feedback (5)
    - never_push_main_skills — Always use branch + PR
    - talk_to_not_oracle_thread — Use /talk-to for threads
    - use_workon_skill — Use skill flow, don't edit directly
    - worktree_naming — worktree name = repo name
    - never_maw_done_without_approval — Ask before cleanup

  📚 reference (3)
    - maw_cli — maw hey, peek, ls commands
    - pulse_cli — board, timeline, scan
    - office_hash_routes — all views, deploy flow

  👤 user (1)
    - work_patterns — maker's schedule, peak hours

  📋 project (0)
    (none)

Mode 5: Clean
/xray memory clean

Find potentially stale memories:

Read each memory file
If type: reference and mentions file paths → check if files still exist
If type: project → check if still relevant (age > 30 days = likely stale)
Show candidates:
🧹 Memory Clean — candidates

  ⚠️  reference_office_hash_routes.md (9d)
      Mentions file paths — verify still current

  ✓  All other memories look current

  Run '/xray memory forget <name>' to remove a specific memory.
  Nothing is deleted without your confirmation.


NEVER auto-delete. Only suggest. User decides.

Mode 6: Forget
/xray memory forget <name>
Find the file
Show its content
Ask confirmation: "Remove this memory? (yes/no)"
If yes:
Delete the file
Remove its entry from MEMORY.md
Confirm: "Forgotten: "
If no: "Kept: "
Cross-Project View

If user says /xray memory scan --all or /xray memory stats --all:

ls -d "$HOME/.claude/projects"/*/memory/ 2>/dev/null


Show memory counts per project:

🧠 All Projects

  Project                          Memories  Size
  ──────────────────────────────── ──────── ──────
  neo-oracle                       14        12.4KB
  arra-oracle-skills-cli                 8         6.2KB
  maw-js                            5         3.1KB
  office-8bit                       3         2.0KB

  Total: 30 memories across 4 projects

Target: skills
/xray skills

List all installed Oracle skills with their profiles and status.

arra-oracle-skills list -g


Display:

🔬 Installed Skills

  Skill                Profile     Status
  ──────────────────── ─────────── ──────
  forward              seed        ✓ installed
  retrospective        seed        ✓ installed
  rrr                  seed        ✓ installed
  awaken               standard    ✓ installed
  trace                standard    ✓ installed
  learn                standard    ✓ installed

  Total: N skills installed
  Profile: [seed|standard|full]

How to gather
Run arra-oracle-skills list -g to get installed skills
Cross-reference with profiles from profiles.ts
Show which profile each skill belongs to
Target: sessions
/xray sessions

Show recent Claude Code session history and retrospectives.

Look for retrospectives in ψ/memory/retrospectives/
Look for session logs in ψ/memory/logs/
Display recent sessions with dates and summaries:
📜 Session History

  Date         Duration  Summary
  ──────────── ──────── ────────────────────────────────
  2026-03-25   45min     Built xray skill, updated profiles
  2026-03-24   30min     Fixed awaken language picker
  2026-03-23   1h20min   Refactored profiles system

  Total: N sessions found
  Source: ψ/memory/retrospectives/

How to gather
Read files in ψ/memory/retrospectives/ sorted by date (newest first)
Extract date, duration, and summary from each retrospective
If no retrospectives exist, check ψ/memory/logs/ for session snapshots
Show "No session history found" if both are empty

ARGUMENTS: $ARGUMENTS

Weekly Installs
18
Repository
soul-brews-stud…e-skills
GitHub Stars
49
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykPass