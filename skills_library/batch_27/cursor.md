---
title: cursor
url: https://skills.sh/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations/cursor
---

# cursor

skills/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations/cursor
cursor
Installation
$ npx skills add https://github.com/dicklesworthstone/agent_flywheel_clawdbot_skills_and_integrations --skill cursor
SKILL.md
Cursor Skill

Use the cursor CLI to control the Cursor AI-powered code editor (VS Code fork).

CLI Location
/usr/local/bin/cursor

Opening Files and Folders

Open current directory:

cursor .


Open specific file:

cursor /path/to/file.ts


Open file at specific line:

cursor /path/to/file.ts:42


Open file at line and column:

cursor /path/to/file.ts:42:10


Open folder:

cursor /path/to/project


Open multiple files:

cursor file1.ts file2.ts file3.ts

Window Options

Open in new window:

cursor -n /path/to/project


Open in new window (alias):

cursor --new-window /path/to/project


Reuse existing window:

cursor -r /path/to/file


Reuse existing window (alias):

cursor --reuse-window /path/to/file

Diff Mode

Compare two files:

cursor -d file1.ts file2.ts


Diff (alias):

cursor --diff file1.ts file2.ts

Wait Mode

Wait for file to close (useful in scripts):

cursor --wait /path/to/file


Short form:

cursor -w /path/to/file


Use as git editor:

git config --global core.editor "cursor --wait"

Adding to Workspace

Add folder to current workspace:

cursor --add /path/to/folder

Extensions

List installed extensions:

cursor --list-extensions


Install extension:

cursor --install-extension <extension-id>


Uninstall extension:

cursor --uninstall-extension <extension-id>


Disable all extensions:

cursor --disable-extensions

Verbose and Debugging

Show version:

cursor --version


Show help:

cursor --help


Verbose output:

cursor --verbose /path/to/file


Open developer tools:

cursor --inspect-extensions

Settings

User settings location:

~/Library/Application Support/Cursor/User/settings.json


Keybindings location:

~/Library/Application Support/Cursor/User/keybindings.json

Portable Mode / Profiles

Specify user data directory:

cursor --user-data-dir /path/to/data


Specify extensions directory:

cursor --extensions-dir /path/to/extensions

Piping Input

Read from stdin:

echo "console.log('hello')" | cursor -

Remote Development

Cursor supports remote development similar to VS Code. SSH remotes are configured in:

~/.ssh/config


Then use command palette or remote explorer in the GUI.

Weekly Installs
76
Repository
dicklesworthsto…grations
GitHub Stars
63
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass