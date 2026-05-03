---
rating: ⭐⭐⭐
title: kitty
url: https://skills.sh/xyenon/agents/kitty
---

# kitty

skills/xyenon/agents/kitty
kitty
Installation
$ npx skills add https://github.com/xyenon/agents --skill kitty
SKILL.md
Kitty Remote Control Skill

This skill empowers you to manage multiple concurrent processes (like servers, watchers, or long builds) using kitty's remote control feature directly from the Bash tool.

Since you are running inside a kitty terminal, you can spawn new windows or tabs to handle these tasks without blocking your main communication channel.

1. Verify Environment & Check Status

First, verify you are running inside kitty with remote control enabled. You can try listing windows:

kitten @ ls


If this fails, check if $KITTY_LISTEN_ON is set. Note that in some configurations it might be empty even if remote control is enabled (using default sockets).

echo $KITTY_LISTEN_ON


If remote control is not enabled, the user should add allow_remote_control yes to their kitty.conf or start kitty with --allow-remote-control.

2. Spawn a Background Process

To run a command (e.g., a dev server) in a way that persists and can be inspected:

Create a new window in the SAME tab as the agent (recommended): Use $KITTY_WINDOW_ID to ensure the new window stays with you.

WID=$(kitten @ launch --match "id:$KITTY_WINDOW_ID" --title "server-log" --keep-focus)
echo "Created window with ID: $WID"


Or create a new tab:

kitten @ launch --type=tab --title "server-log" --keep-focus


Launch with a command directly: (Use --hold if you want the window to stay open after the command finishes)

kitten @ launch --title "server-log" --keep-focus --hold npm start

3. Send Text/Commands to a Window

Send keystrokes to a specific window. Use the window ID for precision, or matching for convenience.

Using ID (Reliable):

kitten @ send-text --match "id:$WID" "npm start\n"


Using Matching (Title):

Note: Use \n for Enter. In some shells, you may need to use $'...' or pipe to ensure the newline is interpreted correctly.

kitten @ send-text --match "title:server-log" "npm start
"
# OR
echo "npm start" | kitten @ send-text --match "title:server-log" --stdin


Or send to all windows:

kitten @ send-text --all "echo hello\n"

4. Inspect Output (Get Text from Window)

Get the current visible text from a window:

kitten @ get-text --match "id:$WID"


Get text including scrollback buffer:

kitten @ get-text --match "title:server-log" --extent=all


Get only the last command output (requires shell integration):

kitten @ get-text --match "title:server-log" --extent=last_cmd_output

5. Focus or Bring Window to Front

Focus a specific window:

kitten @ focus-window --match "id:$WID"


Focus a specific tab:

kitten @ focus-tab --match "title:server-log"

6. Interact with Processes

Send Ctrl+C (Interrupt):

kitten @ send-text --match "id:$WID" "\x03"


Close a window:

kitten @ close-window --match "id:$WID"


Close a tab: (Note: You can close a tab by matching its title or any window ID inside it)

# By ID of a window inside the tab
kitten @ close-tab --match "id:$WID"

# By tab title
kitten @ close-tab --match "title:server-log"

7. Advanced: Window Matching

Kitty supports powerful matching expressions:

title:pattern - Match by window title
id:number - Match by window ID
pid:number - Match by process ID
cwd:path - Match by current working directory
cmdline:pattern - Match by command line
state:focused - Match the focused window
state:active - Match the active window

Combine with and, or, not:

kitten @ focus-window --match "title:server and state:active"

8. Get Window/Tab Information

List all OS windows, tabs, and windows as JSON:

kitten @ ls


Get current focused window ID:

kitten @ ls | jq -r '.[].tabs[] | select(.is_focused) | .windows[] | select(.is_focused) | .id'


Parse for specific info:

kitten @ ls | jq '.[].tabs[].windows[] | {id, title, cmdline}'

Summary of Pattern
WID=$(kitten @ launch --title "NAME" --keep-focus [CMD]) - Create window and save ID
kitten @ send-text --match "id:$WID" "CMD\n" - Send command reliably
kitten @ get-text --match "id:$WID" - Read output
kitten @ close-window --match "id:$WID" - Cleanup
Common Remote Control Commands
Command	Description
kitten @ ls	List all windows/tabs
kitten @ launch	Create new window/tab
kitten @ send-text	Send text to window
kitten @ get-text	Get text from window
kitten @ focus-window	Focus a window
kitten @ focus-tab	Focus a tab
kitten @ close-window	Close a window
kitten @ close-tab	Close a tab
kitten @ signal-child	Send signal to process
kitten @ set-tab-title	Change tab title
kitten @ set-colors	Change terminal colors
Weekly Installs
73
Repository
xyenon/agents
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass