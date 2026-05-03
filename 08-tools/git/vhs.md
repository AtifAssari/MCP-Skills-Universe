---
title: vhs
url: https://skills.sh/knoopx/pi/vhs
---

# vhs

skills/knoopx/pi/vhs
vhs
Installation
$ npx skills add https://github.com/knoopx/pi --skill vhs
SKILL.md
VHS

Terminal recorder from Charm that creates GIFs/PNGs from scripted interactions.

Run
nix run nixpkgs#vhs -- <file>.tape

Tape File Syntax
Output output.gif           # or .png, .mp4, .webm

Set Shell "bash"
Set FontSize 14
Set Width 1200
Set Height 600
Set Theme "Catppuccin Mocha"

Hide                        # Hide commands from output
Type "echo hello"
Enter
Sleep 1s
Show                        # Show commands again

Screenshot output.png       # Capture current frame

Commands
Command	Description
Type "text"	Type text
Enter, Tab, Escape, Space	Press key
Ctrl+x, Alt+x	Key combo
Up, Down, Left, Right	Arrow keys
Sleep 1s	Wait (ms, s)
Screenshot file.png	Capture frame
Hide / Show	Toggle visibility
Settings
Setting	Example
Set Shell "bash"	Shell to use
Set FontSize 14	Font size
Set Width 1200	Terminal width
Set Height 600	Terminal height
Set Theme "Catppuccin Mocha"	Color theme
Set Padding 20	Window padding
Set WindowBar Colorful	Window decorations
Example: TUI Screenshot
Output screenshots/demo.png

Set Shell "bash"
Set FontSize 14
Set Width 1400
Set Height 800
Set Theme "Catppuccin Mocha"

Hide
Type "cd /path/to/project && my-tui-app"
Enter
Sleep 2s
Show

Ctrl+p
Sleep 1s
Screenshot screenshots/demo.png

Escape
Type "q"
Enter

List Themes
nix run nixpkgs#vhs -- themes

Weekly Installs
12
Repository
knoopx/pi
GitHub Stars
45
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass