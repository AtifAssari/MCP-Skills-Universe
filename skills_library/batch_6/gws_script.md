---
title: gws-script
url: https://skills.sh/googleworkspace/cli/gws-script
---

# gws-script

skills/googleworkspace/cli/gws-script
gws-script
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-script
SKILL.md
script (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws script <resource> <method> [flags]

Helper Commands
Command	Description
+push	Upload local files to an Apps Script project
API Resources
processes
list — List information about processes made by or on behalf of a user, such as process type and current status.
listScriptProcesses — List information about a script's executed processes, such as process type and current status.
projects
create — Creates a new, empty script project with no script files and a base manifest file.
get — Gets a script project's metadata.
getContent — Gets the content of the script project, including the code source and metadata for each script file.
getMetrics — Get metrics data for scripts, such as number of executions and active users.
updateContent — Updates the content of the specified script project. This content is stored as the HEAD version, and is used when the script is executed as a trigger, in the script editor, in add-on preview mode, or as a web app or Apps Script API in development mode. This clears all the existing files in the project.
deployments — Operations on the 'deployments' resource
versions — Operations on the 'versions' resource
scripts
run —
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws script --help

# Inspect a method's required params, types, and defaults
gws schema script.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
5.9K
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass